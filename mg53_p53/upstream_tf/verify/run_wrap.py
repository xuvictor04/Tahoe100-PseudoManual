import resource, subprocess, sys, time, os
t0 = time.time()
r = subprocess.run(sys.argv[1:])
ru = resource.getrusage(resource.RUSAGE_CHILDREN)
print(f"WRAP exit {r.returncode}; wall {time.time()-t0:.0f} s; peak RSS (largest child) {ru.ru_maxrss/1e6:.2f} GB; user {ru.ru_utime:.0f} s sys {ru.ru_stime:.0f} s", flush=True)
