---
symbol: "PGGT1B"
type: "gene"
col: 8904
ensembl_id: "ENSG00000164219"
name: "protein geranylgeranyltransferase type I subunit beta"
location: "5q22.3"
module: 64
arm: "+"
pooled_cpm: 61.51
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# PGGT1B

*protein geranylgeranyltransferase type I subunit beta* — 5q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.06× (z +10.8, q 2e-24, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.585× (z -21.6, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CUL5]] (+0.73, fdr 7e-06), [[FAM204A]] (+0.70, fdr 7e-06), [[EHHADH]] (+0.69, fdr 1e-05); moves opposite to [[SNX25]] (-0.62, fdr 2e-05), [[RELL1]] (-0.59, fdr 1e-05), [[RCOR1]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8904.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +10.8 | 2e-24 | 36/49 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +6.4 | 5e-08 | 25/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.48×** | +5.8 | 1e-06 | 23/48 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.21×** | +5.2 | 3e-05 | 18/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.13× | +5.1 | 5e-05 | 13/48 (CFPAC-1, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.18× | +4.8 | 2e-04 | 16/48 (Panc 03.27, SW480, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.025 | 13/49 (A498, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.13× | +3.5 | 0.025 | 10/48 (C32, KATO III, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.09× | +3.5 | 0.025 | 2/48 (Panc 03.27, SNU-1) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.09× | +3.5 | 0.025 | 17/48 (A-427, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.13× | +3.4 | 0.040 | 6/48 (LoVo, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.13× | +3.2 | 0.065 | 11/48 (C-33 A, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8904.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.585×** | -21.6 | 0e+00 | 44/49 (NCI-H2347, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.516×** | -18.9 | 0e+00 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.520×** | -18.7 | 0e+00 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.560×** | -16.5 | 0e+00 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.696×** | -9.9 | 4e-21 | 39/50 (COLO 205, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.711×** | -9.7 | 2e-20 | 40/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.742×** | -8.2 | 2e-14 | 32/48 (SW 1271, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.758×** | -7.9 | 2e-13 | 34/48 (KATO III, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.850× | -6.6 | 3e-09 | 17/48 (SW480, CFPAC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | 0.847× | -4.7 | 1e-04 | 19/48 (SW 1271, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | 0.864× | -4.0 | 0.003 | 17/43 (A-427, NCI-H2347, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.773×** | -3.8 | 0.006 | 17/49 (NCI-H460, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | 0.836× | -3.7 | 0.011 | 14/48 (SW 900, HCT15, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.883× | -3.5 | 0.016 | 14/48 (SK-MEL-2, SW 1088, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.923× | -3.3 | 0.043 | 7/48 (COLO 205, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8904. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 88.7 | 4 (3 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.21× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.67× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.391× (z -11.7) |
| [[HOP62 (line)]] | alt | 64.3 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.386× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 70.5 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.408× (z -15.2) |
| [[SW480 (line)]] | alt | 67.5 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 2.50× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.371× (z -18.4) |
| [[PANC-1 (line)]] | alt | 52.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.486× (z -12.2) |
| [[A-427 (line)]] | wt | 66.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.387× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.511× (z -8.5) |
| [[KATO III (line)]] | alt | 46.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.383× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 72.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.397× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 53.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -12.2) |
| [[SNU-423 (line)]] | alt | 52.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -11.0) |
| [[A549 (line)]] | wt | 53.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.400× (z -10.1) |
| [[COLO 205 (line)]] | alt | 85.2 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.400× (z -9.0) |
| [[LoVo (line)]] | wt | 83.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -10.4) |
| [[LS 180 (line)]] | wt | 71.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.464× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 69.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -17.0) |
| [[Panc 03.27 (line)]] | alt | 57.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 91.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -8.8) |
| [[SW 1271 (line)]] | alt | 96.7 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0605× (z -12.2) ⚠ cell-cycle shift, explains ~22% of this change |
| [[A498 (line)]] | wt | 50.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -11.7) |
| [[AsPC-1 (line)]] | alt | 68.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.380× (z -10.5) |
| [[C32 (line)]] | wt | 50.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 61.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.459× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 69.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -9.1) |
| [[Hs 766T (line)]] | wt | 56.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -15.5) |
| [[HS-578T (line)]] | alt | 55.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.466× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~24% of this change |
| [[HT-29 (line)]] | alt | 57.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -12.1) |
| [[hTERT-HPNE (line)]] | wt | 51.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -12.4) |
| [[J82 (line)]] | alt | 39.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 46.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -8.5) |
| [[RKO (line)]] | wt | 63.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -13.2) |
| [[A-172 (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 102 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 74.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 74.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 87.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8904), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CUL5]] | +0.73 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[FAM204A]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[EHHADH]] | +0.69 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[SCRN3]] | +0.68 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[TMEM128]] | +0.67 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[RBM45]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[RBM41]] | +0.66 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[MTPAP]] | +0.65 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[CC2D2A]] | +0.65 | +0.36 / +0.66 | both halves | 9e-05 |  |
| [[COPS5]] | +0.65 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[NUDT9]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[KRT10-AS1]] | +0.64 | +0.54 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX25]] | -0.62 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[RELL1]] | -0.59 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[RCOR1]] | -0.58 | -0.51 / -0.49 | both halves | 2e-05 |  |
| [[CTBP2]] | -0.57 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[SRGAP2]] | -0.57 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[MAPKAPK2]] | -0.56 | -0.41 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PGGT1B's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises PGGT1B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.632). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-22.4, 3.7); signed map (9.1, -32.6). **Vector** length 91.3, 20.7% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +8.0 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.0 | +6.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.9 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.2 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.6 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.1 | +1.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.3 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -21.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.9 | -7.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.5 | -16.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -9.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.1 | -9.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.6 | -0.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.5 | -0.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -1.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | protein geranylgeranyltransferase type I subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.3 — chr5:115,204,012-115,262,877 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GGTI, BGGI |
| Gene groups (HGNC) | Protein geranylgeranyltransferase type I subunits |
| Reactome | 5 pathways, smallest: OAS antiviral response; GBP-mediated host defense; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P53609](https://www.uniprot.org/uniprotkb/P53609) (Geranylgeranyl transferase type-1 subunit beta):

> Catalyzes the transfer of a geranyl-geranyl moiety from geranyl-geranyl pyrophosphate to a cysteine at the fourth position from the C-terminus of proteins having the C-terminal sequence Cys-aliphatic-aliphatic-X. Known substrates include RAC1, RAC2, RAP1A and RAP1B.

**Summary**, from NCBI Gene [5229](https://www.ncbi.nlm.nih.gov/gene/5229):

> Protein geranylgeranyltransferase type I (GGTase-I) transfers a geranylgeranyl group to the cysteine residue of candidate proteins containing a C-terminal CAAX motif in which 'A' is an aliphatic amino acid and 'X' is leucine (summarized by Zhang et al., 1994 [PubMed 8106351]). The enzyme is composed of a 48-kD alpha subunit (FNTA; MIM 134635) and a 43-kD beta subunit, encoded by the PGGT1B gene. The FNTA gene encodes the alpha subunit for both GGTase-I and the related enzyme …

**Accessions** — [HGNC:8895](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8895) · Entrez [5229](https://www.ncbi.nlm.nih.gov/gene/5229) · UniProt [P53609](https://www.uniprot.org/uniprotkb/P53609) · Ensembl [ENSG00000164219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164219)

## Data

Gene col 8904: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8904); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8904, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8904]; `tensor/DDL_lfc|DDL_z.npy` [8904]; `embed/gene_vectors.npy` [8904]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8904 or target_col == 8904). Every well: [[PGGT1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGGT1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
