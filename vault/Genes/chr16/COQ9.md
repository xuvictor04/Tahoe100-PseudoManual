---
symbol: "COQ9"
type: "gene"
col: 1538
ensembl_id: "ENSG00000088682"
name: "coenzyme Q9"
location: "16q21"
module: 28
arm: "+"
pooled_cpm: 20.3
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# COQ9

*coenzyme Q9* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.62× (z +14.6, q 3e-45, up in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.62× (z +10.0, q 5e-21, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.635× (z -9.7, q 2e-19, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSTF1]] (+0.68, fdr 7e-06), [[CLK4]] (+0.68, fdr 7e-06), [[NFYB]] (+0.67, fdr 1e-05); moves opposite to [[SH3KBP1]] (-0.64, fdr 7e-06), [[TPST2]] (-0.63, fdr 1e-05), [[CYTH1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1538.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.62×** | +14.6 | 3e-45 | 37/47 (NCI-H2030, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +10.0 | 5e-21 | 32/47 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +8.5 | 3e-15 | 29/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +8.1 | 5e-14 | 25/47 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.34×** | +6.3 | 3e-08 | 23/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +6.2 | 4e-08 | 19/48 (CFPAC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +5.7 | 8e-07 | 20/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.7 | 8e-07 | 21/46 (NCI-H2030, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.65×** | +5.6 | 1e-06 | 12/45 (Hs 766T, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +5.3 | 6e-06 | 15/48 (NCI-H1792, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +5.1 | 2e-05 | 15/48 (NCI-H2030, Panc 03.27, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.15× | +4.4 | 6e-04 | 18/47 (NCI-H2030, CFPAC-1, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.22×** | +4.2 | 0.001 | 16/47 (A-172, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.003 | 10/48 (C-33 A, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.20× | +3.6 | 0.012 | 16/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.036 | 4/47 (A549, SW48, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | 1.16× | +3.1 | 0.064 | 9/47 (HEC-1-A, NCI-H1573, …) | top dose only | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.065 | 2/47 (HS-578T, C-33 A) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.15× | +3.0 | 0.066 | 3/48 (SW480, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1538.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.635×** | -9.7 | 2e-19 | 28/48 (C32, C-33 A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.673×** | -8.5 | 8e-15 | 28/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.691×** | -7.9 | 6e-13 | 19/42 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.757×** | -5.5 | 6e-06 | 16/37 (HCT15, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.781×** | -5.3 | 1e-05 | 17/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.801×** | -4.7 | 2e-04 | 14/48 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.812×** | -4.4 | 7e-04 | 16/48 (NCI-H460, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.816×** | -4.1 | 0.003 | 13/48 (HS-578T, SW480, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.827×** | -4.1 | 0.003 | 13/48 (H4, RKO, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.875× | -4.0 | 0.003 | 10/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -3.8 | 0.007 | 16/46 (LOX-IMVI, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -3.7 | 0.010 | 14/48 (NCI-H460, SHP-77, …) | all doses, flat | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.728×** | -3.6 | 0.016 | 13/41 (PANC-1, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.793×** | -3.5 | 0.016 | 10/48 (A-172, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -3.5 | 0.016 | 10/48 (NCI-H1792, NCI-H460, …) | all doses, flat | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | 0.849× | -3.4 | 0.027 | 10/47 (RKO, COLO 205, …) | top dose only | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | 0.906× | -3.0 | 0.087 | 8/48 (PANC-1, SW 1271, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1538. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 20.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -12.6) ⚠ cell-cycle shift, explains ~1% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.314× (z -8.6) |
| [[KATO III (line)]] | alt | 26.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.0) ⚠ cell-cycle shift, explains ~26% of this change | [[Dinaciclib (drug)]] 5 µM 0.143× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 23.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.8) ⚠ cell-cycle shift, explains ~26% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 30.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -14.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -12.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 30.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.252× (z -9.0) |
| [[C32 (line)]] | wt | 18.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.215× (z -9.3) |
| [[HCT15 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -9.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.103× (z -12.8) ⚠ toxic |
| [[HOP62 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.144× (z -12.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[hTERT-HPNE (line)]] | wt | 17.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -9.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.248× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 26.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H2347 (line)]] | alt | 9.04 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 16.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +8.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -9.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 15.3 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0473× (z -13.3) |
| [[SW480 (line)]] | alt | 22.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.1) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1538), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSTF1]] | +0.68 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[CLK4]] | +0.68 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[NFYB]] | +0.67 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[ZC3H6]] | +0.65 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[CEPT1]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[HMG20A]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[COG4]] | +0.61 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[RAD52]] | +0.61 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[HMGCL]] | +0.61 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[LATS1]] | +0.60 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[PPCS]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 | pathway: Metabolism of vitamins and cofactors |
| [[METTL25B]] | +0.60 | +0.59 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3KBP1]] | -0.64 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[TPST2]] | -0.63 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[CYTH1]] | -0.61 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[TMEM41B]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[ACOT7]] | -0.57 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[CAP1]] | -0.56 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[FPGS]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 | pathway: Metabolism of vitamins and cofactors |
| [[NAPG]] | -0.55 | -0.63 / -0.37 | both halves | 8e-05 |  |
| [[BICD2]] | -0.55 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[GPRIN1]] | -0.55 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[PIP5KL1]] | -0.54 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[RSU1]] | -0.54 | -0.53 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers COQ9's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.642). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-26.2, 6.0); signed map (6.9, -16.0). **Vector** length 92.3, 18.5% of its response variance represented; |z| ≥ 3 in 817 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.6 | +14.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +8.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +10.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +5.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.7 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +5.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.8 | +5.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.8 | +2.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.7 | -9.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.5 | -8.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -4.3 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -5.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -3.9 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -4.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.8 | -3.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | coenzyme Q9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:57,447,425-57,461,270 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434K046; previously C16orf49 |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 3 pathways, smallest: Ubiquinol biosynthesis; Metabolism of cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [O75208](https://www.uniprot.org/uniprotkb/O75208) (Ubiquinone biosynthesis protein COQ9, mitochondrial):

> Membrane-associated protein that warps the membrane surface to access and bind aromatic isoprenes with high specificity, including ubiquinone (CoQ) isoprene intermediates and presents them directly to COQ7, therefore facilitating the COQ7-mediated hydroxylase step. Participates in the biosynthesis of coenzyme Q, also named ubiquinone, an essential lipid-soluble electron transporter for aerobic cellular respiration.

**Summary**, from NCBI Gene [57017](https://www.ncbi.nlm.nih.gov/gene/57017):

> This locus represents a mitochondrial ubiquinone biosynthesis gene. The encoded protein is likely necessary for biosynthesis of coenzyme Q10, as mutations at this locus have been associated with autosomal-recessive neonatal-onset primary coenzyme Q10 deficiency.[provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:25302](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25302) · Entrez [57017](https://www.ncbi.nlm.nih.gov/gene/57017) · UniProt [O75208](https://www.uniprot.org/uniprotkb/O75208) · Ensembl [ENSG00000088682](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088682)

## Data

Gene col 1538: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1538); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1538, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1538]; `tensor/DDL_lfc|DDL_z.npy` [1538]; `embed/gene_vectors.npy` [1538]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1538 or target_col == 1538). Every well: [[COQ9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COQ9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
