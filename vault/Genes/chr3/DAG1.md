---
symbol: "DAG1"
type: "gene"
col: 10378
ensembl_id: "ENSG00000173402"
name: "dystroglycan 1"
location: "3p21.31"
module: 50
arm: "+"
pooled_cpm: 54.12
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 16
n_dd_up_clean: 14
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# DAG1

*dystroglycan 1* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.29× (z +14.5, q 1e-44, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.377× (z -16.5, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HYAL2]] (+0.68, fdr 1e-05), [[FAM234A]] (+0.68, fdr 1e-05), [[CELSR2]] (+0.67, fdr 1e-05); moves opposite to [[N4BP2L2]] (-0.61, fdr 1e-05), [[CCDC59]] (-0.60, fdr 1e-05), [[GATAD1]] (-0.59, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10378.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.29×** | +14.5 | 1e-44 | 46/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +12.6 | 6e-34 | 40/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +9.1 | 1e-17 | 40/48 (SW1417, HOP62, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +5.2 | 3e-05 | 30/48 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.66×** | +4.6 | 4e-04 | 27/48 (NCI-H2347, A498, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.27×** | +4.1 | 0.003 | 20/47 (RPMI-7951, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.57×** | +4.1 | 0.003 | 28/48 (HOP62, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.014 | 17/48 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.014 | 18/48 (A-172, LS 180, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.5 | 0.028 | 16/48 (HOP62, C32, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.033 | 18/47 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.038 | 19/47 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.042 | 14/48 (NCI-H460, Hs 766T, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.048 | 15/48 (RPMI-7951, LS 180, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.20×** | +3.2 | 0.049 | 17/47 (NCI-H460, SW480, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.060 | 18/47 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10378.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.377×** | -16.5 | 0e+00 | 43/48 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.430×** | -14.8 | 0e+00 | 41/48 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.451×** | -14.0 | 5e-42 | 44/47 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.535×** | -11.0 | 8e-26 | 43/48 (HT-29, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.566×** | -10.0 | 2e-21 | 38/48 (NCI-H1573, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.573×** | -9.8 | 1e-20 | 37/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.613×** | -8.6 | 8e-16 | 37/48 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.736×** | -7.6 | 2e-12 | 30/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.657×** | -7.1 | 9e-11 | 36/48 (HepG2/C3A, AN3 CA, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.685×** | -6.6 | 2e-09 | 28/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.564×** | -5.2 | 8e-06 | 24/43 (NCI-H2030, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.738×** | -5.1 | 2e-05 | 28/48 (A498, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.790×** | -4.1 | 0.002 | 24/48 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.793×** | -4.1 | 0.002 | 26/48 (A498, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.797×** | -4.0 | 0.002 | 24/48 (A498, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.774×** | -3.2 | 0.043 | 14/48 (A498, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10378. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 64.8 | 18 (2 ⚠) | 10 (4 ⚠) | [[Trametinib (drug)]] 0.5 µM 3.10× (z +14.7) | [[Harringtonine (drug)]] 0.5 µM 0.203× (z -17.3) |
| [[A-172 (line)]] | wt | 63.2 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -23.0) |
| [[SW480 (line)]] | alt | 49.9 | 3 | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.62× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.421× (z -10.8) |
| [[A498 (line)]] | wt | 37.4 | 3 (1 ⚠) | 5 | [[Panobinostat (drug)]] 5 µM 2.43× (z +9.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -20.5) |
| [[HS-578T (line)]] | alt | 77.3 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -18.5) |
| [[A-427 (line)]] | wt | 81.2 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.463× (z -11.3) |
| [[HOP62 (line)]] | alt | 38.5 | 4 | 2 | [[Panobinostat (drug)]] 5 µM 3.66× (z +11.7) | [[Harringtonine (drug)]] 5 µM 0.203× (z -13.9) |
| [[A549 (line)]] | wt | 42.7 | 1 | 4 | [[Panobinostat (drug)]] 5 µM 3.09× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -15.0) |
| [[LoVo (line)]] | wt | 41.3 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0567× (z -30.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.291× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 31.2 | 1 | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.06× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.219× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.323× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 29.4 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.185× (z -14.1) |
| [[PANC-1 (line)]] | alt | 51.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -15.6) |
| [[RKO (line)]] | wt | 43.9 | 1 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.06× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -11.8) |
| [[HepG2_C3A (line)]] | wt | 83.8 | 0 | 4 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.200× (z -12.4) |
| [[J82 (line)]] | alt | 72.2 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.54× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -13.7) |
| [[NCI-H2030 (line)]] | alt | 66.7 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.312× (z -12.9) |
| [[NCI-H23 (line)]] | alt | 46.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -16.0) |
| [[Panc 03.27 (line)]] | alt | 75.0 | 2 | 2 | [[Panobinostat (drug)]] 5 µM 3.18× (z +10.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.377× (z -9.3) |
| [[SNU-1 (line)]] | wt | 62.0 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.196× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.239× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 74.1 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.31× (z +10.5) | [[Auranofin (drug)]] 5 µM 0.451× (z -10.1) |
| [[Hs 766T (line)]] | wt | 40.2 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 3.26× (z +8.6) | [[Harringtonine (drug)]] 5 µM 0.215× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 45.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0792× (z -23.0) |
| [[SW1417 (line)]] | alt | 105 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.22× (z +14.1) | — |
| [[AN3 CA (line)]] | alt | 96.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 44.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.51× (z +10.0) | [[Lonafarnib (drug)]] 5 µM 0.115× (z -9.0) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 26.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +10.4) | — |
| [[CHP-212 (line)]] | wt | 37.3 | 0 | 2 | — | [[Isocorydine (drug)]] 0.5 µM 0.0790× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 28.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +9.6) | — |
| [[KATO III (line)]] | alt | 88.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.297× (z -9.7) |
| [[LS 180 (line)]] | wt | 47.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 55.8 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.207× (z -11.2) |
| [[SNU-423 (line)]] | alt | 30.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +9.9) | — |
| [[SW 1271 (line)]] | alt | 51.6 | 0 | 2 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0547× (z -10.5) |
| [[SW 900 (line)]] | alt | 41.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -10.3) |
| [[C-33 A (line)]] | alt | 79.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.383× (z -8.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 75.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.347× (z -8.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 34.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.264× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 64.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.56× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 73.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.353× (z -8.7) |
| [[SW48 (line)]] | wt | 58.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.270× (z -9.5) |
| [[BT-474 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10378), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HYAL2]] | +0.68 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[FAM234A]] | +0.68 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[CELSR2]] | +0.67 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[SLC25A39]] | +0.66 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[NAGA]] | +0.65 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ATP5F1B]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[CALM3]] | +0.63 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[COLGALT1]] | +0.63 | +0.53 / +0.60 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[BSG]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[ADAM15]] | +0.62 | +0.55 / +0.57 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[BLTP2]] | +0.62 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[NOMO3]] | +0.62 | +0.49 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N4BP2L2]] | -0.61 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[CCDC59]] | -0.60 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[GATAD1]] | -0.59 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[ZNF721]] | -0.58 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[TATDN1]] | -0.57 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[ZNF791]] | -0.56 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[FCF1]] | -0.56 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[ZC3HC1]] | -0.55 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[MRPL45P2]] | -0.55 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[TMEM192]] | -0.55 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[ZBTB8OS]] | -0.55 | -0.56 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers DAG1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[L1CAM]] | B | L1CAM activity raises DAG1's level | lines that do not express L1CAM (22) vs lines expressing it (28) | 1.16× lower at baseline in the lines without L1CAM | 0.080 | ⚠ within organs, on part of the lines; also absent: ELFN1, PDZD4, ARHGAP28 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.664). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.1, -24.9); signed map (-28.5, -40.0). **Vector** length 118, 34.6% of its response variance represented; |z| ≥ 3 in 1,357 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +6.5 | +14.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.0 | +12.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.6 | +9.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.1 | +4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.1 | +3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.0 | +4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.9 | +2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +2.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.3 | -11.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.1 | -16.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.0 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -14.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -5.0 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -4.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.3 | -0.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | dystroglycan 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,468,713-49,535,618 (+) |
| Ensembl biotype | protein_coding |
| Also known as | A3a, 156DAG, AGRNR, DAG |
| Reactome | 20 pathways, smallest: Defective POMT1 causes MDDGA1, MDDGB1 and MDDGC1; Defective POMT2 causes MDDGA2, MDDGB2 and MDDGC2; DAG1 core M1 glycosylations |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14118](https://www.uniprot.org/uniprotkb/Q14118) (Dystroglycan 1):

> The dystroglycan complex is involved in a number of signaling events and processes including laminin deposition and extracellular matrix assembly, acetylcholine receptor clustering, sarcolemmal stability, cell survival, peripheral nerve myelination, nodal structure, cell migration, epithelial polarization, and epithelium branching morphogenesis (By similarity). Required for the formation of photoreceptor ribbon synapses, and long-term maintenance of inhibitory synapses in cerebellar Purkinje …

**Summary**, from NCBI Gene [1605](https://www.ncbi.nlm.nih.gov/gene/1605):

> This gene encodes dystroglycan, a central component of dystrophin-glycoprotein complex that links the extracellular matrix and the cytoskeleton in the skeletal muscle. The encoded preproprotein undergoes O- and N-glycosylation, and proteolytic processing to generate alpha and beta subunits. Certain mutations in this gene are known to cause distinct forms of muscular dystrophy. Alternative splicing results in multiple transcript variants, all encoding the same protein. [provided by RefSeq, Nov …

**Accessions** — [HGNC:2666](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2666) · Entrez [1605](https://www.ncbi.nlm.nih.gov/gene/1605) · UniProt [Q14118](https://www.uniprot.org/uniprotkb/Q14118) · Ensembl [ENSG00000173402](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173402)

## Data

Gene col 10378: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10378); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10378, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10378]; `tensor/DDL_lfc|DDL_z.npy` [10378]; `embed/gene_vectors.npy` [10378]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10378 or target_col == 10378). Every well: [[DAG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DAG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
