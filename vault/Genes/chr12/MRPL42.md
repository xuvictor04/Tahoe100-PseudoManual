---
symbol: "MRPL42"
type: "gene"
col: 12512
ensembl_id: "ENSG00000198015"
name: "mitochondrial ribosomal protein L42"
location: "12q22"
module: 4
arm: "+"
pooled_cpm: 50.44
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MRPL42

*mitochondrial ribosomal protein L42* — 12q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.63× (z +32.6, q 0e+00, up in 45 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.28× (z +6.1, q 1e-07, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.611× (z -17.7, q 0e+00, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPE]] (+0.75, fdr 7e-06), [[FAM98B]] (+0.74, fdr 7e-06), [[TMEM33]] (+0.73, fdr 7e-06); moves opposite to [[ING2]] (-0.75, fdr 7e-06), [[MSX1]] (-0.68, fdr 3e-05), [[LINC00685]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 22 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12512.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.63×** | +32.6 | 0e+00 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.30×** | +29.0 | 0e+00 | 43/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.47×** | +21.1 | 0e+00 | 40/45 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +6.4 | 2e-08 | 0/49 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +6.1 | 1e-07 | 24/48 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.28×** | +6.1 | 1e-07 | 25/47 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +6.0 | 2e-07 | 28/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.27×** | +5.9 | 2e-07 | 23/48 (SNU-423, HCT15, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +5.9 | 2e-07 | 23/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.25×** | +5.2 | 1e-05 | 22/47 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.21×** | +4.9 | 6e-05 | 21/48 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.9 | 6e-05 | 20/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.44×** | +4.8 | 6e-05 | 18/48 (C32, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | 1.20× | +4.5 | 2e-04 | 19/47 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +4.5 | 3e-04 | 17/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.8 | 0.003 | 11/48 (NCI-H23, C32, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.003 | 13/48 (NCI-H460, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.7 | 0.005 | 8/48 (NCI-H2347, SNU-423, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.011 | 8/48 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.013 | 8/48 (CFPAC-1, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sonidegib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.040 | 11/48 (A498, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 1.12× | +2.9 | 0.067 | 5/48 (NCI-H1573, COLO 205, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.12× | +2.8 | 0.090 | 4/48 (A498, SHP-77, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12512.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.611×** | -17.7 | 0e+00 | 37/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.758×** | -9.9 | 1e-20 | 25/48 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.799×** | -5.5 | 9e-06 | 23/47 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.734×** | -4.1 | 0.005 | 15/48 (CFPAC-1, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.847× | -4.1 | 0.005 | 15/47 (J82, NCI-H2030, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.858× | -3.7 | 0.022 | 18/48 (BT-474, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12512. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 62.9 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +20.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -14.7) |
| [[HT-29 (line)]] | alt | 48.3 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +15.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -11.3) |
| [[LoVo (line)]] | wt | 86.5 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +18.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -15.9) |
| [[NCI-H2030 (line)]] | alt | 59.7 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +11.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 82.7 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +8.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -10.7) |
| [[J82 (line)]] | alt | 43.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -10.7) |
| [[KATO III (line)]] | alt | 39.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +14.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -8.7) |
| [[LS 180 (line)]] | wt | 66.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.17× (z +17.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -17.0) |
| [[MIA PaCa-2 (line)]] | alt | 41.0 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.23× (z +15.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 85.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +17.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 37.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -9.3) |
| [[SW480 (line)]] | alt | 65.0 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +19.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -13.6) |
| [[A-172 (line)]] | wt | 32.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.24× (z +12.4) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 41.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +14.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 41.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +14.3) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 31.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.79× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 45.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.77× (z +14.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -9.5) |
| [[HOP62 (line)]] | alt | 30.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +17.0) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 28.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +12.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 58.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +11.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 36.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.98× (z +16.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 46.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.61× (z +17.4) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 66.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.83× (z +21.3) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 82.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +12.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -14.5) |
| [[SNU-423 (line)]] | alt | 33.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.91× (z +16.1) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 37.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +12.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 48.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +11.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 30.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.34× (z +17.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 36.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.78× (z +10.9) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 98.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +9.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -8.5) |
| [[H4 (line)]] | wt | 42.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +11.3) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 55.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +13.4) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 30.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.29× (z +11.9) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 30.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.74× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 42.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 57.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +10.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 71.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -10.3) |
| [[COLO 205 (line)]] | alt | 38.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +11.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 34.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 44.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 79.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -11.6) |
| [[SW 1271 (line)]] | alt | 74.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -9.4) |
| [[BT-474 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 70.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12512), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPE]] | +0.75 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[FAM98B]] | +0.74 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[TMEM33]] | +0.73 | +0.64 / +0.79 | both halves | 7e-06 |  |
| [[GFM1]] | +0.73 | +0.65 / +0.74 | both halves | 7e-06 | pathway: Mitochondrial translation; STRING 831 |
| [[MRPL3]] | +0.73 | +0.67 / +0.77 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 952 |
| [[EFTUD2]] | +0.72 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[PPP5C]] | +0.71 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[PRPF19]] | +0.71 | +0.58 / +0.72 | both halves | 8e-06 |  |
| [[MRPS27]] | +0.70 | +0.75 / +0.66 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 988 |
| [[MEST]] | +0.69 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[ATIC]] | +0.68 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[PPT1]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ING2]] | -0.75 | -0.60 / -0.78 | both halves | 7e-06 |  |
| [[MSX1]] | -0.68 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[LINC00685]] | -0.66 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[TMEM106A]] | -0.66 | -0.58 / -0.66 | both halves | 8e-06 |  |
| [[ZMYM5]] | -0.65 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[DALRD3]] | -0.65 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[SELENOK]] | -0.65 | -0.54 / -0.67 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.64 | -0.58 / -0.63 | both halves | 8e-06 |  |
| [[CATSPERG]] | -0.64 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.64 | -0.58 / -0.72 | both halves | 7e-06 |  |
| [[ARID4A]] | -0.64 | -0.58 / -0.65 | both halves | 8e-06 |  |
| [[IRX5]] | -0.64 | -0.46 / -0.62 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.754). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-23.5, -34.6); signed map (-16.0, -44.8). **Vector** length 103, 25.6% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing in the nucleus* (reactome, mean cos +0.51 to 8); *tRNA processing* (reactome, mean cos +0.51 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +21.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +32.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +29.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +6.0 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.8 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.2 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.3 | -17.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.7 | -9.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -5.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.7 | -1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -4.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L42 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q22 — chr12:93,467,514-93,516,214 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRPS32, MRP-L31, RPML31, PTD007, HSPC204, MRPL31, mL42 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9Y6G3](https://www.uniprot.org/uniprotkb/Q9Y6G3) carries no function annotation.

**Summary**, from NCBI Gene [28977](https://www.ncbi.nlm.nih.gov/gene/28977):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14493](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14493) · Entrez [28977](https://www.ncbi.nlm.nih.gov/gene/28977) · UniProt [Q9Y6G3](https://www.uniprot.org/uniprotkb/Q9Y6G3) · Ensembl [ENSG00000198015](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198015)

## Data

Gene col 12512: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12512); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12512, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12512]; `tensor/DDL_lfc|DDL_z.npy` [12512]; `embed/gene_vectors.npy` [12512]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12512 or target_col == 12512). Every well: [[MRPL42 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL42.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
