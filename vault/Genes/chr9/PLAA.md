---
symbol: "PLAA"
type: "gene"
col: 5960
ensembl_id: "ENSG00000137055"
name: "phospholipase A2 activating protein"
location: "9p21.2"
module: 72
arm: "+"
pooled_cpm: 46.31
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# PLAA

*phospholipase A2 activating protein* — 9p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 3.69× (z +25.0, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.567× (z -15.4, q 0e+00, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD13]] (+0.68, fdr 7e-06), [[PSMB3]] (+0.66, fdr 7e-06), [[PSMB2]] (+0.66, fdr 7e-06); moves opposite to [[PCID2]] (-0.54, fdr 4e-05), [[SNAPC1]] (-0.54, fdr 1e-05), [[EP300]] (-0.50, fdr 7e-04).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5960.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.69×** | +25.0 | 0e+00 | 47/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.67×** | +24.9 | 0e+00 | 47/47 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.30×** | +21.6 | 0e+00 | 47/47 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.45×** | +12.4 | 5e-33 | 44/48 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.18×** | +10.7 | 2e-24 | 45/47 (LOX-IMVI, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.33×** | +8.5 | 2e-15 | 32/47 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.18×** | +7.8 | 5e-13 | 36/42 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +7.7 | 1e-12 | 31/47 (COLO 205, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +5.6 | 1e-06 | 26/47 (NCI-H460, LS 180, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +5.3 | 6e-06 | 24/47 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +5.3 | 6e-06 | 23/47 (NCI-H460, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.20× | +4.9 | 4e-05 | 20/47 (PANC-1, LS 180, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **1.30×** | +4.8 | 7e-05 | 20/47 (LoVo, COLO 205, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.20×** | +3.5 | 0.017 | 22/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.20×** | +3.5 | 0.018 | 22/47 (NCI-H460, LS 180, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5960.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.567×** | -15.4 | 0e+00 | 40/47 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.538×** | -11.4 | 8e-28 | 29/40 (Panc 03.27, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.561×** | -11.1 | 2e-26 | 31/44 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.789×** | -6.4 | 2e-08 | 31/47 (LS 180, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.748×** | -5.6 | 3e-06 | 26/47 (Hs 766T, A-427, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.766×** | -5.1 | 3e-05 | 21/47 (SW48, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.806×** | -4.2 | 0.003 | 19/47 (AN3 CA, A498, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -4.0 | 0.005 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.873× | -3.7 | 0.012 | 15/47 (A-427, HS-578T, …) | all doses, flat | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.827×** | -3.7 | 0.014 | 21/47 (A498, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.774×** | -3.5 | 0.022 | 19/47 (AsPC-1, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.848× | -3.2 | 0.070 | 11/47 (RPMI-7951, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.852× | -3.1 | 0.088 | 15/47 (HOP62, LoVo, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.855× | -3.0 | 0.10 | 15/47 (KATO III, RKO, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5960. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 154 | 2 | 6 (4 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.43× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -31.1) |
| [[LS 180 (line)]] | wt | 60.4 | 5 (2 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 5.30× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.170× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 43.1 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.39× (z +16.7) | — |
| [[HS-578T (line)]] | alt | 57.4 | 2 | 4 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.87× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 55.5 | 4 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.37× (z +15.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -11.3) |
| [[SW480 (line)]] | alt | 42.6 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.26× (z +19.8) | — |
| [[A549 (line)]] | wt | 58.0 | 3 | 2 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.22× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 35.0 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.69× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.201× (z -13.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 40.6 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.56× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -10.4) |
| [[Hs 766T (line)]] | wt | 61.7 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.54× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 0.5 µM 0.360× (z -8.8) |
| [[SNU-423 (line)]] | alt | 34.5 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.72× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.352× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -8.8) |
| [[A-172 (line)]] | wt | 48.0 | 3 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.80× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -15.7) |
| [[A-427 (line)]] | wt | 46.3 | 1 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.90× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -18.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 51.0 | 1 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.59× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0856× (z -17.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 23.7 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 4.23× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 34.5 | 3 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 5.88× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -9.5) |
| [[J82 (line)]] | alt | 65.3 | 1 | 3 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.34× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -13.7) |
| [[KATO III (line)]] | alt | 38.8 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.91× (z +14.0) | — |
| [[LoVo (line)]] | wt | 46.9 | 3 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 4.59× (z +17.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -13.8) |
| [[Panc 03.27 (line)]] | alt | 45.7 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.36× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.0973× (z -18.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 72.1 | 3 | 1 | [[Bortezomib (drug)]] 0.05 µM 3.30× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -8.7) |
| [[SW 900 (line)]] | alt | 64.3 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.03× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -9.3) |
| [[COLO 205 (line)]] | alt | 22.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 9.17× (z +12.1) | — |
| [[HCT15 (line)]] | alt | 35.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.27× (z +10.4) | — |
| [[HepG2_C3A (line)]] | wt | 37.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.73× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 38.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.93× (z +14.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 36.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.88× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 26.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.88× (z +13.7) | — |
| [[PANC-1 (line)]] | alt | 19.2 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.26× (z +14.1) | — |
| [[SNU-1 (line)]] | wt | 61.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.96× (z +11.6) | — |
| [[SW1417 (line)]] | alt | 52.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.18× (z +10.1) | — |
| [[C32 (line)]] | wt | 21.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.95× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 38.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.89× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 72.7 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.06× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -9.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 35.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.80× (z +10.4) | — |
| [[SW48 (line)]] | wt | 61.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.89× (z +11.8) | — |
| [[AN3 CA (line)]] | alt | 88.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -9.1) ⚠ cell-cycle shift, explains ~19% of this change |
| [[AsPC-1 (line)]] | alt | 25.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -13.0) |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0572× (z -14.9) |
| [[CHP-212 (line)]] | wt | 52.5 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 0.5 µM 0.154× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 15.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.38× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 22.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.41× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 34.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[SHP-77 (line)]] | alt | 59.4 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.78× (z +8.9) | — |
| [[H4 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.70 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 42.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5960), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD13]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[PSMB3]] | +0.66 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[PSMB2]] | +0.66 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[SLC10A7]] | +0.65 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[TALDO1]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[HERC2P2]] | +0.65 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[HERC2P3]] | +0.65 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[USP14]] | +0.65 | +0.73 / +0.59 | both halves | 7e-06 | STRING 687 |
| [[ANKRD39]] | +0.65 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[ZW10]] | +0.65 | +0.72 / +0.43 | both halves | 3e-05 |  |
| [[TANGO2]] | +0.64 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[TXNL1]] | +0.64 | +0.67 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCID2]] | -0.54 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[SNAPC1]] | -0.54 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[EP300]] | -0.50 | -0.57 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.5, -8.5); signed map (-27.8, -25.1). **Vector** length 99.6, 27.2% of its response variance represented; |z| ≥ 3 in 1,148 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Degradation of DVL* (reactome, mean cos +0.53 to 12); *proteasome* (control, mean cos +0.55 to 11); *NIK-->noncanonical NF-kB signaling* (reactome, mean cos +0.53 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.7 | +25.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.6 | +24.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.8 | +21.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.8 | +7.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.4 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +7.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.8 | -0.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.6 | -1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -15.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -4.9 | +5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -4.7 | +3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -1.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -4.1 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase A2 activating protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.2 — chr9:26,903,372-26,947,242 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PLAP, PLA2P, FLJ11281, FLJ12699, DOA1 |
| Gene groups (HGNC) | WD repeat domain containing; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y263](https://www.uniprot.org/uniprotkb/Q9Y263) (Phospholipase A-2-activating protein):

> Plays a role in protein ubiquitination, sorting and degradation through its association with VCP. Involved in ubiquitin-mediated membrane proteins trafficking to late endosomes in an ESCRT-dependent manner, and hence plays a role in synaptic vesicle recycling (By similarity). May play a role in macroautophagy, regulating for instance the clearance of damaged lysosomes. Plays a role in cerebellar Purkinje cell development (By similarity). Positively regulates cytosolic and calcium-independent …

**Summary**, from NCBI Gene [9373](https://www.ncbi.nlm.nih.gov/gene/9373):

> Enables phospholipase A2 activator activity. Involved in cellular response to lipopolysaccharide and macroautophagy. Located in several cellular components, including cytosol; extracellular exosome; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9043](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9043) · Entrez [9373](https://www.ncbi.nlm.nih.gov/gene/9373) · UniProt [Q9Y263](https://www.uniprot.org/uniprotkb/Q9Y263) · Ensembl [ENSG00000137055](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137055)

## Data

Gene col 5960: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5960); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5960, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5960]; `tensor/DDL_lfc|DDL_z.npy` [5960]; `embed/gene_vectors.npy` [5960]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5960 or target_col == 5960). Every well: [[PLAA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLAA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
