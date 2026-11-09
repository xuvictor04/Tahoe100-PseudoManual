---
symbol: "OCEL1"
type: "gene"
col: 1794
ensembl_id: "ENSG00000099330"
name: "occludin/ELL domain containing 1"
location: "19p13.11"
module: 24
arm: "+"
pooled_cpm: 5.43
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 16
n_dd_up_clean: 9
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# OCEL1

*occludin/ELL domain containing 1* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.47× (z +7.5, q 5e-11, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.283× (z -10.4, q 1e-22, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (73 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 28 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL55]] (+0.72, fdr 4e-05), [[TRPT1]] (+0.71, fdr 5e-05), [[NUDT22]] (+0.70, fdr 1e-04); moves opposite to [[NDUFS1]] (-0.64, fdr 4e-04), [[SRSF1]] (-0.63, fdr 4e-04), [[UBQLN4]] (-0.61, fdr 1e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1794.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.47×** | +7.5 | 5e-11 | 34/47 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.32×** | +6.9 | 1e-09 | 34/46 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.2 | 0.005 | 16/40 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.008 | 13/46 (A-172, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.009 | 19/48 (A498, BT-474, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.58×** | +3.7 | 0.017 | 13/46 (NCI-H1573, hTERT-HPNE, …) | rises with dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.080 | 9/46 (NCI-H1792, hTERT-HPNE, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.099 | 9/45 (HepG2/C3A, HEC-1-A, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.099 | 14/41 (LoVo, PANC-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1794.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.283×** | -10.4 | 1e-22 | 41/47 (NCI-H2030, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.339×** | -8.9 | 1e-16 | 39/45 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.375×** | -8.1 | 1e-13 | 38/46 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.423×** | -7.1 | 2e-10 | 29/40 (J82, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.599×** | -6.0 | 3e-07 | 25/42 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.498×** | -5.7 | 8e-07 | 23/40 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.220×** | -5.7 | 8e-07 | 30/41 (LoVo, CFPAC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.270×** | -5.0 | 5e-05 | 28/43 (Panc 03.27, BT-474, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.589×** | -4.2 | 0.002 | 16/44 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.618×** | -3.8 | 0.010 | 14/43 (Panc 03.27, BT-474, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.651×** | -3.5 | 0.020 | 16/47 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.669×** | -3.3 | 0.043 | 18/45 (A-172, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.665×** | -3.2 | 0.063 | 13/43 (H4, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.687×** | -3.1 | 0.074 | 16/47 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.688×** | -3.1 | 0.074 | 10/46 (HEC-1-A, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.689×** | -3.1 | 0.074 | 17/46 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1794. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 6.04 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0817× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0831× (z -9.3) |
| [[A-427 (line)]] | wt | 8.96 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -8.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.127× (z -8.7) |
| [[J82 (line)]] | alt | 6.10 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0804× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0945× (z -9.5) |
| [[SW480 (line)]] | alt | 4.00 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0279× (z -15.0) |
| [[A-172 (line)]] | wt | 7.93 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.101× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 3.33 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0441× (z -9.1) |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0492× (z -12.2) |
| [[NCI-H2030 (line)]] | alt | 9.26 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.103× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 2.67 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0446× (z -11.2) |
| [[SNU-423 (line)]] | alt | 6.26 | 0 | 1 | — | [[Phenytoin (sodium) (drug)]] 5 µM 0.0491× (z -10.7) |
| [[A498 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1794), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 18 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL55]] | +0.72 | +0.40 / +0.70 | both halves | 4e-05 |  |
| [[TRPT1]] | +0.71 | +0.39 / +0.67 | both halves | 5e-05 |  |
| [[NUDT22]] | +0.70 | +0.35 / +0.72 | both halves | 1e-04 |  |
| [[TMEM191A-1]] | +0.69 | +0.28 / +0.70 | both halves | 3e-04 |  |
| [[NDUFA7]] | +0.67 | +0.37 / +0.66 | both halves | 8e-05 |  |
| [[LAGE3]] | +0.67 | +0.21 / +0.70 | both halves | 7e-04 |  |
| [[CARHSP1]] | +0.66 | +0.21 / +0.67 | both halves | 7e-04 |  |
| [[RNASE4]] | +0.66 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[C19orf81]] | +0.66 | +0.30 / +0.67 | both halves | 2e-04 |  |
| [[MRPL17]] | +0.65 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[DUSP23]] | +0.65 | +0.34 / +0.60 | both halves | 1e-04 |  |
| [[ALDOC]] | +0.64 | +0.29 / +0.67 | both halves | 2e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFS1]] | -0.64 | -0.26 / -0.63 | both halves | 4e-04 |  |
| [[SRSF1]] | -0.63 | -0.26 / -0.62 | both halves | 4e-04 |  |
| [[UBQLN4]] | -0.61 | -0.33 / -0.62 | both halves | 1e-04 |  |
| [[TMEM138]] | -0.61 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[PSME3IP1]] | -0.60 | -0.10 / -0.70 | ⚠ one half (not replicated) | 0.003 |  |
| [[DHFR]] | -0.60 | -0.16 / -0.67 | ⚠ one half (not replicated) | 0.001 |  |
| [[RCC2]] | -0.60 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[CERS2]] | -0.59 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[ZMPSTE24]] | -0.59 | -0.03 / -0.70 | ⚠ one half (not replicated) | 0.006 |  |
| [[SSU72]] | -0.58 | -0.07 / -0.70 | ⚠ one half (not replicated) | 0.004 |  |
| [[RCN1]] | -0.58 | -0.13 / -0.62 | ⚠ one half (not replicated) | 0.002 |  |
| [[ANAPC7]] | -0.58 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[SLC39A10]] | -0.57 | -0.26 / -0.49 | both halves | 4e-04 |  |
| [[EIF3F]] | -0.57 | -0.22 / -0.59 | both halves | 6e-04 |  |
| [[GNL3L]] | -0.57 | -0.36 / -0.50 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-44.6, -17.2); signed map (-30.4, 14.1). **Vector** length 53.8, 8.43% of its response variance represented; |z| ≥ 3 in 800 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +6.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.7 | +7.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.9 | +4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +3.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +1.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.0 | +2.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.2 | +0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.0 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.9 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | +0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | occludin/ELL domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,226,213-17,229,219 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22709 |
| Hallmark sets | MYOGENESIS |
| Matched by | ensembl_id |

UniProt [Q9H607](https://www.uniprot.org/uniprotkb/Q9H607) carries no function annotation.

**Summary**, from NCBI Gene [79629](https://www.ncbi.nlm.nih.gov/gene/79629):

> Predicted to be involved in bicellular tight junction assembly. Predicted to be active in apical plasma membrane; bicellular tight junction; and cytoplasmic vesicle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26221](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26221) · Entrez [79629](https://www.ncbi.nlm.nih.gov/gene/79629) · UniProt [Q9H607](https://www.uniprot.org/uniprotkb/Q9H607) · Ensembl [ENSG00000099330](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099330)

## Data

Gene col 1794: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1794); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1794, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1794]; `tensor/DDL_lfc|DDL_z.npy` [1794]; `embed/gene_vectors.npy` [1794]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1794 or target_col == 1794). Every well: [[OCEL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OCEL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
