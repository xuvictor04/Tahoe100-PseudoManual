---
symbol: "PARM1"
type: "gene"
col: 9754
ensembl_id: "ENSG00000169116"
name: "prostate androgen-regulated mucin-like protein 1"
location: "4q13.3"
module: 115
arm: "+"
pooled_cpm: 12.88
n_lines_expressing: 23
n_dd_up: 36
n_dd_down: 3
n_dd_up_clean: 26
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# PARM1

*prostate androgen-regulated mucin-like protein 1* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (10 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 5.28× (z +32.8, q 0e+00, up in 17 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.875× (z -6.3, q 2e-07, down in 6 of 21 measured lines) ⚠ position not correctable. The strongest without an alert is [[Dexamethasone (drug)]] 0.5 µM: 0.734× (z -4.3, q 0.005, down in 5 of 20 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNK13]] (+0.54, fdr 4e-05), [[RET]] (+0.54, fdr 3e-05), [[SBK1]] (+0.53, fdr 4e-05); moves opposite to [[EIF1B-AS1]] (-0.45, fdr 1e-04), [[CFLAR]] (-0.45, fdr 1e-04), [[LRRC27]] (-0.43, fdr 8e-05).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ILDR2]] → it (grade C ⚠); 5 go from it, the strongest it → [[ARHGAP44]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9754.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **5.28×** | +32.8 | 0e+00 | 17/20 (NCI-H2030, RKO, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **5.84×** | +24.6 | 0e+00 | 13/20 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.36×** | +23.4 | 0e+00 | 14/20 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.59×** | +21.3 | 0e+00 | 15/20 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.38×** | +17.0 | 0e+00 | 17/19 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.28×** | +16.6 | 0e+00 | 16/20 (NCI-H2030, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.14×** | +15.3 | 0e+00 | 1/10 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.90×** | +14.9 | 0e+00 | 8/15 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +11.0 | 2e-26 | 8/19 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.25×** | +10.5 | 7e-24 | 5/11 (Hs 766T, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.67×** | +7.1 | 5e-11 | 9/20 (NCI-H2030, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +6.0 | 1e-07 | 7/19 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +5.9 | 1e-07 | 9/19 (A549, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.44×** | +4.9 | 3e-05 | 3/16 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.81×** | +4.3 | 6e-04 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.3 | 7e-04 | 3/17 (NCI-H2347, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.002 | 0/20 | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.010 | 2/19 (A549, LoVo) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.010 | 2/18 (LS 180, NCI-H2347) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.014 | 0/20 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9754.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.875× | -6.3 | 2e-07 | 6/21 (MIA PaCa-2, H4, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.734×** | -4.3 | 0.005 | 5/20 (SW 900, NCI-H2030, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.774×** | -3.6 | 0.065 | 5/18 (BT-474, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.764×** | -3.5 | 0.070 | 0/20 | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.801× | -3.1 | 0.22 | 3/20 (SHP-77, SW 900, …) | two highest doses |  |
| [[Malotilate (drug)]] 0.5 µM |  | 0.804× | -3.0 | 0.22 | 0/19 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9754. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 80.6 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -16.2) |
| [[LoVo (line)]] | wt | 60.1 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.207× (z -13.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H2030 (line)]] | alt | 3.37 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 11.1× (z +11.4) | — |
| [[LS 180 (line)]] | wt | 95.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -21.5) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 25.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0879× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 3.84 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 10.0× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 154 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -12.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 3.60 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.01× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.20 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.526× (z -8.5) ⚠ position not correctable |
| [[NCI-H2347 (line)]] | alt | 4.39 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.48× (z +10.8) | — |
| [[RKO (line)]] | wt | 4.83 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.8× (z +10.9) | — |
| [[SW48 (line)]] | wt | 42.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -14.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.74 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9754), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNK13]] | +0.54 | +0.40 / +0.58 | both halves | 4e-05 |  |
| [[RET]] | +0.54 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[SBK1]] | +0.53 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[ZBTB7C]] | +0.53 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[SUSD4]] | +0.53 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[GABRA2]] | +0.52 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[ENTREP2]] | +0.52 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[NAA11]] | +0.50 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[AFF2]] | +0.50 | +0.33 / +0.59 | both halves | 1e-04 |  |
| [[SPTSSB]] | +0.49 | +0.36 / +0.55 | both halves | 9e-05 |  |
| [[MED12L]] | +0.49 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[LINC00937]] | +0.48 | +0.35 / +0.53 | both halves | 1e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF1B-AS1]] | -0.45 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[CFLAR]] | -0.45 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[LRRC27]] | -0.43 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[MFF-DT]] | -0.41 | -0.44 / -0.24 | both halves | 4e-04 |  |
| [[MAILR]] | -0.41 | -0.33 / -0.27 | both halves | 3e-04 |  |
| [[PUS10]] | -0.41 | -0.43 / -0.24 | both halves | 5e-04 |  |
| [[CCDC30]] | -0.40 | -0.34 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[DPH6-DT]] | -0.40 | -0.31 / -0.22 | both halves | 6e-04 |  |
| [[AGA-DT]] | -0.40 | -0.33 / -0.22 | both halves | 6e-04 |  |
| [[ZNF714]] | -0.40 | -0.31 / -0.33 | both halves | 2e-04 |  |
| [[PKN2-AS1]] | -0.40 | -0.31 / -0.31 | both halves | 2e-04 |  |
| [[UBE3B]] | -0.39 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[SUCLG2-DT]] | -0.39 | -0.39 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ILDR2]] | C | ILDR2 activity raises PARM1's level | lines that do not express ILDR2 (31) vs lines expressing it (19) | 2.60× lower at baseline in the lines without ILDR2 | 0.071 | ⚠ within organs, on part of the lines; also absent: NKD1, ENSG00000265554, PADI1; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP44]] | B | PARM1 activity raises ARHGAP44's level | lines that do not express PARM1 (27) vs lines expressing it (23) | 2.29× lower at baseline in the lines without PARM1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ST6GAL2, PRR15L, C2CD4A |
| [[JAKMIP1]] | B | PARM1 activity weakens JAKMIP1's drug response | lines that do not express PARM1 (11) vs lines expressing it (8) | the lines without PARM1 respond 1.41× as strongly (z diff -1.39); strongest at Dinaciclib 5 µM: 1.81x vs 0.76x (z diff -3.9) | 0.055 | ⚠ within organs, on part of the lines; also absent: ST6GAL2, PRR15L, C2CD4A; target measured in part of the lines; artifact flags |
| [[TIAM1]] | B | PARM1 activity strengthens TIAM1's drug response | lines that do not express PARM1 (22) vs lines expressing it (16) | the lines without PARM1 respond 0.97× as strongly (z diff +0.55); strongest at Panobinostat 0.05 µM: 1.96x vs 2.77x (z diff +2.3) | 0.069 | ⚠ within organs, on part of the lines; also absent: ST6GAL2, PRR15L, C2CD4A; target measured in part of the lines; artifact flags |
| [[SUSD4]] | B | PARM1 activity raises SUSD4's level | lines that do not express PARM1 (27) vs lines expressing it (23) | 1.74× lower at baseline in the lines without PARM1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ST6GAL2, PRR15L, C2CD4A |
| [[SLITRK6]] | C | PARM1 activity raises SLITRK6's level | lines that do not express PARM1 (27) vs lines expressing it (23) | 2.60× lower at baseline in the lines without PARM1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ST6GAL2, PRR15L, C2CD4A; co-absent with the target |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.558). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.3, 41.1); signed map (49.6, 30.1). **Vector** length 53.6, 12.8% of its response variance represented; |z| ≥ 3 in 504 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +32.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +17.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +3.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +0.5 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -6.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | prostate androgen-regulated mucin-like protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:74,933,095-75,050,115 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564O0823, Cipar1, WSC4 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UWI2](https://www.uniprot.org/uniprotkb/Q6UWI2) (Prostate androgen-regulated mucin-like protein 1):

> May regulate TLP1 expression and telomerase activity, thus enabling certain prostatic cells to resist apoptosis.

**Summary**, from NCBI Gene [25849](https://www.ncbi.nlm.nih.gov/gene/25849):

> Located in Golgi apparatus; endosome; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24536](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24536) · Entrez [25849](https://www.ncbi.nlm.nih.gov/gene/25849) · UniProt [Q6UWI2](https://www.uniprot.org/uniprotkb/Q6UWI2) · Ensembl [ENSG00000169116](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169116)

## Data

Gene col 9754: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9754); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9754, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9754]; `tensor/DDL_lfc|DDL_z.npy` [9754]; `embed/gene_vectors.npy` [9754]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9754 or target_col == 9754). Every well: [[PARM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
