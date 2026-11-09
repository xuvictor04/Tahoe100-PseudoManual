---
symbol: "HHIPL2"
type: "gene"
col: 6761
ensembl_id: "ENSG00000143512"
name: "HHIP like 2"
location: "1q41"
module: 66
arm: "+"
pooled_cpm: 2.54
n_lines_expressing: 36
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 9
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# HHIPL2

*HHIP like 2* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.67× (z +15.8, q 0e+00, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.54× (z +10.6, q 5e-24, up in 7 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.0921×); [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.189×); [[Harringtonine (drug)]] 5 µM in 1 line (H4 0.122×; ⚠ cell-cycle shift, explains ~20% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0586×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MXRA8]] (+0.59, fdr 5e-05), [[KRT14]] (+0.54, fdr 2e-05), [[COL5A2]] (+0.53, fdr 3e-05); moves opposite to [[FBXL4]] (-0.44, fdr 3e-04), [[DDX50]] (-0.42, fdr 1e-04), [[APPL2]] (-0.41, fdr 8e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SSC5D]] → it (grade B ⚠); 9 go from it, the strongest it → [[EFHD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6761.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.67×** | +15.8 | 0e+00 | 3/4 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.32×** | +14.9 | 0e+00 | 5/8 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +10.6 | 5e-24 | 7/15 (SW 900, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.11×** | +10.1 | 5e-22 | 3/4 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.60×** | +9.9 | 4e-21 | 4/8 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.32×** | +9.6 | 8e-20 | 3/20 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.45×** | +7.2 | 5e-11 | 4/19 (HOP62, LoVo, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.5 | 3e-06 | 1/28 (A-172) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.93×** | +5.3 | 7e-06 | 8/29 (J82, SK-MEL-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.88×** | +4.9 | 7e-05 | 8/14 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +4.8 | 8e-05 | 4/28 (RPMI-7951, H4, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +4.6 | 2e-04 | 2/18 (LoVo, HOP62) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.79×** | +4.5 | 3e-04 | 2/10 (NCI-H1573, PANC-1) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.1 | 0.002 | 0/10 | top dose only | cell-cycle shift (explains ~7% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.47×** | +3.8 | 0.005 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.57×** | +3.6 | 0.011 | 8/21 (H4, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.023 | 4/27 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.53×** | +3.4 | 0.023 | 1/11 (PANC-1) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **2.14×** | +3.2 | 0.040 | 1/22 (NCI-H460) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.62×** | +3.0 | 0.076 | 0/10 | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +3.0 | 0.078 | 2/19 (J82, HOP62) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.46×** | +2.9 | 0.084 | 11/21 (PANC-1, H4, …) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.46×** | +2.9 | 0.084 | 0/13 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6761.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.0921×); [[Homoharringtonine (drug)]] 5 µM in 1 line (H4 0.189×); [[Harringtonine (drug)]] 5 µM in 1 line (H4 0.122×; ⚠ cell-cycle shift, explains ~20% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0586×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | 0.638× | -3.7 | 0.13 | 11/28 (A-172, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Azithromycin (hydrate) (drug)]] 0.5 µM |  | 0.684× | -3.1 | 0.51 | 3/21 (NCI-H1573, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6761. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 24.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -10.4) |
| [[PANC-1 (line)]] | alt | 7.16 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.30× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0921× (z -11.9) |
| [[A498 (line)]] | wt | 2.69 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.5 µM 0.0914× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 4.09 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0586× (z -8.8) |
| [[A-172 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.778 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.592 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.803 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.748 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.776 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.516 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.931 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.666 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.691 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.525 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.733 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.546 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.641 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.909 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.556 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.585 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6761), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXRA8]] | +0.59 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[KRT14]] | +0.54 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[COL5A2]] | +0.53 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[MAP1A]] | +0.53 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[B3GNT9]] | +0.53 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[ARHGEF6]] | +0.53 | +0.38 / +0.60 | both halves | 6e-05 |  |
| [[NID2]] | +0.52 | +0.31 / +0.56 | both halves | 2e-04 |  |
| [[NREP]] | +0.51 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[GLIS1]] | +0.51 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[MATN3]] | +0.51 | +0.36 / +0.41 | both halves | 9e-05 |  |
| [[LINC00842]] | +0.50 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[TDO2]] | +0.50 | +0.52 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXL4]] | -0.44 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[DDX50]] | -0.42 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[APPL2]] | -0.41 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[TIPRL]] | -0.41 | -0.29 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSC5D]] | B | SSC5D activity raises HHIPL2's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.81× lower at baseline in the lines without SSC5D | 0.081 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFHD1]] | B | HHIPL2 activity raises EFHD1's level | lines that do not express HHIPL2 (14) vs lines expressing it (36) | 2.03× lower at baseline in the lines without HHIPL2 | 0.010 | ⚠ within organs, on part of the lines; also absent: PRKD1, BNIP3, SPART; maybe low, not absent |
| [[ARHGEF6]] | B | HHIPL2 activity raises ARHGEF6's level | lines that do not express HHIPL2 (14) vs lines expressing it (36) | 2.90× lower at baseline in the lines without HHIPL2 | 0.035 | ⚠ within organs, on part of the lines; also absent: PRKD1, BNIP3, SPART; maybe low, not absent |
| [[SSC5D]] | B | HHIPL2 activity raises SSC5D's level | lines that do not express HHIPL2 (14) vs lines expressing it (36) | 2.09× lower at baseline in the lines without HHIPL2 | 0.083 | ⚠ within organs, on part of the lines; also absent: PRKD1, BNIP3, SPART; maybe low, not absent |
| [[MXRA8]] | B | HHIPL2 activity raises MXRA8's level | lines that do not express HHIPL2 (14) vs lines expressing it (36) | 1.74× lower at baseline in the lines without HHIPL2 | 0.087 | ⚠ within organs, on part of the lines; also absent: PRKD1, BNIP3, SPART; maybe low, not absent |
| [[BEND6]] | C | HHIPL2 activity raises BEND6's level | lines that do not express HHIPL2 (14) vs lines expressing it (36) | 2.69× lower at baseline in the lines without HHIPL2 | 0.022 | ⚠ within organs, on part of the lines; also absent: PRKD1, BNIP3, SPART; maybe low, not absent; co-absent with the target |
| [[BVES-AS1]] | C | HHIPL2 activity raises BVES-AS1's level | lines that do not express HHIPL2 (14) vs lines expressing it (36) | 1.98× lower at baseline in the lines without HHIPL2 | 0.042 | ⚠ within organs, on part of the lines; also absent: PRKD1, BNIP3, SPART; maybe low, not absent; co-absent with the target |
| [[SAMD11]] | C | HHIPL2 activity raises SAMD11's level | lines that do not express HHIPL2 (14) vs lines expressing it (36) | 3.50× lower at baseline in the lines without HHIPL2 | 0.081 | ⚠ within organs, on part of the lines; also absent: PRKD1, BNIP3, SPART; maybe low, not absent; co-absent with the target |
| [[GLIS1]] | C | HHIPL2 activity raises GLIS1's level | lines that do not express HHIPL2 (14) vs lines expressing it (36) | 3.58× lower at baseline in the lines without HHIPL2 | 0.094 | ⚠ within organs, on part of the lines; also absent: PRKD1, BNIP3, SPART; maybe low, not absent; co-absent with the target |
| [[B4GALNT1]] | C | HHIPL2 activity raises B4GALNT1's level | lines that do not express HHIPL2 (14) vs lines expressing it (36) | 3.53× lower at baseline in the lines without HHIPL2 | 0.095 | ⚠ within organs, on part of the lines; also absent: PRKD1, BNIP3, SPART; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.539). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (56.7, 21.3); signed map (52.8, -14.2). **Vector** length 41.6, 6.98% of its response variance represented; |z| ≥ 3 in 674 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +10.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +10.6 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.8 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +7.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +2.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.8 | -3.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -1.8 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -0.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | HHIP like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:222,522,258-222,548,104 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13840; previously KIAA1822L |
| Matched by | ensembl_id |

UniProt [Q6UWX4](https://www.uniprot.org/uniprotkb/Q6UWX4) carries no function annotation.

**Summary**, from NCBI Gene [79802](https://www.ncbi.nlm.nih.gov/gene/79802):

> Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25842](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25842) · Entrez [79802](https://www.ncbi.nlm.nih.gov/gene/79802) · UniProt [Q6UWX4](https://www.uniprot.org/uniprotkb/Q6UWX4) · Ensembl [ENSG00000143512](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143512)

## Data

Gene col 6761: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6761); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6761, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6761]; `tensor/DDL_lfc|DDL_z.npy` [6761]; `embed/gene_vectors.npy` [6761]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6761 or target_col == 6761). Every well: [[HHIPL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HHIPL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
