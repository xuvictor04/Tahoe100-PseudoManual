---
symbol: "BRCC3"
type: "gene"
col: 11692
ensembl_id: "ENSG00000185515"
name: "BRCA1/BRCA2-containing complex subunit 3"
location: "Xq28"
module: 25
arm: "+"
pooled_cpm: 51.78
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# BRCC3

*BRCA1/BRCA2-containing complex subunit 3* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.80× (z +11.5, q 7e-28, up in 38 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.31× (z +5.3, q 1e-05, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.594× (z -14.3, q 2e-43, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PUS7L]] (+0.61, fdr 1e-05), [[COX11]] (+0.60, fdr 1e-05), [[ZMPSTE24]] (+0.59, fdr 1e-05); moves opposite to [[C19orf81]] (-0.57, fdr 3e-05), [[RCE1]] (-0.56, fdr 4e-05), [[MIEN1]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11692.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +11.5 | 7e-28 | 38/48 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +9.8 | 2e-20 | 34/43 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.33×** | +5.3 | 1e-05 | 25/48 (HT-29, SW480, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +5.3 | 1e-05 | 30/48 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.6 | 4e-04 | 16/48 (NCI-H2347, NCI-H2030, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.26×** | +4.2 | 0.003 | 22/45 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.003 | 21/47 (SW480, A549, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.22×** | +3.8 | 0.012 | 18/48 (HT-29, SW480, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.013 | 18/47 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.20× | +3.5 | 0.028 | 11/48 (HT-29, SW1417, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.035 | 18/48 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.17× | +3.1 | 0.082 | 8/48 (A-427, HT-29, …) | inconsistent across doses |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.096 | 9/47 (NCI-H460, SW480, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11692.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.594×** | -14.3 | 2e-43 | 37/48 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.566×** | -11.0 | 7e-26 | 39/47 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.631×** | -8.9 | 7e-17 | 38/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.653×** | -8.3 | 2e-14 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.661×** | -8.0 | 1e-13 | 41/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.663×** | -7.7 | 2e-12 | 32/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~24% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.723×** | -6.3 | 3e-08 | 30/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.728×** | -5.9 | 2e-07 | 28/47 (HCT15, A-427, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.734×** | -5.6 | 1e-06 | 26/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.769×** | -5.1 | 2e-05 | 30/48 (SNU-423, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.773×** | -5.0 | 3e-05 | 24/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.775×** | -4.9 | 4e-05 | 27/47 (A-427, PANC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.752×** | -3.9 | 0.004 | 23/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **0.805×** | -3.9 | 0.004 | 23/47 (LS 180, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.809×** | -3.9 | 0.004 | 23/48 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.820×** | -3.8 | 0.005 | 22/48 (SW 1271, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.838× | -3.4 | 0.022 | 14/48 (A-427, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11692. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 56.6 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -18.0) |
| [[NCI-H460 (line)]] | wt | 70.0 | 0 | 7 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.411× (z -11.7) |
| [[HT-29 (line)]] | alt | 65.4 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 44.9 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +8.5) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.260× (z -12.5) |
| [[A498 (line)]] | wt | 36.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +11.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 28.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -11.0) |
| [[C32 (line)]] | wt | 52.4 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.295× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.426× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 34.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.14× (z +13.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 51.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +11.4) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.05 µM 0.507× (z -8.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 66.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -14.1) |
| [[A-427 (line)]] | wt | 67.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -19.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.529× (z -10.3) |
| [[A549 (line)]] | wt | 47.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +12.0) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 79.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -15.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 58.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -15.1) |
| [[KATO III (line)]] | alt | 71.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +11.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 47.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +12.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 80.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -12.6) |
| [[NCI-H1792 (line)]] | alt | 46.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 66.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.401× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 69.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -18.5) |
| [[CFPAC-1 (line)]] | alt | 47.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -10.3) |
| [[COLO 205 (line)]] | alt | 53.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -10.4) |
| [[HCT15 (line)]] | alt | 79.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.314× (z -9.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 61.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -16.1) |
| [[Hs 766T (line)]] | wt | 57.8 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0870× (z -12.3) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 35.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 54.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 73.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -21.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 59.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -10.3) |
| [[SW 1271 (line)]] | alt | 56.8 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0951× (z -9.0) ⚠ toxic |
| [[SW1417 (line)]] | alt | 29.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11692), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUS7L]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[COX11]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ZMPSTE24]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[TMX1]] | +0.57 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[EIF4H]] | +0.57 | +0.36 / +0.55 | both halves | 1e-04 |  |
| [[FAM120A]] | +0.57 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[IPO5]] | +0.57 | +0.37 / +0.58 | both halves | 8e-05 |  |
| [[TWF1]] | +0.56 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[DOCK7]] | +0.56 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[LMBRD2]] | +0.56 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[MRPL19]] | +0.55 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[BTBD1]] | +0.54 | +0.42 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C19orf81]] | -0.57 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[RCE1]] | -0.56 | -0.42 / -0.56 | both halves | 4e-05 | pathway: Deubiquitination |
| [[MIEN1]] | -0.53 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[CDC34]] | -0.53 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[IER5]] | -0.52 | -0.37 / -0.55 | both halves | 7e-05 |  |
| [[ZFAND2B]] | -0.52 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[TMEM106A]] | -0.52 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[IER5L]] | -0.52 | -0.30 / -0.58 | both halves | 2e-04 |  |
| [[CIB1]] | -0.52 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[INAFM1]] | -0.51 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[POLD4]] | -0.51 | -0.31 / -0.60 | both halves | 2e-04 | pathway: DNA Double-Strand Break Repair |
| [[NSUN5P1-1]] | -0.51 | -0.43 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.600). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-31.6, -23.8); signed map (-18.2, -41.2). **Vector** length 90.7, 21.8% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +0.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.1 | +2.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.3 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.1 | -14.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -3.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.9 | -1.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | BRCA1/BRCA2-containing complex subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:155,071,420-155,123,077 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C6.1A, BRCC36; previously CXorf53 |
| Gene groups (HGNC) | JAMM/MPN+ metallopeptidase family; BRCA1 A complex; BRISC complex |
| Reactome | 14 pathways, smallest: Metalloprotease DUBs; Nonhomologous End-Joining (NHEJ); Recruitment and ATM-mediated phosphorylation of repair and signaling proteins at DNA double strand breaks |
| Matched by | ensembl_id |

**Function**, from UniProt [P46736](https://www.uniprot.org/uniprotkb/P46736) (Lys-63-specific deubiquitinase BRCC36):

> Metalloprotease that specifically cleaves 'Lys-63'-linked polyubiquitin chains. Does not have activity toward 'Lys-48'-linked polyubiquitin chains. Component of the BRCA1-A complex, a complex that specifically recognizes 'Lys-63'-linked ubiquitinated histones H2A and H2AX at DNA lesions sites, leading to target the BRCA1-BARD1 heterodimer to sites of DNA damage at double-strand breaks (DSBs). In the BRCA1-A complex, it specifically removes 'Lys-63'-linked ubiquitin on histones H2A and H2AX, …

**Summary**, from NCBI Gene [79184](https://www.ncbi.nlm.nih.gov/gene/79184):

> This gene encodes a subunit of the BRCA1-BRCA2-containing complex (BRCC), which is an E3 ubiquitin ligase. This complex plays a role in the DNA damage response, where it is responsible for the stable accumulation of BRCA1 at DNA break sites. The component encoded by this gene can specifically cleave Lys 63-linked polyubiquitin chains, and it regulates the abundance of these polyubiquitin chains in chromatin. The loss of this gene results in abnormal angiogenesis and is associated with syndromic …

**Accessions** — [HGNC:24185](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24185) · Entrez [79184](https://www.ncbi.nlm.nih.gov/gene/79184) · UniProt [P46736](https://www.uniprot.org/uniprotkb/P46736) · Ensembl [ENSG00000185515](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185515)

## Data

Gene col 11692: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11692); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11692, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11692]; `tensor/DDL_lfc|DDL_z.npy` [11692]; `embed/gene_vectors.npy` [11692]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11692 or target_col == 11692). Every well: [[BRCC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRCC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
