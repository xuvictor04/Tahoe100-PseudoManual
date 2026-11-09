---
symbol: "TTC41P"
type: "gene"
col: 13185
ensembl_id: "ENSG00000214198"
name: "tetratricopeptide repeat domain 41, pseudogene"
location: "12q23.3"
module: 26
arm: "+"
pooled_cpm: 4.29
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# TTC41P

*tetratricopeptide repeat domain 41, pseudogene* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.47× (z +33.7, q 0e+00, up in 33 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (J82 0.0670×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD7-DT]] (+0.66, fdr 7e-06), [[CCNT2-AS1]] (+0.65, fdr 2e-05), [[CCDC90B-AS1]] (+0.65, fdr 1e-05); moves opposite to [[COMMD2]] (-0.61, fdr 2e-05), [[RSAD1]] (-0.59, fdr 1e-04), [[RNF2]] (-0.59, fdr 1e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13185.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.47×** | +33.7 | 0e+00 | 33/34 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.31×** | +14.0 | 5e-42 | 27/37 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.12×** | +13.0 | 3e-36 | 16/29 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.08×** | +12.8 | 2e-35 | 3/8 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.79×** | +12.2 | 6e-32 | 30/45 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.68×** | +11.7 | 2e-29 | 34/44 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.99×** | +11.5 | 1e-28 | 18/45 (HOP62, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.78×** | +11.2 | 3e-27 | 4/9 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.63×** | +11.0 | 2e-26 | 26/37 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +6.8 | 6e-10 | 15/34 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +6.6 | 2e-09 | 7/18 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +6.4 | 1e-08 | 16/42 (A-172, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +5.8 | 3e-07 | 13/31 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +5.4 | 2e-06 | 13/46 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.27×** | +5.1 | 2e-05 | 3/15 (NCI-H23, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +4.2 | 8e-04 | 9/43 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.019 | 7/42 (J82, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.022 | 7/40 (C-33 A, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13185.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (J82 0.0670×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.826× | -3.2 | 0.35 | 9/44 (HS-578T, hTERT-HPNE, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 0.764× | -3.1 | 0.35 | 8/40 (NCI-H1573, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13185. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 5.99 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.15× (z +15.2) | — |
| [[NCI-H460 (line)]] | wt | 3.41 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.03× (z +12.7) | — |
| [[SW480 (line)]] | alt | 3.11 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +15.0) | — |
| [[A-172 (line)]] | wt | 2.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.85× (z +9.3) | — |
| [[A498 (line)]] | wt | 1.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 3.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.17× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 3.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.90× (z +10.5) | — |
| [[HS-578T (line)]] | alt | 3.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.06× (z +9.3) | — |
| [[J82 (line)]] | alt | 3.35 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0670× (z -9.2) |
| [[LS 180 (line)]] | wt | 4.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.20× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 2.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.71× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 4.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +11.4) | — |
| [[SW1417 (line)]] | alt | 2.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.4× (z +11.0) | — |
| [[A-427 (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13185), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD7-DT]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[CCNT2-AS1]] | +0.65 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[CCDC90B-AS1]] | +0.65 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[RBM15-AS1]] | +0.64 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[LRP2BP]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[LINC02608]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[LNP1]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[CTDSPL2-DT]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[SLC23A1]] | +0.63 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[FAM184B]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SYNM-AS1]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[STX17-DT]] | +0.61 | +0.71 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD2]] | -0.61 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[RSAD1]] | -0.59 | -0.57 / -0.32 | both halves | 1e-04 |  |
| [[RNF2]] | -0.59 | -0.62 / -0.35 | both halves | 1e-04 |  |
| [[PET117]] | -0.58 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[ZNF74]] | -0.58 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[GNPTAB]] | -0.58 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ZNF30]] | -0.58 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[ZFAND4]] | -0.57 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[MOCS1]] | -0.57 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[TRIM35]] | -0.56 | -0.54 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TTC41P's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.688). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (12.9, 20.0); signed map (26.3, -1.5). **Vector** length 58.0, 7.68% of its response variance represented; |z| ≥ 3 in 1,186 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +33.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +11.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.0 | +14.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +6.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +0.8 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +1.1 | +0.7 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.1 | -0.1 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.6 | +3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 41, pseudogene |
| Locus type | pseudogene |
| Location | 12q23.3 — chr12:103,843,756-103,915,867 (-) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | GNNP |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

UniProt [Q6P2S7](https://www.uniprot.org/uniprotkb/Q6P2S7) carries no function annotation.

**Summary**, from NCBI Gene [253724](https://www.ncbi.nlm.nih.gov/gene/253724):

> Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:49210](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49210) · Entrez [253724](https://www.ncbi.nlm.nih.gov/gene/253724) · UniProt [Q6P2S7](https://www.uniprot.org/uniprotkb/Q6P2S7) · Ensembl [ENSG00000214198](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214198)

## Data

Gene col 13185: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13185); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13185, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13185]; `tensor/DDL_lfc|DDL_z.npy` [13185]; `embed/gene_vectors.npy` [13185]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13185 or target_col == 13185). Every well: [[TTC41P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC41P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
