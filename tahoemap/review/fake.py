"""fake - a scripted stand-in for the Anthropic API (tests, `review run --fake SCRIPT`): no network, no key.

The runner talks to it through the REAL SDK: `FakeAPI.client(secret)` is an `anthropic.Anthropic` whose HTTP
transport is an httpx2.MockTransport answering from the script. So the SDK serialises every request as it would for
the API (and the fake checks it), parses every answer into real BetaMessage objects, and builds every error with its
own factory (anthropic._error_classes.make_status_error) from the HTTP status and error body: the runner's typed
error handling is exercised exactly as against the API. A streamed request ("stream": true, as the runner sends
them: client.beta.messages.stream) is answered with server-sent events (message_start, content_block_start / delta
/ stop per block - text and tool input in pieces, thinking signatures as signature_delta -, message_delta with the
stop reason, stop details and usage, message_stop), which the SDK's stream accumulates into the message.

Script (JSON):
    {
      "keys": ["sk-ant-fake-...", ...],          optional: keys to use when none is configured
      "dead_keys": {"WXYZ": 402},                every call with a key ending in these 4 characters fails so
      "default": [step, ...],                    the steps of an entity without its own list
      "entities": {"gene:56": [step, ...], "Panobinostat": [...]},     by entity_id or name
      "checker": "auto" | [step, ...],           the citation checker: auto = 'supported' for every claim id
      "literature": "stub" | "live"              stub (default): PubMed / Europe PMC / Crossref answered locally
    }
A step is consumed per request of that entity's conversation (reviewer and checker separately); a restarted entity
(new attempt) continues with the next step. Steps:
    {"tool_use": [{"name": "pubmed_search", "input": {...}}, ...]}           stop_reason tool_use
    {"submit_review": {payload}}                                             tool_use of submit_review
    {"submit_check": {payload}}                                              tool_use of submit_check
    {"web_search": "query"}  (+ "pause": true: stop with pause_turn before the result; with "tool_use" /
                             "submit_review" in the same step: a finished search, then those calls)
    {"end_turn": "text"}                                                     text only, end_turn
    {"submit_check": "auto"}                                                 the auto check (every claim supported)
    {"refusal": "bio"}                                                       stop_reason refusal + stop_details
            (+ "recommended_model": "claude-opus-4-8": the fallback model was busy - a transient refusal)
    {"max_tokens": true}  (+ "partial_tool": "submit_review": a cut-off tool_use block)
    {"empty": true}                                                          no content blocks at all, end_turn
    {"error": 402 | 401 | 403 | 429 | 529 | 500 | 400 | 404 | 413 | "billing" | "spend_limit" | "on_hold" |
              "connection" | "timeout"}                                     the SDK raises its typed error
modifiers on any step: "text": "...", "usage": {...} (overrides), "fallback": "claude-opus-5" (a fallback block and
a fallback_message usage iteration at that model), "signal": "SIGINT" (sent to this process before answering),
"sleep": seconds (before the signal), "sleep_after": seconds (after it: the answer comes late), "drop": true (a
streamed answer breaks off with a network error after its first block: a lost response), "drop": "clean" (it just
ends there, without message_stop), "drop": "overloaded" (an overloaded_error event in the middle of the stream) or
"drop": "empty" (the stream closes before message_start).
Usage is made up from the request size (4 characters a token; the previous context read from cache).

Every request is checked like the API would: first message from the user, every tool_use answered by a tool_result
in the next user message (except a trailing server_tool_use after pause_turn), assistant turns echoed unchanged,
no forced tool_choice / thinking budget / sampling parameters, the fallback beta header, cache_control on the system
prompt and top level, strict custom tools. A violation is answered with HTTP 400 and listed in FakeAPI.violations.

FakeLiterature: a tiny local PubMed / Europe PMC / Crossref (install() patches tools.http_get).
sdk_error(what): the SDK's own exception for an HTTP status / named error, built the way the SDK builds it
(anthropic._error_classes.make_status_error on an httpx2.Response with its request), for tests of keys.classify.
FakeAPI.calls: one record per request (entity, role, key's last 4 characters, number of messages and the
messages_sha256 of what was sent, step, thread, start/end times, whether it was streamed, max_tokens).
FakeAPI.violations: what the API would have rejected (the runner logs them at the end of a fake run).
"""

import json
import os
import re
import signal
import threading
import time
import urllib.parse

FAKE_BASE_URL = "http://fake-anthropic.invalid"
FALLBACK_BETA = "server-side-fallback-2026-07-01"
DEFAULT_KEYS = ["sk-ant-fake-0000000000000000-KEY1", "sk-ant-fake-0000000000000000-KEY2"]

ERRORS = {
    400: ("invalid_request_error", "messages: something is wrong with this request (fake)"),
    401: ("authentication_error", "invalid x-api-key"),
    402: ("billing_error", "Your credit balance is too low to access the Anthropic API. Please go to Plans & "
                           "Billing to upgrade or purchase credits."),
    403: ("permission_error", "Your API key does not have permission to use the specified resource."),
    404: ("not_found_error", "model: not found (fake)"),
    413: ("request_too_large", "Request exceeds the maximum allowed number of bytes."),
    429: ("rate_limit_error", "Number of request tokens has exceeded your per-minute rate limit (fake)"),
    500: ("api_error", "Internal server error (fake)"),
    529: ("overloaded_error", "Overloaded"),
}
NAMED = {"billing": (402, None), "auth": (401, None), "permission": (403, None), "rate_limit": (429, None),
         "overloaded": (529, None), "server": (500, None), "bad_request": (400, None),
         "spend_limit": (429, "enforced_spend_limit_reached"), "on_hold": (400, "organization_on_hold")}
_ENTITY_RE = re.compile(r'<dossier entity_id="([^"]+)"')
_CHECK_RE = re.compile(r"literature review of (.+?) \(Tahoe-100M gene map\)")
_CLAIM_RE = re.compile(r"^\[([EMCV]\d+)\]", re.M)


def load(path):
    with open(path, encoding="utf-8") as fh:
        return FakeAPI(json.load(fh))


def _text_of_content(c):
    if isinstance(c, str):
        return c
    out = []
    for b in c or []:
        if isinstance(b, dict) and b.get("type") == "text":
            out.append(b.get("text", ""))
    return "\n".join(out)


class FakeAPI:
    def __init__(self, script):
        self.script = script or {}
        self.lock = threading.Lock()
        self.cursor = {}                 # conversation key -> next step index
        self.returned = {}               # conversation key -> the assistant contents returned so far
        self.calls = []                  # one dict per request (entity, role, key, n_messages, step)
        self.violations = []
        self.n = 0
        self._ctx_tokens = {}            # conversation key -> tokens of its context after the last response
        self.literature = None
        if self.script.get("literature", "stub") != "live":
            self.literature = FakeLiterature()

    # ------------------------------------------------------------------ the client factory (keys.KeyPool)
    def client(self, secret):
        import anthropic
        import httpx2
        transport = httpx2.MockTransport(lambda req: self.handle(req, secret or "sk-ant-fake-default-chain"))
        return anthropic.Anthropic(api_key=secret or "sk-ant-fake-default-chain", base_url=FAKE_BASE_URL,
                                   http_client=anthropic.DefaultHttpxClient(transport=transport), max_retries=0)

    def keys(self):
        return list(self.script.get("keys") or DEFAULT_KEYS)

    # ------------------------------------------------------------------ requests
    def _conversation(self, body):
        msgs = body.get("messages") or []
        tools = [t.get("name") for t in body.get("tools") or []]
        role = "checker" if "submit_check" in tools else "reviewer"
        first = _text_of_content(msgs[0].get("content")) if msgs else ""
        if role == "reviewer":
            m = _ENTITY_RE.search(first)
            ent = m.group(1) if m else "?"
        else:
            m = _CHECK_RE.search(first)
            ent = m.group(1) if m else "?"
        return ent, role, first

    def _steps(self, ent, role):
        if role == "checker":
            ck = self.script.get("checker", "auto")
            if isinstance(ck, dict):
                ck = ck.get(ent, ck.get("*", "auto"))
            return ck
        ents = self.script.get("entities") or {}
        if ent in ents:
            return ents[ent]
        name = ent.split(":", 1)[1] if ":" in ent else ent
        if name in ents:
            return ents[name]
        return self.script.get("default") or []

    def handle(self, req, secret):
        body = json.loads(req.content.decode("utf-8"))
        ent, role, first = self._conversation(body)
        key = f"{ent}|{role}"
        with self.lock:
            self.n += 1
            n = self.n
            problems = self._validate(req, body, key)
            dead = (self.script.get("dead_keys") or {}).get(secret[-4:])
            if dead is None and not problems:
                steps = self._steps(ent, role)
                if steps == "auto" or steps is None:
                    step = {"submit_check": self._auto_check(first)} if role == "checker" else \
                        {"end_turn": "(no script for this entity)"}
                else:
                    i = self.cursor.get(key, 0)
                    step = steps[i] if i < len(steps) else {"end_turn": "(script exhausted)"}
                    self.cursor[key] = i + 1
            else:
                step = {"error": dead} if dead is not None else {"error": 400, "message": "; ".join(problems)}
            self.calls.append({"n": n, "entity": ent, "role": role, "key": secret[-4:],
                               "n_messages": len(body.get("messages") or []), "step": _step_name(step),
                               "stream": bool(body.get("stream")), "max_tokens": body.get("max_tokens"),
                               "thread": threading.current_thread().name, "t0": time.monotonic(),
                               "messages_sha256": messages_sha256(body.get("messages") or [])})
        try:
            return self._answer(req, body, step, n, key)
        finally:
            with self.lock:
                self.calls[n - 1]["t1"] = time.monotonic()

    def _answer(self, req, body, step, n, key):
        import httpx2
        if step.get("sleep"):
            time.sleep(float(step["sleep"]))
        if step.get("signal"):
            os.kill(os.getpid(), getattr(signal, step["signal"]))
            time.sleep(0.2)                          # let the main thread run its handler
        if step.get("sleep_after"):
            time.sleep(float(step["sleep_after"]))
        if "error" in step:
            return self._error(req, step)
        with self.lock:
            msg = self._message(body, step, n)
            if not step.get("drop") and msg["content"]:      # (an empty turn is never sent back)
                self.returned.setdefault(key, []).append(msg["content"])
        if body.get("stream"):
            return httpx2.Response(200, content=sse_stream(msg, drop=step.get("drop")),
                                   headers={"content-type": "text/event-stream", "request-id": f"req_fake_{n}"})
        return httpx2.Response(200, json=msg, headers={"request-id": f"req_fake_{n}"})

    def _validate(self, req, body, key):
        """Problems the API would answer with a 400 (and conversation-integrity problems)."""
        P = []
        msgs = body.get("messages") or []
        if not msgs or msgs[0].get("role") != "user":
            P.append("messages: the first message must be from the user")
        if len(msgs) == 1:
            self.returned[key] = []                  # a new conversation (or an entity restarted)
        for k in ("temperature", "top_p", "top_k"):
            if k in body:
                P.append(f"{k}: not supported on this model")
        tc = (body.get("tool_choice") or {}).get("type")
        if tc in ("any", "tool"):
            P.append('tool_choice: type "tool" and "any" are not supported for this model.')
        th = body.get("thinking") or {}
        if th.get("type") in ("disabled", "enabled"):
            P.append(f'"thinking.type.{th["type"]}" is not supported for this model.')
        if "max_tokens" not in body or "model" not in body:
            P.append("max_tokens and model are required")
        if body.get("fallbacks") == "default" and FALLBACK_BETA not in (req.headers.get("anthropic-beta") or ""):
            P.append("fallbacks: needs the anthropic-beta header " + FALLBACK_BETA)
        sysb = body.get("system")
        if not (isinstance(sysb, list) and sysb and sysb[-1].get("cache_control")):
            P.append("system: expected text blocks with cache_control on the last one")
        if not body.get("cache_control"):
            P.append("top-level cache_control (automatic caching) missing")
        for t in body.get("tools") or []:
            if "input_schema" in t and not t.get("strict"):
                P.append(f"tools: custom tool {t.get('name')} is not strict")
            if "type" in t and t["type"] not in ("web_search_20260209", "web_fetch_20260209"):
                P.append(f"tools: unexpected server tool {t['type']}")
        # every tool_use answered in the next user message; assistant turns echoed unchanged
        returned = self.returned.get(key, [])
        ai = 0
        for i, m in enumerate(msgs):
            if m.get("role") != "assistant":
                continue
            content = m.get("content")
            if ai < len(returned) and content != returned[ai]:
                P.append(f"messages.{i}: the assistant turn differs from the response it came from")
            ai += 1
            uses = [b.get("id") for b in content or [] if isinstance(b, dict) and b.get("type") == "tool_use"]
            if not uses:
                continue                             # (consecutive assistant turns are allowed: pause_turn)
            if i + 1 < len(msgs):
                nxt = msgs[i + 1]
                got = [b.get("tool_use_id") for b in nxt.get("content") or [] if isinstance(b, dict)
                       and b.get("type") == "tool_result"] if isinstance(nxt.get("content"), list) else []
                if nxt.get("role") != "user" or any(u not in got for u in uses):
                    P.append(f"messages.{i + 1}: tool_use ids {uses} need tool_result blocks in the next user "
                             "message")
            elif uses:
                P.append(f"messages.{i}: the last assistant message has tool_use blocks without results")
        if msgs and msgs[-1].get("role") == "assistant":
            last = msgs[-1].get("content") or []
            if not (last and isinstance(last[-1], dict) and last[-1].get("type") == "server_tool_use"):
                P.append("messages: ends with an assistant turn that is not a paused server-tool turn")
        if P:
            self.violations.extend(P)
        return P

    def _auto_check(self, prompt):
        ids = _CLAIM_RE.findall(prompt)
        return {"verdicts": [{"claim_id": c, "verdict": "supported", "reason": "fake check: the abstract says so",
                              "direction": {"M": "not applicable", "C": "opposite to the data"}.get(
                                  c[0], "same as the data")}
                             for c in ids], "summary": f"fake check of {len(ids)} claims"}

    def _error(self, req, step):
        import httpx2
        e = step["error"]
        if e == "connection":
            raise httpx2.ConnectError("fake: connection reset by peer", request=req)
        if e == "timeout":
            raise httpx2.ReadTimeout("fake: read timed out", request=req)
        code = None
        if isinstance(e, str) and e in NAMED:
            status, code = NAMED[e]
        else:
            status = int(e)
        etype, msg = ERRORS.get(status, ("api_error", "error (fake)"))
        err = {"type": etype, "message": step.get("message") or msg}
        if code:
            err["details"] = {"error_code": code}
        headers = {"request-id": "req_fake_error"}
        if status == 429:
            headers["retry-after"] = str(step.get("retry_after", 1))
        return httpx2.Response(status, json={"type": "error", "error": err, "request_id": "req_fake_error"},
                               headers=headers)

    def _usage(self, body, content, step, key):
        size = len(json.dumps(body.get("system"))) + len(json.dumps(body.get("tools"))) + \
            len(json.dumps(body.get("messages")))
        total = max(1, size // 4)
        prev = self._ctx_tokens.get(key, 0) if len(body.get("messages") or []) > 1 else 0
        prev = min(prev, total)
        out = max(1, len(json.dumps(content)) // 4) + 300
        u = {"input_tokens": 5, "cache_creation_input_tokens": max(0, total - prev - 5),
             "cache_read_input_tokens": prev, "output_tokens": out,
             "server_tool_use": {"web_search_requests": 1 if step.get("web_search") is not None else 0,
                                 "web_fetch_requests": 0}}
        u.update(step.get("usage") or {})
        self._ctx_tokens[key] = total + out
        return u

    def _message(self, body, step, n):
        model = body.get("model")
        ent, role, _first = self._conversation(body)
        key = f"{ent}|{role}"
        content = [{"type": "thinking", "thinking": "", "signature": f"fake-signature-{n}"}]
        if step.get("fallback"):
            content.append({"type": "fallback", "from": {"model": model}, "to": {"model": step["fallback"]},
                            "trigger": {"type": "refusal", "category": "cyber"}})
        if step.get("text"):
            content.append({"type": "text", "text": step["text"]})
        stop, details = "end_turn", None
        if "web_search" in step and ("tool_use" in step or "submit_review" in step or "submit_check" in step):
            sid = f"srvtoolu_fake_{n}"                 # a finished web search, then the custom tool call(s)
            content.append({"type": "server_tool_use", "id": sid, "name": "web_search",
                            "input": {"query": step["web_search"]}})
            content.append({"type": "web_search_tool_result", "tool_use_id": sid, "content": [
                {"type": "web_search_result", "url": "https://example.org/fake", "title": "A fake page",
                 "encrypted_content": "ZmFrZQ==", "page_age": None}]})
        if "tool_use" in step:
            for i, t in enumerate(step["tool_use"]):
                content.append({"type": "tool_use", "id": f"toolu_fake_{n}_{i}", "name": t["name"],
                                "input": t.get("input") or {}})
            stop = "tool_use"
        elif "submit_review" in step or "submit_check" in step:
            name = "submit_review" if "submit_review" in step else "submit_check"
            payload = step[name]
            if payload == "auto":
                payload = self._auto_check(_first)
            content.append({"type": "tool_use", "id": f"toolu_fake_{n}_0", "name": name, "input": payload})
            stop = "tool_use"
        elif "web_search" in step:
            sid = f"srvtoolu_fake_{n}"
            content.append({"type": "server_tool_use", "id": sid, "name": "web_search",
                            "input": {"query": step["web_search"]}})
            if step.get("pause"):
                stop = "pause_turn"
            else:
                content.append({"type": "web_search_tool_result", "tool_use_id": sid, "content": [
                    {"type": "web_search_result", "url": "https://example.org/fake", "title": "A fake page",
                     "encrypted_content": "ZmFrZQ==", "page_age": None}]})
                content.append({"type": "text", "text": "The web search found a page (fake)."})
        elif "refusal" in step:
            stop = "refusal"
            details = {"type": "refusal", "category": step["refusal"], "explanation": "declined (fake)"}
            if step.get("recommended_model"):
                details["recommended_model"] = step["recommended_model"]
        elif step.get("empty"):
            content = []
        elif "max_tokens" in step:
            content.append({"type": "text", "text": "This answer is cut off mid-"})
            if step.get("partial_tool"):
                content.append({"type": "tool_use", "id": f"toolu_fake_{n}_cut", "name": step["partial_tool"],
                                "input": {}})
            stop = "max_tokens"
        else:
            content.append({"type": "text", "text": step.get("end_turn") or "Done."})
        usage = self._usage(body, content, step, key)
        if step.get("fallback"):
            fb = dict(usage)
            fb.pop("server_tool_use", None)
            first = {"type": "message", "model": model, "input_tokens": 5, "output_tokens": 20,
                     "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0}
            last = {"type": "fallback_message", "model": step["fallback"], "input_tokens": fb["input_tokens"],
                    "output_tokens": fb["output_tokens"],
                    "cache_creation_input_tokens": fb["cache_creation_input_tokens"],
                    "cache_read_input_tokens": fb["cache_read_input_tokens"]}
            usage["iterations"] = [first, last]
            model = step["fallback"]
        return {"id": f"msg_fake_{n}", "type": "message", "role": "assistant", "model": model, "content": content,
                "stop_reason": stop, "stop_sequence": None, "stop_details": details, "usage": usage}


def _chunks(text, n=3):
    k = max(1, -(-len(text) // n))
    return [text[i:i + k] for i in range(0, len(text), k)] or [""]


def sse_events(msg):
    """The server-sent events of a streamed answer that accumulates to `msg` (as the API streams a message)."""
    u = msg["usage"]
    start = dict(msg, content=[], stop_reason=None, stop_sequence=None, stop_details=None,
                 usage={k: u.get(k) for k in ("input_tokens", "cache_creation_input_tokens",
                                              "cache_read_input_tokens")} | {"output_tokens": 1})
    yield "message_start", {"type": "message_start", "message": start}
    for i, b in enumerate(msg["content"]):
        t = b.get("type")
        if t == "text":
            yield "content_block_start", {"type": "content_block_start", "index": i,
                                          "content_block": {"type": "text", "text": ""}}
            for c in _chunks(b.get("text", "")):
                yield "content_block_delta", {"type": "content_block_delta", "index": i,
                                              "delta": {"type": "text_delta", "text": c}}
        elif t == "thinking":
            yield "content_block_start", {"type": "content_block_start", "index": i,
                                          "content_block": {"type": "thinking", "thinking": "", "signature": ""}}
            if b.get("thinking"):
                yield "content_block_delta", {"type": "content_block_delta", "index": i,
                                              "delta": {"type": "thinking_delta", "thinking": b["thinking"]}}
            yield "content_block_delta", {"type": "content_block_delta", "index": i,
                                          "delta": {"type": "signature_delta", "signature": b.get("signature", "")}}
        elif t in ("tool_use", "server_tool_use"):
            yield "content_block_start", {"type": "content_block_start", "index": i,
                                          "content_block": dict(b, input={})}
            for c in _chunks(json.dumps(b.get("input") or {})):
                yield "content_block_delta", {"type": "content_block_delta", "index": i,
                                              "delta": {"type": "input_json_delta", "partial_json": c}}
        else:                                        # web_search_tool_result, fallback ...: whole at the start
            yield "content_block_start", {"type": "content_block_start", "index": i, "content_block": b}
        yield "content_block_stop", {"type": "content_block_stop", "index": i}
    yield "message_delta", {"type": "message_delta",
                            "delta": {"stop_reason": msg["stop_reason"], "stop_sequence": None,
                                      "stop_details": msg.get("stop_details")}, "usage": u}
    yield "message_stop", {"type": "message_stop"}


def sse_stream(msg, drop=None):
    """The bytes of sse_events(msg); with drop, the stream breaks off after the first content block (True: with a
    network error, 'clean': it just ends, 'overloaded': with an error event; 'empty': nothing after a ping)."""
    import httpx2
    blocks = 0
    yield b"event: ping\ndata: {\"type\": \"ping\"}\n\n"
    if drop == "empty":                              # the connection closes before message_start
        return
    for name, data in sse_events(msg):
        yield f"event: {name}\ndata: {json.dumps(data)}\n\n".encode("utf-8")
        if name == "content_block_stop":
            blocks += 1
        if drop and (blocks >= 1 or name == "message_delta"):
            if drop == "clean":
                return
            if drop == "overloaded":                 # an error event in the middle of the stream (HTTP 200)
                err = {"type": "error", "error": {"type": "overloaded_error", "message": "Overloaded (fake)"}}
                yield f"event: error\ndata: {json.dumps(err)}\n\n".encode("utf-8")
                return
            raise httpx2.ReadError("fake: connection reset by peer in the middle of the response")


def messages_sha256(messages):
    """sha256 of a messages list as canonical JSON (compare what was sent with what a history file holds)."""
    import hashlib
    return hashlib.sha256(json.dumps(messages, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()


def sdk_error(what, message=None, retry_after=None):
    """The exception the SDK raises for `what` (an HTTP status such as 402 / 429 / 529, a name of NAMED, or
    "connection" / "timeout"), built by the SDK's own factory from an HTTP response, as for a real API answer."""
    import anthropic
    import httpx2
    from anthropic._error_classes import make_status_error
    req = httpx2.Request("POST", FAKE_BASE_URL + "/v1/messages")
    if what == "connection":
        return anthropic.APIConnectionError(message=message or "Connection error.", request=req)
    if what == "timeout":
        return anthropic.APITimeoutError(request=req)
    code = None
    if isinstance(what, str) and what in NAMED:
        status, code = NAMED[what]
    else:
        status = int(what)
    etype, msg = ERRORS.get(status, ("api_error", "error (fake)"))
    err = {"type": etype, "message": message or msg}
    if code:
        err["details"] = {"error_code": code}
    body = {"type": "error", "error": err, "request_id": "req_fake_error"}
    headers = {"request-id": "req_fake_error"}
    if retry_after is not None:
        headers["retry-after"] = str(retry_after)
    resp = httpx2.Response(status, json=body, headers=headers, request=req)
    return make_status_error(f"Error code: {status} - {body}", body=body, response=resp)


def _step_name(step):
    for k in ("error", "tool_use", "submit_review", "submit_check", "web_search", "refusal", "max_tokens",
              "empty", "end_turn"):
        if k in step:
            if k == "tool_use":
                return "tool_use:" + ",".join(t["name"] for t in step["tool_use"])
            if k == "error":
                return f"error:{step['error']}"
            return k
    return "?"


# ----------------------------------------------------------------------------- a local literature service
class FakeLiterature:
    """PubMed / Europe PMC / Crossref answered from a small in-memory library (install() / uninstall())."""

    def __init__(self, papers=None):
        self.papers = papers or {
            str(p): {"title": f"Fake paper {p} on gene co-regulation", "journal": "J Fake Biol", "year": "2020",
                     "abstract": f"Fake abstract {p}: the two genes are co-regulated by NRF2 in cancer cells.",
                     "doi": f"10.1000/fake.{p}", "retracted": p == 31000005}
            for p in range(31000001, 31000011)}
        self.requests = []
        self._orig = None

    def install(self):
        from . import tools as TL
        if self._orig is None:
            self._orig = TL.http_get
            TL.http_get = self.http_get
        return self

    def uninstall(self):
        from . import tools as TL
        if self._orig is not None:
            TL.http_get = self._orig
            self._orig = None

    def http_get(self, ctx, service, url, params, max_age_days=None, cache=True):
        from . import tools as TL
        self.requests.append((service, url, dict(params)))
        if url == TL.ESEARCH:
            ids = list(self.papers)[:int(params.get("retmax", 20))]
            return json.dumps({"esearchresult": {"count": str(len(ids)), "idlist": ids,
                                                 "querytranslation": params.get("term", "")}})
        if url == TL.ESUMMARY:
            res = {"uids": []}
            for p in str(params.get("id", "")).split(","):
                r = self.papers.get(p)
                if r is None:
                    res[p] = {"uid": p, "error": "cannot get document summary"}
                    continue
                res["uids"].append(p)
                res[p] = {"uid": p, "pubdate": r["year"], "source": r["journal"], "title": r["title"],
                          "authors": [{"name": "Doe J", "authtype": "Author"}],
                          "pubtype": ["Journal Article"] + (["Retracted Publication"] if r["retracted"] else []),
                          "articleids": [{"idtype": "doi", "value": r["doi"]}], "attributes": ["Has Abstract"]}
            return json.dumps({"result": res})
        if url == TL.EFETCH:
            arts = []
            for p in str(params.get("id", "")).split(","):
                r = self.papers.get(p)
                if r is None:
                    continue
                pt = "<PublicationType>Journal Article</PublicationType>" + (
                    "<PublicationType>Retracted Publication</PublicationType>" if r["retracted"] else "")
                arts.append(f"<PubmedArticle><MedlineCitation><PMID>{p}</PMID><Article><Journal><Title>{r['journal']}"
                            f"</Title><JournalIssue><PubDate><Year>{r['year']}</Year></PubDate></JournalIssue>"
                            f"</Journal><ArticleTitle>{r['title']}</ArticleTitle><Abstract><AbstractText>"
                            f"{r['abstract']}</AbstractText></Abstract><AuthorList><Author><LastName>Doe</LastName>"
                            f"<Initials>J</Initials></Author></AuthorList><PublicationTypeList>{pt}"
                            f"</PublicationTypeList><ELocationID EIdType=\"doi\">{r['doi']}</ELocationID></Article>"
                            "</MedlineCitation></PubmedArticle>")
            return "<PubmedArticleSet>" + "".join(arts) + "</PubmedArticleSet>"
        if url == TL.EUROPEPMC:
            q = params.get("query", "")
            hits = []
            for p, r in self.papers.items():
                if "DOI:" in q and r["doi"] not in q:
                    continue
                hits.append({"pmid": p, "doi": r["doi"], "pubYear": r["year"], "title": r["title"],
                             "journalTitle": r["journal"], "source": "MED", "pubType": "research-article",
                             "authorString": "Doe J", "abstractText": r["abstract"]})
            hits = hits[:int(params.get("pageSize", 20))]
            return json.dumps({"hitCount": len(hits), "resultList": {"result": hits}})
        if url.startswith(TL.CROSSREF):
            doi = urllib.parse.unquote(url[len(TL.CROSSREF):])
            if any(r["doi"] == doi for r in self.papers.values()):
                return json.dumps({"status": "ok", "message": {"DOI": doi}})
            raise TL.NotFoundError(f"crossref: not found ({doi})")
        raise TL.ToolError(f"fake literature: no answer for {service} {url}")


def sample_review(partner="NQO1", pmids=("31000001",), note=None):
    """A valid submit_review payload citing these PMIDs (tests)."""
    cits = [f"PMID:{p}" for p in pmids]
    links = " ".join(f"[PMID:{p}](https://pubmed.ncbi.nlm.nih.gov/{p}/)" for p in pmids)
    return {
        "summary": f"The data agree with the literature on {partner} (fake review).",
        "established": [{"partner_or_topic": partner, "relation": "co-regulated by NRF2",
                         "data_evidence": "cos 0.71, both halves, fdr 0.001", "citations": cits,
                         "confidence": "high"}],
        "unexpected": [{"observation": "moves opposite to GENE_X", "data_evidence": "cos -0.52",
                        "why_unexpected": "no shared pathway", "literature_checked": ["GENE_X AND " + partner],
                        "confidence": "low"}],
        "missing": [{"expected_connection": f"{partner} with KEAP1", "source": "STRING",
                     "data_status": "cos 0.05, not among the 100 partners", "likely_reason": "regulated post-"
                     "translationally", "citations": cits[:1]}],
        "contradicted": [],
        "connection_verdicts": [{"partner": partner, "verdict": "established", "relation": "both NRF2 targets, "
                                 "co-induced by electrophiles", "data_evidence": "moves with: cos 0.71, both halves",
                                 "citations": cits},
                                {"partner": "GENE_X", "verdict": "unexpected", "relation": "no paper found",
                                 "data_evidence": "moves opposite: cos -0.52", "citations": []}],
        "open_questions": ["Why does GENE_X move opposite?"],
        "note_markdown": note or f"## What the literature says\n\n{partner} is a known partner {links}.\n",
    }
