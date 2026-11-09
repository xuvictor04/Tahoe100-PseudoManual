---
symbol: "LIMK1"
type: "gene"
col: 2793
ensembl_id: "ENSG00000106683"
name: "LIM domain kinase 1"
location: "7q11.23"
module: 2
arm: "+"
pooled_cpm: 22.83
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 14
n_dd_up_clean: 17
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# LIMK1

*LIM domain kinase 1* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.73× (z +10.2, q 1e-21, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.402× (z -24.1, q 0e+00, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PACC1]] (+0.73, fdr 1e-05), [[ATP13A2]] (+0.72, fdr 7e-06), [[GNA12]] (+0.72, fdr 7e-06); moves opposite to [[ZNF518A]] (-0.64, fdr 1e-05), [[ERCC6L2-AS1]] (-0.64, fdr 4e-05), [[BCLAF1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[NCS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2793.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.73×** | +10.2 | 1e-21 | 33/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +8.7 | 1e-15 | 25/39 (NCI-H1792, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +8.3 | 2e-14 | 29/48 (NCI-H460, SW48, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +6.8 | 2e-09 | 25/47 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +6.7 | 2e-09 | 26/48 (NCI-H460, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +6.7 | 3e-09 | 21/30 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +6.3 | 2e-08 | 24/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.40×** | +6.3 | 2e-08 | 24/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +6.0 | 2e-07 | 25/48 (C32, NCI-H460, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.52×** | +5.5 | 2e-06 | 22/46 (NCI-H460, HT-29, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.34×** | +5.5 | 2e-06 | 22/48 (AsPC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +5.5 | 2e-06 | 17/34 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +5.3 | 4e-06 | 21/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.67×** | +5.0 | 2e-05 | 13/39 (NCI-H1792, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.64×** | +4.8 | 5e-05 | 15/41 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +4.3 | 5e-04 | 18/46 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 7e-04 | 15/47 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.26×** | +4.2 | 8e-04 | 12/47 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.001 | 9/48 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.002 | 16/48 (HEC-1-A, NCI-H1792, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.045 | 8/48 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.045 | 11/48 (LOX-IMVI, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2793.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.402×** | -24.1 | 0e+00 | 39/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.473×** | -13.5 | 8e-39 | 37/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.525×** | -12.0 | 6e-31 | 30/45 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.439×** | -8.0 | 1e-13 | 31/48 (SW480, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.729×** | -5.9 | 4e-07 | 24/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.740×** | -5.6 | 2e-06 | 20/48 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.812×** | -5.5 | 3e-06 | 19/45 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.751×** | -5.4 | 6e-06 | 18/46 (NCI-H460, BT-474, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[NG25 (drug)]] 5 µM |  | **0.588×** | -5.2 | 1e-05 | 18/45 (C32, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.624×** | -4.6 | 2e-04 | 14/47 (C32, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.849× | -4.3 | 7e-04 | 14/48 (SNU-423, C32, …) | top dose only | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **0.818×** | -3.8 | 0.008 | 7/48 (A-172, NCI-H2347, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.871× | -3.7 | 0.010 | 13/48 (J82, A-172, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.816×** | -3.7 | 0.010 | 20/48 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.783×** | -3.3 | 0.041 | 10/45 (RPMI-7951, A498, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.837× | -3.2 | 0.057 | 11/47 (AN3 CA, SW1417, …) | inconsistent across doses |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | 0.839× | -3.0 | 0.079 | 10/45 (AN3 CA, COLO 205, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2793. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 36.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -21.3) |
| [[PANC-1 (line)]] | alt | 22.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -29.3) |
| [[MIA PaCa-2 (line)]] | alt | 30.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 12.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -16.3) |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0639× (z -14.8) |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -9.9) |
| [[HOP62 (line)]] | alt | 21.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.49× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -9.2) |
| [[LoVo (line)]] | wt | 14.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.00× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 15.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 20.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 20.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 14.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -11.6) |
| [[SW480 (line)]] | alt | 17.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -16.0) |
| [[A-427 (line)]] | wt | 11.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0768× (z -13.6) |
| [[A549 (line)]] | wt | 13.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 13.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.4) |
| [[H4 (line)]] | wt | 22.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.76× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 13.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -12.4) |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 13.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -13.0) |
| [[Panc 03.27 (line)]] | alt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -9.5) |
| [[SW 900 (line)]] | alt | 26.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.12× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 18.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -9.0) |
| [[A-172 (line)]] | wt | 78.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 69.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2793), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACC1]] | +0.73 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[ATP13A2]] | +0.72 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[GNA12]] | +0.72 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[TPST2]] | +0.71 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[TANGO2]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[ST6GALNAC6]] | +0.70 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[CORO7]] | +0.69 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[PPM1F]] | +0.68 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ANKRD27]] | +0.68 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[PRR5]] | +0.67 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[FAM20B]] | +0.67 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[ANKS6]] | +0.67 | +0.66 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF518A]] | -0.64 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[ERCC6L2-AS1]] | -0.64 | -0.67 / -0.41 | both halves | 4e-05 |  |
| [[BCLAF1]] | -0.63 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[ZNF608]] | -0.63 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[HHLA3]] | -0.63 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[EPC1]] | -0.62 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[EP300]] | -0.62 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[SGO1-AS1]] | -0.62 | -0.70 / -0.40 | both halves | 5e-05 |  |
| [[CREBBP]] | -0.61 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[CASC9]] | -0.61 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.60 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[HELQ]] | -0.60 | -0.61 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCS1]] | B | NCS1 activity raises LIMK1's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 1.83× lower at baseline in the lines without NCS1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[KCNC4]] | B | KCNC4 activity raises LIMK1's level | lines that do not express KCNC4 (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without KCNC4 | 0.062 | ⚠ within organs, on part of the lines; also absent: CRTAP, FKBP7, SACS; maybe low, not absent |
| [[ARAP3]] | B | ARAP3 activity raises LIMK1's level | lines that do not express ARAP3 (9) vs lines expressing it (41) | 1.43× lower at baseline in the lines without ARAP3 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: HRH1, TGFB1I1, ENSG00000230479 |
| [[CAV1]] | B | CAV1 activity raises LIMK1's level | lines that do not express CAV1 (13) vs lines expressing it (37) | 1.49× lower at baseline in the lines without CAV1 | 0.091 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, MDFIC, CACNG6 |
| [[RUSC2]] | C | RUSC2 activity raises LIMK1's level | lines that do not express RUSC2 (4) vs lines expressing it (46) | 1.78× lower at baseline in the lines without RUSC2 | 0.075 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ATP8B3, SOAT1, SPAG17 |
| [[DNMT3B]] | C | DNMT3B activity raises LIMK1's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 1.67× lower at baseline in the lines without DNMT3B | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |
| [[GARNL3]] | C | GARNL3 activity raises LIMK1's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.80× lower at baseline in the lines without GARNL3 | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.672). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (2.3, 2.9); signed map (-42.9, -6.2). **Vector** length 104, 23.9% of its response variance represented; |z| ≥ 3 in 1,012 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.2 | +10.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.0 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.7 | +6.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.6 | +6.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.1 | +6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.4 | +5.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.3 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.1 | +3.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.0 | -13.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.2 | -24.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -12.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.1 | -5.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.0 | -8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -3.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.1 | -3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.9 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | LIM domain kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:74,082,933-74,122,525 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LIMK |
| Gene groups (HGNC) | LIM domain containing; PDZ domain containing; LIMK/TESK kinase family |
| Reactome | 16 pathways, smallest: Sema3A PAK dependent Axon repulsion; RHO GTPases Activate ROCKs; Sema4D induced cell migration and growth-cone collapse |
| Matched by | ensembl_id |

**Function**, from UniProt [P53667](https://www.uniprot.org/uniprotkb/P53667) (LIM domain kinase 1):

> Serine/threonine-protein kinase that plays an essential role in the regulation of actin filament dynamics. Acts downstream of several Rho family GTPase signal transduction pathways. Activated by upstream kinases including ROCK1, PAK1 and PAK4, which phosphorylate LIMK1 on a threonine residue located in its activation loop. LIMK1 subsequently phosphorylates and inactivates the actin binding/depolymerizing factors cofilin-1/CFL1, cofilin-2/CFL2 and destrin/DSTN, thereby preventing the cleavage of …

**Summary**, from NCBI Gene [3984](https://www.ncbi.nlm.nih.gov/gene/3984):

> There are approximately 40 known eukaryotic LIM proteins, so named for the LIM domains they contain. LIM domains are highly conserved cysteine-rich structures containing 2 zinc fingers. Although zinc fingers usually function by binding to DNA or RNA, the LIM motif probably mediates protein-protein interactions. LIM kinase-1 and LIM kinase-2 belong to a small subfamily with a unique combination of 2 N-terminal LIM motifs and a C-terminal protein kinase domain. LIMK1 is a serine/threonine kinase …

**Accessions** — [HGNC:6613](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6613) · Entrez [3984](https://www.ncbi.nlm.nih.gov/gene/3984) · UniProt [P53667](https://www.uniprot.org/uniprotkb/P53667) · Ensembl [ENSG00000106683](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106683)

## Data

Gene col 2793: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2793); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2793, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2793]; `tensor/DDL_lfc|DDL_z.npy` [2793]; `embed/gene_vectors.npy` [2793]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2793 or target_col == 2793). Every well: [[LIMK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIMK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
