---
symbol: "SNF8"
type: "gene"
col: 8230
ensembl_id: "ENSG00000159210"
name: "SNF8 subunit of ESCRT-II"
location: "17q21.32"
module: 52
arm: "+"
pooled_cpm: 28.32
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# SNF8

*SNF8 subunit of ESCRT-II* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.59× (z +24.4, q 0e+00, up in 43 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.55× (z +7.0, q 2e-10, up in 30 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM in 1 line (SNU-1 0.106×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASCC2]] (+0.61, fdr 1e-05), [[NCBP1]] (+0.59, fdr 2e-05), [[FAM114A2]] (+0.59, fdr 2e-05); moves opposite to [[HIGD2A]] (-0.50, fdr 1e-04), [[GATA2]] (-0.50, fdr 2e-04), [[RPL15]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8230.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.59×** | +24.4 | 0e+00 | 43/43 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.12×** | +17.5 | 0e+00 | 34/37 (PANC-1, SW480, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.18×** | +17.1 | 0e+00 | 37/40 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.70×** | +8.5 | 2e-15 | 41/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.43×** | +8.2 | 3e-14 | 35/47 (A549, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +7.5 | 5e-12 | 37/45 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +7.0 | 2e-10 | 30/47 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +6.9 | 3e-10 | 35/47 (SW480, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.47×** | +6.1 | 5e-08 | 32/48 (LoVo, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.44×** | +5.9 | 3e-07 | 30/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.43×** | +5.5 | 2e-06 | 24/48 (NCI-H23, HOP62, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.37×** | +5.1 | 2e-05 | 25/46 (NCI-H1792, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.34×** | +4.7 | 1e-04 | 25/47 (COLO 205, C32, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.72×** | +3.9 | 0.004 | 16/47 (NCI-H23, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.58×** | +3.8 | 0.005 | 14/47 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.006 | 15/47 (A-427, A549, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.65×** | +3.6 | 0.010 | 15/46 (SK-MEL-2, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.024 | 17/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM in 1 line (SNU-1 0.106×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8230. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 21.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.50× (z +15.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 43.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +16.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 31.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.62× (z +13.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 24.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.35× (z +12.3) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 30.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.19× (z +14.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 21.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.22× (z +15.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 20.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.96× (z +15.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 20.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +13.0) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 19.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.00× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 21.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.74× (z +12.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 22.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.42× (z +13.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 28.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +11.3) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 25.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +15.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 50.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +19.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 17.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.03× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 22.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +16.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 43.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.47× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HS-578T (line)]] | alt | 23.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +10.2) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 28.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.82× (z +13.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 29.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +11.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 31.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +14.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 34.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.37× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[C-33 A (line)]] | alt | 22.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +9.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 17.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 24.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 20.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.39× (z +9.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 17.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 18.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +9.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 29.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +10.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 21.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 30.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 36.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +12.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 25.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM 0.106× (z -11.6) |
| [[SW 900 (line)]] | alt | 23.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 25.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 17.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +8.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8230), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASCC2]] | +0.61 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NCBP1]] | +0.59 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[FAM114A2]] | +0.59 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[NELFE]] | +0.58 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[MRPL47]] | +0.58 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[ARPC4]] | +0.57 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[AP1B1]] | +0.55 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[DBNL]] | +0.54 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[API5]] | +0.54 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[EDC3]] | +0.54 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[DNAL1]] | +0.54 | +0.31 / +0.55 | both halves | 2e-04 |  |
| [[RTF2]] | +0.52 | +0.31 / +0.54 | both halves | 2e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIGD2A]] | -0.50 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[GATA2]] | -0.50 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[RPL15]] | -0.49 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[SLC25A5]] | -0.49 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[TMEM41A]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ZFAS1]] | -0.48 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[RPS15]] ⚠ | -0.48 | -0.31 / -0.55 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS8]] | -0.47 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[RPS23]] | -0.47 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[RPL13A]] | -0.46 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[RPL7A]] | -0.46 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[RPS13]] ⚠ | -0.46 | -0.34 / -0.52 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS11]] | -0.45 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[AMD1]] | -0.45 | -0.45 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.331). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-33.1, -16.0); signed map (-3.4, -33.3). **Vector** length 55.3, 9.25% of its response variance represented; |z| ≥ 3 in 728 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +24.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +17.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +3.0 | +17.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +2.6 | +3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +2.1 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +6.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +1.2 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.1 | +2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.1 | +2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +0.8 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -1.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.1 | +2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.0 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | SNF8 subunit of ESCRT-II |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:48,929,316-48,944,842 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EAP30, VPS22, Dot3 |
| Gene groups (HGNC) | ESCRT-II |
| Reactome | 6 pathways, smallest: Endosomal Sorting Complex Required For Transport (ESCRT); HCMV Late Events; HCMV Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96H20](https://www.uniprot.org/uniprotkb/Q96H20) (Vacuolar-sorting protein SNF8):

> Component of the endosomal sorting complex required for transport II (ESCRT-II), which is required for multivesicular body (MVB) formation and sorting of endosomal cargo proteins into MVBs, and plays a role in autophagy. The MVB pathway mediates delivery of transmembrane proteins into the lumen of the lysosome for degradation. The ESCRT-II complex is probably involved in the recruitment of the ESCRT-III complex. The ESCRT-II complex may also play a role in transcription regulation by …

**Summary**, from NCBI Gene [11267](https://www.ncbi.nlm.nih.gov/gene/11267):

> The protein encoded by this gene is a component of the endosomal sorting complex required for transport II (ESCRT-II), which regulates the movement of ubiquitinylated transmembrane proteins to the lysosome for degradation. This complex also interacts with the RNA polymerase II elongation factor (ELL) to overcome the repressive effects of ELL on RNA polymerase II activity. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:17028](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17028) · Entrez [11267](https://www.ncbi.nlm.nih.gov/gene/11267) · UniProt [Q96H20](https://www.uniprot.org/uniprotkb/Q96H20) · Ensembl [ENSG00000159210](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159210)

## Data

Gene col 8230: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8230); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8230, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8230]; `tensor/DDL_lfc|DDL_z.npy` [8230]; `embed/gene_vectors.npy` [8230]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8230 or target_col == 8230). Every well: [[SNF8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNF8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
