import os, sys, glob
sys.argv = ["x"]
sys.path.insert(0, "/home/user/Tahoe100-PseudoManual/mg53_p53/upstream_tf")
import numpy as np, pandas as pd
import upstream_tf as U
U.UC.DATA = "/home/user/tahoe_data"
ctx = U.Ctx("/home/user/tahoe_data")
lam = sorted(glob.glob("/home/user/Tahoe100-PseudoManual/**/lambert_DatabaseExtract_v_1.01.csv", recursive=True))
ext = os.path.dirname(lam[0]) if lam else "/nonexistent"
print("lambert file:", lam[:1])
reg = U.lambert_fallback(ext, True, set(ctx.gsym))
print("fallback regulon rows:", len(reg))
excl = np.zeros(ctx.ng, bool); excl[ctx.j_trim] = True
W, tfs, n = U.regulon_matrix(reg, ctx, excl)
print("TFs passing TMIN in the fallback:", len(tfs))
ctrl = reg[(reg["tf"] == "TP53") & ~reg["target"].isin(U.P53_CTRL)].assign(tf=U.TP53_CTRL_TF)
Wc, tfc, _ = U.regulon_matrix(ctrl, ctx, excl)
print("TP53 control regulons in the fallback:", tfc, "-> main() later calls tfs_p.index(TP53_CTRL_TF): would raise ValueError" if not tfc else "")
