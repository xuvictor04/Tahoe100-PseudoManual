---
symbol: "GATA3"
type: "gene"
col: 2853
ensembl_id: "ENSG00000107485"
name: "GATA binding protein 3"
location: "10p14"
module: 68
arm: "+"
pooled_cpm: 10.86
n_lines_expressing: 28
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# GATA3

*GATA binding protein 3* — 10p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.92× (z +16.9, q 0e+00, up in 18 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 3 lines (COLO 205 0.0269×, CHP-212 0.193×, Panc 03.27 0.207×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (BT-474 0.109×, COLO 205 0.105×); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 0.0290×; ⚠ cell-cycle shift, explains ~26% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.0982×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLX2]] (+0.65, fdr 7e-06), [[EID2]] (+0.60, fdr 1e-05), [[H2AJ]] (+0.58, fdr 1e-05); moves opposite to [[FBXW2]] (-0.58, fdr 2e-05), [[BCAP31]] (-0.58, fdr 1e-05), [[NIPA2]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RARRES1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZNF155]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2853.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.92×** | +16.9 | 0e+00 | 18/24 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.50×** | +15.5 | 0e+00 | 17/23 (CFPAC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.20×** | +10.2 | 4e-22 | 20/23 (CFPAC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.05×** | +9.4 | 7e-19 | 19/24 (CFPAC-1, NCI-H23, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.84×** | +7.5 | 6e-12 | 13/24 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.94×** | +5.8 | 6e-07 | 14/24 (A-427, HS-578T, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +4.8 | 9e-05 | 7/24 (RPMI-7951, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.78×** | +4.8 | 9e-05 | 1/13 (NCI-H23) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.8 | 1e-04 | 11/22 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +4.7 | 2e-04 | 11/25 (NCI-H1573, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +4.6 | 2e-04 | 12/24 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +4.6 | 2e-04 | 9/24 (HOP62, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.58×** | +4.0 | 0.003 | 7/24 (NCI-H23, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.54×** | +3.8 | 0.007 | 6/25 (J82, SNU-423, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.020 | 4/24 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.02×** | +3.4 | 0.022 | 4/22 (NCI-H1792, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.040 | 8/25 (A-427, A549, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.042 | 7/23 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2853.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 3 lines (COLO 205 0.0269×, CHP-212 0.193×, Panc 03.27 0.207×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (BT-474 0.109×, COLO 205 0.105×); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 0.0290×; ⚠ cell-cycle shift, explains ~26% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.0982×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.680× | -3.1 | 0.70 | 5/24 (SW1417, A549, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.709× | -3.0 | 0.70 | 2/25 (SW1417, SW 1271) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2853. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 30.1 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0290× (z -22.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0269× (z -16.2) |
| [[A-427 (line)]] | wt | 20.5 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 6.70× (z +10.6) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0982× (z -12.5) |
| [[CFPAC-1 (line)]] | alt | 43.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +13.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.43× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 21.3 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +10.9) | — |
| [[J82 (line)]] | alt | 8.82 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +11.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +9.2) | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0568× (z -11.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-172 (line)]] | wt | 3.13 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +10.2) | — |
| [[CHP-212 (line)]] | wt | 258 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.193× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 63.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +9.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.90× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 35.7 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +10.1) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 5 µM 0.207× (z -9.4) |
| [[SNU-423 (line)]] | alt | 7.89 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +11.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.72× (z +9.8) | — |
| [[A549 (line)]] | wt | 7.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.9× (z +13.7) | — |
| [[BT-474 (line)]] | alt | 127 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.109× (z -12.9) |
| [[HS-578T (line)]] | alt | 7.54 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.87× (z +9.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[PANC-1 (line)]] | alt | 7.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +9.8) | — |
| [[SW480 (line)]] | alt | 3.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.25× (z +13.7) | — |
| [[A498 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.937 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.918 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.678 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.858 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.959 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.970 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2853), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLX2]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[EID2]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[H2AJ]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 | pathway: ESR-mediated signaling; STRING 513 |
| [[FOXA2]] | +0.58 | +0.40 / +0.63 | both halves | 5e-05 | STRING 607 |
| [[EIF4EBP3]] | +0.56 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[TFAP2A]] | +0.56 | +0.47 / +0.50 | both halves | 2e-05 | STRING 693 |
| [[FAM200A]] | +0.56 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[MAP3K2-DT]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[TFAP2C]] | +0.55 | +0.47 / +0.58 | both halves | 2e-05 | STRING 858 |
| [[TOPORS]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[FOXA1]] | +0.54 | +0.55 / +0.47 | both halves | 2e-05 | pathway: ESR-mediated signaling; STRING 997 |
| [[ZNF462]] | +0.54 | +0.54 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW2]] | -0.58 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[BCAP31]] | -0.58 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[NIPA2]] | -0.53 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[STRAP]] | -0.52 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[UFD1]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 | pathway: Deubiquitination |
| [[TPD52L2]] | -0.51 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[ZNF731P]] | -0.51 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[DLST]] | -0.51 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[NAP1L4]] | -0.50 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[MAPK9]] | -0.50 | -0.37 / -0.50 | both halves | 7e-05 |  |
| [[NTAQ1]] | -0.50 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[DROSHA]] | -0.50 | -0.35 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RARRES1]] | B | RARRES1 activity raises GATA3's level | lines that do not express RARRES1 (22) vs lines expressing it (28) | 2.00× lower at baseline in the lines without RARRES1 | 0.049 | ⚠ within organs, on part of the lines; also absent: CASP10, POU5F1, ENSG00000284644; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF155]] | B | GATA3 activity raises ZNF155's level | lines that do not express GATA3 (22) vs lines expressing it (28) | 1.96× lower at baseline in the lines without GATA3 | 0.038 | ⚠ within organs, on part of the lines; also absent: TMEM108, MIR137HG, SLC66A1L |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.538). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (20.1, -4.1); signed map (13.6, -7.3). **Vector** length 66.8, 17.4% of its response variance represented; |z| ≥ 3 in 536 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +6.4 | +15.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +16.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +10.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.8 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +1.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.8 | +2.4 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -2.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | GATA binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p14 — chr10:8,045,378-8,075,198 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HDR |
| Gene groups (HGNC) | GATA zinc finger domain containing |
| Hallmark sets | APICAL_SURFACE, COMPLEMENT |
| Reactome | 16 pathways, smallest: Formation of the nephric duct; Kidney development; RUNX1 regulates transcription of genes involved in differentiation of HSCs |
| Matched by | ensembl_id |

**Function**, from UniProt [P23771](https://www.uniprot.org/uniprotkb/P23771) (Trans-acting T-cell-specific transcription factor GATA-3):

> Transcriptional activator which binds to the enhancer of the T-cell receptor alpha and delta genes. Binds to the consensus sequence 5'-AGATAG-3'. Required for the T-helper 2 (Th2) differentiation process following immune and inflammatory responses. Positively regulates ASB2 expression (By similarity). Coordinates macrophage transcriptional activation and UCP2-dependent metabolic reprogramming in response to IL33. Upon tissue injury, acts downstream of IL33 signaling to drive differentiation of …

**Summary**, from NCBI Gene [2625](https://www.ncbi.nlm.nih.gov/gene/2625):

> This gene encodes a protein which belongs to the GATA family of transcription factors. The protein contains two GATA-type zinc fingers and is an important regulator of T-cell development and plays an important role in endothelial cell biology. Defects in this gene are the cause of hypoparathyroidism with sensorineural deafness and renal dysplasia. [provided by RefSeq, Nov 2009]

**Accessions** — [HGNC:4172](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4172) · Entrez [2625](https://www.ncbi.nlm.nih.gov/gene/2625) · UniProt [P23771](https://www.uniprot.org/uniprotkb/P23771) · Ensembl [ENSG00000107485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107485)

## Data

Gene col 2853: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2853); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2853, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2853]; `tensor/DDL_lfc|DDL_z.npy` [2853]; `embed/gene_vectors.npy` [2853]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2853 or target_col == 2853). Every well: [[GATA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GATA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
