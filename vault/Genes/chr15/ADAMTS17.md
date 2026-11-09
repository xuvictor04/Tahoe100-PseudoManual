---
symbol: "ADAMTS17"
type: "gene"
col: 6414
ensembl_id: "ENSG00000140470"
name: "ADAM metallopeptidase with thrombospondin type 1 motif 17"
location: "15q26.3"
module: 183
arm: "+"
pooled_cpm: 15.96
n_lines_expressing: 34
n_dd_up: 37
n_dd_down: 2
n_dd_up_clean: 31
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/183"]
generated_by: "tahoemap"
---

# ADAMTS17

*ADAM metallopeptidase with thrombospondin type 1 motif 17* — 15q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.20× (z +40.9, q 0e+00, up in 29 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.523× (z -5.0, q 4e-04, down in 12 of 30 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (COLO 205 0.0584×, MIA PaCa-2 0.0352×, KATO III 0.185×, Hs 766T 0.0699×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (KATO III 0.0386×, HT-29 0.0838×, MIA PaCa-2 0.0707×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.416×; ⚠ position not correctable); [[Cobimetinib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.143×); [[Binimetinib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.202×); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (SW 900 0.0526×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSRA]] (+0.50, fdr 3e-05), [[KLHL29]] (+0.48, fdr 3e-05), [[PITX1-AS1]] (+0.47, fdr 2e-05); moves opposite to [[IRAK1BP1]] (-0.52, fdr 8e-05), [[USP30]] (-0.52, fdr 6e-05), [[MRPL19]] (-0.52, fdr 1e-04).
> It is in [[Module 183]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6414.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.20×** | +40.9 | 0e+00 | 29/29 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.87×** | +36.7 | 0e+00 | 25/27 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **10.1×** | +33.8 | 0e+00 | 31/31 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.24×** | +29.0 | 0e+00 | 31/31 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **5.54×** | +25.1 | 0e+00 | 31/31 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.61×** | +24.3 | 0e+00 | 28/29 (HT-29, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.93×** | +22.2 | 0e+00 | 27/32 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.48×** | +21.1 | 0e+00 | 28/29 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.42×** | +18.0 | 0e+00 | 25/28 (C32, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.36×** | +17.7 | 0e+00 | 29/31 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.13×** | +15.6 | 0e+00 | 22/31 (PANC-1, SW1417, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.54×** | +13.6 | 1e-40 | 26/31 (SW1417, COLO 205, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.47×** | +13.2 | 3e-38 | 26/30 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.55×** | +13.2 | 5e-38 | 20/30 (COLO 205, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +11.5 | 8e-29 | 6/14 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.35×** | +9.3 | 8e-19 | 22/31 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6414.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (COLO 205 0.0584×, MIA PaCa-2 0.0352×, KATO III 0.185×, Hs 766T 0.0699×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (KATO III 0.0386×, HT-29 0.0838×, MIA PaCa-2 0.0707×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.416×; ⚠ position not correctable); [[Cobimetinib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.143×); [[Binimetinib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.202×); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (SW 900 0.0526×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.523×** | -5.0 | 4e-04 | 12/30 (KATO III, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.772×** | -3.8 | 0.040 | 17/31 (KATO III, SW480, …) | inconsistent across doses |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | 0.811× | -3.1 | 0.39 | 2/30 (C-33 A, Hs 766T) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6414. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 109 | 6 | 6 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.0386× (z -28.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.394× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 23.2 | 2 | 8 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0352× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change · without an alert: [[Cobimetinib (drug)]] 0.5 µM 0.143× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 4.04 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.2× (z +17.0) | — |
| [[HT-29 (line)]] | alt | 23.4 | 8 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +19.4) | [[Dinaciclib (drug)]] 0.05 µM 0.0838× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[PANC-1 (line)]] | alt | 6.46 | 9 | 0 | [[Panobinostat (drug)]] 5 µM 24.7× (z +17.4) | — |
| [[SW1417 (line)]] | alt | 16.5 | 9 | 0 | [[Panobinostat (drug)]] 5 µM 12.7× (z +14.3) | — |
| [[CFPAC-1 (line)]] | alt | 6.15 | 8 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.3× (z +18.5) | — |
| [[HEC-1-A (line)]] | alt | 7.11 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +16.1) | — |
| [[J82 (line)]] | alt | 12.3 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.48× (z +15.8) | — |
| [[SK-MEL-2 (line)]] | alt | 14.4 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +15.7) | — |
| [[BT-474 (line)]] | alt | 34.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +14.1) | — |
| [[C32 (line)]] | wt | 7.61 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.2× (z +16.6) | — |
| [[LoVo (line)]] | wt | 13.7 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +20.2) | — |
| [[LS 180 (line)]] | wt | 49.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +15.1) | — |
| [[Panc 03.27 (line)]] | alt | 24.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.84× (z +16.4) | — |
| [[COLO 205 (line)]] | alt | 143 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.76× (z +23.3) | [[Dinaciclib (drug)]] 0.5 µM 0.0584× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[NCI-H1573 (line)]] | alt | 13.0 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +16.6) | — |
| [[SW480 (line)]] | alt | 40.5 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +14.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.289× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 7.53 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 21.8× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 6.65 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.21× (z +11.8) | — |
| [[Hs 766T (line)]] | wt | 56.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0699× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change · without an alert: [[venetoclax (drug)]] 5 µM 0.0379× (z -9.6) |
| [[RKO (line)]] | wt | 7.52 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +11.7) | — |
| [[SW 900 (line)]] | alt | 8.04 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +12.2) | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0526× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 22.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.37× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 7.69 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.42× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 5.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.77× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 19.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +10.1) | — |
| [[A-172 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.18 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6414), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSRA]] | +0.50 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[KLHL29]] | +0.48 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[PITX1-AS1]] | +0.47 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[RASGRF2]] | +0.47 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[WDR27]] | +0.47 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[PXDC1]] | +0.46 | +0.50 / +0.22 | both halves | 6e-04 |  |
| [[CATSPERG]] | +0.46 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[NEK10]] | +0.45 | +0.51 / +0.31 | both halves | 2e-04 |  |
| [[SLC4A7]] | +0.45 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[DPH1-AS1]] | +0.44 | +0.50 / +0.32 | both halves | 2e-04 |  |
| [[TMEM132B]] | +0.44 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[IQCJ-SCHIP1]] | +0.43 | +0.30 / +0.35 | both halves | 2e-04 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRAK1BP1]] | -0.52 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[USP30]] | -0.52 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[MRPL19]] | -0.52 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[BCL9]] | -0.51 | -0.62 / -0.36 | both halves | 1e-04 |  |
| [[TERF1]] | -0.49 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[RHOT1]] | -0.49 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[TRAPPC2]] | -0.49 | -0.53 / -0.24 | both halves | 4e-04 |  |
| [[IMMP1L]] | -0.48 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[UBXN2B]] | -0.47 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[NDUFAF5]] | -0.47 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[PEX2]] | -0.46 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[NDUFS2]] | -0.46 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ADAMTS17's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 183]]; 21 genes; every member is in the + arm (projection on the module's main direction -0.477). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.3, -9.8); signed map (9.4, 20.0). **Vector** length 76.5, 15.9% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +22.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +40.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +13.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.6 | +18.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +24.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +1.4 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +15.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -3.7 | -0.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.1 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -3.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | +0.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -0.6 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.3 | +2.1 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase with thrombospondin type 1 motif 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.3 — chr15:99,971,437-100,342,005 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32769, FLJ16363 |
| Gene groups (HGNC) | ADAM metallopeptidases with thrombospondin type 1 motif |
| Reactome | 6 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TE56](https://www.uniprot.org/uniprotkb/Q8TE56) (A disintegrin and metalloproteinase with thrombospondin motifs 17):

> Extracellular metalloprotease that regulates skeletal development by modulating BMP-SMAD signaling and extracellular matrix microfibril organization, which controls chondrocyte differentiation and bone growth.

**Summary**, from NCBI Gene [170691](https://www.ncbi.nlm.nih.gov/gene/170691):

> This gene encodes a member of the ADAMTS (a disintegrin and metalloproteinase with thrombospondin motifs) protein family. ADAMTS family members share several distinct protein modules, including a propeptide region, a metalloproteinase domain, a disintegrin-like domain, and a thrombospondin type 1 (TS) motif. Individual members of this family differ in the number of C-terminal TS motifs, and some have unique C-terminal domains. The encoded preproprotein is proteolytically processed to generate …

**Accessions** — [HGNC:17109](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17109) · Entrez [170691](https://www.ncbi.nlm.nih.gov/gene/170691) · UniProt [Q8TE56](https://www.uniprot.org/uniprotkb/Q8TE56) · Ensembl [ENSG00000140470](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140470)

## Data

Gene col 6414: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6414); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6414, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6414]; `tensor/DDL_lfc|DDL_z.npy` [6414]; `embed/gene_vectors.npy` [6414]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6414 or target_col == 6414). Every well: [[ADAMTS17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTS17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
