---
symbol: "IPPK"
type: "gene"
col: 4786
ensembl_id: "ENSG00000127080"
name: "inositol-pentakisphosphate 2-kinase"
location: "9q22.31"
module: 0
arm: null
pooled_cpm: 29.35
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 15
n_dd_up_clean: 22
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene"]
generated_by: "tahoemap"
---

# IPPK

*inositol-pentakisphosphate 2-kinase* — 9q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (13 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 7.60× (z +16.2, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.518× (z -10.7, q 8e-24, down in 33 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.721× (z -5.8, q 1e-06, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPRED3]] (+0.68, fdr 7e-06), [[PDCD6]] (+0.64, fdr 1e-05), [[DHRS7B]] (+0.64, fdr 8e-06); moves opposite to [[KRAS]] (-0.57, fdr 2e-05), [[SNX15]] (-0.55, fdr 1e-05), [[KIF13A]] (-0.54, fdr 2e-05).
> Its neighbourhood forms no module of 5 or more genes (module 0, unassigned).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4786.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **7.60×** | +16.2 | 0e+00 | 46/48 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +15.0 | 0e+00 | 40/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.04×** | +11.5 | 1e-28 | 42/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.78×** | +9.3 | 1e-18 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +9.3 | 1e-18 | 31/48 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +9.2 | 3e-18 | 39/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.75×** | +9.1 | 8e-18 | 34/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.93×** | +8.6 | 7e-16 | 34/45 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +7.2 | 3e-11 | 33/47 (LoVo, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +7.1 | 5e-11 | 28/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +7.1 | 8e-11 | 35/48 (Hs 766T, NCI-H2030, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +6.7 | 8e-10 | 29/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +6.4 | 6e-09 | 31/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +6.3 | 1e-08 | 28/48 (A498, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.41×** | +5.4 | 3e-06 | 26/47 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +5.2 | 9e-06 | 25/47 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +4.9 | 3e-05 | 24/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.34×** | +4.7 | 9e-05 | 22/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4786.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.518×** | -10.7 | 8e-24 | 33/45 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.533×** | -9.8 | 3e-20 | 26/34 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.721×** | -5.8 | 1e-06 | 27/48 (A-427, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.719×** | -5.2 | 4e-05 | 23/48 (NCI-H1573, C-33 A, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.740×** | -4.9 | 1e-04 | 25/48 (A-427, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Alpelisib (drug)]] 5 µM |  | **0.551×** | -4.8 | 2e-04 | 20/47 (MIA PaCa-2, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.751×** | -4.5 | 6e-04 | 21/47 (C32, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.770×** | -4.3 | 1e-03 | 21/48 (A-427, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -4.3 | 0.001 | 5/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.800×** | -4.1 | 0.002 | 22/48 (A-427, SW 1088, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.777×** | -4.1 | 0.002 | 21/48 (AN3 CA, A-427, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.837× | -4.1 | 0.002 | 20/48 (RPMI-7951, A498, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.679×** | -4.0 | 0.002 | 20/47 (Hs 766T, RPMI-7951, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.790×** | -3.8 | 0.005 | 16/48 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.812×** | -3.6 | 0.011 | 15/48 (RPMI-7951, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.855× | -3.5 | 0.017 | 13/48 (C32, RKO, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.808×** | -3.3 | 0.028 | 15/47 (hTERT-HPNE, NCI-H23, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.823×** | -3.2 | 0.049 | 19/47 (CHP-212, NCI-H460, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.834× | -3.0 | 0.091 | 9/47 (HepG2/C3A, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4786. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 39.9 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -10.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 20.7 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +17.5) | — |
| [[SW480 (line)]] | alt | 33.0 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.57× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -8.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 34.1 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +11.3) | [[Adagrasib (drug)]] 0.05 µM 0.601× (z -12.9) ⚠ position not correctable |
| [[LoVo (line)]] | wt | 19.1 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.6× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.205× (z -12.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 29.6 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.09× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.100× (z -19.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 22.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +9.4) | — |
| [[J82 (line)]] | alt | 53.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -10.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 25.0 | 0 | 2 | — | [[Trametinib (drug)]] 0.5 µM 0.316× (z -8.7) |
| [[A498 (line)]] | wt | 44.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -12.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 30.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +14.3) | [[Dinaciclib (drug)]] 0.05 µM 0.192× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 32.1 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.36× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 26.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.07× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 26.0 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.77× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -9.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 75.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.65× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 36.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -13.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 31.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.148× (z -13.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 25.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -12.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 24.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Palmatine (chloride) (drug)]] 0.5 µM 0.158× (z -9.7) |
| [[A-172 (line)]] | wt | 22.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 27.6 | 0 | 1 | — | [[Ponatinib (drug)]] 0.5 µM 0.0833× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -12.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0670× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -9.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 52.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +12.3) | — |
| [[NCI-H23 (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.626× (z -11.7) ⚠ position not correctable |
| [[NCI-H2347 (line)]] | alt | 17.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -8.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 32.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +8.8) | — |
| [[SW 900 (line)]] | alt | 26.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +9.1) | — |
| [[C-33 A (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4786), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRED3]] | +0.68 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[PDCD6]] | +0.64 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[DHRS7B]] | +0.64 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[NACC1]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[SLC30A7]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ARPC5L]] | +0.61 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[ZNF668]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[TTLL3]] | +0.60 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[GPATCH2L]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[ARPC2]] | +0.59 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[SPRED2]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[SLC25A44]] | +0.58 | +0.44 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRAS]] | -0.57 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[SNX15]] | -0.55 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[KIF13A]] | -0.54 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[FMR1]] | -0.51 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[ZNF326]] | -0.51 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[HINT3]] | -0.50 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[KIDINS220]] | -0.50 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[EPS8]] | -0.50 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[MATR3]] | -0.49 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[CFL2]] | -0.49 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[NR1D2]] | -0.49 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[FPGT]] | -0.49 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises IPPK's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[LNCOG]] | B | LNCOG activity raises IPPK's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 1.35× lower at baseline in the lines without LNCOG | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: none (module 0: its neighbourhood formed no community of ≥ 5 genes).
- **Nodal map** (x, y) = (18.9, -21.0); signed map (8.2, 14.3). **Vector** length 76.9, 17.7% of its response variance represented; |z| ≥ 3 in 1,231 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +7.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.2 | +16.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.1 | +5.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.2 | +2.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.2 | +0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +1.4 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.5 | -4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.0 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.7 | -4.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | inositol-pentakisphosphate 2-kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.31 — chr9:92,613,183-92,670,131 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IP5-2K, INSP5K2, FLJ13163, IP5K, IPK1; previously C9orf12 |
| Gene groups (HGNC) | Inositol phosphate kinases |
| Reactome | 3 pathways, smallest: Synthesis of IPs in the nucleus; Synthesis of pyrophosphates in the cytosol; Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H8X2](https://www.uniprot.org/uniprotkb/Q9H8X2) (Inositol-pentakisphosphate 2-kinase):

> Phosphorylates Ins(1,3,4,5,6)P5 at position 2 to form Ins(1,2,3,4,5,6)P6 (InsP6 or phytate). InsP6 is involved in many processes such as mRNA export, non-homologous end-joining, endocytosis, ion channel regulation. It also protects cells from TNF-induced apoptosis.

**Summary**, from NCBI Gene [64768](https://www.ncbi.nlm.nih.gov/gene/64768):

> The protein encoded by this gene is a kinase that phosphorylates position 2 of inositol-1,3,4,5,6-pentakisphosphate to form inositol-1,2,3,4,5,6-hexakisphosphate (InsP6). InsP6 has a variety of functions, including stimulation of DNA repair, endocytosis, and mRNA export. [provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:14645](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14645) · Entrez [64768](https://www.ncbi.nlm.nih.gov/gene/64768) · UniProt [Q9H8X2](https://www.uniprot.org/uniprotkb/Q9H8X2) · Ensembl [ENSG00000127080](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127080)

## Data

Gene col 4786: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4786); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4786, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4786]; `tensor/DDL_lfc|DDL_z.npy` [4786]; `embed/gene_vectors.npy` [4786]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4786 or target_col == 4786). Every well: [[IPPK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IPPK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
