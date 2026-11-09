---
symbol: "SELENOI"
type: "gene"
col: 6107
ensembl_id: "ENSG00000138018"
name: "selenoprotein I"
location: "2p23.3"
module: 126
arm: "+"
pooled_cpm: 64.99
n_lines_expressing: 50
n_dd_up: 40
n_dd_down: 1
n_dd_up_clean: 25
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# SELENOI

*selenoprotein I* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.30× (z +17.7, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.586× (z -4.2, q 0.013, down in 24 of 49 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DESI1]] (+0.61, fdr 8e-06), [[ECPAS]] (+0.55, fdr 2e-05), [[SETD7]] (+0.54, fdr 2e-05); moves opposite to [[SYF2]] (-0.56, fdr 5e-05), [[CTR9]] (-0.55, fdr 5e-05), [[KLHL20]] (-0.53, fdr 3e-05).
> It is in [[Module 126]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6107.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.30×** | +17.7 | 0e+00 | 47/48 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +14.3 | 5e-44 | 48/48 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.33×** | +12.7 | 8e-35 | 48/48 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.11×** | +11.2 | 4e-27 | 48/48 (SW480, SW1417, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.09×** | +11.1 | 2e-26 | 45/48 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +10.8 | 2e-25 | 44/48 (A-172, NCI-H23, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.05×** | +10.8 | 2e-25 | 46/48 (SW480, SW1417, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +9.4 | 3e-19 | 42/47 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.85×** | +9.2 | 2e-18 | 45/48 (AsPC-1, NCI-H1792, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +9.0 | 1e-17 | 42/50 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +7.3 | 1e-11 | 35/48 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.60×** | +7.0 | 1e-10 | 37/48 (MIA PaCa-2, HOP62, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +6.9 | 2e-10 | 32/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.51×** | +6.1 | 3e-08 | 34/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +6.0 | 6e-08 | 35/48 (A498, C32, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +6.0 | 9e-08 | 36/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +5.7 | 4e-07 | 33/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +5.1 | 8e-06 | 32/48 (A498, HOP62, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +4.7 | 7e-05 | 26/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.30×** | +3.9 | 0.002 | 23/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.29×** | +3.8 | 0.003 | 24/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6107.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.586×** | -4.2 | 0.013 | 24/49 (LoVo, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 0.657× | -3.3 | 0.21 | 18/47 (HCT15, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.808× | -3.3 | 0.21 | 22/48 (KATO III, LoVo, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.820× | -3.0 | 0.31 | 19/48 (COLO 205, SW480, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6107. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 86.0 | 12 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +15.6) | — |
| [[HOP62 (line)]] | alt | 43.6 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +13.8) | — |
| [[A-172 (line)]] | wt | 41.1 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +16.2) | — |
| [[AsPC-1 (line)]] | alt | 57.7 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +20.0) | — |
| [[SNU-423 (line)]] | alt | 24.9 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +11.4) | — |
| [[C32 (line)]] | wt | 42.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 55.4 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +13.9) | — |
| [[NCI-H1792 (line)]] | alt | 51.3 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +13.6) | — |
| [[SW1417 (line)]] | alt | 86.2 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.2) | — |
| [[A549 (line)]] | wt | 60.9 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +11.8) | — |
| [[CFPAC-1 (line)]] | alt | 45.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +14.9) | — |
| [[HEC-1-A (line)]] | alt | 54.8 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 62.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +15.0) | — |
| [[NCI-H23 (line)]] | alt | 67.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +12.6) | — |
| [[NCI-H460 (line)]] | wt | 99.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +14.2) | — |
| [[Panc 03.27 (line)]] | alt | 52.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.5) | — |
| [[HepG2_C3A (line)]] | wt | 65.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +11.5) | — |
| [[LoVo (line)]] | wt | 71.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +15.8) | — |
| [[PANC-1 (line)]] | alt | 52.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +16.1) | — |
| [[SK-MEL-2 (line)]] | alt | 48.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +16.4) | — |
| [[A-427 (line)]] | wt | 89.4 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.39× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 34.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.55× (z +17.9) | — |
| [[HT-29 (line)]] | alt | 85.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +12.6) | — |
| [[hTERT-HPNE (line)]] | wt | 42.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +10.1) | — |
| [[J82 (line)]] | alt | 34.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +10.4) | — |
| [[KATO III (line)]] | alt | 75.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 84.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +16.1) | — |
| [[NCI-H2030 (line)]] | alt | 81.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +10.8) | — |
| [[NCI-H2347 (line)]] | alt | 47.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 68.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.7) | — |
| [[A498 (line)]] | wt | 117 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.3) | — |
| [[BT-474 (line)]] | alt | 75.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.4) | — |
| [[Hs 766T (line)]] | wt | 32.9 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.44× (z +8.5) ⚠ unreliable plate only | — |
| [[LS 180 (line)]] | wt | 72.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +14.2) | — |
| [[RKO (line)]] | wt | 83.2 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 59.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 63.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 85.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6107), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DESI1]] | +0.61 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[ECPAS]] | +0.55 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[SETD7]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[CNDP2]] | +0.51 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[UBQLN4]] | +0.51 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[FASN]] | +0.50 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[CLCC1]] | +0.50 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[RNASEH1]] | +0.50 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[IDE]] | +0.49 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[ACLY]] | +0.49 | +0.32 / +0.56 | both halves | 2e-04 |  |
| [[CYCS]] | +0.49 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[ELK4]] | +0.49 | +0.42 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYF2]] | -0.56 | -0.40 / -0.67 | both halves | 5e-05 |  |
| [[CTR9]] | -0.55 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[KLHL20]] | -0.53 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[CHMP2A]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[MARCHF9]] | -0.52 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[IGBP1]] | -0.52 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[ZNF350]] | -0.51 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[PPP1R3B]] | -0.51 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[TOGARAM1]] | -0.50 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SUMO4]] | -0.50 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[SPOP]] | -0.50 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[C18orf21]] | -0.49 | -0.30 / -0.54 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.371). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.7, -52.0); signed map (-11.7, -38.1). **Vector** length 92.3, 28.9% of its response variance represented; |z| ≥ 3 in 1,349 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.4 | +9.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +10.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +9.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.0 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | +5.0 | +3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +3.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.6 | +3.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -10.3 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.4 | -0.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +1.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[TAK-901 (drug)]] 0.5 µM |  | -2.3 | -1.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.3 | -3.3 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -2.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | selenoprotein I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:26,308,547-26,395,885 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1724, SELI, SEPI; previously EPT1 |
| Gene groups (HGNC) | Selenoproteins |
| Reactome | 4 pathways, smallest: Synthesis of PE; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0D9](https://www.uniprot.org/uniprotkb/Q9C0D9) (Ethanolaminephosphotransferase 1):

> Ethanolaminephosphotransferase that catalyzes the transfer of phosphoethanolamine (PE) from CDP-ethanolamine to lipid acceptors, the final step in the synthesis of PE via the 'Kennedy' pathway. PE is the second most abundant phospholipid of membranes in mammals and is involved in various membrane-related cellular processes. The enzyme is critical for the synthesis of several PE species and also catalyzes the synthesis of plasmanyl-PE, a lipid required for proper myelination and …

**Summary**, from NCBI Gene [85465](https://www.ncbi.nlm.nih.gov/gene/85465):

> The multi-pass transmembrane protein encoded by this gene belongs to the CDP-alcohol phosphatidyltransferase class-I family. It catalyzes the transfer of phosphoethanolamine from CDP-ethanolamine to diacylglycerol to produce phosphatidylethanolamine, which is involved in the formation and maintenance of vesicular membranes, regulation of lipid metabolism, and protein folding. This protein is a selenoprotein, containing the rare selenocysteine (Sec) amino acid at its active site. Sec is encoded …

**Accessions** — [HGNC:29361](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29361) · Entrez [85465](https://www.ncbi.nlm.nih.gov/gene/85465) · UniProt [Q9C0D9](https://www.uniprot.org/uniprotkb/Q9C0D9) · Ensembl [ENSG00000138018](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138018)

## Data

Gene col 6107: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6107); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6107, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6107]; `tensor/DDL_lfc|DDL_z.npy` [6107]; `embed/gene_vectors.npy` [6107]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6107 or target_col == 6107). Every well: [[SELENOI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SELENOI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
