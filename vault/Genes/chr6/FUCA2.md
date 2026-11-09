---
symbol: "FUCA2"
type: "gene"
col: 5
ensembl_id: "ENSG00000001036"
name: "alpha-L-fucosidase 2"
location: "6q24.2"
module: 29
arm: "+"
pooled_cpm: 32.56
n_lines_expressing: 47
n_dd_up: 19
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# FUCA2

*alpha-L-fucosidase 2* — 6q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.41× (z +21.0, q 0e+00, up in 41 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.43× (z +5.1, q 2e-05, up in 28 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.566× (z -11.4, q 2e-27, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPT1]] (+0.82, fdr 7e-06), [[SUMO3]] (+0.77, fdr 7e-06), [[TMX1]] (+0.75, fdr 7e-06); moves opposite to [[NFKBIL1]] (-0.63, fdr 1e-05), [[MTRES1]] (-0.63, fdr 1e-05), [[INAFM1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADGRG6]] → it (grade B ⚠); 3 go from it, the strongest it → [[NNT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 16 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.41×** | +21.0 | 0e+00 | 41/42 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.97×** | +18.8 | 0e+00 | 36/38 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.77×** | +13.4 | 2e-38 | 39/41 (LS 180, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.75×** | +7.9 | 3e-13 | 38/45 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.64×** | +7.0 | 3e-10 | 33/45 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.60×** | +6.6 | 3e-09 | 34/43 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.47×** | +5.4 | 5e-06 | 30/45 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.44×** | +5.2 | 1e-05 | 25/43 (KATO III, CFPAC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +5.1 | 2e-05 | 28/44 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +4.7 | 1e-04 | 26/45 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +4.7 | 1e-04 | 26/45 (SW480, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +3.9 | 0.005 | 21/45 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.32×** | +3.8 | 0.006 | 22/45 (SNU-423, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.29×** | +3.6 | 0.011 | 19/45 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.28×** | +3.5 | 0.018 | 22/45 (SNU-423, KATO III, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.2 | 0.048 | 16/45 (HOP62, A-172, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.50×** | +3.0 | 0.069 | 10/44 (A498, C32, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.566×** | -11.4 | 2e-27 | 39/45 (H4, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.664×** | -5.8 | 2e-06 | 26/45 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.705×** | -4.9 | 1e-04 | 24/45 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.705×** | -4.9 | 1e-04 | 24/45 (SW480, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.731×** | -4.4 | 0.001 | 22/44 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.753×** | -4.0 | 0.005 | 19/45 (MIA PaCa-2, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ciclopirox (drug)]] 5 µM |  | **0.819×** | -4.0 | 0.005 | 20/45 (NCI-H1792, SW48, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.754×** | -4.0 | 0.005 | 19/45 (SW480, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.764×** | -3.7 | 0.015 | 23/44 (hTERT-HPNE, A498, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -3.4 | 0.042 | 1/45 (SW 1088) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.643×** | -3.3 | 0.056 | 15/44 (RKO, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.651×** | -3.2 | 0.070 | 13/44 (LoVo, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tadalafil (drug)]] 5 µM |  | **0.796×** | -3.1 | 0.085 | 8/44 (NCI-H2347, LoVo, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 43.3 | 4 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +11.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.263× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 35.1 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 5.28× (z +13.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 32.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.90× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -9.3) |
| [[A498 (line)]] | wt | 38.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +13.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 12.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.70× (z +9.4) ⚠ toxic; transcription drop | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.121× (z -10.5) |
| [[HS-578T (line)]] | alt | 51.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.99× (z +13.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 53.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +12.7) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 43.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.78× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -8.8) |
| [[LoVo (line)]] | wt | 27.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.12× (z +14.1) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.295× (z -9.8) |
| [[LS 180 (line)]] | wt | 40.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.30× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 32.2 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.4) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[NCI-H460 (line)]] | wt | 36.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -8.8) |
| [[PANC-1 (line)]] | alt | 23.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.26× (z +14.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 59.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +9.3) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.318× (z -9.0) |
| [[SNU-423 (line)]] | alt | 50.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +12.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 38.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.03× (z +14.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 18.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.49× (z +12.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 20.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.60× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 48.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.84× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 42.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +12.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 23.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.67× (z +12.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 29.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +11.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 11.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.10× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 16.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.8× (z +12.3) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 34.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.86× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 29.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.14× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -10.8) |
| [[SNU-1 (line)]] | wt | 68.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -22.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.324× (z -8.6) |
| [[SW 900 (line)]] | alt | 27.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -8.9) |
| [[SW1417 (line)]] | alt | 57.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 30.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +8.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 52.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 15.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +9.3) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 22.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +9.6) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 34.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 53.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 52.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +8.7) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 60.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.37 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPT1]] | +0.82 | +0.79 / +0.83 | both halves | 7e-06 |  |
| [[SUMO3]] | +0.77 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[TMX1]] | +0.75 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[PGRMC1]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[CRTAP]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[MOB1A]] | +0.69 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[TMX3]] | +0.69 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[RCN1]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation |
| [[PON2]] | +0.68 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[LAPTM4B]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CTSZ]] | +0.68 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[TSPAN6]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKBIL1]] | -0.63 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[MTRES1]] | -0.63 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.63 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[MED19]] | -0.62 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[NOSIP]] | -0.62 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[PPP1R35]] ⚠ | -0.61 | -0.51 / -0.65 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[FRG1]] | -0.61 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[NKAP]] | -0.61 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[PMM1]] | -0.60 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[CDKN2D]] | -0.60 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[ZFAND2B]] | -0.60 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[RGP1]] | -0.60 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[UBE2B]] | -0.60 | -0.59 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRG6]] | B | ADGRG6 activity lowers FUCA2's level | lines that do not express ADGRG6 (12) vs lines expressing it (38) | 1.74× higher at baseline in the lines without ADGRG6 | 0.060 | ⚠ within organs, on part of the lines; also absent: RHPN1, FAM83H, TNFRSF10A-DT |
| [[CRTAP]] | C | CRTAP activity raises FUCA2's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 2.24× lower at baseline in the lines without CRTAP | 0.015 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NNT]] | C | FUCA2 activity raises NNT's level | lines that do not express FUCA2 (3) vs lines expressing it (47) | 5.07× lower at baseline in the lines without FUCA2 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPX1, AIFM2, SP100; maybe low, not absent; its own permutation p |
| [[CDKN2D]] | C | FUCA2 activity raises CDKN2D's level | lines that do not express FUCA2 (3) vs lines expressing it (47) | 1.95× lower at baseline in the lines without FUCA2 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPX1, AIFM2, SP100; maybe low, not absent |
| [[HCFC1]] | C | FUCA2 activity lowers HCFC1's level | lines that do not express FUCA2 (3) vs lines expressing it (47) | 1.85× higher at baseline in the lines without FUCA2 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPX1, AIFM2, SP100; maybe low, not absent |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.798). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-27.3, -21.6); signed map (-21.4, -38.6). **Vector** length 90.5, 23.4% of its response variance represented; |z| ≥ 3 in 821 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +18.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +21.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +4.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -11.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -4.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.8 | -0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | alpha-L-fucosidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.2 — chr6:143,494,812-143,511,720 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC1314, dJ20N2.5 |
| Gene groups (HGNC) | Alpha-L-fucosidases |
| Reactome | 4 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs); Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTY2](https://www.uniprot.org/uniprotkb/Q9BTY2) (Plasma alpha-L-fucosidase):

> Alpha-L-fucosidase is responsible for hydrolyzing the alpha-1,6-linked fucose joined to the reducing-end N-acetylglucosamine of the carbohydrate moieties of glycoproteins.

**Summary**, from NCBI Gene [2519](https://www.ncbi.nlm.nih.gov/gene/2519):

> This gene encodes a plasma alpha-L-fucosidase, which represents 10-20% of the total cellular fucosidase activity. The protein is a member of the glycosyl hydrolase 29 family, and catalyzes the hydrolysis of the alpha-1,6-linked fucose joined to the reducing-end N-acetylglucosamine of the carbohydrate moieties of glycoproteins. This enzyme is essential for Helicobacter pylori adhesion to human gastric cancer cells. [provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:4008](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4008) · Entrez [2519](https://www.ncbi.nlm.nih.gov/gene/2519) · UniProt [Q9BTY2](https://www.uniprot.org/uniprotkb/Q9BTY2) · Ensembl [ENSG00000001036](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000001036)

## Data

Gene col 5: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5]; `tensor/DDL_lfc|DDL_z.npy` [5]; `embed/gene_vectors.npy` [5]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5 or target_col == 5). Every well: [[FUCA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FUCA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
