---
symbol: "CDH4"
type: "gene"
col: 11014
ensembl_id: "ENSG00000179242"
name: "cadherin 4"
location: "20q13.33"
module: 193
arm: "+"
pooled_cpm: 21.04
n_lines_expressing: 18
n_dd_up: 35
n_dd_down: 12
n_dd_up_clean: 23
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/193"]
generated_by: "tahoemap"
---

# CDH4

*cadherin 4* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.36× (z +27.2, q 0e+00, up in 10 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Binimetinib (drug)]] 5 µM: 0.643× (z -5.8, q 4e-06, down in 13 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THSD4]] (+0.68, fdr 7e-06), [[SLC35F3]] (+0.64, fdr 7e-06), [[NR2E3]] (+0.61, fdr 1e-05); moves opposite to [[TENT2]] (-0.48, fdr 4e-05), [[TCTN2]] (-0.47, fdr 4e-05), [[C1R]] (-0.46, fdr 8e-05).
> It is in [[Module 193]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 4 go from it, the strongest it → [[AMOTL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11014.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.36×** | +27.2 | 0e+00 | 10/16 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.33×** | +19.1 | 0e+00 | 6/15 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.67×** | +18.1 | 0e+00 | 7/16 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.17×** | +17.9 | 0e+00 | 7/14 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.00×** | +16.7 | 0e+00 | 6/14 (SW1417, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.17×** | +14.3 | 3e-44 | 10/16 (SW1417, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.97×** | +8.9 | 7e-17 | 10/15 (A-172, A-427, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.95×** | +8.7 | 2e-16 | 10/15 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +7.9 | 2e-13 | 9/15 (A-172, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +7.1 | 7e-11 | 7/15 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +7.0 | 1e-10 | 10/15 (hTERT-HPNE, A-172, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +6.8 | 5e-10 | 12/15 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.66×** | +6.6 | 2e-09 | 10/15 (A-172, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +5.9 | 2e-07 | 7/15 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.59×** | +5.8 | 2e-07 | 4/15 (hTERT-HPNE, A-172, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.35×** | +5.6 | 9e-07 | 11/16 (A-172, H4, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +5.2 | 5e-06 | 13/15 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.8 | 5e-05 | 3/16 (hTERT-HPNE, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +4.3 | 4e-04 | 4/15 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[vincristine (drug)]] 5 µM |  | **1.77×** | +3.8 | 0.003 | 7/14 (A-172, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.004 | 0/15 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.005 | 4/15 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.006 | 11/15 (H4, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11014.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Binimetinib (drug)]] 5 µM |  | **0.643×** | -5.8 | 4e-06 | 13/16 (A-427, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.711×** | -5.5 | 1e-05 | 11/16 (NCI-H23, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.671×** | -5.2 | 3e-05 | 11/15 (NCI-H23, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.691×** | -4.9 | 2e-04 | 10/16 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.706×** | -4.6 | 5e-04 | 8/15 (NCI-H23, HOP62, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.697×** | -4.4 | 0.001 | 6/15 (HOP62, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.810×** | -3.9 | 0.009 | 6/16 (HOP62, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.740×** | -3.8 | 0.009 | 10/15 (NCI-H23, HOP62, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -3.6 | 0.018 | 2/16 (HOP62, NCI-H23) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.791×** | -3.6 | 0.019 | 9/16 (HOP62, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.824×** | -3.6 | 0.019 | 3/16 (HOP62, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.772×** | -3.2 | 0.059 | 7/15 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.778×** | -3.2 | 0.065 | 9/15 (NCI-H23, HOP62, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11014. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 93.6 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0860× (z -20.2) |
| [[A-172 (line)]] | wt | 24.9 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.51× (z +17.0) | — |
| [[HOP62 (line)]] | alt | 53.7 | 4 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +12.9) | [[Adagrasib (drug)]] 0.05 µM 0.505× (z -14.6) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.243× (z -9.2) |
| [[A-427 (line)]] | wt | 52.1 | 0 | 3 (2 ⚠) | — | [[Binimetinib (drug)]] 5 µM 0.134× (z -10.8) |
| [[A498 (line)]] | wt | 7.18 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.47× (z +13.2) | [[Selinexor (drug)]] 5 µM 0.244× (z -9.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[hTERT-HPNE (line)]] | wt | 21.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.63× (z +11.5) | — |
| [[NCI-H2030 (line)]] | alt | 226 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -11.3) |
| [[A549 (line)]] | wt | 153 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -8.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +9.7) | — |
| [[H4 (line)]] | wt | 24.2 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 5.70× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 26.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.139× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[SNU-423 (line)]] | alt | 38.2 | 1 | 0 | [[Panobinostat (drug)]] 0.05 µM 5.63× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 22.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.53× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.11 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.04 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11014), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THSD4]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[SLC35F3]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[NR2E3]] | +0.61 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[BMP6]] | +0.61 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[B4GALT6]] | +0.60 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[SRPK1]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ASAP2]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[DOCK4]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[MAMLD1]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[SHANK2]] | +0.57 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[ANKRD44]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[AGO2]] | +0.57 | +0.61 / +0.51 | both halves | 1e-05 | pathway: Adherens junctions interactions |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TENT2]] | -0.48 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[TCTN2]] | -0.47 | -0.56 / -0.43 | both halves | 4e-05 |  |
| [[C1R]] | -0.46 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[CCS]] | -0.46 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[OSCP1]] | -0.46 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[DNAJC27]] | -0.45 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[TMED1]] | -0.44 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[GPATCH1]] | -0.44 | -0.43 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises CDH4's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.1% of all compounds | 0.013 | ⚠ off-target possible; 3 compounds |
| [[MAP2K2]] | B | MAP2K2 activity raises CDH4's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |
| [[TOP2A]] | B | TOP2A activity lowers CDH4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[UNC13A]] | C | UNC13A activity raises CDH4's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 3.04× lower at baseline in the lines without UNC13A | 0.061 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AMOTL1]] | B | CDH4 activity raises AMOTL1's level | lines that do not express CDH4 (32) vs lines expressing it (18) | 2.22× lower at baseline in the lines without CDH4 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, UCHL1, SIRLNT |
| [[MBP]] | B | CDH4 activity lowers MBP's level | lines that do not express CDH4 (32) vs lines expressing it (18) | 1.58× higher at baseline in the lines without CDH4 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, UCHL1, SIRLNT |
| [[MARCHF4]] | C | CDH4 activity raises MARCHF4's level | lines that do not express CDH4 (32) vs lines expressing it (18) | 4.12× lower at baseline in the lines without CDH4 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, UCHL1, SIRLNT; co-absent with the target |
| [[FHL1]] | C | CDH4 activity raises FHL1's level | lines that do not express CDH4 (32) vs lines expressing it (18) | 3.07× lower at baseline in the lines without CDH4 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, UCHL1, SIRLNT; co-absent with the target |

## Where it sits

- **Module**: [[Module 193]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.798). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.8, 8.7); signed map (8.6, 43.9). **Vector** length 64.4, 19.2% of its response variance represented; |z| ≥ 3 in 581 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +19.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +17.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +16.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +5.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.8 | +1.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.3 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -5.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.8 | -3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | cadherin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:61,252,261-61,940,617 (+) |
| Ensembl biotype | protein_coding |
| Also known as | R-CAD |
| Gene groups (HGNC) | Type I classical cadherins |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 5 pathways, smallest: Myogenesis; Adherens junctions interactions; Cell-cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P55283](https://www.uniprot.org/uniprotkb/P55283) (Cadherin-4):

> Cadherins are calcium-dependent cell adhesion proteins. They preferentially interact with themselves in a homophilic manner in connecting cells; cadherins may thus contribute to the sorting of heterogeneous cell types. May play an important role in retinal development.

**Summary**, from NCBI Gene [1002](https://www.ncbi.nlm.nih.gov/gene/1002):

> This gene is a classical cadherin from the cadherin superfamily. The encoded protein is a calcium-dependent cell-cell adhesion glycoprotein comprised of five extracellular cadherin repeats, a transmembrane region and a highly conserved cytoplasmic tail. Based on studies in chicken and mouse, this cadherin is thought to play an important role during brain segmentation and neuronal outgrowth. In addition, a role in kidney and muscle development is indicated. Of particular interest are studies …

**Accessions** — [HGNC:1763](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1763) · Entrez [1002](https://www.ncbi.nlm.nih.gov/gene/1002) · UniProt [P55283](https://www.uniprot.org/uniprotkb/P55283) · Ensembl [ENSG00000179242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179242)

## Data

Gene col 11014: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11014); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11014, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11014]; `tensor/DDL_lfc|DDL_z.npy` [11014]; `embed/gene_vectors.npy` [11014]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11014 or target_col == 11014). Every well: [[CDH4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDH4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
