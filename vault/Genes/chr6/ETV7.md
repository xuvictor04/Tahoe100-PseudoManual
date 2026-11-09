---
symbol: "ETV7"
type: "gene"
col: 197
ensembl_id: "ENSG00000010030"
name: "ETS variant transcription factor 7"
location: "6p21.31"
module: 32
arm: "+"
pooled_cpm: 4.11
n_lines_expressing: 37
n_dd_up: 28
n_dd_down: 9
n_dd_up_clean: 23
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 23
direction_downstream: 64
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# ETV7

*ETS variant transcription factor 7* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.36× (z +22.0, q 0e+00, up in 22 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.548× (z -7.2, q 4e-10, down in 19 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MX1]] (+0.81, fdr 7e-06), [[BATF2]] (+0.80, fdr 7e-06), [[IFIT3]] (+0.79, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[LCN2]] → it (grade B ⚠); 64 go from it, the strongest it → [[MYD88]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 197.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.36×** | +22.0 | 0e+00 | 22/28 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.98×** | +16.4 | 0e+00 | 23/25 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **5.61×** | +14.5 | 3e-45 | 19/32 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.58×** | +14.4 | 6e-45 | 18/31 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.43×** | +14.2 | 1e-43 | 25/29 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **5.44×** | +13.7 | 2e-40 | 25/29 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.48×** | +9.7 | 3e-20 | 1/8 (Panc 03.27) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.03×** | +9.3 | 1e-18 | 21/32 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.95×** | +8.7 | 2e-16 | 1/7 (PANC-1) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.70×** | +8.3 | 6e-15 | 14/32 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.55×** | +7.8 | 2e-13 | 9/30 (NCI-H460, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.31×** | +7.0 | 1e-10 | 2/12 (J82, HEC-1-A) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +6.8 | 4e-10 | 14/31 (A-172, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **2.06×** | +5.8 | 2e-07 | 15/29 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.63×** | +5.8 | 3e-07 | 13/31 (A-172, SW48, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.87×** | +5.2 | 6e-06 | 11/31 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.60×** | +4.1 | 0.001 | 10/32 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.45×** | +3.8 | 0.004 | 10/31 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 197.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.548×** | -7.2 | 4e-10 | 19/31 (LoVo, BT-474, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.603×** | -6.1 | 4e-07 | 16/31 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.519×** | -5.5 | 6e-06 | 18/31 (LoVo, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.553×** | -5.0 | 8e-05 | 16/30 (BT-474, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.687×** | -4.5 | 7e-04 | 14/31 (CFPAC-1, RKO, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.594×** | -4.4 | 0.001 | 14/28 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.708×** | -4.1 | 0.003 | 15/31 (CFPAC-1, COLO 205, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.683×** | -3.2 | 0.082 | 14/33 (LoVo, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.684×** | -3.2 | 0.082 | 11/31 (LoVo, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ciclopirox (drug)]] 5 µM |  | 0.776× | -3.1 | 0.13 | 12/29 (SW1417, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 197. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 21.0 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0229× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.215× (z -12.6) |
| [[SW480 (line)]] | alt | 2.08 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 62.1× (z +13.5) | — |
| [[BT-474 (line)]] | alt | 8.73 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.101× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 10.5 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.195× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 2.82 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 58.2× (z +13.4) | — |
| [[NCI-H2347 (line)]] | alt | 15.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0389× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.247× (z -10.7) |
| [[PANC-1 (line)]] | alt | 2.43 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 17.3× (z +14.2) | [[Digitoxin (drug)]] 0.05 µM 0.0372× (z -11.6) |
| [[A-172 (line)]] | wt | 2.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.8× (z +10.8) | — |
| [[A549 (line)]] | wt | 1.73 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 3.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 2.97 | 0 | 1 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.0361× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 1.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.4× (z +11.4) | — |
| [[SHP-77 (line)]] | alt | 1.33 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 161× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 3.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.0× (z +10.8) | — |
| [[SW48 (line)]] | wt | 8.98 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0613× (z -8.5) |
| [[A-427 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.581 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.628 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.756 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.983 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.838 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.969 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.877 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.464 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.26 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 197), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MX1]] | +0.81 | +0.67 / +0.84 | both halves | 7e-06 |  |
| [[BATF2]] | +0.80 | +0.67 / +0.84 | both halves | 7e-06 | STRING 866 |
| [[IFIT3]] | +0.79 | +0.68 / +0.82 | both halves | 7e-06 |  |
| [[DDX60]] | +0.79 | +0.70 / +0.80 | both halves | 7e-06 |  |
| [[PARP14]] | +0.79 | +0.69 / +0.83 | both halves | 7e-06 |  |
| [[IFI44]] | +0.79 | +0.66 / +0.86 | both halves | 7e-06 |  |
| [[RSAD2]] | +0.79 | +0.69 / +0.83 | both halves | 7e-06 | STRING 420 |
| [[EPSTI1]] | +0.78 | +0.67 / +0.82 | both halves | 7e-06 |  |
| [[OAS2]] | +0.78 | +0.62 / +0.82 | both halves | 7e-06 |  |
| [[XAF1]] | +0.78 | +0.62 / +0.82 | both halves | 7e-06 |  |
| [[IFI44L]] | +0.78 | +0.60 / +0.81 | both halves | 7e-06 |  |
| [[CMPK2]] | +0.77 | +0.61 / +0.82 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 22, C 1. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LCN2]] | B | LCN2 activity raises ETV7's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 2.84× lower at baseline in the lines without LCN2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[MUC4]] | B | MUC4 activity raises ETV7's level | lines that do not express MUC4 (41) vs lines expressing it (9) | 2.83× lower at baseline in the lines without MUC4 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, SLC34A2, CST6 |
| [[MX1]] | B | MX1 activity raises ETV7's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.95× lower at baseline in the lines without MX1 | 0.005 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[RHOV]] | B | RHOV activity raises ETV7's level | lines that do not express RHOV (23) vs lines expressing it (27) | 2.19× lower at baseline in the lines without RHOV | 0.008 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |
| [[STEAP4]] | B | STEAP4 activity raises ETV7's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.56× lower at baseline in the lines without STEAP4 | 0.008 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[GBP4]] | B | GBP4 activity raises ETV7's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.53× lower at baseline in the lines without GBP4 | 0.011 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[IFI44L]] | B | IFI44L activity raises ETV7's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 1.54× lower at baseline in the lines without IFI44L | 0.020 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[DUOX2]] | B | DUOX2 activity raises ETV7's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 1.70× lower at baseline in the lines without DUOX2 | 0.034 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[EPSTI1]] | B | EPSTI1 activity raises ETV7's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 1.85× lower at baseline in the lines without EPSTI1 | 0.039 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[HCP5]] | B | HCP5 activity raises ETV7's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 1.82× lower at baseline in the lines without HCP5 | 0.043 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[SRMS]] | B | SRMS activity raises ETV7's level | lines that do not express SRMS (14) vs lines expressing it (36) | 1.86× lower at baseline in the lines without SRMS | 0.052 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[TNFSF10]] | B | TNFSF10 activity raises ETV7's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 1.82× lower at baseline in the lines without TNFSF10 | 0.059 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |

### Downstream of this gene

*64 arrows, 64 of them with an alert ⚠; grade A 0, B 63, C 1. Shown: the 12 strongest; 52 more arrows (52 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYD88]] | B | ETV7 activity raises MYD88's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 2.73× lower at baseline in the lines without ETV7 | 0.002 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[CMPK2]] | B | ETV7 activity raises CMPK2's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 2.26× lower at baseline in the lines without ETV7 | 0.002 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[PARP14]] | B | ETV7 activity raises PARP14's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 1.96× lower at baseline in the lines without ETV7 | 0.002 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[NRIR]] | B | ETV7 activity raises NRIR's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 2.02× lower at baseline in the lines without ETV7 | 0.005 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[MX1]] | B | ETV7 activity raises MX1's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 3.15× lower at baseline in the lines without ETV7 | 0.007 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[DDX60]] | B | ETV7 activity raises DDX60's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 1.90× lower at baseline in the lines without ETV7 | 0.008 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[OAS3]] | B | ETV7 activity raises OAS3's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 2.06× lower at baseline in the lines without ETV7 | 0.009 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[OAS1]] | B | ETV7 activity raises OAS1's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 2.49× lower at baseline in the lines without ETV7 | 0.009 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[PLSCR1]] | B | ETV7 activity raises PLSCR1's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 1.92× lower at baseline in the lines without ETV7 | 0.011 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[PARP9]] | B | ETV7 activity raises PARP9's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 1.71× lower at baseline in the lines without ETV7 | 0.012 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[TRIM25]] | B | ETV7 activity raises TRIM25's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 1.44× lower at baseline in the lines without ETV7 | 0.012 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[OAS2]] | B | ETV7 activity raises OAS2's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 1.86× lower at baseline in the lines without ETV7 | 0.014 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.815). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.9, 54.0); signed map (64.2, 31.1). **Vector** length 84.3, 20.1% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.67 to 56); *interferon gamma response* (hallmark, mean cos +0.68 to 60); *interferon* (control, mean cos +0.75 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +14.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +13.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +22.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.2 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +16.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +5.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +6.8 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -4.3 | -7.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.6 | -1.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.5 | -6.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.4 | -5.0 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.2 | -4.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.1 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | ETS variant transcription factor 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:36,354,091-36,387,800 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TEL2, TEL-2 |
| Gene groups (HGNC) | ETS transcription factor family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y603](https://www.uniprot.org/uniprotkb/Q9Y603) (Transcription factor ETV7):

> Transcriptional repressor; binds to the DNA sequence 5'-CCGGAAGT-3'. Isoform A does not seem to have a repressor activity. Isoform C does not seem to have a repressor activity.

**Summary**, from NCBI Gene [51513](https://www.ncbi.nlm.nih.gov/gene/51513):

> The protein encoded by this gene belongs to the ETS family of transcription factors, which is a large group of evolutionarily conserved transcriptional regulators that play an important role in a variety of cellular processes throughout development and differentiation, and are involved in oncogenesis as well. This protein is predominantly expressed in hematopoietic tissues. Several alternatively spliced transcript variants encoding different isoforms have been described for this gene …

**Accessions** — [HGNC:18160](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18160) · Entrez [51513](https://www.ncbi.nlm.nih.gov/gene/51513) · UniProt [Q9Y603](https://www.uniprot.org/uniprotkb/Q9Y603) · Ensembl [ENSG00000010030](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010030)

## Data

Gene col 197: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 197); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 197, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 197]; `tensor/DDL_lfc|DDL_z.npy` [197]; `embed/gene_vectors.npy` [197]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 197 or target_col == 197). Every well: [[ETV7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ETV7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
