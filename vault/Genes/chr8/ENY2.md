---
symbol: "ENY2"
type: "gene"
col: 4190
ensembl_id: "ENSG00000120533"
name: "ENY2 transcription and export complex 2 subunit"
location: "8q23.1"
module: 69
arm: "+"
pooled_cpm: 75.44
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# ENY2

*ENY2 transcription and export complex 2 subunit* — 8q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (17 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.17× (z +8.9, q 5e-16, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.49× (z +6.5, q 1e-08, up in 35 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.261×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNIH4]] (+0.62, fdr 1e-05), [[RSRP1]] (+0.60, fdr 1e-05), [[TXNDC16]] (+0.59, fdr 3e-05); moves opposite to [[STIP1]] (-0.59, fdr 4e-05), [[LSG1]] (-0.57, fdr 1e-05), [[ZKSCAN2]] (-0.56, fdr 3e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[YTHDC1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 17 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4190.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.17×** | +8.9 | 5e-16 | 46/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.06×** | +8.3 | 2e-14 | 46/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.12×** | +8.3 | 2e-14 | 47/47 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.00×** | +7.9 | 4e-13 | 42/49 (PANC-1, SNU-423, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **2.01×** | +7.7 | 2e-12 | 43/47 (LoVo, COLO 205, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.5 | 1e-08 | 35/49 (AsPC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.3 | 1e-05 | 31/50 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **1.54×** | +4.8 | 1e-04 | 28/42 (PANC-1, SNU-423, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.32×** | +4.5 | 5e-04 | 30/48 (LoVo, C32, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.4 | 5e-04 | 29/48 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.47×** | +4.4 | 5e-04 | 30/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.50×** | +4.3 | 8e-04 | 30/45 (A-427, PANC-1, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | **1.42×** | +4.0 | 0.003 | 29/47 (HOP62, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.40×** | +3.9 | 0.004 | 27/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.39×** | +3.8 | 0.006 | 27/48 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.041 | 29/49 (SNU-423, HT-29, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.45×** | +3.0 | 0.066 | 22/48 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.29×** | +2.9 | 0.098 | 22/48 (NCI-H1573, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4190.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.261×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.754× | -3.1 | 0.50 | 23/48 (NCI-H1573, AsPC-1, …) | top dose only | plate-row cell shift |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.763× | -3.1 | 0.50 | 25/48 (AsPC-1, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4190. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 39.2 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.88× (z +14.0) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H460 (line)]] | wt | 49.3 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.06× (z +11.7) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[PANC-1 (line)]] | alt | 67.0 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.57× (z +13.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.0) | — |
| [[C32 (line)]] | wt | 62.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +8.5) | — |
| [[SW480 (line)]] | alt | 65.8 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +12.2) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[HOP62 (line)]] | alt | 66.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 49.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[KATO III (line)]] | alt | 79.4 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.59× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H1573 (line)]] | alt | 52.1 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.00× (z +9.9) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H23 (line)]] | alt | 53.9 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +8.9) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A-427 (line)]] | wt | 41.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[AsPC-1 (line)]] | alt | 101 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +10.1) | — |
| [[J82 (line)]] | alt | 93.4 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.19× (z +8.6) ⚠ toxic | — |
| [[LOX-IMVI (line)]] | wt | 125 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +8.9) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[LS 180 (line)]] | wt | 62.1 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.69× (z +9.4) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 53.4 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 55.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[NCI-H2030 (line)]] | alt | 105 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.15× (z +9.5) ⚠ toxic | — |
| [[SNU-1 (line)]] | wt | 66.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 50.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | — |
| [[SW 900 (line)]] | alt | 64.5 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.51× (z +8.9) ⚠ toxic | — |
| [[A-172 (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 72.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 69.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 145 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 62.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 172 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 94.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4190), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNIH4]] | +0.62 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[RSRP1]] | +0.60 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[TXNDC16]] | +0.59 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[ATXN3]] | +0.59 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[PPOX]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[PCMTD1]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[PNISR]] | +0.57 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[SNHG19]] | +0.57 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[RHEBL1]] | +0.57 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[SNHG9]] | +0.56 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[CCS]] | +0.56 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[AAMDC]] | +0.56 | +0.47 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STIP1]] | -0.59 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[LSG1]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | -0.56 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[NUDC]] | -0.55 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[CCT5]] | -0.55 | -0.38 / -0.62 | both halves | 7e-05 |  |
| [[EIF2S1]] | -0.55 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[PSMD1]] | -0.54 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[PTPN11]] | -0.54 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[EIF3I]] | -0.54 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[SMARCA4]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[SLC35F6]] | -0.53 | -0.38 / -0.59 | both halves | 7e-05 |  |
| [[PURB]] | -0.53 | -0.41 / -0.54 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YTHDC1]] | C | YTHDC1's natural level weakens ENY2's drug response | YTHDC1's natural level across 50 lines (lineage-adjusted; a glimpse) | r -0.69, reverse +0.21; direction not clear | 0.011 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.508). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.4, -40.8); signed map (-10.4, 8.6). **Vector** length 81.7, 26.1% of its response variance represented; |z| ≥ 3 in 809 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +4.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.0 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.5 | -1.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.8 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -0.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | +0.8 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | ENY2 transcription and export complex 2 subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q23.1 — chr8:109,334,324-109,345,954 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DC6, FLJ20480, Sus1 |
| Gene groups (HGNC) | SAGA complex; Transcription and export complex 2 |
| Reactome | 3 pathways, smallest: HATs acetylate histones; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPA8](https://www.uniprot.org/uniprotkb/Q9NPA8) (Transcription and mRNA export factor ENY2):

> Involved in mRNA export coupled transcription activation by association with both the TREX-2 and the SAGA complexes. The transcription regulatory histone acetylation (HAT) complex SAGA is a multiprotein complex that activates transcription by remodeling chromatin and mediating histone acetylation and deubiquitination. Within the SAGA complex, participates in a subcomplex that specifically deubiquitinates both histones H2A and H2B. The SAGA complex is recruited to specific gene promoters by …

**Summary**, from NCBI Gene [56943](https://www.ncbi.nlm.nih.gov/gene/56943):

> Enables transcription coactivator activity. Involved in poly(A)+ mRNA export from nucleus; positive regulation of DNA-templated transcription; and regulation of transcription by RNA polymerase II. Part of SAGA complex and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24449](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24449) · Entrez [56943](https://www.ncbi.nlm.nih.gov/gene/56943) · UniProt [Q9NPA8](https://www.uniprot.org/uniprotkb/Q9NPA8) · Ensembl [ENSG00000120533](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120533)

## Data

Gene col 4190: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4190); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4190, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4190]; `tensor/DDL_lfc|DDL_z.npy` [4190]; `embed/gene_vectors.npy` [4190]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4190 or target_col == 4190). Every well: [[ENY2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENY2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
