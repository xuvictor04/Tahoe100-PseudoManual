import numpy as np, pandas as pd
rng=np.random.default_rng(3)
dd=pd.read_csv("/home/user/tahoe_data/atlas/effects/drugdose.csv")
keep=~(dd.unreliable_plate_only.astype(bool)|dd.position_not_correctable.astype(bool)).to_numpy()
drug=dd.drug[keep].to_numpy(); n=len(drug); ud=np.unique(drug)
def r_(a,b): a=a-a.mean(); b=b-b.mean(); return a@b/np.sqrt((a@a)*(b@b))
for rho in (0.36, 0.30, 0.20):
    res={k:[] for k in ["top1","top5","top10","drop20drugs"]}
    for s in range(100):
        # drug-clustered bivariate normal: half the variance shared within drug
        gi=pd.factorize(drug)[0]
        def draw():
            return (rng.standard_normal(len(ud))[gi]*np.sqrt(0.5)+rng.standard_normal(n)*np.sqrt(0.5))
        x=draw(); e=draw(); y=rho*x+np.sqrt(1-rho**2)*e
        c=(x-x.mean())/x.std()*(y-y.mean())/y.std()
        for f,k in ((0.01,"top1"),(0.05,"top5"),(0.10,"top10")):
            m=np.ones(n,bool); m[np.argsort(-c)[:int(round(f*n))]]=False; res[k].append(r_(x[m],y[m]))
        lo=np.array([r_(x[drug!=d],y[drug!=d]) for d in ud])
        m=~np.isin(drug, ud[np.argsort(lo)[:20]]); res["drop20drugs"].append(r_(x[m],y[m]))
    print(rho, {k:f"{np.mean(v):.3f} (sd {np.std(v):.3f})" for k,v in res.items()})
