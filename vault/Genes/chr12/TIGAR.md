---
symbol: "TIGAR"
type: "gene"
col: 1214
ensembl_id: "ENSG00000078237"
name: "TP53 induced glycolysis regulatory phosphatase"
location: "12p13.32"
module: 62
arm: "+"
pooled_cpm: 36.65
n_lines_expressing: 49
n_dd_up: 37
n_dd_down: 14
n_dd_up_clean: 20
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# TIGAR

*TP53 induced glycolysis regulatory phosphatase* — 12p13.32

> [!summary] In one line
> TIGAR encodes a p53-inducible phosphatase that lowers fructose-2,6-bisphosphate, slowing glycolysis and diverting glucose into the pentose phosphate pathway — making it a p53 target that protects cells rather than killing them.

## What it is

The name is the mechanism as proposed: TP53-induced glycolysis and apoptosis regulator. Formerly C12orf5, it was found as a p53-inducible transcript resembling the bisphosphatase half of the bifunctional 6-phosphofructo-2-kinase/fructose-2,6-bisphosphatase enzymes — only that half: histidine-phosphatase fold and catalytic histidine, no kinase domain.

Fructose-2,6-bisphosphate is the allosteric activator of phosphofructokinase-1, the committed step of glycolysis; hydrolysing it inhibits PFK-1, backs glucose-6-phosphate up into the oxidative pentose phosphate pathway and raises NADPH and so reduced glutathione. Lower ROS follows, and apoptosis resistance. This is p53's cytoprotective arm at its clearest: the factor that induces [[BAX]] and [[PMAIP1]] also induces a gene that keeps stressed cells alive and reducing. A second activity has been described: under hypoxia a fraction of TIGAR relocalises to mitochondria and complexes with hexokinase 2, raising its activity in a HIF1α-dependent manner.

The mouse genetics are awkward. Tigar-null mice develop normally; what they cannot do is regenerate intestinal epithelium after damage, a defect rescued by ROS scavengers and nucleosides. In an intestinal adenoma model, TIGAR loss reduces tumour burden and extends survival, and TIGAR is elevated in human colon tumours — on that evidence it supports rapid proliferation, malignant included.

## What is uncertain

Whether fructose-2,6-bisphosphate hydrolysis is the activity that matters in cells is a live question. Catalytic efficiency on that substrate is modest, the structural work shows an active site considerably more open than the specificity-restricted pocket of PFK-2/FBPase-2, and activity on 2,3-bisphosphoglycerate has also been reported. Few studies have separated phosphatase-dependent from phosphatase-independent effects with catalytically dead mutants, so much of what is credited to the enzymology could belong to protein interactions — as the hexokinase 2 result, characterised under hypoxia alone, suggests.

Two further cautions. TIGAR has p53-independent inputs, so its induction under a compound is not evidence that p53 is engaged; it corroborates a p53 reading only alongside more specific members. And its directional meaning for cancer is inverted relative to its origin: a p53 target ought to be tumour-suppressive, but the knockout mice and human tumour expression both argue it supports tumour growth — a context-dependent survival factor that p53 happens to control. The step from transcript to metabolite is also not short: fructose-2,6-bisphosphate is under layered allosteric control, and a modest change in TIGAR mRNA need not move it measurably.

## References

- Bensaad et al., 2006, Cell — identified TIGAR as a p53-inducible regulator of glycolysis and apoptosis acting through fructose-2,6-bisphosphate and the pentose phosphate pathway.
- Li & Jogl, 2009, Journal of Biological Chemistry — structural and biochemical characterisation of TIGAR, showing a histidine-phosphatase fold with a more open active site than PFK-2/FBPase-2.
- Cheung et al., 2012, PNAS — mitochondrial localisation of TIGAR under hypoxia stimulates hexokinase 2 and lowers ROS and cell death.
- Cheung et al., 2013, Developmental Cell — TIGAR is dispensable for normal development but required for efficient intestinal regeneration and for tumour growth in an intestinal adenoma model.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (17 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 4.24× (z +21.6, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.648× (z -6.5, q 5e-08, down in 27 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Omeprazole (drug)]] 0.05 µM: 0.772× (z -3.9, q 0.011, down in 13 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO22]] (+0.71, fdr 7e-06), [[GRIN2C]] (+0.61, fdr 1e-05), [[SESN1]] (+0.59, fdr 1e-05); moves opposite to [[AZIN1]] (-0.50, fdr 3e-05), [[LRBA]] (-0.49, fdr 6e-05), [[CRYZ]] (-0.46, fdr 3e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1214.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **4.24×** | +21.6 | 0e+00 | 47/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.65×** | +20.6 | 0e+00 | 45/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.14×** | +17.1 | 0e+00 | 44/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.95×** | +16.1 | 0e+00 | 45/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.94×** | +16.1 | 0e+00 | 45/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.77×** | +14.6 | 0e+00 | 41/46 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +14.1 | 3e-43 | 37/47 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.49×** | +13.1 | 2e-37 | 43/46 (A498, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.39×** | +13.0 | 6e-37 | 36/46 (A549, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.38×** | +13.0 | 1e-36 | 44/47 (SW480, SW 900, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **5.17×** | +12.8 | 7e-36 | 43/48 (LoVo, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.28×** | +12.3 | 3e-33 | 45/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.24×** | +12.0 | 1e-31 | 41/47 (RKO, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.09×** | +11.0 | 2e-26 | 41/46 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.12×** | +10.8 | 2e-25 | 41/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.28×** | +9.3 | 6e-19 | 34/46 (LS 180, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.73×** | +8.1 | 1e-14 | 34/47 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +7.1 | 3e-11 | 34/47 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +6.2 | 2e-08 | 25/47 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +6.1 | 2e-08 | 27/47 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.49×** | +6.0 | 6e-08 | 30/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.40×** | +5.0 | 1e-05 | 28/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1214.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.648×** | -6.5 | 5e-08 | 27/45 (SW1417, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.651×** | -6.2 | 2e-07 | 25/37 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.716×** | -5.0 | 1e-04 | 25/47 (SW480, PANC-1, …) | all doses, flat |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **0.772×** | -3.9 | 0.011 | 13/47 (SK-MEL-2, LoVo, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.833×** | -3.9 | 0.011 | 23/47 (AsPC-1, SW 900, …) | all doses, flat | low cells (technical?) |
| [[NG25 (drug)]] 5 µM |  | **0.610×** | -3.9 | 0.011 | 15/45 (RPMI-7951, KATO III, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.780×** | -3.7 | 0.016 | 16/46 (SW1417, SW 900, …) | top dose only |  |
| [[AZD-8055 (drug)]] 5 µM |  | **0.641×** | -3.5 | 0.034 | 7/47 (CHP-212, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | **0.794×** | -3.4 | 0.034 | 12/46 (LS 180, NCI-H23, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.795×** | -3.4 | 0.034 | 9/46 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.798×** | -3.4 | 0.039 | 15/47 (SW 900, Panc 03.27, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.803×** | -3.3 | 0.050 | 14/47 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -3.2 | 0.060 | 1/47 (MIA PaCa-2) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.804×** | -3.1 | 0.068 | 11/46 (NCI-H23, HOP62, …) | rises with dose |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.750×** | -3.1 | 0.080 | 11/47 (HS-578T, NCI-H23, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.69 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1214. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 36.3 | 15 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.89× (z +20.9) | — |
| [[A549 (line)]] | wt | 53.0 | 11 (3 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -8.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 49.3 | 12 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.10× (z +19.1) | — |
| [[LoVo (line)]] | wt | 59.1 | 11 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +21.3) | — |
| [[NCI-H23 (line)]] | alt | 110 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +18.7) | — |
| [[RKO (line)]] | wt | 84.2 | 9 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0900× (z -18.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 35.5 | 10 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.54× (z +19.5) | — |
| [[A498 (line)]] | wt | 26.7 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +16.3) | — |
| [[SNU-1 (line)]] | wt | 60.2 | 7 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +12.1) | — |
| [[KATO III (line)]] | alt | 15.7 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 16.3× (z +16.1) | — |
| [[A-427 (line)]] | wt | 108 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.3× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -15.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 26.0 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.30× (z +11.7) | [[Selinexor (drug)]] 5 µM 0.262× (z -12.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[MIA PaCa-2 (line)]] | alt | 24.5 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 42.7 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.24× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.140× (z -14.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 38.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.42× (z +10.4) | [[Selinexor (drug)]] 5 µM 0.341× (z -10.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW48 (line)]] | wt | 55.5 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.21× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.111× (z -12.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 63.7 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +15.1) | — |
| [[H4 (line)]] | wt | 37.5 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +15.4) | — |
| [[HOP62 (line)]] | alt | 45.8 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.19× (z +13.4) | — |
| [[hTERT-HPNE (line)]] | wt | 25.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.95× (z +15.1) | — |
| [[LOX-IMVI (line)]] | wt | 49.9 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +15.0) | — |
| [[HepG2_C3A (line)]] | wt | 36.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.30× (z +15.1) | — |
| [[NCI-H1792 (line)]] | alt | 15.0 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.40× (z +11.0) | — |
| [[NCI-H2347 (line)]] | alt | 26.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 23.6 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.27× (z +12.6) | — |
| [[SW1417 (line)]] | alt | 42.2 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -20.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 13.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 11.4× (z +10.0) | — |
| [[HS-578T (line)]] | alt | 19.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.69× (z +9.4) | — |
| [[A-172 (line)]] | wt | 20.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.09× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 62.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 38.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 15.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.79× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 27.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.397× (z -9.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 41.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0948× (z -15.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 52.3 | 0 | 1 | — | [[Rifaximin (drug)]] 5 µM 0.0568× (z -9.6) |
| [[C-33 A (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.25 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1214), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO22]] | +0.71 | +0.68 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[GRIN2C]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SESN1]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 | pathway: TP53 Regulates Metabolic Genes; STRING 568 |
| [[ZNF79]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[ACER2]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[FDXR]] | +0.58 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[PANK1]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[AEN]] | +0.56 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[PPM1D]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ACTA2]] | +0.55 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[PINCR]] | +0.55 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[GPX1]] | +0.53 | +0.43 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AZIN1]] | -0.50 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[LRBA]] | -0.49 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[CRYZ]] | -0.46 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[PFKM]] | -0.46 | -0.43 / -0.41 | both halves | 4e-05 | STRING 979 |
| [[FXR1]] | -0.46 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[HUWE1]] | -0.45 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[CCDC6]] | -0.45 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[CLCN3]] | -0.45 | -0.29 / -0.44 | both halves | 3e-04 |  |
| [[ST13]] | -0.43 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[LMCD1-AS1]] | -0.43 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[LZTFL1]] | -0.43 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[NONO]] | -0.42 | -0.44 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TIGAR's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GRIN2C]] | B | GRIN2C activity raises TIGAR's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 1.55× lower at baseline in the lines without GRIN2C | 0.067 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[TP53]] | C | TP53 activity strengthens TIGAR's drug response | recorded loss-of-function mutation of TP53 in 30 lines vs 17 not recorded | the TP53-altered lines respond 0.79× as strongly (z diff +1.30); strongest at Doxorubicin (hydrochloride) 5 µM: 2.06x vs 4.67x (z diff +3.9) | 0.847 over the table, 0.066 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.3, 37.0); signed map (43.0, -25.1). **Vector** length 93.8, 29.0% of its response variance represented; |z| ≥ 3 in 1,492 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.4 | +14.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +20.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.9 | +8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.7 | +13.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.1 | +6.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.8 | +3.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.2 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.3 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.4 | +14.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -5.3 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | +0.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.3 | +7.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -4.0 | +3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.0 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | +2.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | TP53 induced glycolysis regulatory phosphatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.32 — chr12:4,307,763-4,360,028 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C12orf5 |
| Gene groups (HGNC) | Sugar phosphatases |
| Reactome | 2 pathways, smallest: TP53 Regulates Metabolic Genes; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ88](https://www.uniprot.org/uniprotkb/Q9NQ88) (Fructose-2,6-bisphosphatase TIGAR):

> Fructose-bisphosphatase hydrolyzing fructose-2,6-bisphosphate as well as fructose-1,6-bisphosphate. Acts as a negative regulator of glycolysis by lowering intracellular levels of fructose-2,6-bisphosphate in a p53/TP53-dependent manner, resulting in the pentose phosphate pathway (PPP) activation and NADPH production. Contributes to the generation of reduced glutathione to cause a decrease in intracellular reactive oxygen species (ROS) content, correlating with its ability to protect cells from …

**Summary**, from NCBI Gene [57103](https://www.ncbi.nlm.nih.gov/gene/57103):

> This gene is regulated as part of the p53 tumor suppressor pathway and encodes a protein with sequence similarity to the bisphosphate domain of the glycolytic enzyme that degrades fructose-2,6-bisphosphate. The protein functions by blocking glycolysis and directing the pathway into the pentose phosphate shunt. Expression of this protein also protects cells from DNA damaging reactive oxygen species and provides some protection from DNA damage-induced apoptosis. The 12p13.32 region that includes …

**Accessions** — [HGNC:1185](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1185) · Entrez [57103](https://www.ncbi.nlm.nih.gov/gene/57103) · UniProt [Q9NQ88](https://www.uniprot.org/uniprotkb/Q9NQ88) · Ensembl [ENSG00000078237](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078237)

## Data

Gene col 1214: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1214); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1214, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1214]; `tensor/DDL_lfc|DDL_z.npy` [1214]; `embed/gene_vectors.npy` [1214]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1214 or target_col == 1214). Every well: [[TIGAR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/TIGAR.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
