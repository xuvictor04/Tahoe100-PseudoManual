---
symbol: "PLD3"
type: "gene"
col: 2565
ensembl_id: "ENSG00000105223"
name: "phospholipase D family member 3"
location: "19q13.2"
module: 30
arm: "+"
pooled_cpm: 59.55
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 22
n_dd_up_clean: 10
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# PLD3

*phospholipase D family member 3* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.91× (z +13.1, q 2e-36, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.423× (z -24.7, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LCMT1]] (+0.72, fdr 1e-05), [[MGST3]] (+0.72, fdr 7e-06), [[RRAS]] (+0.72, fdr 1e-05); moves opposite to [[CPSF2]] (-0.68, fdr 7e-06), [[CYREN]] (-0.66, fdr 1e-05), [[HNRNPA2B1]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2565.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.91×** | +13.1 | 2e-36 | 41/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +13.1 | 2e-36 | 43/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +9.1 | 2e-17 | 35/48 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +6.7 | 3e-09 | 30/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +4.8 | 2e-04 | 24/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +4.7 | 3e-04 | 27/49 (KATO III, LS 180, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.25×** | +4.5 | 5e-04 | 24/48 (A498, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +4.4 | 1e-03 | 24/48 (KATO III, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.20× | +4.2 | 0.002 | 17/48 (A-427, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.008 | 20/49 (NCI-H23, MIA PaCa-2, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.21×** | +3.8 | 0.008 | 21/47 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.19× | +3.7 | 0.010 | 18/49 (SW480, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.010 | 18/49 (NCI-H23, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.6 | 0.013 | 10/48 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.017 | 17/47 (NCI-H2030, A-172, …) | rises with dose | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.019 | 19/48 (NCI-H1573, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.032 | 14/48 (KATO III, HOP62, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.078 | 11/48 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2565.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.423×** | -24.7 | 0e+00 | 43/48 (SW 900, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.364×** | -19.7 | 0e+00 | 45/48 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.384×** | -19.4 | 0e+00 | 41/48 (HS-578T, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.422×** | -17.5 | 0e+00 | 44/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.483×** | -14.8 | 0e+00 | 42/48 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.498×** | -14.1 | 2e-43 | 41/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.507×** | -13.8 | 3e-41 | 42/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.552×** | -12.1 | 1e-31 | 40/48 (SW480, SW 1088, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.573×** | -10.9 | 1e-25 | 40/47 (RPMI-7951, J82, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.645×** | -8.9 | 4e-17 | 35/48 (A549, A498, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.505×** | -7.2 | 2e-11 | 38/49 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.537×** | -6.6 | 2e-09 | 31/48 (RKO, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.737×** | -6.2 | 3e-08 | 28/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.740×** | -6.1 | 4e-08 | 29/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.814×** | -5.9 | 1e-07 | 26/48 (NCI-H460, NCI-H1792, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.775×** | -4.8 | 6e-05 | 24/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.817×** | -4.1 | 0.001 | 20/48 (SW1417, A498, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.687×** | -4.0 | 0.002 | 20/48 (Panc 03.27, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pimozide (drug)]] 5 µM |  | 0.839× | -3.6 | 0.009 | 12/48 (NCI-H1573, NCI-H460, …) | top dose only | position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.845× | -3.3 | 0.026 | 16/49 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2565. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 61.9 | 3 | 8 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.89× (z +13.3) | [[Digitoxin (drug)]] 5 µM 0.208× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.248× (z -17.4) |
| [[NCI-H460 (line)]] | wt | 39.0 | 2 | 8 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +9.9) | [[Harringtonine (drug)]] 0.5 µM 0.354× (z -11.3) |
| [[A549 (line)]] | wt | 105 | 2 | 7 | [[Panobinostat (drug)]] 0.5 µM 2.56× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -22.2) |
| [[HOP62 (line)]] | alt | 83.2 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -25.2) |
| [[HS-578T (line)]] | alt | 88.6 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -26.0) |
| [[C32 (line)]] | wt | 49.9 | 0 | 7 | — | [[Harringtonine (drug)]] 0.5 µM 0.215× (z -13.1) |
| [[H4 (line)]] | wt | 60.3 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -12.2) |
| [[hTERT-HPNE (line)]] | wt | 62.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -15.2) |
| [[NCI-H1792 (line)]] | alt | 99.4 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -18.2) |
| [[SNU-423 (line)]] | alt | 58.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -23.0) |
| [[HT-29 (line)]] | alt | 65.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -13.9) |
| [[KATO III (line)]] | alt | 63.1 | 3 | 3 | [[Panobinostat (drug)]] 5 µM 2.69× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -10.8) |
| [[LoVo (line)]] | wt | 41.0 | 1 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.53× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -10.9) |
| [[LS 180 (line)]] | wt | 61.8 | 1 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.30× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -13.1) |
| [[Panc 03.27 (line)]] | alt | 58.7 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.173× (z -17.0) |
| [[RPMI-7951 (line)]] | alt | 89.4 | 0 | 6 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.178× (z -16.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -16.6) |
| [[SW 900 (line)]] | alt | 88.5 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -28.1) |
| [[A-172 (line)]] | wt | 126 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -18.6) |
| [[A498 (line)]] | wt | 39.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -16.0) |
| [[HCT15 (line)]] | alt | 90.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 71.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -16.2) |
| [[NCI-H23 (line)]] | alt | 60.2 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.376× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 39.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -18.8) |
| [[BT-474 (line)]] | alt | 47.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 59.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -17.4) |
| [[PANC-1 (line)]] | alt | 44.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -19.2) |
| [[HEC-1-A (line)]] | alt | 79.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -17.4) |
| [[SW 1088 (line)]] | alt | 129 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0617× (z -11.8) |
| [[SW1417 (line)]] | alt | 35.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -16.7) |
| [[J82 (line)]] | alt | 41.7 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.271× (z -12.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.538× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 83.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -13.3) |
| [[SK-MEL-2 (line)]] | alt | 30.2 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.0420× (z -11.7) |
| [[SNU-1 (line)]] | wt | 37.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.103× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 35.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -12.2) |
| [[CHP-212 (line)]] | wt | 68.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[COLO 205 (line)]] | alt | 54.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.292× (z -9.0) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 54.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -10.2) |
| [[NCI-H596 (line)]] | alt | 54.7 | 1 | 0 | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 1.88× (z +8.7) | — |
| [[RKO (line)]] | wt | 35.5 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0959× (z -9.2) |
| [[SW 1271 (line)]] | alt | 52.5 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.05 µM 0.0435× (z -11.3) |
| [[A-427 (line)]] | wt | 52.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2565), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCMT1]] | +0.72 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[MGST3]] | +0.72 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[RRAS]] | +0.72 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[MYPOP]] | +0.71 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[ARPC1A]] | +0.70 | +0.59 / +0.57 | both halves | 9e-06 | pathway: Fcgamma receptor (FCGR) dependent phagocytosis |
| [[SEZ6L2]] | +0.70 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[CRYZL1]] | +0.70 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[UNC45A]] | +0.69 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[RNF41]] | +0.69 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[TSC2]] | +0.69 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[SLC17A5]] | +0.69 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[SLC27A1]] | +0.68 | +0.60 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF2]] | -0.68 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[CYREN]] | -0.66 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[HNRNPA2B1]] | -0.66 | -0.70 / -0.58 | both halves | 7e-06 |  |
| [[HNRNPK]] | -0.66 | -0.61 / -0.61 | both halves | 7e-06 | same gene group |
| [[TASOR]] | -0.65 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[ST7L]] | -0.65 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[E2F3]] | -0.64 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[GEN1]] | -0.64 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[FAM111A]] | -0.64 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[PRDM5]] | -0.63 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[USP13]] | -0.63 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[TFAM]] | -0.63 | -0.61 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.765). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.6, -4.2); signed map (-35.3, -1.2). **Vector** length 101, 30.0% of its response variance represented; |z| ≥ 3 in 1,263 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.1 | +13.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +13.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.1 | +9.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +1.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | -1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.9 | +4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.3 | +0.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -8.1 | -5.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.7 | -14.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.3 | -19.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.9 | -8.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.2 | -19.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.6 | -4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.9 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase D family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:40,348,456-40,389,472 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HU-K4 |
| Gene groups (HGNC) | Phospholipases; MicroRNA protein coding host genes |
| Reactome | 7 pathways, smallest: Synthesis of PG; Role of phospholipids in phagocytosis; Fcgamma receptor (FCGR) dependent phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IV08](https://www.uniprot.org/uniprotkb/Q8IV08) (5'-3' exonuclease PLD3):

> Lysosomal 5'->3' exonuclease that functions in nucleic-acid sensing by immune cells. Hydrolyzes phosphodiester bond in single-stranded RNA and DNA molecules, with a higher efficiency for molecules with 5' uridine and guanosine residues. It can stall at certain sites and does not necessarily proceed to complete exonucleolytic degradation, thereby producing nucleoside 3'-monophosphates but also 5'-end 5'-hydroxy deoxyribonucleotide/ribonucleotide fragments. Through the processing of self and …

**Summary**, from NCBI Gene [23646](https://www.ncbi.nlm.nih.gov/gene/23646):

> This gene encodes a member of the phospholipase D (PLD) family of enzymes that catalyze the hydrolysis of membrane phospholipids. The encoded protein is a single-pass type II membrane protein and contains two PLD phosphodiesterase domains. This protein influences processing of amyloid-beta precursor protein. Mutations in this gene are associated with Alzheimer disease risk. Alternatively spliced transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, …

**Accessions** — [HGNC:17158](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17158) · Entrez [23646](https://www.ncbi.nlm.nih.gov/gene/23646) · UniProt [Q8IV08](https://www.uniprot.org/uniprotkb/Q8IV08) · Ensembl [ENSG00000105223](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105223)

## Data

Gene col 2565: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2565); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2565, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2565]; `tensor/DDL_lfc|DDL_z.npy` [2565]; `embed/gene_vectors.npy` [2565]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2565 or target_col == 2565). Every well: [[PLD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
