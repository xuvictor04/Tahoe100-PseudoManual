---
symbol: "C1QTNF3-AMACR"
type: "gene"
col: 15774
ensembl_id: "ENSG00000273294"
name: "C1QTNF3-AMACR readthrough (NMD candidate)"
location: "5p13.2"
module: 83
arm: "-"
pooled_cpm: 50.86
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 52
n_dd_up_clean: 16
n_dd_down_clean: 40
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# C1QTNF3-AMACR

*C1QTNF3-AMACR readthrough (NMD candidate)* — 5p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.66× (z +5.9, q 2e-06, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 52 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.323× (z -19.3, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1QTNF3]] (+0.77, fdr 7e-06, ⚠ read-through risk), [[GUSBP18]] (+0.61, fdr 1e-05), [[ZBTB20]] (+0.58, fdr 3e-05), [[PMFBP1]] (+0.58, fdr 3e-05); moves opposite to [[GMIP]] (-0.57, fdr 2e-05), [[CSRNP2]] (-0.53, fdr 2e-04), [[CCNJ]] (-0.52, fdr 1e-04).
> It sits in the **-** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[FMN1]] → it (grade B ⚠); 2 go from it, the strongest it → [[C1QTNF3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15774.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.66×** | +5.9 | 2e-06 | 34/47 (SW480, SW 900, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +3.9 | 0.030 | 23/48 (SW 900, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.26×** | +3.8 | 0.030 | 25/48 (SW480, SW 900, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.030 | 22/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.37×** | +3.6 | 0.030 | 20/50 (SW 900, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.030 | 19/49 (NCI-H1792, NCI-H23, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.045 | 24/48 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.045 | 24/47 (SW480, Hs 766T, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.70×** | +3.4 | 0.045 | 18/50 (HT-29, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.065 | 15/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.065 | 18/49 (SHP-77, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.065 | 20/47 (SW 900, SW480, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.071 | 14/48 (HS-578T, NCI-H2030, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.078 | 17/48 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.078 | 14/49 (HEC-1-A, A-172, …) | top dose only |  |
| [[AZD-8055 (drug)]] 5 µM |  | **1.61×** | +3.0 | 0.083 | 18/49 (LoVo, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 52 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15774.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.323×** | -19.3 | 0e+00 | 47/49 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.332×** | -18.8 | 0e+00 | 43/47 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.245×** | -17.0 | 0e+00 | 48/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.255×** | -16.5 | 0e+00 | 45/47 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.265×** | -15.4 | 0e+00 | 44/46 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.272×** | -15.1 | 0e+00 | 45/48 (A-427, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.299×** | -14.6 | 0e+00 | 46/48 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.325×** | -13.6 | 5e-40 | 44/48 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.354×** | -12.5 | 3e-34 | 44/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.360×** | -12.3 | 4e-33 | 43/47 (COLO 205, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.387×** | -11.4 | 1e-28 | 46/48 (HT-29, HCT15, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.187×** | -10.6 | 1e-24 | 46/49 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.424×** | -9.8 | 8e-21 | 46/48 (HT-29, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.432×** | -9.7 | 1e-20 | 36/47 (RPMI-7951, COLO 205, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.452×** | -9.6 | 4e-20 | 40/48 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.463×** | -9.3 | 6e-19 | 46/48 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.259×** | -8.5 | 4e-16 | 40/47 (BT-474, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15774. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 92.2 | 0 | 21 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.101× (z -20.9) |
| [[HOP62 (line)]] | alt | 60.4 | 0 | 18 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -24.5) |
| [[COLO 205 (line)]] | alt | 122 | 0 | 15 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0731× (z -21.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -21.3) |
| [[HT-29 (line)]] | alt | 112 | 0 | 15 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -23.6) |
| [[HCT15 (line)]] | alt | 71.0 | 0 | 14 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.113× (z -15.6) |
| [[BT-474 (line)]] | alt | 168 | 0 | 13 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -17.0) |
| [[H4 (line)]] | wt | 69.6 | 0 | 12 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0705× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.169× (z -15.4) |
| [[Panc 03.27 (line)]] | alt | 74.6 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -17.8) |
| [[PANC-1 (line)]] | alt | 35.4 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -17.6) |
| [[HepG2_C3A (line)]] | wt | 90.9 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -18.5) |
| [[NCI-H23 (line)]] | alt | 89.6 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0918× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -15.7) |
| [[SW 900 (line)]] | alt | 61.5 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -16.4) |
| [[A-427 (line)]] | wt | 98.4 | 0 | 10 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0974× (z -24.1) |
| [[SHP-77 (line)]] | alt | 191 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -19.0) |
| [[CFPAC-1 (line)]] | alt | 41.5 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -17.8) |
| [[NCI-H1573 (line)]] | alt | 41.1 | 0 | 9 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0736× (z -16.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.108× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 21.3 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -13.9) |
| [[A498 (line)]] | wt | 36.1 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -18.5) |
| [[J82 (line)]] | alt | 34.5 | 0 | 8 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.160× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 72.2 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -17.1) |
| [[LOX-IMVI (line)]] | wt | 46.9 | 0 | 7 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.142× (z -14.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.378× (z -10.8) |
| [[LS 180 (line)]] | wt | 36.9 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -11.2) |
| [[C32 (line)]] | wt | 45.4 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -12.4) |
| [[LoVo (line)]] | wt | 31.3 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.205× (z -12.5) |
| [[HS-578T (line)]] | alt | 66.0 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -17.2) |
| [[hTERT-HPNE (line)]] | wt | 39.3 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -12.4) |
| [[NCI-H1792 (line)]] | alt | 28.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -16.8) |
| [[A549 (line)]] | wt | 20.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -14.1) |
| [[RPMI-7951 (line)]] | alt | 37.2 | 0 | 4 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0943× (z -13.6) |
| [[SNU-1 (line)]] | wt | 55.4 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -13.0) |
| [[SNU-423 (line)]] | alt | 31.3 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -14.2) |
| [[Hs 766T (line)]] | wt | 22.1 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.308× (z -8.8) |
| [[SW48 (line)]] | wt | 72.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 16.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.124× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 20.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0603× (z -22.0) |
| [[C-33 A (line)]] | alt | 68.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -9.9) |
| [[CHP-212 (line)]] | wt | 65.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 29.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.136× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 26.4 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.243× (z -8.8) |
| [[SW 1271 (line)]] | alt | 81.5 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0826× (z -8.8) |
| [[A-172 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15774), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1QTNF3]] | +0.77 | +0.74 / +0.76 | both halves | 7e-06 | ⚠ **readthrough risk**: C1QTNF3 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[GUSBP18]] | +0.61 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[ZBTB20]] | +0.58 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[PMFBP1]] | +0.58 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[WDPCP]] | +0.58 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[LINC01876]] | +0.57 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[PRKN]] | +0.54 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[USP9X]] | +0.54 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[NIHCOLE]] | +0.52 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[STK3]] | +0.52 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[SMCHD1]] | +0.51 | +0.53 / +0.37 | both halves | 8e-05 |  |
| [[WWOX]] | +0.51 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[FGGY]] | +0.51 | +0.37 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMIP]] | -0.57 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[CSRNP2]] | -0.53 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[CCNJ]] | -0.52 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[CEP164]] | -0.51 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[PTPN9]] | -0.51 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[ZNF621]] | -0.49 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[TEP1]] | -0.49 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[ZNF419]] | -0.48 | -0.46 / -0.26 | both halves | 3e-04 |  |
| [[MICALL1]] | -0.48 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[DDX59]] | -0.48 | -0.25 / -0.37 | both halves | 4e-04 |  |
| [[BTBD10]] | -0.47 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[ZNF142]] | -0.47 | -0.42 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FMN1]] | B | FMN1 activity raises C1QTNF3-AMACR's level | lines that do not express FMN1 (17) vs lines expressing it (33) | 1.41× lower at baseline in the lines without FMN1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000278266, LINC02405, ENSG00000286016; maybe low, not absent |
| [[LINC01876]] | B | LINC01876 activity raises C1QTNF3-AMACR's level | lines that do not express LINC01876 (24) vs lines expressing it (26) | 1.65× lower at baseline in the lines without LINC01876 | 0.032 | ⚠ within organs, on part of the lines; also absent: TOX3, TFF1, TMEM45B |
| [[MAP2K1]] | B | MAP2K1 activity lowers C1QTNF3-AMACR's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[LINC01876]] | B | LINC01876 activity strengthens C1QTNF3-AMACR's drug response | lines that do not express LINC01876 (24) vs lines expressing it (25) | the lines without LINC01876 respond 0.81× as strongly (z diff +1.38); strongest at Idarubicin (hydrochloride) 5 µM: 0.37x vs 0.30x (z diff +1.7) | 0.065 | ⚠ within organs, on part of the lines; also absent: TOX3, TFF1, TMEM45B; target measured in part of the lines; artifact flags |
| [[C1QTNF3]] | C | C1QTNF3's natural level strengthens C1QTNF3-AMACR's drug response | C1QTNF3's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.71; direction not clear | 0.002 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[LINC02937]] | C | LINC02937's natural level strengthens C1QTNF3-AMACR's drug response | LINC02937's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse +0.42; direction not clear | 0.094 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1QTNF3]] | C | C1QTNF3-AMACR's natural level strengthens C1QTNF3's drug response | C1QTNF3-AMACR's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.75; direction not clear | 0.013 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[GUSBP18]] | C | C1QTNF3-AMACR's natural level strengthens GUSBP18's drug response | C1QTNF3-AMACR's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.60; direction not clear | 0.015 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **-** arm (projection on the module's main direction -0.384). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-23.2, 33.2); signed map (2.0, 6.1). **Vector** length 84.4, 28.5% of its response variance represented; |z| ≥ 3 in 1,742 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | +5.4 | -4.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | -0.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | -16.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | -0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -6.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.1 | +2.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -8.6 | -9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.6 | -15.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -19.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -9.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.4 | -4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.7 | -2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.6 | -0.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | C1QTNF3-AMACR readthrough (NMD candidate) |
| Locus type | readthrough (other) |
| Location | 5p13.2 — chr5:33,987,174-34,124,528 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100534612](https://www.ncbi.nlm.nih.gov/gene/100534612):

> This locus represents naturally occurring read-through transcription between the neighboring C1q and tumor necrosis factor related protein 3 (C1QTNF3) and alpha-methylacyl-CoA racemase (AMACR) genes on chromosome 5. The read-through transcript is a candidate for nonsense-mediated mRNA decay (NMD), and is thus not likely to produce a protein product. [provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:49198](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49198) · Entrez [100534612](https://www.ncbi.nlm.nih.gov/gene/100534612) · Ensembl [ENSG00000273294](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000273294)

## Data

Gene col 15774: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15774); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15774, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15774]; `tensor/DDL_lfc|DDL_z.npy` [15774]; `embed/gene_vectors.npy` [15774]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15774 or target_col == 15774). Every well: [[C1QTNF3-AMACR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1QTNF3-AMACR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
