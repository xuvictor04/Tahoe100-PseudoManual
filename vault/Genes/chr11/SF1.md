---
symbol: "SF1"
type: "gene"
col: 9591
ensembl_id: "ENSG00000168066"
name: "splicing factor 1"
location: "11q13.1"
module: 3
arm: "-"
pooled_cpm: 122.02
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SF1

*splicing factor 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.04× (z +17.7, q 0e+00, up in 44 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.490×).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EWSR1]] (+0.67, fdr 2e-05), [[HNRNPD]] (+0.65, fdr 3e-05), [[SFPQ]] (+0.64, fdr 4e-05); moves opposite to [[SEC61G]] (-0.60, fdr 1e-04), [[RAB5IF]] (-0.57, fdr 3e-05), [[RNF181]] (-0.55, fdr 4e-04).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9591.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +17.7 | 0e+00 | 44/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.94×** | +11.2 | 8e-27 | 42/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.24×** | +10.8 | 4e-25 | 46/48 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.96×** | +10.0 | 2e-21 | 46/49 (PANC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +8.4 | 5e-15 | 43/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +7.9 | 3e-13 | 37/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +7.3 | 3e-11 | 35/49 (NCI-H460, KATO III, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +6.9 | 4e-10 | 41/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +6.9 | 4e-10 | 38/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +6.0 | 9e-08 | 40/47 (COLO 205, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +5.5 | 1e-06 | 27/44 (NCI-H23, KATO III, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +5.2 | 9e-06 | 27/45 (A-427, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +5.2 | 9e-06 | 31/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.32×** | +4.9 | 3e-05 | 27/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Baicalin (drug)]] 5 µM |  | 1.18× | +4.1 | 0.001 | 12/49 (NCI-H2347, A-427, …) | inconsistent across doses | position effect removed |
| [[crizotinib (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.011 | 26/48 (A-427, SW1417, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9591.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.490×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -3.6 | 0.20 | 0/50 | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.830× | -3.3 | 0.22 | 23/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.834× | -3.2 | 0.22 | 20/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.2 | 0.22 | 20/48 (SW 900, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9591. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 83.7 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +18.7) | — |
| [[PANC-1 (line)]] | alt | 124 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +24.7) | — |
| [[BT-474 (line)]] | alt | 218 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +15.7) | — |
| [[COLO 205 (line)]] | alt | 115 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +21.7) | — |
| [[KATO III (line)]] | alt | 108 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +13.5) | — |
| [[LS 180 (line)]] | wt | 115 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +16.7) | — |
| [[A-427 (line)]] | wt | 125 | 4 (2 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 6.30× (z +12.3) | — |
| [[AsPC-1 (line)]] | alt | 158 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +25.4) | — |
| [[NCI-H1573 (line)]] | alt | 93.1 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 2.99× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 71.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +14.5) | — |
| [[A549 (line)]] | wt | 99.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +13.8) | — |
| [[HEC-1-A (line)]] | alt | 114 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +16.7) | — |
| [[LoVo (line)]] | wt | 96.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +16.0) | — |
| [[SW1417 (line)]] | alt | 198 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +15.0) | — |
| [[SW480 (line)]] | alt | 166 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +12.8) | — |
| [[A-172 (line)]] | wt | 78.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.0) | — |
| [[LOX-IMVI (line)]] | wt | 109 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.76× (z +12.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 136 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.8) | — |
| [[Panc 03.27 (line)]] | alt | 128 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +13.3) | — |
| [[SHP-77 (line)]] | alt | 107 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.9) | — |
| [[SNU-1 (line)]] | wt | 143 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 2.75× (z +9.3) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.490× (z -9.8) |
| [[A498 (line)]] | wt | 87.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.5) | — |
| [[C32 (line)]] | wt | 92.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +12.1) | — |
| [[CFPAC-1 (line)]] | alt | 122 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +12.2) | — |
| [[HepG2_C3A (line)]] | wt | 97.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 146 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 114 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.7) | — |
| [[HT-29 (line)]] | alt | 147 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +13.8) | — |
| [[hTERT-HPNE (line)]] | wt | 98.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.6) | — |
| [[J82 (line)]] | alt | 138 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.44× (z +10.3) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 138 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.76× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 101 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 116 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.5) | — |
| [[SW 900 (line)]] | alt | 140 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +14.6) | — |
| [[SW48 (line)]] | wt | 165 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.30× (z +13.2) | — |
| [[AN3 CA (line)]] | alt | 140 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 125 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 99.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 112 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9591), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EWSR1]] | +0.67 | +0.46 / +0.77 | both halves | 2e-05 | STRING 756 |
| [[HNRNPD]] | +0.65 | +0.44 / +0.73 | both halves | 3e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 543 |
| [[SFPQ]] | +0.64 | +0.41 / +0.70 | both halves | 4e-05 | STRING 723 |
| [[SUGT1P3]] | +0.59 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[NELFCD]] | +0.58 | +0.39 / +0.63 | both halves | 6e-05 |  |
| [[DHX9]] | +0.57 | +0.46 / +0.65 | both halves | 3e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 872 |
| [[PRPF8]] | +0.57 | +0.45 / +0.63 | both halves | 3e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 682 |
| [[SRSF3]] | +0.57 | +0.47 / +0.58 | both halves | 2e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 605 |
| [[SRSF1]] | +0.56 | +0.38 / +0.63 | both halves | 6e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 813 |
| [[HNRNPM]] | +0.56 | +0.49 / +0.61 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 638 |
| [[MATR3]] | +0.56 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[SRRT]] | +0.56 | +0.47 / +0.59 | both halves | 2e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 927 |

## Genes that move opposite

*34 of its nearest partners move opposite, 11 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61G]] | -0.60 | -0.33 / -0.71 | both halves | 1e-04 |  |
| [[RAB5IF]] | -0.57 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[RNF181]] | -0.55 | -0.25 / -0.67 | both halves | 4e-04 |  |
| [[CHCHD1]] | -0.55 | -0.28 / -0.63 | both halves | 3e-04 |  |
| [[POLR2J]] ⚠ | -0.55 | -0.43 / -0.62 | both halves | 3e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; ⚠ in the vector space only through flagged drug-doses |
| [[NUDT22]] | -0.55 | -0.15 / -0.71 | ⚠ one half (not replicated) | 0.001 |  |
| [[TUBA4A]] | -0.53 | -0.32 / -0.55 | both halves | 1e-04 |  |
| [[EMC6]] | -0.53 | -0.19 / -0.60 | ⚠ one half (not replicated) | 8e-04 |  |
| [[C4orf3]] | -0.53 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[TMEM101]] | -0.51 | -0.10 / -0.70 | ⚠ one half (not replicated) | 0.003 |  |
| [[ATP6V1F]] | -0.51 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[ING2]] | -0.50 | -0.16 / -0.62 | ⚠ one half (not replicated) | 0.001 |  |
| [[ATP5MK]] | -0.50 | -0.30 / -0.58 | both halves | 2e-04 |  |
| [[EMSY]] | -0.50 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[ROMO1]] | -0.49 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[NEDD8]] | -0.49 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[ZNHIT1]] | -0.49 | -0.27 / -0.58 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.436). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.7, -25.0); signed map (13.7, -38.7). **Vector** length 86.4, 24.2% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.8 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.6 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.7 | +5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +17.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +10.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.0 | +0.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.7 | -1.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | +2.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | +2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.4 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | +0.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | splicing factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,764,606-64,778,786 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZFM1, ZCCHC25, BBP; previously ZNF162 |
| Gene groups (HGNC) | Zinc fingers CCHC-type; Spliceosomal A complex; Spliceosomal E complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15637](https://www.uniprot.org/uniprotkb/Q15637) (Splicing factor 1):

> Necessary for the ATP-dependent first step of spliceosome assembly. Binds to the intron branch point sequence (BPS) 5'-UACUAAC-3' of the pre-mRNA. May act as transcription repressor.

**Summary**, from NCBI Gene [7536](https://www.ncbi.nlm.nih.gov/gene/7536):

> This gene encodes a nuclear pre-mRNA splicing factor. The encoded protein specifically recognizes the intron branch point sequence at the 3' splice site, together with the large subunit of U2 auxiliary factor (U2AF), and is required for the early stages of spliceosome assembly. It also plays a role in nuclear pre-mRNA retention and transcriptional repression. The encoded protein contains an N-terminal U2AF ligand motif, a central hnRNP K homology motif and quaking 2 region which bind a key …

**Accessions** — [HGNC:12950](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12950) · Entrez [7536](https://www.ncbi.nlm.nih.gov/gene/7536) · UniProt [Q15637](https://www.uniprot.org/uniprotkb/Q15637) · Ensembl [ENSG00000168066](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168066)

## Data

Gene col 9591: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9591); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9591, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9591]; `tensor/DDL_lfc|DDL_z.npy` [9591]; `embed/gene_vectors.npy` [9591]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9591 or target_col == 9591). Every well: [[SF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
