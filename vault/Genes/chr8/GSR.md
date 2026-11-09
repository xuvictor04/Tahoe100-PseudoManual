---
symbol: "GSR"
type: "gene"
col: 2482
ensembl_id: "ENSG00000104687"
name: "glutathione-disulfide reductase"
location: "8p12"
module: 25
arm: "+"
pooled_cpm: 39.17
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# GSR

*glutathione-disulfide reductase* — 8p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 3.03× (z +20.3, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.693× (z -9.3, q 5e-18, down in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (AsPC-1 0.266×, SNU-1 0.233×, RKO 0.451×, NCI-H1573 0.375×, …; ⚠ cell-cycle shift, explains ~27% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (KATO III 0.446×, HT-29 0.339×, NCI-H460 0.426×, SW480 0.543×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SNU-1 0.193×, A-427 0.409×; ⚠ cell-cycle shift, explains ~91% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBQLN1]] (+0.72, fdr 7e-06), [[RAD23B]] (+0.72, fdr 7e-06), [[LARP1]] (+0.71, fdr 7e-06); moves opposite to [[TNRC6C]] (-0.67, fdr 7e-06), [[RSPRY1]] (-0.61, fdr 1e-05), [[NBPF14]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NOG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2482.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.03×** | +20.3 | 0e+00 | 44/46 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.98×** | +18.8 | 0e+00 | 46/46 (KATO III, A-172, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.69×** | +18.1 | 0e+00 | 45/47 (LoVo, COLO 205, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +15.1 | 0e+00 | 36/40 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.11×** | +13.7 | 2e-40 | 35/44 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +12.3 | 1e-32 | 31/42 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +11.2 | 2e-27 | 38/46 (LoVo, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +10.1 | 6e-22 | 36/45 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.16×** | +7.4 | 1e-11 | 28/40 (AsPC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.75×** | +7.3 | 2e-11 | 35/47 (A-172, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +7.2 | 3e-11 | 29/47 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +5.4 | 4e-06 | 26/45 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.5 | 3e-04 | 16/31 (HEC-1-A, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 4e-04 | 19/47 (KATO III, HCT15, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +4.0 | 0.002 | 17/47 (A498, HOP62, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.062 | 11/45 (AsPC-1, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.18× | +3.0 | 0.079 | 11/46 (A498, SNU-423, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.087 | 7/47 (NCI-H2347, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2482.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (AsPC-1 0.266×, SNU-1 0.233×, RKO 0.451×, NCI-H1573 0.375×, …; ⚠ cell-cycle shift, explains ~27% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (KATO III 0.446×, HT-29 0.339×, NCI-H460 0.426×, SW480 0.543×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SNU-1 0.193×, A-427 0.409×; ⚠ cell-cycle shift, explains ~91% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.693×** | -9.3 | 5e-18 | 28/47 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.787×** | -6.1 | 3e-07 | 24/47 (AsPC-1, SNU-1, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.781×** | -4.4 | 0.003 | 21/47 (AsPC-1, NCI-H23, …) | top dose only | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.938× | -4.0 | 0.011 | 1/48 (hTERT-HPNE) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2482. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 55.1 | 4 (1 ⚠) | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.58× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -12.3) |
| [[LoVo (line)]] | wt | 38.4 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.18× (z +15.4) | — |
| [[A498 (line)]] | wt | 79.2 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Triamcinolone (drug)]] 0.5 µM 2.41× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 29.9 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.76× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 42.3 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.67× (z +13.0) | — |
| [[LS 180 (line)]] | wt | 67.6 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.03× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 38.7 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.95× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -9.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H460 (line)]] | wt | 53.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.74× (z +14.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -11.1) |
| [[SW480 (line)]] | alt | 44.8 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.75× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -10.1) |
| [[A-172 (line)]] | wt | 16.1 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 6.50× (z +12.2) | — |
| [[A549 (line)]] | wt | 49.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.01× (z +16.7) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 19.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.79× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 10.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 9.14× (z +12.4) | — |
| [[Hs 766T (line)]] | wt | 39.4 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.06× (z +11.7) | — |
| [[HS-578T (line)]] | alt | 23.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.19× (z +11.8) | — |
| [[NCI-H1792 (line)]] | alt | 19.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.85× (z +13.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 57.4 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.68× (z +9.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.409× (z -9.0) ⚠ cell-cycle shift, explains ~91% of this change |
| [[AsPC-1 (line)]] | alt | 53.7 | 1 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.24× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -16.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 39.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.60× (z +11.9) | — |
| [[HCT15 (line)]] | alt | 55.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.37× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 60.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.02× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 38.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -11.7) |
| [[J82 (line)]] | alt | 23.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.07× (z +10.3) | — |
| [[SNU-1 (line)]] | wt | 59.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -13.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 61.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 20.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.68× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 21.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.50× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 14.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.25× (z +9.2) | — |
| [[RKO (line)]] | wt | 43.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -9.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 21.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.72× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 100 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -8.8) |
| [[AN3 CA (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.28 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 67.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2482), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBQLN1]] | +0.72 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[RAD23B]] | +0.72 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[LARP1]] | +0.71 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[TALDO1]] | +0.70 | +0.74 / +0.71 | both halves | 7e-06 | pathway: Cellular response to chemical stress; STRING 530 |
| [[HSD17B4]] | +0.69 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[NXPE3]] | +0.69 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[IDE]] | +0.68 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[CCT3]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[FECH]] | +0.66 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[USP14]] | +0.66 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[NAA50]] | +0.65 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[PIR]] | +0.65 | +0.71 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6C]] | -0.67 | -0.68 / -0.60 | both halves | 7e-06 | pathway: TP53 Regulates Metabolic Genes |
| [[RSPRY1]] | -0.61 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[NBPF14]] | -0.60 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[NBPF19]] | -0.58 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[TPRN]] | -0.58 | -0.43 / -0.63 | both halves | 3e-05 |  |
| [[C16orf46]] | -0.57 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[BTG1]] | -0.57 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[MED19]] | -0.57 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[LRCH3]] | -0.57 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[HMGCL]] | -0.57 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[FAM110A]] | -0.57 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[PDCD7]] | -0.56 | -0.42 / -0.63 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOG]] | B | NOG activity lowers GSR's level | lines that do not express NOG (26) vs lines expressing it (24) | 1.83× higher at baseline in the lines without NOG | 0.028 | ⚠ within organs, on part of the lines; also absent: LINC01776, ENSG00000279289, FLI1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.571). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.0, -15.1); signed map (-15.5, -42.2). **Vector** length 126, 35.3% of its response variance represented; |z| ≥ 3 in 1,112 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +11.4 | +20.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +11.0 | +18.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.4 | +18.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.6 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +13.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +4.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.4 | +7.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -9.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.5 | -6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +0.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -3.2 | -1.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -3.2 | -4.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | glutathione-disulfide reductase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p12 — chr8:30,678,066-30,727,846 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GRase |
| Gene groups (HGNC) | Flavoproteins; Oxidoreductases |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, ANDROGEN_RESPONSE, APOPTOSIS, XENOBIOTIC_METABOLISM, MTORC1_SIGNALING |
| Reactome | 14 pathways, smallest: Metabolism of ingested H2SeO4 and H2SeO3 into H2Se; NFE2L2 regulating anti-oxidant/detoxification enzymes; Detoxification of Reactive Oxygen Species |
| Matched by | ensembl_id |

**Function**, from UniProt [P00390](https://www.uniprot.org/uniprotkb/P00390) (Glutathione reductase, mitochondrial):

> Catalyzes the reduction of glutathione disulfide (GSSG) to reduced glutathione (GSH). Constitutes the major mechanism to maintain a high GSH:GSSG ratio in the cytosol.

**Summary**, from NCBI Gene [2936](https://www.ncbi.nlm.nih.gov/gene/2936):

> This gene encodes a member of the class-I pyridine nucleotide-disulfide oxidoreductase family. This enzyme is a homodimeric flavoprotein. It is a central enzyme of cellular antioxidant defense, and reduces oxidized glutathione disulfide (GSSG) to the sulfhydryl form GSH, which is an important cellular antioxidant. Rare mutations in this gene result in hereditary glutathione reductase deficiency. Multiple alternatively spliced transcript variants encoding different isoforms have been found. …

**Accessions** — [HGNC:4623](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4623) · Entrez [2936](https://www.ncbi.nlm.nih.gov/gene/2936) · UniProt [P00390](https://www.uniprot.org/uniprotkb/P00390) · Ensembl [ENSG00000104687](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104687)

## Data

Gene col 2482: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2482); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2482, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2482]; `tensor/DDL_lfc|DDL_z.npy` [2482]; `embed/gene_vectors.npy` [2482]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2482 or target_col == 2482). Every well: [[GSR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
