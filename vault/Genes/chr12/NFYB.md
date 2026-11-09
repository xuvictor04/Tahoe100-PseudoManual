---
symbol: "NFYB"
type: "gene"
col: 4227
ensembl_id: "ENSG00000120837"
name: "nuclear transcription factor Y subunit beta"
location: "12q23.3"
module: 28
arm: "+"
pooled_cpm: 24.85
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# NFYB

*nuclear transcription factor Y subunit beta* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.13× (z +26.2, q 0e+00, up in 47 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-1 0.104×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3H6]] (+0.75, fdr 7e-06), [[SCAF11]] (+0.71, fdr 7e-06), [[TRMT1L]] (+0.68, fdr 7e-06); moves opposite to [[VMP1]] (-0.64, fdr 7e-06), [[RAB5C]] (-0.63, fdr 1e-05), [[CAP1]] (-0.63, fdr 2e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF214]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4227.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.13×** | +26.2 | 0e+00 | 47/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.97×** | +17.7 | 0e+00 | 46/47 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.62×** | +15.0 | 0e+00 | 46/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.40×** | +14.0 | 1e-42 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +11.8 | 8e-30 | 39/48 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.84×** | +9.9 | 5e-21 | 39/48 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.73×** | +8.9 | 3e-17 | 34/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.63×** | +7.9 | 2e-13 | 36/47 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.49×** | +6.2 | 3e-08 | 15/34 (J82, HEC-1-A, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.45×** | +6.0 | 1e-07 | 31/47 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.40×** | +5.4 | 3e-06 | 21/42 (J82, SK-MEL-2, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +5.2 | 1e-05 | 22/45 (SW480, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.35×** | +4.9 | 5e-05 | 25/48 (HOP62, SW480, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.22×** | +4.6 | 2e-04 | 16/48 (MIA PaCa-2, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.5 | 3e-04 | 20/47 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +4.3 | 5e-04 | 22/47 (NCI-H23, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[LJI308 (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.006 | 13/48 (SNU-423, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.7 | 0.007 | 20/48 (HEC-1-A, SNU-1, …) | top dose only |  |
| [[NG25 (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.031 | 8/48 (SNU-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +2.9 | 0.093 | 11/48 (NCI-H1792, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4227.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-1 0.104×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.819× | -3.2 | 0.42 | 17/47 (hTERT-HPNE, SNU-423, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.688× | -3.2 | 0.42 | 9/47 (LoVo, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4227. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 20.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +15.6) | — |
| [[NCI-H460 (line)]] | wt | 24.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +16.6) | — |
| [[HEC-1-A (line)]] | alt | 21.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +13.1) | — |
| [[PANC-1 (line)]] | alt | 27.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +18.6) | — |
| [[SW480 (line)]] | alt | 24.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +15.5) | — |
| [[AsPC-1 (line)]] | alt | 25.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +16.3) | — |
| [[J82 (line)]] | alt | 34.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.98× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[KATO III (line)]] | alt | 25.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +14.5) | — |
| [[LOX-IMVI (line)]] | wt | 25.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +16.8) | — |
| [[SK-MEL-2 (line)]] | alt | 21.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +12.5) | — |
| [[A-427 (line)]] | wt | 36.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.5) | — |
| [[A549 (line)]] | wt | 25.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +15.2) | — |
| [[C32 (line)]] | wt | 15.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +14.6) | — |
| [[HS-578T (line)]] | alt | 22.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 30.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.20× (z +15.5) | — |
| [[NCI-H2030 (line)]] | alt | 23.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +15.1) | — |
| [[NCI-H23 (line)]] | alt | 25.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +14.2) | — |
| [[RKO (line)]] | wt | 25.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +15.0) | — |
| [[SNU-1 (line)]] | wt | 28.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +9.5) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.104× (z -11.8) |
| [[SW1417 (line)]] | alt | 33.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.4) | — |
| [[A-172 (line)]] | wt | 31.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +12.7) | — |
| [[COLO 205 (line)]] | alt | 8.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 24.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 18.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 19.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +13.3) | — |
| [[hTERT-HPNE (line)]] | wt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +9.5) | — |
| [[LoVo (line)]] | wt | 21.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[LS 180 (line)]] | wt | 16.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 21.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 21.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +14.6) | — |
| [[SW 900 (line)]] | alt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +12.2) | — |
| [[A498 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4227), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H6]] | +0.75 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[SCAF11]] | +0.71 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[TRMT1L]] | +0.68 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[COQ9]] | +0.67 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[SEPSECS]] | +0.67 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[GYG1]] | +0.66 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[ACBD5]] | +0.66 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[CLK4]] | +0.66 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[RNF146]] | +0.66 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[PPCS]] | +0.65 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[CCAR1]] | +0.65 | +0.72 / +0.38 | both halves | 6e-05 |  |
| [[PHC3]] | +0.64 | +0.50 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMP1]] | -0.64 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[RAB5C]] | -0.63 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[CAP1]] | -0.63 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[TMEM41B]] | -0.63 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | -0.61 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[LINC02458]] | -0.59 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[BCAP31]] | -0.58 | -0.68 / -0.45 | both halves | 3e-05 |  |
| [[GALNS]] | -0.58 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[NAPG]] | -0.58 | -0.62 / -0.37 | both halves | 7e-05 |  |
| [[MTPN]] | -0.57 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[KIF21B]] | -0.57 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[PSMB7]] | -0.57 | -0.66 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF214]] | B | ZNF214 activity lowers NFYB's level | lines that do not express ZNF214 (6) vs lines expressing it (44) | 1.45× higher at baseline in the lines without ZNF214 | 0.060 | ⚠ within organs, on part of the lines; also absent: S100A6, CDKN1A, PRRG1; maybe low, not absent; its own permutation p |
| [[IL15]] | B | IL15 activity lowers NFYB's level | lines that do not express IL15 (10) vs lines expressing it (40) | 1.31× higher at baseline in the lines without IL15 | 0.074 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[SYDE2]] | C | SYDE2 activity raises NFYB's level | lines that do not express SYDE2 (4) vs lines expressing it (46) | 1.59× lower at baseline in the lines without SYDE2 | 0.058 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MATN2, TLCD5; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.9, 6.1); signed map (6.5, -15.8). **Vector** length 81.8, 17.5% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.2 | +17.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +26.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.1 | +14.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.9 | +15.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +8.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.5 | +2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.4 | +1.7 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +0.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | +0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | nuclear transcription factor Y subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:104,117,086-104,138,241 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CBF-A, HAP3, NF-YB |
| Gene groups (HGNC) | Nuclear transcription factor Y |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 15 pathways, smallest: ATF6 (ATF6-alpha) activates chaperone genes; ATF6 (ATF6-alpha) activates chaperones; FOXO-mediated transcription of cell death genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P25208](https://www.uniprot.org/uniprotkb/P25208) (Nuclear transcription factor Y subunit beta):

> Component of the sequence-specific heterotrimeric transcription factor (NF-Y) which specifically recognizes a 5'-CCAAT-3' box motif found in the promoters of its target genes. NF-Y can function as both an activator and a repressor, depending on its interacting cofactors.

**Summary**, from NCBI Gene [4801](https://www.ncbi.nlm.nih.gov/gene/4801):

> The protein encoded by this gene is one subunit of a trimeric complex, forming a highly conserved transcription factor that binds with high specificity to CCAAT motifs in the promoter regions in a variety of genes. This gene product, subunit B, forms a tight dimer with the C subunit, a prerequisite for subunit A association. The resulting trimer binds to DNA with high specificity and affinity. Subunits B and C each contain a histone-like motif. Observation of the histone nature of these …

**Accessions** — [HGNC:7805](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7805) · Entrez [4801](https://www.ncbi.nlm.nih.gov/gene/4801) · UniProt [P25208](https://www.uniprot.org/uniprotkb/P25208) · Ensembl [ENSG00000120837](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120837)

## Data

Gene col 4227: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4227); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4227, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4227]; `tensor/DDL_lfc|DDL_z.npy` [4227]; `embed/gene_vectors.npy` [4227]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4227 or target_col == 4227). Every well: [[NFYB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFYB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
