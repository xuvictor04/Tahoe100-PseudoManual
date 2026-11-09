---
symbol: "PRDM8"
type: "gene"
col: 7659
ensembl_id: "ENSG00000152784"
name: "PR/SET domain 8"
location: "4q21.21"
module: 81
arm: "+"
pooled_cpm: 12.26
n_lines_expressing: 33
n_dd_up: 1
n_dd_down: 56
n_dd_up_clean: 0
n_dd_down_clean: 53
in_vector_space: true
direction_upstream: 10
direction_downstream: 10
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# PRDM8

*PR/SET domain 8* — 4q21.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.60× (z +4.9, q 4e-04, up in 4 of 15 measured lines) ⚠ toxic; transcription drop.
> Pooled over the cell lines (median), lowered significantly by 56 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.213× (z -16.0, q 0e+00, down in 29 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANTXR2]] (+0.79, fdr 7e-06), [[PHLDA1]] (+0.69, fdr 7e-06), [[LINC00973]] (+0.67, fdr 7e-06); moves opposite to [[PDLIM1]] (-0.54, fdr 3e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[G0S2]] → it (grade B ⚠); 10 go from it, the strongest it → [[PLAUR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7659.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +4.9 | 4e-04 | 4/15 (HT-29, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | 1.37× | +3.4 | 0.11 | 7/30 (A498, A-172, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.58× | +3.4 | 0.11 | 3/26 (Hs 766T, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.36× | +3.4 | 0.11 | 8/28 (A-172, H4, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.55× | +3.2 | 0.13 | 5/25 (A498, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.51× | +3.0 | 0.23 | 2/28 (RKO, LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 57 in all, 3 with an alert ⚠; shown: the 15 strongest. 56 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7659.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.213×** | -16.0 | 0e+00 | 29/31 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.300×** | -13.0 | 4e-36 | 27/30 (RKO, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.310×** | -12.1 | 2e-31 | 23/30 (CFPAC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.419×** | -9.4 | 1e-18 | 22/31 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.406×** | -9.0 | 4e-17 | 19/31 (NCI-H460, LS 180, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.437×** | -8.9 | 6e-17 | 19/31 (NCI-H460, LS 180, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.467×** | -7.9 | 3e-13 | 19/29 (PANC-1, CFPAC-1, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.472×** | -7.6 | 2e-12 | 21/30 (MIA PaCa-2, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.567×** | -7.5 | 3e-12 | 22/30 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.516×** | -7.3 | 2e-11 | 21/31 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.508×** | -7.0 | 2e-10 | 20/30 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.583×** | -6.6 | 2e-09 | 17/30 (CFPAC-1, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.557×** | -6.3 | 2e-08 | 16/29 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.665×** | -6.1 | 4e-08 | 13/30 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.551×** | -6.0 | 6e-08 | 17/30 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7659. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 63.2 | 0 | 9 (4 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.369× (z -20.7) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.112× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 7.34 | 0 | 9 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 0.5 µM 0.138× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 28.1 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0972× (z -14.9) |
| [[LS 180 (line)]] | wt | 51.3 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.142× (z -11.0) |
| [[RKO (line)]] | wt | 48.3 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0583× (z -18.8) |
| [[NCI-H1792 (line)]] | alt | 30.6 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0233× (z -17.7) |
| [[LOX-IMVI (line)]] | wt | 58.9 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -15.2) |
| [[A-172 (line)]] | wt | 15.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0382× (z -18.2) |
| [[NCI-H2347 (line)]] | alt | 24.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0705× (z -15.8) |
| [[AsPC-1 (line)]] | alt | 28.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0951× (z -14.1) |
| [[CHP-212 (line)]] | wt | 27.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0795× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[LJI308 (drug)]] 0.05 µM 0.0787× (z -8.5) |
| [[HOP62 (line)]] | alt | 8.15 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -10.0) |
| [[Hs 766T (line)]] | wt | 7.20 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0711× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.117× (z -8.8) |
| [[PANC-1 (line)]] | alt | 6.59 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.155× (z -8.6) |
| [[A-427 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.875 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.20 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7659), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANTXR2]] | +0.79 | +0.79 / +0.80 | both halves | 7e-06 | STRING 593 |
| [[PHLDA1]] | +0.69 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[LINC00973]] | +0.67 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[NT5E]] | +0.67 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[SEMA3A]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[HBEGF]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[B4GALT6]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[LIF]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[DPF3]] | +0.65 | +0.50 / +0.57 | both halves | 1e-05 | same gene group |
| [[ITGA2]] | +0.63 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[DUSP6]] | +0.63 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[SERPIND1]] | +0.63 | +0.53 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDLIM1]] | -0.54 | -0.45 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[G0S2]] | B | G0S2 activity raises PRDM8's level | lines that do not express G0S2 (33) vs lines expressing it (17) | 2.04× lower at baseline in the lines without G0S2 | 0.033 | ⚠ within organs, on part of the lines; also absent: IL6, EDNRA, RRAD |
| [[MAP2K1]] | B | MAP2K1 activity raises PRDM8's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 8.4% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MANCR]] | B | MANCR activity raises PRDM8's level | lines that do not express MANCR (20) vs lines expressing it (30) | 2.44× lower at baseline in the lines without MANCR | 0.052 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |
| [[C6orf141]] | B | C6orf141 activity raises PRDM8's level | lines that do not express C6orf141 (21) vs lines expressing it (29) | 2.42× lower at baseline in the lines without C6orf141 | 0.059 | ⚠ within organs, on part of the lines; also absent: ADAM8, ENSG00000251584, SAMD12-AS1 |
| [[PINLYP]] | B | PINLYP activity weakens PRDM8's drug response | lines that do not express PINLYP (10) vs lines expressing it (21) | the lines without PINLYP respond 1.92× as strongly (z diff -1.83); strongest at Trametinib (DMSO_TF solvate) 5 µM: 0.30x vs 0.53x (z diff -2.8) | 0.069 | ⚠ within organs, on part of the lines; also absent: C9, BMPER, CALD1; maybe low, not absent; target measured in part of the lines; the reference differs |
| [[CD274]] | B | CD274 activity raises PRDM8's level | lines that do not express CD274 (18) vs lines expressing it (32) | 2.38× lower at baseline in the lines without CD274 | 0.070 | ⚠ within organs, on part of the lines; also absent: GBP5, IL1B, PDCD1LG2 |
| [[GNG11]] | B | GNG11 activity lowers PRDM8's level | lines that do not express GNG11 (21) vs lines expressing it (29) | 1.09× higher at baseline in the lines without GNG11 | 0.089 | ⚠ within organs, on part of the lines; also absent: LOXL2, SLC8A1, NALCN |
| [[ANTXR2]] | C | ANTXR2 activity raises PRDM8's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 3.54× lower at baseline in the lines without ANTXR2 | 0.050 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent; co-absent with the target |
| [[IL1A]] | C | IL1A activity raises PRDM8's level | lines that do not express IL1A (27) vs lines expressing it (23) | 2.61× lower at baseline in the lines without IL1A | 0.057 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT; co-absent with the target |
| [[STC1]] | C | STC1 activity raises PRDM8's level | lines that do not express STC1 (24) vs lines expressing it (26) | 2.37× lower at baseline in the lines without STC1 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAUR]] | B | PRDM8 activity raises PLAUR's level | lines that do not express PRDM8 (17) vs lines expressing it (33) | 2.82× lower at baseline in the lines without PRDM8 | 0.075 | ⚠ within organs, on part of the lines; also absent: TLR6, CFAP299, EDIL3 |
| [[SLC16A7]] | B | PRDM8 activity raises SLC16A7's level | lines that do not express PRDM8 (17) vs lines expressing it (33) | 2.85× lower at baseline in the lines without PRDM8 | 0.078 | ⚠ within organs, on part of the lines; also absent: TLR6, CFAP299, EDIL3 |
| [[VEGFC]] | B | PRDM8 activity raises VEGFC's level | lines that do not express PRDM8 (17) vs lines expressing it (33) | 3.11× lower at baseline in the lines without PRDM8 | 0.081 | ⚠ within organs, on part of the lines; also absent: TLR6, CFAP299, EDIL3 |
| [[NT5E]] | B | PRDM8 activity raises NT5E's level | lines that do not express PRDM8 (17) vs lines expressing it (33) | 3.00× lower at baseline in the lines without PRDM8 | 0.081 | ⚠ within organs, on part of the lines; also absent: TLR6, CFAP299, EDIL3 |
| [[SHC3]] | B | PRDM8 activity raises SHC3's level | lines that do not express PRDM8 (17) vs lines expressing it (33) | 2.32× lower at baseline in the lines without PRDM8 | 0.082 | ⚠ within organs, on part of the lines; also absent: TLR6, CFAP299, EDIL3 |
| [[PLEK2]] | B | PRDM8 activity raises PLEK2's level | lines that do not express PRDM8 (17) vs lines expressing it (33) | 2.38× lower at baseline in the lines without PRDM8 | 0.093 | ⚠ within organs, on part of the lines; also absent: TLR6, CFAP299, EDIL3 |
| [[TIMP1]] | B | PRDM8 activity raises TIMP1's level | lines that do not express PRDM8 (17) vs lines expressing it (33) | 1.70× lower at baseline in the lines without PRDM8 | 0.096 | ⚠ within organs, on part of the lines; also absent: TLR6, CFAP299, EDIL3 |
| [[PKIA]] | B | PRDM8 activity raises PKIA's level | lines that do not express PRDM8 (17) vs lines expressing it (33) | 2.59× lower at baseline in the lines without PRDM8 | 0.097 | ⚠ within organs, on part of the lines; also absent: TLR6, CFAP299, EDIL3 |
| [[ANTXR2]] | C | PRDM8 activity raises ANTXR2's level | lines that do not express PRDM8 (17) vs lines expressing it (33) | 4.57× lower at baseline in the lines without PRDM8 | 0.001 | ⚠ within organs, on part of the lines; also absent: TLR6, CFAP299, EDIL3; co-absent with the target |
| [[BMP2]] | C | PRDM8 activity raises BMP2's level | lines that do not express PRDM8 (17) vs lines expressing it (33) | 3.56× lower at baseline in the lines without PRDM8 | 0.017 | ⚠ within organs, on part of the lines; also absent: TLR6, CFAP299, EDIL3; co-absent with the target |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.707). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.7, 5.1); signed map (9.1, 45.8). **Vector** length 91.5, 24.9% of its response variance represented; |z| ≥ 3 in 900 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *KRAS signaling up* (hallmark, mean cos +0.57 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +0.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.8 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +0.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.3 | +1.9 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.5 | -9.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.1 | -7.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.7 | -7.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.7 | -8.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.5 | -6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.4 | -9.0 |

## What is on record

|  |  |
|---|---|
| Name | PR/SET domain 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.21 — chr4:80,183,879-80,204,329 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KMT8D |
| Gene groups (HGNC) | Zinc fingers C2H2-type; PR/SET domain family; Putative lysine methyltransferases |
| Reactome | 8 pathways, smallest: Regulation of CDH11 gene transcription; Regulation of CDH11 Expression and Function; Regulation of Expression and Function of Type II Classical Cadherins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQV8](https://www.uniprot.org/uniprotkb/Q9NQV8) (PR domain zinc finger protein 8):

> Probable histone methyltransferase, preferentially acting on 'Lys-9' of histone H3 (By similarity). Involved in the control of steroidogenesis through transcriptional repression of steroidogenesis marker genes such as CYP17A1 and LHCGR (By similarity). Forms with BHLHE22 a transcriptional repressor complex controlling genes involved in neural development and neuronal differentiation (By similarity). In the retina, it is required for rod bipolar and type 2 OFF-cone bipolar cell survival (By …

**Summary**, from NCBI Gene [56978](https://www.ncbi.nlm.nih.gov/gene/56978):

> This gene encodes a protein that belongs to a conserved family of histone methyltransferases that predominantly act as negative regulators of transcription. The encoded protein contains an N-terminal Su(var)3-9, Enhancer-of-zeste, and Trithorax (SET) domain and a double zinc-finger domain. Knockout of this gene in mouse results in mistargeting by neurons of the dorsal telencephalon, abnormal itch-like behavior, and impaired differentiation of rod bipolar cells. In humans, the protein has been …

**Accessions** — [HGNC:13993](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13993) · Entrez [56978](https://www.ncbi.nlm.nih.gov/gene/56978) · UniProt [Q9NQV8](https://www.uniprot.org/uniprotkb/Q9NQV8) · Ensembl [ENSG00000152784](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152784)

## Data

Gene col 7659: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7659); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7659, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7659]; `tensor/DDL_lfc|DDL_z.npy` [7659]; `embed/gene_vectors.npy` [7659]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7659 or target_col == 7659). Every well: [[PRDM8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRDM8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
