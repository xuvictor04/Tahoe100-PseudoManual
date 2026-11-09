---
symbol: "TUSC2"
type: "gene"
col: 3546
ensembl_id: "ENSG00000114383"
name: "tumor suppressor 2, mitochondrial calcium regulator"
location: "3p21.31"
module: 3
arm: "+"
pooled_cpm: 7.61
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# TUSC2

*tumor suppressor 2, mitochondrial calcium regulator* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.40× (z +12.1, q 1e-30, up in 45 of 46 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.32× (z +11.7, q 3e-29, up in 40 of 42 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (A-172 0.0837×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.162×; ⚠ cell-cycle shift, explains ~57% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP1S1]] (+0.73, fdr 7e-06), [[MPG]] (+0.71, fdr 1e-05), [[TRAPPC1]] (+0.68, fdr 1e-05); moves opposite to [[YWHAE]] (-0.63, fdr 3e-05), [[SRSF10]] (-0.61, fdr 3e-05), [[POGLUT1]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3546.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **3.40×** | +12.1 | 1e-30 | 45/46 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.32×** | +11.7 | 3e-29 | 40/42 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **3.22×** | +11.5 | 2e-28 | 46/47 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.88×** | +10.4 | 4e-23 | 45/47 (SW480, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.44×** | +8.5 | 3e-15 | 28/36 (SW480, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **2.38×** | +8.2 | 2e-14 | 8/12 (SW480, J82, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **2.27×** | +8.1 | 5e-14 | 25/31 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.02×** | +6.4 | 1e-08 | 18/22 (LS 180, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.86×** | +6.1 | 6e-08 | 27/43 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.84×** | +6.0 | 1e-07 | 23/37 (A-172, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.8 | 3e-07 | 22/48 (SW1417, A549, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.75×** | +5.3 | 5e-06 | 23/40 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +4.8 | 6e-05 | 21/46 (SW480, NCI-H2030, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.53×** | +4.2 | 0.001 | 18/42 (SW480, LS 180, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.55×** | +4.1 | 0.001 | 21/42 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.021 | 11/45 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.030 | 16/46 (A-427, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.69×** | +3.2 | 0.042 | 3/42 (J82, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.052 | 10/47 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Arbutin (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.071 | 7/44 (HS-578T, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3546.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (A-172 0.0837×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.162×; ⚠ cell-cycle shift, explains ~57% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.803× | -3.0 | 0.59 | 19/41 (NCI-H2347, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Rifaximin (drug)]] 5 µM |  | 0.726× | -3.0 | 0.59 | 9/46 (RKO, NCI-H2030, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.67 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3546. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.75 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.99× (z +10.0) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 5.74 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0837× (z -9.5) |
| [[A-427 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -8.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H460 (line)]] | wt | 4.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +8.8) | — |
| [[A498 (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3546), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP1S1]] | +0.73 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[MPG]] | +0.71 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[TRAPPC1]] | +0.68 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[MRPL55]] | +0.67 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[ZNHIT1]] | +0.67 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[SAP130]] | +0.66 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[ZCCHC17]] | +0.66 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[MRPS12]] | +0.66 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[CIAO2B]] | +0.65 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.65 | +0.39 / +0.66 | both halves | 5e-05 |  |
| [[TNPO3]] | +0.64 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[IGSF8]] | +0.64 | +0.43 / +0.65 | both halves | 3e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAE]] | -0.63 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[SRSF10]] | -0.61 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[POGLUT1]] | -0.60 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[DZIP3]] | -0.59 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[TIA1]] | -0.59 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ACADM]] | -0.59 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[GABPB2]] | -0.59 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[SRSF3]] | -0.59 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[ANKRD18A]] | -0.58 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[NEK9]] | -0.58 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[HNRNPK]] | -0.58 | -0.28 / -0.55 | both halves | 3e-04 |  |
| [[ZNF280D]] | -0.57 | -0.36 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TUSC2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.665). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-12.8, -7.3); signed map (-41.2, 6.2). **Vector** length 56.0, 9.08% of its response variance represented; |z| ≥ 3 in 822 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +11.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +2.5 | +10.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.5 | +12.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +2.4 | +11.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.3 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.2 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.0 | +2.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.0 | +3.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -1.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.4 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -3.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.0 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | tumor suppressor 2, mitochondrial calcium regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:50,320,027-50,328,251 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FUS1, PAP, C3orf11; previously PDAP2 |
| Matched by | ensembl_id |

**Function**, from UniProt [O75896](https://www.uniprot.org/uniprotkb/O75896) (Tumor suppressor candidate 2):

> May function as a tumor suppressor, inhibiting colony formation, causing G1 arrest and ultimately inducing apoptosis in homozygous 3p21.3 120-kb region-deficient cells.

**Summary**, from NCBI Gene [11334](https://www.ncbi.nlm.nih.gov/gene/11334):

> Predicted to be involved in inflammatory response and regulation of mitochondrial membrane potential. Predicted to act upstream of or within several processes, including natural killer cell differentiation; neutrophil-mediated killing of gram-negative bacterium; and regulation of cytokine production. Predicted to be active in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17034](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17034) · Entrez [11334](https://www.ncbi.nlm.nih.gov/gene/11334) · UniProt [O75896](https://www.uniprot.org/uniprotkb/O75896) · Ensembl [ENSG00000114383](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114383)

## Data

Gene col 3546: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3546); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3546, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3546]; `tensor/DDL_lfc|DDL_z.npy` [3546]; `embed/gene_vectors.npy` [3546]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3546 or target_col == 3546). Every well: [[TUSC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUSC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
