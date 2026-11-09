---
symbol: "PLD1"
type: "gene"
col: 1128
ensembl_id: "ENSG00000075651"
name: "phospholipase D1"
location: "3q26.31"
module: 167
arm: "+"
pooled_cpm: 174.08
n_lines_expressing: 43
n_dd_up: 12
n_dd_down: 57
n_dd_up_clean: 11
n_dd_down_clean: 36
in_vector_space: true
direction_upstream: 19
direction_downstream: 22
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# PLD1

*phospholipase D1* — 3q26.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.54× (z +9.0, q 2e-16, up in 31 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 57 drug-doses (21 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.217× (z -31.5, q 0e+00, down in 40 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCIM]] (+0.60, fdr 1e-05), [[AHR]] (+0.59, fdr 3e-05), [[LIFR]] (+0.59, fdr 1e-04); moves opposite to [[ASB1]] (-0.45, fdr 6e-05), [[PLEKHH1]] (-0.45, fdr 1e-04), [[ZNF783]] (-0.44, fdr 4e-05, ⚠ ZNF783 in the vector space only through flagged drug-doses), [[ADCY7]] (-0.43, fdr 2e-04).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[ATXN1]] → it (grade B ⚠); 22 go from it, the strongest it → [[DENR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1128.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +9.0 | 2e-16 | 31/41 (Panc 03.27, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +7.6 | 6e-12 | 33/42 (C32, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.64×** | +7.3 | 7e-11 | 28/43 (HOP62, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.51×** | +5.9 | 5e-07 | 25/40 (LOX-IMVI, A498, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.46×** | +5.6 | 3e-06 | 21/42 (HOP62, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.31×** | +5.5 | 3e-06 | 23/41 (HOP62, SW 900, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +5.5 | 4e-06 | 24/40 (A498, SW 900, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.95×** | +5.1 | 2e-05 | 26/43 (HOP62, SW 900, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.33×** | +5.1 | 2e-05 | 23/41 (LOX-IMVI, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.43×** | +5.1 | 2e-05 | 24/41 (SW 900, A498, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.003 | 22/41 (SW 900, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.033 | 18/42 (LOX-IMVI, SW 900, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 59 in all, 22 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 57 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1128.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.217×** | -31.5 | 0e+00 | 40/41 (SK-MEL-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.344×** | -21.9 | 0e+00 | 39/42 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.246×** | -19.6 | 0e+00 | 38/41 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.265×** | -19.3 | 0e+00 | 37/41 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.299×** | -17.5 | 0e+00 | 40/41 (SK-MEL-2, SW 900, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.322×** | -16.5 | 0e+00 | 35/41 (H4, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.332×** | -16.0 | 0e+00 | 36/41 (HepG2/C3A, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.337×** | -15.2 | 0e+00 | 37/40 (BT-474, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.354×** | -15.1 | 0e+00 | 35/41 (HepG2/C3A, H4, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.347×** | -14.8 | 0e+00 | 30/38 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.380×** | -14.0 | 5e-43 | 38/41 (HepG2/C3A, SW 900, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.374×** | -13.7 | 3e-41 | 37/40 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.362×** | -13.6 | 1e-40 | 35/38 (SNU-423, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.414×** | -12.8 | 7e-36 | 35/41 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.422×** | -12.5 | 2e-34 | 37/41 (HepG2/C3A, SW 900, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.451×** | -11.6 | 2e-29 | 35/41 (SK-MEL-2, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.440×** | -11.2 | 9e-28 | 36/41 (NCI-H460, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.510×** | -9.6 | 3e-20 | 34/41 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.331×** | -8.4 | 1e-15 | 36/42 (SK-MEL-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.684×** | -7.8 | 2e-13 | 32/41 (SK-MEL-2, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.399×** | -7.0 | 7e-11 | 35/41 (NCI-H1792, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.424×** | -6.5 | 1e-09 | 33/41 (NCI-H1792, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.448×** | -6.1 | 2e-08 | 30/41 (NCI-H1792, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.662×** | -5.9 | 5e-08 | 26/41 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.66 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1128. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 435 | 0 | 27 (15 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0625× (z -31.4) |
| [[NCI-H1792 (line)]] | alt | 450 | 0 | 25 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -26.8) |
| [[SK-MEL-2 (line)]] | alt | 498 | 0 | 24 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0746× (z -39.4) |
| [[SW 900 (line)]] | alt | 305 | 1 (1 ⚠) | 22 (13 ⚠) | [[Trametinib (drug)]] 5 µM 2.47× (z +8.8) ⚠ cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -27.6) |
| [[BT-474 (line)]] | alt | 171 | 0 | 22 (13 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0150× (z -27.2) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.0896× (z -16.2) |
| [[H4 (line)]] | wt | 359 | 0 | 21 (13 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0470× (z -20.3) |
| [[SNU-423 (line)]] | alt | 491 | 0 | 20 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0837× (z -29.2) |
| [[hTERT-HPNE (line)]] | wt | 266 | 0 | 19 (10 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0961× (z -18.6) |
| [[HepG2_C3A (line)]] | wt | 329 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -26.2) |
| [[PANC-1 (line)]] | alt | 183 | 0 | 18 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -32.1) |
| [[RPMI-7951 (line)]] | alt | 278 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0989× (z -26.6) |
| [[A549 (line)]] | wt | 304 | 0 | 17 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0415× (z -37.8) |
| [[HOP62 (line)]] | alt | 237 | 2 (2 ⚠) | 15 (8 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.60× (z +13.0) ⚠ position not correctable | [[Auranofin (drug)]] 5 µM 0.134× (z -15.6) |
| [[C32 (line)]] | wt | 179 | 1 | 15 (7 ⚠) | [[Tucidinostat (drug)]] 0.5 µM 2.52× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -19.1) |
| [[CFPAC-1 (line)]] | alt | 220 | 0 | 16 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0801× (z -27.2) |
| [[COLO 205 (line)]] | alt | 228 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -25.7) |
| [[Panc 03.27 (line)]] | alt | 132 | 1 | 13 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.86× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -23.6) |
| [[A-172 (line)]] | wt | 283 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -26.2) |
| [[NCI-H1573 (line)]] | alt | 133 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0751× (z -32.5) |
| [[SW480 (line)]] | alt | 62.9 | 0 | 12 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.243× (z -14.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.256× (z -12.9) |
| [[Hs 766T (line)]] | wt | 83.0 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -25.1) |
| [[KATO III (line)]] | alt | 130 | 0 | 11 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -17.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.308× (z -16.5) |
| [[HT-29 (line)]] | alt | 175 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -22.2) |
| [[LoVo (line)]] | wt | 82.4 | 0 | 9 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.217× (z -16.0) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.465× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 83.9 | 1 (1 ⚠) | 8 (2 ⚠) | [[Trametinib (drug)]] 5 µM 3.05× (z +8.7) ⚠ cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -19.3) |
| [[SW1417 (line)]] | alt | 127 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -25.4) |
| [[J82 (line)]] | alt | 122 | 0 | 7 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.250× (z -12.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.357× (z -9.4) |
| [[LS 180 (line)]] | wt | 155 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -17.0) |
| [[NCI-H2030 (line)]] | alt | 211 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.155× (z -14.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 111 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.121× (z -15.7) |
| [[HS-578T (line)]] | alt | 165 | 0 | 6 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.119× (z -13.1) |
| [[NCI-H2347 (line)]] | alt | 94.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -19.8) |
| [[A498 (line)]] | wt | 98.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -16.6) |
| [[HEC-1-A (line)]] | alt | 48.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -13.6) |
| [[SHP-77 (line)]] | alt | 67.3 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.200× (z -12.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H661 (line)]] | alt | 340 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.141× (z -11.1) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -10.5) |
| [[SW 1088 (line)]] | alt | 208 | 0 | 2 | — | [[Dexamethasone (drug)]] 0.5 µM 0.0424× (z -12.2) |
| [[A-427 (line)]] | wt | 80.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[AN3 CA (line)]] | alt | 56.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -9.2) |
| [[NCI-H2122 (line)]] | alt | 231 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0475× (z -8.9) |
| [[SW 1271 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0599× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[C-33 A (line)]] | alt | 22.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[NCI-H23 (line)]] | alt | 40.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 29.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 36.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1128), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCIM]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[AHR]] | +0.59 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[LIFR]] | +0.59 | +0.36 / +0.62 | both halves | 1e-04 |  |
| [[CYP1B1]] | +0.58 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[FBXO32]] | +0.58 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[KYNU]] | +0.57 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[EDIL3]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PTGES]] | +0.54 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[CSGALNACT1]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[GBP2]] | +0.54 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[DPYD]] | +0.53 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[BICC1]] | +0.53 | +0.40 / +0.49 | both halves | 5e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASB1]] | -0.45 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[PLEKHH1]] | -0.45 | -0.41 / -0.36 | both halves | 1e-04 | same gene group |
| [[ZNF783]] ⚠ | -0.44 | -0.43 / -0.42 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ADCY7]] | -0.43 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[DCTD]] | -0.42 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[ITPKB]] | -0.42 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[CRACR2A]] | -0.41 | -0.29 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 17, C 2. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATXN1]] | B | ATXN1 activity raises PLD1's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 4.40× lower at baseline in the lines without ATXN1 | 0.002 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[TNS3]] | B | TNS3 activity raises PLD1's level | lines that do not express TNS3 (8) vs lines expressing it (42) | 3.15× lower at baseline in the lines without TNS3 | 0.002 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[SYTL2]] | B | SYTL2 activity raises PLD1's level | lines that do not express SYTL2 (7) vs lines expressing it (43) | 3.87× lower at baseline in the lines without SYTL2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent |
| [[NEDD9]] | B | NEDD9 activity raises PLD1's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 2.45× lower at baseline in the lines without NEDD9 | 0.007 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[MAP2K1]] | B | MAP2K1 activity lowers PLD1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TEX41]] | B | TEX41 activity raises PLD1's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 2.57× lower at baseline in the lines without TEX41 | 0.025 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12 |
| [[ZEB2]] | B | ZEB2 activity raises PLD1's level | lines that do not express ZEB2 (27) vs lines expressing it (23) | 2.58× lower at baseline in the lines without ZEB2 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADAM12, LINC01583, PRR16 |
| [[KYNU]] | B | KYNU activity raises PLD1's level | lines that do not express KYNU (29) vs lines expressing it (21) | 2.67× lower at baseline in the lines without KYNU | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[LINC00511]] | B | LINC00511 activity raises PLD1's level | lines that do not express LINC00511 (12) vs lines expressing it (38) | 2.32× lower at baseline in the lines without LINC00511 | 0.032 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18 |
| [[FLRT3]] | B | FLRT3 activity raises PLD1's level | lines that do not express FLRT3 (21) vs lines expressing it (29) | 1.73× lower at baseline in the lines without FLRT3 | 0.036 | ⚠ within organs, on part of the lines; also absent: ARHGAP30, TMC5, ENSG00000259925 |
| [[FBXO32]] | B | FBXO32 activity raises PLD1's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 2.10× lower at baseline in the lines without FBXO32 | 0.041 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[MAF]] | B | MAF activity raises PLD1's level | lines that do not express MAF (27) vs lines expressing it (23) | 2.65× lower at baseline in the lines without MAF | 0.051 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 20, C 2. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DENR]] | B | PLD1 activity lowers DENR's level | lines that do not express PLD1 (7) vs lines expressing it (43) | 1.80× higher at baseline in the lines without PLD1 | 0.002 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |
| [[LINC00511]] | B | PLD1 activity raises LINC00511's level | lines that do not express PLD1 (7) vs lines expressing it (43) | 3.95× lower at baseline in the lines without PLD1 | 0.017 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |
| [[FNDC3B]] | B | PLD1 activity raises FNDC3B's level | lines that do not express PLD1 (7) vs lines expressing it (43) | 2.49× lower at baseline in the lines without PLD1 | 0.022 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |
| [[FBXO32]] | B | PLD1 activity raises FBXO32's level | lines that do not express PLD1 (7) vs lines expressing it (43) | 3.69× lower at baseline in the lines without PLD1 | 0.028 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |
| [[UGCG]] | B | PLD1 activity raises UGCG's level | lines that do not express PLD1 (7) vs lines expressing it (43) | 2.16× lower at baseline in the lines without PLD1 | 0.033 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |
| [[NEDD9]] | B | PLD1 activity raises NEDD9's level | lines that do not express PLD1 (7) vs lines expressing it (43) | 4.64× lower at baseline in the lines without PLD1 | 0.038 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |
| [[TNFRSF21]] | B | PLD1 activity raises TNFRSF21's level | lines that do not express PLD1 (7) vs lines expressing it (43) | 2.56× lower at baseline in the lines without PLD1 | 0.040 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |
| [[AHR]] | B | PLD1 activity raises AHR's level | lines that do not express PLD1 (7) vs lines expressing it (43) | 4.49× lower at baseline in the lines without PLD1 | 0.046 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |
| cells under [[Auranofin (drug)]] 5 µM | B | PLD1 activity raises the cells' numbers under Auranofin 5 µM (protects the cells) | lines that do not express PLD1 (7) vs lines expressing it (41) | the lines without PLD1: 0.71× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |
| [[MYO1E]] | B | PLD1 activity strengthens MYO1E's drug response | lines that do not express PLD1 (6) vs lines expressing it (38) | the lines without PLD1 respond 0.57× as strongly (z diff +2.99); strongest at Idarubicin (hydrochloride) 5 µM: 1.07x vs 0.51x (z diff +8.3) | 0.060 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[DHRS3]] | B | PLD1 activity raises DHRS3's level | lines that do not express PLD1 (7) vs lines expressing it (43) | 4.46× lower at baseline in the lines without PLD1 | 0.067 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |
| [[ZNF783]] | B | PLD1 activity lowers ZNF783's level | lines that do not express PLD1 (7) vs lines expressing it (43) | 1.68× higher at baseline in the lines without PLD1 | 0.070 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.709). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.6, 20.9); signed map (49.3, 24.0). **Vector** length 98.7, 38.4% of its response variance represented; |z| ≥ 3 in 2,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +11.1 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.1 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | +5.0 | -11.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | +0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +3.9 | -5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | -0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +5.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.3 | +5.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | +5.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.4 | -12.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.3 | -7.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.7 | -5.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.4 | -1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.9 | -7.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -6.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.6 | -6.5 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase D1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.31 — chr3:171,600,404-171,810,950 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phospholipases; Pleckstrin homology domain containing |
| Reactome | 16 pathways, smallest: Synthesis of PG; Role of phospholipids in phagocytosis; Synthesis of PA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13393](https://www.uniprot.org/uniprotkb/Q13393) (Phospholipase D1):

> Function as phospholipase selective for phosphatidylcholine. Implicated as a critical step in numerous cellular pathways, including signal transduction, membrane trafficking, and the regulation of mitosis. May be involved in the regulation of perinuclear intravesicular membrane traffic (By similarity).

**Summary**, from NCBI Gene [5337](https://www.ncbi.nlm.nih.gov/gene/5337):

> This gene encodes a phosphatidylcholine-specific phospholipase which catalyzes the hydrolysis of phosphatidylcholine in order to yield phosphatidic acid and choline. The enzyme may play a role in signal transduction and subcellular trafficking. Alternative splicing results in multiple transcript variants with both catalytic and regulatory properties. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:9067](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9067) · Entrez [5337](https://www.ncbi.nlm.nih.gov/gene/5337) · UniProt [Q13393](https://www.uniprot.org/uniprotkb/Q13393) · Ensembl [ENSG00000075651](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075651)

## Data

Gene col 1128: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1128); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1128, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1128]; `tensor/DDL_lfc|DDL_z.npy` [1128]; `embed/gene_vectors.npy` [1128]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1128 or target_col == 1128). Every well: [[PLD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
