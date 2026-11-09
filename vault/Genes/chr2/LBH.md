---
symbol: "LBH"
type: "gene"
col: 13120
ensembl_id: "ENSG00000213626"
name: "LBH regulator of Wnt signaling pathway"
location: "2p23.1"
module: 206
arm: "+"
pooled_cpm: 20.89
n_lines_expressing: 28
n_dd_up: 25
n_dd_down: 6
n_dd_up_clean: 18
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 2
tags: ["gene", "module/206"]
generated_by: "tahoemap"
---

# LBH

*LBH regulator of Wnt signaling pathway* — 2p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.25× (z +31.0, q 0e+00, up in 25 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 0.703× (z -4.2, q 0.012, down in 11 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM107B]] (+0.52, fdr 1e-05), [[SLIT2]] (+0.51, fdr 1e-05), [[MXD1]] (+0.51, fdr 3e-05); moves opposite to [[ARMC8]] (-0.48, fdr 2e-05), [[COPS8]] (-0.48, fdr 4e-05), [[ERCC8]] (-0.48, fdr 3e-05).
> It is in [[Module 206]], a single-armed module (Constitutive Signaling by Aberrant PI3K in Cancer).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[OSBPL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13120.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.25×** | +31.0 | 0e+00 | 25/25 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.86×** | +12.6 | 9e-34 | 16/26 (C32, SK-MEL-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +11.8 | 8e-30 | 18/26 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +11.4 | 7e-28 | 14/25 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +10.7 | 1e-24 | 18/23 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.35×** | +10.2 | 2e-22 | 10/21 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.27×** | +9.8 | 1e-20 | 21/26 (SK-MEL-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.26×** | +9.8 | 1e-20 | 17/26 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +8.8 | 6e-17 | 20/24 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +7.0 | 2e-10 | 9/19 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +6.2 | 3e-08 | 9/25 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +5.4 | 3e-06 | 14/26 (SK-MEL-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.37×** | +5.4 | 3e-06 | 11/19 (CFPAC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +5.1 | 1e-05 | 8/26 (A498, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +5.0 | 2e-05 | 6/19 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.64×** | +4.2 | 9e-04 | 7/24 (CFPAC-1, A-172, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.002 | 13/26 (A498, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.006 | 9/25 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.022 | 10/26 (CFPAC-1, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13120.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.703×** | -4.2 | 0.012 | 11/26 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.719×** | -4.0 | 0.020 | 13/25 (NCI-H1792, Hs 766T, …) | all doses, flat | position effect removed |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **0.735×** | -3.7 | 0.037 | 9/26 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.817×** | -3.4 | 0.069 | 6/26 (SW 900, AN3 CA, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 5 µM |  | **0.819×** | -3.4 | 0.069 | 8/26 (A549, SW 900, …) | top dose only | position effect removed |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.756×** | -3.4 | 0.069 | 12/26 (NCI-H2347, SW 900, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 0.835× | -3.1 | 0.16 | 5/26 (SW480, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13120. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 23.4 | 7 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +12.7) | — |
| [[A498 (line)]] | wt | 27.1 | 4 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.51× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 48.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -9.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 30.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +13.3) | — |
| [[SK-MEL-2 (line)]] | alt | 7.58 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.59× (z +10.5) | — |
| [[A549 (line)]] | wt | 36.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.81× (z +15.4) | — |
| [[HOP62 (line)]] | alt | 5.45 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.5× (z +15.6) | — |
| [[J82 (line)]] | alt | 9.14 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.55× (z +14.3) | — |
| [[SNU-423 (line)]] | alt | 28.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +10.9) | — |
| [[SW480 (line)]] | alt | 88.4 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.198× (z -11.0) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.424× (z -8.5) |
| [[A-172 (line)]] | wt | 67.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +11.4) | — |
| [[H4 (line)]] | wt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.92× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 8.50 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.49× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 9.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.88× (z +9.6) | — |
| [[LoVo (line)]] | wt | 11.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 42.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 28.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +16.1) | — |
| [[RPMI-7951 (line)]] | alt | 6.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.29× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 15.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +8.9) | — |
| [[A-427 (line)]] | wt | 3.70 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 117 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.70 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.91 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.38 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13120), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM107B]] | +0.52 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[SLIT2]] | +0.51 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[MXD1]] | +0.51 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[PIK3CD]] | +0.51 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[SORBS1]] | +0.51 | +0.36 / +0.54 | both halves | 9e-05 |  |
| [[LYPD1]] | +0.51 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[SOX11]] | +0.50 | +0.40 / +0.43 | both halves | 4e-05 |  |
| [[PCDH10]] | +0.49 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[PCDH17]] | +0.49 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[C7orf57]] | +0.49 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[MYO6]] | +0.49 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[CLDN4]] | +0.49 | +0.45 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC8]] | -0.48 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[COPS8]] | -0.48 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[ERCC8]] | -0.48 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[GFM1]] | -0.47 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[NDUFAF5]] | -0.46 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[PPP5C]] | -0.44 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[C5orf22]] | -0.43 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[IRAK3]] | -0.43 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[TMEM168]] | -0.43 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[TIMM23B]] | -0.43 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[TIMM23]] | -0.43 | -0.45 / -0.43 | both halves | 4e-05 |  |
| [[MRPL16]] | -0.43 | -0.36 / -0.39 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LBH's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LHX1]] | B | LHX1 activity raises LBH's level | lines that do not express LHX1 (27) vs lines expressing it (23) | 2.99× lower at baseline in the lines without LHX1 | 0.033 | ⚠ within organs, on part of the lines; also absent: LHX1-DT, ADAMTS16, ECSCR |
| [[RALGPS2]] | B | RALGPS2 activity raises LBH's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 3.11× lower at baseline in the lines without RALGPS2 | 0.066 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[KPNA7]] | B | KPNA7 activity raises LBH's level | lines that do not express KPNA7 (10) vs lines expressing it (40) | 2.56× lower at baseline in the lines without KPNA7 | 0.099 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[C7orf57]] | C | C7orf57 activity raises LBH's level | lines that do not express C7orf57 (18) vs lines expressing it (32) | 3.25× lower at baseline in the lines without C7orf57 | 0.021 | ⚠ within organs, on part of the lines; also absent: CACNG6, GNG11, PAPLN; co-absent with the target |
| [[LHX1-DT]] | C | LHX1-DT activity raises LBH's level | lines that do not express LHX1-DT (28) vs lines expressing it (22) | 3.50× lower at baseline in the lines without LHX1-DT | 0.036 | ⚠ within organs, on part of the lines; also absent: LHX1, EYA4, CDH4; co-absent with the target |
| [[SLIT2]] | C | SLIT2 activity raises LBH's level | lines that do not express SLIT2 (20) vs lines expressing it (30) | 2.48× lower at baseline in the lines without SLIT2 | 0.063 | ⚠ within organs, on part of the lines; also absent: CHSY3, MOXD1, IDO1; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSBPL3]] | B | LBH activity raises OSBPL3's level | lines that do not express LBH (22) vs lines expressing it (28) | 1.92× lower at baseline in the lines without LBH | 0.014 | ⚠ within organs, on part of the lines; also absent: SNAI2, GNG2, PLAT |
| [[METTL21A]] | B | LBH activity lowers METTL21A's level | lines that do not express LBH (22) vs lines expressing it (28) | 1.46× higher at baseline in the lines without LBH | 0.032 | ⚠ within organs, on part of the lines; also absent: SNAI2, GNG2, PLAT |

## Where it sits

- **Module**: [[Module 206]] — Constitutive Signaling by Aberrant PI3K in Cancer; 15 genes; every member is in the + arm (projection on the module's main direction 0.415). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.9, 28.9); signed map (37.5, 29.4). **Vector** length 76.8, 19.2% of its response variance represented; |z| ≥ 3 in 808 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +31.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +12.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +5.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +3.4 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -2.6 | -4.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.3 | -2.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.3 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | LBH regulator of Wnt signaling pathway |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.1 — chr2:30,231,534-30,323,730 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53QV2](https://www.uniprot.org/uniprotkb/Q53QV2) (Protein LBH):

> Transcriptional activator which may act in mitogen-activated protein kinase signaling pathway.

**Summary**, from NCBI Gene [81606](https://www.ncbi.nlm.nih.gov/gene/81606):

> Involved in negative regulation of DNA-templated transcription; positive regulation of DNA-templated transcription; and regulation of MAPK cascade. Located in cytoplasm and nucleus. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29532](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29532) · Entrez [81606](https://www.ncbi.nlm.nih.gov/gene/81606) · UniProt [Q53QV2](https://www.uniprot.org/uniprotkb/Q53QV2) · Ensembl [ENSG00000213626](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213626)

## Data

Gene col 13120: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13120); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13120, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13120]; `tensor/DDL_lfc|DDL_z.npy` [13120]; `embed/gene_vectors.npy` [13120]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13120 or target_col == 13120). Every well: [[LBH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LBH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
