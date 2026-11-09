---
symbol: "AFF3"
type: "gene"
col: 6854
ensembl_id: "ENSG00000144218"
name: "ALF transcription elongation factor 3"
location: "2q11.2"
module: 13
arm: "+"
pooled_cpm: 75.7
n_lines_expressing: 28
n_dd_up: 7
n_dd_down: 62
n_dd_up_clean: 7
n_dd_down_clean: 39
in_vector_space: true
direction_upstream: 19
direction_downstream: 23
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# AFF3

*ALF transcription elongation factor 3* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.43× (z +7.6, q 2e-11, up in 14 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 62 drug-doses (23 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.385× (z -14.2, q 6e-43, down in 23 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INSYN2B]] (+0.69, fdr 7e-06), [[KCNMA1]] (+0.69, fdr 7e-06), [[FRMD4A]] (+0.68, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[MEG3]] → it (grade B ⚠); 23 go from it, the strongest it → [[CNIH3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6854.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +7.6 | 2e-11 | 14/26 (NCI-H460, A-427, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +6.4 | 4e-08 | 14/26 (NCI-H460, C-33 A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +6.3 | 6e-08 | 16/26 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.41×** | +5.1 | 4e-05 | 13/26 (H4, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.8 | 2e-04 | 11/26 (A-172, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.19× | +3.8 | 0.015 | 13/26 (J82, A498, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.080 | 10/26 (C-33 A, hTERT-HPNE, …) | top dose only |  |
| [[Dabrafenib (drug)]] 5 µM |  | **1.51×** | +3.2 | 0.094 | 9/27 (C32, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rifaximin (drug)]] 5 µM |  | 1.24× | +3.1 | 0.14 | 9/26 (A-172, NCI-H23, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 65 in all, 23 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 62 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6854.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.385×** | -14.2 | 6e-43 | 23/26 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.378×** | -13.9 | 2e-41 | 20/25 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.480×** | -10.9 | 2e-25 | 20/26 (HOP62, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.473×** | -9.8 | 2e-20 | 19/26 (HOP62, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.520×** | -9.7 | 3e-20 | 20/26 (SNU-423, A-172, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.523×** | -9.6 | 6e-20 | 18/26 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.545×** | -9.0 | 1e-17 | 21/26 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.555×** | -8.7 | 2e-16 | 18/26 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.560×** | -8.6 | 4e-16 | 20/26 (HOP62, A-172, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.565×** | -8.5 | 1e-15 | 18/26 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.675×** | -8.2 | 9e-15 | 16/26 (hTERT-HPNE, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.581×** | -8.1 | 3e-14 | 21/26 (H4, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.565×** | -7.9 | 2e-13 | 17/25 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.594×** | -7.7 | 4e-13 | 20/26 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.693×** | -7.7 | 5e-13 | 18/26 (NCI-H23, SNU-423, …) | top dose only |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.597×** | -7.7 | 6e-13 | 17/26 (H4, HOP62, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.586×** | -7.6 | 7e-13 | 19/26 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.621×** | -7.1 | 4e-11 | 17/26 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.632×** | -6.8 | 3e-10 | 17/26 (HOP62, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.637×** | -6.7 | 5e-10 | 19/26 (SW 1088, A498, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.658×** | -6.2 | 1e-08 | 18/26 (HOP62, H4, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.48 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6854. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 328 | 0 | 30 (12 ⚠) | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.102× (z -16.6) |
| [[A-172 (line)]] | wt | 335 | 5 (2 ⚠) | 13 (11 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +21.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.17× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.0878× (z -25.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.361× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 368 | 0 | 18 (7 ⚠) | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.190× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 491 | 0 | 18 (13 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -25.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.296× (z -12.8) |
| [[SNU-423 (line)]] | alt | 373 | 1 (1 ⚠) | 15 (10 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +13.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -19.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.346× (z -10.7) |
| [[Hs 766T (line)]] | wt | 75.4 | 1 (1 ⚠) | 11 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.76× (z +20.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -14.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Betamethasone dipropionate (drug)]] 5 µM 0.206× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 78.5 | 0 | 12 (10 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.481× (z -17.1) ⚠ position not correctable · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.272× (z -8.6) |
| [[H4 (line)]] | wt | 68.0 | 0 | 10 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0693× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.167× (z -9.8) |
| [[PANC-1 (line)]] | alt | 60.6 | 0 | 9 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -12.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.263× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 188 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.347× (z -10.2) |
| [[C32 (line)]] | wt | 52.2 | 2 | 4 (4 ⚠) | [[Cobimetinib (drug)]] 0.5 µM 4.27× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.215× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[J82 (line)]] | alt | 102 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.186× (z -13.4) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.339× (z -8.9) |
| [[A498 (line)]] | wt | 69.0 | 0 | 4 | — | [[Triamcinolone (drug)]] 5 µM 0.451× (z -9.6) |
| [[SW 1088 (line)]] | alt | 199 | 0 | 4 (1 ⚠) | — | [[Triamcinolone (drug)]] 0.5 µM 0.0219× (z -13.9) |
| [[RPMI-7951 (line)]] | alt | 95.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.79× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 39.1 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.289× (z -9.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[C-33 A (line)]] | alt | 57.7 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -10.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H460 (line)]] | wt | 44.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.85× (z +11.0) | — |
| [[RKO (line)]] | wt | 69.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.174× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 37.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.81× (z +10.6) | — |
| [[A549 (line)]] | wt | 13.0 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.92 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 229 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.80 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.58 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.75 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.32 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 141 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.97 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.05 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.75 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.98 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.48 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 14.8 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.32 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.19 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.24 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.01 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.95 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.39 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.34 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 14.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6854), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INSYN2B]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[KCNMA1]] | +0.69 | +0.59 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[FRMD4A]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[LINC00973]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[IL11]] | +0.64 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[MSANTD3]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[ADAMTS16]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[TRAF1]] | +0.64 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[GDNF]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[SYNJ2]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[GPR68]] | +0.63 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[GRIN2A]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 1, C 18. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEG3]] | B | MEG3 activity raises AFF3's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 3.39× lower at baseline in the lines without MEG3 | 0.098 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8 |
| [[ROBO4]] | C | ROBO4 activity raises AFF3's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 4.79× lower at baseline in the lines without ROBO4 | 0.005 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1; co-absent with the target |
| [[BNC2]] | C | BNC2 activity raises AFF3's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 5.79× lower at baseline in the lines without BNC2 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182; co-absent with the target |
| [[FGF5]] | C | FGF5 activity raises AFF3's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 5.38× lower at baseline in the lines without FGF5 | 0.023 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises AFF3's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 4.73× lower at baseline in the lines without CDH13 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[GDNF]] | C | GDNF activity raises AFF3's level | lines that do not express GDNF (38) vs lines expressing it (12) | 4.67× lower at baseline in the lines without GDNF | 0.029 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[GDNF-AS1]] | C | GDNF-AS1 activity raises AFF3's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 4.42× lower at baseline in the lines without GDNF-AS1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent; co-absent with the target |
| [[ZNF385D]] | C | ZNF385D activity raises AFF3's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 3.68× lower at baseline in the lines without ZNF385D | 0.043 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |
| [[SPOCK1]] | C | SPOCK1 activity raises AFF3's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 4.11× lower at baseline in the lines without SPOCK1 | 0.046 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |
| [[CSMD2]] | C | CSMD2 activity raises AFF3's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 3.99× lower at baseline in the lines without CSMD2 | 0.048 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises AFF3's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 5.72× lower at baseline in the lines without LINC01411 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[KIRREL3]] | C | KIRREL3 activity raises AFF3's level | lines that do not express KIRREL3 (36) vs lines expressing it (14) | 4.70× lower at baseline in the lines without KIRREL3 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 14, C 9. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNIH3]] | B | AFF3 activity raises CNIH3's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 3.22× lower at baseline in the lines without AFF3 | 0.002 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| [[ITPR1]] | B | AFF3 activity raises ITPR1's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 4.64× lower at baseline in the lines without AFF3 | 0.003 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| [[TMEFF1]] | B | AFF3 activity raises TMEFF1's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 2.53× lower at baseline in the lines without AFF3 | 0.007 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| [[FMNL3]] | B | AFF3 activity raises FMNL3's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 3.19× lower at baseline in the lines without AFF3 | 0.008 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| [[FGD4]] | B | AFF3 activity lowers FGD4's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 3.27× higher at baseline in the lines without AFF3 | 0.009 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| [[FAM135A]] | B | AFF3 activity lowers FAM135A's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 2.18× higher at baseline in the lines without AFF3 | 0.013 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| [[MSANTD3]] | B | AFF3 activity raises MSANTD3's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 1.87× lower at baseline in the lines without AFF3 | 0.039 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| [[AMPD3]] | B | AFF3 activity raises AMPD3's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 1.90× lower at baseline in the lines without AFF3 | 0.048 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| cells under [[Doxorubicin (hydrochloride) (drug)]] 5 µM | B | AFF3 activity lowers the cells' numbers under Doxorubicin (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express AFF3 (22) vs lines expressing it (26) | the lines without AFF3: 1.61× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| [[SCARF1]] | B | AFF3 activity raises SCARF1's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 1.30× lower at baseline in the lines without AFF3 | 0.060 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | AFF3 activity raises the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (protects the cells) | lines that do not express AFF3 (22) vs lines expressing it (26) | the lines without AFF3: 0.86× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| [[NOTCH2]] | B | AFF3 activity raises NOTCH2's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 2.04× lower at baseline in the lines without AFF3 | 0.095 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.2, 15.9); signed map (21.1, 48.3). **Vector** length 128, 39.0% of its response variance represented; |z| ≥ 3 in 1,232 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.4 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +7.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | +4.5 | -6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | -2.9 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -5.5 | -9.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -5.2 | -5.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -5.0 | -7.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -4.9 | -7.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.8 | -6.7 |

## What is on record

|  |  |
|---|---|
| Name | ALF transcription elongation factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:99,545,419-100,192,428 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MLLT2-like; previously LAF4 |
| Gene groups (HGNC) | AF4/FMR2 family; Super elongation complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P51826](https://www.uniprot.org/uniprotkb/P51826) (AF4/FMR2 family member 3):

> Putative transcription activator that may function in lymphoid development and oncogenesis. Binds, in vitro, to double-stranded DNA.

**Summary**, from NCBI Gene [3899](https://www.ncbi.nlm.nih.gov/gene/3899):

> This gene encodes a tissue-restricted nuclear transcriptional activator that is preferentially expressed in lymphoid tissue. Isolation of this protein initially defined a highly conserved LAF4/MLLT2 gene family of nuclear transcription factors that may function in lymphoid development and oncogenesis. In some ALL patients, this gene has been found fused to the gene for MLL. Multiple alternatively spliced transcript variants that encode different proteins have been found for this gene. [provided …

**Accessions** — [HGNC:6473](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6473) · Entrez [3899](https://www.ncbi.nlm.nih.gov/gene/3899) · UniProt [P51826](https://www.uniprot.org/uniprotkb/P51826) · Ensembl [ENSG00000144218](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144218)

## Data

Gene col 6854: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6854); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6854, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6854]; `tensor/DDL_lfc|DDL_z.npy` [6854]; `embed/gene_vectors.npy` [6854]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6854 or target_col == 6854). Every well: [[AFF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AFF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
