---
symbol: "EPHB3"
type: "gene"
col: 11303
ensembl_id: "ENSG00000182580"
name: "EPH receptor B3"
location: "3q27.1"
module: 162
arm: "+"
pooled_cpm: 6.2
n_lines_expressing: 35
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 21
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# EPHB3

*EPH receptor B3* — 3q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 5.73× (z +17.5, q 0e+00, up in 29 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.646× (z -4.0, q 0.042, down in 7 of 31 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW1417 0.0662×, NCI-H2347 0.182×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW480 0.136×, HT-29 0.121×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW1417 0.154×, NCI-H2347 0.191×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (LS 180 0.121×); [[Belumosudil (drug)]] 5 µM in 1 line (LoVo 0.131×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BIK]] (+0.66, fdr 1e-05), [[BAIAP3]] (+0.65, fdr 1e-05), [[KLHL26]] (+0.65, fdr 1e-05); moves opposite to [[DPH5-DT]] (-0.50, fdr 2e-04), [[QRSL1]] (-0.50, fdr 3e-04), [[GPALPP1]] (-0.50, fdr 2e-04).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[AZGP1]] → it (grade B ⚠); 21 go from it, the strongest it → [[CDC42BPG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11303.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **5.73×** | +17.5 | 0e+00 | 29/30 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **5.64×** | +17.3 | 0e+00 | 28/31 (SW1417, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.83×** | +14.7 | 0e+00 | 16/24 (SW1417, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.66×** | +13.0 | 2e-36 | 28/31 (NCI-H1573, SW1417, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.26×** | +11.5 | 1e-28 | 17/30 (SW1417, Panc 03.27, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.42×** | +8.9 | 8e-17 | 19/31 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.05×** | +7.2 | 6e-11 | 13/29 (Panc 03.27, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +6.1 | 6e-08 | 8/20 (CFPAC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.71×** | +5.2 | 1e-05 | 0/10 | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +4.7 | 1e-04 | 9/24 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.60×** | +4.5 | 3e-04 | 7/29 (SW1417, C32, …) | top dose only | composition shift; position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +4.1 | 0.002 | 4/13 (LS 180, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.002 | 3/30 (BT-474, SW48, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.75×** | +4.0 | 0.003 | 5/20 (A-427, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.48×** | +3.9 | 0.003 | 8/31 (SW1417, KATO III, …) | top dose only | composition shift; position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.045 | 2/30 (NCI-H1573, RPMI-7951) | inconsistent across doses | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.83×** | +3.2 | 0.053 | 3/21 (CFPAC-1, HCT15, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +3.0 | 0.077 | 1/28 (MIA PaCa-2) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.35×** | +3.0 | 0.081 | 2/31 (SW1417, NCI-H1573) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11303.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW1417 0.0662×, NCI-H2347 0.182×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW480 0.136×, HT-29 0.121×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW1417 0.154×, NCI-H2347 0.191×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (LS 180 0.121×); [[Belumosudil (drug)]] 5 µM in 1 line (LoVo 0.131×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.646×** | -4.0 | 0.042 | 7/31 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); noisy plate (z scaled); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.706× | -3.5 | 0.15 | 7/29 (C-33 A, HT-29, …) | inconsistent across doses |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.718× | -3.3 | 0.15 | 7/30 (BT-474, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11303. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 14.5 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0662× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 12.0 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -11.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[C32 (line)]] | wt | 11.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 6.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 7.04 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.131× (z -9.3) |
| [[LS 180 (line)]] | wt | 28.1 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.121× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 4.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +10.4) | — |
| [[SW480 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.681 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.917 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.658 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.906 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.945 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.933 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11303), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BIK]] | +0.66 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[BAIAP3]] | +0.65 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[KLHL26]] | +0.65 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[SOX13]] | +0.64 | +0.34 / +0.67 | both halves | 1e-04 |  |
| [[RHPN2]] | +0.63 | +0.36 / +0.60 | both halves | 9e-05 |  |
| [[PLEKHO2]] | +0.63 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[BCORL1]] | +0.62 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[PADI2]] | +0.62 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[AHDC1]] | +0.61 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[CNNM4]] | +0.61 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[SEMA3F]] | +0.60 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[STARD5]] | +0.59 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPH5-DT]] | -0.50 | -0.30 / -0.32 | both halves | 2e-04 |  |
| [[QRSL1]] | -0.50 | -0.37 / -0.27 | both halves | 3e-04 |  |
| [[GPALPP1]] | -0.50 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[AP5M1]] | -0.50 | -0.28 / -0.21 | both halves | 7e-04 |  |
| [[NAF1]] | -0.49 | -0.42 / -0.28 | both halves | 3e-04 |  |
| [[ANGEL2]] | -0.49 | -0.34 / -0.32 | both halves | 2e-04 |  |
| [[SETD7]] | -0.49 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[STMP1]] | -0.49 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[DNAJB14]] | -0.48 | -0.29 / -0.40 | both halves | 3e-04 |  |
| [[ANXA2R-OT1]] | -0.48 | -0.26 / -0.34 | both halves | 4e-04 |  |
| [[ZMPSTE24]] | -0.48 | -0.23 / -0.37 | both halves | 5e-04 |  |
| [[MAPKAPK5]] | -0.48 | -0.34 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AZGP1]] | B | AZGP1 activity raises EPHB3's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 3.23× lower at baseline in the lines without AZGP1 | 0.003 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ |
| [[LCK]] | B | LCK activity raises EPHB3's level | lines that do not express LCK (31) vs lines expressing it (19) | 2.56× lower at baseline in the lines without LCK | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent |
| [[SPNS2]] | B | SPNS2 activity raises EPHB3's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 2.47× lower at baseline in the lines without SPNS2 | 0.020 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[ESPN]] | B | ESPN activity raises EPHB3's level | lines that do not express ESPN (26) vs lines expressing it (24) | 2.32× lower at baseline in the lines without ESPN | 0.020 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3 |
| [[LMO3]] | B | LMO3 activity raises EPHB3's level | lines that do not express LMO3 (36) vs lines expressing it (14) | 1.87× lower at baseline in the lines without LMO3 | 0.027 | ⚠ within organs, on part of the lines; also absent: MUC6, LINC02566, APOD; maybe low, not absent |
| [[CRACR2B]] | B | CRACR2B activity raises EPHB3's level | lines that do not express CRACR2B (11) vs lines expressing it (39) | 2.27× lower at baseline in the lines without CRACR2B | 0.029 | ⚠ within organs, on part of the lines; also absent: PNPLA4, ENSG00000285679, DAPK2 |
| [[MOGAT3]] | B | MOGAT3 activity raises EPHB3's level | lines that do not express MOGAT3 (30) vs lines expressing it (20) | 2.50× lower at baseline in the lines without MOGAT3 | 0.061 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819 |
| [[NECTIN1]] | B | NECTIN1 activity raises EPHB3's level | lines that do not express NECTIN1 (8) vs lines expressing it (42) | 2.72× lower at baseline in the lines without NECTIN1 | 0.066 | ⚠ within organs, on part of the lines; also absent: PRR5; maybe low, not absent |
| [[CDC42BPG]] | B | CDC42BPG activity raises EPHB3's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.95× lower at baseline in the lines without CDC42BPG | 0.085 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[KCNK5]] | B | KCNK5 activity raises EPHB3's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 2.07× lower at baseline in the lines without KCNK5 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2 |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 21, C 0. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC42BPG]] | B | EPHB3 activity raises CDC42BPG's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 2.47× lower at baseline in the lines without EPHB3 | 0.010 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[TENT5C]] | B | EPHB3 activity raises TENT5C's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 2.13× lower at baseline in the lines without EPHB3 | 0.014 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[ZNF511]] | B | EPHB3 activity raises ZNF511's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.52× lower at baseline in the lines without EPHB3 | 0.034 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[RAP1GAP]] | B | EPHB3 activity raises RAP1GAP's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.63× lower at baseline in the lines without EPHB3 | 0.036 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[BAIAP3]] | B | EPHB3 activity raises BAIAP3's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.61× lower at baseline in the lines without EPHB3 | 0.043 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[BIK]] | B | EPHB3 activity raises BIK's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.96× lower at baseline in the lines without EPHB3 | 0.050 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[SERPINI1]] | B | EPHB3 activity raises SERPINI1's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 2.01× lower at baseline in the lines without EPHB3 | 0.062 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[PLK3]] | B | EPHB3 activity raises PLK3's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.16× lower at baseline in the lines without EPHB3 | 0.068 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[ING1]] | B | EPHB3 activity raises ING1's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.30× lower at baseline in the lines without EPHB3 | 0.071 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[CHKA]] | B | EPHB3 activity raises CHKA's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.23× lower at baseline in the lines without EPHB3 | 0.072 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[LRCH4]] | B | EPHB3 activity raises LRCH4's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.37× lower at baseline in the lines without EPHB3 | 0.073 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| cells under [[Omeprazole (drug)]] 5 µM | B | EPHB3 activity lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | lines that do not express EPHB3 (15) vs lines expressing it (33) | the lines without EPHB3: 1.15× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.747). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.1, -6.1); signed map (-2.0, 25.8). **Vector** length 60.1, 11.6% of its response variance represented; |z| ≥ 3 in 778 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +11.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +17.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.6 | +7.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.6 | +17.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +4.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.6 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.3 | +2.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +0.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.4 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +0.4 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.0 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | +0.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | EPH receptor B3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:184,561,785-184,582,408 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Hek2, Tyro6; previously ETK2 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; EPH receptors |
| Hallmark sets | MYOGENESIS |
| Reactome | 6 pathways, smallest: Ephrin signaling; EPHB-mediated forward signaling; EPH-ephrin mediated repulsion of cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P54753](https://www.uniprot.org/uniprotkb/P54753) (Ephrin type-B receptor 3):

> Receptor tyrosine kinase which binds promiscuously transmembrane ephrin-B family ligands residing on adjacent cells, leading to contact-dependent bidirectional signaling into neighboring cells. The signaling pathway downstream of the receptor is referred to as forward signaling while the signaling pathway downstream of the ephrin ligand is referred to as reverse signaling. Generally has an overlapping and redundant function with EPHB2. Like EPHB2, functions in axon guidance during development …

**Summary**, from NCBI Gene [2049](https://www.ncbi.nlm.nih.gov/gene/2049):

> Ephrin receptors and their ligands, the ephrins, mediate numerous developmental processes, particularly in the nervous system. Based on their structures and sequence relationships, ephrins are divided into the ephrin-A (EFNA) class, which are anchored to the membrane by a glycosylphosphatidylinositol linkage, and the ephrin-B (EFNB) class, which are transmembrane proteins. The Eph family of receptors are divided into two groups based on the similarity of their extracellular domain sequences and …

**Accessions** — [HGNC:3394](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3394) · Entrez [2049](https://www.ncbi.nlm.nih.gov/gene/2049) · UniProt [P54753](https://www.uniprot.org/uniprotkb/P54753) · Ensembl [ENSG00000182580](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182580)

## Data

Gene col 11303: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11303); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11303, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11303]; `tensor/DDL_lfc|DDL_z.npy` [11303]; `embed/gene_vectors.npy` [11303]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11303 or target_col == 11303). Every well: [[EPHB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
