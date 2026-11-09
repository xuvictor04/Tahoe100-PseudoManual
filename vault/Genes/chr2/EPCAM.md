---
symbol: "EPCAM"
type: "gene"
col: 4130
ensembl_id: "ENSG00000119888"
name: "epithelial cell adhesion molecule"
location: "2p21"
module: 44
arm: "+"
pooled_cpm: 147.86
n_lines_expressing: 22
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 52
direction_downstream: 82
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# EPCAM

*epithelial cell adhesion molecule* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.65× (z +18.5, q 0e+00, up in 21 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.65× (z +8.6, q 2e-15, up in 7 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.686× (z -4.5, q 0.003, down in 10 of 20 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2347 0.450×, LS 180 0.434×, Panc 03.27 0.473×, KATO III 0.462×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 0.463×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LYZ]] (+0.79, fdr 7e-06), [[KLK7]] (+0.71, fdr 7e-06), [[PHGR1]] (+0.65, fdr 1e-05); moves opposite to [[FICD]] (-0.38, fdr 6e-04), [[SYDE1]] (-0.38, fdr 3e-04), [[INO80E]] (-0.37, fdr 7e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 52 arrows point to it, the strongest [[KALRN]] → it (grade B ⚠); 82 go from it, the strongest it → [[SYDE1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4130.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.65×** | +18.5 | 0e+00 | 21/21 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.81×** | +15.5 | 0e+00 | 19/19 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.41×** | +13.7 | 3e-40 | 17/19 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +8.6 | 2e-15 | 7/21 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +7.7 | 2e-12 | 7/22 (HEC-1-A, SW48, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.61×** | +5.7 | 9e-07 | 14/20 (COLO 205, SW480, …) | top dose only | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.50×** | +4.9 | 8e-05 | 0/20 | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +4.5 | 4e-04 | 7/15 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.45×** | +4.5 | 5e-04 | 11/20 (SW1417, NCI-H661, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.4 | 5e-04 | 11/20 (NCI-H1573, COLO 205, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.020 | 5/20 (BT-474, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4130.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2347 0.450×, LS 180 0.434×, Panc 03.27 0.473×, KATO III 0.462×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 0.463×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.686×** | -4.5 | 0.003 | 10/20 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Folic acid (drug)]] 5 µM |  | **0.803×** | -3.7 | 0.058 | 12/20 (HEC-1-A, CFPAC-1, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.818× | -3.4 | 0.11 | 17/20 (NCI-H2347, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.756× | -3.4 | 0.11 | 9/20 (NCI-H2347, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.607× | -3.1 | 0.19 | 16/21 (BT-474, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4130. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 230 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +11.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 584 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 153 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.38× (z +14.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 469 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 243 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +11.0) | — |
| [[CFPAC-1 (line)]] | alt | 272 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 391 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +10.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 305 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -10.1) |
| [[SHP-77 (line)]] | alt | 62.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +11.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 252 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +12.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 134 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 419 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 586 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -10.2) |
| [[A-172 (line)]] | wt | 18.2 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 12.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 27.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 22.2 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 420 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 153 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.0 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 308 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 23.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.5 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.0 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 18.1 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 15.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 29.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 30.5 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 618 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 309 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4130), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYZ]] | +0.79 | +0.71 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[KLK7]] | +0.71 | +0.58 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[PHGR1]] | +0.65 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[SPINT2]] | +0.62 | +0.47 / +0.72 | both halves | 2e-05 | STRING 880 |
| [[KLK6]] | +0.61 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[TSPAN1]] | +0.60 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[PIGR]] | +0.59 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CTSH]] | +0.59 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[REG4]] | +0.57 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[TSPAN8]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 | STRING 812 |
| [[FXYD3]] | +0.53 | +0.44 / +0.57 | both halves | 3e-05 | same gene group |
| [[MSLN]] | +0.53 | +0.54 / +0.60 | both halves | 1e-05 | STRING 586 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FICD]] | -0.38 | -0.33 / -0.22 | both halves | 6e-04 |  |
| [[SYDE1]] | -0.38 | -0.27 / -0.30 | both halves | 3e-04 |  |
| [[INO80E]] | -0.37 | -0.44 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 1, C 51. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KALRN]] | B | KALRN activity raises EPCAM's level | lines that do not express KALRN (10) vs lines expressing it (40) | 1.91× lower at baseline in the lines without KALRN | 0.044 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CLDN3]] | C | CLDN3 activity raises EPCAM's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 11.99× lower at baseline in the lines without CLDN3 | 5e-06 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1; co-absent with the target |
| [[SPINT1-AS1]] | C | SPINT1-AS1 activity raises EPCAM's level | lines that do not express SPINT1-AS1 (27) vs lines expressing it (23) | 12.77× lower at baseline in the lines without SPINT1-AS1 | 1e-05 | ⚠ within organs, on part of the lines; also absent: EPCAM, CLDN3, CRB3; co-absent with the target |
| [[LAD1]] | C | LAD1 activity raises EPCAM's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 12.23× lower at baseline in the lines without LAD1 | 1e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1; co-absent with the target |
| [[CLDN7]] | C | CLDN7 activity raises EPCAM's level | lines that do not express CLDN7 (30) vs lines expressing it (20) | 12.54× lower at baseline in the lines without CLDN7 | 1e-05 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14; co-absent with the target |
| [[CRB3]] | C | CRB3 activity raises EPCAM's level | lines that do not express CRB3 (29) vs lines expressing it (21) | 13.32× lower at baseline in the lines without CRB3 | 1e-05 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: KDF1, MARVELD3, CDH1; co-absent with the target |
| [[MAL2]] | C | MAL2 activity raises EPCAM's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 11.40× lower at baseline in the lines without MAL2 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |
| [[MYH14]] | C | MYH14 activity raises EPCAM's level | lines that do not express MYH14 (21) vs lines expressing it (29) | 7.87× lower at baseline in the lines without MYH14 | 3e-05 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2; co-absent with the target |
| [[LCN2]] | C | LCN2 activity raises EPCAM's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 13.13× lower at baseline in the lines without LCN2 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[RAB25]] | C | RAB25 activity raises EPCAM's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 12.60× lower at baseline in the lines without RAB25 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8; co-absent with the target |
| [[TMEM30B]] | C | TMEM30B activity raises EPCAM's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 11.86× lower at baseline in the lines without TMEM30B | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; co-absent with the target |
| [[NPNT]] | C | NPNT activity raises EPCAM's level | lines that do not express NPNT (33) vs lines expressing it (17) | 10.83× lower at baseline in the lines without NPNT | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |

### Downstream of this gene

*82 arrows, 82 of them with an alert ⚠; grade A 0, B 41, C 41. Shown: the 12 strongest; 70 more arrows (70 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYDE1]] | B | EPCAM activity lowers SYDE1's level | lines that do not express EPCAM (28) vs lines expressing it (22) | 3.94× higher at baseline in the lines without EPCAM | 0.014 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| cells under [[5-Azacytidine (drug)]] 5 µM | B | EPCAM activity raises the cells' numbers under 5-Azacytidine 5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.76× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| cells under [[Almonertinib (mesylate) (drug)]] 5 µM | B | EPCAM activity lowers the cells' numbers under Almonertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 1.24× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| cells under [[Lactate (calcium) (drug)]] 0.05 µM | B | EPCAM activity lowers the cells' numbers under Lactate (calcium) 0.05 µM (makes them more sensitive) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 1.20× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | EPCAM activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 1.19× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[CD46]] | B | EPCAM activity raises CD46's level | lines that do not express EPCAM (28) vs lines expressing it (22) | 1.64× lower at baseline in the lines without EPCAM | 0.020 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[KRTCAP3]] | B | EPCAM activity raises KRTCAP3's level | lines that do not express EPCAM (28) vs lines expressing it (22) | 2.52× lower at baseline in the lines without EPCAM | 0.024 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| cells under [[Dihydroartemisinin (drug)]] 5 µM | B | EPCAM activity raises the cells' numbers under Dihydroartemisinin 5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.73× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| cells under [[Ivermectin (drug)]] 0.5 µM | B | EPCAM activity raises the cells' numbers under Ivermectin 0.5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.85× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| cells under [[Salicylic acid (drug)]] 5 µM | B | EPCAM activity raises the cells' numbers under Salicylic acid 5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.86× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| cells under [[Apalutamide (drug)]] 0.5 µM | B | EPCAM activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 1.24× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[CXCL16]] | B | EPCAM activity raises CXCL16's level | lines that do not express EPCAM (28) vs lines expressing it (22) | 2.38× lower at baseline in the lines without EPCAM | 0.039 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.490). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.6, 59.7); signed map (66.8, 5.0). **Vector** length 61.7, 23.2% of its response variance represented; |z| ≥ 3 in 363 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +18.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +13.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +0.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.6 | +1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +0.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.8 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | +2.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | epithelial cell adhesion molecule |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:47,345,158-47,387,601 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Ly74, TROP1, GA733-2, EGP34, EGP40, EGP-2, KSA, CD326; previously M4S1, MIC18, TACSTD1 |
| Gene groups (HGNC) | CD molecules; MicroRNA protein coding host genes |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 6 pathways, smallest: Attachment of bacteria to epithelial cells; Biofilm formation; Infection with Enterobacteria |
| Matched by | ensembl_id |

**Function**, from UniProt [P16422](https://www.uniprot.org/uniprotkb/P16422) (Epithelial cell adhesion molecule):

> May act as a physical homophilic interaction molecule between intestinal epithelial cells (IECs) and intraepithelial lymphocytes (IELs) at the mucosal epithelium for providing immunological barrier as a first line of defense against mucosal infection. Plays a role in embryonic stem cells proliferation and differentiation. Up-regulates the expression of FABP5, MYC and cyclins A and E.

**Summary**, from NCBI Gene [4072](https://www.ncbi.nlm.nih.gov/gene/4072):

> This gene encodes a carcinoma-associated antigen and is a member of a family that includes at least two type I membrane proteins. This antigen is expressed on most normal epithelial cells and gastrointestinal carcinomas and functions as a homotypic calcium-independent cell adhesion molecule. The antigen is being used as a target for immunotherapy treatment of human carcinomas. Mutations in this gene result in congenital tufting enteropathy. [provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:11529](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11529) · Entrez [4072](https://www.ncbi.nlm.nih.gov/gene/4072) · UniProt [P16422](https://www.uniprot.org/uniprotkb/P16422) · Ensembl [ENSG00000119888](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119888)

## Data

Gene col 4130: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4130); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4130, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4130]; `tensor/DDL_lfc|DDL_z.npy` [4130]; `embed/gene_vectors.npy` [4130]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4130 or target_col == 4130). Every well: [[EPCAM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPCAM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
