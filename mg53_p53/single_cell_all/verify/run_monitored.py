"""Verifier helper: run a command, poll the PSS / RSS of its whole process tree every 2 s, report wall time and peaks."""
import os, subprocess, sys, time

def tree(pid):
    kids = {}
    for p in os.listdir("/proc"):
        if p.isdigit():
            try:
                with open(f"/proc/{p}/stat") as fh:
                    pp = int(fh.read().rsplit(")", 1)[1].split()[1])
                kids.setdefault(pp, []).append(int(p))
            except Exception:
                pass
    out, st = [], [pid]
    while st:
        x = st.pop(); out.append(x); st.extend(kids.get(x, []))
    return out

def mem(p):
    pss = rss = 0
    try:
        with open(f"/proc/{p}/smaps_rollup") as fh:
            for line in fh:
                if line.startswith("Pss:"): pss = int(line.split()[1])
                elif line.startswith("Rss:"): rss = int(line.split()[1])
    except Exception:
        pass
    return pss, rss

log = open(sys.argv[1], "w")
t0 = time.time()
proc = subprocess.Popen(sys.argv[2:], stdout=log, stderr=subprocess.STDOUT)
peak_pss = peak_rss_main = peak_rss_child = 0
while proc.poll() is None:
    ps = tree(proc.pid)
    m = [mem(p) for p in ps]
    peak_pss = max(peak_pss, sum(x[0] for x in m))
    peak_rss_main = max(peak_rss_main, max([mem(c)[1] for c in ps[1:2]] or [0]))
    peak_rss_child = max(peak_rss_child, max([x[1] for x in m[2:]] or [0]))
    time.sleep(2)
log.flush()
print(f"MONITOR exit {proc.returncode} wall {time.time() - t0:.0f} s peak tree PSS {peak_pss / 1024**2:.2f} GB "
      f"main RSS {peak_rss_main / 1024**2:.2f} GB largest other RSS {peak_rss_child / 1024**2:.2f} GB", file=log, flush=True)
