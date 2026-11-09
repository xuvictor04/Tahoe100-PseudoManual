---
symbol: "TMEM255B"
type: "gene"
col: 11545
ensembl_id: "ENSG00000184497"
name: "transmembrane protein 255B"
location: "13q34"
module: 84
arm: "+"
pooled_cpm: 16.0
n_lines_expressing: 31
n_dd_up: 13
n_dd_down: 28
n_dd_up_clean: 10
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# TMEM255B

*transmembrane protein 255B* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Thymol (drug)]] 0.5 µM: 1.87× (z +6.1, q 6e-07, up in 14 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.332× (z -10.3, q 6e-22, down in 23 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX1A]] (+0.66, fdr 9e-06), [[CSNK1E]] (+0.66, fdr 1e-05), [[CELSR1]] (+0.66, fdr 7e-06); moves opposite to [[FIGN]] (-0.56, fdr 1e-05), [[NFIB]] (-0.55, fdr 1e-05), [[ABCC2]] (-0.51, fdr 4e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MTSS1]] → it (grade B ⚠); 10 go from it, the strongest it → [[ZNF385A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11545.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Thymol (drug)]] 0.5 µM |  | **1.87×** | +6.1 | 6e-07 | 14/26 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +5.7 | 3e-06 | 13/28 (SW480, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.03×** | +4.9 | 1e-04 | 15/25 (LOX-IMVI, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.59×** | +4.5 | 7e-04 | 13/27 (SW1417, A549, …) | all doses, flat |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.59×** | +4.5 | 7e-04 | 16/28 (SW480, PANC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.58×** | +4.5 | 7e-04 | 20/28 (SW480, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Naproxen (drug)]] 0.05 µM |  | **1.58×** | +4.2 | 0.002 | 11/27 (NCI-H2030, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +4.1 | 0.003 | 8/29 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.06×** | +3.7 | 0.015 | 11/28 (SW480, HOP62, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +3.5 | 0.024 | 2/17 (A498, PANC-1) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +3.3 | 0.049 | 6/22 (SW 900, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.072 | 5/28 (C32, COLO 205, …) | all doses, flat |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.092 | 10/28 (Hs 766T, SHP-77, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11545.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.332×** | -10.3 | 6e-22 | 23/29 (C32, A549, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.476×** | -10.1 | 1e-21 | 22/27 (SK-MEL-2, C32, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.368×** | -9.7 | 9e-20 | 24/28 (Hs 766T, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.561×** | -7.9 | 4e-13 | 23/28 (C32, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.519×** | -6.3 | 3e-08 | 21/29 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.557×** | -5.6 | 2e-06 | 18/29 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.560×** | -5.6 | 2e-06 | 16/28 (PANC-1, HS-578T, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.378×** | -4.9 | 6e-05 | 20/28 (C32, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.696×** | -4.9 | 7e-05 | 13/28 (SK-MEL-2, SHP-77, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.616×** | -4.7 | 2e-04 | 16/27 (NCI-H460, A549, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.600×** | -4.5 | 3e-04 | 14/29 (PANC-1, SHP-77, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.619×** | -4.4 | 4e-04 | 16/25 (NCI-H460, C32, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.650×** | -4.1 | 0.002 | 16/29 (C32, HS-578T, …) | top dose only | position effect removed |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.653×** | -4.1 | 0.002 | 10/28 (HCT15, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.715×** | -3.9 | 0.003 | 16/28 (SHP-77, PANC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.750×** | -3.9 | 0.003 | 14/29 (C32, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.674×** | -3.9 | 0.003 | 15/29 (C32, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.491×** | -3.6 | 0.011 | 12/26 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~24% here); noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.774×** | -3.5 | 0.016 | 11/28 (A549, HS-578T, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.700×** | -3.4 | 0.017 | 12/29 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.700×** | -3.4 | 0.017 | 13/28 (SHP-77, NCI-H2030, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11545. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 118 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0638× (z -23.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -16.7) |
| [[NCI-H460 (line)]] | wt | 15.5 | 0 | 10 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0671× (z -13.4) ⚠ toxic; cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0950× (z -11.7) |
| [[A-172 (line)]] | wt | 44.8 | 0 | 7 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0647× (z -15.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.151× (z -10.3) |
| [[HS-578T (line)]] | alt | 29.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -18.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.115× (z -11.9) |
| [[Hs 766T (line)]] | wt | 33.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0478× (z -14.6) |
| [[A549 (line)]] | wt | 13.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0587× (z -17.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0489× (z -12.5) |
| [[PANC-1 (line)]] | alt | 17.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -10.8) |
| [[SHP-77 (line)]] | alt | 152 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0746× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 34.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0379× (z -24.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.178× (z -9.0) |
| [[SNU-423 (line)]] | alt | 24.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0610× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -8.6) |
| [[SW480 (line)]] | alt | 7.61 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.44× (z +9.9) | — |
| [[J82 (line)]] | alt | 31.7 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.266× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 14.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0653× (z -18.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0897× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 8.83 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -9.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[crizotinib (drug)]] 0.05 µM 0.0610× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 28.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -11.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A498 (line)]] | wt | 5.10 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -13.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HCT15 (line)]] | alt | 7.05 | 0 | 1 | — | [[Busulfan (drug)]] 0.05 µM 0.0589× (z -8.8) |
| [[SW 900 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -9.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.57 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.38 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.09 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11545), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX1A]] | +0.66 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[CSNK1E]] | +0.66 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[CELSR1]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[PYGL]] | +0.65 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[TNNT1]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[RASA3]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ZFYVE28]] | +0.61 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[MTSS1]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[UBA6]] | +0.60 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ARID3B]] | +0.60 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[MMP17]] | +0.59 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[TMEM158]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FIGN]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[NFIB]] | -0.55 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ABCC2]] | -0.51 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[ZFX]] | -0.51 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[ADGRG6]] | -0.50 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[SLFN12]] | -0.50 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[IQCH-AS1]] | -0.50 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[ZNF644]] | -0.50 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[RPRD2]] | -0.50 | -0.30 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTSS1]] | B | MTSS1 activity raises TMEM255B's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 2.59× lower at baseline in the lines without MTSS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[ADGRG6]] | B | ADGRG6 activity lowers TMEM255B's level | lines that do not express ADGRG6 (12) vs lines expressing it (38) | 2.18× higher at baseline in the lines without ADGRG6 | 0.052 | ⚠ within organs, on part of the lines; also absent: RHPN1, FAM83H, TNFRSF10A-DT |
| [[RASSF8]] | B | RASSF8 activity raises TMEM255B's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 3.12× lower at baseline in the lines without RASSF8 | 0.058 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1 |
| [[TRIM9]] | C | TRIM9 activity raises TMEM255B's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 3.84× lower at baseline in the lines without TRIM9 | 0.003 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF385A]] | B | TMEM255B activity raises ZNF385A's level | lines that do not express TMEM255B (19) vs lines expressing it (31) | 2.16× lower at baseline in the lines without TMEM255B | 0.039 | ⚠ within organs, on part of the lines; also absent: DOCK10, ENSG00000289600, OR4F15; maybe low, not absent |
| [[MTSS1]] | B | TMEM255B activity raises MTSS1's level | lines that do not express TMEM255B (19) vs lines expressing it (31) | 2.57× lower at baseline in the lines without TMEM255B | 0.077 | ⚠ within organs, on part of the lines; also absent: DOCK10, ENSG00000289600, OR4F15; maybe low, not absent |
| [[SORBS2]] | B | TMEM255B activity raises SORBS2's level | lines that do not express TMEM255B (19) vs lines expressing it (31) | 1.64× lower at baseline in the lines without TMEM255B | 0.077 | ⚠ within organs, on part of the lines; also absent: DOCK10, ENSG00000289600, OR4F15; maybe low, not absent |
| [[CSPG4]] | B | TMEM255B activity raises CSPG4's level | lines that do not express TMEM255B (19) vs lines expressing it (31) | 2.78× lower at baseline in the lines without TMEM255B | 0.086 | ⚠ within organs, on part of the lines; also absent: DOCK10, ENSG00000289600, OR4F15; maybe low, not absent |
| [[TREM1]] | B | TMEM255B activity raises TREM1's level | lines that do not express TMEM255B (19) vs lines expressing it (31) | 1.92× lower at baseline in the lines without TMEM255B | 0.086 | ⚠ within organs, on part of the lines; also absent: DOCK10, ENSG00000289600, OR4F15; maybe low, not absent |
| [[FAM219A]] | B | TMEM255B activity raises FAM219A's level | lines that do not express TMEM255B (19) vs lines expressing it (31) | 1.72× lower at baseline in the lines without TMEM255B | 0.090 | ⚠ within organs, on part of the lines; also absent: DOCK10, ENSG00000289600, OR4F15; maybe low, not absent |
| [[UBE2O]] | B | TMEM255B activity raises UBE2O's level | lines that do not express TMEM255B (19) vs lines expressing it (31) | 1.34× lower at baseline in the lines without TMEM255B | 0.094 | ⚠ within organs, on part of the lines; also absent: DOCK10, ENSG00000289600, OR4F15; maybe low, not absent |
| [[LOXL2]] | B | TMEM255B activity raises LOXL2's level | lines that do not express TMEM255B (19) vs lines expressing it (31) | 3.38× lower at baseline in the lines without TMEM255B | 0.097 | ⚠ within organs, on part of the lines; also absent: DOCK10, ENSG00000289600, OR4F15; maybe low, not absent |
| [[LINC03047]] | C | TMEM255B activity raises LINC03047's level | lines that do not express TMEM255B (19) vs lines expressing it (31) | 3.26× lower at baseline in the lines without TMEM255B | 0.071 | ⚠ within organs, on part of the lines; also absent: DOCK10, ENSG00000289600, OR4F15; maybe low, not absent; co-absent with the target |
| [[KCNMA1]] | C | TMEM255B activity raises KCNMA1's level | lines that do not express TMEM255B (19) vs lines expressing it (31) | 4.37× lower at baseline in the lines without TMEM255B | 0.075 | ⚠ within organs, on part of the lines; also absent: DOCK10, ENSG00000289600, OR4F15; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (50.0, 3.8); signed map (1.2, 50.3). **Vector** length 97.4, 28.3% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.6 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +4.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +2.9 |
|  | [[Glycyrrhizic acid (drug)]] 0.05 µM |  | +2.1 | +2.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.2 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.6 | -10.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.5 | -3.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.4 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.0 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 255B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:113,759,226-113,816,995 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC20579; previously FAM70B |
| Matched by | ensembl_id |

UniProt [Q8WV15](https://www.uniprot.org/uniprotkb/Q8WV15) carries no function annotation.

**Summary**, from NCBI Gene [348013](https://www.ncbi.nlm.nih.gov/gene/348013):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28297](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28297) · Entrez [348013](https://www.ncbi.nlm.nih.gov/gene/348013) · UniProt [Q8WV15](https://www.uniprot.org/uniprotkb/Q8WV15) · Ensembl [ENSG00000184497](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184497)

## Data

Gene col 11545: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11545); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11545, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11545]; `tensor/DDL_lfc|DDL_z.npy` [11545]; `embed/gene_vectors.npy` [11545]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11545 or target_col == 11545). Every well: [[TMEM255B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM255B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
