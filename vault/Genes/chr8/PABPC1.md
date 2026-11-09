---
symbol: "PABPC1"
type: "gene"
col: 962
ensembl_id: "ENSG00000070756"
name: "poly(A) binding protein cytoplasmic 1"
location: "8q22.3"
module: 43
arm: "+"
pooled_cpm: 1133.75
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# PABPC1

*poly(A) binding protein cytoplasmic 1* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.18× (z +17.6, q 0e+00, up in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.52× (z +6.4, q 2e-08, up in 44 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C-33 A 0.470×, CHP-212 0.567×; ⚠ cell-cycle shift, explains ~66% of this change).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EEF2]] (+0.70, fdr 7e-06), [[SLC25A6]] (+0.66, fdr 1e-05), [[SNHG29]] (+0.65, fdr 7e-06); moves opposite to [[MRPS11]] (-0.54, fdr 3e-05), [[CIAPIN1]] (-0.53, fdr 6e-05), [[WDR53]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 962.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.18×** | +17.6 | 0e+00 | 48/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.74×** | +14.8 | 0e+00 | 43/43 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +11.4 | 1e-27 | 44/44 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.62×** | +7.4 | 2e-11 | 42/47 (KATO III, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +6.4 | 2e-08 | 44/47 (BT-474, SHP-77, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.51×** | +6.3 | 3e-08 | 42/47 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.33×** | +6.2 | 5e-08 | 25/47 (COLO 205, AsPC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.42×** | +5.4 | 6e-06 | 38/47 (A-172, KATO III, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.41×** | +5.2 | 1e-05 | 43/47 (A-172, SHP-77, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.38×** | +4.8 | 1e-04 | 36/46 (COLO 205, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.30×** | +4.1 | 0.002 | 34/47 (NCI-H460, AsPC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.30×** | +4.0 | 0.003 | 32/47 (SW 900, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.007 | 31/47 (KATO III, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.28×** | +3.7 | 0.007 | 26/47 (hTERT-HPNE, MIA PaCa-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.59×** | +3.7 | 0.008 | 43/47 (KATO III, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.040 | 30/48 (KATO III, COLO 205, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.044 | 30/46 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.45×** | +3.0 | 0.086 | 35/47 (SK-MEL-2, H4, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 962.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (C-33 A 0.470×, CHP-212 0.567×; ⚠ cell-cycle shift, explains ~66% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | 0.779× | -3.6 | 0.20 | 35/46 (SW480, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 962. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 802 | 9 (9 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +17.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 417 | 8 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.20× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 922 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +15.1) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 750 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +13.3) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[A498 (line)]] | wt | 1,043 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +18.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 1,536 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +16.1) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[C32 (line)]] | wt | 1,098 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +14.3) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 748 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +17.1) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 894 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +21.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 1,030 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +15.0) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 730 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +15.1) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 783 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +17.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.92× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 1,785 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +14.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 1,233 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +18.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 1,046 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +16.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -14.0) ⚠ cell-cycle shift, explains ~66% of this change |
| [[HepG2_C3A (line)]] | wt | 935 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +13.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 1,214 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +14.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 1,559 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +14.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 1,006 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +15.0) ⚠ cell-cycle shift, explains ~66% of this change | — |
| [[J82 (line)]] | alt | 957 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +12.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 1,134 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +18.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 1,772 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +11.9) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[PANC-1 (line)]] | alt | 1,365 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +16.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 896 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +15.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 863 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +17.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 1,213 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +14.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 802 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +11.7) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 1,034 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.567× (z -9.5) ⚠ cell-cycle shift, explains ~66% of this change |
| [[HEC-1-A (line)]] | alt | 848 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +16.3) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 1,391 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +13.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 1,660 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +16.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 1,202 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +12.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 1,533 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +15.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 1,074 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +13.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 1,098 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +18.9) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 1,019 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.04× (z +10.0) | — |
| [[H4 (line)]] | wt | 902 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +15.3) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 1,224 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +15.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 1,773 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +13.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 708 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +14.3) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 1,349 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +12.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 1,294 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +13.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 2,485 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 1,108 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +14.7) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 579 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +12.7) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 282 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 920 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1,081 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1,369 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 890 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 962), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF2]] | +0.70 | +0.65 / +0.71 | both halves | 7e-06 | STRING 775 |
| [[SLC25A6]] | +0.66 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[SNHG29]] | +0.65 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[RPLP0]] | +0.61 | +0.50 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 620 |
| [[PCBP2]] | +0.61 | +0.51 / +0.75 | both halves | 1e-05 | STRING 922 |
| [[CCNI]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[RPS2]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 715 |
| [[NPM1]] | +0.59 | +0.43 / +0.73 | both halves | 3e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 471 |
| [[HNRNPA1]] | +0.59 | +0.42 / +0.59 | both halves | 4e-05 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 945 |
| [[RPL8]] ⚠ | +0.58 | +0.58 / +0.49 | both halves | 2e-05 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 741; ⚠ in the vector space only through flagged drug-doses |
| [[PPP1CC]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 | STRING 579 |
| [[PSAP]] | +0.58 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[EIF2S3]] | +0.56 | +0.37 / +0.66 | both halves | 8e-05 | pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 696 |

## Genes that move opposite

*34 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS11]] | -0.54 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[CIAPIN1]] | -0.53 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[WDR53]] | -0.51 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[MRPL38]] | -0.50 | -0.24 / -0.54 | both halves | 5e-04 |  |
| [[ASAH2B]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[PHF5A]] | -0.50 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[TOE1]] | -0.50 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[COMMD5]] | -0.48 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[LRR1]] | -0.48 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[COQ6]] | -0.48 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[RRP36]] | -0.48 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ZNF101]] | -0.48 | -0.24 / -0.44 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.411). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-46.9, -30.7); signed map (-61.5, -7.6). **Vector** length 110, 48.3% of its response variance represented; |z| ≥ 3 in 1,001 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.2 | +0.9 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +3.2 | +0.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.1 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +2.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.7 | +0.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.0 | -0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.9 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.7 | -0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.3 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | +2.0 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | poly(A) binding protein cytoplasmic 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.3 — chr8:100,685,816-100,722,809 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PABP1, PABPL1; previously PAB1, PABPC2 |
| Gene groups (HGNC) | RNA binding motif containing; MicroRNA protein coding host genes |
| Hallmark sets | PEROXISOME, MYC_TARGETS_V1 |
| Reactome | 24 pathways, smallest: Z-decay: degradation of maternal mRNAs by zygotically expressed factors; Deadenylation of mRNA; M-decay: degradation of maternal mRNAs by maternally stored factors |
| Matched by | ensembl_id |

**Function**, from UniProt [P11940](https://www.uniprot.org/uniprotkb/P11940) (Polyadenylate-binding protein 1):

> Binds the poly(A) tail of mRNA, including that of its own transcript, and regulates processes of mRNA metabolism such as pre-mRNA splicing and mRNA stability. Its function in translational initiation regulation can either be enhanced by PAIP1 or repressed by PAIP2. Can probably bind to cytoplasmic RNA sequences other than poly(A) in vivo. Binds to N6-methyladenosine (m6A)-containing mRNAs and contributes to MYC stability by binding to m6A-containing MYC mRNAs. Involved in translationally …

**Summary**, from NCBI Gene [26986](https://www.ncbi.nlm.nih.gov/gene/26986):

> This gene encodes a poly(A) binding protein. The protein shuttles between the nucleus and cytoplasm and binds to the 3' poly(A) tail of eukaryotic messenger RNAs via RNA-recognition motifs. The binding of this protein to poly(A) promotes ribosome recruitment and translation initiation; it is also required for poly(A) shortening which is the first step in mRNA decay. The gene is part of a small gene family including three protein-coding genes and several pseudogenes.[provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:8554](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8554) · Entrez [26986](https://www.ncbi.nlm.nih.gov/gene/26986) · UniProt [P11940](https://www.uniprot.org/uniprotkb/P11940) · Ensembl [ENSG00000070756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070756)

## Data

Gene col 962: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 962); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 962, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 962]; `tensor/DDL_lfc|DDL_z.npy` [962]; `embed/gene_vectors.npy` [962]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 962 or target_col == 962). Every well: [[PABPC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PABPC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
