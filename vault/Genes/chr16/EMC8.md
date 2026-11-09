---
symbol: "EMC8"
type: "gene"
col: 5176
ensembl_id: "ENSG00000131148"
name: "ER membrane protein complex subunit 8"
location: "16q24.1"
module: 36
arm: "+"
pooled_cpm: 23.83
n_lines_expressing: 50
n_dd_up: 46
n_dd_down: 1
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# EMC8

*ER membrane protein complex subunit 8* — 16q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 46 drug-doses (22 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.62× (z +14.0, q 2e-41, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.759× (z -4.5, q 0.003, down in 21 of 48 measured lines) ⚠ cell-cycle shift, explains ~35% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.185×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.227×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 1 line (A498 0.615×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HIRA]] (+0.68, fdr 2e-05), [[PCSK7]] (+0.65, fdr 7e-06), [[FLAD1]] (+0.63, fdr 7e-06); moves opposite to [[SDCBP]] (-0.65, fdr 1e-05), [[MORF4L2]] (-0.59, fdr 1e-05), [[TENT5C]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 22 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 46 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5176.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.62×** | +14.0 | 2e-41 | 46/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.33×** | +13.8 | 1e-40 | 44/46 (SW480, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.16×** | +12.5 | 1e-33 | 44/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.71×** | +12.3 | 8e-33 | 38/47 (SW 900, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +11.9 | 2e-30 | 41/47 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.99×** | +11.2 | 5e-27 | 44/47 (HOP62, COLO 205, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.95×** | +10.9 | 2e-25 | 45/48 (NCI-H1792, COLO 205, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.93×** | +10.7 | 8e-25 | 44/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.91×** | +10.6 | 3e-24 | 41/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.39×** | +9.9 | 3e-21 | 38/46 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.78×** | +9.3 | 5e-19 | 37/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +9.0 | 8e-18 | 35/47 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.70×** | +8.6 | 3e-16 | 38/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +7.4 | 6e-12 | 35/47 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.70×** | +6.8 | 5e-10 | 28/47 (LS 180, NCI-H1792, …) | rises with dose | composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +6.6 | 2e-09 | 29/48 (NCI-H1792, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +6.5 | 3e-09 | 31/48 (SW480, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +6.1 | 2e-08 | 28/48 (MIA PaCa-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +4.6 | 9e-05 | 17/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +4.3 | 3e-04 | 24/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.005 | 19/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.5 | 0.006 | 13/48 (CFPAC-1, A549, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.36×** | +3.5 | 0.008 | 13/44 (HepG2/C3A, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.008 | 15/47 (NCI-H460, HOP62, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5176.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (A549 0.185×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.227×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Selinexor (drug)]] 5 µM in 1 line (A498 0.615×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.759×** | -4.5 | 0.003 | 21/48 (SW1417, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.856× | -3.6 | 0.064 | 21/48 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.858× | -3.6 | 0.064 | 21/48 (A498, A-427, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~83% of this change | 0.825× | -3.2 | 0.17 | 13/48 (HEC-1-A, PANC-1, …) | all doses, flat |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.781× | -3.2 | 0.17 | 8/48 (CFPAC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5176. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 22.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.185× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 22.4 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +10.8) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H460 (line)]] | wt | 17.8 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.8) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[SW480 (line)]] | alt | 20.7 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.97× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 27.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 11.5× (z +9.1) | — |
| [[A498 (line)]] | wt | 42.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.615× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 12.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +10.5) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[H4 (line)]] | wt | 16.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.20× (z +11.6) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[HepG2_C3A (line)]] | wt | 27.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +10.6) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[KATO III (line)]] | alt | 22.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +12.1) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H1573 (line)]] | alt | 25.5 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.32× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 24.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +13.7) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[A-172 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5176), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIRA]] | +0.68 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[PCSK7]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[FLAD1]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[EHMT1]] | +0.63 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[TRAPPC10]] | +0.61 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[LRRC14]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[PGP]] | +0.61 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[PARGP1]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[WDR53]] | +0.60 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[FBXL18]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ARPC5L]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[FOXK2]] | +0.59 | +0.39 / +0.66 | both halves | 5e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDCBP]] | -0.65 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[MORF4L2]] | -0.59 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[TENT5C]] | -0.56 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[SNX16]] | -0.51 | -0.30 / -0.60 | both halves | 2e-04 |  |
| [[MATCAP2]] | -0.50 | -0.29 / -0.55 | both halves | 2e-04 |  |
| [[ATF3]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.662). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-11.2, -17.5); signed map (-47.2, -23.5). **Vector** length 66.6, 13.8% of its response variance represented; |z| ≥ 3 in 1,105 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.2 | +14.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +11.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +9.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.6 | +7.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.6 | +3.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.4 | +3.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.3 | +3.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.6 | -3.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.8 | -4.5 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~83% of this change | -2.6 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -2.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.6 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.1 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ER membrane protein complex subunit 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.1 — chr16:85,771,758-85,799,608 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FAM158B; previously C16orf4, NOC4, C16orf2, COX4NB |
| Gene groups (HGNC) | ER membrane protein complex subunits |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [O43402](https://www.uniprot.org/uniprotkb/O43402) (ER membrane protein complex subunit 8):

> Part of the endoplasmic reticulum membrane protein complex (EMC) that enables the energy-independent insertion into endoplasmic reticulum membranes of newly synthesized membrane proteins. Preferentially accommodates proteins with transmembrane domains that are weakly hydrophobic or contain destabilizing features such as charged and aromatic residues. Involved in the cotranslational insertion of multi-pass membrane proteins in which stop-transfer membrane-anchor sequences become ER membrane …

**Summary**, from NCBI Gene [10328](https://www.ncbi.nlm.nih.gov/gene/10328):

> Contributes to membrane insertase activity. Involved in protein insertion into ER membrane by stop-transfer membrane-anchor sequence and tail-anchored membrane protein insertion into ER membrane. Located in endoplasmic reticulum. Part of EMC complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7864](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7864) · Entrez [10328](https://www.ncbi.nlm.nih.gov/gene/10328) · UniProt [O43402](https://www.uniprot.org/uniprotkb/O43402) · Ensembl [ENSG00000131148](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131148)

## Data

Gene col 5176: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5176); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5176, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5176]; `tensor/DDL_lfc|DDL_z.npy` [5176]; `embed/gene_vectors.npy` [5176]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5176 or target_col == 5176). Every well: [[EMC8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMC8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
