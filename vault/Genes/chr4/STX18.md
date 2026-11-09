---
symbol: "STX18"
type: "gene"
col: 9706
ensembl_id: "ENSG00000168818"
name: "syntaxin 18"
location: "4p16.3-p16.2"
module: 178
arm: "+"
pooled_cpm: 90.74
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# STX18

*syntaxin 18* — 4p16.3-p16.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.14× (z +9.6, q 4e-19, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.354× (z -15.9, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.568× (z -12.6, q 3e-34, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEKHM3]] (+0.63, fdr 1e-05), [[REPS1]] (+0.63, fdr 3e-05), [[THYN1]] (+0.63, fdr 4e-05); moves opposite to [[IGF2BP3]] (-0.55, fdr 3e-05), [[SECISBP2]] (-0.54, fdr 1e-04), [[KDM6B]] (-0.54, fdr 1e-04).
> It is in [[Module 178]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9706.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.14×** | +9.6 | 4e-19 | 47/49 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.51×** | +7.7 | 3e-12 | 39/48 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +6.0 | 5e-07 | 36/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +4.9 | 2e-04 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +4.6 | 4e-04 | 33/48 (LS 180, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +4.3 | 0.002 | 32/48 (PANC-1, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.003 | 26/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +4.0 | 0.005 | 27/47 (HOP62, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.9 | 0.005 | 27/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.005 | 25/48 (LS 180, SK-MEL-2, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.022 | 25/48 (A498, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.15× | +3.1 | 0.100 | 14/48 (LS 180, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9706.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.354×** | -15.9 | 0e+00 | 46/49 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.364×** | -15.5 | 0e+00 | 42/44 (SW48, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.568×** | -12.6 | 3e-34 | 38/49 (NCI-H2347, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.564×** | -8.4 | 5e-15 | 34/45 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.750×** | -6.4 | 1e-08 | 36/48 (NCI-H2347, Hs 766T, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.687×** | -6.0 | 2e-07 | 34/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.685×** | -5.8 | 6e-07 | 36/50 (LOX-IMVI, C32, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~17% of this change | **0.764×** | -4.3 | 0.001 | 30/48 (SW 900, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.764×** | -4.1 | 0.002 | 30/48 (HOP62, H4, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.785×** | -3.8 | 0.007 | 28/49 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.865× | -3.2 | 0.075 | 12/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9706. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 88.6 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.13× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -17.6) |
| [[NCI-H2347 (line)]] | alt | 125 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -20.9) |
| [[SW 900 (line)]] | alt | 114 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -12.6) |
| [[SW480 (line)]] | alt | 104 | 3 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.01× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.384× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.588× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 90.6 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -15.4) |
| [[C32 (line)]] | wt | 101 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -13.3) |
| [[LOX-IMVI (line)]] | wt | 115 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -17.9) |
| [[CFPAC-1 (line)]] | alt | 154 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 100 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 89.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -9.3) |
| [[RKO (line)]] | wt | 141 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.21× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -13.7) |
| [[SW48 (line)]] | wt | 119 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0578× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -11.0) |
| [[A-172 (line)]] | wt | 63.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -16.4) |
| [[A498 (line)]] | wt | 109 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -15.7) |
| [[HS-578T (line)]] | alt | 67.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 84.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 65.1 | 2 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 7.19× (z +10.4) | [[Auranofin (drug)]] 5 µM 0.345× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 76.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 47.5 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -11.2) |
| [[SNU-423 (line)]] | alt | 84.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -9.4) |
| [[SW1417 (line)]] | alt | 85.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -12.5) |
| [[H4 (line)]] | wt | 109 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -13.1) ⚠ cell-cycle shift, explains ~18% of this change |
| [[HEC-1-A (line)]] | alt | 93.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -11.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 89.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -11.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 87.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -13.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 82.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -15.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 95.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 70.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.290× (z -12.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 82.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.281× (z -9.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 144 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.281× (z -9.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 70.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.392× (z -9.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 73.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -9.3) |
| [[C-33 A (line)]] | alt | 84.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -17.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -8.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 69.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -10.3) |
| [[LoVo (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 51.8 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.226× (z -8.5) |
| [[SW 1271 (line)]] | alt | 103 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.152× (z -8.7) |
| [[A549 (line)]] | wt | 77.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 114 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9706), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHM3]] | +0.63 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[REPS1]] | +0.63 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[THYN1]] | +0.63 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[COX14]] | +0.62 | +0.57 / +0.38 | both halves | 6e-05 |  |
| [[MRPS34]] | +0.61 | +0.60 / +0.36 | both halves | 9e-05 |  |
| [[DNAJC19]] | +0.61 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[NDUFB7]] | +0.61 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[MED23]] | +0.61 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[PRMT9]] | +0.60 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[NUBP2]] | +0.60 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[KLHDC10]] | +0.60 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[MED30]] | +0.60 | +0.69 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGF2BP3]] | -0.55 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[SECISBP2]] | -0.54 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[KDM6B]] | -0.54 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[KDSR]] | -0.53 | -0.62 / -0.31 | both halves | 2e-04 |  |
| [[ARRDC3-AS1]] | -0.53 | -0.59 / -0.36 | both halves | 9e-05 |  |
| [[NOTCH2NLB]] | -0.53 | -0.62 / -0.37 | both halves | 9e-05 |  |
| [[KRBOX5]] | -0.52 | -0.64 / -0.30 | both halves | 2e-04 |  |
| [[ERCC6L2]] | -0.52 | -0.69 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[DGKH]] | -0.52 | -0.56 / -0.30 | both halves | 2e-04 |  |
| [[MMRN2]] | -0.52 | -0.50 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises STX18's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.598). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.6, -9.3); signed map (-30.5, -10.9). **Vector** length 79.2, 22.4% of its response variance represented; |z| ≥ 3 in 980 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | -1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | -15.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | -1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.8 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | -1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +1.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.4 | -0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | +0.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.9 | -3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -1.0 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3-p16.2 — chr4:4,415,742-4,542,346 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Ufe1 |
| Gene groups (HGNC) | Syntaxins |
| Reactome | 5 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport; Intra-Golgi and retrograde Golgi-to-ER traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2W9](https://www.uniprot.org/uniprotkb/Q9P2W9) (Syntaxin-18):

> Syntaxin that may be involved in targeting and fusion of Golgi-derived retrograde transport vesicles with the ER.

**Summary**, from NCBI Gene [53407](https://www.ncbi.nlm.nih.gov/gene/53407):

> This gene encodes a member of the syntaxin family of soluble N-ethylmaleimide-sensitive factor attachment protein receptors (SNAREs) which is part of a membrane tethering complex that includes other SNAREs and several peripheral membrane proteins, and is involved in vesicular transport between the endoplasmic reticulum (ER) and the Golgi complex. The encoded protein is important for the organization of the smooth, rough, and exit site ER subdomains. A pseudogene of this gene has been …

**Accessions** — [HGNC:15942](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15942) · Entrez [53407](https://www.ncbi.nlm.nih.gov/gene/53407) · UniProt [Q9P2W9](https://www.uniprot.org/uniprotkb/Q9P2W9) · Ensembl [ENSG00000168818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168818)

## Data

Gene col 9706: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9706); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9706, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9706]; `tensor/DDL_lfc|DDL_z.npy` [9706]; `embed/gene_vectors.npy` [9706]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9706 or target_col == 9706). Every well: [[STX18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STX18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
