---
symbol: "CLPTM1"
type: "gene"
col: 2506
ensembl_id: "ENSG00000104853"
name: "CLPTM1 regulator of GABA type A receptor forward trafficking"
location: "19q13.32"
module: 3
arm: "+"
pooled_cpm: 51.73
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CLPTM1

*CLPTM1 regulator of GABA type A receptor forward trafficking* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.25× (z +17.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.931× (z -5.4, q 3e-05, down in 0 of 49 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HOP62 0.577×; ⚠ cell-cycle shift, explains ~17% of this change); [[DTP3 (drug)]] 5 µM in 1 line (C-33 A 0.0913×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (AN3 CA 0.148×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB5C]] (+0.68, fdr 1e-05), [[DHPS]] (+0.65, fdr 1e-05), [[GLG1]] (+0.64, fdr 1e-05); moves opposite to [[TMA16]] (-0.56, fdr 9e-05), [[GLRX2]] (-0.54, fdr 2e-05), [[NSRP1]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2506.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.25×** | +17.2 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.17×** | +16.4 | 0e+00 | 46/48 (SW480, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.03×** | +15.0 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +14.3 | 5e-44 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.87×** | +13.3 | 4e-38 | 47/48 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.01×** | +12.2 | 3e-32 | 45/49 (SW480, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.62×** | +10.2 | 1e-22 | 35/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.61×** | +10.1 | 6e-22 | 39/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.39×** | +9.7 | 3e-20 | 38/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +8.8 | 9e-17 | 35/48 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +6.4 | 7e-09 | 38/48 (A-427, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +5.3 | 6e-06 | 25/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.24×** | +4.4 | 5e-04 | 21/47 (RKO, C-33 A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +4.4 | 5e-04 | 22/48 (SK-MEL-2, A-427, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.19× | +3.6 | 0.012 | 16/48 (BT-474, KATO III, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.025 | 10/49 (HOP62, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Isocorydine (drug)]] 5 µM |  | 1.10× | +3.0 | 0.070 | 0/49 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2506.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HOP62 0.577×; ⚠ cell-cycle shift, explains ~17% of this change); [[DTP3 (drug)]] 5 µM in 1 line (C-33 A 0.0913×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (AN3 CA 0.148×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -5.4 | 3e-05 | 0/49 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.800×** | -4.8 | 6e-04 | 23/48 (LoVo, RPMI-7951, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.866× | -4.3 | 0.003 | 19/48 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.846× | -3.5 | 0.055 | 13/48 (SW48, KATO III, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.897× | -3.3 | 0.12 | 6/48 (HS-578T, KATO III, …) | top dose only |  |
| [[Finasteride (drug)]] 5 µM |  | 0.861× | -3.1 | 0.20 | 14/48 (PANC-1, A498, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2506. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 46.9 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +16.5) | — |
| [[HOP62 (line)]] | alt | 158 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.23× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.577× (z -10.8) ⚠ cell-cycle shift, explains ~17% of this change |
| [[BT-474 (line)]] | alt | 55.8 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.28× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.14× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 69.0 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.77× (z +11.6) | — |
| [[KATO III (line)]] | alt | 61.8 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +12.7) | — |
| [[LoVo (line)]] | wt | 33.4 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.07× (z +13.4) | — |
| [[LS 180 (line)]] | wt | 45.0 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.21× (z +10.4) | — |
| [[NCI-H460 (line)]] | wt | 37.7 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +13.5) | — |
| [[A549 (line)]] | wt | 67.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.1) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.36× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 42.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 40.6 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.34× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 63.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 46.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.95× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 30.7 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 53.7 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.66× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.57× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 53.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.43× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 37.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +12.6) | — |
| [[SHP-77 (line)]] | alt | 39.4 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.83× (z +8.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.74× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 52.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +10.2) | — |
| [[A498 (line)]] | wt | 52.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.5) ⚠ cell-cycle shift, explains ~17% of this change | — |
| [[AN3 CA (line)]] | alt | 58.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.148× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 50.3 | 0 | 1 | — | [[DTP3 (drug)]] 5 µM 0.0913× (z -10.5) |
| [[HS-578T (line)]] | alt | 69.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.45× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 42.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.86× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 55.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.14× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 65.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.38× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 41.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.53× (z +8.8) | — |
| [[A-172 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2506), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB5C]] | +0.68 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[DHPS]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[GLG1]] | +0.64 | +0.67 / +0.54 | both halves | 1e-05 | STRING 524 |
| [[GRN]] | +0.63 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[GNPTG]] | +0.62 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[GNB2]] | +0.62 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[MOSPD3]] | +0.62 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[GM2A]] | +0.62 | +0.64 / +0.39 | both halves | 5e-05 |  |
| [[PCYOX1]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[OS9]] | +0.61 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[PIK3R2]] | +0.61 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[LMAN2]] | +0.60 | +0.61 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMA16]] | -0.56 | -0.62 / -0.37 | both halves | 9e-05 |  |
| [[GLRX2]] | -0.54 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[NSRP1]] | -0.53 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[CDV3]] | -0.52 | -0.64 / -0.35 | both halves | 1e-04 |  |
| [[BCL2]] | -0.52 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[KCNMB3]] | -0.51 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[GCFC2]] | -0.51 | -0.51 / -0.36 | both halves | 1e-04 |  |
| [[PPID]] | -0.51 | -0.59 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.379). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-15.4, -18.8); signed map (-50.4, -8.5). **Vector** length 79.0, 17.8% of its response variance represented; |z| ≥ 3 in 989 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.8 | +17.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.5 | +16.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.0 | +12.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.8 | +13.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | +3.2 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +9.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.2 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.2 | +0.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.2 | -0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.8 | -1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -5.4 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -3.9 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -0.9 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | CLPTM1 regulator of GABA type A receptor forward trafficking |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:44,954,585-44,993,341 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [O96005](https://www.uniprot.org/uniprotkb/O96005) (Putative lipid scramblase CLPTM1):

> Involved in GABAergic but not glutamatergic transmission. Binds and traps GABAA receptors in the endoplasmic reticulum (ER). Modulates postsynaptic GABAergic transmission, and therefore inhibitory neurotransmission, by reducing the plasma membrane expression of these receptors. Altered GABAergic signaling is one among many causes of cleft palate (By similarity). Might function as a lipid scramblase, translocating lipids in membranes from one leaflet to the other one (By similarity). Required …

**Summary**, from NCBI Gene [1209](https://www.ncbi.nlm.nih.gov/gene/1209):

> Predicted to enable GABA receptor binding activity. Predicted to be involved in regulation of T cell differentiation in thymus and regulation of postsynaptic membrane neurotransmitter receptor levels. Predicted to act upstream of or within inhibitory chemical synaptic transmission; memory; and regulation of synaptic plasticity. Located in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:2087](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2087) · Entrez [1209](https://www.ncbi.nlm.nih.gov/gene/1209) · UniProt [O96005](https://www.uniprot.org/uniprotkb/O96005) · Ensembl [ENSG00000104853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104853)

## Data

Gene col 2506: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2506); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2506, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2506]; `tensor/DDL_lfc|DDL_z.npy` [2506]; `embed/gene_vectors.npy` [2506]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2506 or target_col == 2506). Every well: [[CLPTM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLPTM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
