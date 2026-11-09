---
symbol: "SPRED1"
type: "gene"
col: 9233
ensembl_id: "ENSG00000166068"
name: "sprouty related EVH1 domain containing 1"
location: "15q14"
module: 92
arm: "+"
pooled_cpm: 160.15
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 38
n_dd_up_clean: 8
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# SPRED1

*sprouty related EVH1 domain containing 1* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.49× (z +8.8, q 7e-16, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (6 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.377× (z -16.6, q 0e+00, down in 48 of 50 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPRY4]] (+0.77, fdr 7e-06), [[SPRY2]] (+0.76, fdr 7e-06), [[ETV4]] (+0.76, fdr 7e-06); moves opposite to [[CALCOCO2]] (-0.54, fdr 1e-05), [[KIF13A]] (-0.54, fdr 1e-05), [[TOM1]] (-0.54, fdr 2e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[HTR7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9233.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +8.8 | 7e-16 | 34/48 (A498, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.97×** | +8.6 | 2e-15 | 45/49 (SW480, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.45×** | +7.1 | 2e-10 | 43/48 (SW480, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +6.7 | 2e-09 | 37/48 (A498, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +5.3 | 1e-05 | 32/48 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.6 | 3e-04 | 28/48 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.009 | 27/48 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.009 | 27/49 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | **1.26×** | +3.7 | 0.013 | 28/48 (HepG2/C3A, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.21× | +3.1 | 0.12 | 24/48 (KATO III, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.21× | +3.1 | 0.12 | 24/48 (CHP-212, NCI-H661, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9233.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.377×** | -16.6 | 0e+00 | 48/50 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.362×** | -16.0 | 0e+00 | 47/49 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.351×** | -15.8 | 0e+00 | 47/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.445×** | -15.7 | 0e+00 | 47/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.378×** | -14.7 | 0e+00 | 45/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.440×** | -14.0 | 2e-42 | 47/49 (COLO 205, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.484×** | -11.4 | 3e-28 | 44/49 (RKO, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.577×** | -10.5 | 4e-24 | 41/48 (SHP-77, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.502×** | -10.4 | 1e-23 | 39/44 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.530×** | -10.0 | 1e-21 | 43/47 (C32, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.535×** | -9.1 | 5e-18 | 41/48 (SHP-77, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.671×** | -8.8 | 1e-16 | 40/48 (SHP-77, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.586×** | -8.4 | 2e-15 | 43/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.588×** | -8.3 | 3e-15 | 44/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.565×** | -8.3 | 4e-15 | 36/45 (J82, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[RMC-6236 (drug)]] 5 µM |  | **0.398×** | -7.3 | 9e-12 | 42/48 (NCI-H1573, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.658×** | -6.6 | 1e-09 | 37/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.451×** | -6.3 | 8e-09 | 40/50 (SW480, SHP-77, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9233. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 416 | 2 | 19 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.96× (z +11.3) | [[Binimetinib (drug)]] 0.5 µM 0.287× (z -17.3) |
| [[SW480 (line)]] | alt | 147 | 2 | 16 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.74× (z +11.6) | [[Trametinib (drug)]] 5 µM 0.272× (z -18.6) |
| [[BT-474 (line)]] | alt | 80.9 | 0 | 16 (3 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.264× (z -14.5) |
| [[MIA PaCa-2 (line)]] | alt | 95.2 | 1 | 15 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.6) | [[Adagrasib (drug)]] 0.05 µM 0.517× (z -22.9) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 5 µM 0.194× (z -17.0) |
| [[HEC-1-A (line)]] | alt | 185 | 0 | 15 (2 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.410× (z -14.2) |
| [[LS 180 (line)]] | wt | 224 | 0 | 14 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 0.391× (z -12.9) |
| [[SHP-77 (line)]] | alt | 131 | 0 | 14 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.141× (z -19.2) |
| [[COLO 205 (line)]] | alt | 231 | 0 | 13 (1 ⚠) | — | [[Binimetinib (drug)]] 5 µM 0.0747× (z -18.0) |
| [[HOP62 (line)]] | alt | 265 | 0 | 12 (4 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.661× (z -13.4) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.262× (z -13.2) |
| [[Hs 766T (line)]] | wt | 103 | 0 | 12 | — | [[Trametinib (drug)]] 0.5 µM 0.269× (z -15.2) |
| [[HT-29 (line)]] | alt | 223 | 2 | 10 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +12.9) | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.322× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 195 | 1 | 11 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.99× (z +11.0) | [[Trametinib (drug)]] 5 µM 0.137× (z -24.3) |
| [[NCI-H23 (line)]] | alt | 141 | 3 | 9 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.0898× (z -29.5) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.279× (z -15.6) |
| [[HCT15 (line)]] | alt | 170 | 0 | 11 (2 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.249× (z -14.5) |
| [[NCI-H2030 (line)]] | alt | 109 | 3 | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.9) | [[Trametinib (drug)]] 5 µM 0.296× (z -14.6) |
| [[CFPAC-1 (line)]] | alt | 142 | 1 | 9 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +13.2) | [[Trametinib (drug)]] 0.5 µM 0.359× (z -13.4) |
| [[LoVo (line)]] | wt | 205 | 1 | 9 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.70× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 5 µM 0.413× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 106 | 0 | 10 (1 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.377× (z -12.3) |
| [[A549 (line)]] | wt | 137 | 0 | 9 (3 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.248× (z -16.6) |
| [[KATO III (line)]] | alt | 108 | 0 | 9 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.408× (z -11.1) |
| [[SW1417 (line)]] | alt | 115 | 1 | 8 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.9) | [[Trametinib (drug)]] 5 µM 0.402× (z -11.3) |
| [[J82 (line)]] | alt | 131 | 1 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.5) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.328× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 133 | 0 | 8 (2 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.338× (z -14.2) |
| [[PANC-1 (line)]] | alt | 185 | 0 | 8 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.418× (z -10.8) |
| [[SW 900 (line)]] | alt | 186 | 0 | 8 (2 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.229× (z -13.7) |
| [[A498 (line)]] | wt | 85.9 | 4 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +20.6) | [[Binimetinib (drug)]] 5 µM 0.473× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 68.4 | 2 (1 ⚠) | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.5) | [[Trametinib (drug)]] 5 µM 0.397× (z -10.8) |
| [[H4 (line)]] | wt | 192 | 0 | 7 (1 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.281× (z -9.7) |
| [[RKO (line)]] | wt | 239 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.388× (z -10.2) |
| [[SNU-1 (line)]] | wt | 229 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 5 µM 0.348× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 107 | 0 | 6 | — | [[Trametinib (drug)]] 0.5 µM 0.278× (z -15.0) |
| [[SK-MEL-2 (line)]] | alt | 245 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +11.6) | [[Auranofin (drug)]] 5 µM 0.365× (z -12.3) |
| [[CHP-212 (line)]] | wt | 161 | 0 | 5 (1 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.222× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 259 | 0 | 5 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.338× (z -11.8) |
| [[A-427 (line)]] | wt | 111 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 7.11× (z +10.7) | [[Trametinib (drug)]] 5 µM 0.438× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 343 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.406× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 204 | 0 | 4 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.296× (z -11.5) |
| [[C-33 A (line)]] | alt | 178 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 5 µM 0.414× (z -9.4) |
| [[HS-578T (line)]] | alt | 97.1 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.9) | [[Trametinib (drug)]] 5 µM 0.380× (z -10.7) |
| [[A-172 (line)]] | wt | 77.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +13.2) | [[Trametinib (drug)]] 5 µM 0.424× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 73.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.3) | [[Trametinib (drug)]] 0.5 µM 0.526× (z -8.7) |
| [[SNU-423 (line)]] | alt | 121 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.407× (z -9.1) |
| [[AN3 CA (line)]] | alt | 175 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -10.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[hTERT-HPNE (line)]] | wt | 260 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 121 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9233), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRY4]] | +0.77 | +0.74 / +0.79 | both halves | 7e-06 | STRING 550 |
| [[SPRY2]] | +0.76 | +0.76 / +0.73 | both halves | 7e-06 | pathway: Signaling by FGFR; STRING 554 |
| [[ETV4]] | +0.76 | +0.76 / +0.79 | both halves | 7e-06 | pathway: MAPK family signaling cascades |
| [[SPRY4-AS1]] | +0.75 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[EXTL2]] | +0.75 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[DUSP6]] | +0.74 | +0.76 / +0.78 | both halves | 7e-06 | pathway: MAPK family signaling cascades; STRING 450 |
| [[ITGB5]] | +0.73 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[ETV1]] | +0.72 | +0.70 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[SPRED2]] | +0.72 | +0.69 / +0.75 | both halves | 7e-06 | same gene group; pathway: FGFRL1 modulation of FGFR1 signaling; STRING 892 |
| [[STAMBPL1]] | +0.71 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[B4GALT6]] | +0.67 | +0.57 / +0.70 | both halves | 8e-06 |  |
| [[DUSP4]] | +0.66 | +0.61 / +0.68 | both halves | 7e-06 | pathway: MAPK family signaling cascades |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALCOCO2]] | -0.54 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[KIF13A]] | -0.54 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[TOM1]] | -0.54 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[LRRFIP2]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[TKT]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[CRYAB]] | -0.51 | -0.50 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HTR7]] | B | HTR7 activity raises SPRED1's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.23× lower at baseline in the lines without HTR7 | 0.021 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[RGS17]] | B | RGS17 activity raises SPRED1's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 1.23× lower at baseline in the lines without RGS17 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |
| [[EGR3]] | B | EGR3 activity raises SPRED1's level | lines that do not express EGR3 (9) vs lines expressing it (41) | 1.40× lower at baseline in the lines without EGR3 | 0.047 | ⚠ within organs, on part of the lines; also absent: ENSG00000261026 |
| [[NPAS2]] | B | NPAS2 activity raises SPRED1's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 1.44× lower at baseline in the lines without NPAS2 | 0.050 | ⚠ within organs, on part of the lines |
| [[BCL2L1]] | B | BCL2L1 activity lowers SPRED1's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 1.46× higher at baseline in the lines without BCL2L1 | 0.052 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |
| [[TMEM156]] | B | TMEM156 activity raises SPRED1's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.05× lower at baseline in the lines without TMEM156 | 0.084 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.843). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.2, 6.9); signed map (9.0, 47.6). **Vector** length 151, 56.9% of its response variance represented; |z| ≥ 3 in 1,966 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *KRAS signaling up* (hallmark, mean cos +0.60 to 7); *Pre-NOTCH Expression and Processing* (reactome, mean cos +0.50 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +4.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.1 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.3 | +3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.6 | -2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +1.0 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +3.2 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | -0.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | +3.0 | +1.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -15.0 | -16.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -13.7 | -15.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -12.9 | -14.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -12.6 | -16.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -11.8 | -15.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -11.1 | -14.7 |

## What is on record

|  |  |
|---|---|
| Name | sprouty related EVH1 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:38,252,836-38,357,249 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33903, PPP1R147, SPRED-1 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Sprouty related EVH1 domain containing |
| Reactome | 11 pathways, smallest: FGFRL1 modulation of FGFR1 signaling; RAS signaling downstream of NF1 loss-of-function variants; Signaling by FGFR1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z699](https://www.uniprot.org/uniprotkb/Q7Z699) (Sprouty-related, EVH1 domain-containing protein 1):

> Tyrosine kinase substrate that inhibits growth-factor-mediated activation of MAP kinase (By similarity). Negatively regulates hematopoiesis of bone marrow (By similarity). Inhibits fibroblast growth factor (FGF)-induced retinal lens fiber differentiation, probably by inhibiting FGF-mediated phosphorylation of ERK1/2 (By similarity). Attenuates actin stress fiber formation via inhibition of TESK1-mediated phosphorylation of cofilin. Inhibits TGFB-induced epithelial-to-mesenchymal transition in …

**Summary**, from NCBI Gene [161742](https://www.ncbi.nlm.nih.gov/gene/161742):

> The protein encoded by this gene is a member of the Sprouty family of proteins and is phosphorylated by tyrosine kinase in response to several growth factors. The encoded protein can act as a homodimer or as a heterodimer with SPRED2 to regulate activation of the MAP kinase cascade. Defects in this gene are a cause of neurofibromatosis type 1-like syndrome (NFLS). [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20249](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20249) · Entrez [161742](https://www.ncbi.nlm.nih.gov/gene/161742) · UniProt [Q7Z699](https://www.uniprot.org/uniprotkb/Q7Z699) · Ensembl [ENSG00000166068](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166068)

## Data

Gene col 9233: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9233); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9233, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9233]; `tensor/DDL_lfc|DDL_z.npy` [9233]; `embed/gene_vectors.npy` [9233]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9233 or target_col == 9233). Every well: [[SPRED1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPRED1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
