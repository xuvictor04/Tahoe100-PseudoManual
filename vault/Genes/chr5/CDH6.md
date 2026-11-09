---
symbol: "CDH6"
type: "gene"
col: 3454
ensembl_id: "ENSG00000113361"
name: "cadherin 6"
location: "5p13.3"
module: 9
arm: "+"
pooled_cpm: 9.62
n_lines_expressing: 17
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 24
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CDH6

*cadherin 6* — 5p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.95× (z +14.5, q 7e-45, up in 7 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.87× (z +7.5, q 1e-11, up in 1 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 0.585× (z -4.6, q 0.003, down in 6 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOK5]] (+0.72, fdr 7e-06), [[SULF1]] (+0.66, fdr 7e-06), [[LINC01592]] (+0.65, fdr 7e-06); moves opposite to [[CEBPB]] (-0.51, fdr 3e-05), [[MT1F]] (-0.47, fdr 4e-05), [[RILPL2]] (-0.46, fdr 4e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CHRDL1]] → it (grade C ⚠); 24 go from it, the strongest it → [[COL21A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3454.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.95×** | +14.5 | 7e-45 | 7/9 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.41×** | +12.5 | 1e-33 | 9/12 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.68×** | +10.2 | 4e-22 | 4/9 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +7.5 | 1e-11 | 1/13 (HOP62) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +5.5 | 3e-06 | 5/14 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.82×** | +5.0 | 4e-05 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.98×** | +4.1 | 0.003 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.5 | 0.029 | 3/10 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.4 | 0.040 | 1/14 (HS-578T) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.14×** | +3.4 | 0.044 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.098 | 4/14 (CFPAC-1, SHP-77, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.65× | +3.0 | 0.12 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3454.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.585×** | -4.6 | 0.003 | 6/14 (Hs 766T, H4, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.611×** | -4.2 | 0.008 | 5/14 (Hs 766T, SHP-77, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.630×** | -3.9 | 0.016 | 5/14 (Hs 766T, SHP-77, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.640×** | -3.8 | 0.019 | 2/14 (CHP-212, SNU-423) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.642×** | -3.8 | 0.019 | 5/14 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.648×** | -3.7 | 0.021 | 0/14 | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.661×** | -3.5 | 0.035 | 1/14 (HS-578T) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.681×** | -3.3 | 0.070 | 4/14 (J82, HEC-1-A, …) | two highest doses |  |
| [[Artesunate (drug)]] 5 µM |  | **0.763×** | -3.3 | 0.070 | 8/14 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.768×** | -3.2 | 0.082 | 6/14 (H4, A498, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.700× | -3.0 | 0.12 | 4/14 (Hs 766T, CFPAC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3454. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 114 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -15.6) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -12.6) |
| [[NCI-H661 (line)]] | alt | 1,533 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -10.5) |
| [[A498 (line)]] | wt | 19.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.59× (z +8.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 9.75 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.170× (z -8.9) ⚠ cell-cycle shift, explains ~55% of this change |
| [[A-172 (line)]] | wt | 0.789 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.642 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.819 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.831 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.903 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.878 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.898 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.759 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.938 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.769 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.750 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.802 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.733 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.902 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.700 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.690 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.865 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.747 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.944 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.945 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.933 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.777 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.920 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.760 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3454), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOK5]] | +0.72 | +0.73 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[SULF1]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[LINC01592]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[PCDH18]] | +0.64 | +0.57 / +0.66 | both halves | 9e-06 | **novel candidate** |
| [[CCDC190]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[SIM1]] | +0.62 | +0.62 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[ABCA13]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[MOXD1]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[PAK3]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SRPX2]] | +0.59 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[LINC01116]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[TNFRSF11B]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_APICAL_JUNCTION |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEBPB]] | -0.51 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[MT1F]] | -0.47 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[RILPL2]] | -0.46 | -0.43 / -0.46 | both halves | 4e-05 |  |
| [[MT1M]] | -0.45 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[MT1A]] | -0.44 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[TLR2]] | -0.44 | -0.40 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHRDL1]] | C | CHRDL1 activity raises CDH6's level | lines that do not express CHRDL1 (37) vs lines expressing it (13) | 3.64× lower at baseline in the lines without CHRDL1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01592, PAX3, LINC01035; co-absent with the target |
| [[LINC01592]] | C | LINC01592 activity raises CDH6's level | lines that do not express LINC01592 (35) vs lines expressing it (15) | 3.20× lower at baseline in the lines without LINC01592 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHRDL1, ESM1, CCL3; maybe low, not absent; co-absent with the target |
| [[TOX]] | C | TOX activity raises CDH6's level | lines that do not express TOX (30) vs lines expressing it (20) | 4.16× lower at baseline in the lines without TOX | 0.083 | ⚠ within organs, on part of the lines; also absent: CDH6, DKK3, MXRA5; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 7, C 17. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL21A1]] | B | CDH6 activity raises COL21A1's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 1.60× lower at baseline in the lines without CDH6 | 0.030 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC |
| [[OFCC1]] | B | CDH6 activity raises OFCC1's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 1.95× lower at baseline in the lines without CDH6 | 0.035 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC |
| [[ABCA13]] | B | CDH6 activity raises ABCA13's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 1.96× lower at baseline in the lines without CDH6 | 0.039 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC |
| [[LDB2]] | B | CDH6 activity raises LDB2's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 2.72× lower at baseline in the lines without CDH6 | 0.047 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC |
| [[MIR325HG]] | B | CDH6 activity raises MIR325HG's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 1.49× lower at baseline in the lines without CDH6 | 0.053 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC |
| [[ADAMTSL1]] | B | CDH6 activity raises ADAMTSL1's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 2.24× lower at baseline in the lines without CDH6 | 0.085 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC |
| [[BMPER]] | B | CDH6 activity raises BMPER's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 2.44× lower at baseline in the lines without CDH6 | 0.098 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC |
| [[TOX]] | C | CDH6 activity raises TOX's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 7.11× lower at baseline in the lines without CDH6 | 0.018 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC; co-absent with the target |
| [[NCKAP5]] | C | CDH6 activity raises NCKAP5's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 2.83× lower at baseline in the lines without CDH6 | 0.019 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC; co-absent with the target |
| [[LINC01592]] | C | CDH6 activity raises LINC01592's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 1.58× lower at baseline in the lines without CDH6 | 0.022 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC; co-absent with the target |
| [[HHIP]] | C | CDH6 activity raises HHIP's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 3.55× lower at baseline in the lines without CDH6 | 0.023 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC; co-absent with the target |
| [[NRP2]] | C | CDH6 activity raises NRP2's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 2.02× lower at baseline in the lines without CDH6 | 0.044 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.542). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.3, 20.3); signed map (35.3, 30.3). **Vector** length 48.2, 14.6% of its response variance represented; |z| ≥ 3 in 375 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +14.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +3.5 | +2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | -0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +1.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +1.7 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -3.8 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.6 | -2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -3.9 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | cadherin 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.3 — chr5:31,193,686-31,329,146 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Type II classical cadherins |
| Hallmark sets | APICAL_JUNCTION, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 4 pathways, smallest: Adherens junctions interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [P55285](https://www.uniprot.org/uniprotkb/P55285) (Cadherin-6):

> Cadherins are calcium-dependent cell adhesion proteins. They preferentially interact with themselves in a homophilic manner in connecting cells; cadherins may thus contribute to the sorting of heterogeneous cell types.

**Summary**, from NCBI Gene [1004](https://www.ncbi.nlm.nih.gov/gene/1004):

> This gene encodes a member of the cadherin superfamily. Cadherins are membrane glycoproteins that mediate homophilic cell-cell adhesion and play critical roles in cell differentiation and morphogenesis. The encoded protein is a type II cadherin and may play a role in kidney development as well as endometrium and placenta formation. Decreased expression of this gene may be associated with tumor growth and metastasis. [provided by RefSeq, May 2011]

**Accessions** — [HGNC:1765](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1765) · Entrez [1004](https://www.ncbi.nlm.nih.gov/gene/1004) · UniProt [P55285](https://www.uniprot.org/uniprotkb/P55285) · Ensembl [ENSG00000113361](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113361)

## Data

Gene col 3454: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3454); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3454, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3454]; `tensor/DDL_lfc|DDL_z.npy` [3454]; `embed/gene_vectors.npy` [3454]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3454 or target_col == 3454). Every well: [[CDH6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDH6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
