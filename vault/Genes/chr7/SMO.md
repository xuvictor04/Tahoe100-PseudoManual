---
symbol: "SMO"
type: "gene"
col: 4902
ensembl_id: "ENSG00000128602"
name: "smoothened, frizzled class receptor"
location: "7q32.1"
module: 102
arm: "+"
pooled_cpm: 6.42
n_lines_expressing: 33
n_dd_up: 13
n_dd_down: 27
n_dd_up_clean: 9
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 14
direction_downstream: 4
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# SMO

*smoothened, frizzled class receptor* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 2.31× (z +10.0, q 1e-20, up in 22 of 28 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 2.19× (z +9.9, q 1e-20, up in 21 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.263× (z -16.8, q 0e+00, down in 23 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSI1]] (+0.66, fdr 1e-05), [[SYNGR1]] (+0.65, fdr 1e-05), [[FGD1]] (+0.62, fdr 1e-05); moves opposite to [[PICALM]] (-0.51, fdr 8e-05), [[GALE]] (-0.50, fdr 3e-05), [[VGF]] (-0.47, fdr 1e-04).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[MSI1]] → it (grade B ⚠); 4 go from it, the strongest it → [[SYNGR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4902.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.31×** | +10.0 | 1e-20 | 22/28 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.19×** | +9.9 | 1e-20 | 21/30 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.70×** | +6.7 | 5e-09 | 16/30 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.58×** | +6.3 | 6e-08 | 8/17 (SNU-1, A498, …) | all doses, flat | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.36×** | +5.5 | 5e-06 | 17/31 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.82×** | +5.4 | 7e-06 | 10/30 (A-172, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +3.6 | 0.024 | 4/31 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.053 | 7/30 (LoVo, A498, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.063 | 4/31 (HOP62, C-33 A, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.063 | 3/31 (A498, NCI-H23, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.29×** | +3.2 | 0.063 | 3/28 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.063 | 3/30 (SW480, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.095 | 9/28 (A498, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4902.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.263×** | -16.8 | 0e+00 | 23/28 (SNU-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.446×** | -14.4 | 1e-44 | 24/30 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.310×** | -14.2 | 2e-43 | 25/30 (AN3 CA, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.338×** | -13.7 | 2e-40 | 21/30 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.354×** | -13.1 | 4e-37 | 22/29 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.419×** | -11.0 | 6e-26 | 24/30 (C-33 A, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.453×** | -10.0 | 2e-21 | 20/30 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.506×** | -8.6 | 6e-16 | 20/28 (HOP62, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.507×** | -8.6 | 7e-16 | 21/30 (MIA PaCa-2, C-33 A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.513×** | -8.4 | 2e-15 | 19/27 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.520×** | -8.2 | 9e-15 | 19/30 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.593×** | -6.3 | 1e-08 | 14/28 (SNU-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.599×** | -6.2 | 2e-08 | 14/23 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.400×** | -6.0 | 6e-08 | 15/28 (SNU-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.645×** | -5.5 | 1e-06 | 16/30 (LoVo, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.648×** | -5.2 | 5e-06 | 12/29 (HOP62, NCI-H661, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.748×** | -3.7 | 0.007 | 5/29 (SW 1271, C-33 A, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.814×** | -3.7 | 0.007 | 8/31 (NCI-H2030, MIA PaCa-2, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.763×** | -3.3 | 0.027 | 13/29 (BT-474, C32, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.777×** | -3.2 | 0.036 | 11/28 (LoVo, C32, …) | rises with dose |  |
| [[Auranofin (drug)]] 0.5 µM |  | **0.791×** | -2.9 | 0.067 | 5/30 (HepG2/C3A, SW 1271, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4902. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 17.0 | 0 | 11 (7 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0859× (z -14.6) ⚠ toxic; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 7.64 | 0 | 9 (5 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0849× (z -13.8) |
| [[A-172 (line)]] | wt | 12.3 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -12.8) |
| [[C-33 A (line)]] | alt | 59.8 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0748× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 9.64 | 0 | 5 (5 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0470× (z -12.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 9.52 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0617× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -8.5) |
| [[AN3 CA (line)]] | alt | 70.1 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.104× (z -10.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -9.1) |
| [[HOP62 (line)]] | alt | 7.46 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.152× (z -10.1) |
| [[LoVo (line)]] | wt | 10.2 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0884× (z -15.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.213× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 12.9 | 0 | 4 (4 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.132× (z -12.2) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 38.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -12.9) |
| [[A549 (line)]] | wt | 9.39 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -10.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SW480 (line)]] | alt | 3.77 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0524× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.123× (z -9.9) |
| [[CHP-212 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0392× (z -9.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HS-578T (line)]] | alt | 4.15 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0705× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 3.38 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0646× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 7.80 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0660× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[A-427 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.787 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.746 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.543 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.633 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4902), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSI1]] | +0.66 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[SYNGR1]] | +0.65 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[FGD1]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[CASP6]] | +0.61 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[OSBPL1A]] | +0.59 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ABCC5]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[MVB12B]] | +0.56 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[TUB]] | +0.56 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[PSMA1]] | +0.56 | +0.53 / +0.45 | both halves | 3e-05 | pathway: Hedgehog 'off' state |
| [[LRRN2]] | +0.55 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[TMEM161A]] | +0.55 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ANKRD39]] | +0.54 | +0.57 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PICALM]] | -0.51 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[GALE]] | -0.50 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[VGF]] | -0.47 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[CLIC1]] | -0.47 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[HIVEP2]] | -0.45 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[MYL12A]] | -0.45 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[SDC4]] | -0.44 | -0.42 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSI1]] | B | MSI1 activity raises SMO's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.42× lower at baseline in the lines without MSI1 | 0.021 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[ARHGEF25]] | B | ARHGEF25 activity raises SMO's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 2.62× lower at baseline in the lines without ARHGEF25 | 0.022 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10 |
| [[PRTG]] | B | PRTG activity raises SMO's level | lines that do not express PRTG (14) vs lines expressing it (36) | 3.48× lower at baseline in the lines without PRTG | 0.030 | ⚠ within organs, on part of the lines; also absent: ANKRD6, BNIP3, SNRPN |
| [[B4GALNT1]] | B | B4GALNT1 activity raises SMO's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 2.88× lower at baseline in the lines without B4GALNT1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1 |
| [[TUB]] | B | TUB activity raises SMO's level | lines that do not express TUB (18) vs lines expressing it (32) | 2.58× lower at baseline in the lines without TUB | 0.041 | ⚠ within organs, on part of the lines; also absent: SLC22A17, CPEB1, ZFP82 |
| [[MAP2K1]] | B | MAP2K1 activity lowers SMO's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[CECR2]] | B | CECR2 activity raises SMO's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 2.47× lower at baseline in the lines without CECR2 | 0.045 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent |
| [[SYNGR1]] | B | SYNGR1 activity raises SMO's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 3.06× lower at baseline in the lines without SYNGR1 | 0.050 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1 |
| [[LRRN2]] | B | LRRN2 activity raises SMO's level | lines that do not express LRRN2 (30) vs lines expressing it (20) | 1.84× lower at baseline in the lines without LRRN2 | 0.055 | ⚠ within organs, on part of the lines; also absent: LGSN, KIF1A, NEFL |
| [[PRAME]] | B | PRAME activity raises SMO's level | lines that do not express PRAME (25) vs lines expressing it (25) | 2.41× lower at baseline in the lines without PRAME | 0.055 | ⚠ within organs, on part of the lines; also absent: GLDC, NR0B1, PAX2 |
| [[B4GALNT4]] | B | B4GALNT4 activity strengthens SMO's drug response | lines that do not express B4GALNT4 (8) vs lines expressing it (23) | the lines without B4GALNT4 respond 0.54× as strongly (z diff +2.12); strongest at Homoharringtonine 5 µM: 0.61x vs 0.34x (z diff +4.1) | 0.056 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A; target measured in part of the lines; artifact flags |
| [[MINDY4]] | B | MINDY4 activity raises SMO's level | lines that do not express MINDY4 (5) vs lines expressing it (45) | 2.73× lower at baseline in the lines without MINDY4 | 0.068 | ⚠ within organs, on part of the lines; also absent: MPP4, DPH6-DT, CFAP58; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYNGR1]] | B | SMO activity raises SYNGR1's level | lines that do not express SMO (17) vs lines expressing it (33) | 2.43× lower at baseline in the lines without SMO | 0.046 | ⚠ within organs, on part of the lines; also absent: RADIL, DUSP9, APBA2 |
| [[AKAP7]] | B | SMO activity raises AKAP7's level | lines that do not express SMO (17) vs lines expressing it (33) | 1.68× lower at baseline in the lines without SMO | 0.060 | ⚠ within organs, on part of the lines; also absent: RADIL, DUSP9, APBA2 |
| [[ZNF346]] | B | SMO activity raises ZNF346's level | lines that do not express SMO (17) vs lines expressing it (33) | 1.42× lower at baseline in the lines without SMO | 0.078 | ⚠ within organs, on part of the lines; also absent: RADIL, DUSP9, APBA2 |
| [[PDE8B]] | B | SMO activity raises PDE8B's level | lines that do not express SMO (17) vs lines expressing it (33) | 1.68× lower at baseline in the lines without SMO | 0.091 | ⚠ within organs, on part of the lines; also absent: RADIL, DUSP9, APBA2 |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.479). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-12.6, 18.7); signed map (-26.2, -21.8). **Vector** length 71.7, 15.5% of its response variance represented; |z| ≥ 3 in 861 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.3 | +9.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.5 | +10.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.0 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +6.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +5.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | -0.6 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.1 | +1.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -16.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -13.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.4 | -14.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.3 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -3.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -0.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | smoothened, frizzled class receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.1 — chr7:129,188,633-129,213,545 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FZD11; previously SMOH |
| Gene groups (HGNC) | G protein-coupled receptors, Class F frizzled |
| Reactome | 12 pathways, smallest: Activation of SMO; BBSome-mediated cargo-targeting to cilium; Class B/2 (Secretin family receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99835](https://www.uniprot.org/uniprotkb/Q99835) (Protein smoothened):

> G protein-coupled receptor, which transduces the smoothened signaling pathway. Activated by cholesterol in response to hedgehog (DHH, IHH or SHH) morphogens. In absence of hedgehog, SMO is inactivated by patched protein (PTCH1 or PTCH2), which prevents SMO access to cholesterol. In response to hedgehog-binding to pathched, inhibition is relieved, promoting SMO translocation to primary cilium and activation by cholesterol: cholesterol causes a conformation change that triggers signaling via G …

**Summary**, from NCBI Gene [6608](https://www.ncbi.nlm.nih.gov/gene/6608):

> The protein encoded by this gene is a G protein-coupled receptor that interacts with the patched protein, a receptor for hedgehog proteins. The encoded protein tranduces signals to other proteins after activation by a hedgehog protein/patched protein complex. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:11119](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11119) · Entrez [6608](https://www.ncbi.nlm.nih.gov/gene/6608) · UniProt [Q99835](https://www.uniprot.org/uniprotkb/Q99835) · Ensembl [ENSG00000128602](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128602)

## Data

Gene col 4902: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4902); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4902, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4902]; `tensor/DDL_lfc|DDL_z.npy` [4902]; `embed/gene_vectors.npy` [4902]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4902 or target_col == 4902). Every well: [[SMO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
