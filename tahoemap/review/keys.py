"""keys - the Anthropic API keys of a review run: where they come from, which one is in use, which are dead, and
what an API error means for the run.

    KeyPool(keys_file=None, env=True, interactive=None, client_factory=None)
        the keys, in this order: --keys-file PATH (one key per line, '#' comments; UTF-8, with or without a BOM, or
        UTF-16; a warning when the file is readable by others), ANTHROPIC_API_KEYS (comma-separated),
        ANTHROPIC_API_KEY; with none of those, the SDK's default credential chain (`anthropic.Anthropic()`
        resolves ANTHROPIC_AUTH_TOKEN or an `ant auth` profile). A malformed key (a line break, a space or another
        character an HTTP header cannot carry) is dead from the start.
        current() -> Key        the key to start (or restart) an entity with; when every key is dead it asks for a
                                new one with getpass on a terminal ("press Enter to stop"; terminal(): on Windows
                                stdin, stdout and stderr must all be the console), else (and on Enter or
                                Ctrl-C) it raises AllKeysDead: the run pauses. The pool lock is never held while it
                                asks (describe() and the other threads go on); with main_prompts set (the runner's
                                main loop calls serve_prompt()), a worker thread's request is asked by the main
                                thread, where Ctrl-C interrupts getpass and getpass restores the terminal.
        mark_dead(key, reason)  the key failed for good (401, 402, 403, spend limit, organization on hold)
        client(key)             one SDK client per key (thread-safe; shared by the threads using that key)
    classify(exc) -> (category, info)
        DEAD_KEY: rotate to the next key and restart the entity; WAIT: back off and retry the same request (no
        rotation); ENTITY: the entity fails (recorded; the run moves on). `info` is JSON-ready and scrubbed;
        info["network"] is True for timeouts and connection errors (also a stream cut mid-response), which the
        runner retries on a small budget of their own, and info["sent"] says whether the request may have reached
        the API (False only when the connection was never made or the request could not be written on this
        machine), i.e. whether the lost response may be billed.
    refuse_key_value(value, option, expects)    ValueError, not showing the value, when a path option got a key
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

from ..common import log, read_text_file

DEAD_KEY, WAIT, ENTITY = "dead_key", "wait", "entity"
SDK_MAX_RETRIES = 1                  # the SDK's own retries (429, 5xx, connection) before an error reaches us; the
                                     # runner retries after that (waits; a small budget for timeouts / connections)
DEFAULT_ID = "default-credentials"   # the key id of the SDK's default credential chain

_SECRETS = {}                        # secret -> key id, for scrub()
_SECRETS_LOCK = threading.Lock()
_KEY_SHAPE = re.compile(r"sk-ant-[A-Za-z0-9_\-]{6,}")
_KEY_LIKE = re.compile(r"^(sk-ant-\S+|[A-Za-z0-9_\-]{40,})$")     # a bare key, not a path
_BEARER = re.compile(r"(?i)(bearer\s+|x-api-key['\"]?\s*[:=]\s*['\"]?)([A-Za-z0-9_\-\.]{16,})")
_HEADER_SAFE = re.compile(r"^[\x21-\x7e]+$")      # what a key in an HTTP header can be: visible ASCII
MALFORMED = ("the key is malformed: it holds a line break, a space or a character a key cannot have (several keys "
             "in one variable? ANTHROPIC_API_KEYS takes them comma-separated, a keys file one a line)")


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


def refuse_key_value(value, option, expects):
    """Raise ValueError (without showing the value) when the value given for a path option (--keys-file, --fake)
    is not a file and looks like an API key itself: it would end up in messages, tracebacks and logs."""
    raw = str(value).strip()
    base = os.path.basename(raw.rstrip("/\\"))
    if not os.path.isfile(os.path.expanduser(raw)) and (_KEY_SHAPE.search(raw) or _KEY_LIKE.match(base)):
        register_secret(base)
        register_secret(raw)
        raise ValueError(f"{option} expects {expects}; the value given looks like an API key itself (not shown). "
                         "Put the key in a file (chmod 600) or in ANTHROPIC_API_KEY, and clear it from your shell "
                         "history.")


def read_keys_file(path):
    """The keys of a keys file (one per line; blank lines and '#' comments ignored). Warns when others can read it.
    A value that looks like a key itself (not a path) is refused without being shown: it would end up in messages
    and logs."""
    raw = str(path).strip()
    refuse_key_value(raw, "--keys-file", "the path of a FILE with one key a line")
    path = os.path.abspath(os.path.expanduser(raw))
    if not os.path.exists(path):
        raise FileNotFoundError(f"--keys-file {path} does not exist")
    if os.name == "posix":
        mode = os.stat(path).st_mode
        if mode & (stat.S_IRGRP | stat.S_IROTH):
            log(f"WARNING: the keys file {path} can be read by other users; protect it with: chmod 600 {path}")
    out = []
    for line in read_text_file(path).splitlines():          # (UTF-8, UTF-8 with a BOM, or UTF-16: PowerShell 5.1)
        t = line.split("#", 1)[0].replace("\ufeff", "").strip()
        if t:
            out.append(t)
    return out


def _win_console(stream):
    """Windows: stream's handle is a console (GetConsoleMode succeeds). The C runtime's isatty() is also true for
    NUL, and stdin is the console of the window a run was started from even when nobody can answer there."""
    import ctypes
    import msvcrt
    h = msvcrt.get_osfhandle(stream.fileno())
    mode = ctypes.c_uint32()
    return bool(ctypes.windll.kernel32.GetConsoleMode(ctypes.c_void_p(h), ctypes.byref(mode)))


def terminal():
    """Can this run ask for a key (getpass)? POSIX: stdin is a terminal. Windows: stdin, stdout and stderr are all
    the console: a run started with Start-Process and its output redirected to files, or with input from NUL (a
    scheduled task, another program), would wait at a prompt nobody sees - it pauses instead (exit code 3)."""
    if os.name != "nt":
        return sys.stdin is not None and sys.stdin.isatty()
    try:
        return all(s is not None and s.isatty() and _win_console(s) for s in (sys.stdin, sys.stdout, sys.stderr))
    except (AttributeError, OSError, ValueError, ImportError):
        return False


class KeyPool:
    def __init__(self, keys_file=None, env=True, interactive=None, client_factory=None, default_chain=True,
                 prompt=None, on_dead=None):
        self.keys = []
        self._lock = threading.RLock()
        self._clients = {}
        self._factory = client_factory or _default_factory
        self._prompt = prompt or (lambda text: getpass.getpass(text))
        self.interactive = terminal() if interactive is None else interactive
        self.paused = False
        self.on_dead = on_dead
        self._cond = threading.Condition(self._lock)
        self._prompting = None               # the thread asking for a key right now
        self._want_key = False               # a worker waits for the main thread to ask (main_prompts)
        self.main_prompts = False            # set by the runner while its main loop calls serve_prompt()
        self.stopping = lambda: False        # the runner's stop flag: no prompt while the run is stopping
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
        """Add a key (ignored if already known); returns its Key. A malformed key - one an HTTP header cannot carry
        (a line break, a space, a control or non-ASCII character), say two keys in one variable - is dead from the
        start (never sent: the request would fail on this machine, not at the API)."""
        secret = secret.strip()
        register_secret(secret)
        for part in secret.split():
            register_secret(part)
        with self._lock:
            for k in self.keys:
                if k.secret == secret:
                    return k
            k = Key(secret=secret, key_id=key_id(secret), source=source)
            if not _HEADER_SAFE.match(secret):
                k.dead, k.reason = True, MALFORMED
                odd = sorted({f"U+{ord(ch):04X}" for ch in secret if ord(ch) > 0x7e})
                log(f"API key {k.key_id} ({source}) is malformed: {MALFORMED}"
                    + (f" - it holds the invisible or non-ASCII character(s) {', '.join(odd)} (U+FEFF is a byte-order "
                       "mark: save the file as plain UTF-8 or ASCII)" if odd else ""))
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
        """The first live key; with none: ask on a terminal, else raise AllKeysDead (and stay paused). Only one thread
        asks; the others wait for its answer. The pool lock is not held while asking."""
        me = threading.current_thread()
        with self._lock:
            while True:
                for k in self.keys:
                    if not k.dead:
                        return k
                if self.paused or not self.interactive or self.stopping():
                    self.paused = True
                    raise AllKeysDead(self._why())
                if self._prompting is not None or (self.main_prompts and me is not threading.main_thread()):
                    self._want_key = self._want_key or self._prompting is None
                    self._cond.notify_all()
                    self._cond.wait(0.25)            # the main thread (or another one) asks; then look again
                    continue
                self._prompting = me
                break
        self._ask()
        return self.current()

    def serve_prompt(self):
        """Main thread (runner loop): ask for a new key when a worker waits for one. True if it asked."""
        with self._lock:
            if not self._want_key or self._prompting is not None:
                return False
            self._want_key = False
            if self.paused or any(not k.dead for k in self.keys) or self.stopping():
                self._cond.notify_all()           # (the waiting workers look again: a key, or AllKeysDead)
                return False
            self._prompting = threading.current_thread()
        self._ask()
        return True

    def prompting_here(self):
        """True while this thread is asking for a key (the runner's Ctrl-C handler then interrupts getpass)."""
        return self._prompting is threading.current_thread()

    def _ask(self):
        """Ask for a key (getpass) outside the lock; Enter, end of input or Ctrl-C mean: pause."""
        new = ""
        try:
            log("Every API key is used up or invalid: " + "; ".join(f"{k.key_id} ({k.reason})" for k in self.keys)
                if self.keys else "No Anthropic API key found (--keys-file, ANTHROPIC_API_KEYS, ANTHROPIC_API_KEY).")
            new = self._prompt("Paste a new Anthropic API key (it is not saved anywhere), or press Enter to stop: ")
        except (EOFError, KeyboardInterrupt, OSError):
            new = ""                          # (getpass restores the terminal in its own finally)
        finally:
            with self._lock:
                self._prompting = None
                self._want_key = False
                if (new or "").strip():
                    k = self.add(new.strip(), "typed in")
                    if k.reason != MALFORMED:            # (a malformed one stays dead: asked again)
                        k.dead, k.reason = False, ""
                        log(f"Using the new key {k.key_id}")
                else:
                    self.paused = True
                self._cond.notify_all()

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
        if v is None:
            continue
        try:
            return max(0.0, float(v) * scale)
        except (TypeError, ValueError):
            continue                        # (an HTTP date: the exponential backoff decides)
    return None


def _chain(exc):
    seen = []
    while exc is not None and exc not in seen and len(seen) < 8:
        seen.append(exc)
        exc = exc.__cause__ or exc.__context__
    return seen


def _is_transport_error(exc):
    try:
        import httpx2
    except ImportError:
        return False
    return isinstance(exc, httpx2.TransportError)


def _never_connected(exc):
    """True when the request certainly never reached the API: the connection itself failed (refused, timed out,
    no free connection, the proxy refused it), or the request could not even be written on this machine (an illegal
    header value - a malformed key -, a URL or protocol httpx cannot use)."""
    try:
        import httpx2
    except ImportError:
        return False
    local = tuple(c for c in (getattr(httpx2, n, None) for n in (
        "ConnectError", "ConnectTimeout", "PoolTimeout", "ProxyError", "LocalProtocolError", "UnsupportedProtocol",
        "InvalidURL")) if isinstance(c, type))
    return any(isinstance(e, local) for e in _chain(exc))


def classify(exc):
    """(category, info) of an exception raised by a request; see the module docstring. The order matters:
    EnforcedSpendLimitReachedError is a RateLimitError and OrganizationOnHoldError a BadRequestError."""
    import anthropic as AN
    status = getattr(exc, "status_code", None)
    etype = getattr(exc, "type", None)
    am = getattr(exc, "api_message", None)
    info = {"class": type(exc).__name__, "status": status, "type": etype if isinstance(etype, str) else None,
            "error_code": getattr(exc, "error_code", None), "request_id": getattr(exc, "request_id", None),
            "retry_after": _retry_after(exc), "api_message": scrub(am)[:1000] if isinstance(am, str) else None,
            "message": scrub(exc)[:2000]}
    spend = getattr(AN, "EnforcedSpendLimitReachedError", ())
    hold = getattr(AN, "OrganizationOnHoldError", ())
    if (spend and isinstance(exc, spend)) or (hold and isinstance(exc, hold)):
        return DEAD_KEY, info
    if isinstance(exc, (AN.AuthenticationError, AN.PermissionDeniedError)):
        return DEAD_KEY, info
    if isinstance(exc, AN.APIStatusError) and (status == 402 or etype == "billing_error"):
        return DEAD_KEY, info
    if isinstance(exc, AN.APIConnectionError) or _is_transport_error(exc):
        info["network"] = True             # APITimeoutError is an APIConnectionError; a raw httpx2 error: the stream
        info["sent"] = not _never_connected(exc)    # was cut mid-response
        return WAIT, info
    if isinstance(exc, (AN.RateLimitError, AN.InternalServerError)):
        return WAIT, info                  # OverloadedError (529) is a 5xx
    if isinstance(exc, AN.APIStatusError):
        if (status or 0) >= 500 or status in (408, 409):
            return WAIT, info              # 408 / 409: retried by the SDK too
        if status == 200 and etype in ("overloaded_error", "api_error", "rate_limit_error", "timeout_error"):
            return WAIT, info              # an error event in the middle of a stream (HTTP status 200)
        return ENTITY, info                # 400 (not billing), 404, 413, 422 ...
    if isinstance(exc, getattr(AN, "CredentialsError", ())) or (
            isinstance(exc, TypeError) and "resolve authentication method" in str(exc)):
        info["class"] = "NoCredentials"
        return DEAD_KEY, info
    return ENTITY, info
