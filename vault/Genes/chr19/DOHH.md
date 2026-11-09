---
symbol: "DOHH"
type: "gene"
col: 5007
ensembl_id: "ENSG00000129932"
name: "deoxyhypusine hydroxylase"
location: "19p13.3"
module: 114
arm: "+"
pooled_cpm: 6.42
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# DOHH

*deoxyhypusine hydroxylase* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.13× (z +14.9, q 0e+00, up in 37 of 43 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 3.31× (z +11.0, q 7e-26, up in 37 of 42 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Hesperidin (drug)]] 5 µM in 1 line (SNU-423 0.0902×); [[Rapamycin (drug)]] 0.5 µM in 1 line (NCI-H460 0.175×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZCCHC3]] (+0.78, fdr 7e-06), [[ZC3HC1]] (+0.72, fdr 7e-06), [[YJU2]] (+0.71, fdr 1e-05); moves opposite to [[TMEM106C]] (-0.62, fdr 4e-05), [[TMED7]] (-0.61, fdr 1e-05), [[TMEM30A]] (-0.59, fdr 7e-06).
> It is in [[Module 114]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5007.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **3.13×** | +14.9 | 0e+00 | 37/43 (NCI-H460, C32, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.31×** | +11.0 | 7e-26 | 37/42 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.78×** | +9.4 | 8e-19 | 36/43 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.22×** | +7.3 | 3e-11 | 37/47 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +7.1 | 1e-10 | 31/35 (NCI-H2347, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.12×** | +6.6 | 3e-09 | 35/45 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.03×** | +6.5 | 7e-09 | 29/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.02×** | +6.5 | 7e-09 | 33/46 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.89×** | +5.8 | 3e-07 | 29/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.97×** | +5.3 | 8e-06 | 26/46 (RKO, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.74×** | +5.1 | 2e-05 | 26/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.68×** | +4.8 | 8e-05 | 15/30 (J82, PANC-1, …) | inconsistent across doses | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.7 | 1e-04 | 24/42 (HT-29, LS 180, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.75×** | +4.7 | 1e-04 | 11/16 (A498, SW1417, …) | inconsistent across doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.64×** | +4.6 | 2e-04 | 14/34 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.99×** | +4.3 | 6e-04 | 16/36 (NCI-H460, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +4.0 | 0.002 | 15/45 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.52×** | +3.8 | 0.004 | 17/46 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.52×** | +3.6 | 0.008 | 15/43 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.5 µM |  | **1.69×** | +3.3 | 0.028 | 1/46 (PANC-1) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.67×** | +3.2 | 0.036 | 5/36 (J82, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.65×** | +3.1 | 0.045 | 9/45 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.87×** | +3.0 | 0.060 | 4/39 (SW1417, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.079 | 12/47 (HS-578T, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5007.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Hesperidin (drug)]] 5 µM in 1 line (SNU-423 0.0902×); [[Rapamycin (drug)]] 0.5 µM in 1 line (NCI-H460 0.175×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pemetrexed (drug)]] 0.5 µM |  | 0.674× | -3.7 | 0.13 | 15/47 (hTERT-HPNE, HEC-1-A, …) | two highest doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.701× | -3.3 | 0.25 | 11/45 (KATO III, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.792× | -3.1 | 0.36 | 17/48 (BT-474, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5007. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.59 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +18.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 15.9× (z +13.5) | [[Rapamycin (drug)]] 0.5 µM 0.175× (z -8.5) |
| [[A498 (line)]] | wt | 9.33 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +8.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[C32 (line)]] | wt | 5.77 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +12.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HOP62 (line)]] | alt | 3.67 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +9.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LoVo (line)]] | wt | 5.52 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +8.9) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2030 (line)]] | alt | 8.61 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +9.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[PANC-1 (line)]] | alt | 6.45 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +8.7) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[RPMI-7951 (line)]] | alt | 7.40 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +9.3) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 6.01 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.82× (z +10.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SNU-423 (line)]] | alt | 6.35 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0902× (z -8.5) |
| [[A-172 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5007), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC3]] | +0.78 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[ZC3HC1]] | +0.72 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[YJU2]] | +0.71 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[MTG2]] | +0.71 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[ZCCHC10]] | +0.70 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[MED18]] | +0.69 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[ZNF316]] | +0.69 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[COIL]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[RPP14]] | +0.67 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[ARMC5]] | +0.67 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[GMEB2]] | +0.66 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[SETDB1]] | +0.66 | +0.50 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM106C]] | -0.62 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[TMED7]] | -0.61 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[TMEM30A]] | -0.59 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[MAPK9]] | -0.58 | -0.47 / -0.58 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.792). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.9, 7.0); signed map (-3.0, -14.6). **Vector** length 58.7, 9.47% of its response variance represented; |z| ≥ 3 in 818 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.3 | +14.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +11.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +7.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +1.1 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.8 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.3 | +2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.2 |
|  | [[Lapatinib ditosylate (drug)]] 0.5 µM |  | -1.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | deoxyhypusine hydroxylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:3,490,821-3,500,674 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4293; previously HLRC1 |
| Gene groups (HGNC) | Armadillo like helical domain containing; Oxygenases |
| Reactome | 2 pathways, smallest: Hypusine synthesis from eIF5A-lysine; Gamma carboxylation, hypusinylation, hydroxylation, and arylsulfatase activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BU89](https://www.uniprot.org/uniprotkb/Q9BU89) (Deoxyhypusine hydroxylase):

> Catalyzes the hydroxylation of the N(6)-(4-aminobutyl)-L-lysine intermediate produced by deoxyhypusine synthase/DHPS on a critical lysine of the eukaryotic translation initiation factor 5A/eIF-5A. This is the second step of the post-translational modification of that lysine into an unusual amino acid residue named hypusine. Hypusination is unique to mature eIF-5A factor and is essential for its function (By similarity).

**Summary**, from NCBI Gene [83475](https://www.ncbi.nlm.nih.gov/gene/83475):

> This gene encodes a metalloenzyme that catalyzes the last step in the conversion of lysine to the unique amino acid hypusine in eukaryotic initiation factor 5A. The encoded protein hydroxylates deoxyhypusine to form hypusine in the mature eukaryotic initiation factor 5A protein. Alternative splicing results in multiple transcript variants.[provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:28662](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28662) · Entrez [83475](https://www.ncbi.nlm.nih.gov/gene/83475) · UniProt [Q9BU89](https://www.uniprot.org/uniprotkb/Q9BU89) · Ensembl [ENSG00000129932](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129932)

## Data

Gene col 5007: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5007); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5007, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5007]; `tensor/DDL_lfc|DDL_z.npy` [5007]; `embed/gene_vectors.npy` [5007]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5007 or target_col == 5007). Every well: [[DOHH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOHH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
