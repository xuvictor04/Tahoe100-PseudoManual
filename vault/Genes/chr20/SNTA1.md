---
symbol: "SNTA1"
type: "gene"
col: 2130
ensembl_id: "ENSG00000101400"
name: "syntrophin alpha 1"
location: "20q11.21"
module: 30
arm: "+"
pooled_cpm: 9.83
n_lines_expressing: 45
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 8
direction_downstream: 30
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# SNTA1

*syntrophin alpha 1* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.84× (z +9.5, q 2e-18, up in 27 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.379× (z -21.3, q 0e+00, down in 33 of 40 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD9]] (+0.72, fdr 1e-05), [[SLC9A6]] (+0.70, fdr 5e-05), [[PEDS1]] (+0.69, fdr 2e-05); moves opposite to [[LEKR1]] (-0.70, fdr 2e-05), [[ST7L]] (-0.67, fdr 1e-04), [[RFX3-DT]] (-0.66, fdr 3e-04).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[STARD9]] → it (grade B ⚠); 30 go from it, the strongest it → [[PLBD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2130.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +9.5 | 2e-18 | 27/43 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.82×** | +9.3 | 3e-18 | 25/43 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +8.5 | 3e-15 | 21/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +8.0 | 1e-13 | 8/18 (A498, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +7.6 | 5e-12 | 13/30 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +4.9 | 8e-05 | 12/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +3.9 | 0.009 | 5/42 (PANC-1, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.009 | 13/41 (NCI-H2030, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.009 | 8/43 (HS-578T, NCI-H2030, …) | rises with dose | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.018 | 4/36 (LS 180, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.25×** | +3.5 | 0.029 | 9/42 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.085 | 6/40 (Hs 766T, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2130.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.379×** | -21.3 | 0e+00 | 33/40 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.391×** | -14.6 | 1e-45 | 30/40 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.462×** | -11.5 | 2e-28 | 27/41 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.762×** | -6.0 | 4e-07 | 19/39 (MIA PaCa-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.501×** | -5.6 | 2e-06 | 16/38 (HS-578T, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.724×** | -4.7 | 2e-04 | 16/42 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.766×** | -4.1 | 0.003 | 12/43 (SNU-1, C32, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.602×** | -4.1 | 0.003 | 15/42 (C32, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.773×** | -4.0 | 0.004 | 14/42 (SNU-1, NCI-H460, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.778×** | -3.9 | 0.006 | 17/42 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.781×** | -3.7 | 0.012 | 16/41 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.800×** | -3.4 | 0.027 | 9/42 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.808×** | -3.3 | 0.042 | 14/41 (SNU-1, Panc 03.27, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2130. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 30.5 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -19.2) |
| [[NCI-H460 (line)]] | wt | 9.88 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.190× (z -11.5) |
| [[C32 (line)]] | wt | 17.2 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.195× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.202× (z -12.5) |
| [[HOP62 (line)]] | alt | 20.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -17.2) |
| [[NCI-H1792 (line)]] | alt | 17.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 15.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0891× (z -14.9) |
| [[RPMI-7951 (line)]] | alt | 18.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0973× (z -12.8) |
| [[SNU-423 (line)]] | alt | 21.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -15.8) |
| [[SW 900 (line)]] | alt | 6.26 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0534× (z -10.6) |
| [[A498 (line)]] | wt | 6.81 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -9.1) |
| [[Hs 766T (line)]] | wt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.5) |
| [[HS-578T (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -18.5) |
| [[J82 (line)]] | alt | 27.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -17.3) |
| [[NCI-H2030 (line)]] | alt | 10.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 7.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -8.5) |
| [[SHP-77 (line)]] | alt | 8.79 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.112× (z -9.8) |
| [[SNU-1 (line)]] | wt | 8.61 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0744× (z -8.5) ⚠ cell-cycle shift, explains ~16% of this change |
| [[A-427 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2130), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD9]] | +0.72 | +0.66 / +0.57 | both halves | 1e-05 | same gene group |
| [[SLC9A6]] | +0.70 | +0.69 / +0.39 | both halves | 5e-05 |  |
| [[PEDS1]] | +0.69 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[USP35]] | +0.69 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[UNC45A]] | +0.68 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[CLTCL1]] | +0.67 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[TRIM62]] | +0.67 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[PLD2]] | +0.66 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[PDZD7]] | +0.66 | +0.58 / +0.49 | both halves | 1e-05 | same gene group |
| [[LRFN3]] | +0.66 | +0.61 / +0.36 | both halves | 9e-05 |  |
| [[ATRN]] | +0.65 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[YIF1B]] | +0.65 | +0.58 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEKR1]] | -0.70 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[ST7L]] | -0.67 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[RFX3-DT]] | -0.66 | -0.63 / -0.27 | both halves | 3e-04 |  |
| [[WARS2-AS1]] | -0.66 | -0.59 / -0.36 | both halves | 9e-05 |  |
| [[TASOR]] | -0.63 | -0.63 / -0.40 | both halves | 5e-05 |  |
| [[CYREN]] | -0.62 | -0.65 / -0.35 | both halves | 1e-04 |  |
| [[HCG17]] | -0.62 | -0.64 / -0.30 | both halves | 2e-04 |  |
| [[MCTS1]] | -0.61 | -0.64 / -0.29 | both halves | 3e-04 |  |
| [[GNG12-AS1]] | -0.61 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[ZC3H4]] | -0.60 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[POGLUT1]] | -0.60 | -0.64 / -0.35 | both halves | 1e-04 |  |
| [[NSUN6]] | -0.60 | -0.70 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD9]] | B | STARD9 activity raises SNTA1's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 2.67× lower at baseline in the lines without STARD9 | 0.007 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[RECK]] | B | RECK activity raises SNTA1's level | lines that do not express RECK (12) vs lines expressing it (38) | 2.04× lower at baseline in the lines without RECK | 0.042 | ⚠ within organs, on part of the lines; also absent: OSBPL6, DZIP1L, STARD9 |
| [[PPP1R1C]] | B | PPP1R1C activity lowers SNTA1's level | lines that do not express PPP1R1C (13) vs lines expressing it (37) | 1.67× higher at baseline in the lines without PPP1R1C | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, LINC01239, ADGRL4; maybe low, not absent |
| [[MPP2]] | B | MPP2 activity raises SNTA1's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 2.16× lower at baseline in the lines without MPP2 | 0.064 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[SYNGR1]] | B | SYNGR1 activity raises SNTA1's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 2.34× lower at baseline in the lines without SYNGR1 | 0.073 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1 |
| [[GPR155]] | B | GPR155 activity raises SNTA1's level | lines that do not express GPR155 (6) vs lines expressing it (44) | 2.16× lower at baseline in the lines without GPR155 | 0.085 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PKIG, TBC1D19; maybe low, not absent |
| [[CLTCL1]] | C | CLTCL1 activity raises SNTA1's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 3.74× lower at baseline in the lines without CLTCL1 | 0.030 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT; co-absent with the target |
| [[SMARCD3]] | C | SMARCD3 activity raises SNTA1's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 1.83× lower at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 29, C 1. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLBD2]] | B | SNTA1 activity raises PLBD2's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.92× lower at baseline in the lines without SNTA1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[HACE1]] | B | SNTA1 activity raises HACE1's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 2.70× lower at baseline in the lines without SNTA1 | 0.012 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[SIN3B]] | B | SNTA1 activity raises SIN3B's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.55× lower at baseline in the lines without SNTA1 | 0.025 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[STARD9]] | B | SNTA1 activity raises STARD9's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 4.16× lower at baseline in the lines without SNTA1 | 0.026 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[STX2]] | B | SNTA1 activity raises STX2's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 2.68× lower at baseline in the lines without SNTA1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[SHANK3]] | B | SNTA1 activity raises SHANK3's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 2.74× lower at baseline in the lines without SNTA1 | 0.030 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[LRFN3]] | B | SNTA1 activity raises LRFN3's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.35× lower at baseline in the lines without SNTA1 | 0.033 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[PLD2]] | B | SNTA1 activity raises PLD2's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.35× lower at baseline in the lines without SNTA1 | 0.034 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[PTDSS2]] | B | SNTA1 activity raises PTDSS2's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without SNTA1 | 0.034 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[PSMD9]] | B | SNTA1 activity raises PSMD9's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.32× lower at baseline in the lines without SNTA1 | 0.034 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[ECI2]] | B | SNTA1 activity raises ECI2's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 2.69× lower at baseline in the lines without SNTA1 | 0.039 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[NTAN1]] | B | SNTA1 activity raises NTAN1's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.75× lower at baseline in the lines without SNTA1 | 0.042 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.744). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (2.1, -1.7); signed map (-37.1, -3.4). **Vector** length 76.8, 14.2% of its response variance represented; |z| ≥ 3 in 818 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.1 | +9.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.0 | +9.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.8 | +8.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +3.5 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -14.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -21.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -11.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -0.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -3.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -4.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -1.7 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.4 | -2.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | syntrophin alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21 — chr20:33,407,957-33,443,763 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TACIP1, LQT12; previously SNT1 |
| Gene groups (HGNC) | PDZ domain containing; Syntrophin family |
| Reactome | 3 pathways, smallest: Formation of the dystrophin-glycoprotein complex (DGC); Non-integrin membrane-ECM interactions; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13424](https://www.uniprot.org/uniprotkb/Q13424) (Alpha-1-syntrophin):

> Adapter protein that binds to and probably organizes the subcellular localization of a variety of membrane proteins. May link various receptors to the actin cytoskeleton and the extracellular matrix via the dystrophin glycoprotein complex. Plays an important role in synapse formation and in the organization of UTRN and acetylcholine receptors at the neuromuscular synapse. Binds to phosphatidylinositol 4,5-bisphosphate (By similarity).

**Summary**, from NCBI Gene [6640](https://www.ncbi.nlm.nih.gov/gene/6640):

> Syntrophins are cytoplasmic peripheral membrane scaffold proteins that are components of the dystrophin-associated protein complex. This gene is a member of the syntrophin gene family and encodes the most common syntrophin isoform found in cardiac tissues. The N-terminal PDZ domain of this syntrophin protein interacts with the C-terminus of the pore-forming alpha subunit (SCN5A) of the cardiac sodium channel Nav1.5. This protein also associates cardiac sodium channels with the nitric oxide …

**Accessions** — [HGNC:11167](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11167) · Entrez [6640](https://www.ncbi.nlm.nih.gov/gene/6640) · UniProt [Q13424](https://www.uniprot.org/uniprotkb/Q13424) · Ensembl [ENSG00000101400](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101400)

## Data

Gene col 2130: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2130); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2130, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2130]; `tensor/DDL_lfc|DDL_z.npy` [2130]; `embed/gene_vectors.npy` [2130]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2130 or target_col == 2130). Every well: [[SNTA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNTA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
