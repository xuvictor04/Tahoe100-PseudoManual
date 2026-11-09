---
symbol: "ADGRE2"
type: "gene"
col: 4815
ensembl_id: "ENSG00000127507"
name: "adhesion G protein-coupled receptor E2"
location: "19p13.12"
module: 174
arm: "+"
pooled_cpm: 10.46
n_lines_expressing: 25
n_dd_up: 6
n_dd_down: 35
n_dd_up_clean: 4
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 16
direction_downstream: 11
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# ADGRE2

*adhesion G protein-coupled receptor E2* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.82× (z +13.5, q 9e-39, up in 17 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (2 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.417× (z -7.4, q 8e-11, down in 16 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFRSF6B]] (+0.72, fdr 1e-05), [[NIBAN2]] (+0.66, fdr 8e-06), [[DUSP6]] (+0.65, fdr 7e-06).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[MTSS1]] → it (grade B ⚠); 11 go from it, the strongest it → [[SLCO4A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4815.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.82×** | +13.5 | 9e-39 | 17/23 (NCI-H460, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.84×** | +9.6 | 2e-19 | 16/22 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +6.7 | 4e-09 | 1/9 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +5.5 | 5e-06 | 1/13 (NCI-H1792) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +5.4 | 6e-06 | 10/22 (NCI-H460, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.58×** | +4.2 | 0.002 | 6/22 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | 1.38× | +3.0 | 0.20 | 4/22 (CFPAC-1, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 2 with an alert ⚠; shown: the 15 strongest. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4815.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.417×** | -7.4 | 8e-11 | 16/22 (HOP62, BT-474, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.469×** | -7.3 | 1e-10 | 21/23 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.445×** | -7.1 | 2e-10 | 19/22 (HOP62, RPMI-7951, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.565×** | -6.5 | 2e-08 | 17/23 (HOP62, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.578×** | -5.8 | 7e-07 | 17/23 (HOP62, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.648×** | -5.5 | 3e-06 | 18/22 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.535×** | -5.5 | 3e-06 | 15/21 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.577×** | -5.0 | 4e-05 | 12/21 (H4, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.588×** | -4.8 | 8e-05 | 17/22 (HOP62, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.683×** | -4.8 | 8e-05 | 13/23 (BT-474, NCI-H460, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.655×** | -4.8 | 8e-05 | 17/23 (HOP62, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.598×** | -4.7 | 1e-04 | 13/22 (HOP62, BT-474, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.602×** | -4.6 | 2e-04 | 16/22 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.645×** | -4.0 | 0.003 | 12/22 (HOP62, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.640×** | -3.9 | 0.004 | 8/22 (NCI-H1573, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4815. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 38.3 | 0 | 22 (8 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0478× (z -13.0) |
| [[BT-474 (line)]] | alt | 21.0 | 0 | 10 | — | [[Neratinib (drug)]] 5 µM 0.0139× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 28.5 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -13.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.152× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 41.2 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -13.3) |
| [[RPMI-7951 (line)]] | alt | 57.5 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0541× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.117× (z -10.9) |
| [[SW 900 (line)]] | alt | 44.8 | 0 | 4 (1 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0503× (z -10.1) |
| [[SW480 (line)]] | alt | 28.6 | 0 | 4 | — | [[Cobimetinib (drug)]] 5 µM 0.296× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 20.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -11.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H460 (line)]] | wt | 7.19 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 4.45× (z +10.5) | [[Binimetinib (drug)]] 0.05 µM 0.270× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 38.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -9.8) |
| [[H4 (line)]] | wt | 9.39 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0356× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 30.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.256× (z -9.7) |
| [[SW1417 (line)]] | alt | 9.16 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.96× (z +8.9) | — |
| [[SW48 (line)]] | wt | 24.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0687× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.920 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.940 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.975 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4815), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF6B]] | +0.72 | +0.57 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[NIBAN2]] | +0.66 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[DUSP6]] | +0.65 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[SERPINA1]] | +0.63 | +0.52 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[PTPN12]] | +0.62 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[TREM1]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 | same gene group |
| [[HPCAL1]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ADAM28]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ST3GAL1]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[PITPNC1]] | +0.60 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[TGM2]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[S100A9]] | +0.60 | +0.51 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 12, C 4. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTSS1]] | B | MTSS1 activity strengthens ADGRE2's drug response | lines that do not express MTSS1 (10) vs lines expressing it (13) | the lines without MTSS1 respond 0.95× as strongly (z diff +0.74); strongest at Trametinib 5 µM: 0.40x vs 0.23x (z diff +3.7) | 0.014 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1; target measured in part of the lines; artifact flags |
| [[ABCC3]] | B | ABCC3 activity raises ADGRE2's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.71× lower at baseline in the lines without ABCC3 | 0.017 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[NPAS2]] | B | NPAS2 activity raises ADGRE2's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 2.58× lower at baseline in the lines without NPAS2 | 0.019 | ⚠ within organs, on part of the lines |
| [[GALNT18]] | B | GALNT18 activity raises ADGRE2's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 3.04× lower at baseline in the lines without GALNT18 | 0.044 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[FMN1]] | B | FMN1 activity raises ADGRE2's level | lines that do not express FMN1 (17) vs lines expressing it (33) | 2.39× lower at baseline in the lines without FMN1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000278266, LINC02405, ENSG00000286016; maybe low, not absent |
| [[TRIB2]] | B | TRIB2 activity raises ADGRE2's level | lines that do not express TRIB2 (10) vs lines expressing it (40) | 2.60× lower at baseline in the lines without TRIB2 | 0.047 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ADGRE2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[LINC02813]] | B | LINC02813 activity raises ADGRE2's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 2.01× lower at baseline in the lines without LINC02813 | 0.068 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[GNA15]] | B | GNA15 activity weakens ADGRE2's drug response | lines that do not express GNA15 (13) vs lines expressing it (10) | the lines without GNA15 respond 1.30× as strongly (z diff -0.61); strongest at Dinaciclib 0.05 µM: 0.97x vs 0.25x (z diff -5.6) | 0.085 | ⚠ within organs, on part of the lines; also absent: GDPD4, LINC02725, RDUR; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[ADAM28]] | B | ADAM28 activity raises ADGRE2's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 2.40× lower at baseline in the lines without ADAM28 | 0.092 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[RASD1]] | B | RASD1 activity raises ADGRE2's level | lines that do not express RASD1 (21) vs lines expressing it (29) | 2.50× lower at baseline in the lines without RASD1 | 0.093 | ⚠ within organs, on part of the lines; also absent: MTSS1, TREM1, APOE |
| [[DUSP4]] | B | DUSP4 activity raises ADGRE2's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.63× lower at baseline in the lines without DUSP4 | 0.096 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 8, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLCO4A1]] | B | ADGRE2 activity raises SLCO4A1's level | lines that do not express ADGRE2 (25) vs lines expressing it (25) | 1.84× lower at baseline in the lines without ADGRE2 | 0.025 | ⚠ within organs, on part of the lines; also absent: CRLF2, ENSG00000272297, RSPO3 |
| [[SHB]] | B | ADGRE2 activity raises SHB's level | lines that do not express ADGRE2 (25) vs lines expressing it (25) | 1.54× lower at baseline in the lines without ADGRE2 | 0.032 | ⚠ within organs, on part of the lines; also absent: CRLF2, ENSG00000272297, RSPO3 |
| [[NPAS2]] | B | ADGRE2 activity raises NPAS2's level | lines that do not express ADGRE2 (25) vs lines expressing it (25) | 1.89× lower at baseline in the lines without ADGRE2 | 0.033 | ⚠ within organs, on part of the lines; also absent: CRLF2, ENSG00000272297, RSPO3 |
| [[ABCC3]] | B | ADGRE2 activity raises ABCC3's level | lines that do not express ADGRE2 (25) vs lines expressing it (25) | 2.19× lower at baseline in the lines without ADGRE2 | 0.042 | ⚠ within organs, on part of the lines; also absent: CRLF2, ENSG00000272297, RSPO3 |
| [[ITGB5]] | B | ADGRE2 activity raises ITGB5's level | lines that do not express ADGRE2 (25) vs lines expressing it (25) | 1.50× lower at baseline in the lines without ADGRE2 | 0.042 | ⚠ within organs, on part of the lines; also absent: CRLF2, ENSG00000272297, RSPO3 |
| [[PTPRE]] | B | ADGRE2 activity raises PTPRE's level | lines that do not express ADGRE2 (25) vs lines expressing it (25) | 1.97× lower at baseline in the lines without ADGRE2 | 0.051 | ⚠ within organs, on part of the lines; also absent: CRLF2, ENSG00000272297, RSPO3 |
| [[TBC1D8]] | B | ADGRE2 activity raises TBC1D8's level | lines that do not express ADGRE2 (25) vs lines expressing it (25) | 1.78× lower at baseline in the lines without ADGRE2 | 0.057 | ⚠ within organs, on part of the lines; also absent: CRLF2, ENSG00000272297, RSPO3 |
| [[HAL]] | B | ADGRE2 activity raises HAL's level | lines that do not express ADGRE2 (25) vs lines expressing it (25) | 1.50× lower at baseline in the lines without ADGRE2 | 0.095 | ⚠ within organs, on part of the lines; also absent: CRLF2, ENSG00000272297, RSPO3 |
| [[LINC02320]] | C | ADGRE2 activity raises LINC02320's level | lines that do not express ADGRE2 (25) vs lines expressing it (25) | 2.95× lower at baseline in the lines without ADGRE2 | 0.006 | ⚠ within organs, on part of the lines; also absent: CRLF2, ENSG00000272297, RSPO3; co-absent with the target |
| [[CCDC33]] | C | ADGRE2 activity raises CCDC33's level | lines that do not express ADGRE2 (25) vs lines expressing it (25) | 1.99× lower at baseline in the lines without ADGRE2 | 0.093 | ⚠ within organs, on part of the lines; also absent: CRLF2, ENSG00000272297, RSPO3; co-absent with the target |
| [[SLPI]] | C | ADGRE2 activity raises SLPI's level | lines that do not express ADGRE2 (25) vs lines expressing it (25) | 2.40× lower at baseline in the lines without ADGRE2 | 0.098 | ⚠ within organs, on part of the lines; also absent: CRLF2, ENSG00000272297, RSPO3; co-absent with the target |

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.749). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.5, 5.2); signed map (7.4, 48.8). **Vector** length 100, 32.0% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +13.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +9.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.6 | +5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +0.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.6 | +4.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.3 | +1.5 |
|  | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | +1.2 | +1.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.8 | -7.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.9 | -5.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.8 | -6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.6 | -7.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.5 | -4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.5 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor E2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:14,732,392-14,778,560 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD312; previously EMR2 |
| Gene groups (HGNC) | CD molecules; Adhesion G protein-coupled receptors, subfamily E |
| Reactome | 3 pathways, smallest: Class B/2 (Secretin family receptors); GPCR ligand binding; Signaling by GPCR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHX3](https://www.uniprot.org/uniprotkb/Q9UHX3) (Adhesion G protein-coupled receptor E2):

> Cell surface receptor that binds to the chondroitin sulfate moiety of glycosaminoglycan chains and promotes cell attachment. Promotes granulocyte chemotaxis, degranulation and adhesion. In macrophages, promotes the release of inflammatory cytokines, including IL8 and TNF. Probably signals through G proteins. Is a regulator of mast cell degranulation.

**Summary**, from NCBI Gene [30817](https://www.ncbi.nlm.nih.gov/gene/30817):

> This gene encodes a member of the class B seven-span transmembrane (TM7) subfamily of G-protein coupled receptors. These proteins are characterized by an extended extracellular region with a variable number of N-terminal epidermal growth factor-like domains coupled to a TM7 domain via a mucin-like spacer domain. The encoded protein is expressed mainly in myeloid cells where it promotes cell-cell adhesion through interaction with chondroitin sulfate chains. This gene is situated in a cluster of …

**Accessions** — [HGNC:3337](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3337) · Entrez [30817](https://www.ncbi.nlm.nih.gov/gene/30817) · UniProt [Q9UHX3](https://www.uniprot.org/uniprotkb/Q9UHX3) · Ensembl [ENSG00000127507](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127507)

## Data

Gene col 4815: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4815); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4815, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4815]; `tensor/DDL_lfc|DDL_z.npy` [4815]; `embed/gene_vectors.npy` [4815]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4815 or target_col == 4815). Every well: [[ADGRE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
