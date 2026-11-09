---
symbol: "XK"
type: "gene"
col: 519
ensembl_id: "ENSG00000047597"
name: "X-linked Kx blood group antigen, Kell and VPS13A binding protein"
location: "Xp21.1"
module: 55
arm: "+"
pooled_cpm: 2.75
n_lines_expressing: 32
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 8
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# XK

*X-linked Kx blood group antigen, Kell and VPS13A binding protein* — Xp21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.31× (z +13.2, q 8e-37, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.77× (z +7.5, q 9e-12, up in 13 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.579× (z -5.2, q 1e-04, down in 15 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KBTBD11]] (+0.68, fdr 1e-05), [[DENND2D]] (+0.63, fdr 1e-05), [[RAB15]] (+0.62, fdr 1e-05); moves opposite to [[INAFM1]] (-0.52, fdr 3e-05), [[TRNAU1AP]] (-0.51, fdr 3e-05), [[POLR2J3-1]] (-0.50, fdr 1e-04).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ESRP2]] → it (grade B ⚠); 8 go from it, the strongest it → [[PLPP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 519.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.31×** | +13.2 | 8e-37 | 2/2 (KATO III, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.23×** | +11.0 | 1e-25 | 8/11 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.02×** | +9.6 | 2e-19 | 3/4 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +7.5 | 9e-12 | 13/28 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.67×** | +4.8 | 2e-04 | 11/25 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.66×** | +4.7 | 2e-04 | 1/11 (SHP-77) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +4.6 | 4e-04 | 1/11 (LS 180) | top dose only | cell-cycle shift (explains ~4% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.96×** | +4.5 | 5e-04 | 1/8 (NCI-H2030) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.3 | 0.001 | 2/16 (NCI-H1792, LS 180) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.33×** | +4.1 | 0.002 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.36×** | +4.0 | 0.003 | 4/27 (KATO III, SW48, …) | top dose only | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.9 | 0.005 | 0/17 | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.74×** | +3.7 | 0.010 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +3.2 | 0.051 | 1/7 (NCI-H2030) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.060 | 5/28 (A-427, NCI-H23, …) | top dose only |  |
| [[Roxadustat (drug)]] 0.05 µM |  | **1.43×** | +3.1 | 0.077 | 1/20 (NCI-H2030) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.43×** | +3.0 | 0.077 | 1/17 (A-427) | inconsistent across doses | low cells (technical?) |
| [[Naproxen (drug)]] 0.05 µM |  | **1.42×** | +3.0 | 0.087 | 4/19 (NCI-H2030, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 519.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.579×** | -5.2 | 1e-04 | 15/28 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.672×** | -3.8 | 0.043 | 14/25 (SW48, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.668×** | -3.6 | 0.073 | 2/28 (A-172, LOX-IMVI) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.713× | -3.2 | 0.18 | 6/20 (NCI-H2030, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.727× | -3.1 | 0.24 | 5/28 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Methotrexate (drug)]] 0.5 µM |  | 0.730× | -3.0 | 0.24 | 6/26 (KATO III, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 519. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 7.80 | 0 | 2 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0927× (z -9.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.105× (z -9.1) |
| [[SW48 (line)]] | wt | 9.87 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -10.6) |
| [[KATO III (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.219× (z -9.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -13.0) ⚠ cell-cycle shift, explains ~81% of this change |
| [[A-172 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.846 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.962 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.729 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.562 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.309 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.414 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.255 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.746 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.633 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.733 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.520 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.341 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.822 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.681 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 519), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD11]] | +0.68 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[DENND2D]] | +0.63 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[RAB15]] | +0.62 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[RAB4A-AS1]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[CTSE]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[AGMAT]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[TTPA]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[SPTBN2]] | +0.58 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SLC27A2]] | +0.57 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[DHX15]] | +0.57 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[ZNF860]] | +0.56 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[LAD1]] | +0.56 | +0.46 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INAFM1]] | -0.52 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[TRNAU1AP]] | -0.51 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[POLR2J3-1]] | -0.50 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[CWC25]] | -0.50 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[RANBP10]] | -0.49 | -0.50 / -0.40 | both halves | 4e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[UPF2]] | -0.49 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[TERF2IP]] | -0.48 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[POLR2J4]] | -0.48 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[MAPK8IP3]] | -0.48 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[NOL3]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[NOSIP]] | -0.48 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[BBOF1]] | -0.48 | -0.39 / -0.44 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ESRP2]] | B | ESRP2 activity raises XK's level | lines that do not express ESRP2 (26) vs lines expressing it (24) | 1.89× lower at baseline in the lines without ESRP2 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS22, MARVELD3, CRB3 |
| [[PIK3AP1]] | B | PIK3AP1 activity raises XK's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 2.00× lower at baseline in the lines without PIK3AP1 | 0.046 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLPP2]] | B | XK activity raises PLPP2's level | lines that do not express XK (18) vs lines expressing it (32) | 2.11× lower at baseline in the lines without XK | 0.013 | ⚠ within organs, on part of the lines; also absent: SAMD12, MARVELD2, BTC; maybe low, not absent |
| [[KBTBD11]] | B | XK activity raises KBTBD11's level | lines that do not express XK (18) vs lines expressing it (32) | 1.95× lower at baseline in the lines without XK | 0.022 | ⚠ within organs, on part of the lines; also absent: SAMD12, MARVELD2, BTC; maybe low, not absent |
| [[SLC27A2]] | B | XK activity raises SLC27A2's level | lines that do not express XK (18) vs lines expressing it (32) | 2.00× lower at baseline in the lines without XK | 0.022 | ⚠ within organs, on part of the lines; also absent: SAMD12, MARVELD2, BTC; maybe low, not absent |
| [[BBOF1]] | B | XK activity lowers BBOF1's level | lines that do not express XK (18) vs lines expressing it (32) | 1.43× higher at baseline in the lines without XK | 0.029 | ⚠ within organs, on part of the lines; also absent: SAMD12, MARVELD2, BTC; maybe low, not absent |
| [[PIK3AP1]] | B | XK activity raises PIK3AP1's level | lines that do not express XK (18) vs lines expressing it (32) | 2.21× lower at baseline in the lines without XK | 0.069 | ⚠ within organs, on part of the lines; also absent: SAMD12, MARVELD2, BTC; maybe low, not absent |
| [[SLC9A2]] | B | XK activity raises SLC9A2's level | lines that do not express XK (18) vs lines expressing it (32) | 2.43× lower at baseline in the lines without XK | 0.070 | ⚠ within organs, on part of the lines; also absent: SAMD12, MARVELD2, BTC; maybe low, not absent |
| cells under [[Tucidinostat (drug)]] 5 µM | B | XK activity raises the cells' numbers under Tucidinostat 5 µM (protects the cells) | lines that do not express XK (18) vs lines expressing it (30) | the lines without XK: 0.90× the cells of the other lines | 0.077 | ⚠ within organs, on part of the lines; also absent: SAMD12, MARVELD2, BTC; maybe low, not absent |
| [[COBL]] | B | XK activity raises COBL's level | lines that do not express XK (18) vs lines expressing it (32) | 2.53× lower at baseline in the lines without XK | 0.085 | ⚠ within organs, on part of the lines; also absent: SAMD12, MARVELD2, BTC; maybe low, not absent |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.500). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.5, 46.3); signed map (68.5, 11.1). **Vector** length 37.4, 5.22% of its response variance represented; |z| ≥ 3 in 678 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +13.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +9.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.8 | +1.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -2.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -2.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -0.9 | -5.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -1.9 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -0.7 | -2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | X-linked Kx blood group antigen, Kell and VPS13A binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp21.1 — chrX:37,685,791-37,732,130 (+) |
| Ensembl biotype | protein_coding |
| Also known as | XKR1, Kx, X1k; previously NA, NAC |
| Gene groups (HGNC) | Blood group antigens; XK related family |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 18 pathways, smallest: Budding; Fusion and Uncoating of the Influenza Virion; Fusion of the Influenza Virion to the Host Cell Endosome |
| Matched by | ensembl_id |

**Function**, from UniProt [P51811](https://www.uniprot.org/uniprotkb/P51811) (Endoplasmic reticulum membrane adapter protein XK):

> Recruits the lipid transfer protein VPS13A from lipid droplets to the endoplasmic reticulum (ER) membrane.

**Summary**, from NCBI Gene [7504](https://www.ncbi.nlm.nih.gov/gene/7504):

> This locus controls the synthesis of the Kell blood group 'precursor substance' (Kx). Mutations in this gene have been associated with McLeod syndrome, an X-linked, recessive disorder characterized by abnormalities in the neuromuscular and hematopoietic systems. The encoded protein has structural characteristics of prokaryotic and eukaryotic membrane transport proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12811](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12811) · Entrez [7504](https://www.ncbi.nlm.nih.gov/gene/7504) · UniProt [P51811](https://www.uniprot.org/uniprotkb/P51811) · Ensembl [ENSG00000047597](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000047597)

## Data

Gene col 519: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 519); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 519, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 519]; `tensor/DDL_lfc|DDL_z.npy` [519]; `embed/gene_vectors.npy` [519]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 519 or target_col == 519). Every well: [[XK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
