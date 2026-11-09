---
symbol: "STX5"
type: "gene"
col: 8493
ensembl_id: "ENSG00000162236"
name: "syntaxin 5"
location: "11q12.3"
module: 41
arm: "+"
pooled_cpm: 90.47
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 17
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# STX5

*syntaxin 5* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.12× (z +10.2, q 1e-21, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.527× (z -8.4, q 3e-14, down in 32 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.672× (z -7.2, q 1e-10, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB5A]] (+0.77, fdr 7e-06), [[STX5-DT]] (+0.71, fdr 7e-06, ⚠ same locus), [[COQ10B]] (+0.69, fdr 7e-06), [[SELENOK]] (+0.69, fdr 1e-05); moves opposite to [[ATIC]] (-0.69, fdr 7e-06), [[ZDHHC21]] (-0.67, fdr 7e-06), [[CCT2]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8493.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.12×** | +10.2 | 1e-21 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +7.2 | 2e-10 | 39/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +5.9 | 6e-07 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.3 | 2e-05 | 34/49 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +5.1 | 3e-05 | 1/50 (NCI-H2030) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +4.6 | 4e-04 | 32/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.6 | 4e-04 | 31/48 (SNU-1, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.009 | 24/48 (LOX-IMVI, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8493.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.527×** | -8.4 | 3e-14 | 32/43 (SW48, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.672×** | -7.2 | 1e-10 | 39/48 (NCI-H1792, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.594×** | -6.9 | 1e-09 | 35/49 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.658×** | -5.5 | 5e-06 | 33/48 (NCI-H1573, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.669×** | -5.5 | 5e-06 | 43/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.714×** | -4.6 | 4e-04 | 34/49 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.784×** | -4.5 | 6e-04 | 33/48 (NCI-H2347, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.735×** | -3.9 | 0.008 | 26/45 (RKO, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.583×** | -3.8 | 0.008 | 30/48 (AsPC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.738×** | -3.8 | 0.008 | 27/47 (HS-578T, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **0.597×** | -3.7 | 0.012 | 28/48 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.734×** | -3.5 | 0.020 | 29/48 (SW 900, hTERT-HPNE, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.638×** | -3.2 | 0.061 | 26/47 (C32, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.793×** | -3.2 | 0.064 | 26/48 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.761×** | -3.1 | 0.070 | 24/48 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.800×** | -3.0 | 0.085 | 22/48 (NCI-H1792, hTERT-HPNE, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.654×** | -3.0 | 0.085 | 22/48 (SNU-1, Panc 03.27, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8493. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 126 | 2 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +12.1) | [[Lonafarnib (drug)]] 5 µM 0.184× (z -9.6) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.534× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 50.3 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.82× (z +15.2) | — |
| [[SW48 (line)]] | wt | 71.6 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.30× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -13.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 190 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -10.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 59.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +13.0) | — |
| [[PANC-1 (line)]] | alt | 66.1 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.65× (z +12.8) | — |
| [[SNU-1 (line)]] | wt | 74.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.37× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -14.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 67.0 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.22× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 110 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +8.5) | [[Selinexor (drug)]] 5 µM 0.494× (z -10.5) |
| [[HS-578T (line)]] | alt | 111 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -12.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 125 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.446× (z -9.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 79.1 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +10.0) | — |
| [[RKO (line)]] | wt | 57.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -12.1) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 89.1 | 0 | 2 | — | [[Rutin (trihydrate) (drug)]] 0.5 µM 0.0742× (z -9.2) |
| [[SW 900 (line)]] | alt | 95.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -11.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 155 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.387× (z -9.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 78.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +12.9) | — |
| [[A-427 (line)]] | wt | 82.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -10.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 74.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 70.8 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.166× (z -8.9) |
| [[C32 (line)]] | wt | 71.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +11.7) | — |
| [[CFPAC-1 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.368× (z -9.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 133 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -13.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -9.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -11.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -9.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 61.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 86.2 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.305× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 64.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -9.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 36.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.407× (z -8.5) |
| [[SNU-423 (line)]] | alt | 101 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.463× (z -10.6) |
| [[A-172 (line)]] | wt | 73.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 85.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 73.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 95.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 106 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 99.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8493), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB5A]] | +0.77 | +0.72 / +0.82 | both halves | 7e-06 | STRING 486 |
| [[STX5-DT]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 | ⚠ same locus (0.2 kb: neighbours can correlate without regulation) |
| [[COQ10B]] | +0.69 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[SELENOK]] | +0.69 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[OTUD5]] | +0.69 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[MON2]] | +0.64 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[OSBP]] | +0.64 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[ARFGAP3]] | +0.63 | +0.67 / +0.66 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[TNXB]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[TESK2]] | +0.63 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[RABGEF1]] | +0.62 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[INAFM1]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[PDXDC2P-NPIPB14P]] | +0.61 | +0.60 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATIC]] | -0.69 | -0.70 / -0.66 | both halves | 7e-06 |  |
| [[ZDHHC21]] | -0.67 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[CCT2]] | -0.64 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[AGPS]] | -0.64 | -0.61 / -0.62 | both halves | 7e-06 | pathway: Protein localization |
| [[CCT5]] | -0.62 | -0.67 / -0.56 | both halves | 1e-05 |  |
| [[FAM98B]] | -0.61 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[IPO8]] | -0.61 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.61 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[DLAT]] | -0.60 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[MEST]] | -0.60 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[FARSB]] | -0.60 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[RUVBL1]] | -0.59 | -0.66 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.596). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (8.9, -39.5); signed map (-48.3, 14.7). **Vector** length 143, 50.0% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.0 | +2.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.4 | +10.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | +3.2 | +2.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +3.2 | +1.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.9 | +1.5 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.8 | -7.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.2 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -2.9 |
|  | [[EX229 (drug)]] 5 µM |  | -5.5 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -4.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.8 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.5 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,806,860-62,832,051 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SED5; previously STX5A |
| Gene groups (HGNC) | Syntaxins |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS |
| Reactome | 18 pathways, smallest: Insertion of tail-anchored proteins into the endoplasmic reticulum membrane; Cargo concentration in the ER; Intra-Golgi traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13190](https://www.uniprot.org/uniprotkb/Q13190) (Syntaxin-5):

> Mediates endoplasmic reticulum to Golgi transport. Together with p115/USO1 and GM130/GOLGA2, involved in vesicle tethering and fusion at the cis-Golgi membrane to maintain the stacked and inter-connected structure of the Golgi apparatus.; [Isoform 2]: Required for Golgi to endoplasmic reticulum retrogade transport, and for intra-Golgi transport.; (Microbial infection) Required for the efficient production of infectious virion during human cytomegalovirus infection. Mechanistically, participates …

**Summary**, from NCBI Gene [6811](https://www.ncbi.nlm.nih.gov/gene/6811):

> This gene encodes a member of the syntaxin or t-SNARE (target-SNAP receptor) family. These proteins are found on cell membranes and serve as the targets for v-SNAREs (vesicle-SNAP receptors), permitting specific synaptic vesicle docking and fusion. The encoded protein regulates endoplasmic reticulum to Golgi transport and plays a critical role in autophagy. Autoantibodies targeting the encoded protein may be a diagnostic marker for endometriosis. Alternatively spliced transcript variants …

**Accessions** — [HGNC:11440](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11440) · Entrez [6811](https://www.ncbi.nlm.nih.gov/gene/6811) · UniProt [Q13190](https://www.uniprot.org/uniprotkb/Q13190) · Ensembl [ENSG00000162236](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162236)

## Data

Gene col 8493: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8493); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8493, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8493]; `tensor/DDL_lfc|DDL_z.npy` [8493]; `embed/gene_vectors.npy` [8493]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8493 or target_col == 8493). Every well: [[STX5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STX5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
