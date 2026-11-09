---
symbol: "ITGB2"
type: "gene"
col: 8328
ensembl_id: "ENSG00000160255"
name: "integrin subunit beta 2"
location: "21q22.3"
module: 10
arm: "+"
pooled_cpm: 2.66
n_lines_expressing: 27
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ITGB2

*integrin subunit beta 2* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.97× (z +14.3, q 1e-43, up in 10 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.61× (z +10.8, q 5e-25, up in 10 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (NCI-H2030 0.0506×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.199×; ⚠ cell-cycle shift, explains ~26% of this change).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACKR2]] (+0.62, fdr 5e-05), [[SOCS3-DT]] (+0.59, fdr 3e-05), [[CYP1B1-AS1]] (+0.58, fdr 2e-04); moves opposite to [[PIGU]] (-0.47, fdr 3e-04), [[SLC30A6]] (-0.45, fdr 3e-04), [[MRPL2]] (-0.44, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ATAD3C]] → it (grade B ⚠); 5 go from it, the strongest it → [[LRRC56]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8328.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.97×** | +14.3 | 1e-43 | 10/10 (CFPAC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.23×** | +12.7 | 1e-34 | 5/6 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.61×** | +10.8 | 5e-25 | 10/16 (A498, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.86×** | +9.5 | 2e-19 | 8/8 (CFPAC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.80×** | +6.6 | 3e-09 | 5/24 (A498, SW480, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.11×** | +6.0 | 2e-07 | 1/8 (NCI-H2347) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.68×** | +5.8 | 5e-07 | 4/16 (HepG2/C3A, A498, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +5.2 | 1e-05 | 3/11 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +4.1 | 0.002 | 3/22 (SW480, A498, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.0 | 0.003 | 2/13 (CFPAC-1, NCI-H2030) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.38×** | +3.6 | 0.016 | 2/6 (NCI-H2347, A498) | top dose only | noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.021 | 2/16 (AsPC-1, CFPAC-1) | top dose only |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.5 | 0.021 | 2/12 (NCI-H2030, HEC-1-A) | top dose only |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.54×** | +3.4 | 0.025 | 2/16 (HEC-1-A, CFPAC-1) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +3.3 | 0.032 | 2/14 (HEC-1-A, SW480) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.036 | 3/17 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.53×** | +3.0 | 0.088 | 1/15 (SW480) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.0 | 0.088 | 2/14 (A498, NCI-H2030) | top dose only | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8328.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (NCI-H2030 0.0506×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.199×; ⚠ cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.637× | -3.6 | 0.16 | 9/24 (Hs 766T, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8328. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 8.77 | 0 | 2 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.0506× (z -13.6) |
| [[A-172 (line)]] | wt | 0.503 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.702 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.885 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.393 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.395 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.388 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.330 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.497 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.294 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.996 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.904 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.641 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8328), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACKR2]] | +0.62 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[SOCS3-DT]] | +0.59 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[CYP1B1-AS1]] | +0.58 | +0.55 / +0.29 | both halves | 2e-04 |  |
| [[STK31]] | +0.57 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[PRRT3]] | +0.55 | +0.45 / +0.38 | both halves | 7e-05 |  |
| [[B4GAT1-DT]] | +0.55 | +0.53 / +0.26 | both halves | 4e-04 |  |
| [[ID2-AS1]] | +0.54 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[LINC01503]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[IL1RAPL2]] | +0.53 | +0.33 / +0.44 | both halves | 1e-04 |  |
| [[CFL1P1-1]] | +0.52 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[IQCD]] | +0.52 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[LNCRNA-IUR]] | +0.51 | +0.23 / +0.53 | both halves | 5e-04 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGU]] | -0.47 | -0.50 / -0.27 | both halves | 3e-04 |  |
| [[SLC30A6]] | -0.45 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[MRPL2]] | -0.44 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[BLOC1S5]] | -0.44 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[SKIC8]] | -0.43 | -0.46 / -0.25 | both halves | 4e-04 | pathway: Affinity selection of immunoglobulins |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATAD3C]] | B | ATAD3C activity raises ITGB2's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 1.71× lower at baseline in the lines without ATAD3C | 0.041 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[TNNT2]] | B | TNNT2 activity raises ITGB2's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 1.59× lower at baseline in the lines without TNNT2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[TSPAN1]] | B | TSPAN1 activity raises ITGB2's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 1.65× lower at baseline in the lines without TSPAN1 | 0.062 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC56]] | B | ITGB2 activity raises LRRC56's level | lines that do not express ITGB2 (23) vs lines expressing it (27) | 1.16× lower at baseline in the lines without ITGB2 | 0.011 | ⚠ within organs, on part of the lines; also absent: RASGEF1A, CNTNAP3, ENSG00000290457; maybe low, not absent |
| [[TMEM184A]] | B | ITGB2 activity raises TMEM184A's level | lines that do not express ITGB2 (23) vs lines expressing it (27) | 1.61× lower at baseline in the lines without ITGB2 | 0.029 | ⚠ within organs, on part of the lines; also absent: RASGEF1A, CNTNAP3, ENSG00000290457; maybe low, not absent |
| [[ATAD3C]] | B | ITGB2 activity raises ATAD3C's level | lines that do not express ITGB2 (23) vs lines expressing it (27) | 1.58× lower at baseline in the lines without ITGB2 | 0.044 | ⚠ within organs, on part of the lines; also absent: RASGEF1A, CNTNAP3, ENSG00000290457; maybe low, not absent |
| [[GRAMD2A]] | B | ITGB2 activity raises GRAMD2A's level | lines that do not express ITGB2 (23) vs lines expressing it (27) | 1.25× lower at baseline in the lines without ITGB2 | 0.082 | ⚠ within organs, on part of the lines; also absent: RASGEF1A, CNTNAP3, ENSG00000290457; maybe low, not absent |
| [[ELFN2]] | C | ITGB2 activity raises ELFN2's level | lines that do not express ITGB2 (23) vs lines expressing it (27) | 2.54× lower at baseline in the lines without ITGB2 | 0.094 | ⚠ within organs, on part of the lines; also absent: RASGEF1A, CNTNAP3, ENSG00000290457; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.392). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.4, 27.7); signed map (35.9, -6.5). **Vector** length 26.8, 3.77% of its response variance represented; |z| ≥ 3 in 440 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +14.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.4 | +9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +6.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +2.6 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.9 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | +1.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.9 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.8 | -1.4 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit beta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:44,885,953-44,931,989 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LFA-1, MAC-1; previously CD18, MFI7 |
| Gene groups (HGNC) | CD molecules; Integrin beta subunits; Complement system regulators and receptors |
| Hallmark sets | ALLOGRAFT_REJECTION, KRAS_SIGNALING_UP, MTORC1_SIGNALING |
| Reactome | 15 pathways, smallest: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Integrin cell surface interactions; Interleukin-4 and Interleukin-13 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P05107](https://www.uniprot.org/uniprotkb/P05107) (Integrin beta-2):

> Integrin ITGAL:ITGB2 is a receptor for ICAM1, ICAM2 and ICAM3. Integrin ITGAL:ITGB2 is also a receptor for the secreted form of ubiquitin-like protein ISG15; the interaction is mediated by ITGAL. Integrins ITGAM:ITGB2 and ITGAX:ITGB2 are receptors for the iC3b fragment of the third complement component and for fibrinogen. Integrin ITGAX:ITGB2 recognizes the sequence G-P-R in fibrinogen alpha-chain. Integrin ITGAM:ITGB2 recognizes P1 and P2 peptides of fibrinogen gamma chain. Integrin …

**Summary**, from NCBI Gene [3689](https://www.ncbi.nlm.nih.gov/gene/3689):

> This gene encodes an integrin beta chain, which combines with multiple different alpha chains to form different integrin heterodimers. Integrins are integral cell-surface proteins that participate in cell adhesion as well as cell-surface mediated signalling. The encoded protein plays an important role in immune response and defects in this gene cause leukocyte adhesion deficiency. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:6155](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6155) · Entrez [3689](https://www.ncbi.nlm.nih.gov/gene/3689) · UniProt [P05107](https://www.uniprot.org/uniprotkb/P05107) · Ensembl [ENSG00000160255](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160255)

## Data

Gene col 8328: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8328); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8328, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8328]; `tensor/DDL_lfc|DDL_z.npy` [8328]; `embed/gene_vectors.npy` [8328]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8328 or target_col == 8328). Every well: [[ITGB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
