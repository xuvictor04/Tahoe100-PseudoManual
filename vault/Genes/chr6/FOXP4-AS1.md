---
symbol: "FOXP4-AS1"
type: "gene"
col: 13982
ensembl_id: "ENSG00000234753"
name: "FOXP4 antisense RNA 1"
location: "6p21.1"
module: 1
arm: "+"
pooled_cpm: 6.46
n_lines_expressing: 46
n_dd_up: 15
n_dd_down: 20
n_dd_up_clean: 11
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# FOXP4-AS1

*FOXP4 antisense RNA 1* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.41× (z +22.2, q 0e+00, up in 36 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.458× (z -10.0, q 8e-21, down in 25 of 42 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC5A6]] (+0.61, fdr 3e-05), [[SLC16A9]] (+0.59, fdr 6e-05), [[ZDHHC23]] (+0.59, fdr 2e-05); moves opposite to [[RMC1]] (-0.51, fdr 3e-04), [[PSMD9]] (-0.51, fdr 1e-04), [[TAOK3]] (-0.50, fdr 4e-04).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13982.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.41×** | +22.2 | 0e+00 | 36/38 (SW1417, A-172, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +6.1 | 3e-07 | 15/36 (Panc 03.27, BT-474, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +5.7 | 2e-06 | 4/9 (HT-29, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.42×** | +4.5 | 0.001 | 5/42 (SHP-77, HepG2/C3A, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.40×** | +4.3 | 0.002 | 5/44 (LoVo, J82, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +4.2 | 0.002 | 12/40 (NCI-H2347, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.38×** | +4.1 | 0.003 | 6/40 (NCI-H23, A-172, …) | two highest doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.8 | 0.009 | 13/39 (NCI-H2030, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.019 | 15/38 (NCI-H2347, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.021 | 3/42 (LoVo, NCI-H2030, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.026 | 15/40 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.032 | 5/40 (HOP62, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +3.4 | 0.034 | 3/14 (NCI-H2347, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Radotinib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.060 | 5/39 (A549, A-427, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | 1.19× | +3.1 | 0.065 | 11/42 (NCI-H23, COLO 205, …) | two highest doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.085 | 4/42 (NCI-H1792, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13982.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.458×** | -10.0 | 8e-21 | 25/42 (NCI-H23, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.553×** | -7.6 | 9e-12 | 21/42 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.356×** | -6.9 | 7e-10 | 20/40 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.583×** | -6.9 | 7e-10 | 19/42 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.421×** | -5.8 | 8e-07 | 19/38 (C-33 A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.655×** | -5.4 | 6e-06 | 15/42 (SW480, SW48, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.685×** | -4.8 | 1e-04 | 16/39 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.686×** | -4.8 | 1e-04 | 15/41 (LS 180, SW480, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.503×** | -4.6 | 3e-04 | 13/35 (NCI-H23, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.782×** | -4.4 | 5e-04 | 11/42 (LoVo, SW480, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.723×** | -4.0 | 0.003 | 9/41 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.744×** | -3.8 | 0.007 | 11/42 (HEC-1-A, SW48, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.766×** | -3.4 | 0.028 | 12/42 (LS 180, SW480, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.760×** | -3.4 | 0.030 | 11/41 (LS 180, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.761×** | -3.3 | 0.036 | 13/39 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | **0.788×** | -3.0 | 0.076 | 3/41 (J82, A549, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.793×** | -3.0 | 0.091 | 14/42 (LoVo, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13982. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.1 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -16.6) |
| [[LS 180 (line)]] | wt | 13.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0578× (z -12.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0696× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 18.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -15.5) |
| [[SW1417 (line)]] | alt | 4.15 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.18× (z +10.8) | [[Vandetanib (drug)]] 0.5 µM 0.0801× (z -8.6) |
| [[A-172 (line)]] | wt | 4.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.47× (z +10.3) | — |
| [[A-427 (line)]] | wt | 8.02 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0994× (z -10.5) |
| [[A498 (line)]] | wt | 1.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.30× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 8.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.75× (z +9.8) | — |
| [[C32 (line)]] | wt | 3.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 4.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 5.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.97× (z +9.7) | — |
| [[LoVo (line)]] | wt | 9.71 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.183× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 1.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.94× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 3.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 4.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +8.6) | — |
| [[RKO (line)]] | wt | 11.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -9.4) |
| [[SW48 (line)]] | wt | 14.0 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0696× (z -9.8) |
| [[A549 (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.918 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13982), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC5A6]] | +0.61 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[SLC16A9]] | +0.59 | +0.57 / +0.39 | both halves | 6e-05 |  |
| [[ZDHHC23]] | +0.59 | +0.61 / +0.49 | both halves | 2e-05 |  |
| [[LINC01357]] | +0.58 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[GABPB1-AS1]] | +0.57 | +0.54 / +0.33 | both halves | 1e-04 | same gene group |
| [[ADGRA3]] | +0.57 | +0.60 / +0.38 | both halves | 6e-05 |  |
| [[ASB4]] | +0.57 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[EPM2A]] | +0.55 | +0.54 / +0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[NEMP2-DT]] | +0.54 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[PALD1]] | +0.54 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[TRAF3]] | +0.53 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[QTRT1]] | +0.53 | +0.50 / +0.30 | both halves | 2e-04 |  |
| [[NFKBID]] | +0.53 | +0.35 / +0.47 | both halves | 1e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RMC1]] | -0.51 | -0.29 / -0.36 | both halves | 3e-04 |  |
| [[PSMD9]] | -0.51 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[TAOK3]] | -0.50 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[SNAP29]] | -0.49 | -0.23 / -0.35 | both halves | 5e-04 |  |
| [[RAB2A]] | -0.49 | -0.48 / -0.29 | both halves | 2e-04 |  |
| [[GNAI2]] | -0.49 | -0.35 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[KCTD21]] | -0.49 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[ESS2]] | -0.48 | -0.38 / -0.23 | both halves | 5e-04 |  |
| [[COMMD2]] | -0.48 | -0.29 / -0.30 | both halves | 2e-04 |  |
| [[YKT6]] | -0.48 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[ERP44]] | -0.48 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[TECPR1]] | -0.47 | -0.33 / -0.20 | both halves | 7e-04 |  |
| [[IK]] | -0.47 | -0.34 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.287). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.8, 6.4); signed map (23.6, -33.9). **Vector** length 83.0, 16.1% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +22.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +4.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.4 | +3.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.7 | -10.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.3 | -7.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -4.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | FOXP4 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p21.1 — chr6:41,452,889-41,548,621 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50332](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50332) · Entrez [101060264](https://www.ncbi.nlm.nih.gov/gene/101060264) · Ensembl [ENSG00000234753](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234753)

## Data

Gene col 13982: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13982); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13982, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13982]; `tensor/DDL_lfc|DDL_z.npy` [13982]; `embed/gene_vectors.npy` [13982]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13982 or target_col == 13982). Every well: [[FOXP4-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXP4-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
