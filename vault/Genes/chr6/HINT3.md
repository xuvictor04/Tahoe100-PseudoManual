---
symbol: "HINT3"
type: "gene"
col: 3306
ensembl_id: "ENSG00000111911"
name: "histidine triad nucleotide binding protein 3"
location: "6q22.32"
module: 29
arm: "+"
pooled_cpm: 25.89
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 19
n_dd_up_clean: 10
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# HINT3

*histidine triad nucleotide binding protein 3* — 6q22.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.87× (z +11.6, q 1e-28, up in 32 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.32× (z +5.0, q 7e-05, up in 19 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.719× (z -8.7, q 2e-15, down in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.797× (z -6.0, q 2e-07, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM106B]] (+0.64, fdr 1e-05), [[CFL2]] (+0.63, fdr 1e-05), [[DLD]] (+0.63, fdr 9e-06); moves opposite to [[C11orf91]] (-0.63, fdr 1e-05), [[TUBB6]] (-0.58, fdr 1e-05), [[POLG]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3306.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +11.6 | 1e-28 | 32/40 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.91×** | +11.6 | 1e-28 | 26/33 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +6.9 | 1e-09 | 20/39 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.24×** | +5.6 | 2e-06 | 21/48 (LoVo, A-172, …) | rises with dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +5.6 | 2e-06 | 21/44 (LS 180, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +5.0 | 7e-05 | 19/47 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.29×** | +4.5 | 4e-04 | 20/47 (AsPC-1, LS 180, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 0.001 | 16/48 (NCI-H23, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.26×** | +4.3 | 0.001 | 17/48 (AsPC-1, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +4.3 | 0.001 | 14/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.17× | +4.1 | 0.002 | 14/48 (Hs 766T, PANC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.26×** | +4.0 | 0.003 | 12/47 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.22×** | +3.9 | 0.005 | 16/48 (NCI-H2347, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.9 | 0.005 | 11/48 (LoVo, Hs 766T, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.006 | 13/47 (AsPC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.007 | 16/48 (A-427, J82, …) | rises with dose |  |
| [[Trifluridine (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.008 | 12/48 (LOX-IMVI, SW 1271, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Alpelisib (drug)]] 5 µM |  | **1.47×** | +3.6 | 0.010 | 7/45 (LoVo, COLO 205, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.025 | 6/48 (J82, HEC-1-A, …) | rises with dose |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.041 | 10/47 (LS 180, HT-29, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.049 | 7/48 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.057 | 12/48 (SW480, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3306.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.719×** | -8.7 | 2e-15 | 33/48 (RKO, SNU-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.675×** | -7.3 | 7e-11 | 28/48 (NCI-H460, LS 180, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.691×** | -6.9 | 1e-09 | 27/46 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.714×** | -6.3 | 5e-08 | 25/47 (NCI-H460, LoVo, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.718×** | -6.2 | 8e-08 | 24/48 (PANC-1, SW480, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.797×** | -6.0 | 2e-07 | 23/48 (PANC-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.550×** | -5.6 | 2e-06 | 25/46 (SNU-423, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.746×** | -5.5 | 3e-06 | 22/47 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.565×** | -5.3 | 7e-06 | 21/46 (LOX-IMVI, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.818×** | -5.3 | 7e-06 | 21/48 (SW1417, MIA PaCa-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.749×** | -5.2 | 1e-05 | 21/47 (A498, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.762×** | -5.1 | 2e-05 | 24/48 (NCI-H460, LS 180, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.778×** | -4.7 | 1e-04 | 22/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.779×** | -4.7 | 1e-04 | 23/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.716×** | -4.4 | 3e-04 | 19/48 (KATO III, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.832×** | -3.4 | 0.019 | 11/47 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Bergenin (drug)]] 0.5 µM |  | 0.834× | -3.4 | 0.022 | 11/47 (SW1417, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.779×** | -3.3 | 0.025 | 12/48 (KATO III, SNU-423, …) | two highest doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.891× | -3.0 | 0.060 | 16/48 (NCI-H460, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3306. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 26.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -13.1) |
| [[LoVo (line)]] | wt | 35.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +11.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 13.9 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -10.2) |
| [[COLO 205 (line)]] | alt | 24.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -11.1) |
| [[J82 (line)]] | alt | 17.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 28.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -10.8) |
| [[SNU-1 (line)]] | wt | 27.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -8.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Rapamycin (drug)]] 0.5 µM 0.212× (z -8.8) |
| [[SNU-423 (line)]] | alt | 46.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -9.9) |
| [[SW480 (line)]] | alt | 27.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.372× (z -9.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-427 (line)]] | wt | 25.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -12.2) ⚠ cell-cycle shift, explains ~69% of this change |
| [[HEC-1-A (line)]] | alt | 23.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.64× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 46.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -16.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 28.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -9.8) |
| [[RKO (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -9.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW48 (line)]] | wt | 26.4 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.139× (z -9.7) |
| [[A-172 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3306), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM106B]] | +0.64 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[CFL2]] | +0.63 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[DLD]] | +0.63 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[SYNJ2BP]] | +0.62 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[PAIP1]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[TMEM126B]] | +0.61 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[SCP2]] | +0.61 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[BROX]] | +0.61 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[CREBL2]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SCARB2]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[RBBP9]] | +0.60 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[SCRN3]] | +0.59 | +0.46 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf91]] | -0.63 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[TUBB6]] | -0.58 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[POLG]] | -0.58 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[MEIS3]] | -0.57 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[IL9RP3]] | -0.56 | -0.38 / -0.62 | both halves | 6e-05 |  |
| [[CCM2]] | -0.56 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[TTLL3]] | -0.56 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[BLZF2P]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[DMPK]] | -0.54 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[MYO9B]] | -0.54 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[UBASH3B]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[TRIOBP]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises HINT3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers HINT3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.486). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-16.6, 2.7); signed map (-17.3, -41.5). **Vector** length 94.7, 20.5% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +6.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +5.4 | +5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | +3.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.3 | +4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.1 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | +4.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -3.4 | -5.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -5.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -2.3 | -6.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -2.2 | -3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -5.6 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -1.8 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | histidine triad nucleotide binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.32 — chr6:125,956,770-125,980,244 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33126, HINT4 |
| Gene groups (HGNC) | Histidine triad superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQE9](https://www.uniprot.org/uniprotkb/Q9NQE9) (Adenosine 5'-monophosphoramidase HINT3):

> Exhibits adenosine 5'-monophosphoramidase activity, hydrolyzing purine nucleotide phosphoramidates with a single phosphate group such as adenosine 5'monophosphoramidate (AMP-NH2) to yield AMP and NH2. Hydrolyzes lysyl-AMP (AMP-N-epsilon-(N-alpha-acetyl lysine methyl ester)) generated by lysine tRNA ligase. Hydrolyzes 3-indolepropionic acyl-adenylate and fluorogenic purine nucleoside tryptamine phosphoramidates in vitro.

**Summary**, from NCBI Gene [135114](https://www.ncbi.nlm.nih.gov/gene/135114):

> Histidine triad proteins, such as HINT3, are nucleotide hydrolases and transferases that act on the alpha-phosphate of ribonucleotides (Brenner, 2002 [PubMed 12119013]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:18468](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18468) · Entrez [135114](https://www.ncbi.nlm.nih.gov/gene/135114) · UniProt [Q9NQE9](https://www.uniprot.org/uniprotkb/Q9NQE9) · Ensembl [ENSG00000111911](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111911)

## Data

Gene col 3306: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3306); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3306, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3306]; `tensor/DDL_lfc|DDL_z.npy` [3306]; `embed/gene_vectors.npy` [3306]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3306 or target_col == 3306). Every well: [[HINT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HINT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
