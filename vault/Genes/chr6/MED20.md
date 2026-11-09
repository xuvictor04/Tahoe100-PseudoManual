---
symbol: "MED20"
type: "gene"
col: 4556
ensembl_id: "ENSG00000124641"
name: "mediator complex subunit 20"
location: "6p21.1"
module: 17
arm: "+"
pooled_cpm: 7.76
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# MED20

*mediator complex subunit 20* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.01× (z +17.0, q 0e+00, up in 47 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (NCI-H23 0.0651×; ⚠ transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW1417 0.115×; ⚠ toxic; cell-cycle shift, explains ~79% of this change); [[Bimatoprost (drug)]] 0.5 µM in 1 line (SHP-77 0.0797×); [[Canagliflozin (drug)]] 5 µM in 1 line (A498 0.0670×); [[Zileuton (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0509×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF141]] (+0.64, fdr 1e-05), [[SNX11]] (+0.60, fdr 1e-05), [[ZNF18]] (+0.59, fdr 1e-05); moves opposite to [[MAFG]] (-0.51, fdr 2e-04), [[ATP1B3]] (-0.50, fdr 3e-04), [[LRRC69]] (-0.48, fdr 1e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DENND5B]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4556.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.01×** | +17.0 | 0e+00 | 47/47 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.98×** | +16.9 | 0e+00 | 47/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.05×** | +13.7 | 3e-40 | 44/47 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +12.3 | 1e-32 | 34/44 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.20×** | +7.8 | 9e-13 | 19/48 (NCI-H2347, NCI-H2030, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +7.3 | 3e-11 | 22/43 (PANC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +5.8 | 6e-07 | 26/46 (NCI-H2030, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +5.8 | 6e-07 | 22/46 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.47×** | +4.5 | 4e-04 | 10/41 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.3 | 9e-04 | 17/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +4.2 | 0.001 | 17/47 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.85×** | +3.9 | 0.004 | 6/47 (LoVo, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +3.8 | 0.006 | 11/45 (KATO III, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +3.5 | 0.022 | 11/40 (NCI-H460, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.034 | 6/47 (Panc 03.27, NCI-H2347, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.27×** | +2.9 | 0.097 | 8/47 (SW 1271, HEC-1-A, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4556.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (NCI-H23 0.0651×; ⚠ transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW1417 0.115×; ⚠ toxic; cell-cycle shift, explains ~79% of this change); [[Bimatoprost (drug)]] 0.5 µM in 1 line (SHP-77 0.0797×); [[Canagliflozin (drug)]] 5 µM in 1 line (A498 0.0670×); [[Zileuton (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0509×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | 0.748× | -3.6 | 0.19 | 16/46 (SW480, RKO, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 0.761× | -3.4 | 0.21 | 12/31 (HEC-1-A, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | 0.769× | -3.2 | 0.22 | 4/47 (HepG2/C3A, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4556. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.88 | 0 | 2 | — | [[Canagliflozin (drug)]] 5 µM 0.0670× (z -10.1) |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.115× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~79% of this change |
| [[SW480 (line)]] | alt | 9.13 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.31× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 8.17 | 0 | 1 | — | [[Sacubitril_Valsartan (drug)]] 0.05 µM 0.0659× (z -9.1) |
| [[COLO 205 (line)]] | alt | 29.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.47× (z +8.7) | — |
| [[H4 (line)]] | wt | 9.38 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 5 µM 0.153× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 7.37 | 0 | 1 | — | [[Zileuton (drug)]] 0.5 µM 0.0509× (z -10.0) |
| [[HOP62 (line)]] | alt | 6.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 7.29 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0939× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 9.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0651× (z -13.6) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 9.45 | 0 | 1 | — | [[Bimatoprost (drug)]] 0.5 µM 0.0797× (z -10.3) |
| [[SNU-423 (line)]] | alt | 8.48 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.90× (z +8.8) | — |
| [[A-172 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4556), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF141]] | +0.64 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SNX11]] | +0.60 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[ZNF18]] | +0.59 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[FAM114A2]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[HARS2]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[TRAPPC11]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[GEMIN2]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[FAM220A]] | +0.55 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[AAAS]] | +0.55 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ARMC1]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[BBS2]] | +0.54 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[SRP68]] | +0.54 | +0.57 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAFG]] | -0.51 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[ATP1B3]] | -0.50 | -0.50 / -0.29 | both halves | 3e-04 |  |
| [[LRRC69]] | -0.48 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[FKBP11]] | -0.47 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[MIA]] | -0.47 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[CDR2]] | -0.47 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[DCAF4L1]] | -0.46 | -0.23 / -0.43 | both halves | 5e-04 |  |
| [[ACVR1C]] | -0.46 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[CCDC65]] | -0.45 | -0.25 / -0.49 | both halves | 4e-04 |  |
| [[GBX1]] | -0.45 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[DYNLT2B]] | -0.45 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[RPS6KA3]] | -0.45 | -0.43 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DENND5B]] | C | DENND5B activity lowers MED20's level | lines that do not express DENND5B (3) vs lines expressing it (47) | 2.07× higher at baseline in the lines without DENND5B | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC26A11, SLC4A7, USP31; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.496). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-28.6, -0.7); signed map (-23.7, -17.5). **Vector** length 59.5, 8.53% of its response variance represented; |z| ≥ 3 in 1,128 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +2.7 | +5.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.6 | +3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.3 | +16.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +4.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.0 | +7.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.5 | +2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.3 | +3.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.8 | -3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.7 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.7 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -0.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -1.2 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | mediator complex subunit 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:41,905,354-41,921,139 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp586D2223, PRO0213, SRB2; previously TRFP |
| Gene groups (HGNC) | Mediator complex |
| Reactome | 13 pathways, smallest: Transcriptional regulation of white adipocyte differentiation; RSV-host interactions; Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H944](https://www.uniprot.org/uniprotkb/Q9H944) (Mediator of RNA polymerase II transcription subunit 20):

> Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general …

**Summary**, from NCBI Gene [9477](https://www.ncbi.nlm.nih.gov/gene/9477):

> This gene encodes a component of the mediator complex (also known as TRAP, SMCC, DRIP, or ARC), a transcriptional coactivator complex thought to be required for the expression of almost all genes. The mediator complex is recruited by transcriptional activators or nuclear receptors to induce gene expression, by interacting with RNA polymerase II and promoting the formation of a transcriptional pre-initiation complex. A mutation in this gene has been associated with a novel infantile-onset …

**Accessions** — [HGNC:16840](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16840) · Entrez [9477](https://www.ncbi.nlm.nih.gov/gene/9477) · UniProt [Q9H944](https://www.uniprot.org/uniprotkb/Q9H944) · Ensembl [ENSG00000124641](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124641)

## Data

Gene col 4556: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4556); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4556, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4556]; `tensor/DDL_lfc|DDL_z.npy` [4556]; `embed/gene_vectors.npy` [4556]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4556 or target_col == 4556). Every well: [[MED20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MED20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
