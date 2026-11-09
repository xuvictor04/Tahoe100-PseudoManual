---
symbol: "SEPTIN9-DT"
type: "gene"
col: 15422
ensembl_id: "ENSG00000263718"
name: "SEPTIN9 divergent transcript"
location: "17q25.3"
module: 73
arm: "+"
pooled_cpm: 3.18
n_lines_expressing: 37
n_dd_up: 8
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 34
direction_downstream: 20
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# SEPTIN9-DT

*SEPTIN9 divergent transcript* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.54× (z +18.5, q 0e+00, up in 24 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.480× (z -6.3, q 1e-07, down in 22 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SULF2]] (+0.69, fdr 7e-06), [[SLC6A20]] (+0.66, fdr 7e-06), [[UBE2R2-AS1]] (+0.65, fdr 9e-06); moves opposite to [[COMMD2]] (-0.55, fdr 1e-04), [[ESD]] (-0.53, fdr 3e-05), [[UBXN2B]] (-0.53, fdr 1e-04).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 34 arrows point to it, the strongest [[IL20RA]] → it (grade B ⚠); 20 go from it, the strongest it → [[KRT8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15422.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.54×** | +18.5 | 0e+00 | 24/26 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.32×** | +9.6 | 2e-19 | 1/8 (PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.74×** | +8.4 | 9e-15 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.60×** | +8.3 | 2e-14 | 5/16 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.90×** | +7.9 | 3e-13 | 12/31 (PANC-1, A498, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +5.3 | 9e-06 | 9/26 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +5.2 | 2e-05 | 14/24 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +3.3 | 0.076 | 2/9 (LoVo, LS 180) | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.96× | +3.1 | 0.14 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Trifluridine (drug)]] 5 µM |  | 1.28× | +3.0 | 0.14 | 3/31 (SW1417, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15422.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.480×** | -6.3 | 1e-07 | 22/32 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.502×** | -5.9 | 8e-07 | 23/31 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.550×** | -5.1 | 5e-05 | 14/32 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.554×** | -4.6 | 6e-04 | 17/31 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.391×** | -4.2 | 0.003 | 10/30 (HT-29, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.623×** | -4.1 | 0.004 | 12/32 (SW480, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.671×** | -4.1 | 0.004 | 11/32 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.618×** | -3.8 | 0.009 | 10/32 (SNU-423, LoVo, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.639×** | -3.7 | 0.013 | 10/29 (LS 180, HT-29, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.678×** | -3.3 | 0.047 | 13/32 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.690×** | -3.2 | 0.072 | 12/29 (COLO 205, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.692×** | -3.2 | 0.072 | 3/32 (AsPC-1, PANC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.775×** | -3.1 | 0.082 | 14/31 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.906× | -3.1 | 0.082 | 8/32 (A-172, NCI-H23, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.700×** | -3.1 | 0.082 | 6/30 (LS 180, NCI-H23, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.514×** | -3.0 | 0.094 | 4/28 (HT-29, J82, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15422. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 10.4 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0564× (z -16.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0523× (z -11.8) |
| [[LoVo (line)]] | wt | 8.20 | 0 | 7 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.00895× (z -18.7) |
| [[AsPC-1 (line)]] | alt | 8.48 | 0 | 4 | — | [[Panobinostat (drug)]] 0.05 µM 0.0618× (z -9.5) |
| [[Hs 766T (line)]] | wt | 7.56 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0418× (z -10.7) |
| [[HT-29 (line)]] | alt | 17.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0653× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0263× (z -12.5) |
| [[A498 (line)]] | wt | 4.37 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.94× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.1000× (z -8.7) |
| [[LS 180 (line)]] | wt | 6.02 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0972× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0785× (z -8.6) |
| [[A549 (line)]] | wt | 1.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.3× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 4.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.09× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 1.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 27.3× (z +13.9) | — |
| [[PANC-1 (line)]] | alt | 2.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.92× (z +11.0) | — |
| [[SNU-1 (line)]] | wt | 8.11 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0369× (z -9.7) |
| [[SW480 (line)]] | alt | 2.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +9.5) | — |
| [[A-172 (line)]] | wt | 0.907 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.717 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.905 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.585 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.749 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.735 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.660 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.842 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.997 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.604 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.786 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.885 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.880 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15422), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SULF2]] | +0.69 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[SLC6A20]] | +0.66 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[UBE2R2-AS1]] | +0.65 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[TRABD2A]] | +0.65 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[NPSR1]] | +0.65 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[HSD17B2]] | +0.65 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[FAM3D]] | +0.64 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[SLC22A3]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[TPRXL]] | +0.62 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[SMG1-DT]] | +0.62 | +0.47 / +0.62 | both halves | 2e-05 | same gene group |
| [[GNA14]] | +0.61 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[SPON1]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD2]] | -0.55 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[ESD]] | -0.53 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[UBXN2B]] | -0.53 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[ARRB2]] | -0.52 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[ZNF559]] | -0.51 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[NIPSNAP2]] | -0.50 | -0.39 / -0.46 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 31, C 3. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL20RA]] | B | IL20RA activity raises SEPTIN9-DT's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 2.50× lower at baseline in the lines without IL20RA | 3e-04 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10 |
| [[THRB]] | B | THRB activity raises SEPTIN9-DT's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.92× lower at baseline in the lines without THRB | 0.002 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[UGT1A1]] | B | UGT1A1 activity raises SEPTIN9-DT's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 2.17× lower at baseline in the lines without UGT1A1 | 0.003 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1 |
| [[TOP2A]] | B | TOP2A activity lowers SEPTIN9-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 1.7% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[UGT1A1]] | B | UGT1A1 activity strengthens SEPTIN9-DT's drug response | lines that do not express UGT1A1 (22) vs lines expressing it (10) | the lines without UGT1A1 respond 0.83× as strongly (z diff +0.60); strongest at Panobinostat 0.05 µM: 0.74x vs 0.14x (z diff +5.4) | 0.014 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; target measured in part of the lines; both ways; artifact flags |
| [[KLK10]] | B | KLK10 activity raises SEPTIN9-DT's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 2.33× lower at baseline in the lines without KLK10 | 0.015 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[PTPRB]] | B | PTPRB activity raises SEPTIN9-DT's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 1.48× lower at baseline in the lines without PTPRB | 0.017 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[C4BPB]] | B | C4BPB activity raises SEPTIN9-DT's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 2.33× lower at baseline in the lines without C4BPB | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[NPSR1]] | B | NPSR1 activity raises SEPTIN9-DT's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 2.82× lower at baseline in the lines without NPSR1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17 |
| [[REG4]] | B | REG4 activity raises SEPTIN9-DT's level | lines that do not express REG4 (43) vs lines expressing it (7) | 2.80× lower at baseline in the lines without REG4 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975 |
| [[SLC52A3]] | B | SLC52A3 activity raises SEPTIN9-DT's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.01× lower at baseline in the lines without SLC52A3 | 0.027 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[GJB2]] | B | GJB2 activity raises SEPTIN9-DT's level | lines that do not express GJB2 (21) vs lines expressing it (29) | 1.56× lower at baseline in the lines without GJB2 | 0.039 | ⚠ within organs, on part of the lines; also absent: SDR16C5, CYP2S1, SLC52A3 |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 18, C 2. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT8]] | B | SEPTIN9-DT activity raises KRT8's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 4.10× lower at baseline in the lines without SEPTIN9-DT | 0.004 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[ITGB4]] | B | SEPTIN9-DT activity raises ITGB4's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 6.11× lower at baseline in the lines without SEPTIN9-DT | 0.005 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[THRB]] | B | SEPTIN9-DT activity raises THRB's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 4.48× lower at baseline in the lines without SEPTIN9-DT | 0.007 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[HTR1D]] | B | SEPTIN9-DT activity raises HTR1D's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 1.82× lower at baseline in the lines without SEPTIN9-DT | 0.042 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[PLEKHA6]] | B | SEPTIN9-DT activity raises PLEKHA6's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 3.05× lower at baseline in the lines without SEPTIN9-DT | 0.043 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[SLC25A45]] | B | SEPTIN9-DT activity raises SLC25A45's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 1.78× lower at baseline in the lines without SEPTIN9-DT | 0.044 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[GJB2]] | B | SEPTIN9-DT activity raises GJB2's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 2.39× lower at baseline in the lines without SEPTIN9-DT | 0.049 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[PPP1R15B-AS1]] | B | SEPTIN9-DT activity raises PPP1R15B-AS1's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 1.34× lower at baseline in the lines without SEPTIN9-DT | 0.059 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[TNNT2]] | B | SEPTIN9-DT activity raises TNNT2's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 2.36× lower at baseline in the lines without SEPTIN9-DT | 0.070 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| cells under [[Filgotinib (drug)]] 0.05 µM | B | SEPTIN9-DT activity lowers the cells' numbers under Filgotinib 0.05 µM (makes them more sensitive) | lines that do not express SEPTIN9-DT (13) vs lines expressing it (35) | the lines without SEPTIN9-DT: 1.16× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[COL17A1]] | B | SEPTIN9-DT activity raises COL17A1's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 3.38× lower at baseline in the lines without SEPTIN9-DT | 0.074 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |
| [[ARHGAP27]] | B | SEPTIN9-DT activity raises ARHGAP27's level | lines that do not express SEPTIN9-DT (13) vs lines expressing it (37) | 2.53× lower at baseline in the lines without SEPTIN9-DT | 0.078 | ⚠ within organs, on part of the lines; also absent: MALL, CDCP1, EPHA2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.3, 48.6); signed map (68.6, 7.1). **Vector** length 79.8, 18.3% of its response variance represented; |z| ≥ 3 in 960 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +18.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +7.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.1 | -1.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.0 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | SEPTIN9 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q25.3 — chr17:77,257,735-77,282,054 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52818](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52818) · Entrez [105371907](https://www.ncbi.nlm.nih.gov/gene/105371907) · Ensembl [ENSG00000263718](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000263718)

## Data

Gene col 15422: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15422); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15422, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15422]; `tensor/DDL_lfc|DDL_z.npy` [15422]; `embed/gene_vectors.npy` [15422]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15422 or target_col == 15422). Every well: [[SEPTIN9-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEPTIN9-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
