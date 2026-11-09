---
symbol: "PRAME"
type: "gene"
col: 11717
ensembl_id: "ENSG00000185686"
name: "PRAME nuclear receptor transcriptional regulator"
location: "22q11.22"
module: 7
arm: "+"
pooled_cpm: 23.05
n_lines_expressing: 25
n_dd_up: 4
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# PRAME

*PRAME nuclear receptor transcriptional regulator* — 22q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.55× (z +6.8, q 8e-09, up in 15 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.534× (z -9.6, q 3e-19, down in 20 of 23 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBR1]] (+0.54, fdr 4e-05), [[SMO]] (+0.54, fdr 2e-04), [[PRKD1]] (+0.53, fdr 5e-05); moves opposite to [[ARL6IP6]] (-0.47, fdr 5e-04), [[DAP]] (-0.44, fdr 5e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SAMD11]] → it (grade B ⚠); 10 go from it, the strongest it → [[CHST10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11717.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +6.8 | 8e-09 | 15/23 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +5.8 | 2e-06 | 1/21 (NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +5.2 | 4e-05 | 15/23 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +5.0 | 9e-05 | 15/23 (HEC-1-A, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | 1.24× | +3.3 | 0.13 | 8/23 (C32, NCI-H23, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.34× | +3.1 | 0.16 | 4/22 (RPMI-7951, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11717.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.534×** | -9.6 | 3e-19 | 20/23 (LOX-IMVI, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.436×** | -9.0 | 5e-17 | 18/22 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.554×** | -6.4 | 3e-08 | 18/23 (NCI-H1573, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.622×** | -5.0 | 1e-04 | 14/23 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.678×** | -4.2 | 0.003 | 19/23 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.705×** | -3.8 | 0.014 | 6/23 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.710×** | -3.7 | 0.016 | 16/23 (NCI-H23, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.715×** | -3.6 | 0.019 | 10/23 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.550×** | -3.4 | 0.042 | 8/22 (A-172, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.735×** | -3.3 | 0.046 | 19/23 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.743×** | -3.2 | 0.063 | 15/23 (NCI-H23, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11717. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 27.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 23.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0981× (z -20.5) |
| [[CHP-212 (line)]] | wt | 110 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.116× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change |
| [[NCI-H1792 (line)]] | alt | 16.8 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -15.0) |
| [[NCI-H23 (line)]] | alt | 47.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -19.1) |
| [[A-427 (line)]] | wt | 36.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -11.7) |
| [[C-33 A (line)]] | alt | 71.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.401× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 47.7 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.37× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 107 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 10.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -15.6) |
| [[RPMI-7951 (line)]] | alt | 37.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -12.0) |
| [[A-172 (line)]] | wt | 27.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -9.1) |
| [[AN3 CA (line)]] | alt | 106 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -17.3) |
| [[C32 (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0411× (z -13.5) ⚠ toxic |
| [[HS-578T (line)]] | alt | 22.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -13.6) |
| [[NCI-H661 (line)]] | alt | 44.7 | 0 | 1 | — | [[palbociclib (drug)]] 0.05 µM 0.0845× (z -8.7) |
| [[PANC-1 (line)]] | alt | 32.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -11.7) |
| [[RKO (line)]] | wt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 228 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -17.4) |
| [[A498 (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.72 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.43 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.78 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11717), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBR1]] | +0.54 | +0.43 / +0.72 | both halves | 4e-05 |  |
| [[SMO]] | +0.54 | +0.55 / +0.29 | both halves | 2e-04 |  |
| [[PRKD1]] | +0.53 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[TUBA4A]] | +0.53 | +0.29 / +0.59 | both halves | 2e-04 |  |
| [[THAP11]] | +0.52 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[BARX1]] | +0.51 | +0.49 / +0.38 | both halves | 6e-05 |  |
| [[TENT4B]] | +0.51 | +0.30 / +0.49 | both halves | 2e-04 |  |
| [[ARHGEF25]] | +0.50 | +0.63 / +0.29 | both halves | 2e-04 |  |
| [[BCL7A]] | +0.50 | +0.37 / +0.46 | both halves | 8e-05 |  |
| [[PCOLCE2]] | +0.50 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[TMEM17]] | +0.49 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[PAQR7]] | +0.49 | +0.36 / +0.46 | both halves | 1e-04 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL6IP6]] | -0.47 | -0.23 / -0.55 | both halves | 5e-04 |  |
| [[DAP]] | -0.44 | -0.23 / -0.53 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD11]] | B | SAMD11 activity raises PRAME's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 4.19× lower at baseline in the lines without SAMD11 | 0.017 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[DLX1]] | B | DLX1 activity raises PRAME's level | lines that do not express DLX1 (13) vs lines expressing it (37) | 2.20× lower at baseline in the lines without DLX1 | 0.091 | ⚠ within organs, on part of the lines; also absent: TMEM145, GXYLT2, FSD1 |
| [[HDAC6]] | B | HDAC6 activity raises PRAME's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LRRC4B]] | C | LRRC4B activity raises PRAME's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 4.29× lower at baseline in the lines without LRRC4B | 0.080 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHST10]] | B | PRAME activity raises CHST10's level | lines that do not express PRAME (25) vs lines expressing it (25) | 2.46× lower at baseline in the lines without PRAME | 0.019 | ⚠ within organs, on part of the lines; also absent: GLDC, NR0B1, PAX2 |
| [[SPR]] | B | PRAME activity raises SPR's level | lines that do not express PRAME (25) vs lines expressing it (25) | 1.27× lower at baseline in the lines without PRAME | 0.034 | ⚠ within organs, on part of the lines; also absent: GLDC, NR0B1, PAX2 |
| [[SMO]] | B | PRAME activity raises SMO's level | lines that do not express PRAME (25) vs lines expressing it (25) | 2.41× lower at baseline in the lines without PRAME | 0.055 | ⚠ within organs, on part of the lines; also absent: GLDC, NR0B1, PAX2 |
| [[UPK1A-AS1]] | B | PRAME activity raises UPK1A-AS1's level | lines that do not express PRAME (25) vs lines expressing it (25) | 2.22× lower at baseline in the lines without PRAME | 0.058 | ⚠ within organs, on part of the lines; also absent: GLDC, NR0B1, PAX2 |
| [[SOX12]] | B | PRAME activity strengthens SOX12's drug response | lines that do not express PRAME (21) vs lines expressing it (22) | the lines without PRAME respond 0.78× as strongly (z diff +1.51); strongest at Belinostat 5 µM: 0.50x vs 0.33x (z diff +2.7) | 0.060 | ⚠ within organs, on part of the lines; also absent: GLDC, NR0B1, PAX2; target measured in part of the lines; artifact flags |
| [[ASCC1]] | B | PRAME activity raises ASCC1's level | lines that do not express PRAME (25) vs lines expressing it (25) | 1.27× lower at baseline in the lines without PRAME | 0.060 | ⚠ within organs, on part of the lines; also absent: GLDC, NR0B1, PAX2 |
| [[BOLA3-DT]] | B | PRAME activity raises BOLA3-DT's level | lines that do not express PRAME (25) vs lines expressing it (25) | 1.68× lower at baseline in the lines without PRAME | 0.064 | ⚠ within organs, on part of the lines; also absent: GLDC, NR0B1, PAX2 |
| cells under [[Docetaxel (drug)]] 5 µM | B | PRAME activity lowers the cells' numbers under Docetaxel 5 µM (makes them more sensitive) | lines that do not express PRAME (25) vs lines expressing it (23) | the lines without PRAME: 1.08× the cells of the other lines | 0.077 | ⚠ within organs, on part of the lines; also absent: GLDC, NR0B1, PAX2 |
| [[DEDD2]] | B | PRAME activity lowers DEDD2's level | lines that do not express PRAME (25) vs lines expressing it (25) | 1.41× higher at baseline in the lines without PRAME | 0.082 | ⚠ within organs, on part of the lines; also absent: GLDC, NR0B1, PAX2 |
| [[B4GALNT1]] | C | PRAME activity raises B4GALNT1's level | lines that do not express PRAME (25) vs lines expressing it (25) | 2.44× lower at baseline in the lines without PRAME | 0.076 | ⚠ within organs, on part of the lines; also absent: GLDC, NR0B1, PAX2; co-absent with the target |

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.271). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-12.3, 32.0); signed map (-25.9, -21.5). **Vector** length 60.2, 17.1% of its response variance represented; |z| ≥ 3 in 428 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.4 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +6.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | +2.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +5.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -6.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.2 | -3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.9 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -9.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -1.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | PRAME nuclear receptor transcriptional regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.22 — chr22:22,547,701-22,559,361 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CT130; previously MAPE |
| Gene groups (HGNC) | PRAME family |
| Matched by | ensembl_id |

**Function**, from UniProt [P78395](https://www.uniprot.org/uniprotkb/P78395) (Melanoma antigen preferentially expressed in tumors):

> Substrate-recognition component of a Cul2-RING (CRL2) E3 ubiquitin-protein ligase complex, which mediates ubiquitination of target proteins, leading to their degradation. The CRL2(PRAME) complex mediates ubiquitination and degradation of truncated MSRB1/SEPX1 selenoproteins produced by failed UGA/Sec decoding. In the nucleus, the CRL2(PRAME) complex is recruited to epigenetically and transcriptionally active promoter regions bound by nuclear transcription factor Y (NFY) and probably plays a …

**Summary**, from NCBI Gene [23532](https://www.ncbi.nlm.nih.gov/gene/23532):

> This gene encodes an antigen that is preferentially expressed in human melanomas and that is recognized by cytolytic T lymphocytes. It is not expressed in normal tissues, except testis. The encoded protein acts as a repressor of retinoic acid receptor, and likely confers a growth advantage to cancer cells via this function. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:9336](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9336) · Entrez [23532](https://www.ncbi.nlm.nih.gov/gene/23532) · UniProt [P78395](https://www.uniprot.org/uniprotkb/P78395) · Ensembl [ENSG00000185686](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185686)

## Data

Gene col 11717: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11717); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11717, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11717]; `tensor/DDL_lfc|DDL_z.npy` [11717]; `embed/gene_vectors.npy` [11717]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11717 or target_col == 11717). Every well: [[PRAME — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRAME.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
