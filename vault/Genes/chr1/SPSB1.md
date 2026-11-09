---
symbol: "SPSB1"
type: "gene"
col: 10142
ensembl_id: "ENSG00000171621"
name: "splA/ryanodine receptor domain and SOCS box containing 1"
location: "1p36.22"
module: 81
arm: "+"
pooled_cpm: 83.67
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# SPSB1

*splA/ryanodine receptor domain and SOCS box containing 1* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +10.0, q 1e-20, up in 34 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.368× (z -13.4, q 4e-38, down in 41 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.524× (z -4.5, q 6e-04, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RABGEF1]] (+0.67, fdr 7e-06), [[SLC9A1]] (+0.63, fdr 1e-05), [[PNP]] (+0.63, fdr 1e-05); moves opposite to [[YEATS4]] (-0.55, fdr 1e-05), [[NHLRC2]] (-0.54, fdr 1e-05), [[CASC2]] (-0.54, fdr 2e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC01705]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10142.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +10.0 | 1e-20 | 34/49 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.47×** | +5.1 | 8e-05 | 30/48 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +4.8 | 3e-04 | 26/48 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +4.5 | 8e-04 | 27/48 (LS 180, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.41×** | +4.5 | 1e-03 | 27/47 (Panc 03.27, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.004 | 22/48 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.005 | 26/49 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.007 | 24/48 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.013 | 27/48 (KATO III, J82, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.67×** | +3.6 | 0.020 | 24/48 (SW480, LS 180, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.041 | 20/48 (KATO III, AsPC-1, …) | rises with dose | position effect removed |
| [[Infigratinib (drug)]] 5 µM |  | **1.55×** | +3.1 | 0.097 | 17/47 (HT-29, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.25× | +3.0 | 0.11 | 19/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10142.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.368×** | -13.4 | 4e-38 | 41/47 (NCI-H2347, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.405×** | -11.7 | 5e-29 | 34/40 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.417×** | -10.9 | 3e-25 | 33/43 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.662×** | -5.3 | 2e-05 | 31/48 (A549, RKO, …) | rises with dose | composition shift; position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.524×** | -4.5 | 6e-04 | 32/47 (RKO, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.715×** | -4.5 | 6e-04 | 32/48 (RKO, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.731×** | -4.2 | 0.002 | 25/48 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.748×** | -3.9 | 0.007 | 21/48 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.752×** | -3.8 | 0.008 | 24/48 (SHP-77, RKO, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.825×** | -3.7 | 0.014 | 19/48 (LoVo, RKO, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.703×** | -3.4 | 0.038 | 21/47 (HCT15, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -3.2 | 0.051 | 3/50 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.785×** | -3.2 | 0.051 | 21/48 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.788×** | -3.2 | 0.057 | 20/49 (RKO, SHP-77, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.786×** | -3.1 | 0.071 | 20/49 (HS-578T, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10142. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 140 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.368× (z -10.9) |
| [[A549 (line)]] | wt | 128 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -21.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 130 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.291× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 180 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0827× (z -21.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 53.5 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -9.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 45.1 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +13.5) | — |
| [[PANC-1 (line)]] | alt | 63.0 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.104× (z -20.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 81.3 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +12.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.158× (z -18.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 174 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.244× (z -10.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.285× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 284 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0750× (z -19.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 40.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.42× (z +13.2) | — |
| [[A-172 (line)]] | wt | 69.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -12.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 191 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -16.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 139 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -10.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 84.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.430× (z -9.0) |
| [[SNU-423 (line)]] | alt | 196 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0543× (z -20.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 149 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -14.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 57.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.68× (z +9.4) | — |
| [[H4 (line)]] | wt | 83.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -9.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 138 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -13.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 73.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.121× (z -12.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 95.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -14.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 66.9 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Clobetasol propionate (drug)]] 0.05 µM 0.318× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 71.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 69.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +11.9) | — |
| [[RPMI-7951 (line)]] | alt | 125 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -12.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 53.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -9.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 48.2 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0587× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 45.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -12.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 41.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -10.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 37.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +12.1) | — |
| [[COLO 205 (line)]] | alt | 131 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +14.8) | — |
| [[HCT15 (line)]] | alt | 53.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 40.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 47.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +13.4) | — |
| [[J82 (line)]] | alt | 53.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 32.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +14.3) | — |
| [[SW 1088 (line)]] | alt | 99.6 | 0 | 1 | — | [[Rosiglitazone (drug)]] 0.05 µM 0.0684× (z -8.6) |
| [[SW48 (line)]] | wt | 64.3 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.218× (z -9.1) |
| [[A-427 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10142), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGEF1]] | +0.67 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[SLC9A1]] | +0.63 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[PNP]] | +0.63 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[PDE2A]] | +0.63 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[KCTD5]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[KCNK13]] | +0.60 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[POR]] | +0.59 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[MDGA1]] | +0.59 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[CORO2B]] | +0.57 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[LINC01705]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[RAB7A]] | +0.56 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[ABTB3]] | +0.56 | +0.54 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YEATS4]] | -0.55 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[NHLRC2]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[CASC2]] | -0.54 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[SCRN3]] | -0.52 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[ZZZ3]] | -0.52 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[RBM26]] | -0.52 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[MTPAP]] | -0.52 | -0.46 / -0.62 | both halves | 2e-05 |  |
| [[ARMC8]] | -0.52 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[USP24]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[LUC7L2]] | -0.52 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[LSM14A]] | -0.52 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[ZNF280D]] | -0.51 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01705]] | B | LINC01705 activity raises SPSB1's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 1.67× lower at baseline in the lines without LINC01705 | 0.005 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137 |
| [[GCKR]] | B | GCKR activity raises SPSB1's level | lines that do not express GCKR (24) vs lines expressing it (26) | 1.53× lower at baseline in the lines without GCKR | 0.042 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent |
| [[NDRG1]] | B | NDRG1 activity raises SPSB1's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 2.05× lower at baseline in the lines without NDRG1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[KRT7]] | B | KRT7 activity raises SPSB1's level | lines that do not express KRT7 (34) vs lines expressing it (16) | 1.34× lower at baseline in the lines without KRT7 | 0.094 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3 |
| [[BACE2]] | B | BACE2 activity raises SPSB1's level | lines that do not express BACE2 (10) vs lines expressing it (40) | 1.47× lower at baseline in the lines without BACE2 | 0.095 | ⚠ within organs, on part of the lines; also absent: FBXO32, STAT5A, ETS2 |
| [[ATP6V0D2]] | B | ATP6V0D2 activity raises SPSB1's level | lines that do not express ATP6V0D2 (18) vs lines expressing it (32) | 1.52× lower at baseline in the lines without ATP6V0D2 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D, ARID1A; also absent: GBP5, NALCN, IGFBP7; maybe low, not absent |
| [[ABTB3]] | B | ABTB3 activity raises SPSB1's level | lines that do not express ABTB3 (23) vs lines expressing it (27) | 1.61× lower at baseline in the lines without ABTB3 | 0.099 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000287335, TNFSF14 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.9, -3.7); signed map (-1.5, 32.2). **Vector** length 129, 40.8% of its response variance represented; |z| ≥ 3 in 1,566 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.0 | +4.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.7 | +5.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.6 | +3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.5 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.5 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +3.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -6.0 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.6 | -4.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.3 | -3.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.2 | -3.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.0 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | splA/ryanodine receptor domain and SOCS box containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:9,292,894-9,369,532 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SSB-1 |
| Gene groups (HGNC) | SplA/ryanodine receptor domain and SOCS box containing family |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BD6](https://www.uniprot.org/uniprotkb/Q96BD6) (SPRY domain-containing SOCS box protein 1):

> Substrate recognition component of a SCF-like ECS (Elongin BC-CUL2/5-SOCS-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Negatively regulates nitric oxide (NO) production and limits cellular toxicity in activated macrophages by mediating the ubiquitination and proteasomal degradation of NOS2. Acts as a bridge which links NOS2 with the ECS E3 ubiquitin ligase complex components ELOC and CUL5.

**Summary**, from NCBI Gene [80176](https://www.ncbi.nlm.nih.gov/gene/80176):

> Enables ubiquitin-like ligase-substrate adaptor activity. Involved in protein ubiquitination and ubiquitin-dependent protein catabolic process. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30628](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30628) · Entrez [80176](https://www.ncbi.nlm.nih.gov/gene/80176) · UniProt [Q96BD6](https://www.uniprot.org/uniprotkb/Q96BD6) · Ensembl [ENSG00000171621](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171621)

## Data

Gene col 10142: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10142); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10142, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10142]; `tensor/DDL_lfc|DDL_z.npy` [10142]; `embed/gene_vectors.npy` [10142]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10142 or target_col == 10142). Every well: [[SPSB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPSB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
