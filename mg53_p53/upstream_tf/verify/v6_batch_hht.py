import numpy as np, pandas as pd
from scipy import stats
FXD="/home/user/tahoe_data/atlas/effects"; T="/home/user/Tahoe100-PseudoManual/mg53_p53/upstream_tf/tables/"
dd=pd.read_csv(FXD+"/drugdose.csv"); keep=~(dd.unreliable_plate_only.astype(bool)|dd.position_not_correctable.astype(bool)).to_numpy()
ddk=dd[keep].reset_index(drop=True)
g=pd.read_csv(FXD+"/genes.csv"); g=g[g.kind=="gene"].reset_index(drop=True); gi={s:i for i,s in enumerate(g.symbol)}
Z=np.nan_to_num(np.load(FXD+"/DD_z.npy",mmap_mode="r")[np.flatnonzero(keep)][:, g.col.to_numpy()]).astype(float)
y=Z[:,gi["TRIM72"]]; act=pd.read_csv(T+"a1_tf_activity_by_drugdose.csv.gz")
rms=np.sqrt((Z**2).mean(1))
cov=np.column_stack([np.log1p(ddk.n_sig_genes.fillna(0)),ddk.cells_log2_vs_plate.fillna(0),ddk.umi_per_cell_log2_vs_plate.fillna(0),ddk.genes_per_cell_log2_vs_plate.fillna(0),ddk.composition_shift_log2.fillna(0),ddk.S_PHASE_z.fillna(0),ddk.G2M_PHASE_z.fillna(0),ddk.PROTEASOME_z.fillna(0),rms])
def pr(x,yv,C,m):
    X=np.column_stack([np.ones(m.sum()),C[m]]); a=x[m]-X@np.linalg.lstsq(X,x[m],rcond=None)[0]; b=yv[m]-X@np.linalg.lstsq(X,yv[m],rcond=None)[0]; return a@b/np.sqrt((a@a)*(b@b))
pl=ddk.plates.astype(str)
hi=pl.apply(lambda s: all(p in ("plate1","plate2","plate3","plate14") for p in s.split(";"))).to_numpy()
lo=pl.apply(lambda s: all(p not in ("plate1","plate2","plate3","plate14") for p in s.split(";"))).to_numpy()
print("drug-doses on high-TRIM72 plates only:", hi.sum(), "low plates only:", lo.sum(), "mixed:", (~hi&~lo).sum(), "example plates field:", pl.iloc[0])
for tf in ["ATF5","ATF4","XBP1","SRF","ELK4","AP1","NFKB","HSF1","TP53"]:
    x=act[tf].to_numpy()
    print(f"{tf}: high plates r {pr(x,y,cov,hi):.3f}  low plates r {pr(x,y,cov,lo):.3f}")
b1=pd.read_csv(T+"b1_line_outcomes.csv")
for oc in ["TRIM72_r2_idarubicin_5","TRIM72_r2_homoharringtonine_5","TRIM72_induction_mean"]:
    m=b1[[oc,"TRIM72_untreated_rel"]].dropna()
    print(oc, "Spearman with untreated level:", round(stats.spearmanr(m[oc], m.TRIM72_untreated_rel).correlation,3), "Pearson R2", round(np.corrcoef(m[oc], m.TRIM72_untreated_rel)[0,1]**2,3), "n", len(m))
h=[c for c in b1.columns if c.startswith("TRIM72_r2_homoharringtonine_5_well_")]
m=b1[h+["TRIM72_untreated_rel"]].dropna(); y_=m.TRIM72_untreated_rel
res=[m[c]-np.polyval(np.polyfit(y_,m[c],1),y_) for c in h]
print("HHT cross-well after untreated adjustment:", round(stats.spearmanr(res[0],res[1]).correlation,3), "raw", round(stats.spearmanr(m[h[0]],m[h[1]]).correlation,3))
