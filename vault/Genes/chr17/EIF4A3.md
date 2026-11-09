---
symbol: "EIF4A3"
type: "gene"
col: 6541
ensembl_id: "ENSG00000141543"
name: "eukaryotic translation initiation factor 4A3"
location: "17q25.3"
module: 99
arm: "+"
pooled_cpm: 65.87
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 4
n_dd_up_clean: 27
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# EIF4A3

*eukaryotic translation initiation factor 4A3* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 4.27× (z +18.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.676× (z -5.1, q 2e-04, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FEM1C]] (+0.64, fdr 1e-05), [[FAM162A]] (+0.63, fdr 1e-05), [[NCKIPSD]] (+0.62, fdr 1e-05); moves opposite to [[NDUFS1]] (-0.62, fdr 2e-05), [[UPF3A]] (-0.52, fdr 5e-05), [[AMMECR1]] (-0.52, fdr 7e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CRYBG3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6541.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **4.27×** | +18.6 | 0e+00 | 48/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.74×** | +16.9 | 0e+00 | 48/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.85×** | +13.4 | 8e-39 | 47/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.04×** | +12.6 | 3e-34 | 47/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.97×** | +12.2 | 2e-32 | 36/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.58×** | +12.1 | 7e-32 | 47/48 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +11.6 | 2e-29 | 42/49 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.52×** | +10.5 | 7e-24 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.39×** | +9.9 | 4e-21 | 44/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.96×** | +8.6 | 4e-16 | 46/48 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.42×** | +8.2 | 9e-15 | 44/49 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.89×** | +8.2 | 1e-14 | 41/48 (A-427, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.76×** | +7.2 | 3e-11 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.63×** | +6.2 | 2e-08 | 38/48 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~21% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +6.0 | 1e-07 | 33/48 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +5.1 | 9e-06 | 34/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +4.7 | 9e-05 | 31/48 (HEC-1-A, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.01×** | +4.7 | 1e-04 | 29/48 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.99×** | +4.6 | 1e-04 | 38/48 (SHP-77, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.94×** | +4.4 | 3e-04 | 32/48 (SK-MEL-2, A-172, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6541.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.676×** | -5.1 | 2e-04 | 38/48 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.709×** | -3.9 | 0.024 | 28/48 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.818×** | -3.7 | 0.044 | 24/49 (SK-MEL-2, CFPAC-1, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.734×** | -3.5 | 0.059 | 25/48 (J82, HEC-1-A, …) | two highest doses | position effect removed |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.838× | -3.2 | 0.12 | 15/49 (HCT15, A498, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.771× | -3.2 | 0.12 | 21/43 (SW48, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6541. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 55.9 | 14 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 25.6× (z +25.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 24.1× (z +25.1) | — |
| [[SW480 (line)]] | alt | 55.9 | 11 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.48× (z +17.2) | — |
| [[PANC-1 (line)]] | alt | 51.1 | 10 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.67× (z +21.4) | — |
| [[KATO III (line)]] | alt | 99.0 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.01× (z +23.5) | — |
| [[HOP62 (line)]] | alt | 55.9 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.09× (z +16.0) | — |
| [[HT-29 (line)]] | alt | 43.9 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +12.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.84× (z +12.4) | — |
| [[SW 900 (line)]] | alt | 57.0 | 7 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.98× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.94× (z +11.4) | — |
| [[LoVo (line)]] | wt | 60.8 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.41× (z +12.9) | — |
| [[LS 180 (line)]] | wt | 50.8 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 11.2× (z +19.8) | — |
| [[NCI-H1573 (line)]] | alt | 38.0 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.72× (z +16.1) | — |
| [[NCI-H1792 (line)]] | alt | 61.0 | 6 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 10.8× (z +15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 10.1× (z +15.1) | — |
| [[SW1417 (line)]] | alt | 70.1 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.88× (z +12.2) | — |
| [[H4 (line)]] | wt | 51.0 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.63× (z +11.8) | — |
| [[Hs 766T (line)]] | wt | 36.6 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.80× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 58.4 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.40× (z +13.4) | — |
| [[SK-MEL-2 (line)]] | alt | 119 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.59× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -9.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 56.1 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.52× (z +11.3) | — |
| [[A-427 (line)]] | wt | 71.8 | 2 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.64× (z +11.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.309× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 48.9 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.54× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.289× (z -8.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 97.0 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.25× (z +13.5) | — |
| [[J82 (line)]] | alt | 65.5 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.51× (z +12.2) | — |
| [[SNU-1 (line)]] | wt | 56.0 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.35× (z +12.2) | — |
| [[A-172 (line)]] | wt | 61.3 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.20× (z +10.1) | — |
| [[A549 (line)]] | wt | 66.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.65× (z +10.3) | — |
| [[COLO 205 (line)]] | alt | 37.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +10.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.22× (z +10.0) | — |
| [[HepG2_C3A (line)]] | wt | 68.5 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.19× (z +10.5) | — |
| [[HS-578T (line)]] | alt | 52.7 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.76× (z +10.7) | — |
| [[hTERT-HPNE (line)]] | wt | 71.1 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.05× (z +11.3) | — |
| [[NCI-H23 (line)]] | alt | 59.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.35× (z +10.6) | — |
| [[SW48 (line)]] | wt | 80.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.65× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.0714× (z -16.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 49.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.04× (z +10.3) | — |
| [[AN3 CA (line)]] | alt | 71.4 | 1 | 1 | [[Auranofin (drug)]] 5 µM 5.57× (z +8.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 79.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.8) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[HEC-1-A (line)]] | alt | 76.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.04× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 148 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.54× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 87.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.58× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -8.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 74.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.37× (z +11.6) | — |
| [[RKO (line)]] | wt | 68.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 75.9 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +10.4) | — |
| [[C-33 A (line)]] | alt | 70.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.74× (z +10.0) | — |
| [[C32 (line)]] | wt | 70.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +9.2) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[LOX-IMVI (line)]] | wt | 102 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.62× (z +11.4) | — |
| [[RPMI-7951 (line)]] | alt | 52.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.04× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6541), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FEM1C]] | +0.64 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[FAM162A]] | +0.63 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[NCKIPSD]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SNAI1]] | +0.62 | +0.43 / +0.63 | both halves | 4e-05 |  |
| [[PGK1]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 | STRING 545 |
| [[BNIP3]] | +0.61 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[HILPDA]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ERO1A]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[SLC2A1]] | +0.60 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[FAM210A]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[P4HA1]] | +0.58 | +0.47 / +0.56 | both halves | 2e-05 | pathway: Dengue Virus Genome Translation and Replication |
| [[WDR45B]] | +0.58 | +0.42 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFS1]] | -0.62 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[UPF3A]] | -0.52 | -0.39 / -0.47 | both halves | 5e-05 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC); STRING 999 |
| [[AMMECR1]] | -0.52 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[ETFA]] | -0.51 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[ZNF253]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ATG2B]] | -0.49 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[C9orf85]] | -0.49 | -0.52 / -0.37 | both halves | 9e-05 |  |
| [[MCCC2]] | -0.49 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[DNAJB14]] | -0.48 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[CCT6P1]] | -0.47 | -0.45 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRYBG3]] | C | CRYBG3 activity lowers EIF4A3's level | lines that do not express CRYBG3 (3) vs lines expressing it (47) | 1.72× higher at baseline in the lines without CRYBG3 | 0.082 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPR137B, PAM, DTX3L |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.6, -15.3); signed map (-37.0, 27.4). **Vector** length 87.7, 29.9% of its response variance represented; |z| ≥ 3 in 1,172 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.51 to 17); *mTORC1 signaling* (hallmark, mean cos +0.52 to 15); *Glycolysis* (reactome, mean cos +0.51 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +16.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +12.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | +4.0 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +8.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.3 | +1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +4.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.9 | +0.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | -7.5 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.6 | +12.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | +6.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.3 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.8 | +4.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.6 | -3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -5.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | +4.7 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 4A3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:80,134,369-80,147,151 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0111, EIF4AIII, Fal1; previously DDX48 |
| Gene groups (HGNC) | DEAD-box helicases; Exon junction complex; SSU processome; Spliceosomal Bact complex; Spliceosomal P complex |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 26 pathways, smallest: Z-decay: degradation of maternal mRNAs by zygotically expressed factors; Deadenylation of mRNA; M-decay: degradation of maternal mRNAs by maternally stored factors |
| Matched by | ensembl_id |

**Function**, from UniProt [P38919](https://www.uniprot.org/uniprotkb/P38919) (Eukaryotic initiation factor 4A-III):

> ATP-dependent RNA helicase. Involved in pre-mRNA splicing as component of the spliceosome. Core component of the splicing-dependent multiprotein exon junction complex (EJC) deposited at splice junctions on mRNAs. The EJC is a dynamic structure consisting of core proteins and several peripheral nuclear and cytoplasmic associated factors that join the complex only transiently either during EJC assembly or during subsequent mRNA metabolism. The EJC marks the position of the exon-exon junction in …

**Summary**, from NCBI Gene [9775](https://www.ncbi.nlm.nih.gov/gene/9775):

> This gene encodes a member of the DEAD box protein family. DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure, such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this family are believed to be involved in embryogenesis, …

**Accessions** — [HGNC:18683](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18683) · Entrez [9775](https://www.ncbi.nlm.nih.gov/gene/9775) · UniProt [P38919](https://www.uniprot.org/uniprotkb/P38919) · Ensembl [ENSG00000141543](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141543)

## Data

Gene col 6541: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6541); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6541, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6541]; `tensor/DDL_lfc|DDL_z.npy` [6541]; `embed/gene_vectors.npy` [6541]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6541 or target_col == 6541). Every well: [[EIF4A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF4A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
