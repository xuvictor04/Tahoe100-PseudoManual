---
symbol: "NSF"
type: "gene"
col: 1066
ensembl_id: "ENSG00000073969"
name: "N-ethylmaleimide sensitive factor, vesicle fusing ATPase"
location: "17q21.31"
module: 134
arm: "+"
pooled_cpm: 42.0
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# NSF

*N-ethylmaleimide sensitive factor, vesicle fusing ATPase* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.63× (z +10.3, q 4e-22, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.613× (z -9.9, q 2e-20, down in 34 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.684× (z -8.0, q 3e-13, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NSFP1]] (+0.52, fdr 2e-05), [[NDUFB8]] (+0.50, fdr 4e-05), [[UBE2V2]] (+0.49, fdr 2e-05); moves opposite to [[FAM85B]] (-0.50, fdr 3e-05), [[CTTN-DT]] (-0.47, fdr 2e-04), [[TMEM69]] (-0.44, fdr 2e-04).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HYDIN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1066.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.63×** | +10.3 | 4e-22 | 32/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +9.3 | 3e-18 | 33/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +5.3 | 2e-05 | 26/47 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.24×** | +4.4 | 0.002 | 20/47 (A-172, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.25×** | +4.3 | 0.002 | 13/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +4.2 | 0.003 | 12/48 (HEC-1-A, KATO III, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.21×** | +4.0 | 0.004 | 16/48 (A549, SK-MEL-2, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.20× | +4.0 | 0.004 | 12/48 (HEC-1-A, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.004 | 16/47 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.20× | +3.8 | 0.008 | 13/49 (A-172, HEC-1-A, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.17× | +3.3 | 0.049 | 21/48 (A-172, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.2 | 0.070 | 13/48 (CHP-212, SW480, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.12× | +3.1 | 0.070 | 10/48 (SW480, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.14× | +3.1 | 0.070 | 14/49 (A-172, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.0 | 0.096 | 8/48 (A498, A549, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1066.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.613×** | -9.9 | 2e-20 | 34/47 (NCI-H460, C-33 A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.641×** | -9.4 | 2e-18 | 33/47 (SW48, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.684×** | -8.0 | 3e-13 | 30/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.697×** | -7.6 | 4e-12 | 28/46 (Panc 03.27, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.682×** | -7.5 | 9e-12 | 26/43 (HT-29, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.787×** | -7.1 | 1e-10 | 22/47 (C32, A-172, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.543×** | -6.7 | 1e-09 | 32/49 (A-427, SW1417, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.555×** | -6.5 | 6e-09 | 28/48 (LOX-IMVI, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.748×** | -5.9 | 2e-07 | 24/48 (C32, NCI-H460, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.779×** | -5.3 | 8e-06 | 24/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.854× | -4.7 | 1e-04 | 22/48 (KATO III, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.806×** | -4.5 | 3e-04 | 19/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **0.816×** | -4.3 | 8e-04 | 19/46 (CHP-212, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.816×** | -4.3 | 8e-04 | 24/48 (C32, HT-29, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.685×** | -4.2 | 0.001 | 17/35 (C32, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM |  | **0.828×** | -4.0 | 0.002 | 12/48 (HOP62, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.832×** | -3.9 | 0.004 | 17/47 (NCI-H1792, NCI-H460, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.837× | -3.7 | 0.005 | 15/48 (Panc 03.27, C32, …) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **0.833×** | -3.7 | 0.006 | 16/47 (NCI-H2030, Panc 03.27, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.851× | -3.4 | 0.017 | 9/48 (NCI-H460, SNU-423, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.855× | -3.3 | 0.023 | 18/48 (KATO III, C32, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.859× | -3.2 | 0.031 | 7/48 (NCI-H2030, BT-474, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.810×** | -3.2 | 0.033 | 10/48 (CFPAC-1, LS 180, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1066. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 91.4 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -24.4) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.383× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 47.6 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.205× (z -17.3) |
| [[NCI-H1792 (line)]] | alt | 72.3 | 0 | 5 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 56.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.178× (z -9.1) |
| [[J82 (line)]] | alt | 31.2 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.15× (z +9.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.262× (z -10.9) ⚠ toxic |
| [[SW 900 (line)]] | alt | 47.6 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.287× (z -11.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 41.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.98× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.486× (z -8.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 40.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 71.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -12.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 48.3 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0892× (z -11.7) ⚠ transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.140× (z -9.5) |
| [[HOP62 (line)]] | alt | 41.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.365× (z -10.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 44.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.306× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 28.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -11.2) ⚠ cell-cycle shift, explains ~86% of this change |
| [[A-427 (line)]] | wt | 54.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -12.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 44.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -9.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 23.7 | 0 | 1 | — | [[Hydroxyfasudil (drug)]] 5 µM 0.0815× (z -8.7) |
| [[HT-29 (line)]] | alt | 48.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 34.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.283× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 37.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.328× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 56.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.462× (z -8.8) ⚠ transcription drop; cell-cycle shift, explains ~60% of this change |
| [[Panc 03.27 (line)]] | alt | 39.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -15.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.471× (z -8.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[RKO (line)]] | wt | 44.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.142× (z -15.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 40.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.323× (z -9.0) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 37.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -9.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 37.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -8.5) ⚠ cell-cycle shift, explains ~86% of this change |
| [[SW48 (line)]] | wt | 43.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0647× (z -16.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1066), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSFP1]] | +0.52 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[NDUFB8]] | +0.50 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[UBE2V2]] | +0.49 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[PPFIA1]] | +0.48 | +0.44 / +0.45 | both halves | 3e-05 | pathway: Neuronal System |
| [[DPYSL4]] | +0.47 | +0.40 / +0.44 | both halves | 5e-05 |  |
| [[CABIN1]] | +0.47 | +0.31 / +0.49 | both halves | 2e-04 |  |
| [[MED27]] | +0.47 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[ABCD3]] | +0.45 | +0.36 / +0.47 | both halves | 1e-04 |  |
| [[ASCC3]] | +0.45 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[BNIP3]] | +0.43 | +0.37 / +0.36 | both halves | 1e-04 |  |
| [[SPTSSA]] | +0.42 | +0.41 / +0.40 | both halves | 4e-05 |  |
| [[NBAS]] | +0.42 | +0.28 / +0.37 | both halves | 3e-04 | pathway: COPI-dependent Golgi-to-ER retrograde traffic; STRING 613 |

## Genes that move opposite

*44 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM85B]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[CTTN-DT]] | -0.47 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[TMEM69]] | -0.44 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[MTURN]] | -0.42 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[FAM161A]] | -0.42 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[ENTREP1]] | -0.42 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[KCNN2]] | -0.41 | -0.37 / -0.30 | both halves | 2e-04 | pathway: Neuronal System |
| [[FZD4-DT]] | -0.41 | -0.23 / -0.46 | both halves | 5e-04 |  |
| [[PRDM4]] | -0.41 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[EIF3J-DT]] | -0.40 | -0.18 / -0.41 | ⚠ not reproduced | 1e-03 |  |
| [[MTMR9LP]] | -0.40 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[LINC02614]] | -0.40 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[ABCA15P]] | -0.40 | -0.28 / -0.37 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HYDIN]] | B | HYDIN activity raises NSF's level | lines that do not express HYDIN (9) vs lines expressing it (41) | 1.15× lower at baseline in the lines without HYDIN | 0.096 | ⚠ within organs, on part of the lines; also absent: SNRPN, ZNF613, MOCS1; maybe low, not absent |
| [[LINC02614]] | C | LINC02614 activity lowers NSF's level | lines that do not express LINC02614 (3) vs lines expressing it (47) | 1.24× higher at baseline in the lines without LINC02614 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CDC45, CDC20, PKMYT1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.400). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-25.4, 19.5); signed map (-38.2, 27.2). **Vector** length 84.5, 18.5% of its response variance represented; |z| ≥ 3 in 1,074 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.0 | +1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +2.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.0 | +9.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +5.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | -0.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.8 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.2 | -4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.4 | -3.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.9 | -9.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.7 | -7.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | +1.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | N-ethylmaleimide sensitive factor, vesicle fusing ATPase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:46,590,669-46,757,679 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SKD2, SEC18 |
| Gene groups (HGNC) | AAA ATPases |
| Reactome | 18 pathways, smallest: Trafficking of GluR2-containing AMPA receptors; Glutamate binding, activation of AMPA receptors and synaptic plasticity; Trafficking of AMPA receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P46459](https://www.uniprot.org/uniprotkb/P46459) (Vesicle-fusing ATPase):

> Required for vesicle-mediated transport. Catalyzes the fusion of transport vesicles within the Golgi cisternae. Is also required for transport from the endoplasmic reticulum to the Golgi stack. Seems to function as a fusion protein required for the delivery of cargo proteins to all compartments of the Golgi stack independent of vesicle origin. Interaction with AMPAR subunit GRIA2 leads to influence GRIA2 membrane cycling (By similarity).

**Summary**, from NCBI Gene [4905](https://www.ncbi.nlm.nih.gov/gene/4905):

> Enables PDZ domain binding activity and ionotropic glutamate receptor binding activity. Involved in intracellular protein transport; positive regulation of protein catabolic process; and positive regulation of receptor recycling. Located in cytosol and plasma membrane. Implicated in cocaine dependence and developmental and epileptic encephalopathy 96. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:8016](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8016) · Entrez [4905](https://www.ncbi.nlm.nih.gov/gene/4905) · UniProt [P46459](https://www.uniprot.org/uniprotkb/P46459) · Ensembl [ENSG00000073969](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073969)

## Data

Gene col 1066: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1066); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1066, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1066]; `tensor/DDL_lfc|DDL_z.npy` [1066]; `embed/gene_vectors.npy` [1066]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1066 or target_col == 1066). Every well: [[NSF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
