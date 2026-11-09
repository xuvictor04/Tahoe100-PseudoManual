---
symbol: "LYPD3"
type: "gene"
col: 4532
ensembl_id: "ENSG00000124466"
name: "LY6/PLAUR domain containing 3"
location: "19q13.31"
module: 34
arm: "+"
pooled_cpm: 2.9
n_lines_expressing: 35
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 40
direction_downstream: 51
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# LYPD3

*LY6/PLAUR domain containing 3* — 19q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.79× (z +10.0, q 8e-21, up in 23 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.517× (z -4.8, q 1e-03, down in 14 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (Hs 766T 0.0833×, CFPAC-1 0.159×, NCI-H2030 0.177×, LS 180 0.142×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AsPC-1 0.244×, LoVo 0.165×; ⚠ cell-cycle shift, explains ~47% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0895×); [[Bendamustine (drug)]] 5 µM in 1 line (NCI-H2030 0.0831×); [[Harringtonine (drug)]] 5 µM in 1 line (Hs 766T 0.0727×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEK2]] (+0.73, fdr 7e-06), [[TMEM92]] (+0.73, fdr 1e-05), [[GIPR]] (+0.69, fdr 7e-06); moves opposite to [[ZMYND11]] (-0.60, fdr 3e-05), [[HNF1A]] (-0.60, fdr 3e-05), [[MTUS1-DT]] (-0.59, fdr 1e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 40 arrows point to it, the strongest [[PKP1]] → it (grade B ⚠); 51 go from it, the strongest it → [[KRT19]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4532.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.79×** | +10.0 | 8e-21 | 23/26 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.48×** | +9.0 | 6e-17 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.29×** | +8.9 | 7e-17 | 23/29 (AsPC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.26×** | +8.7 | 6e-16 | 20/26 (BT-474, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.64×** | +7.3 | 3e-11 | 16/27 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.20×** | +5.9 | 3e-07 | 14/23 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.99×** | +5.2 | 2e-05 | 16/29 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.93×** | +4.9 | 6e-05 | 0/11 | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +4.8 | 1e-04 | 4/12 (NCI-H2030, HOP62, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.65×** | +3.5 | 0.030 | 0/8 | all doses, stronger at high dose | composition shift |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.56×** | +3.4 | 0.041 | 0/18 | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **2.33×** | +3.3 | 0.043 | 9/17 (Hs 766T, SW480, …) | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 1.95× | +3.0 | 0.11 | 1/8 (CFPAC-1) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4532.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (Hs 766T 0.0833×, CFPAC-1 0.159×, NCI-H2030 0.177×, LS 180 0.142×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (AsPC-1 0.244×, LoVo 0.165×; ⚠ cell-cycle shift, explains ~47% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0895×); [[Bendamustine (drug)]] 5 µM in 1 line (NCI-H2030 0.0831×); [[Harringtonine (drug)]] 5 µM in 1 line (Hs 766T 0.0727×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.517×** | -4.8 | 1e-03 | 14/25 (Hs 766T, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.639× | -3.4 | 0.20 | 10/28 (C32, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.661× | -3.1 | 0.33 | 11/26 (NCI-H1573, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4532. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 16.9 | 3 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 7.89× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -9.5) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Trametinib (drug)]] 0.05 µM 0.248× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 13.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0895× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 8.98 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bendamustine (drug)]] 5 µM 0.0831× (z -9.9) |
| [[BT-474 (line)]] | alt | 12.9 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.81× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[HOP62 (line)]] | alt | 3.87 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0553× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM 0.0651× (z -8.7) |
| [[Hs 766T (line)]] | wt | 7.35 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0833× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0727× (z -9.4) |
| [[LoVo (line)]] | wt | 4.54 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -8.8) ⚠ cell-cycle shift, explains ~47% of this change |
| [[LS 180 (line)]] | wt | 7.69 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.653 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.503 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.555 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.550 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.788 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.858 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.766 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.992 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.744 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.531 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.816 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.445 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.831 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.257 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.526 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.893 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4532), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEK2]] | +0.73 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[TMEM92]] | +0.73 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[GIPR]] | +0.69 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[LMTK3]] | +0.68 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[PLEKHG5]] | +0.67 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[FA2H]] | +0.67 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[SH3BGRL3]] | +0.67 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[FCHO1]] | +0.67 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[PRSS3]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[GDPGP1]] | +0.64 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SERPINB1]] | +0.64 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[KRT15]] | +0.62 | +0.52 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_DN; STRING 415 |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYND11]] | -0.60 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[HNF1A]] | -0.60 | -0.53 / -0.43 | both halves | 3e-05 | pathway: HALLMARK_KRAS_SIGNALING_DN |
| [[MTUS1-DT]] | -0.59 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[MCCC2]] | -0.58 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[SAFB]] | -0.58 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[HDGF]] | -0.57 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[PSME3IP1]] | -0.56 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[UFL1-AS1]] | -0.56 | -0.49 / -0.26 | both halves | 4e-04 |  |
| [[ARFGAP2]] | -0.56 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[MBNL3]] | -0.55 | -0.48 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 38, C 2. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKP1]] | B | PKP1 activity raises LYPD3's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 2.44× lower at baseline in the lines without PKP1 | 0.003 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[SERPINB5]] | B | SERPINB5 activity raises LYPD3's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.42× lower at baseline in the lines without SERPINB5 | 0.005 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[LAMA3]] | B | LAMA3 activity raises LYPD3's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.22× lower at baseline in the lines without LAMA3 | 0.005 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[SULT2B1]] | B | SULT2B1 activity raises LYPD3's level | lines that do not express SULT2B1 (28) vs lines expressing it (22) | 2.22× lower at baseline in the lines without SULT2B1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ATP2C2, ST14, SGPP2; maybe low, not absent |
| [[LCK]] | B | LCK activity raises LYPD3's level | lines that do not express LCK (31) vs lines expressing it (19) | 2.12× lower at baseline in the lines without LCK | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent |
| [[LINC00659]] | B | LINC00659 activity raises LYPD3's level | lines that do not express LINC00659 (26) vs lines expressing it (24) | 1.96× lower at baseline in the lines without LINC00659 | 0.009 | ⚠ within organs, on part of the lines; also absent: KLK6, TRIM15, ENSG00000225680 |
| [[DHRS9]] | B | DHRS9 activity raises LYPD3's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 2.40× lower at baseline in the lines without DHRS9 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610 |
| [[CEMIP]] | B | CEMIP activity raises LYPD3's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 2.09× lower at baseline in the lines without CEMIP | 0.011 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[TMEM92]] | B | TMEM92 activity raises LYPD3's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.96× lower at baseline in the lines without TMEM92 | 0.013 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[SCEL]] | B | SCEL activity raises LYPD3's level | lines that do not express SCEL (35) vs lines expressing it (15) | 2.09× lower at baseline in the lines without SCEL | 0.016 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[MTUS1-DT]] | B | MTUS1-DT activity raises LYPD3's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 1.73× lower at baseline in the lines without MTUS1-DT | 0.019 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[S100A14]] | B | S100A14 activity raises LYPD3's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 2.35× lower at baseline in the lines without S100A14 | 0.019 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |

### Downstream of this gene

*51 arrows, 51 of them with an alert ⚠; grade A 0, B 49, C 2. Shown: the 12 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT19]] | B | LYPD3 activity raises KRT19's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 3.77× lower at baseline in the lines without LYPD3 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[SCAT1]] | B | LYPD3 activity raises SCAT1's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 2.35× lower at baseline in the lines without LYPD3 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[SERPINB5]] | B | LYPD3 activity raises SERPINB5's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 4.02× lower at baseline in the lines without LYPD3 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[TINAGL1]] | B | LYPD3 activity raises TINAGL1's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 3.94× lower at baseline in the lines without LYPD3 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[JUP]] | B | LYPD3 activity raises JUP's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 4.02× lower at baseline in the lines without LYPD3 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[ARFGEF2]] | B | LYPD3 activity raises ARFGEF2's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 1.22× lower at baseline in the lines without LYPD3 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[LAMA3]] | B | LYPD3 activity raises LAMA3's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 3.56× lower at baseline in the lines without LYPD3 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[S100A14]] | B | LYPD3 activity raises S100A14's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 3.62× lower at baseline in the lines without LYPD3 | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[CREG2]] | B | LYPD3 activity raises CREG2's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 2.33× lower at baseline in the lines without LYPD3 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[SEMA3B]] | B | LYPD3 activity raises SEMA3B's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 2.90× lower at baseline in the lines without LYPD3 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[HS3ST1]] | B | LYPD3 activity raises HS3ST1's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 3.17× lower at baseline in the lines without LYPD3 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[LAMC2]] | B | LYPD3 activity raises LAMC2's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 3.53× lower at baseline in the lines without LYPD3 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.790). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.1, 2.9); signed map (-3.5, 45.1). **Vector** length 65.7, 15.9% of its response variance represented; |z| ≥ 3 in 685 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.8 | +10.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +4.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.6 | +8.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | -0.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.7 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -2.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.8 | -1.6 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.7 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -0.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | LY6/PLAUR domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.31 — chr19:43,460,787-43,465,608 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C4.4A |
| Gene groups (HGNC) | LY6/PLAUR domain containing |
| Hallmark sets | APICAL_SURFACE, KRAS_SIGNALING_DN |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O95274](https://www.uniprot.org/uniprotkb/O95274) (Ly6/PLAUR domain-containing protein 3):

> Supports cell migration. May be involved in urothelial cell-matrix interactions. May be involved in tumor progression.

**Summary**, from NCBI Gene [27076](https://www.ncbi.nlm.nih.gov/gene/27076):

> Predicted to enable laminin binding activity. Involved in negative regulation of smooth muscle cell apoptotic process. Located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24880](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24880) · Entrez [27076](https://www.ncbi.nlm.nih.gov/gene/27076) · UniProt [O95274](https://www.uniprot.org/uniprotkb/O95274) · Ensembl [ENSG00000124466](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124466)

## Data

Gene col 4532: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4532); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4532, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4532]; `tensor/DDL_lfc|DDL_z.npy` [4532]; `embed/gene_vectors.npy` [4532]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4532 or target_col == 4532). Every well: [[LYPD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYPD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
