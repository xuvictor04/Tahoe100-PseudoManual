---
symbol: "CRTAP"
type: "gene"
col: 9927
ensembl_id: "ENSG00000170275"
name: "cartilage associated protein"
location: "3p22.3"
module: 29
arm: "+"
pooled_cpm: 51.6
n_lines_expressing: 46
n_dd_up: 5
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 8
direction_downstream: 25
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# CRTAP

*cartilage associated protein* — 3p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.75× (z +25.1, q 0e+00, up in 42 of 42 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (A498 4.10×, HOP62 4.47×, NCI-H460 3.54×, SW480 4.27×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (A-172 4.44×, A498 3.51×, HOP62 4.03×, SW480 4.44×, …; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 1.70×).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.333× (z -29.5, q 0e+00, down in 44 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPT1]] (+0.82, fdr 7e-06), [[FKBP9]] (+0.81, fdr 7e-06), [[STT3B]] (+0.75, fdr 7e-06); moves opposite to [[MED18]] (-0.69, fdr 7e-06), [[ZNF593]] (-0.68, fdr 7e-06), [[H3-3B]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[FHL1]] → it (grade B ⚠); 25 go from it, the strongest it → [[RPSA]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 8 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9927.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (A498 4.10×, HOP62 4.47×, NCI-H460 3.54×, SW480 4.27×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (A-172 4.44×, A498 3.51×, HOP62 4.03×, SW480 4.44×, …; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 1.70×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.75×** | +25.1 | 0e+00 | 42/42 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.67×** | +23.8 | 0e+00 | 38/38 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.68×** | +17.3 | 0e+00 | 37/40 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.5 | 1e-03 | 14/33 (HOP62, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.21×** | +3.7 | 0.026 | 19/44 (HS-578T, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.20× | +3.4 | 0.059 | 14/44 (NCI-H460, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.3 | 0.067 | 0/44 | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.20× | +3.3 | 0.067 | 17/44 (A-172, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9927.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.333×** | -29.5 | 0e+00 | 44/44 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.309×** | -22.3 | 0e+00 | 44/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.489×** | -13.1 | 1e-36 | 38/44 (LOX-IMVI, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.676×** | -7.4 | 1e-11 | 28/44 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.711×** | -6.5 | 1e-08 | 27/44 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.721×** | -6.2 | 5e-08 | 29/44 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.731×** | -5.9 | 2e-07 | 26/44 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.750×** | -5.5 | 3e-06 | 29/44 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.781×** | -4.7 | 2e-04 | 21/44 (A-427, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.840× | -3.3 | 0.049 | 18/44 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.834× | -3.3 | 0.049 | 12/43 (A549, NCI-H2030, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9927. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 98.5 | 7 (7 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +16.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -23.7) |
| [[SW480 (line)]] | alt | 37.6 | 3 (3 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +15.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -23.3) |
| [[A-172 (line)]] | wt | 91.2 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.44× (z +17.2) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.70× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 47.4 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +14.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -18.2) |
| [[NCI-H2347 (line)]] | alt | 69.8 | 4 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -14.8) |
| [[HOP62 (line)]] | alt | 79.9 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +17.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -20.3) |
| [[HS-578T (line)]] | alt | 75.5 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +12.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.248× (z -13.6) |
| [[LoVo (line)]] | wt | 32.4 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.30× (z +13.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -13.6) |
| [[LOX-IMVI (line)]] | wt | 64.7 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +13.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -22.0) |
| [[LS 180 (line)]] | wt | 25.8 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -25.3) |
| [[MIA PaCa-2 (line)]] | alt | 43.9 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.79× (z +13.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -15.6) |
| [[NCI-H2030 (line)]] | alt | 53.6 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.41× (z +14.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -18.0) |
| [[SNU-423 (line)]] | alt | 81.4 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +15.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -10.7) |
| [[SW 900 (line)]] | alt | 26.7 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 6.39× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -13.1) |
| [[A498 (line)]] | wt | 81.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +19.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.534× (z -8.7) |
| [[A549 (line)]] | wt | 66.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.30× (z +15.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -11.0) |
| [[Hs 766T (line)]] | wt | 67.0 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +14.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -18.3) |
| [[J82 (line)]] | alt | 65.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -15.8) |
| [[KATO III (line)]] | alt | 24.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +11.0) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.244× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 40.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -18.8) |
| [[PANC-1 (line)]] | alt | 38.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +14.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -18.1) |
| [[SK-MEL-2 (line)]] | alt | 86.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +13.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -13.1) |
| [[SNU-1 (line)]] | wt | 93.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -23.0) |
| [[SW1417 (line)]] | alt | 43.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -16.2) |
| [[C32 (line)]] | wt | 83.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +13.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 19.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.85× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -9.1) |
| [[H4 (line)]] | wt | 75.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.80× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -17.0) |
| [[HCT15 (line)]] | alt | 30.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.01× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 51.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.68× (z +15.4) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 81.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -9.9) |
| [[A-427 (line)]] | wt | 40.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -17.0) |
| [[AsPC-1 (line)]] | alt | 17.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.78× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -11.0) |
| [[CHP-212 (line)]] | wt | 63.9 | 0 | 2 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.111× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 87.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -12.3) |
| [[RKO (line)]] | wt | 34.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -16.9) |
| [[RPMI-7951 (line)]] | alt | 81.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -15.7) |
| [[SW 1088 (line)]] | alt | 63.5 | 0 | 2 | — | [[Estrone sulfate (potassium) (drug)]] 5 µM 0.0513× (z -9.6) |
| [[SW48 (line)]] | wt | 45.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -9.0) |
| [[C-33 A (line)]] | alt | 33.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 27.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -9.3) |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -10.3) |
| [[SHP-77 (line)]] | alt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -15.0) |
| [[AN3 CA (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9927), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPT1]] | +0.82 | +0.84 / +0.75 | both halves | 7e-06 |  |
| [[FKBP9]] | +0.81 | +0.78 / +0.78 | both halves | 7e-06 |  |
| [[STT3B]] | +0.75 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[PRDX3]] | +0.75 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[ERMP1]] | +0.73 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[TXNDC5]] | +0.72 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[RPN1]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[FUCA2]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[CTSZ]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[EEF1A1]] | +0.70 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[SELENON]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[IPO5]] | +0.69 | +0.62 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED18]] | -0.69 | -0.72 / -0.68 | both halves | 7e-06 |  |
| [[ZNF593]] | -0.68 | -0.61 / -0.72 | both halves | 7e-06 |  |
| [[H3-3B]] | -0.68 | -0.70 / -0.63 | both halves | 7e-06 |  |
| [[EID2]] | -0.67 | -0.57 / -0.75 | both halves | 9e-06 |  |
| [[CROCCP2-1]] | -0.67 | -0.68 / -0.65 | both halves | 7e-06 |  |
| [[MRPS18C]] | -0.66 | -0.61 / -0.68 | both halves | 7e-06 |  |
| [[ZNF75A]] | -0.66 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[CCDC174]] | -0.66 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[SURF6]] | -0.65 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[MED19]] | -0.65 | -0.69 / -0.58 | both halves | 8e-06 |  |
| [[NSRP1]] | -0.65 | -0.72 / -0.58 | both halves | 7e-06 |  |
| [[PPP1R35]] ⚠ | -0.65 | -0.57 / -0.69 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[FBXL6]] | -0.64 | -0.57 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FHL1]] | B | FHL1 activity raises CRTAP's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 2.07× lower at baseline in the lines without FHL1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[ANXA6]] | B | ANXA6 activity raises CRTAP's level | lines that do not express ANXA6 (8) vs lines expressing it (42) | 2.09× lower at baseline in the lines without ANXA6 | 0.009 | ⚠ within organs, on part of the lines; also absent: KATNAL1, PHC1, FAM171A1 |
| [[SCARA3]] | B | SCARA3 activity raises CRTAP's level | lines that do not express SCARA3 (19) vs lines expressing it (31) | 1.62× lower at baseline in the lines without SCARA3 | 0.041 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SHISAL1, C5orf46 |
| [[TYMP]] | B | TYMP activity lowers CRTAP's level | lines that do not express TYMP (20) vs lines expressing it (30) | 1.47× higher at baseline in the lines without TYMP | 0.041 | ⚠ within organs, on part of the lines; also absent: ODF3B, CGAS, CCL20 |
| [[HDAC6]] | B | HDAC6 activity raises CRTAP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MYL9]] | B | MYL9 activity raises CRTAP's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.51× lower at baseline in the lines without MYL9 | 0.071 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[CPVL]] | B | CPVL activity lowers CRTAP's level | lines that do not express CPVL (21) vs lines expressing it (29) | 1.32× higher at baseline in the lines without CPVL | 0.075 | ⚠ within organs, on part of the lines; also absent: CHN2, PTPRR, BBOX1-AS1 |
| [[CNN3]] | B | CNN3 activity raises CRTAP's level | lines that do not express CNN3 (5) vs lines expressing it (45) | 2.15× lower at baseline in the lines without CNN3 | 0.086 | ⚠ within organs, on part of the lines; also absent: SLC9A9, SLC35F1, CNN3-DT |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 0, C 25. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPSA]] | C | CRTAP activity raises RPSA's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.82× lower at baseline in the lines without CRTAP | 0.015 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |
| [[FUCA2]] | C | CRTAP activity raises FUCA2's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 2.24× lower at baseline in the lines without CRTAP | 0.015 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |
| [[TUBB]] | C | CRTAP activity raises TUBB's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 2.24× lower at baseline in the lines without CRTAP | 0.016 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |
| [[PRDX3]] | C | CRTAP activity raises PRDX3's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.79× lower at baseline in the lines without CRTAP | 0.021 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |
| [[TMEM109]] | C | CRTAP activity raises TMEM109's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.83× lower at baseline in the lines without CRTAP | 0.022 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |
| [[YWHAQ]] | C | CRTAP activity raises YWHAQ's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.57× lower at baseline in the lines without CRTAP | 0.025 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |
| [[PRPF8]] | C | CRTAP activity raises PRPF8's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.60× lower at baseline in the lines without CRTAP | 0.030 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |
| [[SELENON]] | C | CRTAP activity raises SELENON's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 2.61× lower at baseline in the lines without CRTAP | 0.033 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent; co-absent with the target |
| [[CNPY3]] | C | CRTAP activity raises CNPY3's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.70× lower at baseline in the lines without CRTAP | 0.042 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |
| [[CCNG1]] | C | CRTAP activity raises CCNG1's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.93× lower at baseline in the lines without CRTAP | 0.043 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |
| [[YBX1]] | C | CRTAP activity raises YBX1's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.67× lower at baseline in the lines without CRTAP | 0.044 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |
| [[RPL18A]] | C | CRTAP activity raises RPL18A's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.42× lower at baseline in the lines without CRTAP | 0.047 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.836). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.7, -22.0); signed map (-23.0, -38.6). **Vector** length 113, 31.0% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +17.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +23.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +25.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | -0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.5 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.1 | -22.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.7 | -13.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.7 | -7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -29.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.3 | -6.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cartilage associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.3 — chr3:33,114,014-33,147,773 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CASP, LEPREL3, P3H5 |
| Gene groups (HGNC) | Prolyl 3-hydroxylase family |
| Reactome | 3 pathways, smallest: Collagen biosynthesis and modifying enzymes; Collagen formation; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [O75718](https://www.uniprot.org/uniprotkb/O75718) (Cartilage-associated protein):

> Necessary for efficient 3-hydroxylation of fibrillar collagen prolyl residues.

**Summary**, from NCBI Gene [10491](https://www.ncbi.nlm.nih.gov/gene/10491):

> The protein encoded by this gene is similar to the chicken and mouse CRTAP genes. The encoded protein is a scaffolding protein that may influence the activity of at least one member of the cytohesin/ARNO family in response to specific cellular stimuli. Defects in this gene are associated with osteogenesis imperfecta, a connective tissue disorder characterized by bone fragility and low bone mass. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2379](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2379) · Entrez [10491](https://www.ncbi.nlm.nih.gov/gene/10491) · UniProt [O75718](https://www.uniprot.org/uniprotkb/O75718) · Ensembl [ENSG00000170275](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170275)

## Data

Gene col 9927: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9927); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9927, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9927]; `tensor/DDL_lfc|DDL_z.npy` [9927]; `embed/gene_vectors.npy` [9927]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9927 or target_col == 9927). Every well: [[CRTAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRTAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
