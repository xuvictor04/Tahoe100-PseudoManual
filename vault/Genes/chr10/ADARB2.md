---
symbol: "ADARB2"
type: "gene"
col: 11724
ensembl_id: "ENSG00000185736"
name: "adenosine deaminase RNA specific B2 (inactive)"
location: "10p15.3"
module: 9
arm: "+"
pooled_cpm: 47.42
n_lines_expressing: 11
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 21
direction_downstream: 13
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ADARB2

*adenosine deaminase RNA specific B2 (inactive)* — 10p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.42× (z +19.3, q 0e+00, up in 6 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.527× (z -4.8, q 1e-03, down in 4 of 8 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB3C]] (+0.70, fdr 1e-05), [[LINC01035]] (+0.69, fdr 7e-06), [[PCSK1]] (+0.69, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[BMP5]] → it (grade C ⚠); 13 go from it, the strongest it → [[KCNMB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11724.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.42×** | +19.3 | 0e+00 | 6/8 (NCI-H2030, COLO 205, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.31×** | +11.8 | 9e-30 | 2/7 (NCI-H2030, H4) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.56×** | +10.3 | 2e-22 | 5/8 (NCI-H2030, H4, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +10.0 | 2e-21 | 3/9 (NCI-H2030, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.02×** | +8.3 | 2e-14 | 2/6 (NCI-H2030, H4) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.57×** | +7.6 | 2e-12 | 5/8 (COLO 205, AN3 CA, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +7.4 | 2e-11 | 1/6 (NCI-H2030) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.47×** | +7.0 | 2e-10 | 5/8 (COLO 205, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.67×** | +4.1 | 0.002 | 1/8 (H4) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.99×** | +4.0 | 0.004 | 1/8 (H4) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.62×** | +3.9 | 0.005 | 2/7 (NCI-H460, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.008 | 4/9 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.58×** | +3.7 | 0.009 | 1/8 (NCI-H2030) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +3.6 | 0.011 | 0/11 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.31×** | +3.5 | 0.015 | 1/5 (NCI-H2030) | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.038 | 1/8 (NCI-H2030) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11724.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.527×** | -4.8 | 1e-03 | 4/8 (NCI-H460, AN3 CA, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.589×** | -4.1 | 0.010 | 4/11 (NCI-H460, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.700×** | -4.0 | 0.011 | 3/9 (H4, NCI-H460, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.614×** | -3.9 | 0.012 | 2/8 (NCI-H460, AN3 CA) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.679× | -3.1 | 0.20 | 3/8 (NCI-H2030, H4, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11724. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 1,085 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -13.9) |
| [[NCI-H2030 (line)]] | alt | 17.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 61.8× (z +24.0) | — |
| [[COLO 205 (line)]] | alt | 13.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 31.7× (z +16.4) | — |
| [[NCI-H23 (line)]] | alt | 134 | 1 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 1.64× (z +8.5) ⚠ position not correctable | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -11.0) |
| [[H4 (line)]] | wt | 17.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 13.5× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 374 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -9.8) |
| [[A-172 (line)]] | wt | 7.24 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.95 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.21 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.52 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.17 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.09 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.84 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.51 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.41 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.73 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.71 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.26 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.47 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.29 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.87 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.57 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.87 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.84 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.78 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.22 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.38 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.67 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.99 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.90 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.35 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.64 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11724), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3C]] | +0.70 | +0.50 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[LINC01035]] | +0.69 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[PCSK1]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[FGF14]] | +0.68 | +0.62 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[BMP5]] | +0.68 | +0.59 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[LRFN2]] | +0.64 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[GRIK1]] | +0.64 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[LINC02197]] | +0.64 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[SCG2]] | +0.63 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[CDH10]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[SRRM4]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[ASCL1]] | +0.61 | +0.66 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 0, C 21. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMP5]] | C | BMP5 activity raises ADARB2's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 5.12× lower at baseline in the lines without BMP5 | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3; co-absent with the target |
| [[LINC01035]] | C | LINC01035 activity raises ADARB2's level | lines that do not express LINC01035 (43) vs lines expressing it (7) | 11.07× lower at baseline in the lines without LINC01035 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, CALCA, GSG1L2; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises ADARB2's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 4.79× lower at baseline in the lines without DPP10 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[PCSK1]] | C | PCSK1 activity raises ADARB2's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 3.91× lower at baseline in the lines without PCSK1 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[NKAIN2]] | C | NKAIN2 activity raises ADARB2's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 2.84× lower at baseline in the lines without NKAIN2 | 0.019 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[VIPR2]] | C | VIPR2 activity raises ADARB2's level | lines that do not express VIPR2 (32) vs lines expressing it (18) | 3.33× lower at baseline in the lines without VIPR2 | 0.036 | ⚠ within organs, on part of the lines; also absent: DPP10, KCNH5, ASXL3; maybe low, not absent; co-absent with the target |
| [[POU6F2]] | C | POU6F2 activity raises ADARB2's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 2.93× lower at baseline in the lines without POU6F2 | 0.038 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent; co-absent with the target |
| [[PDE10A]] | C | PDE10A activity raises ADARB2's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 2.19× lower at baseline in the lines without PDE10A | 0.044 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90; co-absent with the target |
| [[ASXL3]] | C | ASXL3 activity raises ADARB2's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 3.11× lower at baseline in the lines without ASXL3 | 0.044 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent; co-absent with the target |
| [[SGIP1]] | C | SGIP1 activity raises ADARB2's level | lines that do not express SGIP1 (31) vs lines expressing it (19) | 2.85× lower at baseline in the lines without SGIP1 | 0.051 | ⚠ within organs, on part of the lines; also absent: MEG3, HGF, MIR493HG; co-absent with the target |
| [[RAB3C]] | C | RAB3C activity raises ADARB2's level | lines that do not express RAB3C (31) vs lines expressing it (19) | 2.80× lower at baseline in the lines without RAB3C | 0.060 | ⚠ within organs, on part of the lines; also absent: VGF, SCG3, CDH10; maybe low, not absent; co-absent with the target |
| [[SLITRK4]] | C | SLITRK4 activity raises ADARB2's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 3.13× lower at baseline in the lines without SLITRK4 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 2, C 11. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNMB2]] | B | ADARB2 activity raises KCNMB2's level | lines that do not express ADARB2 (39) vs lines expressing it (11) | 3.14× lower at baseline in the lines without ADARB2 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, GSG1L2 |
| [[AGBL1]] | B | ADARB2 activity raises AGBL1's level | lines that do not express ADARB2 (39) vs lines expressing it (11) | 1.82× lower at baseline in the lines without ADARB2 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, GSG1L2 |
| [[RAB3C]] | C | ADARB2 activity raises RAB3C's level | lines that do not express ADARB2 (39) vs lines expressing it (11) | 2.80× lower at baseline in the lines without ADARB2 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, GSG1L2; co-absent with the target |
| [[BMP5]] | C | ADARB2 activity raises BMP5's level | lines that do not express ADARB2 (39) vs lines expressing it (11) | 4.21× lower at baseline in the lines without ADARB2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, GSG1L2; co-absent with the target |
| [[NKAIN2]] | C | ADARB2 activity raises NKAIN2's level | lines that do not express ADARB2 (39) vs lines expressing it (11) | 3.25× lower at baseline in the lines without ADARB2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, GSG1L2; co-absent with the target |
| [[PDE10A]] | C | ADARB2 activity raises PDE10A's level | lines that do not express ADARB2 (39) vs lines expressing it (11) | 3.97× lower at baseline in the lines without ADARB2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, GSG1L2; co-absent with the target |
| [[NCKAP5-AS2]] | C | ADARB2 activity raises NCKAP5-AS2's level | lines that do not express ADARB2 (39) vs lines expressing it (11) | 2.05× lower at baseline in the lines without ADARB2 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, GSG1L2; co-absent with the target |
| [[LINC01035]] | C | ADARB2 activity raises LINC01035's level | lines that do not express ADARB2 (39) vs lines expressing it (11) | 3.57× lower at baseline in the lines without ADARB2 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, GSG1L2; co-absent with the target |
| [[DPP10]] | C | ADARB2 activity raises DPP10's level | lines that do not express ADARB2 (39) vs lines expressing it (11) | 2.90× lower at baseline in the lines without ADARB2 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, GSG1L2; co-absent with the target |
| [[SNAP25]] | C | ADARB2 activity raises SNAP25's level | lines that do not express ADARB2 (39) vs lines expressing it (11) | 3.76× lower at baseline in the lines without ADARB2 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, GSG1L2; co-absent with the target |
| [[H19]] | C | ADARB2 activity raises H19's level | lines that do not express ADARB2 (39) vs lines expressing it (11) | 2.28× lower at baseline in the lines without ADARB2 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, GSG1L2; co-absent with the target |
| [[MARCHF1]] | C | ADARB2 activity raises MARCHF1's level | lines that do not express ADARB2 (39) vs lines expressing it (11) | 2.51× lower at baseline in the lines without ADARB2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, GSG1L2; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.591). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.1, 35.8); signed map (45.1, 35.8). **Vector** length 39.0, 15.5% of its response variance represented; |z| ≥ 3 in 216 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +19.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +7.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.4 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -4.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.2 | -4.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | adenosine deaminase RNA specific B2 (inactive) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.3 — chr10:1,177,313-1,737,525 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RED2, hRED2, ADAR3 |
| Gene groups (HGNC) | Adenosine deaminases acting on RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NS39](https://www.uniprot.org/uniprotkb/Q9NS39) (Inactive double-stranded RNA-specific editase B2):

> Single- and double-stranded RNA-binding protein that interferes with the RNA editing activities of ADAR/ADAR1 and ADARB1/ADAR2. Likely competes with these proteins for target binding, repressing RNA editing across the transcriptome. Additionally, it binds and stabilizes specific mRNAs and regulates the expression of proteins such as MAVS, DUSP1, and EGR1, independently of RNA editing mechanisms.

**Summary**, from NCBI Gene [105](https://www.ncbi.nlm.nih.gov/gene/105):

> This gene encodes a member of the double-stranded RNA adenosine deaminase family of RNA-editing enzymes and may play a regulatory role in RNA editing. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:227](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:227) · Entrez [105](https://www.ncbi.nlm.nih.gov/gene/105) · UniProt [Q9NS39](https://www.uniprot.org/uniprotkb/Q9NS39) · Ensembl [ENSG00000185736](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185736)

## Data

Gene col 11724: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11724); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11724, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11724]; `tensor/DDL_lfc|DDL_z.npy` [11724]; `embed/gene_vectors.npy` [11724]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11724 or target_col == 11724). Every well: [[ADARB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADARB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
