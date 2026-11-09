---
symbol: "JAKMIP1"
type: "gene"
col: 7675
ensembl_id: "ENSG00000152969"
name: "janus kinase and microtubule interacting protein 1"
location: "4p16.1"
module: 82
arm: "+"
pooled_cpm: 3.84
n_lines_expressing: 23
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 7
direction_downstream: 16
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# JAKMIP1

*janus kinase and microtubule interacting protein 1* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.01× (z +17.7, q 0e+00, up in 18 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.622× (z -4.3, q 0.009, down in 9 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPYSL5]] (+0.75, fdr 7e-06), [[RET]] (+0.75, fdr 7e-06), [[NOVA2]] (+0.72, fdr 7e-06); moves opposite to [[DECR1]] (-0.55, fdr 5e-05), [[RNF146]] (-0.55, fdr 2e-04), [[FBXW4]] (-0.52, fdr 2e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PARM1]] → it (grade B ⚠); 16 go from it, the strongest it → [[RNF146]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7675.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.01×** | +17.7 | 0e+00 | 18/19 (SW480, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.88×** | +14.3 | 9e-44 | 18/18 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.80×** | +14.1 | 5e-43 | 18/18 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.51×** | +13.6 | 9e-40 | 19/19 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.93×** | +12.3 | 9e-33 | 17/17 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.84×** | +11.7 | 2e-29 | 1/3 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.44×** | +11.3 | 8e-28 | 5/17 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.36×** | +10.9 | 7e-26 | 13/17 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.09×** | +10.1 | 2e-22 | 2/11 (PANC-1, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **2.88×** | +9.5 | 1e-19 | 13/15 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.20×** | +7.1 | 7e-11 | 8/17 (NCI-H460, SW480, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **3.83×** | +6.3 | 1e-08 | 13/17 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.02×** | +5.8 | 2e-07 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.85×** | +3.9 | 0.003 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.006 | 0/18 | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.67×** | +3.3 | 0.031 | 1/11 (NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7675.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.622×** | -4.3 | 0.009 | 9/18 (C-33 A, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.632×** | -4.2 | 0.009 | 16/20 (NCI-H23, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.674×** | -3.6 | 0.065 | 10/16 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Malotilate (drug)]] 0.5 µM |  | 0.696× | -3.3 | 0.14 | 6/18 (NCI-H460, C-33 A, …) | two highest doses |  |
| [[Gefitinib (drug)]] 5 µM |  | 0.708× | -3.1 | 0.17 | 2/20 (BT-474, A-172) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.712× | -3.1 | 0.17 | 12/17 (A-427, SW480, …) | inconsistent across doses |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | 0.703× | -3.1 | 0.17 | 4/16 (PANC-1, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7675. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 6.09 | 7 | 9 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.35× (z +13.5) | [[Digitoxin (drug)]] 5 µM 0.0413× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.108× (z -12.7) |
| [[A-427 (line)]] | wt | 50.4 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0752× (z -18.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0307× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 15.9 | 0 | 10 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0340× (z -16.2) |
| [[PANC-1 (line)]] | alt | 0.973 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 23.0× (z +10.9) | — |
| [[A-172 (line)]] | wt | 9.73 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 8.96× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 21.1 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0347× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 1.76 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 22.8× (z +9.7) | — |
| [[A498 (line)]] | wt | 3.12 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 15.6× (z +9.6) | [[Simotinib (drug)]] 0.05 µM 0.0719× (z -8.6) |
| [[HOP62 (line)]] | alt | 1.88 | 1 | 0 | [[Panobinostat (drug)]] 0.05 µM 30.3× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 10.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -11.5) |
| [[A549 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.422 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.899 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.930 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.816 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.456 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.767 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.531 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.385 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.868 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.422 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.651 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.803 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.503 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7675), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPYSL5]] | +0.75 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[RET]] | +0.75 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[NOVA2]] | +0.72 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[GNAO1]] | +0.71 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[LPAR3]] | +0.69 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[KCNK13]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[EBF2]] | +0.68 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[SLC6A17]] | +0.67 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[GPRIN1]] | +0.65 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[KCNQ2]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[GPC3]] | +0.65 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[WSCD1]] | +0.65 | +0.55 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DECR1]] | -0.55 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[RNF146]] | -0.55 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[FBXW4]] | -0.52 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[DDX59]] | -0.52 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[GTF2IRD2]] | -0.50 | -0.33 / -0.31 | both halves | 2e-04 |  |
| [[DNAI4]] | -0.49 | -0.29 / -0.30 | both halves | 2e-04 |  |
| [[RC3H2]] | -0.49 | -0.23 / -0.40 | both halves | 5e-04 |  |
| [[MAIP1]] | -0.49 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[CCAR1]] | -0.49 | -0.29 / -0.36 | both halves | 2e-04 |  |
| [[ERCC6L2-AS1]] | -0.49 | -0.24 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARM1]] | B | PARM1 activity weakens JAKMIP1's drug response | lines that do not express PARM1 (11) vs lines expressing it (8) | the lines without PARM1 respond 1.41× as strongly (z diff -1.39); strongest at Dinaciclib 5 µM: 1.81x vs 0.76x (z diff -3.9) | 0.055 | ⚠ within organs, on part of the lines; also absent: ST6GAL2, PRR15L, C2CD4A; target measured in part of the lines; artifact flags |
| [[SDK1]] | C | SDK1 activity raises JAKMIP1's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 2.44× lower at baseline in the lines without SDK1 | 0.026 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3; co-absent with the target |
| [[NFASC]] | C | NFASC activity raises JAKMIP1's level | lines that do not express NFASC (27) vs lines expressing it (23) | 2.29× lower at baseline in the lines without NFASC | 0.049 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A; co-absent with the target |
| [[KIF1A]] | C | KIF1A activity raises JAKMIP1's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 2.87× lower at baseline in the lines without KIF1A | 0.051 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7; co-absent with the target |
| [[AFF2]] | C | AFF2 activity raises JAKMIP1's level | lines that do not express AFF2 (25) vs lines expressing it (25) | 2.19× lower at baseline in the lines without AFF2 | 0.069 | ⚠ within organs, on part of the lines; also absent: KIF1A, TMEM163, LINC02315; maybe low, not absent; co-absent with the target |
| [[NOVA2]] | C | NOVA2 activity raises JAKMIP1's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 2.39× lower at baseline in the lines without NOVA2 | 0.074 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1; co-absent with the target |
| [[SYT11]] | C | SYT11 activity raises JAKMIP1's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 1.97× lower at baseline in the lines without SYT11 | 0.096 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 5, C 11. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF146]] | B | JAKMIP1 activity raises RNF146's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 1.25× lower at baseline in the lines without JAKMIP1 | 0.024 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2 |
| [[SDK2]] | B | JAKMIP1 activity raises SDK2's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 2.98× lower at baseline in the lines without JAKMIP1 | 0.053 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2 |
| [[PTPRS]] | B | JAKMIP1 activity raises PTPRS's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 2.32× lower at baseline in the lines without JAKMIP1 | 0.054 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2 |
| [[IQSEC1]] | B | JAKMIP1 activity raises IQSEC1's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 1.87× lower at baseline in the lines without JAKMIP1 | 0.069 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2 |
| [[KCNK13]] | B | JAKMIP1 activity raises KCNK13's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 1.48× lower at baseline in the lines without JAKMIP1 | 0.073 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2 |
| [[CACNA1H]] | C | JAKMIP1 activity raises CACNA1H's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 3.53× lower at baseline in the lines without JAKMIP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2; co-absent with the target |
| [[JPH3]] | C | JAKMIP1 activity raises JPH3's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 4.24× lower at baseline in the lines without JAKMIP1 | 0.003 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2; co-absent with the target |
| [[SDK1]] | C | JAKMIP1 activity raises SDK1's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 3.36× lower at baseline in the lines without JAKMIP1 | 0.011 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2; co-absent with the target |
| [[OLFM1]] | C | JAKMIP1 activity raises OLFM1's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 4.11× lower at baseline in the lines without JAKMIP1 | 0.036 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2; co-absent with the target |
| [[MED12L]] | C | JAKMIP1 activity raises MED12L's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 3.34× lower at baseline in the lines without JAKMIP1 | 0.040 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2; co-absent with the target |
| [[CRMP1]] | C | JAKMIP1 activity raises CRMP1's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 2.98× lower at baseline in the lines without JAKMIP1 | 0.042 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2; co-absent with the target |
| [[LAMC3]] | C | JAKMIP1 activity raises LAMC3's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 2.70× lower at baseline in the lines without JAKMIP1 | 0.048 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.834). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.4, 39.2); signed map (27.1, 28.0). **Vector** length 58.4, 15.1% of its response variance represented; |z| ≥ 3 in 627 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +17.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +7.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +6.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | -0.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.9 | +2.7 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.7 | -1.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +0.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | janus kinase and microtubule interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:6,026,199-6,200,591 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MARLIN1, JAMIP1, Gababrbp, FLJ31564 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96N16](https://www.uniprot.org/uniprotkb/Q96N16) (Janus kinase and microtubule-interacting protein 1):

> Associates with microtubules and may play a role in the microtubule-dependent transport of the GABA-B receptor. May play a role in JAK1 signaling and regulate microtubule cytoskeleton rearrangements.

**Summary**, from NCBI Gene [152789](https://www.ncbi.nlm.nih.gov/gene/152789):

> Enables GABA receptor binding activity and RNA binding activity. Involved in cognition. Located in membrane. Part of ribonucleoprotein complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26460](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26460) · Entrez [152789](https://www.ncbi.nlm.nih.gov/gene/152789) · UniProt [Q96N16](https://www.uniprot.org/uniprotkb/Q96N16) · Ensembl [ENSG00000152969](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152969)

## Data

Gene col 7675: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7675); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7675, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7675]; `tensor/DDL_lfc|DDL_z.npy` [7675]; `embed/gene_vectors.npy` [7675]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7675 or target_col == 7675). Every well: [[JAKMIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JAKMIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
