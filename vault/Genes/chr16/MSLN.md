---
symbol: "MSLN"
type: "gene"
col: 2276
ensembl_id: "ENSG00000102854"
name: "mesothelin"
location: "16p13.3"
module: 44
arm: "+"
pooled_cpm: 3.88
n_lines_expressing: 17
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 24
direction_downstream: 28
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# MSLN

*mesothelin* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 8.48× (z +13.3, q 7e-38, up in 5 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.26× (z +7.7, q 2e-12, up in 4 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.424× (z -5.4, q 3e-05, down in 14 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (LS 180 0.0590×, KATO III 0.126×, NCI-H2347 0.189×, HEC-1-A 0.0937×, …; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 6 lines (LS 180 0.0405×, KATO III 0.0667×, AsPC-1 0.161×, SW480 0.0800×, …); [[Harringtonine (drug)]] 5 µM in 3 lines (NCI-H2347 0.178×, LS 180 0.202×, KATO III 0.202×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOD3]] (+0.67, fdr 1e-05), [[KLK7]] (+0.67, fdr 7e-06), [[PIGR]] (+0.63, fdr 1e-05); moves opposite to [[THAP5]] (-0.53, fdr 1e-04), [[ASF1A]] (-0.52, fdr 5e-05), [[LZIC]] (-0.47, fdr 5e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[PCSK9]] → it (grade C ⚠); 28 go from it, the strongest it → [[ASAH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2276.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.48×** | +13.3 | 7e-38 | 5/5 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.01×** | +10.8 | 8e-25 | 9/9 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.38×** | +10.5 | 3e-23 | 5/6 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +7.7 | 2e-12 | 4/14 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.47×** | +5.6 | 2e-06 | 3/10 (LS 180, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.19×** | +5.2 | 2e-05 | 4/10 (HEC-1-A, AsPC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.66×** | +4.8 | 1e-04 | 3/15 (SW480, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +4.6 | 3e-04 | 3/12 (LS 180, AsPC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +4.5 | 4e-04 | 2/10 (LoVo, AsPC-1) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.92×** | +3.8 | 0.007 | 2/13 (A-172, LS 180) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +3.6 | 0.015 | 3/12 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.79×** | +3.6 | 0.015 | 0/11 | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.37×** | +3.5 | 0.018 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.72×** | +3.4 | 0.027 | 2/11 (SW48, NCI-H2347) | inconsistent across doses | low cells (technical?) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.63×** | +3.2 | 0.046 | 1/13 (CFPAC-1) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.58×** | +3.1 | 0.068 | 2/13 (KATO III, LS 180) | rises with dose | position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.64×** | +3.0 | 0.068 | 2/13 (COLO 205, J82) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.08×** | +3.0 | 0.075 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.55×** | +2.9 | 0.096 | 2/14 (LoVo, A-172) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2276.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (LS 180 0.0590×, KATO III 0.126×, NCI-H2347 0.189×, HEC-1-A 0.0937×, …; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 6 lines (LS 180 0.0405×, KATO III 0.0667×, AsPC-1 0.161×, SW480 0.0800×, …); [[Harringtonine (drug)]] 5 µM in 3 lines (NCI-H2347 0.178×, LS 180 0.202×, KATO III 0.202×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.424×** | -5.4 | 3e-05 | 14/15 (NCI-H2347, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.611× | -3.4 | 0.17 | 14/15 (LS 180, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.592× | -3.3 | 0.17 | 2/15 (SW48, HEC-1-A) | inconsistent across doses |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.615× | -3.1 | 0.20 | 1/15 (SW480) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.611× | -3.1 | 0.20 | 3/15 (SW480, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2276. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 27.2 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.64× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -18.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0667× (z -16.9) |
| [[LS 180 (line)]] | wt | 34.2 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0590× (z -26.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0405× (z -20.9) |
| [[NCI-H2347 (line)]] | alt | 15.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -14.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.178× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 33.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -11.0) |
| [[SW48 (line)]] | wt | 12.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0662× (z -9.2) |
| [[SW480 (line)]] | alt | 3.18 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0800× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 2.24 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0937× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 8.63 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.392 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.257 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.195 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.236 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.206 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.987 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.319 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.285 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.222 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.155 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.256 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.775 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.202 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.217 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.183 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.236 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.399 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.665 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2276), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOD3]] | +0.67 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[KLK7]] | +0.67 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[PIGR]] | +0.63 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[LYZ]] | +0.62 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[FXYD3]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[CTSH]] | +0.60 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[SPINT2]] | +0.59 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[CKMT1B]] | +0.59 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[CKMT1A]] | +0.59 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[RAB25]] | +0.59 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[ELMO3]] | +0.58 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[PPP1R1B]] | +0.58 | +0.51 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP5]] | -0.53 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[ASF1A]] | -0.52 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[LZIC]] | -0.47 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[GSPT2]] | -0.46 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[GLRX2]] | -0.45 | -0.50 / -0.25 | both halves | 4e-04 |  |
| [[NME6]] | -0.44 | -0.50 / -0.23 | both halves | 5e-04 |  |
| [[PRKG2-AS1]] | -0.43 | -0.47 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[METTL18]] | -0.43 | -0.52 / -0.26 | both halves | 4e-04 |  |
| [[ERCC4]] | -0.43 | -0.46 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 0, C 24. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCSK9]] | C | PCSK9 activity raises MSLN's level | lines that do not express PCSK9 (28) vs lines expressing it (22) | 3.51× lower at baseline in the lines without PCSK9 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: C6orf132, RNF223, CDH1; co-absent with the target |
| [[LCN2]] | C | LCN2 activity raises MSLN's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 3.51× lower at baseline in the lines without LCN2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises MSLN's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 3.16× lower at baseline in the lines without MUC5B | 0.010 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[TSPAN1]] | C | TSPAN1 activity raises MSLN's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 2.89× lower at baseline in the lines without TSPAN1 | 0.018 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6; co-absent with the target |
| [[PIGR]] | C | PIGR activity raises MSLN's level | lines that do not express PIGR (45) vs lines expressing it (5) | 3.85× lower at baseline in the lines without PIGR | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[REG4]] | C | REG4 activity raises MSLN's level | lines that do not express REG4 (43) vs lines expressing it (7) | 5.05× lower at baseline in the lines without REG4 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[CLDN3]] | C | CLDN3 activity raises MSLN's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 2.61× lower at baseline in the lines without CLDN3 | 0.032 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1; co-absent with the target |
| [[EPCAM]] | C | EPCAM activity raises MSLN's level | lines that do not express EPCAM (28) vs lines expressing it (22) | 2.80× lower at baseline in the lines without EPCAM | 0.033 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3; co-absent with the target |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises MSLN's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 3.45× lower at baseline in the lines without ST6GALNAC1 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |
| [[S100P]] | C | S100P activity raises MSLN's level | lines that do not express S100P (34) vs lines expressing it (16) | 2.99× lower at baseline in the lines without S100P | 0.036 | ⚠ within organs, on part of the lines; also absent: POF1B, ENSG00000287426, CEACAM6; co-absent with the target |
| [[LYZ]] | C | LYZ activity raises MSLN's level | lines that do not express LYZ (40) vs lines expressing it (10) | 4.08× lower at baseline in the lines without LYZ | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, TRIM31, MUC17; co-absent with the target |
| [[AZGP1]] | C | AZGP1 activity raises MSLN's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 3.10× lower at baseline in the lines without AZGP1 | 0.039 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ; co-absent with the target |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 6, C 22. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASAH1]] | B | MSLN activity raises ASAH1's level | lines that do not express MSLN (33) vs lines expressing it (17) | 1.50× lower at baseline in the lines without MSLN | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR |
| [[TSPO]] | B | MSLN activity raises TSPO's level | lines that do not express MSLN (33) vs lines expressing it (17) | 1.45× lower at baseline in the lines without MSLN | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR |
| [[AMN]] | B | MSLN activity raises AMN's level | lines that do not express MSLN (33) vs lines expressing it (17) | 2.12× lower at baseline in the lines without MSLN | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR |
| [[CD9]] | B | MSLN activity raises CD9's level | lines that do not express MSLN (33) vs lines expressing it (17) | 2.78× lower at baseline in the lines without MSLN | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR |
| [[KRTCAP3]] | B | MSLN activity raises KRTCAP3's level | lines that do not express MSLN (33) vs lines expressing it (17) | 2.22× lower at baseline in the lines without MSLN | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR |
| [[ACSM3]] | B | MSLN activity raises ACSM3's level | lines that do not express MSLN (33) vs lines expressing it (17) | 1.34× lower at baseline in the lines without MSLN | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR |
| [[LCN2]] | C | MSLN activity raises LCN2's level | lines that do not express MSLN (33) vs lines expressing it (17) | 6.25× lower at baseline in the lines without MSLN | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR; co-absent with the target |
| [[PCSK9]] | C | MSLN activity raises PCSK9's level | lines that do not express MSLN (33) vs lines expressing it (17) | 3.60× lower at baseline in the lines without MSLN | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR; co-absent with the target |
| [[TSPAN1]] | C | MSLN activity raises TSPAN1's level | lines that do not express MSLN (33) vs lines expressing it (17) | 2.86× lower at baseline in the lines without MSLN | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR; co-absent with the target |
| [[EPCAM]] | C | MSLN activity raises EPCAM's level | lines that do not express MSLN (33) vs lines expressing it (17) | 5.64× lower at baseline in the lines without MSLN | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR; co-absent with the target |
| [[S100P]] | C | MSLN activity raises S100P's level | lines that do not express MSLN (33) vs lines expressing it (17) | 5.53× lower at baseline in the lines without MSLN | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR; co-absent with the target |
| [[MUC5B]] | C | MSLN activity raises MUC5B's level | lines that do not express MSLN (33) vs lines expressing it (17) | 2.48× lower at baseline in the lines without MSLN | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.532). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.5, 59.9); signed map (67.0, 4.8). **Vector** length 32.2, 7.35% of its response variance represented; |z| ≥ 3 in 287 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +10.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.9 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -0.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.8 | -1.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -3.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | mesothelin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:760,734-768,865 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAK1, MPF |
| Reactome | 3 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins; Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13421](https://www.uniprot.org/uniprotkb/Q13421) (Mesothelin):

> Membrane-anchored forms may play a role in cellular adhesion.; Megakaryocyte-potentiating factor (MPF) potentiates megakaryocyte colony formation in vitro.

**Summary**, from NCBI Gene [10232](https://www.ncbi.nlm.nih.gov/gene/10232):

> This gene encodes a preproprotein that is proteolytically processed to generate two protein products, megakaryocyte potentiating factor and mesothelin. Megakaryocyte potentiating factor functions as a cytokine that can stimulate colony formation of bone marrow megakaryocytes. Mesothelin is a glycosylphosphatidylinositol-anchored cell-surface protein that may function as a cell adhesion protein. This protein is overexpressed in epithelial mesotheliomas, ovarian cancers and in specific squamous …

**Accessions** — [HGNC:7371](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7371) · Entrez [10232](https://www.ncbi.nlm.nih.gov/gene/10232) · UniProt [Q13421](https://www.uniprot.org/uniprotkb/Q13421) · Ensembl [ENSG00000102854](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102854)

## Data

Gene col 2276: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2276); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2276, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2276]; `tensor/DDL_lfc|DDL_z.npy` [2276]; `embed/gene_vectors.npy` [2276]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2276 or target_col == 2276). Every well: [[MSLN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSLN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
