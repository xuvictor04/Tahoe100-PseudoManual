---
symbol: "PPIL4"
type: "gene"
col: 5155
ensembl_id: "ENSG00000131013"
name: "peptidylprolyl isomerase like 4"
location: "6q25.1"
module: 41
arm: "+"
pooled_cpm: 109.47
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# PPIL4

*peptidylprolyl isomerase like 4* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.83× (z +17.0, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.786× (z -6.7, q 1e-08, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (KATO III 0.228×, AN3 CA 0.274×, CFPAC-1 0.455×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H2347 0.473×, LOX-IMVI 0.481×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 0.620×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UFL1]] (+0.81, fdr 7e-06), [[VIRMA]] (+0.77, fdr 7e-06), [[CIR1]] (+0.77, fdr 7e-06); moves opposite to [[TTL]] (-0.67, fdr 7e-06), [[GATAD2A]] (-0.62, fdr 7e-06), [[EIF5A]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5155.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +17.0 | 0e+00 | 44/48 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +13.5 | 6e-39 | 44/48 (LOX-IMVI, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.74×** | +10.6 | 3e-24 | 44/49 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +8.4 | 7e-15 | 42/48 (LOX-IMVI, A-427, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.99×** | +7.3 | 4e-11 | 34/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.30×** | +5.0 | 5e-05 | 27/48 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.28×** | +5.0 | 5e-05 | 28/48 (LoVo, NCI-H1573, …) | top dose only | composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.5 | 0.032 | 20/48 (SW480, PANC-1, …) | two highest doses |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.13× | +3.4 | 0.039 | 10/48 (HT-29, SNU-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.048 | 20/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +3.3 | 0.048 | 22/48 (LoVo, SNU-1, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 1.12× | +3.2 | 0.061 | 2/49 (C-33 A, H4) | top dose only |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.17× | +3.0 | 0.12 | 10/48 (NCI-H2030, NCI-H23, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5155.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (KATO III 0.228×, AN3 CA 0.274×, CFPAC-1 0.455×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H2347 0.473×, LOX-IMVI 0.481×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change); [[Tucidinostat (drug)]] 5 µM in 1 line (SW480 0.620×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.786×** | -6.7 | 1e-08 | 34/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.823×** | -5.4 | 2e-05 | 20/48 (A498, A-172, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.850× | -3.3 | 0.13 | 17/49 (NCI-H2347, H4, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -3.2 | 0.13 | 17/48 (SW1417, NCI-H2347, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change | 0.848× | -3.2 | 0.13 | 18/44 (NCI-H2347, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.853× | -3.2 | 0.13 | 15/48 (NCI-H2347, SW 900, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change | 0.846× | -3.1 | 0.15 | 21/45 (KATO III, AN3 CA, …) | all doses, flat | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5155. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 132 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +19.6) | [[Dinaciclib (drug)]] 5 µM 0.481× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change |
| [[SW480 (line)]] | alt | 161 | 4 | 1 | [[TAK-901 (drug)]] 5 µM 4.61× (z +12.3) | [[Tucidinostat (drug)]] 5 µM 0.620× (z -10.2) |
| [[LoVo (line)]] | wt | 97.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +14.5) | — |
| [[RKO (line)]] | wt | 127 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.91× (z +12.5) | — |
| [[A-427 (line)]] | wt | 98.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.9) | — |
| [[HEC-1-A (line)]] | alt | 101 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +15.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 123 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.35× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 71.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +16.0) | — |
| [[NCI-H460 (line)]] | wt | 77.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.9) | — |
| [[C32 (line)]] | wt | 95.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +11.0) | — |
| [[KATO III (line)]] | alt | 38.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change |
| [[NCI-H1792 (line)]] | alt | 117 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.1) | — |
| [[NCI-H2030 (line)]] | alt | 133 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 204 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +16.1) | — |
| [[PANC-1 (line)]] | alt | 91.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.1) | — |
| [[RPMI-7951 (line)]] | alt | 155 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +12.5) | — |
| [[SK-MEL-2 (line)]] | alt | 85.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +18.2) | — |
| [[SW48 (line)]] | wt | 104 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +11.1) | — |
| [[A-172 (line)]] | wt | 92.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.6) | — |
| [[A498 (line)]] | wt | 117 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -9.3) ⚠ cell-cycle shift, explains ~55% of this change |
| [[A549 (line)]] | wt | 91.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.2) | — |
| [[AN3 CA (line)]] | alt | 160 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.274× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change |
| [[AsPC-1 (line)]] | alt | 122 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 88.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.455× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~6% of this change |
| [[COLO 205 (line)]] | alt | 61.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.53× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 141 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.5) | — |
| [[HepG2_C3A (line)]] | wt | 159 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 119 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.1) | — |
| [[Hs 766T (line)]] | wt | 111 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 124 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 86.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.9) | — |
| [[hTERT-HPNE (line)]] | wt | 138 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 115 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 96.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.473× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change |
| [[Panc 03.27 (line)]] | alt | 93.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.196× (z -9.9) ⚠ toxic |
| [[SW 900 (line)]] | alt | 132 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 87.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 117 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5155), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UFL1]] | +0.81 | +0.82 / +0.68 | both halves | 7e-06 |  |
| [[VIRMA]] | +0.77 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[CIR1]] | +0.77 | +0.81 / +0.70 | both halves | 7e-06 |  |
| [[ERCC5]] | +0.76 | +0.79 / +0.65 | both halves | 7e-06 |  |
| [[TRIM23]] | +0.75 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[TMF1]] | +0.73 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[AKAP9]] | +0.72 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[IK]] | +0.70 | +0.72 / +0.68 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[SF3B2]] | +0.70 | +0.80 / +0.56 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 481 |
| [[SLC4A1AP]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[ZRSR2]] | +0.69 | +0.71 / +0.59 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[CCDC174]] | +0.68 | +0.73 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTL]] | -0.67 | -0.65 / -0.65 | both halves | 7e-06 |  |
| [[GATAD2A]] | -0.62 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[EIF5A]] | -0.62 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[LRP8]] | -0.61 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[HNRNPAB]] | -0.57 | -0.57 / -0.52 | both halves | 1e-05 | same gene group |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.775). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-3.2, -48.8); signed map (-13.9, -10.0). **Vector** length 115, 35.0% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +17.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.9 | +13.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | +3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | -0.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.3 | +3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +1.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.0 | +0.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.7 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.8 | +1.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.5 | +1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.3 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -5.9 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | +1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.5 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -0.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | peptidylprolyl isomerase like 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:149,504,495-149,546,043 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RNA binding motif containing; Cyclophilin peptidylprolyl isomerases |
| Reactome | 7 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Dengue Virus-Host Interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUA2](https://www.uniprot.org/uniprotkb/Q8WUA2) (Peptidyl-prolyl cis-trans isomerase-like 4):

> PPIases accelerate the folding of proteins. It catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides (By similarity).

**Summary**, from NCBI Gene [85313](https://www.ncbi.nlm.nih.gov/gene/85313):

> This gene is a member of the cyclophilin family of peptidylprolyl isomerases. The cyclophilins are a highly conserved family, members of which play an important role in protein folding, immunosuppression by cyclosporin A, and infection of HIV-1 virions. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15702](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15702) · Entrez [85313](https://www.ncbi.nlm.nih.gov/gene/85313) · UniProt [Q8WUA2](https://www.uniprot.org/uniprotkb/Q8WUA2) · Ensembl [ENSG00000131013](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131013)

## Data

Gene col 5155: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5155); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5155, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5155]; `tensor/DDL_lfc|DDL_z.npy` [5155]; `embed/gene_vectors.npy` [5155]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5155 or target_col == 5155). Every well: [[PPIL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPIL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
