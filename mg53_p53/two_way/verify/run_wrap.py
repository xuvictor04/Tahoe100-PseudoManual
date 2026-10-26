"""Run a command, report wall time and peak RSS of the child (ru_maxrss of children, GB)."""
import resource, subprocess, sys, time
t0 = time.time()
rc = subprocess.call(sys.argv[1:])
ru = resource.getrusage(resource.RUSAGE_CHILDREN)
print(f"[wrap] exit {rc}; wall {time.time() - t0:.0f} s; peak RSS children {ru.ru_maxrss / 1e6:.2f} GB", flush=True)
sys.exit(rc)
