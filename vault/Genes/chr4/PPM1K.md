---
symbol: "PPM1K"
type: "gene"
col: 8744
ensembl_id: "ENSG00000163644"
name: "protein phosphatase, Mg2+/Mn2+ dependent 1K"
location: "4q22.1"
module: 32
arm: "+"
pooled_cpm: 26.83
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 12
n_dd_up_clean: 15
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# PPM1K

*protein phosphatase, Mg2+/Mn2+ dependent 1K* — 4q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.65× (z +26.4, q 0e+00, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.397× (z -9.2, q 1e-17, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM5]] (+0.72, fdr 7e-06), [[PARP14]] (+0.71, fdr 7e-06), [[DDX60]] (+0.71, fdr 7e-06); moves opposite to [[ZNF891]] (-0.54, fdr 3e-05), [[BCR]] (-0.54, fdr 7e-05), [[AHCY]] (-0.53, fdr 2e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CADPS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8744.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.65×** | +26.4 | 0e+00 | 40/47 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +22.4 | 0e+00 | 43/48 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.00×** | +12.8 | 4e-35 | 35/47 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +12.8 | 4e-35 | 27/45 (C32, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +11.1 | 2e-26 | 32/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +9.2 | 3e-18 | 29/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.53×** | +7.8 | 5e-13 | 30/47 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +5.8 | 4e-07 | 22/48 (PANC-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.30×** | +5.0 | 4e-05 | 18/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.29×** | +4.9 | 5e-05 | 18/47 (C32, CFPAC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +4.8 | 1e-04 | 16/48 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.3 | 9e-04 | 18/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.24×** | +4.3 | 9e-04 | 13/48 (LoVo, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.3 | 9e-04 | 10/48 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +4.1 | 0.002 | 14/48 (LoVo, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.005 | 11/48 (PANC-1, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.007 | 11/47 (LoVo, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8744.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.397×** | -9.2 | 1e-17 | 33/48 (RKO, H4, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.408×** | -9.0 | 8e-17 | 30/46 (RKO, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.775×** | -6.9 | 8e-10 | 23/48 (A549, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.716×** | -5.9 | 5e-07 | 18/38 (RPMI-7951, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.556×** | -5.9 | 5e-07 | 16/31 (NCI-H2347, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.762×** | -4.9 | 8e-05 | 16/47 (BT-474, RPMI-7951, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -4.9 | 9e-05 | 20/48 (NCI-H1573, RPMI-7951, …) | top dose only | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.787×** | -4.6 | 3e-04 | 20/47 (KATO III, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.858× | -4.2 | 0.002 | 16/48 (A498, NCI-H1792, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.806×** | -4.1 | 0.002 | 20/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.811×** | -4.0 | 0.003 | 18/48 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.820×** | -3.8 | 0.007 | 20/48 (RPMI-7951, LoVo, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.696×** | -3.6 | 0.012 | 10/47 (NCI-H1573, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.831×** | -3.6 | 0.015 | 16/48 (KATO III, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.847× | -3.2 | 0.056 | 17/48 (A549, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8744. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 48.2 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 31.1 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.154× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 28.4 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +16.7) | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -14.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 30.1 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.25× (z +20.5) | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -12.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 32.1 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.153× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0491× (z -9.0) |
| [[KATO III (line)]] | alt | 28.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.296× (z -9.3) |
| [[RKO (line)]] | wt | 60.6 | 0 | 4 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0150× (z -20.3) |
| [[A498 (line)]] | wt | 64.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 19.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +16.6) | — |
| [[LS 180 (line)]] | wt | 19.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +15.7) | — |
| [[PANC-1 (line)]] | alt | 9.30 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.63× (z +19.9) | — |
| [[A549 (line)]] | wt | 18.7 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.268× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 26.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 17.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +13.3) | — |
| [[HT-29 (line)]] | alt | 19.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 41.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.86× (z +18.3) | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 20.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +13.3) | — |
| [[LOX-IMVI (line)]] | wt | 25.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +11.1) | [[Selinexor (drug)]] 5 µM 0.319× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 41.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 22.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +11.6) | — |
| [[RPMI-7951 (line)]] | alt | 40.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0868× (z -15.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 27.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +9.8) | — |
| [[SW480 (line)]] | alt | 15.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +14.4) | — |
| [[BT-474 (line)]] | alt | 34.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0906× (z -8.6) |
| [[Hs 766T (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 27.7 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0645× (z -10.1) |
| [[SW1417 (line)]] | alt | 7.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +10.4) | — |
| [[SW48 (line)]] | wt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.18× (z +8.5) | — |
| [[A-427 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8744), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM5]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[PARP14]] | +0.71 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[DDX60]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[IFIH1]] | +0.71 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[IFI27]] | +0.69 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[DDX60L]] | +0.68 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[HLA-E]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[IRF7]] | +0.68 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[IFIT3]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[RSAD2]] | +0.67 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[PLEKHA4]] | +0.67 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[IFI44]] | +0.67 | +0.62 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF891]] | -0.54 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[BCR]] | -0.54 | -0.61 / -0.38 | both halves | 7e-05 |  |
| [[AHCY]] | -0.53 | -0.49 / -0.46 | both halves | 2e-05 | pathway: Diseases of metabolism |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CADPS2]] | B | CADPS2 activity raises PPM1K's level | lines that do not express CADPS2 (14) vs lines expressing it (36) | 1.61× lower at baseline in the lines without CADPS2 | 0.025 | ⚠ within organs, on part of the lines; also absent: DGKG, RBPMS, FAM3B |
| [[MX1]] | B | MX1 activity weakens PPM1K's drug response | lines that do not express MX1 (19) vs lines expressing it (29) | the lines without MX1 respond 1.10× as strongly (z diff -0.52); strongest at Homoharringtonine 0.5 µM: 2.59x vs 1.44x (z diff -3.6) | 0.049 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1; target measured in part of the lines; both ways; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers PPM1K's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[TOP2A]] | B | TOP2A activity lowers PPM1K's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.677). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.1, 52.0); signed map (64.1, 29.9). **Vector** length 111, 28.2% of its response variance represented; |z| ≥ 3 in 1,177 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.55 to 56); *interferon gamma response* (hallmark, mean cos +0.56 to 60); *interferon* (control, mean cos +0.62 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +26.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.0 | +12.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +12.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +22.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.3 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +2.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.8 | +4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +4.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.2 | -4.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -5.2 | -6.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | +1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.7 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | -9.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.9 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase, Mg2+/Mn2+ dependent 1K |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.1 — chr4:88,257,620-88,284,769 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761G058, PP2Ckappa, hPTMP, PP2Cm, BDP |
| Gene groups (HGNC) | Protein phosphatases, Mg2+/Mn2+ dependent; Branched chain alpha-keto acid dehydrogenase complex subunits |
| Reactome | 6 pathways, smallest: H139Hfs13* PPM1K causes a mild variant of  MSUD; Maple Syrup Urine Disease; Diseases of branched-chain amino acid catabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3J5](https://www.uniprot.org/uniprotkb/Q8N3J5) (Protein phosphatase Mn(2+)-dependent 1K):

> Serine/threonine-protein phosphatase component of macronutrients metabolism. Forms a functional kinase and phosphatase pair with BCKDK, serving as a metabolic regulatory node that coordinates branched-chain amino acids (BCAAs) with glucose and lipid metabolism via two distinct phosphoprotein targets: mitochondrial BCKDHA subunit of the branched-chain alpha-ketoacid dehydrogenase (BCKDH) complex and cytosolic ACLY, a lipogenic enzyme of Krebs cycle. At high levels of branched-chain ketoacids, …

**Summary**, from NCBI Gene [152926](https://www.ncbi.nlm.nih.gov/gene/152926):

> This gene encodes a member of the PPM family of Mn2+/Mg2+-dependent protein phosphatases. The encoded protein, essential for cell survival and development, is targeted to the mitochondria where it plays a key role in regulation of the mitochondrial permeability transition pore. [provided by RefSeq, Sep 2012]

**Accessions** — [HGNC:25415](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25415) · Entrez [152926](https://www.ncbi.nlm.nih.gov/gene/152926) · UniProt [Q8N3J5](https://www.uniprot.org/uniprotkb/Q8N3J5) · Ensembl [ENSG00000163644](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163644)

## Data

Gene col 8744: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8744); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8744, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8744]; `tensor/DDL_lfc|DDL_z.npy` [8744]; `embed/gene_vectors.npy` [8744]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8744 or target_col == 8744). Every well: [[PPM1K — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPM1K.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
