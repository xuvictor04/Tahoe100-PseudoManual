"""keys - the Anthropic API keys of a review run: where they come from, which one is in use, which are dead, and
what an API error means for the run.

    KeyPool(keys_file=None, env=True, interactive=None, client_factory=None)
        the keys, in this order: --keys-file PATH (one key per line, '#' comments; a warning when the file is readable
        by others), ANTHROPIC_API_KEYS (comma-separated), ANTHROPIC_API_KEY; with none of those, the SDK's default
        credential chain (`anthropic.Anthropic()` resolves ANTHROPIC_AUTH_TOKEN or an `ant auth` profile).
        current() -> Key        the key to start (or restart) an entity with; when every key is dead it asks for a
                                new one with getpass on a terminal ("press Enter to stop"), else (and on Enter) it
                                raises AllKeysDead: the run pauses.
        mark_dead(key, reason)  the key failed for good (401, 402, 403, spend limit, organization on hold)
        client(key)             one SDK client per key (thread-safe; shared by the threads using that key)
    classify(exc) -> (category, info)
        DEAD_KEY: rotate to the next key and restart the entity; WAIT: back off and retry the same request (no
        rotation); ENTITY: the entity fails (recorded; the run moves on). `info` is JSON-ready and scrubbed.
    key_id(secret)              last 4 characters + a short hash: what the ledger, histories and status show
    scrub(text)                 the text with every known key (and anything shaped like one) replaced by its id

Keys live only in memory: never in a file this package writes, never in a log line (every history / ledger line and
every error message goes through scrub()).
"""

import getpass
import hashlib
import os
import re
import stat
import sys
import threading
from dataclasses import dataclass, field

from ..common import log

DEAD_KEY, WAIT, ENTITY = "dead_key", "wait", "entity"
SDK_MAX_RETRIES = 3                  # the SDK's own retries (429, 5xx, connection) before an error reaches us
DEFAULT_ID = "default-credentials"   # the key id of the SDK's default credential chain

_SECRETS = {}                        # secret -> key id, for scrub()
_SECRETS_LOCK = threading.Lock()
_KEY_SHAPE = re.compile(r"sk-ant-[A-Za-z0-9_\-]{6,}")
_BEARER = re.compile(r"(?i)(bearer\s+|x-api-key['\"]?\s*[:=]\s*['\"]?)([A-Za-z0-9_\-\.]{16,})")


class AllKeysDead(Exception):
    """No key works and no new one was given: the run pauses (exit code 3)."""


def key_id(secret):
    if not secret:
        return DEFAULT_ID
    return f"{secret[-4:]}-{hashlib.sha256(secret.encode('utf-8')).hexdigest()[:8]}"


def register_secret(secret):
    if secret:
        with _SECRETS_LOCK:
            _SECRETS[secret] = key_id(secret)


def scrub(text):
    """`text` (anything; str() of it) with every registered key replaced by [key <id>] and anything shaped like an
    Anthropic key or a bearer token replaced by [key]."""
    s = str(text)
    with _SECRETS_LOCK:
        items = sorted(_SECRETS.items(), key=lambda kv: -len(kv[0]))
    for sec, kid in items:
        if sec in s:
            s = s.replace(sec, f"[key {kid}]")
    s = _KEY_SHAPE.sub("[key]", s)
    return _BEARER.sub(lambda m: m.group(1) + "[key]", s)


@dataclass
class Key:
    secret: str = field(repr=False)          # None for the SDK's default credential chain
    key_id: str = ""
    source: str = ""
    dead: bool = False
    reason: str = ""

    def describe(self):
        return {"key_id": self.key_id, "source": self.source, "dead": self.dead, "reason": self.reason}


def _default_factory(secret):
    import anthropic
    if secret:
        return anthropic.Anthropic(api_key=secret, max_retries=SDK_MAX_RETRIES)
    return anthropic.Anthropic(max_retries=SDK_MAX_RETRIES)


def _default_chain_works():
    """True when anthropic.Anthropic() without a key finds credentials (ANTHROPIC_AUTH_TOKEN, an `ant auth` profile)."""
    try:
        import anthropic
        c = anthropic.Anthropic()
    except Exception:  # noqa: BLE001  (CredentialsError, a broken profile file, no SDK ...)
        return False
    return any(getattr(c, a, None) for a in ("api_key", "auth_token", "credentials", "_token_cache"))


def read_keys_file(path):
    """The keys of a keys file (one per line; blank lines and '#' comments ignored). Warns when others can read it."""
    path = os.path.abspath(os.path.expanduser(path))
    if not os.path.exists(path):
        raise FileNotFoundError(f"--keys-file {path} does not exist")
    if os.name == "posix":
        mode = os.stat(path).st_mode
        if mode & (stat.S_IRGRP | stat.S_IROTH):
            log(f"WARNING: the keys file {path} can be read by other users; protect it with: chmod 600 {path}")
    out = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            t = line.split("#", 1)[0].strip()
            if t:
                out.append(t)
    return out


class KeyPool:
    def __init__(self, keys_file=None, env=True, interactive=None, client_factory=None, default_chain=True,
                 prompt=None, on_dead=None):
        self.keys = []
        self._lock = threading.RLock()
        self._clients = {}
        self._factory = client_factory or _default_factory
        self._prompt = prompt or (lambda text: getpass.getpass(text))
        self.interactive = (sys.stdin is not None and sys.stdin.isatty()) if interactive is None else interactive
        self.paused = False
        self.on_dead = on_dead
        if keys_file:
            for k in read_keys_file(keys_file):
                self.add(k, f"keys file {os.path.basename(keys_file)}")
        if env:
            for k in (os.environ.get("ANTHROPIC_API_KEYS") or "").split(","):
                if k.strip():
                    self.add(k.strip(), "ANTHROPIC_API_KEYS")
            if (os.environ.get("ANTHROPIC_API_KEY") or "").strip():
                self.add(os.environ["ANTHROPIC_API_KEY"].strip(), "ANTHROPIC_API_KEY")
        if not self.keys and default_chain and _default_chain_works():
            self.keys.append(Key(secret=None, key_id=DEFAULT_ID, source="the SDK's default credentials"))

    def __len__(self):
        return len(self.keys)

    def add(self, secret, source):
        """Add a key (ignored if already known); returns its Key."""
        secret = secret.strip()
        register_secret(secret)
        with self._lock:
            for k in self.keys:
                if k.secret == secret:
                    return k
            k = Key(secret=secret, key_id=key_id(secret), source=source)
            self.keys.append(k)
            return k

    def live(self):
        with self._lock:
            return [k for k in self.keys if not k.dead]

    def dead_ids(self):
        with self._lock:
            return [k.key_id for k in self.keys if k.dead]

    def describe(self):
        with self._lock:
            return [k.describe() for k in self.keys]

    def current(self):
        """The first live key; with none: ask on a terminal, else raise AllKeysDead (and stay paused)."""
        with self._lock:                     # one thread asks; the others wait here and then get its answer
            for k in self.keys:
                if not k.dead:
                    return k
            if self.paused or not self.interactive:
                self.paused = True
                raise AllKeysDead(self._why())
            log("Every API key is used up or invalid: " + "; ".join(f"{k.key_id} ({k.reason})" for k in self.keys)
                if self.keys else "No Anthropic API key found (--keys-file, ANTHROPIC_API_KEYS, ANTHROPIC_API_KEY).")
            try:
                new = self._prompt("Paste a new Anthropic API key (it is not saved anywhere), or press Enter to "
                                   "stop: ")
            except (EOFError, KeyboardInterrupt, OSError):
                new = ""
            if not (new or "").strip():
                self.paused = True
                raise AllKeysDead(self._why())
            k = self.add(new.strip(), "typed in")
            k.dead, k.reason = False, ""
            log(f"Using the new key {k.key_id}")
            return k

    def _why(self):
        if not self.keys:
            return "no Anthropic API key was found"
        return "every API key failed: " + "; ".join(f"{k.key_id}: {k.reason}" for k in self.keys)

    def mark_dead(self, key, reason):
        with self._lock:
            if key.dead:
                return
            key.dead, key.reason = True, scrub(reason)[:300]
        log(f"API key {key.key_id} stopped working ({key.reason}); switching to the next key")
        if self.on_dead:
            self.on_dead(key)

    def client(self, key):
        with self._lock:
            c = self._clients.get(key.key_id)
            if c is None:
                c = self._factory(key.secret)
                self._clients[key.key_id] = c
            return c


# ----------------------------------------------------------------------------- error classification
def _retry_after(exc):
    resp = getattr(exc, "response", None)
    h = getattr(resp, "headers", None)
    if h is None:
        return None
    for name, scale in (("retry-after-ms", 0.001), ("retry-after", 1.0)):
        v = h.get(name)
        try:
            return max(0.0, float(v) * scale) if v is not None else None
        except (TypeError, ValueError):
            continue
    return None


def classify(exc):
    """(category, info) of an exception raised by a request; see the module docstring. The order matters:
    EnforcedSpendLimitReachedError is a RateLimitError and OrganizationOnHoldError a BadRequestError."""
    import anthropic as AN
    status = getattr(exc, "status_code", None)
    etype = getattr(exc, "type", None)
    info = {"class": type(exc).__name__, "status": status, "type": etype if isinstance(etype, str) else None,
            "error_code": getattr(exc, "error_code", None), "request_id": getattr(exc, "request_id", None),
            "retry_after": _retry_after(exc), "message": scrub(exc)[:2000]}
    spend = getattr(AN, "EnforcedSpendLimitReachedError", ())
    hold = getattr(AN, "OrganizationOnHoldError", ())
    if (spend and isinstance(exc, spend)) or (hold and isinstance(exc, hold)):
        return DEAD_KEY, info
    if isinstance(exc, (AN.AuthenticationError, AN.PermissionDeniedError)):
        return DEAD_KEY, info
    if isinstance(exc, AN.APIStatusError) and (status == 402 or etype == "billing_error"):
        return DEAD_KEY, info
    if isinstance(exc, (AN.RateLimitError, AN.InternalServerError, AN.APIConnectionError)):
        return WAIT, info                  # APITimeoutError is an APIConnectionError; OverloadedError (529) a 5xx
    if isinstance(exc, AN.APIStatusError):
        if (status or 0) >= 500 or status in (408, 409):
            return WAIT, info              # 408 / 409: retried by the SDK too
        return ENTITY, info                # 400 (not billing), 404, 413, 422 ...
    if isinstance(exc, getattr(AN, "CredentialsError", ())) or (
            isinstance(exc, TypeError) and "resolve authentication method" in str(exc)):
        info["class"] = "NoCredentials"
        return DEAD_KEY, info
    return ENTITY, info
