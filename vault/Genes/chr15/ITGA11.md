---
symbol: "ITGA11"
type: "gene"
col: 6070
ensembl_id: "ENSG00000137809"
name: "integrin subunit alpha 11"
location: "15q23"
module: 13
arm: "+"
pooled_cpm: 17.8
n_lines_expressing: 16
n_dd_up: 5
n_dd_down: 25
n_dd_up_clean: 1
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 61
direction_downstream: 97
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# ITGA11

*integrin subunit alpha 11* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.50× (z +14.4, q 3e-44, up in 7 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +6.7, q 2e-09, up in 1 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.523× (z -5.5, q 2e-05, down in 9 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYNDIG1]] (+0.79, fdr 7e-06), [[APCDD1L]] (+0.78, fdr 7e-06), [[SAMD3]] (+0.76, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 61 arrows point to it, the strongest [[CARMN]] → it (grade C ⚠); 97 go from it, the strongest it → [[FBLN7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6070.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.50×** | +14.4 | 3e-44 | 7/9 (SW 900, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.90×** | +14.0 | 9e-42 | 7/13 (H4, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.68×** | +10.6 | 6e-24 | 3/10 (SW 900, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.7 | 2e-09 | 1/14 (A-172) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.48×** | +3.9 | 0.012 | 1/10 (A-172) | top dose only | noisy plate (z scaled) |
| [[Pimitespib (drug)]] 0.05 µM |  | 1.48× | +3.3 | 0.10 | 2/13 (HS-578T, RPMI-7951) | inconsistent across doses | position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 1.66× | +3.2 | 0.12 | 0/13 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.29× | +3.1 | 0.12 | 2/14 (NCI-H1792, HS-578T) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.28× | +3.1 | 0.12 | 2/14 (J82, A-172) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.48× | +3.1 | 0.12 | 5/14 (NCI-H1792, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, none with an alert; shown: the 15 strongest. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6070.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.523×** | -5.5 | 2e-05 | 9/12 (HOP62, SHP-77, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.526×** | -5.4 | 2e-05 | 12/14 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.517×** | -5.3 | 3e-05 | 11/14 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.557×** | -5.1 | 4e-05 | 13/14 (RPMI-7951, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.576×** | -4.5 | 8e-04 | 6/14 (HOP62, SHP-77, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **0.699×** | -4.4 | 8e-04 | 10/14 (SHP-77, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.612×** | -4.3 | 0.001 | 7/14 (HOP62, SHP-77, …) | all doses, flat | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.616×** | -4.3 | 0.001 | 7/13 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.617×** | -4.2 | 0.001 | 10/14 (HOP62, SW 900, …) | all doses, flat | position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.618×** | -4.2 | 0.001 | 8/13 (SHP-77, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.654×** | -3.7 | 0.010 | 10/14 (HOP62, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.660×** | -3.6 | 0.012 | 3/14 (SW 1088, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.651×** | -3.6 | 0.012 | 9/13 (HOP62, J82, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.651×** | -3.5 | 0.020 | 8/12 (HOP62, SHP-77, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.757×** | -3.4 | 0.025 | 6/14 (HOP62, SHP-77, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6070. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 85.9 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0733× (z -18.3) |
| [[hTERT-HPNE (line)]] | wt | 255 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0840× (z -11.6) |
| [[SHP-77 (line)]] | alt | 22.2 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0897× (z -9.5) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.225× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 228 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0926× (z -18.5) |
| [[H4 (line)]] | wt | 12.4 | 0 | 1 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.0344× (z -9.0) |
| [[HS-578T (line)]] | alt | 213 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 45.5 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.475× (z -12.9) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.79 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 59.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.92 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6070), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNDIG1]] | +0.79 | +0.80 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1L]] | +0.78 | +0.69 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[SAMD3]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[RFX8]] | +0.76 | +0.76 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[KCNK3]] | +0.74 | +0.73 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[INSYN2B]] | +0.72 | +0.73 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[GPR68]] | +0.72 | +0.71 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[TMEM200A]] | +0.71 | +0.70 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[LINC02813]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[COL6A2]] | +0.69 | +0.64 / +0.65 | both halves | 7e-06 | pathway: Extracellular matrix organization; STRING 863 |
| [[LAMA4]] | +0.69 | +0.67 / +0.72 | both halves | 7e-06 | pathway: Extracellular matrix organization; STRING 800 |
| [[SCUBE3]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 | pathway: Extracellular matrix organization |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*61 arrows, 61 of them with an alert ⚠; grade A 0, B 0, C 61. Shown: the 12 strongest; 49 more arrows (49 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARMN]] | C | CARMN activity raises ITGA11's level | lines that do not express CARMN (40) vs lines expressing it (10) | 12.81× lower at baseline in the lines without CARMN | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises ITGA11's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 10.54× lower at baseline in the lines without LINC01411 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises ITGA11's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 8.64× lower at baseline in the lines without PDGFRB | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises ITGA11's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 6.57× lower at baseline in the lines without COL5A1 | 0.001 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[PXDN]] | C | PXDN activity raises ITGA11's level | lines that do not express PXDN (29) vs lines expressing it (21) | 6.26× lower at baseline in the lines without PXDN | 0.002 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, ITGA11, SOX11; co-absent with the target |
| [[SPOCK1]] | C | SPOCK1 activity raises ITGA11's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 5.72× lower at baseline in the lines without SPOCK1 | 0.002 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises ITGA11's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 7.40× lower at baseline in the lines without CDH13 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[WNT5A]] | C | WNT5A activity raises ITGA11's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 6.15× lower at baseline in the lines without WNT5A | 0.003 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[GPR173]] | C | GPR173 activity raises ITGA11's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 6.06× lower at baseline in the lines without GPR173 | 0.003 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2; co-absent with the target |
| [[GDNF]] | C | GDNF activity raises ITGA11's level | lines that do not express GDNF (38) vs lines expressing it (12) | 6.53× lower at baseline in the lines without GDNF | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[TMEM200A]] | C | TMEM200A activity raises ITGA11's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 5.01× lower at baseline in the lines without TMEM200A | 0.005 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615; co-absent with the target |
| [[RFX8]] | C | RFX8 activity raises ITGA11's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 5.86× lower at baseline in the lines without RFX8 | 0.007 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN; co-absent with the target |

### Downstream of this gene

*97 arrows, 97 of them with an alert ⚠; grade A 0, B 19, C 78. Shown: the 12 strongest; 85 more arrows (85 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBLN7]] | B | ITGA11 activity raises FBLN7's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.97× lower at baseline in the lines without ITGA11 | 0.005 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[RAC2]] | B | ITGA11 activity raises RAC2's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 4.52× lower at baseline in the lines without ITGA11 | 0.017 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[ZCCHC24]] | B | ITGA11 activity raises ZCCHC24's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.50× lower at baseline in the lines without ITGA11 | 0.031 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[MIR3936HG]] | B | ITGA11 activity weakens MIR3936HG's drug response | lines that do not express ITGA11 (33) vs lines expressing it (14) | the lines without ITGA11 respond 1.68× as strongly (z diff -1.31); strongest at Ouabain (Octahydrate) 0.5 µM: 0.52x vs 0.81x (z diff -2.9) | 0.033 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; target measured in part of the lines; artifact flags |
| [[SH2B3]] | B | ITGA11 activity raises SH2B3's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.31× lower at baseline in the lines without ITGA11 | 0.034 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[AMZ1]] | B | ITGA11 activity raises AMZ1's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 1.71× lower at baseline in the lines without ITGA11 | 0.035 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[MIR3936HG]] | B | ITGA11 activity lowers MIR3936HG's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 1.69× higher at baseline in the lines without ITGA11 | 0.045 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[CD82]] | B | ITGA11 activity raises CD82's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.36× lower at baseline in the lines without ITGA11 | 0.047 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[GPR68]] | B | ITGA11 activity raises GPR68's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.29× lower at baseline in the lines without ITGA11 | 0.048 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[NRP1]] | B | ITGA11 activity raises NRP1's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 3.64× lower at baseline in the lines without ITGA11 | 0.048 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[LINC01119]] | B | ITGA11 activity raises LINC01119's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.23× lower at baseline in the lines without ITGA11 | 0.050 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |
| [[ZNF175]] | B | ITGA11 activity raises ZNF175's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.13× lower at baseline in the lines without ITGA11 | 0.058 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.808). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.6, 15.1); signed map (22.4, 46.7). **Vector** length 80.2, 35.8% of its response variance represented; |z| ≥ 3 in 485 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Collagen formation* (reactome, mean cos +0.54 to 12); *Assembly of collagen fibrils and other multimeric structures* (reactome, mean cos +0.56 to 10); *Defective B3GALTL causes PpS* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +3.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.0 | +3.2 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.8 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -4.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -3.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.0 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit alpha 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:68,296,532-68,432,163 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HsT18964 |
| Gene groups (HGNC) | Integrin alpha subunits |
| Reactome | 2 pathways, smallest: Integrin cell surface interactions; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKX5](https://www.uniprot.org/uniprotkb/Q9UKX5) (Integrin alpha-11):

> Integrin alpha-11/beta-1 is a receptor for collagen.

**Summary**, from NCBI Gene [22801](https://www.ncbi.nlm.nih.gov/gene/22801):

> This gene encodes an alpha integrin. Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain. This protein contains an I domain, is expressed in muscle tissue, dimerizes with beta 1 integrin in vitro, and appears to bind collagen in this form. Therefore, the protein may be involved in attaching muscle tissue to the extracellular matrix. Alternative transcriptional splice variants have been found for this gene, but their biological validity is not …

**Accessions** — [HGNC:6136](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6136) · Entrez [22801](https://www.ncbi.nlm.nih.gov/gene/22801) · UniProt [Q9UKX5](https://www.uniprot.org/uniprotkb/Q9UKX5) · Ensembl [ENSG00000137809](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137809)

## Data

Gene col 6070: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6070); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6070, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6070]; `tensor/DDL_lfc|DDL_z.npy` [6070]; `embed/gene_vectors.npy` [6070]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6070 or target_col == 6070). Every well: [[ITGA11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGA11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
