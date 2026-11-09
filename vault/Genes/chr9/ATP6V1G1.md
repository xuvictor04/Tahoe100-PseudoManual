---
symbol: "ATP6V1G1"
type: "gene"
col: 5932
ensembl_id: "ENSG00000136888"
name: "ATPase H+ transporting V1 subunit G1"
location: "9q32"
module: 6
arm: "-"
pooled_cpm: 53.53
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# ATP6V1G1

*ATPase H+ transporting V1 subunit G1* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.42× (z +11.7, q 9e-29, up in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +9.6, q 1e-19, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Citalopram (hydrobromide) (drug)]] 0.05 µM in 1 line (NCI-H596 1.05×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V1E1]] (+0.74, fdr 7e-06), [[TSC1]] (+0.67, fdr 7e-06), [[ATP6V1C1]] (+0.65, fdr 1e-05); moves opposite to [[CDCA7]] (-0.69, fdr 7e-06), [[CDC7]] (-0.67, fdr 7e-06), [[DSCC1]] (-0.65, fdr 7e-06).
> It sits in the **-** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 19 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5932.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.42×** | +11.7 | 9e-29 | 47/49 (SW480, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.85×** | +11.3 | 3e-27 | 40/41 (SW480, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.66×** | +10.2 | 5e-22 | 42/45 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +9.6 | 1e-19 | 46/48 (KATO III, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.25×** | +9.1 | 8e-18 | 44/48 (BT-474, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.74×** | +8.8 | 1e-16 | 37/47 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.74×** | +6.3 | 3e-08 | 44/48 (RKO, SHP-77, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.71×** | +6.0 | 1e-07 | 42/48 (NCI-H460, NCI-H1573, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +6.0 | 1e-07 | 41/47 (HepG2/C3A, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.68×** | +5.6 | 1e-06 | 33/48 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.64×** | +5.6 | 1e-06 | 39/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.64×** | +5.6 | 1e-06 | 38/48 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +4.8 | 8e-05 | 39/48 (A498, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +4.8 | 8e-05 | 40/48 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.56×** | +4.7 | 8e-05 | 36/48 (LOX-IMVI, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.1 | 1e-03 | 31/49 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.034 | 24/48 (SW48, hTERT-HPNE, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.32×** | +2.9 | 0.085 | 22/48 (NCI-H460, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5932.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Citalopram (hydrobromide) (drug)]] 0.05 µM in 1 line (NCI-H596 1.05×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.747× | -3.3 | 0.61 | 29/48 (A498, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5932. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 56.9 | 9 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +16.0) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 3.35× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 33.9 | 7 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +13.2) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[J82 (line)]] | alt | 74.2 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +13.2) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 31.8 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 61.6 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +10.2) | — |
| [[SW480 (line)]] | alt | 50.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.03× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +8.7) | — |
| [[A-172 (line)]] | wt | 49.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.0) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.11× (z +9.2) | — |
| [[A498 (line)]] | wt | 87.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.90× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 37.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.58× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 31.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.53× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.06× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 48.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.56× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H23 (line)]] | alt | 47.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.2) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.27× (z +8.7) | — |
| [[A-427 (line)]] | wt | 37.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.16× (z +9.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 53.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.57× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 32.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.40× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 60.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.92× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 82.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +13.5) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.15× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 61.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.0) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[BT-474 (line)]] | alt | 70.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.41× (z +11.9) | — |
| [[C32 (line)]] | wt | 57.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.97× (z +9.3) | — |
| [[COLO 205 (line)]] | alt | 73.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +12.9) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[HCT15 (line)]] | alt | 55.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.40× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[Hs 766T (line)]] | wt | 85.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +12.6) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[KATO III (line)]] | alt | 74.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 50.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H1792 (line)]] | alt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H2347 (line)]] | alt | 51.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 47.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +8.8) | — |
| [[RKO (line)]] | wt | 68.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.05× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 61.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.88× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[SW 900 (line)]] | alt | 74.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[AN3 CA (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 67.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5932), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1E1]] | +0.74 | +0.65 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[TSC1]] | +0.67 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ATP6V1C1]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 998 |
| [[CELF6]] | +0.65 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[AP5Z1]] | +0.64 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[DAZAP2]] | +0.63 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[RRAGC-DT]] | +0.62 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[RNASEK]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 | STRING 987 |
| [[WASHC2C]] | +0.61 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[HPS1]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[SYNRG]] | +0.60 | +0.74 / +0.44 | both halves | 3e-05 |  |
| [[HEXA]] | +0.60 | +0.42 / +0.59 | both halves | 4e-05 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDCA7]] | -0.69 | -0.69 / -0.66 | both halves | 7e-06 |  |
| [[CDC7]] | -0.67 | -0.59 / -0.69 | both halves | 7e-06 |  |
| [[DSCC1]] | -0.65 | -0.69 / -0.59 | both halves | 7e-06 |  |
| [[MSH5]] | -0.64 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[UBE2T]] | -0.63 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[RFC4]] | -0.63 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[BLM]] | -0.62 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[BRI3BP]] | -0.61 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[CCDC150]] | -0.61 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[FANCB]] | -0.61 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[RRM2]] | -0.61 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[CEP78]] | -0.61 | -0.54 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **-** arm (projection on the module's main direction -0.609). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-32.1, -42.0); signed map (-1.6, -5.8). **Vector** length 68.8, 19.9% of its response variance represented; |z| ≥ 3 in 912 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.7 | +9.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.2 | +4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +2.9 | +8.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +9.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.2 | -1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +0.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +0.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.0 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -2.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | +0.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -2.3 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -1.9 | +4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -0.3 |
|  | [[vincristine (drug)]] 5 µM |  | -1.4 | +1.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.3 | +1.2 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.3 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting V1 subunit G1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:114,587,706-114,598,915 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATP6GL, Vma10, ATP6G, DKFZp547P234; previously ATP6J, ATP6G1 |
| Gene groups (HGNC) | V-type ATPase subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 16 pathways, smallest: Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy; Insulin receptor recycling; ROS and RNS production in phagocytes |
| Matched by | ensembl_id |

**Function**, from UniProt [O75348](https://www.uniprot.org/uniprotkb/O75348) (V-type proton ATPase subunit G 1):

> Subunit of the V1 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons. V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it promotes acidification of the extracellular environment. The V-ATPase complex also acts as an activator for mTORC1 on lysosomal …

**Summary**, from NCBI Gene [9550](https://www.ncbi.nlm.nih.gov/gene/9550):

> This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of eukaryotic intracellular organelles. V-ATPase dependent organelle acidification is necessary for such intracellular processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. V-ATPase is composed of a cytosolic V1 domain and a transmembrane V0 domain. The V1 domain consists of three A, three B, and two G …

**Accessions** — [HGNC:864](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:864) · Entrez [9550](https://www.ncbi.nlm.nih.gov/gene/9550) · UniProt [O75348](https://www.uniprot.org/uniprotkb/O75348) · Ensembl [ENSG00000136888](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136888)

## Data

Gene col 5932: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5932); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5932, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5932]; `tensor/DDL_lfc|DDL_z.npy` [5932]; `embed/gene_vectors.npy` [5932]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5932 or target_col == 5932). Every well: [[ATP6V1G1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V1G1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
