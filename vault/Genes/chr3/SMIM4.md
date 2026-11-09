---
symbol: "SMIM4"
type: "gene"
col: 9622
ensembl_id: "ENSG00000168273"
name: "ubiquinol-cytochrome c reductase complex assembly factor 5"
location: "3p21.1"
module: 23
arm: "+"
pooled_cpm: 18.14
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# SMIM4

*ubiquinol-cytochrome c reductase complex assembly factor 5* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.96× (z +30.9, q 0e+00, up in 46 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Fenofibrate (drug)]] 5 µM in 1 line (AN3 CA 0.0733×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EMC1-AS1]] (+0.75, fdr 7e-06), [[KMT2E-AS1]] (+0.68, fdr 1e-05), [[CASS4]] (+0.67, fdr 1e-05); moves opposite to [[BRD7]] (-0.66, fdr 2e-05), [[SAAL1]] (-0.57, fdr 2e-04), [[NSMCE4A]] (-0.56, fdr 6e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9622.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.96×** | +30.9 | 0e+00 | 46/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.38×** | +21.1 | 0e+00 | 44/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.61×** | +15.7 | 0e+00 | 47/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.65×** | +15.2 | 0e+00 | 44/44 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.46×** | +15.2 | 0e+00 | 45/47 (SW480, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.30×** | +14.6 | 0e+00 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.31×** | +14.1 | 5e-43 | 42/46 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.01×** | +13.5 | 2e-39 | 47/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.85×** | +12.3 | 5e-33 | 43/48 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.73×** | +12.3 | 6e-33 | 44/48 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.85×** | +10.7 | 8e-25 | 43/48 (NCI-H2347, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +10.6 | 1e-24 | 43/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.15×** | +9.4 | 3e-19 | 34/41 (NCI-H460, SW480, …) | all doses, flat | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.21×** | +9.3 | 5e-19 | 38/47 (NCI-H1792, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.04×** | +8.7 | 1e-16 | 33/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.03×** | +8.6 | 2e-16 | 37/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.00×** | +8.5 | 7e-16 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.58×** | +7.8 | 1e-13 | 34/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +5.2 | 5e-06 | 28/48 (SK-MEL-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9622.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Fenofibrate (drug)]] 5 µM in 1 line (AN3 CA 0.0733×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.782× | -3.0 | 0.96 | 8/48 (LOX-IMVI, HT-29, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9622. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.3 | 14 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.51× (z +19.9) | — |
| [[SW480 (line)]] | alt | 25.7 | 13 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +18.8) | — |
| [[HEC-1-A (line)]] | alt | 36.8 | 8 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.47× (z +19.5) | — |
| [[HOP62 (line)]] | alt | 21.0 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.40× (z +18.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.3 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.10× (z +16.1) | — |
| [[LoVo (line)]] | wt | 17.7 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.49× (z +17.6) | — |
| [[A-172 (line)]] | wt | 14.5 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.22× (z +16.6) | — |
| [[AsPC-1 (line)]] | alt | 9.11 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.62× (z +13.4) | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.08× (z +16.2) | — |
| [[NCI-H2347 (line)]] | alt | 25.8 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +14.3) | — |
| [[PANC-1 (line)]] | alt | 13.6 | 5 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.42× (z +22.3) | — |
| [[A498 (line)]] | wt | 11.6 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +17.6) | — |
| [[C32 (line)]] | wt | 17.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.68× (z +16.3) | — |
| [[HT-29 (line)]] | alt | 14.4 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.33× (z +15.3) | — |
| [[J82 (line)]] | alt | 21.0 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.63× (z +18.6) | — |
| [[KATO III (line)]] | alt | 19.9 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.48× (z +15.2) | — |
| [[LS 180 (line)]] | wt | 20.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +13.8) | — |
| [[RKO (line)]] | wt | 36.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +11.6) | — |
| [[SK-MEL-2 (line)]] | alt | 21.9 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +13.1) | — |
| [[SNU-423 (line)]] | alt | 16.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.52× (z +15.1) | — |
| [[SW1417 (line)]] | alt | 19.7 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +14.5) | — |
| [[CFPAC-1 (line)]] | alt | 9.73 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.40× (z +15.6) | — |
| [[Hs 766T (line)]] | wt | 15.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +12.1) | — |
| [[HS-578T (line)]] | alt | 20.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.69× (z +13.6) | — |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.92× (z +13.3) | — |
| [[NCI-H2030 (line)]] | alt | 19.6 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +14.3) | — |
| [[A549 (line)]] | wt | 9.61 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +16.6) | — |
| [[BT-474 (line)]] | alt | 13.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.72× (z +12.5) | — |
| [[C-33 A (line)]] | alt | 19.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 8.99 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +11.7) | — |
| [[HCT15 (line)]] | alt | 27.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 9.08 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +10.4) | — |
| [[NCI-H1792 (line)]] | alt | 15.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.44× (z +15.1) | — |
| [[Panc 03.27 (line)]] | alt | 13.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.20× (z +15.3) | — |
| [[RPMI-7951 (line)]] | alt | 29.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.48× (z +14.2) | — |
| [[SNU-1 (line)]] | wt | 22.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +11.1) | — |
| [[SW 900 (line)]] | alt | 15.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.11× (z +13.5) | — |
| [[A-427 (line)]] | wt | 17.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.15× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 24.9 | 0 | 1 | — | [[Fenofibrate (drug)]] 5 µM 0.0733× (z -8.8) |
| [[H4 (line)]] | wt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 14.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.69× (z +12.5) | — |
| [[SHP-77 (line)]] | alt | 18.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.77× (z +12.3) | — |
| [[SW48 (line)]] | wt | 35.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.23× (z +13.6) | — |
| [[CHP-212 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9622), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMC1-AS1]] | +0.75 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[KMT2E-AS1]] | +0.68 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[CASS4]] | +0.67 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[RSL1D1-DT]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[SLC25A53]] | +0.65 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[LINC01004]] | +0.65 | +0.75 / +0.46 | both halves | 3e-05 |  |
| [[FAM117A]] | +0.64 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[POLR2A]] | +0.64 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[LSMEM1]] | +0.63 | +0.68 / +0.40 | both halves | 5e-05 |  |
| [[CCDC62]] | +0.62 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[TOB2]] | +0.62 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[CD27-AS1]] | +0.62 | +0.63 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRD7]] | -0.66 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[SAAL1]] | -0.57 | -0.60 / -0.32 | both halves | 2e-04 |  |
| [[NSMCE4A]] | -0.56 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[USP14]] | -0.55 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[RBM17]] | -0.55 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[ANXA7]] | -0.53 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[COG2]] | -0.53 | -0.40 / -0.25 | both halves | 4e-04 |  |
| [[WDR7]] | -0.52 | -0.23 / -0.32 | both halves | 5e-04 |  |
| [[BLMH]] | -0.52 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[NUP93]] | -0.51 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[FIGNL1]] | -0.51 | -0.49 / -0.25 | both halves | 4e-04 |  |
| [[IMMT]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SMIM4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.540). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (28.6, -24.1); signed map (3.9, 14.0). **Vector** length 70.7, 16.6% of its response variance represented; |z| ≥ 3 in 1,282 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.2 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +15.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.3 | +15.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.7 | +14.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +10.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +7.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +4.1 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -3.5 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | +1.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.1 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.1 | +3.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.9 | +12.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | +0.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ubiquinol-cytochrome c reductase complex assembly factor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:52,534,013-52,579,237 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C3orf78, SMIM4 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex III assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVI0](https://www.uniprot.org/uniprotkb/Q8WVI0) (Ubiquinol-cytochrome c reductase complex assembly factor 5):

> Required for the assembly and stability of the mitochondrial ubiquinol-cytochrome c reductase complex (complex III (CIII) or cytochrome b-c1 complex), a multisubunit transmembrane complex that is part of the mitochondrial electron transport chain (ETC) which drives oxidative phosphorylation (By similarity). Mediates early complex III biogenesis (By similarity). Participates in regulating the levels of electron transport chain proteins, and therefore energy supply, in response to changes in …

**Summary**, from NCBI Gene [440957](https://www.ncbi.nlm.nih.gov/gene/440957):

> Enables mitochondrial ribosome binding activity. Involved in mitochondrial respiratory chain complex IV assembly. Located in mitochondrion. Is active in mitochondrial inner membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:37257](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37257) · Entrez [440957](https://www.ncbi.nlm.nih.gov/gene/440957) · UniProt [Q8WVI0](https://www.uniprot.org/uniprotkb/Q8WVI0) · Ensembl [ENSG00000168273](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168273)

## Data

Gene col 9622: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9622); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9622, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9622]; `tensor/DDL_lfc|DDL_z.npy` [9622]; `embed/gene_vectors.npy` [9622]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9622 or target_col == 9622). Every well: [[SMIM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMIM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
