---
symbol: "TENM2"
type: "gene"
col: 7045
ensembl_id: "ENSG00000145934"
name: "teneurin transmembrane protein 2"
location: "5q34"
module: 108
arm: "+"
pooled_cpm: 51.43
n_lines_expressing: 17
n_dd_up: 22
n_dd_down: 5
n_dd_up_clean: 18
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 8
direction_downstream: 34
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# TENM2

*teneurin transmembrane protein 2* — 5q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.83× (z +19.3, q 0e+00, up in 2 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.673× (z -5.2, q 1e-04, down in 13 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCF4]] (+0.66, fdr 9e-06), [[PDGFRB]] (+0.64, fdr 7e-06), [[ADGRB3]] (+0.64, fdr 7e-06); moves opposite to [[ARHGEF5]] (-0.47, fdr 5e-05), [[ARHGEF34P]] (-0.45, fdr 7e-05), [[IQANK1]] (-0.43, fdr 1e-04).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 34 go from it, the strongest it → [[PRSS23]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7045.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.83×** | +19.3 | 0e+00 | 2/15 (A-172, HS-578T) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.91×** | +13.5 | 9e-39 | 3/13 (RPMI-7951, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.74×** | +13.2 | 1e-37 | 1/14 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +11.4 | 7e-28 | 6/15 (BT-474, RPMI-7951, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.13×** | +9.9 | 5e-21 | 2/15 (A-172, HS-578T) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +8.6 | 6e-16 | 2/13 (BT-474, A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +5.9 | 2e-07 | 7/15 (BT-474, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.35×** | +5.5 | 2e-06 | 3/15 (A-172, BT-474, …) | top dose only | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.2 | 1e-05 | 2/16 (BT-474, A-172) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +4.6 | 3e-04 | 5/15 (BT-474, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.5 | 3e-04 | 2/15 (A-172, BT-474) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.41×** | +4.3 | 7e-04 | 6/15 (BT-474, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.020 | 6/15 (BT-474, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.027 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.030 | 0/15 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.034 | 8/14 (BT-474, HOP62, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.034 | 3/15 (SW 1271, NCI-H460, …) | all doses, flat |  |
| [[Ferulic acid (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.043 | 4/14 (SNU-423, A-172, …) | all doses, flat | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.069 | 5/15 (BT-474, HOP62, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7045.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.673×** | -5.2 | 1e-04 | 13/15 (NCI-H460, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.715×** | -4.4 | 0.003 | 10/15 (HOP62, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.765×** | -3.5 | 0.081 | 3/15 (H4, NCI-H460, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | **0.831×** | -3.4 | 0.081 | 7/15 (H4, A-172, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | **0.772×** | -3.4 | 0.081 | 1/15 (J82) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.792× | -3.1 | 0.19 | 0/15 | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.5 µM |  | 0.793× | -3.0 | 0.19 | 5/15 (HOP62, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7045. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 553 | 0 | 19 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0442× (z -25.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 192 | 0 | 16 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0292× (z -24.3) |
| [[LOX-IMVI (line)]] | wt | 166 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -13.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.164× (z -10.4) |
| [[BT-474 (line)]] | alt | 269 | 10 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 22.8× (z +15.8) | — |
| [[H4 (line)]] | wt | 50.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -10.0) ⚠ cell-cycle shift, explains ~35% of this change |
| [[C-33 A (line)]] | alt | 164 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -11.1) |
| [[A-172 (line)]] | wt | 21.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +10.8) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[J82 (line)]] | alt | 39.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.248× (z -8.7) ⚠ cell-cycle shift, explains ~53% of this change |
| [[NCI-H661 (line)]] | alt | 370 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.168× (z -11.7) |
| [[A-427 (line)]] | wt | 8.31 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.10 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.92 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.71 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.74 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.47 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.86 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.05 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.01 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.72 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.12 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.85 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.93 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.18 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.93 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.36 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.80 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.10 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.21 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.76 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.36 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.42 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.34 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.15 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.81 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.42 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.55 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.21 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7045), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF4]] | +0.66 | +0.57 / +0.66 | both halves | 9e-06 | **novel candidate** |
| [[PDGFRB]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[ADGRB3]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[CDH7]] | +0.63 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[ADAMTS6]] | +0.62 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[ANKRD30A]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[PDE3A]] | +0.60 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[SLC8A1]] | +0.59 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[APCDD1L]] | +0.57 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[APCDD1L-DT]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[NOL4]] | +0.57 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[NALF1]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF5]] | -0.47 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[ARHGEF34P]] | -0.45 | -0.48 / -0.37 | both halves | 7e-05 |  |
| [[IQANK1]] | -0.43 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[CEACAM1]] | -0.43 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[PSD4]] | -0.43 | -0.42 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers TENM2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[FBXL7]] | C | FBXL7 activity raises TENM2's level | lines that do not express FBXL7 (27) vs lines expressing it (23) | 5.52× lower at baseline in the lines without FBXL7 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, HS3ST3A1, FAM133A; co-absent with the target |
| [[PGR]] | C | PGR activity raises TENM2's level | lines that do not express PGR (36) vs lines expressing it (14) | 4.68× lower at baseline in the lines without PGR | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent; co-absent with the target |
| [[NTM]] | C | NTM activity raises TENM2's level | lines that do not express NTM (33) vs lines expressing it (17) | 5.36× lower at baseline in the lines without NTM | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1; co-absent with the target |
| [[ADAMTS6]] | C | ADAMTS6 activity raises TENM2's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 4.02× lower at baseline in the lines without ADAMTS6 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2; co-absent with the target |
| [[COL4A6]] | C | COL4A6 activity raises TENM2's level | lines that do not express COL4A6 (36) vs lines expressing it (14) | 2.60× lower at baseline in the lines without COL4A6 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX7, ENSG00000238054, LINC01035; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises TENM2's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 4.49× lower at baseline in the lines without PDGFRB | 0.079 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[FENDRR]] | C | FENDRR activity raises TENM2's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 4.31× lower at baseline in the lines without FENDRR | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10; co-absent with the target |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 3, C 31. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS23]] | B | TENM2 activity raises PRSS23's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 2.03× lower at baseline in the lines without TENM2 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1 |
| [[BMPER]] | B | TENM2 activity raises BMPER's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 3.30× lower at baseline in the lines without TENM2 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1 |
| [[SLCO1C1]] | B | TENM2 activity raises SLCO1C1's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 1.60× lower at baseline in the lines without TENM2 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1 |
| [[COL5A1]] | C | TENM2 activity raises COL5A1's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 8.88× lower at baseline in the lines without TENM2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1; co-absent with the target |
| [[PDGFRB]] | C | TENM2 activity raises PDGFRB's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 6.14× lower at baseline in the lines without TENM2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1; co-absent with the target |
| [[ADAMTS6]] | C | TENM2 activity raises ADAMTS6's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 4.74× lower at baseline in the lines without TENM2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1; co-absent with the target |
| [[SIRLNT]] | C | TENM2 activity raises SIRLNT's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 2.96× lower at baseline in the lines without TENM2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1; co-absent with the target |
| [[WNT5B]] | C | TENM2 activity raises WNT5B's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 4.96× lower at baseline in the lines without TENM2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1; co-absent with the target |
| [[COL6A2]] | C | TENM2 activity raises COL6A2's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 5.73× lower at baseline in the lines without TENM2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1; co-absent with the target |
| [[VEPH1]] | C | TENM2 activity raises VEPH1's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 2.39× lower at baseline in the lines without TENM2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1; co-absent with the target |
| [[PDCD1LG2]] | C | TENM2 activity raises PDCD1LG2's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 2.94× lower at baseline in the lines without TENM2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1; co-absent with the target |
| [[CDH13]] | C | TENM2 activity raises CDH13's level | lines that do not express TENM2 (33) vs lines expressing it (17) | 6.01× lower at baseline in the lines without TENM2 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: THY1, PDGFRB, COL3A1; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.528). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.5, 22.3); signed map (35.2, 43.4). **Vector** length 73.8, 27.4% of its response variance represented; |z| ≥ 3 in 530 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +2.2 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +13.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +1.6 | +5.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.3 | +3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +4.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.1 | -5.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -3.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.6 | -2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | teneurin transmembrane protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q34 — chr5:166,979,029-168,264,157 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1127, Ten-M2, TEN2; previously ODZ2 |
| Gene groups (HGNC) | Teneurin transmembrane protein family |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NT68](https://www.uniprot.org/uniprotkb/Q9NT68) (Teneurin-2):

> Involved in neural development, regulating the establishment of proper connectivity within the nervous system. Acts as a ligand of the ADGRL1 and ADGRL3 receptors that are expressed at the surface of adjacent cells. Promotes the formation of filopodia and enlarged growth cone in neuronal cells. Mediates axon guidance and homophilic and heterophilic cell-cell adhesion. May function as a cellular signal transducer.; [Isoform 2]: Acts as a ligand of the ADGRL1 receptor. Mediates axon guidance and …

**Summary**, from NCBI Gene [57451](https://www.ncbi.nlm.nih.gov/gene/57451):

> Enables cell adhesion molecule binding activity and signaling receptor binding activity. Involved in retrograde trans-synaptic signaling by trans-synaptic protein complex. Located in cell-cell junction and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29943](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29943) · Entrez [57451](https://www.ncbi.nlm.nih.gov/gene/57451) · UniProt [Q9NT68](https://www.uniprot.org/uniprotkb/Q9NT68) · Ensembl [ENSG00000145934](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145934)

## Data

Gene col 7045: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7045); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7045, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7045]; `tensor/DDL_lfc|DDL_z.npy` [7045]; `embed/gene_vectors.npy` [7045]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7045 or target_col == 7045). Every well: [[TENM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TENM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
