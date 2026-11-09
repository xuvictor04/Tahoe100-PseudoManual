---
symbol: "SIK2"
type: "gene"
col: 9908
ensembl_id: "ENSG00000170145"
name: "salt inducible kinase 2"
location: "11q23.1"
module: 223
arm: "+"
pooled_cpm: 88.05
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 24
n_dd_up_clean: 8
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/223"]
generated_by: "tahoemap"
---

# SIK2

*salt inducible kinase 2* — 11q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.58× (z +7.9, q 2e-12, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.566× (z -9.7, q 2e-19, down in 37 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.406× (z -8.1, q 1e-13, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ID4]] (+0.48, fdr 4e-05), [[HNRNPA0]] (+0.48, fdr 2e-05), [[ATXN7L1]] (+0.48, fdr 2e-05); moves opposite to [[HPRT1]] (-0.47, fdr 5e-05), [[DENR]] (-0.47, fdr 7e-05), [[ZNF774]] (-0.47, fdr 5e-04).
> It is in [[Module 223]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9908.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +7.9 | 2e-12 | 37/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.39×** | +5.6 | 5e-06 | 33/48 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +5.4 | 1e-05 | 25/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +4.1 | 0.005 | 24/48 (PANC-1, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +4.1 | 0.005 | 23/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.9 | 0.010 | 20/49 (CFPAC-1, SW 900, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.014 | 21/48 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +3.7 | 0.014 | 19/48 (NCI-H23, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.18× | +3.6 | 0.017 | 18/48 (HepG2/C3A, NCI-H460, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.039 | 16/49 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.094 | 18/50 (NCI-H460, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.13 | 15/48 (NCI-H460, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9908.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.566×** | -9.7 | 2e-19 | 37/48 (SHP-77, LS 180, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.573×** | -8.8 | 4e-16 | 31/43 (KATO III, LoVo, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.406×** | -8.1 | 1e-13 | 42/49 (SW480, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.659×** | -7.1 | 2e-10 | 35/48 (SHP-77, RPMI-7951, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.669×** | -6.9 | 6e-10 | 31/48 (KATO III, SHP-77, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.669×** | -6.9 | 6e-10 | 35/48 (RPMI-7951, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.683×** | -6.5 | 6e-09 | 30/49 (NCI-H23, KATO III, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.683×** | -6.5 | 6e-09 | 33/48 (hTERT-HPNE, RPMI-7951, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.500×** | -6.2 | 4e-08 | 28/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.789×** | -5.7 | 7e-07 | 32/49 (CHP-212, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.712×** | -5.6 | 1e-06 | 25/42 (KATO III, SW480, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.742×** | -5.1 | 2e-05 | 29/48 (SHP-77, CHP-212, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.727×** | -4.7 | 1e-04 | 28/48 (SHP-77, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.771×** | -4.4 | 4e-04 | 29/48 (CHP-212, SW48, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.772×** | -4.4 | 4e-04 | 25/48 (SHP-77, KATO III, …) | rises with dose |  |
| [[Aprepitant (drug)]] 0.05 µM |  | **0.807×** | -3.6 | 0.008 | 21/48 (NCI-H661, SW 1088, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.810×** | -3.5 | 0.015 | 19/48 (NCI-H460, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.810×** | -3.4 | 0.015 | 22/50 (MIA PaCa-2, CHP-212, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.811×** | -3.4 | 0.015 | 20/49 (NCI-H2030, PANC-1, …) | top dose only | plate-row cell shift |
| [[Asciminib (drug)]] 0.05 µM |  | 0.838× | -3.0 | 0.056 | 12/48 (RKO, Panc 03.27, …) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.838× | -2.9 | 0.078 | 14/48 (A549, SW1417, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9908. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 316 | 0 | 14 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -18.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.233× (z -13.9) |
| [[KATO III (line)]] | alt | 183 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 125 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.347× (z -9.3) |
| [[PANC-1 (line)]] | alt | 80.3 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.91× (z +13.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.418× (z -10.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[CHP-212 (line)]] | wt | 296 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 134 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[NCI-H23 (line)]] | alt | 64.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 59.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.06× (z +12.0) ⚠ unreliable plate only | [[Lonafarnib (drug)]] 5 µM 0.177× (z -9.7) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 86.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.265× (z -11.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 84.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.216× (z -12.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 55.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.65× (z +10.3) | — |
| [[LoVo (line)]] | wt | 77.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 68.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.16× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -11.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 64.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[C-33 A (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[H4 (line)]] | wt | 80.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -11.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 109 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.160× (z -11.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 91.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HT-29 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 124 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.340× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 71.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.352× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 65.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[RKO (line)]] | wt | 44.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 136 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.368× (z -9.7) |
| [[SNU-1 (line)]] | wt | 32.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.124× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~37% of this change |
| [[SW48 (line)]] | wt | 77.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -13.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 106 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 87.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 62.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9908), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 6 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ID4]] | +0.48 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[HNRNPA0]] | +0.48 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ATXN7L1]] | +0.48 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[PHACTR4]] | +0.47 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[PKN2]] | +0.47 | +0.34 / +0.42 | both halves | 1e-04 |  |
| [[ID3]] | +0.47 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[C1QTNF3-AMACR]] | +0.47 | +0.55 / +0.30 | both halves | 2e-04 |  |
| [[PDK4]] | +0.46 | +0.44 / +0.37 | both halves | 8e-05 |  |
| [[NR4A2]] | +0.45 | +0.44 / +0.39 | both halves | 5e-05 |  |
| [[TRIR]] ⚠ | +0.44 | +0.44 / +0.43 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SLC7A2]] | +0.43 | +0.44 / +0.38 | both halves | 7e-05 |  |
| [[AHI1]] | +0.43 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[TOB1]] | +0.43 | +0.40 / +0.44 | both halves | 5e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPRT1]] | -0.47 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[DENR]] | -0.47 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[ZNF774]] | -0.47 | -0.23 / -0.33 | both halves | 5e-04 |  |
| [[MORC4]] | -0.45 | -0.36 / -0.28 | both halves | 3e-04 |  |
| [[RHCE]] | -0.45 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[MAP6]] | -0.45 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[SCAMP5]] | -0.43 | -0.18 / -0.36 | ⚠ not reproduced | 9e-04 |  |
| [[TMEM139-AS1]] | -0.43 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[HAGLR]] | -0.43 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[ANO7]] | -0.43 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[LINC00941]] | -0.42 | -0.45 / -0.37 | both halves | 7e-05 |  |
| [[CEP170P1]] | -0.42 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[STX6]] | -0.42 | -0.55 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SIK2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 223]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.418). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.1, 20.6); signed map (6.1, -12.0). **Vector** length 94.8, 25.9% of its response variance represented; |z| ≥ 3 in 1,144 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.3 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +4.9 | -6.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | +4.8 | -3.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.3 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.2 | -1.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.9 | +0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.0 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +3.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.5 | -7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | +0.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.6 | +0.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | salt inducible kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.1 — chr11:111,602,449-111,730,855 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0781, QIK, DKFZp434K1115, LOH11CR1I; previously SNF1LK2 |
| Gene groups (HGNC) | SIK family kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0K1](https://www.uniprot.org/uniprotkb/Q9H0K1) (Serine/threonine-protein kinase SIK2):

> Serine/threonine-protein kinase that plays a role in many biological processes such as fatty acid oxidation, autophagy, immune response or glucose metabolism. Phosphorylates 'Ser-794' of IRS1 in insulin-stimulated adipocytes, potentially modulating the efficiency of insulin signal transduction. Inhibits CREB activity by phosphorylating and repressing TORCs, the CREB-specific coactivators. Phosphorylates EP300 and thus inhibits its histone acetyltransferase activity. In turn, regulates the …

**Summary**, from NCBI Gene [23235](https://www.ncbi.nlm.nih.gov/gene/23235):

> Enables ATP binding activity; magnesium ion binding activity; and protein kinase activity. Involved in intracellular signal transduction; positive regulation of ERAD pathway; and protein autophosphorylation. Is active in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21680](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21680) · Entrez [23235](https://www.ncbi.nlm.nih.gov/gene/23235) · UniProt [Q9H0K1](https://www.uniprot.org/uniprotkb/Q9H0K1) · Ensembl [ENSG00000170145](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170145)

## Data

Gene col 9908: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9908); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9908, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9908]; `tensor/DDL_lfc|DDL_z.npy` [9908]; `embed/gene_vectors.npy` [9908]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9908 or target_col == 9908). Every well: [[SIK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
