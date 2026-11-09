---
symbol: "RBM10"
type: "gene"
col: 11338
ensembl_id: "ENSG00000182872"
name: "RNA binding motif protein 10"
location: "Xp11.3"
module: 51
arm: "+"
pooled_cpm: 69.17
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# RBM10

*RNA binding motif protein 10* — Xp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.66× (z +18.6, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.593× (z -13.4, q 3e-38, down in 39 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.643× (z -11.4, q 1e-27, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARMC5]] (+0.67, fdr 1e-05), [[HMGXB4]] (+0.64, fdr 1e-05), [[SPOP]] (+0.64, fdr 1e-05); moves opposite to [[MAPK9]] (-0.55, fdr 2e-05), [[HACD3]] (-0.54, fdr 3e-05), [[PIGF]] (-0.53, fdr 1e-04).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11338.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +18.6 | 0e+00 | 45/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +10.9 | 2e-25 | 41/48 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +9.5 | 3e-19 | 32/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +8.8 | 3e-16 | 36/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.71×** | +7.2 | 6e-11 | 34/49 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.61×** | +6.4 | 1e-08 | 29/48 (SW480, MIA PaCa-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.16× | +3.9 | 0.008 | 14/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | 1.16× | +3.9 | 0.008 | 20/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.6 | 0.018 | 14/48 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.2 | 0.067 | 4/48 (BT-474, NCI-H2030, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.11 | 19/47 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.13× | +3.1 | 0.11 | 12/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11338.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.593×** | -13.4 | 3e-38 | 39/48 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.619×** | -11.8 | 7e-30 | 32/42 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.643×** | -11.4 | 1e-27 | 42/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.653×** | -11.0 | 8e-26 | 40/48 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.692×** | -9.5 | 4e-19 | 41/48 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.692×** | -8.7 | 2e-16 | 29/45 (SNU-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.800×** | -8.1 | 6e-14 | 29/49 (RKO, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.752×** | -7.3 | 2e-11 | 35/48 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.843× | -6.2 | 4e-08 | 21/48 (A-172, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.800×** | -5.5 | 2e-06 | 24/48 (SW 900, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.803×** | -5.4 | 3e-06 | 27/50 (NCI-H2347, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.671×** | -5.4 | 4e-06 | 25/49 (CHP-212, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.830×** | -4.8 | 9e-05 | 23/48 (RKO, SNU-423, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.880× | -4.6 | 2e-04 | 12/48 (SK-MEL-2, BT-474, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.847× | -4.2 | 8e-04 | 18/48 (BT-474, CHP-212, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.855× | -4.0 | 0.002 | 17/48 (J82, A549, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.858× | -3.9 | 0.003 | 14/48 (BT-474, SNU-423, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.860× | -3.7 | 0.006 | 13/47 (A-427, NCI-H23, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.862× | -3.7 | 0.008 | 16/48 (NCI-H2347, J82, …) | top dose only |  |
| [[Erlotinib (drug)]] 5 µM |  | 0.875× | -3.3 | 0.029 | 10/47 (NCI-H2030, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11338. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 77.5 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +19.2) | — |
| [[SW480 (line)]] | alt | 109 | 7 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +15.0) | [[Panobinostat (drug)]] 0.5 µM 0.614× (z -9.3) |
| [[A549 (line)]] | wt | 80.2 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +16.1) | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -13.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 50.4 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.431× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 50.7 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -8.9) |
| [[LoVo (line)]] | wt | 56.2 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.452× (z -9.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 70.3 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -20.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 60.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.445× (z -10.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 62.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +12.5) | [[Dinaciclib (drug)]] 0.05 µM 0.392× (z -11.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 91.7 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.509× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 126 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +15.0) | — |
| [[NCI-H1573 (line)]] | alt | 57.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.447× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 69.0 | 2 | 1 (1 ⚠) | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 3.99× (z +13.4) | [[Trametinib (drug)]] 5 µM 0.313× (z -11.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[Panc 03.27 (line)]] | alt | 69.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -15.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 63.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.420× (z -8.7) |
| [[SW1417 (line)]] | alt | 95.2 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.486× (z -9.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 62.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -8.5) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.500× (z -8.5) |
| [[C32 (line)]] | wt | 59.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -12.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 72.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +12.3) | [[Lonafarnib (drug)]] 5 µM 0.244× (z -8.7) ⚠ toxic |
| [[J82 (line)]] | alt | 102 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -12.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 74.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +15.3) | — |
| [[SW 1088 (line)]] | alt | 80.2 | 0 | 2 (1 ⚠) | — | [[Arbutin (drug)]] 0.5 µM 0.0886× (z -9.0) |
| [[A-427 (line)]] | wt | 80.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.493× (z -9.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -11.4) ⚠ cell-cycle shift, explains ~9% of this change |
| [[AN3 CA (line)]] | alt | 79.6 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.233× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 44.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -10.5) ⚠ cell-cycle shift, explains ~9% of this change |
| [[BT-474 (line)]] | alt | 71.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -11.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 78.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.4) | — |
| [[HCT15 (line)]] | alt | 77.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -10.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 72.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 54.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -9.1) ⚠ cell-cycle shift, explains ~9% of this change |
| [[LS 180 (line)]] | wt | 49.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 56.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +13.6) | — |
| [[NCI-H661 (line)]] | alt | 55.0 | 0 | 1 | — | [[Cabozantinib (S-malate) (drug)]] 0.5 µM 0.0487× (z -12.3) |
| [[RPMI-7951 (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -11.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 47.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 67.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -14.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 96.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 70.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 82.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11338), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC5]] | +0.67 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[HMGXB4]] | +0.64 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[SPOP]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[RBM23]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 | same gene group |
| [[HELQ]] | +0.63 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[CCDC97]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[GOSR1]] | +0.62 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[RBM5]] | +0.62 | +0.45 / +0.62 | both halves | 3e-05 | same gene group; pathway: Dengue Virus-Host Interactions |
| [[CCDC174]] | +0.61 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[ZNF75A]] | +0.60 | +0.53 / +0.53 | both halves | 1e-05 | same gene group |
| [[DOHH]] | +0.60 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[EPC1]] | +0.59 | +0.53 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK9]] | -0.55 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[HACD3]] | -0.54 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PIGF]] | -0.53 | -0.63 / -0.35 | both halves | 1e-04 |  |
| [[APP]] | -0.53 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[EPS15]] | -0.53 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[NUTF2]] | -0.52 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[RPS18]] | -0.52 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[WRNIP1]] | -0.52 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[BCAP31]] | -0.52 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[HPRT1]] | -0.52 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[SLC41A3]] | -0.52 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[C1orf198]] | -0.51 | -0.51 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises RBM10's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.600). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-38.2, 5.3); signed map (-0.7, -14.1). **Vector** length 91.3, 21.5% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.7 | +18.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.0 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +8.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +0.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | -0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +1.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.1 | +2.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.0 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +1.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.0 | +0.9 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.3 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -3.2 | +3.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.1 | -6.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -0.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.0 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | +0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -5.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.3 — chrX:47,145,221-47,186,813 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DXS8237E, KIAA0122, GPATC9, ZRANB5, GPATCH9, S1-1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Zinc fingers RANBP2-type; G-patch domain containing; RNA binding motif containing; Spliceosomal A complex |
| Reactome | 10 pathways, smallest: Dengue virus activates/modulates innate and adaptive immune responses; mRNA Polyadenylation; mRNA 3'-end processing |
| Matched by | ensembl_id |

**Function**, from UniProt [P0DW28](https://www.uniprot.org/uniprotkb/P0DW28) (Ribosome biogenesis inhibitor MINAS-60):

> Acts as a late-stage inhibitor of pre-60S ribosome assembly by preventing pre-60S ribosome export from nucleus.

**Summary**, from NCBI Gene [8241](https://www.ncbi.nlm.nih.gov/gene/8241):

> This gene encodes a nuclear protein that belongs to a family proteins that contain an RNA-binding motif. The encoded protein associates with hnRNP proteins and may be involved in regulating alternative splicing. Defects in this gene are the cause of the X-linked recessive disorder, TARP syndrome. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:9896](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9896) · Entrez [8241](https://www.ncbi.nlm.nih.gov/gene/8241) · UniProt [P0DW28](https://www.uniprot.org/uniprotkb/P0DW28) · Ensembl [ENSG00000182872](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182872)

## Data

Gene col 11338: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11338); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11338, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11338]; `tensor/DDL_lfc|DDL_z.npy` [11338]; `embed/gene_vectors.npy` [11338]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11338 or target_col == 11338). Every well: [[RBM10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
