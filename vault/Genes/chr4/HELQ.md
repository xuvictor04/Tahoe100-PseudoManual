---
symbol: "HELQ"
type: "gene"
col: 8665
ensembl_id: "ENSG00000163312"
name: "helicase, POLQ like"
location: "4q21.23"
module: 51
arm: "+"
pooled_cpm: 19.79
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 15
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# HELQ

*helicase, POLQ like* — 4q21.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.32× (z +24.6, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.497× (z -10.1, q 3e-21, down in 29 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.570× (z -8.1, q 5e-14, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAIF1]] (+0.77, fdr 7e-06), [[ZNF764]] (+0.77, fdr 1e-05), [[FAM200A]] (+0.76, fdr 8e-06); moves opposite to [[HACD3]] (-0.70, fdr 7e-06), [[RPA1]] (-0.70, fdr 1e-05), [[TBC1D24]] (-0.69, fdr 4e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8665.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.32×** | +24.6 | 0e+00 | 46/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.77×** | +14.7 | 0e+00 | 44/46 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.14×** | +10.6 | 8e-24 | 41/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +9.3 | 1e-18 | 34/46 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.34×** | +6.0 | 2e-07 | 24/48 (NCI-H2347, SW480, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +5.7 | 1e-06 | 24/44 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +5.4 | 4e-06 | 25/48 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +5.4 | 4e-06 | 25/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +5.4 | 5e-06 | 24/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +4.0 | 0.003 | 15/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.007 | 18/48 (NCI-H2347, J82, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.011 | 18/46 (J82, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.032 | 12/48 (A498, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.4 | 0.032 | 10/48 (MIA PaCa-2, SW 900, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.034 | 3/46 (HEC-1-A, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.044 | 7/48 (HOP62, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.068 | 9/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 11 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8665.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.497×** | -10.1 | 3e-21 | 29/41 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.527×** | -9.3 | 5e-18 | 33/46 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.555×** | -8.2 | 4e-14 | 32/45 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.570×** | -8.1 | 5e-14 | 30/47 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.640×** | -6.5 | 1e-08 | 28/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.647×** | -6.1 | 1e-07 | 19/31 (LoVo, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.660×** | -5.6 | 2e-06 | 19/35 (SHP-77, SW1417, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.692×** | -5.3 | 7e-06 | 23/48 (LoVo, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.696×** | -5.3 | 9e-06 | 23/48 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.756×** | -4.1 | 0.003 | 22/47 (PANC-1, NCI-H2030, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.842× | -3.5 | 0.022 | 14/48 (CFPAC-1, SW 1088, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.632×** | -3.5 | 0.024 | 13/28 (HEC-1-A, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.790×** | -3.4 | 0.028 | 16/48 (PANC-1, KATO III, …) | two highest doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **0.804×** | -3.2 | 0.062 | 18/45 (Panc 03.27, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.668×** | -3.1 | 0.081 | 15/41 (NCI-H460, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM |  | **0.810×** | -3.0 | 0.081 | 6/48 (J82, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8665. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.7 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.58× (z +24.0) | [[Dinaciclib (drug)]] 0.5 µM 0.0695× (z -20.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 29.5 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.146× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 35.2 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +16.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0669× (z -21.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 23.2 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +13.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -14.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[HEC-1-A (line)]] | alt | 25.3 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -18.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 18.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -8.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.126× (z -10.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 22.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +12.2) | [[Digitoxin (drug)]] 5 µM 0.0711× (z -18.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 14.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +12.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -12.3) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 16.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 26.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.117× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 10.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.07× (z +16.1) | — |
| [[SW480 (line)]] | alt | 28.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.1) | [[Digitoxin (drug)]] 5 µM 0.265× (z -12.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 12.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +11.4) | — |
| [[HepG2_C3A (line)]] | wt | 21.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0947× (z -12.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 26.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -11.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 12.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.85× (z +16.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0788× (z -14.4) ⚠ toxic |
| [[LS 180 (line)]] | wt | 13.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 20.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +11.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.131× (z -12.2) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.68× (z +14.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -10.7) |
| [[A-427 (line)]] | wt | 20.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.48× (z +11.8) | — |
| [[A549 (line)]] | wt | 17.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 27.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -9.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 19.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +10.4) | — |
| [[COLO 205 (line)]] | alt | 25.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +10.5) | — |
| [[HCT15 (line)]] | alt | 30.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 22.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +14.1) | — |
| [[HT-29 (line)]] | alt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.67× (z +15.4) | — |
| [[Panc 03.27 (line)]] | alt | 17.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +9.8) | — |
| [[RKO (line)]] | wt | 21.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +10.9) | — |
| [[RPMI-7951 (line)]] | alt | 26.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -9.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 14.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +10.5) | — |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -9.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 14.6 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0822× (z -8.8) |
| [[A498 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8665), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAIF1]] | +0.77 | +0.79 / +0.60 | both halves | 7e-06 |  |
| [[ZNF764]] | +0.77 | +0.81 / +0.56 | both halves | 1e-05 |  |
| [[FAM200A]] | +0.76 | +0.82 / +0.58 | both halves | 8e-06 |  |
| [[BPTF]] | +0.73 | +0.84 / +0.55 | both halves | 1e-05 |  |
| [[ZNF75A]] | +0.73 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[RBM23]] | +0.72 | +0.78 / +0.49 | both halves | 1e-05 |  |
| [[TRIP11]] | +0.72 | +0.81 / +0.53 | both halves | 1e-05 |  |
| [[LATS1]] | +0.70 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[ZNF830]] | +0.70 | +0.76 / +0.46 | both halves | 3e-05 |  |
| [[ZNF585A]] | +0.69 | +0.77 / +0.50 | both halves | 1e-05 |  |
| [[ZNF181]] | +0.69 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[ZNF140]] | +0.69 | +0.71 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HACD3]] | -0.70 | -0.67 / -0.61 | both halves | 7e-06 |  |
| [[RPA1]] | -0.70 | -0.75 / -0.53 | both halves | 1e-05 | STRING 486 |
| [[TBC1D24]] | -0.69 | -0.68 / -0.41 | both halves | 4e-05 |  |
| [[METAP1]] | -0.68 | -0.80 / -0.37 | both halves | 8e-05 |  |
| [[NDRG3]] | -0.67 | -0.71 / -0.45 | both halves | 3e-05 |  |
| [[PACC1]] | -0.67 | -0.68 / -0.35 | both halves | 1e-04 |  |
| [[PIP4K2A]] | -0.67 | -0.73 / -0.45 | both halves | 3e-05 |  |
| [[MAPK9]] | -0.66 | -0.63 / -0.58 | both halves | 8e-06 |  |
| [[ATP2C1]] | -0.65 | -0.74 / -0.64 | both halves | 7e-06 |  |
| [[NAPB]] | -0.65 | -0.71 / -0.55 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | -0.65 | -0.68 / -0.43 | both halves | 3e-05 |  |
| [[JAM3]] | -0.65 | -0.63 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HELQ's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HAGLR]] | B | HAGLR activity raises HELQ's level | lines that do not express HAGLR (14) vs lines expressing it (36) | 1.19× lower at baseline in the lines without HAGLR | 0.090 | ⚠ within organs, on part of the lines; also absent: ARNT2, BEND6, ITPR1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.643). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-28.6, 8.7); signed map (6.3, -17.9). **Vector** length 95.1, 22.7% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.9 | +24.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +14.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.5 | +10.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.6 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.2 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | -0.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +1.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.8 | +3.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.8 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.7 | -8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.5 | -10.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -6.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | +3.4 |

## What is on record

|  |  |
|---|---|
| Name | helicase, POLQ like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.23 — chr4:83,407,343-83,455,855 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Hel308 |
| Gene groups (HGNC) | DexD/H helicases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDG4](https://www.uniprot.org/uniprotkb/Q8TDG4) (Helicase POLQ-like):

> Single-stranded 3'-5' DNA helicase that plays a key role in homology-driven double-strand break (DSB) repair. Involved in different DSB repair mechanisms that are guided by annealing of extensive stretches of complementary bases at break ends, such as microhomology-mediated end-joining (MMEJ), single-strand annealing (SSA) or synthesis-dependent strand annealing (SDSA). Possesses both DNA unwinding and annealing activities. Forms a complex with RAD51, stimulating HELQ DNA helicase activity and …

**Summary**, from NCBI Gene [113510](https://www.ncbi.nlm.nih.gov/gene/113510):

> HEL308 is a single-stranded DNA-dependent ATPase and DNA helicase (Marini and Wood, 2002 [PubMed 11751861]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:18536](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18536) · Entrez [113510](https://www.ncbi.nlm.nih.gov/gene/113510) · UniProt [Q8TDG4](https://www.uniprot.org/uniprotkb/Q8TDG4) · Ensembl [ENSG00000163312](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163312)

## Data

Gene col 8665: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8665); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8665, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8665]; `tensor/DDL_lfc|DDL_z.npy` [8665]; `embed/gene_vectors.npy` [8665]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8665 or target_col == 8665). Every well: [[HELQ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HELQ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
