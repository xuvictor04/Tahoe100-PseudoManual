---
symbol: "PEX14"
type: "gene"
col: 6641
ensembl_id: "ENSG00000142655"
name: "peroxisomal biogenesis factor 14"
location: "1p36.22"
module: 119
arm: "+"
pooled_cpm: 88.09
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 20
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# PEX14

*peroxisomal biogenesis factor 14* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.38× (z +8.3, q 9e-14, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.476× (z -26.8, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL16]] (+0.70, fdr 7e-06), [[MTA3]] (+0.68, fdr 7e-06), [[PSMC1]] (+0.63, fdr 1e-05); moves opposite to [[TMEM178A]] (-0.52, fdr 6e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6641.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +8.3 | 9e-14 | 36/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.34×** | +7.1 | 5e-10 | 30/48 (PANC-1, COLO 205, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +5.8 | 1e-06 | 28/48 (COLO 205, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.61×** | +5.7 | 1e-06 | 29/49 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | 1.13× | +4.4 | 0.001 | 13/48 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | 1.18× | +4.3 | 0.002 | 17/48 (KATO III, SW48, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.010 | 16/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.078 | 6/49 (COLO 205, C32, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6641.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.476×** | -26.8 | 0e+00 | 46/49 (HOP62, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.458×** | -19.2 | 0e+00 | 41/44 (HCT15, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.480×** | -18.7 | 0e+00 | 48/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.500×** | -17.7 | 0e+00 | 45/49 (NCI-H23, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.521×** | -16.7 | 0e+00 | 47/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.560×** | -14.3 | 4e-44 | 42/50 (A-427, HOP62, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.560×** | -13.7 | 7e-41 | 39/45 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.588×** | -13.6 | 6e-40 | 45/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.584×** | -13.2 | 4e-38 | 36/48 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.664×** | -10.5 | 7e-24 | 45/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.764×** | -9.7 | 1e-20 | 39/48 (SW480, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.744×** | -7.5 | 2e-12 | 33/48 (HS-578T, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.764×** | -6.9 | 3e-10 | 30/48 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.577×** | -6.6 | 1e-09 | 35/49 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.806×** | -5.5 | 1e-06 | 29/49 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.780×** | -3.8 | 0.003 | 18/47 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.783×** | -3.0 | 0.082 | 13/49 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 0.05 µM |  | 0.887× | -2.9 | 0.094 | 12/47 (H4, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6641. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 104 | 0 | 11 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -23.4) |
| [[MIA PaCa-2 (line)]] | alt | 110 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.413× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 109 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -20.0) |
| [[SW480 (line)]] | alt | 99.8 | 1 | 8 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.12× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -19.2) |
| [[CFPAC-1 (line)]] | alt | 116 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -20.9) |
| [[NCI-H2030 (line)]] | alt | 116 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -18.2) |
| [[PANC-1 (line)]] | alt | 109 | 1 | 7 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.64× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -18.6) |
| [[HS-578T (line)]] | alt | 79.7 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -13.2) |
| [[NCI-H23 (line)]] | alt | 120 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0729× (z -35.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -14.9) |
| [[J82 (line)]] | alt | 87.0 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -18.9) |
| [[SW 900 (line)]] | alt | 82.4 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -19.1) |
| [[LOX-IMVI (line)]] | wt | 58.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.378× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 82.0 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -10.6) |
| [[SNU-423 (line)]] | alt | 82.7 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -18.0) |
| [[A-427 (line)]] | wt | 91.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -25.6) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -16.7) |
| [[A549 (line)]] | wt | 67.7 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -10.3) |
| [[C-33 A (line)]] | alt | 98.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -12.7) |
| [[HepG2_C3A (line)]] | wt | 157 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -12.6) |
| [[Hs 766T (line)]] | wt | 90.7 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -16.7) |
| [[HT-29 (line)]] | alt | 81.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 87.5 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -14.1) |
| [[NCI-H460 (line)]] | wt | 79.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.461× (z -11.9) |
| [[RKO (line)]] | wt | 115 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0959× (z -29.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -14.2) |
| [[SW48 (line)]] | wt | 101 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -9.4) |
| [[A498 (line)]] | wt | 53.5 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.456× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 75.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -18.1) |
| [[LS 180 (line)]] | wt | 91.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.278× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 75.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -23.3) |
| [[SHP-77 (line)]] | alt | 79.7 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 77.7 | 0 | 3 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -10.2) |
| [[SW1417 (line)]] | alt | 62.0 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -12.2) |
| [[A-172 (line)]] | wt | 44.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.361× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -9.1) |
| [[HCT15 (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0613× (z -28.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 65.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -9.5) |
| [[KATO III (line)]] | alt | 70.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -9.8) |
| [[LoVo (line)]] | wt | 89.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 69.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -13.2) |
| [[AN3 CA (line)]] | alt | 85.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -11.1) |
| [[BT-474 (line)]] | alt | 85.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -12.8) |
| [[C32 (line)]] | wt | 82.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[COLO 205 (line)]] | alt | 98.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -10.0) |
| [[H4 (line)]] | wt | 94.8 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.128× (z -9.6) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 80.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -12.4) |
| [[SNU-1 (line)]] | wt | 92.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0924× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW 1271 (line)]] | alt | 71.5 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.130× (z -8.7) |
| [[CHP-212 (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6641), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL16]] | +0.70 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[MTA3]] | +0.68 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[PSMC1]] | +0.63 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[KEAP1]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[CCDC43]] | +0.62 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[CUL5]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[GPATCH3]] | +0.62 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[CSTPP1]] | +0.62 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[ANKAR]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[PSMB6]] | +0.60 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[CCDC12]] | +0.59 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[AAR2]] | +0.59 | +0.64 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM178A]] | -0.52 | -0.39 / -0.54 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers PEX14's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.436). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.9, 11.5); signed map (-7.8, -18.6). **Vector** length 83.9, 21.7% of its response variance represented; |z| ≥ 3 in 1,220 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.6 | +8.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +7.3 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.6 | +5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | +6.5 | +7.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +4.3 | +4.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.4 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | -1.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +3.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.7 | -5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.7 | -10.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | -3.6 | -5.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -14.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -6.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.7 | -1.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.6 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | peroxisomal biogenesis factor 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:10,472,288-10,630,758 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Peroxins |
| Hallmark sets | PEROXISOME, UV_RESPONSE_DN, ADIPOGENESIS |
| Reactome | 5 pathways, smallest: Class I peroxisomal membrane protein import; E3 ubiquitin ligases ubiquitinate target proteins; Peroxisomal protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [O75381](https://www.uniprot.org/uniprotkb/O75381) (Peroxisomal membrane protein PEX14):

> Component of the PEX13-PEX14 docking complex, a translocon channel that specifically mediates the import of peroxisomal cargo proteins bound to PEX5 receptor. The PEX13-PEX14 docking complex forms a large import pore which can be opened to a diameter of about 9 nm (By similarity). Mechanistically, PEX5 receptor along with cargo proteins associates with the PEX14 subunit of the PEX13-PEX14 docking complex in the cytosol, leading to the insertion of the receptor into the organelle membrane with …

**Summary**, from NCBI Gene [5195](https://www.ncbi.nlm.nih.gov/gene/5195):

> This gene encodes an essential component of the peroxisomal import machinery. The protein is integrated into peroxisome membranes with its C-terminus exposed to the cytosol, and interacts with the cytosolic receptor for proteins containing a PTS1 peroxisomal targeting signal. The protein also functions as a transcriptional corepressor and interacts with a histone deacetylase. A mutation in this gene results in one form of Zellweger syndrome. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8856) · Entrez [5195](https://www.ncbi.nlm.nih.gov/gene/5195) · UniProt [O75381](https://www.uniprot.org/uniprotkb/O75381) · Ensembl [ENSG00000142655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142655)

## Data

Gene col 6641: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6641); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6641, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6641]; `tensor/DDL_lfc|DDL_z.npy` [6641]; `embed/gene_vectors.npy` [6641]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6641 or target_col == 6641). Every well: [[PEX14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEX14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
