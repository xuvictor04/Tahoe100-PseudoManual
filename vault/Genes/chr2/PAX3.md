---
symbol: "PAX3"
type: "gene"
col: 5772
ensembl_id: "ENSG00000135903"
name: "paired box 3"
location: "2q36.1"
module: 108
arm: "+"
pooled_cpm: 19.47
n_lines_expressing: 12
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 12
direction_downstream: 8
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# PAX3

*paired box 3* — 2q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.75× (z +12.6, q 2e-33, up in 0 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.35× (z +11.5, q 4e-28, up in 5 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Diphenhydramine (drug)]] 0.05 µM: 0.593× (z -4.6, q 0.003, down in 0 of 10 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02267]] (+0.71, fdr 7e-06), [[ACSS3]] (+0.66, fdr 9e-06), [[CNRIP1]] (+0.64, fdr 1e-05).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[NLGN1]] → it (grade C ⚠); 8 go from it, the strongest it → [[OCA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5772.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.75×** | +12.6 | 2e-33 | 0/9 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +11.5 | 4e-28 | 5/10 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.09×** | +10.3 | 1e-22 | 0/8 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.03×** | +9.7 | 3e-20 | 0/9 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.49×** | +4.5 | 7e-04 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.0 | 0.004 | 3/10 (H4, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.004 | 1/10 (SNU-423) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.030 | 0/10 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.49×** | +3.5 | 0.030 | 1/10 (NCI-H23) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | 1.38× | +3.1 | 0.10 | 4/10 (SNU-423, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 0.5 µM |  | 1.38× | +3.1 | 0.10 | 0/10 | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.38× | +3.0 | 0.11 | 0/10 | top dose only | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5772.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.593×** | -4.6 | 0.003 | 0/10 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.643×** | -4.0 | 0.016 | 6/10 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | **0.647×** | -3.8 | 0.025 | 0/10 | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.674×** | -3.5 | 0.070 | 0/10 | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.681×** | -3.4 | 0.070 | 1/10 (SK-MEL-2) | inconsistent across doses |  |
| [[MK-8353 (drug)]] 0.5 µM |  | **0.509×** | -3.3 | 0.070 | 0/10 | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.706×** | -3.3 | 0.070 | 6/10 (LOX-IMVI, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.708×** | -3.3 | 0.070 | 5/10 (NCI-H460, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.692×** | -3.2 | 0.070 | 0/10 | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.712×** | -3.2 | 0.070 | 1/10 (HOP62) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.713×** | -3.2 | 0.070 | 4/10 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.723×** | -3.1 | 0.098 | 0/10 | inconsistent across doses |  |
| [[DTP3 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.728× | -3.0 | 0.11 | 0/10 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5772. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 253 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 17.9 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.217× (z -10.3) |
| [[NCI-H23 (line)]] | alt | 24.9 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +9.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0781× (z -16.5) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0793× (z -8.9) |
| [[C32 (line)]] | wt | 376 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -15.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -9.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0749× (z -13.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -11.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0822× (z -8.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.36 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5772), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02267]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[ACSS3]] | +0.66 | +0.65 / +0.57 | both halves | 9e-06 | **novel candidate** |
| [[CNRIP1]] | +0.64 | +0.59 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[PTPRD]] | +0.63 | +0.55 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[COL19A1]] | +0.61 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[MIR548XHG]] | +0.61 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[C10orf90]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[RHOJ]] | +0.60 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[LRAT]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[ZNF521]] | +0.59 | +0.49 / +0.69 | both halves | 1e-05 | pathway: Gastrulation |
| [[LEF1]] | +0.58 | +0.48 / +0.63 | both halves | 2e-05 | pathway: Gastrulation; STRING 663 |
| [[LEF1-AS1]] | +0.58 | +0.42 / +0.64 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NLGN1]] | C | NLGN1 activity raises PAX3's level | lines that do not express NLGN1 (30) vs lines expressing it (20) | 3.76× lower at baseline in the lines without NLGN1 | 0.014 | ⚠ within organs, on part of the lines; also absent: EPB41L3, PAX3, NEGR1; co-absent with the target |
| [[C10orf90]] | C | C10orf90 activity raises PAX3's level | lines that do not express C10orf90 (35) vs lines expressing it (15) | 4.80× lower at baseline in the lines without C10orf90 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GRIN2A, LINC01242, ADGRG7; maybe low, not absent; co-absent with the target |
| [[EPHA3]] | C | EPHA3 activity raises PAX3's level | lines that do not express EPHA3 (26) vs lines expressing it (24) | 3.23× lower at baseline in the lines without EPHA3 | 0.024 | ⚠ within organs, on part of the lines; also absent: ADGRB3, MARCHF1, LINC00491; co-absent with the target |
| [[FBXL7]] | C | FBXL7 activity raises PAX3's level | lines that do not express FBXL7 (27) vs lines expressing it (23) | 3.78× lower at baseline in the lines without FBXL7 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, HS3ST3A1, FAM133A; co-absent with the target |
| [[LEF1-AS1]] | C | LEF1-AS1 activity raises PAX3's level | lines that do not express LEF1-AS1 (33) vs lines expressing it (17) | 5.18× lower at baseline in the lines without LEF1-AS1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent; co-absent with the target |
| [[COL19A1]] | C | COL19A1 activity raises PAX3's level | lines that do not express COL19A1 (36) vs lines expressing it (14) | 6.49× lower at baseline in the lines without COL19A1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: AEBP1, ENSG00000224865, ADGRG7; co-absent with the target |
| [[EDNRB]] | C | EDNRB activity raises PAX3's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 5.31× lower at baseline in the lines without EDNRB | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[PANTR1]] | C | PANTR1 activity raises PAX3's level | lines that do not express PANTR1 (37) vs lines expressing it (13) | 2.93× lower at baseline in the lines without PANTR1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: POU3F3, LINC01508, TIMD4; co-absent with the target |
| [[LINC01684]] | C | LINC01684 activity raises PAX3's level | lines that do not express LINC01684 (30) vs lines expressing it (20) | 1.99× lower at baseline in the lines without LINC01684 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IRAG2, COL3A1, LINC01592; maybe low, not absent; co-absent with the target |
| [[ADGRB3]] | C | ADGRB3 activity raises PAX3's level | lines that do not express ADGRB3 (28) vs lines expressing it (22) | 3.78× lower at baseline in the lines without ADGRB3 | 0.081 | ⚠ within organs, on part of the lines; also absent: EPHA3, NCAM2, ST8SIA4; co-absent with the target |
| [[LINC01242]] | C | LINC01242 activity raises PAX3's level | lines that do not express LINC01242 (42) vs lines expressing it (8) | 3.32× lower at baseline in the lines without LINC01242 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, LINC00879, ENSG00000234426; maybe low, not absent; co-absent with the target |
| [[DAAM2]] | C | DAAM2 activity raises PAX3's level | lines that do not express DAAM2 (27) vs lines expressing it (23) | 3.14× lower at baseline in the lines without DAAM2 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GDNF-AS1, ZNF471, SDC2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OCA2]] | B | PAX3 activity raises OCA2's level | lines that do not express PAX3 (38) vs lines expressing it (12) | 3.56× lower at baseline in the lines without PAX3 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, ENSG00000241168 |
| [[CCDC102B]] | B | PAX3 activity raises CCDC102B's level | lines that do not express PAX3 (38) vs lines expressing it (12) | 3.47× lower at baseline in the lines without PAX3 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, ENSG00000241168 |
| [[DAAM2]] | C | PAX3 activity raises DAAM2's level | lines that do not express PAX3 (38) vs lines expressing it (12) | 2.84× lower at baseline in the lines without PAX3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, ENSG00000241168; co-absent with the target |
| [[COL19A1]] | C | PAX3 activity raises COL19A1's level | lines that do not express PAX3 (38) vs lines expressing it (12) | 3.49× lower at baseline in the lines without PAX3 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, ENSG00000241168; co-absent with the target |
| [[ADGRB3]] | C | PAX3 activity raises ADGRB3's level | lines that do not express PAX3 (38) vs lines expressing it (12) | 4.62× lower at baseline in the lines without PAX3 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, ENSG00000241168; co-absent with the target |
| [[EPHA3]] | C | PAX3 activity raises EPHA3's level | lines that do not express PAX3 (38) vs lines expressing it (12) | 5.32× lower at baseline in the lines without PAX3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, ENSG00000241168; co-absent with the target |
| [[EDNRB]] | C | PAX3 activity raises EDNRB's level | lines that do not express PAX3 (38) vs lines expressing it (12) | 2.32× lower at baseline in the lines without PAX3 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, ENSG00000241168; co-absent with the target |
| [[C10orf90]] | C | PAX3 activity raises C10orf90's level | lines that do not express PAX3 (38) vs lines expressing it (12) | 4.06× lower at baseline in the lines without PAX3 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, LINC01425, ENSG00000241168; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.1, 27.6); signed map (33.1, 41.9). **Vector** length 42.7, 16.3% of its response variance represented; |z| ≥ 3 in 258 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +10.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | +1.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | -0.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.9 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.8 | +2.8 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -3.4 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -1.4 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.9 | -0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.9 | +0.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -0.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | paired box 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.1 — chr2:222,199,887-222,298,998 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HUP2, PAX-3; previously WS1 |
| Gene groups (HGNC) | PRD class homeoboxes and pseudogenes; Paired boxes |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 7 pathways, smallest: Specification of the neural plate border; Transcriptional and post-translational regulation of MITF-M expression and activity; Gastrulation |
| Matched by | ensembl_id |

**Function**, from UniProt [P23760](https://www.uniprot.org/uniprotkb/P23760) (Paired box protein Pax-3):

> Transcription factor that may regulate cell proliferation, migration and apoptosis. Involved in neural development and myogenesis. Transcriptional activator of MITF, acting synergistically with SOX10.

**Summary**, from NCBI Gene [5077](https://www.ncbi.nlm.nih.gov/gene/5077):

> This gene is a member of the paired box (PAX) family of transcription factors. Members of the PAX family typically contain a paired box domain and a paired-type homeodomain. These genes play critical roles during fetal development. Mutations in paired box gene 3 are associated with Waardenburg syndrome, craniofacial-deafness-hand syndrome, and alveolar rhabdomyosarcoma. The translocation t(2;13)(q35;q14), which represents a fusion between PAX3 and the forkhead gene, is a frequent finding in …

**Accessions** — [HGNC:8617](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8617) · Entrez [5077](https://www.ncbi.nlm.nih.gov/gene/5077) · UniProt [P23760](https://www.uniprot.org/uniprotkb/P23760) · Ensembl [ENSG00000135903](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135903)

## Data

Gene col 5772: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5772); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5772, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5772]; `tensor/DDL_lfc|DDL_z.npy` [5772]; `embed/gene_vectors.npy` [5772]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5772 or target_col == 5772). Every well: [[PAX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
