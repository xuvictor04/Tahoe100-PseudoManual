---
symbol: "OSMR"
type: "gene"
col: 7008
ensembl_id: "ENSG00000145623"
name: "oncostatin M receptor"
location: "5p13.1"
module: 13
arm: "+"
pooled_cpm: 304.68
n_lines_expressing: 37
n_dd_up: 0
n_dd_down: 44
n_dd_up_clean: 0
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 9
direction_downstream: 6
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# OSMR

*oncostatin M receptor* — 5p13.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.258× (z -25.8, q 0e+00, down in 35 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OSMR-DT]] (+0.72, fdr 7e-06, ⚠ same locus), [[CCDC71L]] (+0.61, fdr 2e-05), [[ZNF281]] (+0.59, fdr 1e-05), [[LINC02015]] (+0.58, fdr 2e-05); moves opposite to [[WDSUB1]] (-0.53, fdr 1e-05), [[PREPL]] (-0.51, fdr 3e-05), [[SORL1]] (-0.51, fdr 2e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[RAI14]] → it (grade B ⚠); 6 go from it, the strongest it → [[RAI14]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7008.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.25× | +3.0 | 0.95 | 19/35 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 20 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7008.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.258×** | -25.8 | 0e+00 | 35/35 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.339×** | -14.6 | 1e-45 | 35/35 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.314×** | -14.1 | 7e-43 | 35/35 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.388×** | -12.8 | 4e-35 | 31/35 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.399×** | -12.4 | 4e-33 | 35/35 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.416×** | -11.8 | 3e-30 | 35/35 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.401×** | -11.1 | 9e-27 | 30/34 (SW 900, H4, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.410×** | -10.9 | 1e-25 | 33/34 (RPMI-7951, BT-474, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.572×** | -10.6 | 2e-24 | 32/36 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.472×** | -10.1 | 3e-22 | 30/35 (NCI-H460, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.501×** | -9.3 | 8e-19 | 33/35 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.633×** | -8.7 | 2e-16 | 31/35 (BT-474, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.568×** | -7.6 | 1e-12 | 28/35 (BT-474, C32, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.568×** | -7.6 | 1e-12 | 34/35 (BT-474, HepG2/C3A, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.694×** | -6.9 | 2e-10 | 31/36 (BT-474, C32, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.710×** | -6.5 | 3e-09 | 29/36 (BT-474, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.647×** | -5.9 | 2e-07 | 26/35 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.437×** | -5.8 | 2e-07 | 32/34 (BT-474, NCI-H23, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.453×** | -5.6 | 7e-07 | 23/35 (C32, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | **0.499×** | -4.9 | 2e-05 | 28/35 (NCI-H23, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.698×** | -4.8 | 3e-05 | 27/35 (BT-474, C32, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.709×** | -4.6 | 8e-05 | 29/36 (BT-474, HepG2/C3A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7008. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 342 | 0 | 34 (15 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -27.2) |
| [[NCI-H460 (line)]] | wt | 413 | 0 | 18 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -39.5) |
| [[C32 (line)]] | wt | 450 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -29.1) |
| [[H4 (line)]] | wt | 593 | 0 | 15 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -20.2) |
| [[HepG2_C3A (line)]] | wt | 331 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -31.5) |
| [[LOX-IMVI (line)]] | wt | 306 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -26.0) |
| [[NCI-H1573 (line)]] | alt | 819 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0597× (z -31.9) |
| [[NCI-H23 (line)]] | alt | 662 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -17.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.303× (z -15.6) |
| [[SW 900 (line)]] | alt | 631 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -25.0) |
| [[HOP62 (line)]] | alt | 361 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -15.6) |
| [[hTERT-HPNE (line)]] | wt | 475 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -13.4) |
| [[J82 (line)]] | alt | 490 | 0 | 9 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.429× (z -14.5) |
| [[NCI-H1792 (line)]] | alt | 870 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -21.7) |
| [[A549 (line)]] | wt | 663 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -22.6) |
| [[KATO III (line)]] | alt | 123 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -22.5) |
| [[RPMI-7951 (line)]] | alt | 249 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -24.8) |
| [[SNU-1 (line)]] | wt | 240 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -16.1) |
| [[Hs 766T (line)]] | wt | 533 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -21.4) |
| [[MIA PaCa-2 (line)]] | alt | 227 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -13.6) |
| [[NCI-H2030 (line)]] | alt | 483 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -23.3) |
| [[PANC-1 (line)]] | alt | 239 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -19.5) |
| [[AsPC-1 (line)]] | alt | 409 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -14.5) |
| [[CFPAC-1 (line)]] | alt | 526 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -15.4) |
| [[Panc 03.27 (line)]] | alt | 413 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -20.1) |
| [[SNU-423 (line)]] | alt | 283 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.282× (z -10.7) |
| [[SW 1271 (line)]] | alt | 581 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -13.0) |
| [[A-427 (line)]] | wt | 188 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -14.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.199× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 335 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -21.8) |
| [[A-172 (line)]] | wt | 315 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -12.3) |
| [[A498 (line)]] | wt | 346 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -15.3) |
| [[SW 1088 (line)]] | alt | 257 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0489× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.263× (z -9.2) |
| [[CHP-212 (line)]] | wt | 85.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -13.1) |
| [[HS-578T (line)]] | alt | 489 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -15.1) |
| [[SK-MEL-2 (line)]] | alt | 96.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -10.3) |
| [[AN3 CA (line)]] | alt | 107 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 23.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 25.8 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 23.9 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 29.9 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 25.2 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 23.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 389 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 259 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.8 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 25.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 22.6 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 28.8 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 22.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7008), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSMR-DT]] | +0.72 | +0.82 / +0.70 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CCDC71L]] | +0.61 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[ZNF281]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[LINC02015]] | +0.58 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[SERPINB4]] | +0.57 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[ELL2]] | +0.57 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[GLIS3]] | +0.56 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[SERPINB3]] | +0.56 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[MAP3K20]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[RAB31]] | +0.55 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[TFPI]] | +0.54 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[IL4R]] | +0.54 | +0.48 / +0.59 | both halves | 2e-05 | pathway: HALLMARK_IL6_JAK_STAT3_SIGNALING |
| [[STRIP2]] | +0.54 | +0.44 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDSUB1]] | -0.53 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[PREPL]] | -0.51 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[SORL1]] | -0.51 | -0.59 / -0.47 | both halves | 2e-05 | same gene group |
| [[PPFIBP2]] | -0.50 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[NHLRC3]] | -0.50 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[RAVER2]] | -0.50 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[BMP7]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[TRIM2]] | -0.49 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[RNF43]] | -0.48 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[PIK3C2B]] | -0.48 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[SLC43A1]] | -0.48 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ABO]] | -0.47 | -0.54 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAI14]] | B | RAI14 activity raises OSMR's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 4.57× lower at baseline in the lines without RAI14 | 5e-04 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[C11orf91]] | B | C11orf91 activity raises OSMR's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 4.08× lower at baseline in the lines without C11orf91 | 0.002 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[CD59]] | B | CD59 activity raises OSMR's level | lines that do not express CD59 (7) vs lines expressing it (43) | 3.43× lower at baseline in the lines without CD59 | 0.007 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[CCDC71L]] | B | CCDC71L activity raises OSMR's level | lines that do not express CCDC71L (8) vs lines expressing it (42) | 3.41× lower at baseline in the lines without CCDC71L | 0.008 | ⚠ within organs, on part of the lines; also absent: RAI14, VIM-AS1, ENSG00000243797; maybe low, not absent |
| [[RHCG]] | B | RHCG activity raises OSMR's level | lines that do not express RHCG (33) vs lines expressing it (17) | 4.37× lower at baseline in the lines without RHCG | 0.026 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[IL1RAP]] | B | IL1RAP activity raises OSMR's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 3.71× lower at baseline in the lines without IL1RAP | 0.063 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[ELL2]] | B | ELL2 activity raises OSMR's level | lines that do not express ELL2 (12) vs lines expressing it (38) | 4.12× lower at baseline in the lines without ELL2 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent |
| [[HRH1]] | B | HRH1 activity raises OSMR's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 2.22× lower at baseline in the lines without HRH1 | 0.092 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[OSMR-DT]] | C | OSMR-DT activity raises OSMR's level | lines that do not express OSMR-DT (15) vs lines expressing it (35) | 11.12× lower at baseline in the lines without OSMR-DT | 5e-05 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: OSMR, LIFR, IL1R1; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAI14]] | B | OSMR activity raises RAI14's level | lines that do not express OSMR (13) vs lines expressing it (37) | 3.50× lower at baseline in the lines without OSMR | 0.060 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A, APC, SETD1B; also absent: OSMR-DT, LIFR, IL1R1; its own permutation p |
| [[IL4R]] | B | OSMR activity raises IL4R's level | lines that do not express OSMR (13) vs lines expressing it (37) | 1.23× lower at baseline in the lines without OSMR | 0.060 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A, APC, SETD1B; also absent: OSMR-DT, LIFR, IL1R1; its own permutation p |
| [[CD59]] | B | OSMR activity raises CD59's level | lines that do not express OSMR (13) vs lines expressing it (37) | 2.41× lower at baseline in the lines without OSMR | 0.063 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A, APC, SETD1B; also absent: OSMR-DT, LIFR, IL1R1 |
| [[ZNF281]] | B | OSMR activity raises ZNF281's level | lines that do not express OSMR (13) vs lines expressing it (37) | 1.59× lower at baseline in the lines without OSMR | 0.076 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A, APC, SETD1B; also absent: OSMR-DT, LIFR, IL1R1 |
| [[MAP3K20]] | B | OSMR activity raises MAP3K20's level | lines that do not express OSMR (13) vs lines expressing it (37) | 1.24× lower at baseline in the lines without OSMR | 0.081 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A, APC, SETD1B; also absent: OSMR-DT, LIFR, IL1R1 |
| [[OSMR-DT]] | C | OSMR activity raises OSMR-DT's level | lines that do not express OSMR (13) vs lines expressing it (37) | 11.71× lower at baseline in the lines without OSMR | 0.060 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A, APC, SETD1B; also absent: OSMR-DT, LIFR, IL1R1; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.296). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.3, 8.4); signed map (10.8, 24.8). **Vector** length 111, 42.1% of its response variance represented; |z| ≥ 3 in 1,330 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | -0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | -1.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | -0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.2 | +0.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +1.9 | +2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +1.3 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -6.8 | -7.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.9 | -8.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.2 | -4.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.1 | -6.5 |
|  | [[NG25 (drug)]] 5 µM |  | -4.7 | -5.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.6 | -6.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.4 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | oncostatin M receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.1 — chr5:38,845,858-38,945,596 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OSMRB, OSMRbeta |
| Gene groups (HGNC) | Fibronectin type III domain containing |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, INFLAMMATORY_RESPONSE |
| Reactome | 4 pathways, smallest: IL-6-type cytokine receptor ligand interactions; Interleukin-6 family signaling; Signaling by Interleukins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99650](https://www.uniprot.org/uniprotkb/Q99650) (Oncostatin-M-specific receptor subunit beta):

> Functions as a shared membrane-bound signal-transducing subunit in two distinct receptor complexes, the type II OSM receptor (heterodimer composed of OSMR and IL6ST) and the IL31 receptor complex (heterodimer composed of OSMR and IL31RA) which respectively bind OSM and IL31. Functionally, OSM signaling via OSMR/IL6ST regulates many processes including cell proliferation, cell differentiation, cytokine production, whereas the IL31 signaling via OSMR/IL31RA is particularly important in skin …

**Summary**, from NCBI Gene [9180](https://www.ncbi.nlm.nih.gov/gene/9180):

> This gene encodes a member of the type I cytokine receptor family. The encoded protein heterodimerizes with interleukin 6 signal transducer to form the type II oncostatin M receptor and with interleukin 31 receptor A to form the interleukin 31 receptor, and thus transduces oncostatin M and interleukin 31 induced signaling events. Mutations in this gene have been associated with familial primary localized cutaneous amyloidosis. Alternatively spliced transcript variants encoding different …

**Accessions** — [HGNC:8507](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8507) · Entrez [9180](https://www.ncbi.nlm.nih.gov/gene/9180) · UniProt [Q99650](https://www.uniprot.org/uniprotkb/Q99650) · Ensembl [ENSG00000145623](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145623)

## Data

Gene col 7008: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7008); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7008, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7008]; `tensor/DDL_lfc|DDL_z.npy` [7008]; `embed/gene_vectors.npy` [7008]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7008 or target_col == 7008). Every well: [[OSMR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSMR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
