---
symbol: "ARMT1"
type: "gene"
col: 7099
ensembl_id: "ENSG00000146476"
name: "damage control phosphatase 1"
location: "6q25.1"
module: 77
arm: "-"
pooled_cpm: 14.03
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# ARMT1

*damage control phosphatase 1* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.28× (z +19.8, q 0e+00, up in 42 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vandetanib (drug)]] 0.05 µM in 1 line (SW48 0.0530×); [[Bentamapimod (drug)]] 0.05 µM in 1 line (SNU-1 0.0620×); [[Ipatasertib (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0613×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCRN1]] (+0.70, fdr 1e-05), [[RIMOC1]] (+0.68, fdr 1e-05), [[TAF9B]] (+0.68, fdr 1e-05); moves opposite to [[DRD4]] (-0.68, fdr 7e-06), [[PI4KAP2]] (-0.66, fdr 3e-05), [[OGG1]] (-0.64, fdr 1e-05).
> It sits in the **-** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7099.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.28×** | +19.8 | 0e+00 | 42/46 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +14.1 | 2e-42 | 40/46 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.28×** | +14.0 | 3e-42 | 38/45 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.28×** | +13.5 | 4e-39 | 41/45 (SNU-423, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.15×** | +13.0 | 2e-36 | 31/37 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +12.6 | 2e-34 | 26/29 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +8.7 | 4e-16 | 35/47 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +8.6 | 5e-16 | 34/47 (A-172, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +7.3 | 1e-11 | 26/48 (HEC-1-A, A-427, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.50×** | +6.9 | 2e-10 | 30/47 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +6.6 | 3e-09 | 23/48 (J82, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.5 | 4e-09 | 23/45 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +6.0 | 7e-08 | 21/45 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.45×** | +5.8 | 2e-07 | 17/35 (A498, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.39×** | +5.6 | 9e-07 | 23/48 (NCI-H2030, NCI-H460, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +5.3 | 4e-06 | 14/48 (SNU-423, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +4.6 | 1e-04 | 13/47 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.002 | 12/47 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.006 | 15/47 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.013 | 12/47 (SNU-423, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7099.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vandetanib (drug)]] 0.05 µM in 1 line (SW48 0.0530×); [[Bentamapimod (drug)]] 0.05 µM in 1 line (SNU-1 0.0620×); [[Ipatasertib (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0613×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | 0.688× | -3.3 | 0.33 | 15/44 (PANC-1, C32, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Decitabine (drug)]] 5 µM |  | 0.824× | -3.2 | 0.33 | 6/47 (NCI-H460, HepG2/C3A, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.774× | -3.1 | 0.33 | 11/44 (Panc 03.27, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | 0.781× | -3.0 | 0.35 | 12/45 (SNU-1, hTERT-HPNE, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7099. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 13.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +11.7) | — |
| [[A498 (line)]] | wt | 15.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +13.0) | — |
| [[HEC-1-A (line)]] | alt | 13.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +11.5) | — |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.04× (z +12.3) | — |
| [[PANC-1 (line)]] | alt | 15.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +11.4) | — |
| [[SNU-423 (line)]] | alt | 20.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.9) | — |
| [[SW480 (line)]] | alt | 19.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +10.6) | — |
| [[A-172 (line)]] | wt | 15.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 9.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +8.5) | — |
| [[J82 (line)]] | alt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +8.6) | — |
| [[KATO III (line)]] | alt | 17.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +9.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 9.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +11.2) | — |
| [[Panc 03.27 (line)]] | alt | 9.75 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0613× (z -9.8) |
| [[SNU-1 (line)]] | wt | 10.8 | 0 | 1 | — | [[Bentamapimod (drug)]] 0.05 µM 0.0620× (z -10.2) |
| [[SW48 (line)]] | wt | 11.2 | 0 | 1 | — | [[Vandetanib (drug)]] 0.05 µM 0.0530× (z -10.4) |
| [[A-427 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7099), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCRN1]] | +0.70 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[RIMOC1]] | +0.68 | +0.72 / +0.57 | both halves | 1e-05 |  |
| [[TAF9B]] | +0.68 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[CFL2]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[RNF6]] | +0.66 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[NCOA4]] | +0.65 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[CILK1]] | +0.65 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[RAP2C]] | +0.65 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ZXDB]] | +0.64 | +0.71 / +0.38 | both halves | 6e-05 |  |
| [[TAF9]] | +0.63 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[LACTB2]] | +0.63 | +0.72 / +0.39 | both halves | 5e-05 |  |
| [[NXT2]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRD4]] | -0.68 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[PI4KAP2]] | -0.66 | -0.68 / -0.46 | both halves | 3e-05 |  |
| [[OGG1]] | -0.64 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[GFOD2]] | -0.63 | -0.57 / -0.58 | both halves | 9e-06 |  |
| [[TMEM120B]] | -0.63 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[TOMM5]] | -0.62 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[NUP160]] | -0.61 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[ST6GALNAC6-1]] | -0.61 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[UQCRH]] | -0.61 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[PI4KAP1]] | -0.60 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[COX6A1]] | -0.59 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[ATAT1]] | -0.59 | -0.70 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ARMT1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **-** arm (projection on the module's main direction -0.633). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-9.5, 1.8); signed map (16.5, -31.1). **Vector** length 69.4, 11.7% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +19.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.9 | +13.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +14.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.3 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.0 | +13.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +3.5 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -3.6 | +5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -3.3 | +4.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.5 | +6.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | -3.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | +0.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.4 | -1.2 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -1.3 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | damage control phosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:151,452,258-151,470,101 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12910; previously C6orf211, ARMT1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H993](https://www.uniprot.org/uniprotkb/Q9H993) (Damage-control phosphatase 1):

> Metal-dependent phosphatase that shows phosphatase activity against several substrates, including fructose-1-phosphate and fructose-6-phosphate. Its preference for fructose-1-phosphate, a strong glycating agent that causes DNA damage rather than a canonical yeast metabolite, suggests a damage-control function in hexose phosphate metabolism. Has also been shown to have O-methyltransferase activity that methylates glutamate residues of target proteins to form gamma-glutamyl methyl ester residues. …

**Summary**, from NCBI Gene [79624](https://www.ncbi.nlm.nih.gov/gene/79624):

> Enables enzyme binding activity; fructose-1-phosphatase activity; and methyltransferase activity. Involved in DNA damage response. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17872](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17872) · Entrez [79624](https://www.ncbi.nlm.nih.gov/gene/79624) · UniProt [Q9H993](https://www.uniprot.org/uniprotkb/Q9H993) · Ensembl [ENSG00000146476](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146476)

## Data

Gene col 7099: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7099); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7099, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7099]; `tensor/DDL_lfc|DDL_z.npy` [7099]; `embed/gene_vectors.npy` [7099]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7099 or target_col == 7099). Every well: [[ARMT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARMT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
