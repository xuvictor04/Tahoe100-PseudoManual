---
symbol: "ELMOD2"
type: "gene"
col: 11026
ensembl_id: "ENSG00000179387"
name: "ELMO domain containing 2"
location: "4q31.1"
module: 25
arm: "+"
pooled_cpm: 27.67
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 17
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# ELMOD2

*ELMO domain containing 2* — 4q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.72× (z +10.6, q 3e-23, up in 27 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.63× (z +9.9, q 1e-20, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.408× (z -18.1, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OCRL]] (+0.65, fdr 1e-05), [[PHF6]] (+0.65, fdr 3e-05), [[ZDHHC6]] (+0.63, fdr 1e-05); moves opposite to [[SPATC1]] (-0.60, fdr 1e-04), [[EIF4EBP3]] (-0.56, fdr 2e-04), [[ZBTB7A]] (-0.56, fdr 9e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11026.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +10.6 | 3e-23 | 27/36 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +9.9 | 1e-20 | 36/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +7.6 | 5e-12 | 21/44 (A498, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +7.6 | 5e-12 | 31/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +7.4 | 2e-11 | 27/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +4.4 | 9e-04 | 17/48 (HT-29, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | 1.17× | +4.4 | 9e-04 | 25/48 (RKO, J82, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.008 | 12/48 (KATO III, CFPAC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.21×** | +3.8 | 0.009 | 15/48 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +3.3 | 0.052 | 11/47 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +3.1 | 0.087 | 6/48 (KATO III, A-427, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.087 | 10/48 (KATO III, NCI-H2347, …) | rises with dose | position effect removed |
| [[Folic acid (drug)]] 5 µM |  | 1.11× | +3.1 | 0.087 | 2/48 (Hs 766T, AsPC-1) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.087 | 3/48 (A-172, CFPAC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.16× | +3.0 | 0.090 | 7/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11026.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.408×** | -18.1 | 0e+00 | 43/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.438×** | -16.7 | 0e+00 | 40/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.568×** | -11.4 | 7e-28 | 39/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.570×** | -11.4 | 9e-28 | 33/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.693×** | -10.5 | 1e-23 | 34/47 (NCI-H1792, NCI-H460, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.617×** | -9.4 | 6e-19 | 28/48 (NCI-H460, J82, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.421×** | -9.1 | 5e-18 | 34/47 (LOX-IMVI, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.454×** | -8.3 | 6e-15 | 36/48 (LoVo, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.676×** | -7.9 | 2e-13 | 28/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.734×** | -6.2 | 3e-08 | 23/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.820×** | -5.7 | 7e-07 | 26/48 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.757×** | -5.4 | 3e-06 | 23/47 (HCT15, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.781×** | -5.0 | 3e-05 | 20/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.759×** | -4.0 | 0.003 | 18/47 (Hs 766T, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.834× | -3.7 | 0.009 | 22/47 (PANC-1, A549, …) | rises with dose |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.893× | -3.2 | 0.041 | 7/48 (SW 900, HT-29, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.800×** | -3.2 | 0.041 | 8/48 (NCI-H23, HT-29, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.803×** | -3.2 | 0.045 | 11/48 (SHP-77, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 0.859× | -3.1 | 0.057 | 15/46 (LS 180, HS-578T, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.811×** | -3.0 | 0.065 | 5/48 (PANC-1, HCT15, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Mifepristone (drug)]] 5 µM |  | 0.860× | -2.9 | 0.084 | 4/48 (SW 1271, SW 1088, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11026. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.7 | 0 | 10 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -15.0) |
| [[PANC-1 (line)]] | alt | 32.0 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.189× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.242× (z -16.1) |
| [[SW480 (line)]] | alt | 25.2 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -14.8) |
| [[NCI-H1573 (line)]] | alt | 50.3 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.263× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 31.5 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -13.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 26.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -12.0) ⚠ cell-cycle shift, explains ~48% of this change |
| [[C-33 A (line)]] | alt | 49.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 22.1 | 0 | 2 (1 ⚠) | — | [[Ipatasertib (drug)]] 0.5 µM 0.151× (z -9.2) |
| [[HT-29 (line)]] | alt | 24.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -10.2) |
| [[J82 (line)]] | alt | 27.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.352× (z -8.7) |
| [[LS 180 (line)]] | wt | 27.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.226× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.370× (z -8.6) |
| [[SW 900 (line)]] | alt | 21.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.221× (z -10.4) |
| [[A-172 (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -8.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A-427 (line)]] | wt | 33.6 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0916× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 33.3 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.102× (z -8.8) |
| [[C32 (line)]] | wt | 30.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -9.6) |
| [[HCT15 (line)]] | alt | 38.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.150× (z -12.8) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 35.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -10.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 32.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.254× (z -11.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -15.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 26.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.304× (z -10.8) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 22.3 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0615× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 17.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.13× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0797× (z -9.0) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 25.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.375× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.180× (z -11.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 24.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.171× (z -9.0) |
| [[A498 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11026), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OCRL]] | +0.65 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[PHF6]] | +0.65 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[ZDHHC6]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[DTD1]] | +0.63 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ZDHHC21]] | +0.62 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[TMEM209]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[EXOC5]] | +0.61 | +0.49 / +0.62 | both halves | 2e-05 |  |
| [[DNAJC10]] | +0.61 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ALG10]] | +0.60 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[RFT1]] | +0.59 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[FBXW2]] | +0.59 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[ACP1]] | +0.59 | +0.46 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATC1]] | -0.60 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[EIF4EBP3]] | -0.56 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[ZBTB7A]] | -0.56 | -0.37 / -0.60 | both halves | 9e-05 |  |
| [[ARMC5]] | -0.55 | -0.29 / -0.55 | both halves | 3e-04 |  |
| [[GPRC5C]] | -0.55 | -0.29 / -0.55 | both halves | 2e-04 |  |
| [[LINC00685]] | -0.54 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[ANKHD1]] | -0.54 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[EPS15-AS1]] | -0.54 | -0.32 / -0.48 | both halves | 1e-04 |  |
| [[ANKHD1-EIF4EBP3]] | -0.54 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[C2]] | -0.54 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[IL12RB2]] | -0.53 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[SMIM27]] | -0.53 | -0.28 / -0.50 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ELMOD2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.634). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.8, -36.1); signed map (-34.4, -32.6). **Vector** length 71.2, 13.4% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +10.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +2.4 | +4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.2 | +7.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.2 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +1.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +1.5 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -16.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -3.2 | -10.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.7 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -1.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.2 | -3.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ELMO domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.1 — chr4:140,524,168-140,553,770 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10084 |
| Gene groups (HGNC) | ELMO domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZ81](https://www.uniprot.org/uniprotkb/Q8IZ81) (ELMO domain-containing protein 2):

> Acts as a GTPase-activating protein (GAP) toward guanine nucleotide exchange factors like ARL2, ARL3, ARF1 and ARF6, but not for GTPases outside the Arf family. Regulates IFN-related antiviral responses.

**Summary**, from NCBI Gene [255520](https://www.ncbi.nlm.nih.gov/gene/255520):

> This gene encodes one of six engulfment and motility (ELMO) domain-containing proteins. This gene is thought to play a role in antiviral responses. Mutations in this gene may be involved in the cause of familial idiopathic pulmonary fibrosis. [provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:28111](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28111) · Entrez [255520](https://www.ncbi.nlm.nih.gov/gene/255520) · UniProt [Q8IZ81](https://www.uniprot.org/uniprotkb/Q8IZ81) · Ensembl [ENSG00000179387](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179387)

## Data

Gene col 11026: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11026); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11026, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11026]; `tensor/DDL_lfc|DDL_z.npy` [11026]; `embed/gene_vectors.npy` [11026]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11026 or target_col == 11026). Every well: [[ELMOD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELMOD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
