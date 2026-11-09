---
symbol: "UTP23"
type: "gene"
col: 7215
ensembl_id: "ENSG00000147679"
name: "UTP23 small subunit processome component"
location: "8q24.11"
module: 11
arm: "+"
pooled_cpm: 50.18
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# UTP23

*UTP23 small subunit processome component* — 8q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.40× (z +17.5, q 0e+00, up in 47 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (HEC-1-A 0.212×, SHP-77 0.317×, SK-MEL-2 0.279×, LoVo 0.398×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (CHP-212 0.120×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[γ-Oryzanol (drug)]] 0.5 µM in 1 line (NCI-H661 0.0885×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEBPZ]] (+0.73, fdr 7e-06), [[ZNF264]] (+0.71, fdr 7e-06), [[CCDC174]] (+0.70, fdr 7e-06); moves opposite to [[MAPK9]] (-0.62, fdr 1e-05), [[ELOVL5]] (-0.61, fdr 1e-05), [[MFSD14B]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7215.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.40×** | +17.5 | 0e+00 | 47/47 (HT-29, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +16.3 | 0e+00 | 43/47 (NCI-H2030, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.03×** | +14.1 | 3e-43 | 45/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.03×** | +14.1 | 3e-43 | 44/48 (LOX-IMVI, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.05×** | +13.8 | 3e-41 | 44/47 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.04×** | +13.7 | 1e-40 | 45/48 (HT-29, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +13.1 | 5e-37 | 43/48 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +10.0 | 1e-21 | 39/48 (NCI-H460, HT-29, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.63×** | +9.8 | 7e-21 | 41/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +9.3 | 1e-18 | 36/48 (PANC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.23×** | +8.4 | 2e-15 | 38/49 (A498, KATO III, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +7.6 | 2e-12 | 33/48 (SHP-77, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +6.6 | 1e-09 | 31/49 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +6.3 | 1e-08 | 24/48 (NCI-H2347, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +5.8 | 2e-07 | 29/48 (KATO III, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.7 | 3e-07 | 27/48 (J82, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7215.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (HEC-1-A 0.212×, SHP-77 0.317×, SK-MEL-2 0.279×, LoVo 0.398×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (CHP-212 0.120×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[γ-Oryzanol (drug)]] 0.5 µM in 1 line (NCI-H661 0.0885×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.892× | -7.7 | 8e-12 | 4/49 (COLO 205, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 0.894× | -3.2 | 0.39 | 2/48 (CFPAC-1, SW 900) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7215. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 54.3 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.33× (z +14.2) | — |
| [[NCI-H2347 (line)]] | alt | 54.8 | 8 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.11× (z +12.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.95× (z +12.6) | — |
| [[HT-29 (line)]] | alt | 101 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.02× (z +17.3) | — |
| [[SW480 (line)]] | alt | 55.4 | 7 | 0 | [[Harringtonine (drug)]] 0.5 µM 2.19× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 72.4 | 6 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +12.1) | — |
| [[NCI-H460 (line)]] | wt | 30.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.3) | — |
| [[J82 (line)]] | alt | 46.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.4) | — |
| [[NCI-H23 (line)]] | alt | 38.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +13.0) | — |
| [[PANC-1 (line)]] | alt | 57.8 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 46.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 60.8 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.27× (z +13.3) | — |
| [[NCI-H2030 (line)]] | alt | 32.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +14.8) | — |
| [[A498 (line)]] | wt | 58.4 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.40× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 37.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +10.7) | — |
| [[KATO III (line)]] | alt | 64.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 39.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.99× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.398× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 53.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +13.8) | — |
| [[NCI-H1792 (line)]] | alt | 33.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +13.4) | — |
| [[Panc 03.27 (line)]] | alt | 55.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.83× (z +10.0) | — |
| [[RKO (line)]] | wt | 100 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.59× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 43.7 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.21× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 43.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.85× (z +9.5) | — |
| [[LS 180 (line)]] | wt | 33.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 95.4 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.29× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 46.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.39× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 73.0 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.38× (z +9.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +8.6) | — |
| [[A-427 (line)]] | wt | 23.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +8.7) | — |
| [[A549 (line)]] | wt | 42.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +8.8) | — |
| [[C32 (line)]] | wt | 44.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 80.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 51.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 52.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +10.5) | — |
| [[NCI-H661 (line)]] | alt | 43.3 | 0 | 1 | — | [[γ-Oryzanol (drug)]] 0.5 µM 0.0885× (z -8.9) |
| [[SNU-423 (line)]] | alt | 32.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 43.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.14× (z +8.8) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7215), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEBPZ]] | +0.73 | +0.77 / +0.74 | both halves | 7e-06 | STRING 658 |
| [[ZNF264]] | +0.71 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[SURF6]] | +0.70 | +0.73 / +0.71 | both halves | 7e-06 | STRING 705 |
| [[MRPS18B]] | +0.69 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[ESF1]] | +0.69 | +0.77 / +0.66 | both halves | 7e-06 | same gene group; STRING 787 |
| [[ZNF585A]] | +0.68 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[RPP38]] | +0.67 | +0.70 / +0.66 | both halves | 7e-06 | STRING 563 |
| [[HELQ]] | +0.67 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[ZNF146]] | +0.67 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.66 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.66 | +0.70 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK9]] | -0.62 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[ELOVL5]] | -0.61 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[MFSD14B]] | -0.60 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[DPY19L1]] | -0.59 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[ZDHHC20]] | -0.58 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[AKT1]] | -0.56 | -0.55 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UTP23's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.726). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.4, 2.9); signed map (-1.0, -19.1). **Vector** length 93.8, 24.9% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.7 | +14.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +17.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.7 | +9.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.0 | +13.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +8.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +5.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.1 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +7.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.5 | +2.9 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | -2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.0 | -2.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +0.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.0 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +0.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -0.6 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.5 | -2.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | UTP23 small subunit processome component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.11 — chr8:116,766,505-116,849,463 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14595; previously C8orf53 |
| Gene groups (HGNC) | SSU processome; PIN-like domain superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRU9](https://www.uniprot.org/uniprotkb/Q9BRU9) (rRNA-processing protein UTP23 homolog):

> Involved in rRNA-processing and ribosome biogenesis.

**Summary**, from NCBI Gene [84294](https://www.ncbi.nlm.nih.gov/gene/84294):

> Enables mRNA 3'-UTR binding activity and mRNA 5'-UTR binding activity. Predicted to be involved in rRNA processing. Predicted to act upstream of or within endonucleolytic cleavage in 5'-ETS of tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA). Predicted to be part of small-subunit processome. Predicted to be active in nucleolus. Implicated in colorectal adenocarcinoma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28224](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28224) · Entrez [84294](https://www.ncbi.nlm.nih.gov/gene/84294) · UniProt [Q9BRU9](https://www.uniprot.org/uniprotkb/Q9BRU9) · Ensembl [ENSG00000147679](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147679)

## Data

Gene col 7215: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7215); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7215, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7215]; `tensor/DDL_lfc|DDL_z.npy` [7215]; `embed/gene_vectors.npy` [7215]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7215 or target_col == 7215). Every well: [[UTP23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UTP23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
