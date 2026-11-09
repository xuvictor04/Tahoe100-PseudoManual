---
symbol: "FBXW11"
type: "gene"
col: 1031
ensembl_id: "ENSG00000072803"
name: "F-box and WD repeat domain containing 11"
location: "5q35.1"
module: 36
arm: "+"
pooled_cpm: 160.75
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# FBXW11

*F-box and WD repeat domain containing 11* — 5q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.15× (z +12.7, q 3e-34, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.429× (z -19.2, q 0e+00, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.708× (z -8.1, q 5e-14, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COP1]] (+0.71, fdr 7e-06), [[TRAPPC10]] (+0.64, fdr 7e-06), [[NLK]] (+0.64, fdr 7e-06); moves opposite to [[NOTCH2NLC]] (-0.58, fdr 1e-05), [[NFKB2]] (-0.58, fdr 1e-05), [[WASHC4]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HLF]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1031.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.15×** | +12.7 | 3e-34 | 48/49 (SW480, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.31×** | +9.3 | 5e-18 | 40/48 (SW480, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +7.5 | 1e-11 | 38/48 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.33×** | +5.4 | 8e-06 | 34/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +4.6 | 5e-04 | 26/48 (SW480, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.2 | 0.002 | 24/48 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +4.2 | 0.002 | 24/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.8 | 0.012 | 20/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.1 | 0.10 | 10/47 (SW480, A-172, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 5 µM |  | 1.15× | +3.1 | 0.10 | 5/48 (HepG2/C3A, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.14× | +3.1 | 0.10 | 17/48 (A-172, SNU-423, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.10 | 1/48 (H4) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1031.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.429×** | -19.2 | 0e+00 | 41/44 (A549, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.544×** | -14.4 | 3e-44 | 45/49 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.654×** | -9.6 | 1e-19 | 38/48 (A498, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.620×** | -9.6 | 1e-19 | 39/45 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.708×** | -8.1 | 5e-14 | 38/48 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.709×** | -8.1 | 6e-14 | 37/48 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.790×** | -7.8 | 4e-13 | 27/48 (J82, A-172, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **0.736×** | -7.2 | 4e-11 | 39/48 (SW 900, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.749×** | -6.8 | 6e-10 | 31/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.836× | -4.2 | 0.001 | 23/48 (SNU-1, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.836× | -4.0 | 0.003 | 20/47 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.895× | -3.7 | 0.011 | 10/48 (NCI-H2347, NCI-H23, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.866× | -3.4 | 0.032 | 15/48 (NCI-H1792, AN3 CA, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.905× | -3.3 | 0.037 | 10/48 (SW480, A549, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.858× | -3.1 | 0.082 | 19/47 (AsPC-1, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1031. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 150 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.01× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.592× (z -11.4) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.545× (z -9.3) |
| [[SW1417 (line)]] | alt | 187 | 1 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.34× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -15.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 148 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.43× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.595× (z -10.0) |
| [[LS 180 (line)]] | wt | 140 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.74× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.248× (z -16.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 177 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.474× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 182 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.443× (z -10.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 136 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.55× (z +8.6) | [[Harringtonine (drug)]] 5 µM 0.400× (z -12.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[C32 (line)]] | wt | 139 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.63× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -9.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 121 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -17.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 193 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.83× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -17.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 139 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.67× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -25.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 169 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.71× (z +10.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.373× (z -13.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 162 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.530× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 152 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.50× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -18.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 430 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -16.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 184 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -15.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 178 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.27× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.191× (z -26.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 128 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.13× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -12.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 172 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.29× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.629× (z -9.0) ⚠ cell-cycle shift, explains ~58% of this change |
| [[PANC-1 (line)]] | alt | 182 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.25× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.463× (z -11.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 150 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0853× (z -34.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 193 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -10.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 151 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.07× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.0877× (z -29.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 151 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -17.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 162 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.512× (z -10.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 175 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.414× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 144 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -11.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 123 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.444× (z -9.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 133 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -20.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 146 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0626× (z -27.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 170 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.496× (z -10.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[AN3 CA (line)]] | alt | 256 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -13.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -9.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -14.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 117 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.10× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.432× (z -10.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 177 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -11.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.404× (z -10.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[CFPAC-1 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 126 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 127 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 140 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 94.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 216 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1031), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COP1]] | +0.71 | +0.75 / +0.65 | both halves | 7e-06 | same gene group; pathway: Cell Cycle Checkpoints |
| [[TRAPPC10]] | +0.64 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[NLK]] | +0.64 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[TMEM11-DT]] | +0.63 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[KPNA6]] | +0.62 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[VPS53]] | +0.62 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[RAB5IF]] | +0.62 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[CDC123]] | +0.62 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[MCM9]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TMEM248]] | +0.61 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[GID4]] | +0.61 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[ARIH2]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH2NLC]] | -0.58 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[NFKB2]] | -0.58 | -0.54 / -0.60 | both halves | 1e-05 | pathway: C-type lectin receptors (CLRs); STRING 898 |
| [[WASHC4]] | -0.58 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[TNKS1BP1]] | -0.57 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[SETDB2]] | -0.55 | -0.57 / -0.57 | both halves | 8e-06 |  |
| [[CCDC159]] | -0.55 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[BHLHE41]] | -0.54 | -0.43 / -0.62 | both halves | 3e-05 | pathway: Circadian clock; STRING 429 |
| [[ZFP36]] | -0.52 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[ARL4A]] | -0.51 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[DZIP3]] | -0.51 | -0.55 / -0.56 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[LINC01473]] | -0.51 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[TRMT10B]] | -0.51 | -0.57 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLF]] | B | HLF activity lowers FBXW11's level | lines that do not express HLF (19) vs lines expressing it (31) | 1.12× higher at baseline in the lines without HLF | 0.039 | ⚠ within organs, on part of the lines; also absent: FAM230C, CHST8, GPR158; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity lowers FBXW11's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.629). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-12.5, -16.8); signed map (-46.5, -21.6). **Vector** length 106, 34.2% of its response variance represented; |z| ≥ 3 in 1,023 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.3 | +3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.5 | +5.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +12.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +9.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | -0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +2.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -8.9 | -9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -8.4 | -7.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.1 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -5.7 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | F-box and WD repeat domain containing 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.1 — chr5:171,861,549-172,006,873 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0696, Fbw1b, BTRCP2, BTRC2, Hos, Fbw11; previously FBXW1B |
| Gene groups (HGNC) | WD repeat domain containing; F-box and WD repeat domain containing |
| Hallmark sets | NOTCH_SIGNALING |
| Reactome | 51 pathways, smallest: MAP3K8 (TPL2)-dependent MAPK1/3 activation; NIK-->noncanonical NF-kB signaling; Dectin-1 mediated noncanonical NF-kB signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKB1](https://www.uniprot.org/uniprotkb/Q9UKB1) (F-box/WD repeat-containing protein 11):

> Substrate recognition component of a SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Probably recognizes and binds to phosphorylated target proteins: the interaction with substrates requires the phosphorylation of the two serine residues in the substrates' destruction motif D-S-G-X(2,3,4)-S. SCF(FBXW11) mediates the ubiquitination of phosphorylated CTNNB1 and participates in Wnt …

**Summary**, from NCBI Gene [23291](https://www.ncbi.nlm.nih.gov/gene/23291):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:13607](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13607) · Entrez [23291](https://www.ncbi.nlm.nih.gov/gene/23291) · UniProt [Q9UKB1](https://www.uniprot.org/uniprotkb/Q9UKB1) · Ensembl [ENSG00000072803](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072803)

## Data

Gene col 1031: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1031); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1031, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1031]; `tensor/DDL_lfc|DDL_z.npy` [1031]; `embed/gene_vectors.npy` [1031]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1031 or target_col == 1031). Every well: [[FBXW11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXW11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
