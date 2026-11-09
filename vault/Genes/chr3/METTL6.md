---
symbol: "METTL6"
type: "gene"
col: 13052
ensembl_id: "ENSG00000206562"
name: "methyltransferase 6, tRNA N3-cytidine"
location: "3p25.1"
module: 23
arm: "+"
pooled_cpm: 23.73
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 12
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# METTL6

*methyltransferase 6, tRNA N3-cytidine* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.87× (z +18.3, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.613× (z -10.1, q 3e-21, down in 34 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.748× (z -6.0, q 2e-07, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THAP2]] (+0.81, fdr 2e-05), [[PCNX4-DT]] (+0.79, fdr 3e-05), [[ATE1OSP]] (+0.79, fdr 4e-05); moves opposite to [[FAM118A]] (-0.71, fdr 1e-04), [[GNA12]] (-0.70, fdr 1e-04), [[PACC1]] (-0.67, fdr 4e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[EFCAB6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13052.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +18.3 | 0e+00 | 44/48 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +16.3 | 0e+00 | 34/47 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.99×** | +14.2 | 2e-43 | 40/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +11.0 | 5e-26 | 40/48 (SW1417, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.36×** | +8.9 | 6e-17 | 28/48 (LS 180, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +7.4 | 2e-11 | 16/32 (NCI-H2030, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +6.5 | 5e-09 | 24/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +6.5 | 5e-09 | 23/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +6.5 | 5e-09 | 25/48 (LoVo, C32, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.2 | 3e-08 | 25/47 (HS-578T, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +5.6 | 9e-07 | 22/48 (NCI-H1573, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +5.6 | 1e-06 | 19/47 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.65×** | +5.4 | 3e-06 | 18/47 (SK-MEL-2, SNU-423, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.29×** | +5.3 | 5e-06 | 23/48 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.28×** | +5.1 | 1e-05 | 18/42 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +4.9 | 3e-05 | 13/48 (SW480, C32, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.003 | 11/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.19× | +3.6 | 0.008 | 7/47 (A-172, A498, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.012 | 7/48 (HEC-1-A, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13052.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.613×** | -10.1 | 3e-21 | 34/47 (SNU-423, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.690×** | -7.7 | 5e-12 | 30/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.703×** | -6.6 | 6e-09 | 29/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.726×** | -6.4 | 3e-08 | 24/46 (Panc 03.27, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.748×** | -6.0 | 2e-07 | 21/47 (HEC-1-A, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.730×** | -5.9 | 3e-07 | 23/48 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.593×** | -5.6 | 1e-06 | 23/47 (SW1417, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.806×** | -4.5 | 6e-04 | 17/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.817×** | -4.2 | 0.002 | 9/48 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.684×** | -4.1 | 0.002 | 16/41 (NCI-H1792, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.881× | -3.7 | 0.011 | 8/48 (A-172, NCI-H661, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.827×** | -3.6 | 0.017 | 15/47 (SW480, SW1417, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -3.4 | 0.025 | 14/48 (SNU-423, HS-578T, …) | all doses, flat |  |
| [[Piroxicam (drug)]] 0.05 µM |  | 0.861× | -3.1 | 0.077 | 9/48 (NCI-H2030, SW1417, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.852× | -3.0 | 0.097 | 12/48 (COLO 205, SNU-423, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.758×** | -3.0 | 0.097 | 8/47 (A549, NCI-H661, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13052. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 19.6 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +13.3) | [[Digitoxin (drug)]] 5 µM 0.441× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HCT15 (line)]] | alt | 29.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +12.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.210× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~20% of this change |
| [[NCI-H1573 (line)]] | alt | 19.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +13.2) | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -17.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 50.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.6) | [[Docetaxel (drug)]] 0.05 µM 0.331× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 18.4 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +9.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.226× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~20% of this change |
| [[A-172 (line)]] | wt | 33.5 | 1 | 1 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.07× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.373× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[BT-474 (line)]] | alt | 26.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +9.1) | — |
| [[C32 (line)]] | wt | 20.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 19.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +11.2) | — |
| [[LoVo (line)]] | wt | 17.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +17.3) | — |
| [[NCI-H1792 (line)]] | alt | 33.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +10.3) | [[Bortezomib (drug)]] 5 µM 0.105× (z -9.8) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 17.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +10.3) | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.239× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 16.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.8) | — |
| [[SW480 (line)]] | alt | 27.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.2) | — |
| [[CHP-212 (line)]] | wt | 42.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -8.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 26.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 67.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 37.8 | 1 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.06× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 10.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 24.8 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.136× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 15.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.32× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 26.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +13.6) | — |
| [[SK-MEL-2 (line)]] | alt | 41.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.4) | — |
| [[SNU-1 (line)]] | wt | 28.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0929× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.225× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13052), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP2]] | +0.81 | +0.82 / +0.47 | both halves | 2e-05 |  |
| [[PCNX4-DT]] | +0.79 | +0.81 / +0.45 | both halves | 3e-05 |  |
| [[ATE1OSP]] | +0.79 | +0.79 / +0.43 | both halves | 4e-05 |  |
| [[AK9]] | +0.78 | +0.85 / +0.46 | both halves | 3e-05 |  |
| [[TMEM202-AS1]] | +0.78 | +0.76 / +0.43 | both halves | 3e-05 |  |
| [[OXA1L-DT]] | +0.77 | +0.77 / +0.52 | both halves | 1e-05 |  |
| [[ZNF407-AS1]] | +0.77 | +0.82 / +0.40 | both halves | 5e-05 |  |
| [[MFF-DT]] | +0.77 | +0.74 / +0.41 | both halves | 4e-05 |  |
| [[PKN2-AS1]] | +0.77 | +0.78 / +0.42 | both halves | 4e-05 |  |
| [[FAM200A]] | +0.76 | +0.81 / +0.37 | both halves | 7e-05 |  |
| [[GTF2H1]] | +0.75 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[BCDIN3D]] | +0.75 | +0.73 / +0.45 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM118A]] | -0.71 | -0.70 / -0.35 | both halves | 1e-04 |  |
| [[GNA12]] | -0.70 | -0.75 / -0.34 | both halves | 1e-04 |  |
| [[PACC1]] | -0.67 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[WASF3]] | -0.67 | -0.63 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFCAB6]] | B | EFCAB6 activity raises METTL6's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.68× lower at baseline in the lines without EFCAB6 | 0.037 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers METTL6's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MTX3]] | C | MTX3 activity raises METTL6's level | lines that do not express MTX3 (3) vs lines expressing it (47) | 1.87× lower at baseline in the lines without MTX3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WDR35, GGT7, MNS1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.834). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.1, 13.8); signed map (18.2, -19.0). **Vector** length 88.4, 18.5% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.5 | +14.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +16.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +18.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +6.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +5.2 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +11.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +6.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +6.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +1.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | +0.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.9 | -1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | +2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -4.1 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | +1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -5.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | methyltransferase 6, tRNA N3-cytidine |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:15,381,275-15,440,566 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC24132 |
| Gene groups (HGNC) | 7BS N3-cytosine RNA methyltransferases; DNA/RNA methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCB7](https://www.uniprot.org/uniprotkb/Q8TCB7) (tRNA N(3)-cytidine methyltransferase METTL6):

> S-adenosyl-L-methionine-dependent methyltransferase that mediates N(3)-methylcytidine modification of residue 32 of the tRNA anticodon loop of tRNA(Ser), including tRNA(Ser)(UGA) and tRNA(Ser)(GCU). Interaction with SARS1/SerRS is required for N(3)-methylcytidine methylation.

**Summary**, from NCBI Gene [131965](https://www.ncbi.nlm.nih.gov/gene/131965):

> Enables enzyme binding activity and tRNA (cytidine-N3)-methyltransferase activity. Involved in tRNA C3-cytosine methylation. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28343](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28343) · Entrez [131965](https://www.ncbi.nlm.nih.gov/gene/131965) · UniProt [Q8TCB7](https://www.uniprot.org/uniprotkb/Q8TCB7) · Ensembl [ENSG00000206562](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206562)

## Data

Gene col 13052: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13052); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13052, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13052]; `tensor/DDL_lfc|DDL_z.npy` [13052]; `embed/gene_vectors.npy` [13052]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13052 or target_col == 13052). Every well: [[METTL6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/METTL6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
