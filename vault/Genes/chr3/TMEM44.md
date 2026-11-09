---
symbol: "TMEM44"
type: "gene"
col: 6950
ensembl_id: "ENSG00000145014"
name: "transmembrane protein 44"
location: "3q29"
module: 218
arm: "+"
pooled_cpm: 45.59
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 42
n_dd_up_clean: 1
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/218"]
generated_by: "tahoemap"
---

# TMEM44

*transmembrane protein 44* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.33× (z +4.3, q 0.007, up in 24 of 46 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.31× (z +4.2, q 0.007, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.217× (z -33.5, q 0e+00, down in 46 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO9B]] (+0.60, fdr 7e-06), [[STK10]] (+0.57, fdr 1e-05), [[SMTN]] (+0.57, fdr 3e-05); moves opposite to [[FIGN]] (-0.53, fdr 1e-05), [[RAB14]] (-0.52, fdr 3e-05), [[CILK1]] (-0.51, fdr 1e-05).
> It is in [[Module 218]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RAC2]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6950.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.33×** | +4.3 | 0.007 | 24/46 (SNU-423, A549, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.31×** | +4.2 | 0.007 | 27/46 (HCT15, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.7 | 0.042 | 0/47 | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.18× | +3.6 | 0.053 | 12/47 (A-172, PANC-1, …) | rises with dose |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.23× | +3.1 | 0.19 | 14/47 (SW480, NCI-H1573, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 21 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6950.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.217×** | -33.5 | 0e+00 | 46/46 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.169×** | -26.5 | 0e+00 | 47/47 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.325×** | -17.5 | 0e+00 | 44/46 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.456×** | -17.2 | 0e+00 | 39/46 (Panc 03.27, J82, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.358×** | -15.9 | 0e+00 | 46/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.392×** | -14.6 | 0e+00 | 43/47 (SW480, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.399×** | -14.3 | 4e-44 | 42/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.401×** | -14.2 | 9e-44 | 44/47 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.403×** | -14.1 | 2e-43 | 42/47 (hTERT-HPNE, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.425×** | -13.3 | 2e-38 | 39/47 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.421×** | -12.9 | 2e-36 | 37/46 (NCI-H23, H4, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.537×** | -9.6 | 2e-20 | 38/47 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.569×** | -8.8 | 9e-17 | 31/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **0.577×** | -8.5 | 5e-16 | 29/46 (J82, NCI-H1792, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.578×** | -8.5 | 6e-16 | 34/47 (LOX-IMVI, RPMI-7951, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.590×** | -8.2 | 9e-15 | 41/47 (LOX-IMVI, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.604×** | -7.8 | 1e-13 | 35/47 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.612×** | -7.2 | 1e-11 | 33/47 (HOP62, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.652×** | -6.6 | 7e-10 | 37/47 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.781×** | -5.4 | 1e-06 | 25/47 (HOP62, HEC-1-A, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.521×** | -5.3 | 2e-06 | 25/46 (SNU-1, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.582×** | -4.4 | 2e-04 | 24/47 (AsPC-1, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.786×** | -3.7 | 0.003 | 20/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6950. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 40.8 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -23.1) |
| [[HOP62 (line)]] | alt | 82.7 | 0 | 17 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -23.6) |
| [[HEC-1-A (line)]] | alt | 64.9 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -29.3) |
| [[MIA PaCa-2 (line)]] | alt | 57.7 | 0 | 16 (10 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.118× (z -18.0) |
| [[PANC-1 (line)]] | alt | 84.4 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -38.4) |
| [[A-172 (line)]] | wt | 62.3 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -21.9) |
| [[SNU-423 (line)]] | alt | 53.1 | 0 | 13 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0676× (z -20.4) |
| [[NCI-H23 (line)]] | alt | 50.0 | 0 | 12 (8 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0467× (z -26.6) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.151× (z -24.0) |
| [[NCI-H460 (line)]] | wt | 27.0 | 0 | 12 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0921× (z -19.8) |
| [[SW480 (line)]] | alt | 42.7 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -21.3) |
| [[A549 (line)]] | wt | 51.3 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0883× (z -26.5) |
| [[AsPC-1 (line)]] | alt | 59.4 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0446× (z -40.8) |
| [[J82 (line)]] | alt | 79.0 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -23.4) |
| [[NCI-H1792 (line)]] | alt | 50.1 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -20.0) |
| [[A498 (line)]] | wt | 55.1 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -21.6) |
| [[Panc 03.27 (line)]] | alt | 65.4 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -26.0) |
| [[RPMI-7951 (line)]] | alt | 53.8 | 0 | 9 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0792× (z -18.6) |
| [[H4 (line)]] | wt | 47.1 | 0 | 8 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0746× (z -15.1) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0943× (z -14.3) |
| [[HT-29 (line)]] | alt | 57.3 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0897× (z -27.2) |
| [[hTERT-HPNE (line)]] | wt | 47.6 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -19.3) |
| [[A-427 (line)]] | wt | 34.8 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -18.0) |
| [[HS-578T (line)]] | alt | 75.7 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -17.1) |
| [[LoVo (line)]] | wt | 32.2 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.173× (z -16.7) |
| [[CFPAC-1 (line)]] | alt | 44.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -17.2) |
| [[COLO 205 (line)]] | alt | 48.1 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0605× (z -20.3) |
| [[KATO III (line)]] | alt | 41.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -22.0) |
| [[RKO (line)]] | wt | 29.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -18.3) |
| [[BT-474 (line)]] | alt | 26.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -17.6) |
| [[LS 180 (line)]] | wt | 29.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 25.7 | 0 | 4 | — | [[Harringtonine (drug)]] 0.5 µM 0.181× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 21.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 23.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 33.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[SW 900 (line)]] | alt | 19.4 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.128× (z -11.9) |
| [[SW1417 (line)]] | alt | 32.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -17.4) |
| [[SW48 (line)]] | wt | 26.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -12.3) |
| [[Hs 766T (line)]] | wt | 37.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -15.2) |
| [[SNU-1 (line)]] | wt | 38.8 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0725× (z -15.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 1271 (line)]] | alt | 84.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0555× (z -10.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.164× (z -9.4) |
| [[HCT15 (line)]] | alt | 37.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -15.2) |
| [[AN3 CA (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 72.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6950), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO9B]] | +0.60 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[STK10]] | +0.57 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[SMTN]] | +0.57 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[ARID3B]] | +0.57 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[CCM2]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[KCNC4]] | +0.56 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[PLAUR]] | +0.56 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[FAAP20]] | +0.56 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[OGG1]] | +0.56 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[PLEKHG5]] | +0.56 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SMURF1]] | +0.55 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[MARCHF3]] | +0.55 | +0.51 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FIGN]] | -0.53 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[RAB14]] | -0.52 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[CILK1]] | -0.51 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[BBX]] | -0.50 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[MBNL2]] | -0.50 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[COX15]] | -0.49 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[PTPN13]] | -0.48 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[KCTD3]] | -0.47 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[NFIA]] | -0.47 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[ANGPT1]] | -0.47 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[TRUB1]] | -0.47 | -0.50 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAC2]] | B | RAC2 activity raises TMEM44's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 1.70× lower at baseline in the lines without RAC2 | 0.021 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[TUBB6]] | B | TUBB6 activity raises TMEM44's level | lines that do not express TUBB6 (11) vs lines expressing it (39) | 1.25× lower at baseline in the lines without TUBB6 | 0.055 | ⚠ within organs, on part of the lines; also absent: DNAAF9, CHST10, SYDE1 |
| [[PLAUR]] | B | PLAUR activity raises TMEM44's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 1.67× lower at baseline in the lines without PLAUR | 0.064 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises TMEM44's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | TMEM44's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | TMEM44's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.57 | 0.529 over the table, 0.099 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 218]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.642). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.3, 1.1); signed map (-0.6, 47.0). **Vector** length 63.5, 16.0% of its response variance represented; |z| ≥ 3 in 1,533 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | -6.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.4 | -14.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.3 | -14.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +2.3 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | -0.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.7 | +3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.6 | -0.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +1.4 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.1 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.3 | -13.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.7 | -8.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | -2.5 | -12.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 44 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:194,587,673-194,633,689 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686O18124 |
| Matched by | ensembl_id |

UniProt [Q2T9K0](https://www.uniprot.org/uniprotkb/Q2T9K0) carries no function annotation.

**Summary**, from NCBI Gene [93109](https://www.ncbi.nlm.nih.gov/gene/93109):

> Predicted to enable basic amino acid transmembrane transporter activity. Predicted to be involved in basic amino acid transmembrane transport. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25120](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25120) · Entrez [93109](https://www.ncbi.nlm.nih.gov/gene/93109) · UniProt [Q2T9K0](https://www.uniprot.org/uniprotkb/Q2T9K0) · Ensembl [ENSG00000145014](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145014)

## Data

Gene col 6950: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6950); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6950, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6950]; `tensor/DDL_lfc|DDL_z.npy` [6950]; `embed/gene_vectors.npy` [6950]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6950 or target_col == 6950). Every well: [[TMEM44 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM44.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
