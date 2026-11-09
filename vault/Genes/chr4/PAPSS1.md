---
symbol: "PAPSS1"
type: "gene"
col: 6245
ensembl_id: "ENSG00000138801"
name: "3'-phosphoadenosine 5'-phosphosulfate synthase 1"
location: "4q25"
module: 57
arm: "+"
pooled_cpm: 48.49
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 12
n_dd_up_clean: 15
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# PAPSS1

*3'-phosphoadenosine 5'-phosphosulfate synthase 1* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.13× (z +20.1, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.433× (z -22.3, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDRG3]] (+0.77, fdr 7e-06), [[POGLUT2]] (+0.76, fdr 7e-06), [[HACE1]] (+0.73, fdr 1e-05); moves opposite to [[SLC9A8]] (-0.70, fdr 1e-05), [[ERCC6L2]] (-0.70, fdr 2e-05), [[RAB30-DT]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[STRA6LP]], [[SUGT1P4-STRA6LP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6245.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.13×** | +20.1 | 0e+00 | 46/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.87×** | +16.7 | 0e+00 | 44/48 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.86×** | +16.5 | 0e+00 | 45/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +12.6 | 4e-34 | 42/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +11.9 | 2e-30 | 38/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.98×** | +9.5 | 2e-19 | 42/48 (PANC-1, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +7.2 | 6e-11 | 32/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +6.7 | 1e-09 | 26/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +5.6 | 1e-06 | 14/48 (C32, COLO 205, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +5.4 | 3e-06 | 20/48 (C32, SW48, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +4.8 | 9e-05 | 19/42 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +4.6 | 2e-04 | 15/48 (SW1417, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.12× | +4.2 | 0.001 | 12/48 (CHP-212, RPMI-7951, …) | top dose only | low cells (technical?) |
| [[Ipatasertib (drug)]] 5 µM |  | **1.35×** | +4.2 | 0.001 | 11/48 (C32, SW48, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.16× | +3.9 | 0.004 | 9/48 (HS-578T, HepG2/C3A, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.008 | 5/47 (HepG2/C3A, H4, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.15× | +3.5 | 0.013 | 6/47 (CFPAC-1, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6245.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.433×** | -22.3 | 0e+00 | 46/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.462×** | -20.6 | 0e+00 | 45/48 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.493×** | -18.9 | 0e+00 | 46/48 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.548×** | -15.5 | 0e+00 | 43/48 (AN3 CA, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.579×** | -14.6 | 0e+00 | 38/48 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.682×** | -14.4 | 3e-45 | 32/48 (HOP62, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.630×** | -12.4 | 4e-33 | 37/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.635×** | -12.1 | 5e-32 | 40/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.769×** | -7.0 | 1e-10 | 26/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.846× | -6.3 | 1e-08 | 23/48 (A-427, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -5.5 | 2e-06 | 17/48 (HOP62, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.814×** | -5.1 | 2e-05 | 19/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.827×** | -5.1 | 2e-05 | 17/47 (SK-MEL-2, NCI-H23, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.840× | -4.7 | 1e-04 | 18/47 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.838× | -4.6 | 2e-04 | 22/47 (hTERT-HPNE, A-427, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.865× | -3.9 | 0.003 | 12/48 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.873× | -3.6 | 0.008 | 5/48 (A-427, HOP62, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.888× | -3.2 | 0.039 | 7/48 (LS 180, COLO 205, …) | inconsistent across doses |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | 0.889× | -3.1 | 0.043 | 12/48 (SK-MEL-2, RKO, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6245. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 31.3 | 4 (1 ⚠) | 7 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.51× (z +10.7) | [[Harringtonine (drug)]] 0.5 µM 0.326× (z -13.1) |
| [[HOP62 (line)]] | alt | 56.7 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -21.8) |
| [[PANC-1 (line)]] | alt | 35.1 | 2 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -12.0) |
| [[A-172 (line)]] | wt | 55.7 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -13.2) |
| [[HT-29 (line)]] | alt | 50.1 | 2 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.53× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 43.1 | 2 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.86× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.255× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -13.3) |
| [[AsPC-1 (line)]] | alt | 41.8 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.77× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.340× (z -9.9) |
| [[A549 (line)]] | wt | 34.2 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.370× (z -9.1) |
| [[J82 (line)]] | alt | 30.4 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.54× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.309× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.493× (z -9.4) |
| [[KATO III (line)]] | alt | 38.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.124× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.239× (z -13.8) |
| [[LoVo (line)]] | wt | 42.8 | 2 | 2 | [[Tucidinostat (drug)]] 5 µM 1.82× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.364× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 39.0 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.09× (z +10.3) | [[Digitoxin (drug)]] 5 µM 0.380× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.392× (z -8.6) |
| [[RKO (line)]] | wt | 51.5 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.303× (z -14.6) |
| [[SW480 (line)]] | alt | 40.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.348× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.379× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 42.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.67× (z +10.4) | — |
| [[HepG2_C3A (line)]] | wt | 68.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.305× (z -9.2) |
| [[Hs 766T (line)]] | wt | 45.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.253× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.413× (z -11.7) |
| [[HS-578T (line)]] | alt | 54.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -10.9) |
| [[SW 900 (line)]] | alt | 46.5 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.257× (z -10.3) |
| [[SW1417 (line)]] | alt | 47.2 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.36× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.378× (z -10.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 69.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -14.0) |
| [[C32 (line)]] | wt | 53.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.78× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 78.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.294× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 62.0 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -11.3) |
| [[LOX-IMVI (line)]] | wt | 41.0 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.339× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 68.6 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.97× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.447× (z -10.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 57.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -12.7) |
| [[A-427 (line)]] | wt | 54.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -15.3) |
| [[COLO 205 (line)]] | alt | 27.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0513× (z -16.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 46.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.250× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 45.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.35× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 42.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.315× (z -10.5) |
| [[SNU-1 (line)]] | wt | 57.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -11.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 91.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6245), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG3]] | +0.77 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[POGLUT2]] | +0.76 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[HACE1]] | +0.73 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[MPP1]] | +0.73 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[ELP1]] | +0.73 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[SKIC3]] | +0.73 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[SKP2]] | +0.73 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.71 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[ANXA6]] | +0.70 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[WASF3]] | +0.69 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[HLTF]] | +0.69 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[ARL6]] | +0.69 | +0.61 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A8]] | -0.70 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.70 | -0.68 / -0.46 | both halves | 2e-05 |  |
| [[RAB30-DT]] | -0.68 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | -0.68 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[LINC01004]] | -0.66 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[ITPA]] | -0.66 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[UNK]] | -0.65 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[ZC3HC1]] | -0.65 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[ANKRD17-DT]] | -0.64 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[ZNF764]] | -0.64 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[ST7L]] | -0.64 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[ZBED5]] | -0.63 | -0.49 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STRA6LP]], [[SUGT1P4-STRA6LP]] | B | STRA6LP, SUGT1P4-STRA6LP activity lowers PAPSS1's level | lines that do not express STRA6LP, SUGT1P4-STRA6LP (9) vs lines expressing them (41) | 1.32× higher at baseline in the lines without STRA6LP, SUGT1P4-STRA6LP | 0.027 | ⚠ within organs, on part of the lines; also absent: CCDC180; co-absent genes |
| [[SORT1]] | B | SORT1 activity raises PAPSS1's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.20× lower at baseline in the lines without SORT1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.804). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.0, -7.1); signed map (-35.6, -13.1). **Vector** length 118, 33.4% of its response variance represented; |z| ≥ 3 in 1,293 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM |  | +6.2 | +12.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.1 | +16.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +11.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.3 | +9.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.9 | +16.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.8 | +4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.5 | +5.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +3.2 | +4.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.6 | -5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -8.1 | -18.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.5 | -14.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.3 | -20.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -12.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.4 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.7 | -7.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.9 | -5.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | 3'-phosphoadenosine 5'-phosphosulfate synthase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:107,590,276-107,720,234 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ATPSK1, PAPSS |
| Reactome | 9 pathways, smallest: Metabolism of ingested H2SeO4 and H2SeO3 into H2Se; Transport and metabolism of PAPS; Signaling by BRAF and RAF1 fusions |
| Matched by | ensembl_id |

**Function**, from UniProt [O43252](https://www.uniprot.org/uniprotkb/O43252) (Bifunctional 3'-phosphoadenosine 5'-phosphosulfate synthase 1):

> Bifunctional enzyme with both ATP sulfurylase and APS kinase activity, which mediates two steps in the sulfate activation pathway. The first step is the transfer of a sulfate group to ATP to yield adenosine 5'-phosphosulfate (APS), and the second step is the transfer of a phosphate group from ATP to APS yielding 3'-phosphoadenylylsulfate (PAPS: activated sulfate donor used by sulfotransferase). In mammals, PAPS is the sole source of sulfate; APS appears to be only an intermediate in the …

**Summary**, from NCBI Gene [9061](https://www.ncbi.nlm.nih.gov/gene/9061):

> Three-prime-phosphoadenosine 5-prime-phosphosulfate (PAPS) is the sulfate donor cosubstrate for all sulfotransferase (SULT) enzymes (Xu et al., 2000 [PubMed 10679223]). SULTs catalyze the sulfate conjugation of many endogenous and exogenous compounds, including drugs and other xenobiotics. In humans, PAPS is synthesized from adenosine 5-prime triphosphate (ATP) and inorganic sulfate by 2 isoforms, PAPSS1 and PAPSS2 (MIM 603005).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:8603](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8603) · Entrez [9061](https://www.ncbi.nlm.nih.gov/gene/9061) · UniProt [O43252](https://www.uniprot.org/uniprotkb/O43252) · Ensembl [ENSG00000138801](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138801)

## Data

Gene col 6245: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6245); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6245, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6245]; `tensor/DDL_lfc|DDL_z.npy` [6245]; `embed/gene_vectors.npy` [6245]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6245 or target_col == 6245). Every well: [[PAPSS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAPSS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
