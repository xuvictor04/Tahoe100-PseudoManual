---
symbol: "DPP4"
type: "gene"
col: 12436
ensembl_id: "ENSG00000197635"
name: "dipeptidyl peptidase 4"
location: "2q24.2"
module: 8
arm: "+"
pooled_cpm: 35.1
n_lines_expressing: 21
n_dd_up: 33
n_dd_down: 6
n_dd_up_clean: 26
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 44
direction_downstream: 69
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# DPP4

*dipeptidyl peptidase 4* — 2q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.58× (z +20.5, q 0e+00, up in 10 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.07× (z +16.5, q 0e+00, up in 12 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.643× (z -7.1, q 7e-10, down in 15 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMP7]] (+0.68, fdr 1e-05), [[BCL2L15]] (+0.65, fdr 1e-05), [[TM4SF4]] (+0.65, fdr 1e-05); moves opposite to [[NR2C1]] (-0.48, fdr 2e-04), [[GNA12]] (-0.46, fdr 2e-04), [[PPP2R3B]] (-0.46, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 44 arrows point to it, the strongest [[ITGB8]] → it (grade B ⚠); 69 go from it, the strongest it → [[TMC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12436.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.58×** | +20.5 | 0e+00 | 10/18 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +16.5 | 0e+00 | 12/19 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.85×** | +16.2 | 0e+00 | 8/15 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.58×** | +14.0 | 1e-42 | 8/16 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +8.6 | 8e-16 | 12/19 (HepG2/C3A, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +8.6 | 1e-15 | 7/19 (HCT15, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.15×** | +6.4 | 1e-08 | 5/11 (HEC-1-A, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +5.9 | 3e-07 | 3/19 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.4 | 4e-06 | 3/19 (HEC-1-A, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +5.2 | 1e-05 | 12/18 (CFPAC-1, RPMI-7951, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +5.0 | 3e-05 | 6/19 (LS 180, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +4.9 | 5e-05 | 6/19 (NCI-H1792, CFPAC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +4.8 | 6e-05 | 8/19 (SW1417, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.30×** | +4.2 | 9e-04 | 5/19 (NCI-H1792, NCI-H2347, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +4.2 | 9e-04 | 5/19 (AsPC-1, HepG2/C3A, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +4.2 | 0.001 | 7/19 (AsPC-1, CFPAC-1, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.60×** | +3.9 | 0.003 | 7/19 (RPMI-7951, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.004 | 2/19 (Panc 03.27, HEC-1-A) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.004 | 4/19 (NCI-H1792, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12436.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.643×** | -7.1 | 7e-10 | 15/19 (COLO 205, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.659×** | -6.7 | 6e-09 | 15/19 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.690×** | -6.0 | 5e-07 | 16/19 (CFPAC-1, COLO 205, …) | two highest doses | cell-cycle shift (explains ~25% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.723×** | -5.2 | 3e-05 | 8/19 (CFPAC-1, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.781×** | -4.0 | 0.008 | 11/19 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.773×** | -3.9 | 0.009 | 2/19 (RPMI-7951, HCT15) | inconsistent across doses | position effect removed |
| [[Retinoic acid (drug)]] 0.5 µM |  | 0.818× | -3.2 | 0.10 | 6/19 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[Ferulic acid (drug)]] 0.5 µM |  | 0.826× | -3.1 | 0.15 | 0/18 | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12436. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 54.2 | 0 | 8 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.152× (z -13.2) |
| [[LoVo (line)]] | wt | 63.2 | 3 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -9.8) |
| [[COLO 205 (line)]] | alt | 158 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -12.8) |
| [[HEC-1-A (line)]] | alt | 244 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +10.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 50.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 172 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.163× (z -11.2) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.266× (z -8.7) |
| [[LS 180 (line)]] | wt | 58.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +15.6) | [[Panobinostat (drug)]] 5 µM 0.312× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 166 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -9.7) |
| [[Hs 766T (line)]] | wt | 43.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -8.5) |
| [[A-172 (line)]] | wt | 4.46 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 7.07 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.85 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.10 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.54 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 128 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.46 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.11 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.53 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.82 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.13 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.70 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.43 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.22 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.68 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12436), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMP7]] | +0.68 | +0.72 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_COAGULATION |
| [[BCL2L15]] | +0.65 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[TM4SF4]] | +0.65 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[SLC34A2]] | +0.63 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[SPATA6L]] | +0.59 | +0.59 / +0.39 | both halves | 6e-05 |  |
| [[GABRP]] | +0.59 | +0.74 / +0.44 | both halves | 3e-05 |  |
| [[NPNT]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[MUC4]] | +0.57 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[FMO5]] | +0.56 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[PRSS51]] | +0.56 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[MGAM2]] | +0.56 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[OCLN]] | +0.55 | +0.61 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR2C1]] | -0.48 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[GNA12]] | -0.46 | -0.30 / -0.30 | both halves | 2e-04 |  |
| [[PPP2R3B]] | -0.46 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[MPP3]] | -0.46 | -0.40 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 8, C 36. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB8]] | B | ITGB8 activity raises DPP4's level | lines that do not express ITGB8 (17) vs lines expressing it (33) | 3.09× lower at baseline in the lines without ITGB8 | 0.027 | ⚠ within organs, on part of the lines; also absent: LRATD2, HNMT, B3GALT5 |
| [[PLSCR4]] | B | PLSCR4 activity raises DPP4's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 2.14× lower at baseline in the lines without PLSCR4 | 0.030 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[SEC16B]] | B | SEC16B activity raises DPP4's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 3.76× lower at baseline in the lines without SEC16B | 0.044 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[SCIN]] | B | SCIN activity raises DPP4's level | lines that do not express SCIN (22) vs lines expressing it (28) | 2.24× lower at baseline in the lines without SCIN | 0.058 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[HDAC6]] | B | HDAC6 activity raises DPP4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HGD]] | B | HGD activity raises DPP4's level | lines that do not express HGD (15) vs lines expressing it (35) | 2.69× lower at baseline in the lines without HGD | 0.065 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[PDLIM1]] | B | PDLIM1 activity raises DPP4's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 2.48× lower at baseline in the lines without PDLIM1 | 0.087 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[FCGRT]] | B | FCGRT activity raises DPP4's level | lines that do not express FCGRT (12) vs lines expressing it (38) | 2.59× lower at baseline in the lines without FCGRT | 0.094 | ⚠ within organs, on part of the lines; also absent: STEAP2, IGDCC4, SORL1 |
| [[SLC44A4]] | C | SLC44A4 activity raises DPP4's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 5.51× lower at baseline in the lines without SLC44A4 | 0.003 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[MMP7]] | C | MMP7 activity raises DPP4's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 5.45× lower at baseline in the lines without MMP7 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP; co-absent with the target |
| [[TSPAN1]] | C | TSPAN1 activity raises DPP4's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 4.77× lower at baseline in the lines without TSPAN1 | 0.006 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6; co-absent with the target |
| [[MAL2]] | C | MAL2 activity raises DPP4's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 4.07× lower at baseline in the lines without MAL2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |

### Downstream of this gene

*69 arrows, 69 of them with an alert ⚠; grade A 0, B 32, C 37. Shown: the 12 strongest; 57 more arrows (57 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMC1]] | B | DPP4 activity raises TMC1's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 1.90× lower at baseline in the lines without DPP4 | 0.003 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[EPS8]] | B | DPP4 activity raises EPS8's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 2.74× lower at baseline in the lines without DPP4 | 0.003 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[MUC20]] | B | DPP4 activity raises MUC20's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 2.77× lower at baseline in the lines without DPP4 | 0.005 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[PLEKHA7]] | B | DPP4 activity raises PLEKHA7's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 2.26× lower at baseline in the lines without DPP4 | 0.007 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[PLA2R1]] | B | DPP4 activity raises PLA2R1's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 3.03× lower at baseline in the lines without DPP4 | 0.009 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[ACTR3C]] | B | DPP4 activity raises ACTR3C's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 2.72× lower at baseline in the lines without DPP4 | 0.012 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[INPP4B]] | B | DPP4 activity raises INPP4B's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 1.69× lower at baseline in the lines without DPP4 | 0.012 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[PDLIM1]] | B | DPP4 activity raises PDLIM1's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 2.49× lower at baseline in the lines without DPP4 | 0.012 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| cells under [[Trifluridine (drug)]] 5 µM | B | DPP4 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express DPP4 (29) vs lines expressing it (19) | the lines without DPP4: 0.89× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | DPP4 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express DPP4 (29) vs lines expressing it (19) | the lines without DPP4: 1.12× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[ITGB8]] | B | DPP4 activity raises ITGB8's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 2.39× lower at baseline in the lines without DPP4 | 0.021 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[KLF8]] | B | DPP4 activity raises KLF8's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 1.50× lower at baseline in the lines without DPP4 | 0.023 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.7, 53.9); signed map (60.8, 1.6). **Vector** length 67.2, 19.8% of its response variance represented; |z| ≥ 3 in 533 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +20.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +16.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +14.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +8.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +4.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.0 | +4.2 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -5.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.7 | -6.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.2 | -4.0 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.1 | -2.0 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.0 | -2.9 |
|  | [[Ivermectin (drug)]] 5 µM |  | -0.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | dipeptidyl peptidase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.2 — chr2:161,992,245-162,074,394 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DPPIV; previously CD26, ADCP2 |
| Gene groups (HGNC) | CD molecules; DASH family |
| Hallmark sets | PANCREAS_BETA_CELLS, COAGULATION, COMPLEMENT |
| Reactome | 4 pathways, smallest: Synthesis, secretion, and inactivation of Glucose-dependent Insulinotropic Polypeptide (GIP); Synthesis, secretion, and inactivation of Glucagon-like Peptide-1 (GLP-1); Incretin synthesis, secretion, and inactivation |
| Matched by | ensembl_id |

**Function**, from UniProt [P27487](https://www.uniprot.org/uniprotkb/P27487) (Dipeptidyl peptidase 4):

> Cell surface glycoprotein receptor involved in the costimulatory signal essential for T-cell receptor (TCR)-mediated T-cell activation. Acts as a positive regulator of T-cell coactivation, by binding at least ADA, CAV1, IGF2R, and PTPRC. Its binding to CAV1 and CARD11 induces T-cell proliferation and NF-kappa-B activation in a T-cell receptor/CD3-dependent manner. Its interaction with ADA also regulates lymphocyte-epithelial cell adhesion. In association with FAP is involved in the pericellular …

**Summary**, from NCBI Gene [1803](https://www.ncbi.nlm.nih.gov/gene/1803):

> The DPP4 gene encodes dipeptidyl peptidase 4, which is identical to adenosine deaminase complexing protein-2, and to the T-cell activation antigen CD26. It is an intrinsic type II transmembrane glycoprotein and a serine exopeptidase that cleaves X-proline dipeptides from the N-terminus of polypeptides. Dipeptidyl peptidase 4 is highly involved in glucose and insulin metabolism, as well as in immune regulation. This protein was shown to be a functional receptor for Middle East respiratory …

**Accessions** — [HGNC:3009](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3009) · Entrez [1803](https://www.ncbi.nlm.nih.gov/gene/1803) · UniProt [P27487](https://www.uniprot.org/uniprotkb/P27487) · Ensembl [ENSG00000197635](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197635)

## Data

Gene col 12436: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12436); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12436, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12436]; `tensor/DDL_lfc|DDL_z.npy` [12436]; `embed/gene_vectors.npy` [12436]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12436 or target_col == 12436). Every well: [[DPP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
