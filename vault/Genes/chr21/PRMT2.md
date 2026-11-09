---
symbol: "PRMT2"
type: "gene"
col: 8338
ensembl_id: "ENSG00000160310"
name: "protein arginine methyltransferase 2"
location: "21q22.3"
module: 74
arm: "+"
pooled_cpm: 102.4
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 35
n_dd_up_clean: 0
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# PRMT2

*protein arginine methyltransferase 2* — 21q22.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.266× (z -28.2, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RANBP10]] (+0.58, fdr 3e-05), [[BSDC1]] (+0.58, fdr 7e-06), [[UBE2B]] (+0.58, fdr 1e-05); moves opposite to [[ELOVL6]] (-0.57, fdr 3e-05), [[MBNL3]] (-0.55, fdr 1e-05), [[PTGFRN]] (-0.54, fdr 1e-04).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8338.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.28× | +3.6 | 0.11 | 27/47 (RKO, C32, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.43× | +3.4 | 0.11 | 30/48 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.25× | +3.4 | 0.11 | 27/47 (RKO, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.23× | +3.2 | 0.19 | 26/49 (KATO III, COLO 205, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.22× | +3.0 | 0.28 | 24/49 (Panc 03.27, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8338.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.266×** | -28.2 | 0e+00 | 48/48 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.240×** | -20.6 | 0e+00 | 48/48 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.280×** | -19.1 | 0e+00 | 48/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.324×** | -17.0 | 0e+00 | 47/48 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.334×** | -16.5 | 0e+00 | 46/48 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.469×** | -16.1 | 0e+00 | 48/49 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.364×** | -15.2 | 0e+00 | 46/48 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.387×** | -14.3 | 2e-44 | 46/48 (A-172, HOP62, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.392×** | -14.0 | 5e-43 | 47/48 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.429×** | -12.7 | 3e-35 | 45/48 (H4, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.456×** | -11.8 | 3e-30 | 47/48 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.225×** | -11.6 | 2e-29 | 47/49 (MIA PaCa-2, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.462×** | -11.6 | 2e-29 | 43/48 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.473×** | -11.2 | 1e-27 | 45/48 (H4, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.246×** | -10.9 | 4e-26 | 47/48 (LOX-IMVI, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.536×** | -9.4 | 3e-19 | 43/48 (J82, H4, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.454×** | -6.1 | 2e-08 | 41/49 (SNU-423, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.750×** | -6.1 | 3e-08 | 36/48 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.706×** | -5.2 | 5e-06 | 35/49 (LOX-IMVI, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.61 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8338. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 182 | 0 | 21 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0663× (z -28.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0966× (z -24.1) |
| [[HOP62 (line)]] | alt | 158 | 0 | 20 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -28.5) |
| [[NCI-H460 (line)]] | wt | 76.9 | 0 | 20 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -22.8) |
| [[LOX-IMVI (line)]] | wt | 136 | 0 | 18 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -26.1) |
| [[MIA PaCa-2 (line)]] | alt | 200 | 0 | 17 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -30.4) |
| [[NCI-H1573 (line)]] | alt | 143 | 0 | 17 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -25.9) |
| [[HEC-1-A (line)]] | alt | 168 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -23.5) |
| [[HS-578T (line)]] | alt | 138 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -26.3) |
| [[BT-474 (line)]] | alt | 79.5 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -22.8) |
| [[SNU-423 (line)]] | alt | 106 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -25.2) |
| [[SW480 (line)]] | alt | 110 | 0 | 14 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.147× (z -24.1) |
| [[A-172 (line)]] | wt | 135 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -22.2) |
| [[hTERT-HPNE (line)]] | wt | 132 | 0 | 13 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.160× (z -15.8) |
| [[NCI-H1792 (line)]] | alt | 93.4 | 0 | 13 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.162× (z -16.9) |
| [[CFPAC-1 (line)]] | alt | 144 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -29.6) |
| [[A549 (line)]] | wt | 86.8 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -26.2) |
| [[LS 180 (line)]] | wt | 91.1 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -22.6) |
| [[NCI-H23 (line)]] | alt | 104 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -26.5) |
| [[Panc 03.27 (line)]] | alt | 76.0 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -22.2) |
| [[PANC-1 (line)]] | alt | 83.3 | 0 | 11 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.153× (z -22.3) |
| [[SNU-1 (line)]] | wt | 127 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -14.5) |
| [[SW 900 (line)]] | alt | 85.7 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -19.1) |
| [[Hs 766T (line)]] | wt | 87.6 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -23.8) |
| [[RPMI-7951 (line)]] | alt | 105 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -15.3) |
| [[HCT15 (line)]] | alt | 144 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -19.1) |
| [[AsPC-1 (line)]] | alt | 71.7 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -19.5) |
| [[A498 (line)]] | wt | 104 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -19.1) |
| [[HepG2_C3A (line)]] | wt | 85.8 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -13.4) |
| [[HT-29 (line)]] | alt | 69.4 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -23.1) |
| [[J82 (line)]] | alt | 65.0 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -15.2) |
| [[LoVo (line)]] | wt | 75.3 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -13.8) |
| [[NCI-H2347 (line)]] | alt | 79.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -19.4) |
| [[A-427 (line)]] | wt | 111 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -20.4) |
| [[RKO (line)]] | wt | 69.5 | 0 | 6 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.103× (z -18.2) ⚠ toxic; cell-cycle shift, explains ~72% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.332× (z -13.0) |
| [[COLO 205 (line)]] | alt | 79.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -16.7) |
| [[KATO III (line)]] | alt | 55.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -16.5) |
| [[SW48 (line)]] | wt | 89.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -11.0) |
| [[CHP-212 (line)]] | wt | 116 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0924× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.268× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 87.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -16.4) |
| [[SK-MEL-2 (line)]] | alt | 77.1 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.228× (z -13.3) |
| [[SW1417 (line)]] | alt | 57.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -16.8) |
| [[SW 1088 (line)]] | alt | 192 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -13.3) |
| [[AN3 CA (line)]] | alt | 70.4 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0716× (z -13.6) |
| [[C32 (line)]] | wt | 99.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -10.9) |
| [[C-33 A (line)]] | alt | 110 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -10.6) |
| [[NCI-H661 (line)]] | alt | 86.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -15.0) |
| [[SHP-77 (line)]] | alt | 53.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.313× (z -8.9) |
| [[NCI-H2122 (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 102 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8338), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RANBP10]] | +0.58 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[BSDC1]] | +0.58 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[UBE2B]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ZNF765]] | +0.57 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[TBC1D17]] | +0.57 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[ZNF761]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[TRADD]] | +0.55 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[TCF25]] | +0.54 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[TBRG1]] | +0.54 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[STX12]] | +0.54 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[SAMD4B]] | +0.54 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[PEX16]] | +0.53 | +0.47 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELOVL6]] | -0.57 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[MBNL3]] | -0.55 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[PTGFRN]] | -0.54 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[NFIA]] | -0.52 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[PPARGC1B]] | -0.52 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[TFRC]] | -0.51 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[TRAF5]] | -0.50 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[NME1]] | -0.50 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[EPB41L2]] | -0.50 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[TMEM123]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[EXTL2]] | -0.48 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[SLC12A2-DT]] | -0.48 | -0.46 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PRMT2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NFIA]] | B | NFIA activity lowers PRMT2's level | lines that do not express NFIA (11) vs lines expressing it (39) | 1.39× higher at baseline in the lines without NFIA | 0.091 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.469). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.7, -49.3); signed map (-17.0, 4.8). **Vector** length 74.1, 27.8% of its response variance represented; |z| ≥ 3 in 1,500 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | -28.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.2 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.1 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | -2.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.5 | -14.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.1 | +0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.1 | +3.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.7 | +3.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -6.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.8 | -5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -16.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.0 | -11.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.9 | -11.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -10.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.1 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -6.1 |

## What is on record

|  |  |
|---|---|
| Name | protein arginine methyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:46,635,595-46,665,124 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC111373; previously HRMT1L1 |
| Gene groups (HGNC) | 7BS protein arginine methyltranferases; Arginine methyltransferases; SH3 domain containing |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [P55345](https://www.uniprot.org/uniprotkb/P55345) (Protein arginine N-methyltransferase 2):

> Arginine methyltransferase that methylates the guanidino nitrogens of arginyl residues in proteins such as STAT3, FBL, histone H4. Acts as a coactivator (with NCOA2) of the androgen receptor (AR)-mediated transactivation. Acts as a coactivator (with estrogen) of estrogen receptor (ER)-mediated transactivation. Enhances PGR, PPARG, RARA-mediated transactivation. May inhibit NF-kappa-B transcription and promote apoptosis. Represses E2F1 transcriptional activity (in a RB1-dependent manner) (By …

**Summary**, from NCBI Gene [3275](https://www.ncbi.nlm.nih.gov/gene/3275):

> Enables several functions, including nuclear receptor binding activity; peroxisome proliferator activated receptor binding activity; and protein homodimerization activity. Involved in negative regulation of inflammatory response; positive regulation of DNA-templated transcription; and regulation of intracellular signal transduction. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:5186](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5186) · Entrez [3275](https://www.ncbi.nlm.nih.gov/gene/3275) · UniProt [P55345](https://www.uniprot.org/uniprotkb/P55345) · Ensembl [ENSG00000160310](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160310)

## Data

Gene col 8338: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8338); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8338, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8338]; `tensor/DDL_lfc|DDL_z.npy` [8338]; `embed/gene_vectors.npy` [8338]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8338 or target_col == 8338). Every well: [[PRMT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRMT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
