---
symbol: "AKAP7"
type: "gene"
col: 3996
ensembl_id: "ENSG00000118507"
name: "A-kinase anchoring protein 7"
location: "6q23.2"
module: 18
arm: "+"
pooled_cpm: 17.53
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 38
n_dd_up_clean: 9
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# AKAP7

*A-kinase anchoring protein 7* — 6q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.53× (z +5.9, q 2e-06, up in 24 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.370× (z -19.2, q 0e+00, down in 40 of 46 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.341× (z -14.7, q 0e+00, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF236]] (+0.61, fdr 2e-05), [[ANGEL2]] (+0.61, fdr 1e-05), [[ZNF618]] (+0.61, fdr 1e-05); moves opposite to [[NBEAL1]] (-0.59, fdr 2e-05), [[SCART1]] (-0.55, fdr 1e-04), [[PPARA]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PAX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3996.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +5.9 | 2e-06 | 24/45 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.38×** | +4.3 | 0.005 | 18/45 (NCI-H23, C32, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.008 | 14/46 (C32, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +4.0 | 0.008 | 17/45 (C32, SNU-423, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.015 | 11/46 (SK-MEL-2, C32, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.20× | +3.5 | 0.040 | 18/46 (KATO III, SW1417, …) | all doses, flat | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.29×** | +3.5 | 0.044 | 11/46 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.077 | 12/46 (C32, NCI-H1792, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.28×** | +3.1 | 0.099 | 10/46 (PANC-1, SW1417, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.099 | 7/46 (SK-MEL-2, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.099 | 8/45 (NCI-H1792, NCI-H661, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.099 | 11/46 (LS 180, KATO III, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.25×** | +3.1 | 0.099 | 10/45 (SNU-423, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3996.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.370×** | -19.2 | 0e+00 | 40/46 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.341×** | -14.7 | 0e+00 | 43/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.390×** | -12.9 | 1e-35 | 36/44 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.409×** | -12.2 | 3e-32 | 33/46 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.410×** | -12.2 | 4e-32 | 39/45 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.419×** | -11.9 | 1e-30 | 41/46 (SNU-423, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.424×** | -11.7 | 8e-30 | 36/45 (SK-MEL-2, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.426×** | -11.7 | 1e-29 | 38/46 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.431×** | -11.5 | 7e-29 | 37/46 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.478×** | -9.7 | 2e-20 | 31/44 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.516×** | -9.0 | 8e-18 | 35/45 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.312×** | -8.3 | 4e-15 | 35/46 (RKO, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.536×** | -8.2 | 1e-14 | 31/46 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.578×** | -7.5 | 3e-12 | 29/45 (H4, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.369×** | -7.1 | 4e-11 | 34/45 (RKO, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.666×** | -5.5 | 1e-06 | 24/46 (HT-29, PANC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.704×** | -4.8 | 5e-05 | 20/45 (PANC-1, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.704×** | -4.5 | 2e-04 | 19/46 (PANC-1, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.737×** | -4.2 | 8e-04 | 17/45 (NCI-H23, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3996. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 24.2 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -17.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.226× (z -10.5) |
| [[PANC-1 (line)]] | alt | 31.8 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0959× (z -31.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.154× (z -17.6) |
| [[A-172 (line)]] | wt | 32.2 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -19.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.156× (z -12.9) |
| [[MIA PaCa-2 (line)]] | alt | 33.4 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -20.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.211× (z -9.9) |
| [[LoVo (line)]] | wt | 17.7 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -13.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.199× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 11.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -15.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.130× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 17.6 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.235× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.276× (z -9.8) |
| [[A498 (line)]] | wt | 18.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -17.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.232× (z -10.9) |
| [[C32 (line)]] | wt | 26.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -11.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.193× (z -9.9) |
| [[HT-29 (line)]] | alt | 18.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -9.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0861× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 14.2 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.120× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 39.6 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.107× (z -15.9) |
| [[SNU-423 (line)]] | alt | 23.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -19.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.116× (z -12.7) |
| [[A-427 (line)]] | wt | 41.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 17.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -15.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.243× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 21.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 24.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -17.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -12.0) |
| [[H4 (line)]] | wt | 18.5 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0553× (z -11.9) |
| [[SW480 (line)]] | alt | 7.98 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +8.8) ⚠ cell-cycle shift, explains ~21% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -11.8) |
| [[AN3 CA (line)]] | alt | 49.6 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.108× (z -8.9) |
| [[C-33 A (line)]] | alt | 23.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -9.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HS-578T (line)]] | alt | 12.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.101× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 16.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -10.5) |
| [[RKO (line)]] | wt | 22.5 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0434× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -11.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -8.5) |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0950× (z -10.5) |
| [[SW1417 (line)]] | alt | 15.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.168× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3996), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF236]] | +0.61 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[ANGEL2]] | +0.61 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[ZNF618]] | +0.61 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[MVB12B]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[ERAP2]] | +0.60 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[RNASEH2B]] | +0.59 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[KLHL42]] | +0.59 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[SLC16A14]] | +0.59 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[B3GALNT1]] | +0.57 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[GTF3C6]] | +0.57 | +0.46 / +0.37 | both halves | 8e-05 |  |
| [[MOV10]] | +0.57 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[TMCO4]] | +0.57 | +0.48 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBEAL1]] | -0.59 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[SCART1]] | -0.55 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[PPARA]] | -0.55 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[PPARD]] | -0.54 | -0.52 / -0.37 | both halves | 7e-05 |  |
| [[CYP2E1]] | -0.54 | -0.28 / -0.59 | both halves | 3e-04 |  |
| [[SRSF9]] ⚠ | -0.52 | -0.44 / -0.39 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PLEKHM1P1]] | -0.51 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[SCAT1]] | -0.51 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[PLEKHM1]] | -0.51 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[NDRG1]] | -0.50 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[RASA4B]] | -0.50 | -0.44 / -0.36 | both halves | 9e-05 |  |
| [[RGP1]] | -0.49 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[SPAG9]] | -0.49 | -0.38 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAX2]] | B | PAX2 activity raises AKAP7's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 1.68× lower at baseline in the lines without PAX2 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[MAP2K1]] | B | MAP2K1 activity lowers AKAP7's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[PRDM5]] | B | PRDM5 activity raises AKAP7's level | lines that do not express PRDM5 (13) vs lines expressing it (37) | 1.47× lower at baseline in the lines without PRDM5 | 0.046 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| [[DZIP1L]] | B | DZIP1L activity raises AKAP7's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 2.03× lower at baseline in the lines without DZIP1L | 0.060 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[SMO]] | B | SMO activity raises AKAP7's level | lines that do not express SMO (17) vs lines expressing it (33) | 1.68× lower at baseline in the lines without SMO | 0.060 | ⚠ within organs, on part of the lines; also absent: RADIL, DUSP9, APBA2 |
| [[SCAT1]] | B | SCAT1 activity lowers AKAP7's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 1.46× higher at baseline in the lines without SCAT1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.378). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.8, 14.0); signed map (13.7, -44.7). **Vector** length 81.5, 19.2% of its response variance represented; |z| ≥ 3 in 1,229 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.9 | +5.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.8 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.1 | -1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.3 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.0 | +2.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.0 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +2.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.6 | -11.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.7 | -7.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.3 | -12.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.0 | -3.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.0 | -11.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -3.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.4 | -1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | A-kinase anchoring protein 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.2 — chr6:131,135,467-131,283,535 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AKAP18, AKAP15 |
| Gene groups (HGNC) | A-kinase anchoring proteins |
| Hallmark sets | APICAL_SURFACE |
| Matched by | ensembl_id |

**Function**, from UniProt [O43687](https://www.uniprot.org/uniprotkb/O43687) (A-kinase anchor protein 7 isoforms alpha and beta):

> Targets the cAMP-dependent protein kinase (PKA) to the plasma membrane, and permits functional coupling to the L-type calcium channel. The membrane-associated form reduces epithelial sodium channel (ENaC) activity, whereas the free cytoplasmic form may negatively regulate ENaC channel feedback inhibition by intracellular sodium.

**Summary**, from NCBI Gene [9465](https://www.ncbi.nlm.nih.gov/gene/9465):

> This gene encodes a member of the A-kinase anchoring protein (AKAP) family, a group of functionally related proteins that bind to a regulatory subunit (RII) of cAMP-dependent protein kinase A (PKA) and target the enzyme to specific subcellular compartments. AKAPs have a common RII-binding domain, but contain different targeting motifs responsible for directing PKA to distinct intracellular locations. Three alternatively spliced transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:377](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:377) · Entrez [9465](https://www.ncbi.nlm.nih.gov/gene/9465) · UniProt [O43687](https://www.uniprot.org/uniprotkb/O43687) · Ensembl [ENSG00000118507](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118507)

## Data

Gene col 3996: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3996); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3996, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3996]; `tensor/DDL_lfc|DDL_z.npy` [3996]; `embed/gene_vectors.npy` [3996]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3996 or target_col == 3996). Every well: [[AKAP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKAP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
