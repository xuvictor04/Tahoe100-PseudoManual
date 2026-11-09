---
symbol: "ARNT"
type: "gene"
col: 6744
ensembl_id: "ENSG00000143437"
name: "aryl hydrocarbon receptor nuclear translocator"
location: "1q21.3"
module: 65
arm: "+"
pooled_cpm: 83.55
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# ARNT

*aryl hydrocarbon receptor nuclear translocator* — 1q21.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.34×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.523× (z -15.1, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCTP]] (+0.67, fdr 3e-05), [[USP30]] (+0.67, fdr 1e-05), [[PRMT9]] (+0.66, fdr 7e-06); moves opposite to [[DDX5]] (-0.67, fdr 1e-05), [[PLEKHA6]] (-0.65, fdr 1e-05), [[NEK10]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6744.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.34×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.21× | +3.1 | 0.64 | 19/47 (NCI-H2030, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.22× | +3.1 | 0.64 | 20/50 (HOP62, SW480, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 13 with an alert ⚠; shown: the 15 strongest. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6744.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.523×** | -15.1 | 0e+00 | 47/49 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.453×** | -13.0 | 2e-36 | 44/49 (NCI-H460, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.459×** | -12.3 | 1e-32 | 34/44 (LOX-IMVI, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.500×** | -10.6 | 7e-24 | 39/45 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.573×** | -8.8 | 1e-16 | 39/50 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.612×** | -8.1 | 5e-14 | 39/48 (A-172, SNU-423, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.603×** | -8.0 | 9e-14 | 41/48 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.713×** | -7.9 | 3e-13 | 29/48 (C32, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.628×** | -7.7 | 1e-12 | 36/48 (NCI-H1792, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.751×** | -6.7 | 1e-09 | 36/48 (A-172, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.749×** | -4.6 | 3e-04 | 29/47 (CHP-212, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.762×** | -4.5 | 4e-04 | 27/48 (NCI-H1792, SNU-423, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.765×** | -4.2 | 1e-03 | 25/48 (NCI-H1792, C32, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.789×** | -3.9 | 0.004 | 26/48 (A-172, SNU-423, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 0.848× | -3.8 | 0.005 | 15/48 (SW 1088, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6744. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 91.3 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -20.4) |
| [[SW 900 (line)]] | alt | 143 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -16.2) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -10.8) |
| [[A-172 (line)]] | wt | 126 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -19.8) |
| [[LOX-IMVI (line)]] | wt | 79.8 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 139 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.266× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 91.6 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -14.0) |
| [[C32 (line)]] | wt | 69.0 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -20.1) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.366× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 86.1 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -15.4) |
| [[HOP62 (line)]] | alt | 80.9 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -14.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -12.9) |
| [[hTERT-HPNE (line)]] | wt | 76.9 | 0 | 6 (5 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -15.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 125 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -14.7) |
| [[MIA PaCa-2 (line)]] | alt | 111 | 0 | 5 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.303× (z -12.5) |
| [[SNU-423 (line)]] | alt | 88.5 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -16.9) |
| [[HEC-1-A (line)]] | alt | 68.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -9.9) |
| [[A549 (line)]] | wt | 92.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -13.5) |
| [[AN3 CA (line)]] | alt | 97.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -13.4) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -12.4) |
| [[CHP-212 (line)]] | wt | 125 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -11.1) |
| [[Hs 766T (line)]] | wt | 110 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -10.4) |
| [[HS-578T (line)]] | alt | 66.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -14.1) |
| [[LS 180 (line)]] | wt | 62.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 76.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.346× (z -9.0) |
| [[SHP-77 (line)]] | alt | 116 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.366× (z -10.8) |
| [[SNU-1 (line)]] | wt | 83.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -11.9) |
| [[SW480 (line)]] | alt | 65.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.412× (z -10.6) |
| [[A498 (line)]] | wt | 75.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -11.0) |
| [[J82 (line)]] | alt | 62.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -10.5) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LoVo (line)]] | wt | 55.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.405× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H1573 (line)]] | alt | 67.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.354× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 136 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 62.8 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.289× (z -10.7) |
| [[BT-474 (line)]] | alt | 52.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -9.9) |
| [[COLO 205 (line)]] | alt | 60.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -11.3) ⚠ cell-cycle shift, explains ~46% of this change |
| [[H4 (line)]] | wt | 70.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -8.7) |
| [[HCT15 (line)]] | alt | 96.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[HT-29 (line)]] | alt | 55.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H2030 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.394× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H596 (line)]] | alt | 84.5 | 0 | 1 | — | [[Methylthiouracil (drug)]] 5 µM 0.335× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 47.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW 1088 (line)]] | alt | 75.6 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0684× (z -9.9) |
| [[A-427 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 79.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6744), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCTP]] | +0.67 | +0.71 / +0.46 | both halves | 3e-05 |  |
| [[USP30]] | +0.67 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[PRMT9]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ALG9]] | +0.66 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[PRUNE1]] | +0.66 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[PLD3]] | +0.65 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[ARL3]] | +0.65 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[CASC3]] | +0.65 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[METTL14]] | +0.65 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SLC9A6]] | +0.64 | +0.72 / +0.46 | both halves | 3e-05 |  |
| [[LRIG2]] | +0.64 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.64 | +0.69 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX5]] | -0.67 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[PLEKHA6]] | -0.65 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[NEK10]] | -0.64 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[MPDU1]] | -0.64 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[IDI2-AS1]] | -0.63 | -0.68 / -0.53 | both halves | 1e-05 |  |
| [[E2F3]] | -0.63 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[MYH15]] | -0.62 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[PPIEL-1]] | -0.62 | -0.70 / -0.51 | both halves | 1e-05 |  |
| [[PARD6G-AS1]] | -0.62 | -0.70 / -0.41 | both halves | 4e-05 |  |
| [[AGO2]] | -0.61 | -0.51 / -0.52 | both halves | 1e-05 | pathway: Transcriptional Regulation by NPAS4 |
| [[LINC01204]] | -0.61 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[HCG18]] | -0.60 | -0.48 / -0.50 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ARNT's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.713). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-0.9, -10.9); signed map (-30.3, -9.6). **Vector** length 97.3, 29.2% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +4.1 | -4.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -1.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.5 | -1.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.4 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.6 | +1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.0 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.9 | -7.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.7 | -8.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -6.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -1.9 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | aryl hydrocarbon receptor nuclear translocator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:150,809,713-150,876,708 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HIF1B, HIF-1beta, bHLHe2, ARNT1 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; PAS domain containing; Hypoxia inducible factor subunits |
| Reactome | 15 pathways, smallest: Aryl hydrocarbon receptor signalling; Xenobiotics; Regulation of gene expression by Hypoxia-inducible Factor |
| Matched by | ensembl_id |

**Function**, from UniProt [P27540](https://www.uniprot.org/uniprotkb/P27540) (Aryl hydrocarbon receptor nuclear translocator):

> Transcription factor that functions as an obligate heterodimerization partner for several basic helix-loop-helix PER-ARNT-SIM (bHLH-PAS) proteins. Forms heterodimers with the aryl hydrocarbon receptor (AHR) to mediate the transcriptional response to xenobiotics by binding xenobiotic response elements (XREs) or dioxin response elements (DREs) in target gene promoters. Also heterodimerizes with hypoxia-inducible factor alpha subunits (HIF1A, EPAS1, NPAS1 or NPAS3) to form hypoxia-inducible …

**Summary**, from NCBI Gene [405](https://www.ncbi.nlm.nih.gov/gene/405):

> This gene encodes a protein containing a basic helix-loop-helix domain and two characteristic PAS domains along with a PAC domain. The encoded protein binds to ligand-bound aryl hydrocarbon receptor and aids in the movement of this complex to the nucleus, where it promotes the expression of genes involved in xenobiotic metabolism. This protein is also a co-factor for transcriptional regulation by hypoxia-inducible factor 1. Chromosomal translocation of this locus with the ETV6 (ets variant 6) …

**Accessions** — [HGNC:700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:700) · Entrez [405](https://www.ncbi.nlm.nih.gov/gene/405) · UniProt [P27540](https://www.uniprot.org/uniprotkb/P27540) · Ensembl [ENSG00000143437](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143437)

## Data

Gene col 6744: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6744); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6744, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6744]; `tensor/DDL_lfc|DDL_z.npy` [6744]; `embed/gene_vectors.npy` [6744]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6744 or target_col == 6744). Every well: [[ARNT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARNT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
