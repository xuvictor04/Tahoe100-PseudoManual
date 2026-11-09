---
symbol: "PTGS1"
type: "gene"
col: 1740
ensembl_id: "ENSG00000095303"
name: "prostaglandin-endoperoxide synthase 1"
location: "9q33.2"
module: 84
arm: "+"
pooled_cpm: 8.35
n_lines_expressing: 24
n_dd_up: 15
n_dd_down: 19
n_dd_up_clean: 6
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 4
direction_downstream: 11
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# PTGS1

*prostaglandin-endoperoxide synthase 1* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.24× (z +10.2, q 9e-22, up in 12 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.414× (z -7.9, q 2e-12, down in 14 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAEP]] (+0.68, fdr 7e-06), [[RAC2]] (+0.68, fdr 7e-06), [[ATP2C2]] (+0.63, fdr 1e-05); moves opposite to [[EFCAB2]] (-0.54, fdr 2e-04), [[CLIP1]] (-0.53, fdr 3e-05), [[ARID1B]] (-0.53, fdr 5e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PRAG1]] → it (grade B ⚠); 11 go from it, the strongest it → [[ADSS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1740.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.24×** | +10.2 | 9e-22 | 12/20 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.13×** | +6.8 | 4e-09 | 13/20 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.08×** | +6.6 | 1e-08 | 11/21 (LS 180, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.65×** | +6.3 | 3e-08 | 3/20 (LoVo, NCI-H460, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.79×** | +5.2 | 2e-05 | 0/15 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.82×** | +5.2 | 2e-05 | 0/8 | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +4.7 | 3e-04 | 10/21 (NCI-H460, LS 180, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.67×** | +4.2 | 0.002 | 1/11 (hTERT-HPNE) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +3.8 | 0.009 | 8/21 (NCI-H460, LS 180, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.52×** | +3.8 | 0.010 | 8/21 (SW1417, LS 180, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.024 | 1/20 (BT-474) | top dose only | cell-cycle shift (explains ~11% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.67×** | +3.3 | 0.047 | 1/11 (CFPAC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.43×** | +3.2 | 0.057 | 1/15 (hTERT-HPNE) | all doses, flat | composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +3.1 | 0.068 | 0/10 | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.90×** | +3.0 | 0.099 | 1/9 (HEC-1-A) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1740.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.414×** | -7.9 | 2e-12 | 14/20 (HOP62, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.456×** | -6.5 | 3e-08 | 10/20 (SHP-77, HEC-1-A, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.503×** | -6.1 | 2e-07 | 18/21 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.535×** | -5.4 | 8e-06 | 12/21 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.559×** | -5.2 | 2e-05 | 16/20 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.546×** | -5.2 | 2e-05 | 13/20 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.600×** | -4.6 | 4e-04 | 11/20 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.609×** | -4.4 | 7e-04 | 10/21 (HOP62, SHP-77, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.611×** | -4.4 | 7e-04 | 13/21 (HEC-1-A, HS-578T, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.624×** | -4.0 | 0.003 | 12/20 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.715×** | -3.9 | 0.005 | 12/20 (HOP62, SHP-77, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.733×** | -3.8 | 0.005 | 8/20 (SHP-77, HEC-1-A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.733×** | -3.8 | 0.005 | 9/20 (HOP62, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.655×** | -3.8 | 0.007 | 14/20 (RPMI-7951, HOP62, …) | two highest doses |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.748×** | -3.6 | 0.010 | 7/21 (Panc 03.27, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1740. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 18.6 | 0 | 13 (4 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0303× (z -13.4) |
| [[HT-29 (line)]] | alt | 8.70 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0586× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 10.1 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0721× (z -10.0) ⚠ toxic; cell-cycle shift, explains ~13% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 89.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -11.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.190× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 17.5 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0531× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 8.40 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 72.2 | 0 | 2 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.192× (z -9.4) |
| [[SHP-77 (line)]] | alt | 63.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -12.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -12.5) |
| [[SW480 (line)]] | alt | 9.15 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 4.59× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.0966× (z -9.3) |
| [[Hs 766T (line)]] | wt | 6.12 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -8.9) |
| [[LS 180 (line)]] | wt | 2.73 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 13.8× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 5.18 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0625× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.553 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.896 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.920 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.854 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.808 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.938 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.994 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.800 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.31 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1740), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAEP]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[RAC2]] | +0.68 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[ATP2C2]] | +0.63 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[KRT15]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[SLCO4A1]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[LAPTM5]] | +0.61 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[FCHO1]] | +0.59 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[SEMA4B]] | +0.58 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[RIN1]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[PLCH2]] | +0.58 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[TRIOBP]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[KIF21B]] | +0.58 | +0.50 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB2]] | -0.54 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[CLIP1]] | -0.53 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[ARID1B]] | -0.53 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[TLK2]] | -0.53 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[RUFY3]] | -0.52 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[SETD7]] | -0.52 | -0.48 / -0.32 | both halves | 1e-04 |  |
| [[BLTP3A]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[MGST1]] | -0.51 | -0.51 / -0.38 | both halves | 7e-05 | pathway: Biological oxidations |
| [[GTF2I]] | -0.50 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[TLK1]] | -0.50 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[HMGA1P4]] | -0.50 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[AK3]] | -0.50 | -0.51 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRAG1]] | B | PRAG1 activity raises PTGS1's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 1.85× lower at baseline in the lines without PRAG1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises PTGS1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[NES]] | C | NES activity raises PTGS1's level | lines that do not express NES (26) vs lines expressing it (24) | 2.65× lower at baseline in the lines without NES | 0.030 | ⚠ within organs, on part of the lines; also absent: LAPTM5, CSPG4, ENSG00000230490; co-absent with the target |
| [[LINC02970]] | C | LINC02970 activity raises PTGS1's level | lines that do not express LINC02970 (24) vs lines expressing it (26) | 1.53× lower at baseline in the lines without LINC02970 | 0.088 | ⚠ within organs, on part of the lines; also absent: TOX, MXRA5, ENSG00000255595; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADSS1]] | B | PTGS1 activity raises ADSS1's level | lines that do not express PTGS1 (26) vs lines expressing it (24) | 1.47× lower at baseline in the lines without PTGS1 | 0.016 | ⚠ within organs, on part of the lines; also absent: C2CD4A, ARHGEF38, ILDR1 |
| [[TGFA]] | B | PTGS1 activity raises TGFA's level | lines that do not express PTGS1 (26) vs lines expressing it (24) | 2.25× lower at baseline in the lines without PTGS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: C2CD4A, ARHGEF38, ILDR1 |
| [[BAIAP3]] | B | PTGS1 activity strengthens BAIAP3's drug response | lines that do not express PTGS1 (19) vs lines expressing it (19) | the lines without PTGS1 respond 0.74× as strongly (z diff +0.79); strongest at Panobinostat 0.05 µM: 1.93x vs 2.94x (z diff +1.3) | 0.034 | ⚠ within organs, on part of the lines; also absent: C2CD4A, ARHGEF38, ILDR1; target measured in part of the lines; artifact flags |
| [[DUSP5]] | B | PTGS1 activity raises DUSP5's level | lines that do not express PTGS1 (26) vs lines expressing it (24) | 1.96× lower at baseline in the lines without PTGS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: C2CD4A, ARHGEF38, ILDR1 |
| [[NFYA]] | B | PTGS1 activity lowers NFYA's level | lines that do not express PTGS1 (26) vs lines expressing it (24) | 1.15× higher at baseline in the lines without PTGS1 | 0.088 | ⚠ within organs, on part of the lines; also absent: C2CD4A, ARHGEF38, ILDR1 |
| [[TRIOBP]] | B | PTGS1 activity raises TRIOBP's level | lines that do not express PTGS1 (26) vs lines expressing it (24) | 1.45× lower at baseline in the lines without PTGS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: C2CD4A, ARHGEF38, ILDR1 |
| [[BLTP3A]] | B | PTGS1 activity lowers BLTP3A's level | lines that do not express PTGS1 (26) vs lines expressing it (24) | 1.34× higher at baseline in the lines without PTGS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: C2CD4A, ARHGEF38, ILDR1 |
| [[PAEP]] | C | PTGS1 activity raises PAEP's level | lines that do not express PTGS1 (26) vs lines expressing it (24) | 2.22× lower at baseline in the lines without PTGS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: C2CD4A, ARHGEF38, ILDR1; co-absent with the target |
| [[SPNS2]] | C | PTGS1 activity raises SPNS2's level | lines that do not express PTGS1 (26) vs lines expressing it (24) | 2.53× lower at baseline in the lines without PTGS1 | 0.029 | ⚠ within organs, on part of the lines; also absent: C2CD4A, ARHGEF38, ILDR1; co-absent with the target |
| [[SYT13]] | C | PTGS1 activity raises SYT13's level | lines that do not express PTGS1 (26) vs lines expressing it (24) | 2.11× lower at baseline in the lines without PTGS1 | 0.059 | ⚠ within organs, on part of the lines; also absent: C2CD4A, ARHGEF38, ILDR1; co-absent with the target |
| [[LINC02970]] | C | PTGS1 activity raises LINC02970's level | lines that do not express PTGS1 (26) vs lines expressing it (24) | 1.49× lower at baseline in the lines without PTGS1 | 0.093 | ⚠ within organs, on part of the lines; also absent: C2CD4A, ARHGEF38, ILDR1; co-absent with the target |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.618). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.8, 0.6); signed map (0.6, 48.0). **Vector** length 74.0, 20.9% of its response variance represented; |z| ≥ 3 in 710 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +10.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +3.2 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +2.8 | +5.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.8 | +6.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +2.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.2 | +1.8 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.9 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.6 | -6.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.1 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.0 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.0 | -4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | prostaglandin-endoperoxide synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:122,370,530-122,395,703 (+) |
| Ensembl biotype | protein_coding |
| Also known as | COX1, PGHS-1, PTGHS |
| Gene groups (HGNC) | Prostaglandin-endoperoxide synthase family |
| Reactome | 6 pathways, smallest: Synthesis of Prostaglandins (PG) and Thromboxanes (TX); Arachidonate metabolism; Phase I - Functionalization of compounds |
| Matched by | ensembl_id |

**Function**, from UniProt [P23219](https://www.uniprot.org/uniprotkb/P23219) (Prostaglandin G/H synthase 1):

> Dual cyclooxygenase and peroxidase that plays an important role in the biosynthesis pathway of prostanoids, a class of C20 oxylipins mainly derived from arachidonate ((5Z,8Z,11Z,14Z)-eicosatetraenoate, AA, C20:4(n-6)), with a particular role in the inflammatory response. The cyclooxygenase activity oxygenates AA to the hydroperoxy endoperoxide prostaglandin G2 (PGG2), and the peroxidase activity reduces PGG2 to the hydroxy endoperoxide prostaglandin H2 (PGH2), the precursor of all 2-series …

**Summary**, from NCBI Gene [5742](https://www.ncbi.nlm.nih.gov/gene/5742):

> This is one of two genes encoding similar enzymes that catalyze the conversion of arachidonate to prostaglandin. The encoded protein regulates angiogenesis in endothelial cells, and is inhibited by nonsteroidal anti-inflammatory drugs such as aspirin. Based on its ability to function as both a cyclooxygenase and as a peroxidase, the encoded protein has been identified as a moonlighting protein. The protein may promote cell proliferation during tumor progression. Alternative splicing results in …

**Accessions** — [HGNC:9604](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9604) · Entrez [5742](https://www.ncbi.nlm.nih.gov/gene/5742) · UniProt [P23219](https://www.uniprot.org/uniprotkb/P23219) · Ensembl [ENSG00000095303](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095303)

## Data

Gene col 1740: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1740); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1740, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1740]; `tensor/DDL_lfc|DDL_z.npy` [1740]; `embed/gene_vectors.npy` [1740]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1740 or target_col == 1740). Every well: [[PTGS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTGS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
