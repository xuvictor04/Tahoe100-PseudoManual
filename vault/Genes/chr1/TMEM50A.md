---
symbol: "TMEM50A"
type: "gene"
col: 11444
ensembl_id: "ENSG00000183726"
name: "transmembrane protein 50A"
location: "1p36.11"
module: 145
arm: "+"
pooled_cpm: 74.74
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# TMEM50A

*transmembrane protein 50A* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.59× (z +6.2, q 4e-07, up in 29 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.22× (z +3.8, q 0.013, up in 25 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H23 4.17×, C32 3.26×, A549 2.71×, LOX-IMVI 2.35×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.500× (z -9.5, q 1e-18, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.503× (z -4.4, q 0.003, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PINK1]] (+0.71, fdr 7e-06), [[FBXL20]] (+0.68, fdr 1e-05), [[RICTOR]] (+0.68, fdr 1e-05); moves opposite to [[TCERG1]] (-0.61, fdr 2e-05), [[GTF2H3]] (-0.60, fdr 1e-05), [[CRACR2A]] (-0.58, fdr 1e-05).
> It is in [[Module 145]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 10 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11444.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H23 4.17×, C32 3.26×, A549 2.71×, LOX-IMVI 2.35×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.59×** | +6.2 | 4e-07 | 29/42 (NCI-H23, C32, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.52×** | +5.8 | 2e-06 | 32/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.58×** | +5.5 | 6e-06 | 38/49 (J82, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.48×** | +5.4 | 9e-06 | 36/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.39×** | +4.6 | 5e-04 | 35/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.38×** | +4.4 | 8e-04 | 31/48 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.013 | 25/49 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.29×** | +3.4 | 0.045 | 26/47 (NCI-H460, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.27×** | +3.3 | 0.052 | 21/48 (COLO 205, H4, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.28×** | +3.3 | 0.056 | 23/50 (LOX-IMVI, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +3.3 | 0.056 | 26/47 (CFPAC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11444.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.500×** | -9.5 | 1e-18 | 47/48 (AsPC-1, NCI-H460, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.503×** | -4.4 | 0.003 | 34/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.507×** | -4.3 | 0.003 | 31/48 (AsPC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.514×** | -4.2 | 0.003 | 33/48 (hTERT-HPNE, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.911× | -4.0 | 0.006 | 2/49 (SW 1271, SW 1088) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.562×** | -3.7 | 0.023 | 26/48 (A498, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.749×** | -3.5 | 0.044 | 29/48 (A549, BT-474, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.595×** | -3.3 | 0.067 | 24/48 (SNU-1, HCT15, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11444. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 94.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 93.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.17× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.374× (z -9.3) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 63.4 | 0 | 2 (1 ⚠) | — | [[venetoclax (drug)]] 5 µM 0.0453× (z -9.6) |
| [[A-427 (line)]] | wt | 79.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.372× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 83.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.300× (z -11.5) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 85.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[C32 (line)]] | wt | 46.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[HS-578T (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.435× (z -9.4) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 61.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.356× (z -8.7) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 95.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 59.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.238× (z -11.7) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 90.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 52.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.310× (z -11.9) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 97.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.407× (z -9.2) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 68.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 65.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 128 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 91.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 81.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 65.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 53.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11444), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 7 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PINK1]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[FBXL20]] | +0.68 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[RICTOR]] | +0.68 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[GPX4]] | +0.64 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[KLHL24]] | +0.64 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[GARRE1]] | +0.62 | +0.44 / +0.73 | both halves | 3e-05 |  |
| [[MAP3K3]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[GABARAPL2]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[EIF1B]] | +0.62 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[ELF2]] | +0.61 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[RB1CC1]] | +0.61 | +0.39 / +0.68 | both halves | 5e-05 |  |
| [[PDE6D]] | +0.60 | +0.54 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCERG1]] | -0.61 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[GTF2H3]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[CRACR2A]] | -0.58 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[MRPL3]] | -0.57 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[IPO4]] | -0.57 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[MAK16]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[PSPH]] | -0.56 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[TRIM16]] | -0.55 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[CCT2]] | -0.55 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[ZNF202]] | -0.54 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[LARS1]] | -0.54 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[CCT7]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.8, -43.4); signed map (-16.9, 14.3). **Vector** length 92.7, 29.0% of its response variance represented; |z| ≥ 3 in 617 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +5.2 | +5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +4.9 | +4.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +4.8 | +5.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +3.8 | +3.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | -0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | -0.1 |
|  | [[Cyclosporin A (drug)]] 5 µM |  | +1.3 | +1.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.3 | +0.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.9 | -9.5 |
|  | [[EX229 (drug)]] 5 µM |  | -6.3 | -4.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.2 | -4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.9 | -4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.3 | -3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -5.0 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 50A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:25,338,317-25,362,361 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SMP1 |
| Hallmark sets | ANDROGEN_RESPONSE |
| Matched by | ensembl_id |

UniProt [O95807](https://www.uniprot.org/uniprotkb/O95807) carries no function annotation.

**Summary**, from NCBI Gene [23585](https://www.ncbi.nlm.nih.gov/gene/23585):

> This gene is located in the RH gene locus, between the RHD and RHCE genes. The function of its protein product is unknown; however, its sequence has potential transmembrane domains suggesting that it may be an integral membrane protein. Its position between the RH genes suggests that polymorphisms in this gene may be tightly linked to RH haplotypes and may contribute to selective pressure for or against certain RH haplotypes. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:30590](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30590) · Entrez [23585](https://www.ncbi.nlm.nih.gov/gene/23585) · UniProt [O95807](https://www.uniprot.org/uniprotkb/O95807) · Ensembl [ENSG00000183726](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183726)

## Data

Gene col 11444: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11444); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11444, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11444]; `tensor/DDL_lfc|DDL_z.npy` [11444]; `embed/gene_vectors.npy` [11444]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11444 or target_col == 11444). Every well: [[TMEM50A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM50A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
