---
symbol: "SIVA1"
type: "gene"
col: 11603
ensembl_id: "ENSG00000184990"
name: "SIVA1 apoptosis inducing factor"
location: "14q32.33"
module: 3
arm: "+"
pooled_cpm: 24.68
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SIVA1

*SIVA1 apoptosis inducing factor* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.42× (z +6.5, q 5e-08, up in 37 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 5.70×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW480 4.18×; ⚠ toxic).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.555× (z -6.2, q 3e-07, down in 38 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.168×, HOP62 0.284×, SW480 0.307×, J82 0.348×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.0803×; ⚠ cell-cycle shift, would explain all of this change); [[Neratinib (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.132×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANAPC11]] (+0.79, fdr 7e-06), [[NUBP2]] (+0.72, fdr 1e-05), [[GLRX5]] (+0.72, fdr 1e-05); moves opposite to [[EIF4G2]] (-0.71, fdr 1e-05), [[ZNF300]] (-0.67, fdr 2e-05), [[HNRNPK]] (-0.64, fdr 2e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11603.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 5.70×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW480 4.18×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **2.42×** | +6.5 | 5e-08 | 37/41 (A549, HCT15, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.88×** | +4.6 | 7e-04 | 25/35 (Panc 03.27, A-172, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.83×** | +4.6 | 7e-04 | 38/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +4.6 | 7e-04 | 31/44 (SW480, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.79×** | +4.4 | 0.001 | 32/45 (Panc 03.27, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.79×** | +4.4 | 0.001 | 36/48 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.70×** | +4.0 | 0.005 | 32/48 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.88×** | +4.0 | 0.005 | 24/38 (CFPAC-1, LOX-IMVI, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **1.52×** | +3.2 | 0.099 | 26/46 (SHP-77, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | 1.51× | +3.1 | 0.11 | 26/47 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11603.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.168×, HOP62 0.284×, SW480 0.307×, J82 0.348×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.0803×; ⚠ cell-cycle shift, would explain all of this change); [[Neratinib (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.132×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.555×** | -6.2 | 3e-07 | 38/47 (A-427, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.743× | -3.1 | 0.50 | 22/48 (SNU-1, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11603. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 44.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -13.1) |
| [[SW480 (line)]] | alt | 31.1 | 1 (1 ⚠) | 1 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.18× (z +9.0) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -10.6) |
| [[COLO 205 (line)]] | alt | 9.08 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0498× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 31.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 25.0 | 0 | 1 | — | [[Neratinib (drug)]] 0.05 µM 0.132× (z -10.2) |
| [[J82 (line)]] | alt | 40.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 33.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.70× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[RKO (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0803× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11603), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC11]] | +0.79 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[NUBP2]] | +0.72 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[GLRX5]] | +0.72 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SDHAP2]] | +0.70 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[COX14]] | +0.70 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[SDHAP1]] | +0.68 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[SPSB3]] | +0.68 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SMYD4]] | +0.68 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[LCMT1]] | +0.67 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[LSM2]] | +0.67 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[MRPL41]] ⚠ | +0.67 | +0.41 / +0.62 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MIGA2]] | +0.67 | +0.37 / +0.61 | both halves | 9e-05 |  |
| [[MPG]] | +0.66 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.71 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[ZNF300]] | -0.67 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[HNRNPK]] | -0.64 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[ZXDA]] | -0.63 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[RNF6]] | -0.61 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[ZSCAN30]] | -0.61 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[YWHAE]] | -0.61 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[KRT8P12]] | -0.61 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[ZXDB]] | -0.60 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[HNRNPU]] | -0.60 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[MMADHC-DT]] | -0.60 | -0.58 / -0.26 | both halves | 4e-04 |  |
| [[RIPK2-DT]] | -0.60 | -0.53 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SIVA1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.702). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-0.0, -16.3); signed map (-36.5, 4.1). **Vector** length 80.3, 23.7% of its response variance represented; |z| ≥ 3 in 564 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +5.0 | +4.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +4.8 | +4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.4 | +4.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.1 | +3.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.9 | +1.4 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +1.4 | +1.3 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.2 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.9 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.1 | +0.6 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.1 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | -3.6 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | +0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | SIVA1 apoptosis inducing factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:104,753,147-104,768,494 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SIVA, Siva-1, Siva-2, CD27BP |
| Matched by | ensembl_id |

**Function**, from UniProt [O15304](https://www.uniprot.org/uniprotkb/O15304) (Apoptosis regulatory protein Siva):

> Induces CD27-mediated apoptosis. Inhibits BCL2L1 isoform Bcl-x(L) anti-apoptotic activity. Inhibits activation of NF-kappa-B and promotes T-cell receptor-mediated apoptosis.

**Summary**, from NCBI Gene [10572](https://www.ncbi.nlm.nih.gov/gene/10572):

> This gene encodes an E3 ubiquitin ligase that regulates cell cycle progression, cell proliferation and apoptosis. The N-terminus of this protein binds to the cytoplasmic tail of the CD27 antigen, a member of the tumor necrosis factor receptor (TNFR) superfamily. In response to UV radiation-induced DNA damage, this protein has been shown to mediate the ubiquitination of proliferating cell nuclear antigen (PCNA), an important step in translesion DNA synthesis. [provided by RefSeq, Sep 2018]

**Accessions** — [HGNC:17712](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17712) · Entrez [10572](https://www.ncbi.nlm.nih.gov/gene/10572) · UniProt [O15304](https://www.uniprot.org/uniprotkb/O15304) · Ensembl [ENSG00000184990](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184990)

## Data

Gene col 11603: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11603); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11603, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11603]; `tensor/DDL_lfc|DDL_z.npy` [11603]; `embed/gene_vectors.npy` [11603]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11603 or target_col == 11603). Every well: [[SIVA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIVA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
