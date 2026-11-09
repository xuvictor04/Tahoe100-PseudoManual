---
symbol: "CAMKK1"
type: "gene"
col: 49
ensembl_id: "ENSG00000004660"
name: "calcium/calmodulin dependent protein kinase kinase 1"
location: "17p13.2"
module: 3
arm: "+"
pooled_cpm: 15.02
n_lines_expressing: 46
n_dd_up: 15
n_dd_down: 21
n_dd_up_clean: 15
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CAMKK1

*calcium/calmodulin dependent protein kinase kinase 1* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 1.75× (z +6.7, q 1e-08, up in 23 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.599× (z -8.6, q 6e-15, down in 28 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD27]] (+0.73, fdr 7e-06), [[SLC27A1]] (+0.71, fdr 9e-06), [[MAST1]] (+0.69, fdr 1e-05); moves opposite to [[DECR1]] (-0.65, fdr 4e-05), [[EIF4G2]] (-0.63, fdr 2e-05), [[TUG1]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[STK32C]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, none with an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 49.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.75×** | +6.7 | 1e-08 | 23/43 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.46×** | +6.4 | 3e-08 | 25/44 (A549, HCT15, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.65×** | +6.0 | 4e-07 | 20/44 (KATO III, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +5.7 | 2e-06 | 22/44 (KATO III, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +5.4 | 6e-06 | 19/44 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +4.6 | 5e-04 | 19/38 (A549, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +4.4 | 0.001 | 16/41 (SW480, J82, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +4.3 | 0.001 | 15/40 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.010 | 20/43 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.014 | 14/44 (LOX-IMVI, HOP62, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +3.6 | 0.018 | 15/44 (A549, HOP62, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.035 | 12/44 (KATO III, SW1417, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.32×** | +3.4 | 0.035 | 7/44 (HOP62, A-172, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.061 | 13/44 (SW480, KATO III, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.070 | 10/43 (A498, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 49.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.599×** | -8.6 | 6e-15 | 28/44 (A-172, A498, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.492×** | -8.1 | 2e-13 | 26/42 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -7.0 | 5e-10 | 25/40 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.560×** | -6.8 | 1e-09 | 24/43 (NCI-H460, PANC-1, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.564×** | -6.8 | 1e-09 | 20/33 (MIA PaCa-2, SW48, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.555×** | -6.7 | 2e-09 | 23/43 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.560×** | -6.6 | 3e-09 | 26/41 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.579×** | -6.5 | 7e-09 | 24/41 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.582×** | -6.4 | 1e-08 | 25/44 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.695×** | -6.1 | 7e-08 | 22/44 (LS 180, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.613×** | -5.6 | 1e-06 | 17/20 (SW480, LS 180, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.657×** | -4.6 | 2e-04 | 17/25 (NCI-H460, A-172, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.698×** | -4.2 | 9e-04 | 19/43 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **0.703×** | -4.2 | 0.001 | 17/43 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.724×** | -3.8 | 0.005 | 17/42 (HS-578T, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.725×** | -3.8 | 0.005 | 19/43 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Amsacrine (drug)]] 5 µM |  | **0.802×** | -3.7 | 0.008 | 11/44 (A498, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.743×** | -3.5 | 0.014 | 14/43 (A498, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.750×** | -3.4 | 0.020 | 12/43 (A498, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 49. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 35.6 | 0 | 10 (4 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0357× (z -22.3) |
| [[A498 (line)]] | wt | 27.9 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.211× (z -11.1) |
| [[PANC-1 (line)]] | alt | 17.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.178× (z -10.9) |
| [[A-172 (line)]] | wt | 62.7 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.233× (z -13.0) |
| [[SW48 (line)]] | wt | 42.4 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0781× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.133× (z -12.2) |
| [[HOP62 (line)]] | alt | 21.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -10.6) |
| [[SNU-423 (line)]] | alt | 16.7 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0617× (z -13.2) |
| [[LS 180 (line)]] | wt | 22.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.399× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 33.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -14.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 16.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -13.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -8.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 4.56 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0612× (z -8.8) |
| [[H4 (line)]] | wt | 22.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -10.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 5.33 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.137× (z -8.7) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H23 (line)]] | alt | 12.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -8.6) |
| [[RKO (line)]] | wt | 13.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0670× (z -12.9) |
| [[A-427 (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 49), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD27]] | +0.73 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[SLC27A1]] | +0.71 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[MAST1]] | +0.69 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[CCDC112]] | +0.67 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[EML2]] | +0.64 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[DCAF4]] | +0.64 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[MGST3]] | +0.64 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SH3PXD2B]] | +0.62 | +0.64 / +0.36 | both halves | 9e-05 |  |
| [[RAB40C]] | +0.62 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[PKD1P6]] | +0.61 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[RAC3]] | +0.60 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[NTHL1]] | +0.60 | +0.32 / +0.52 | both halves | 1e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DECR1]] | -0.65 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[EIF4G2]] | -0.63 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[TUG1]] | -0.62 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[TRIP12]] | -0.61 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[TAX1BP3]] | -0.59 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[PBLD]] | -0.58 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[ARSB]] | -0.58 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[PSME3IP1]] | -0.58 | -0.43 / -0.44 | both halves | 4e-05 |  |
| [[MOB1A]] | -0.58 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[CHMP3]] | -0.57 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[CRPPA]] | -0.57 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[TAFA2]] | -0.56 | -0.46 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CAMKK1's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[RAC3]] | B | RAC3 activity raises CAMKK1's level | lines that do not express RAC3 (7) vs lines expressing it (43) | 1.78× lower at baseline in the lines without RAC3 | 0.086 | ⚠ within organs, on part of the lines; also absent: FKBP10; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STK32C]] | C | CAMKK1 activity raises STK32C's level | lines that do not express CAMKK1 (4) vs lines expressing it (46) | 1.79× lower at baseline in the lines without CAMKK1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CKAP4, ADGRB2, POGLUT3; maybe low, not absent; its own permutation p |
| [[RAC3]] | C | CAMKK1 activity raises RAC3's level | lines that do not express CAMKK1 (4) vs lines expressing it (46) | 2.07× lower at baseline in the lines without CAMKK1 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CKAP4, ADGRB2, POGLUT3; maybe low, not absent |
| [[IMPDH1]] | C | CAMKK1 activity raises IMPDH1's level | lines that do not express CAMKK1 (4) vs lines expressing it (46) | 1.84× lower at baseline in the lines without CAMKK1 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CKAP4, ADGRB2, POGLUT3; maybe low, not absent |
| [[MCRIP2]] | C | CAMKK1 activity raises MCRIP2's level | lines that do not express CAMKK1 (4) vs lines expressing it (46) | 1.52× lower at baseline in the lines without CAMKK1 | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CKAP4, ADGRB2, POGLUT3; maybe low, not absent |
| [[HIP1]] | C | CAMKK1 activity raises HIP1's level | lines that do not express CAMKK1 (4) vs lines expressing it (46) | 1.80× lower at baseline in the lines without CAMKK1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CKAP4, ADGRB2, POGLUT3; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (8.0, -1.2); signed map (-27.1, 21.9). **Vector** length 105, 24.3% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +5.2 | +6.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.9 | +6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +5.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +6.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.1 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +4.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +2.8 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +3.2 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -8.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.2 | -6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.1 | -8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.1 | -4.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.0 | -6.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.4 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | calcium/calmodulin dependent protein kinase kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:3,860,315-3,894,891 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761M0423, CAMKKA, MGC34095 |
| Gene groups (HGNC) | Calcium/calmodulin dependent protein kinase kinase family |
| Reactome | 19 pathways, smallest: Activation of RAC1 downstream of NMDARs; CREB1 phosphorylation through the activation of CaMKII/CaMKK/CaMKIV cascasde; CaMK IV-mediated phosphorylation of CREB |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5S9](https://www.uniprot.org/uniprotkb/Q8N5S9) (Calcium/calmodulin-dependent protein kinase kinase 1):

> Calcium/calmodulin-dependent protein kinase that belongs to a proposed calcium-triggered signaling cascade involved in a number of cellular processes. Phosphorylates CAMK1, CAMK1D, CAMK1G and CAMK4. Involved in regulating cell apoptosis. Promotes cell survival by phosphorylating AKT1/PKB that inhibits pro-apoptotic BAD/Bcl2-antagonist of cell death.

**Summary**, from NCBI Gene [84254](https://www.ncbi.nlm.nih.gov/gene/84254):

> The product of this gene belongs to the Serine/Threonine protein kinase family, and to the Ca(2+)/calmodulin-dependent protein kinase subfamily. This protein plays a role in the calcium/calmodulin-dependent (CaM) kinase cascade. Three transcript variants encoding two distinct isoforms have been identified for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1469](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1469) · Entrez [84254](https://www.ncbi.nlm.nih.gov/gene/84254) · UniProt [Q8N5S9](https://www.uniprot.org/uniprotkb/Q8N5S9) · Ensembl [ENSG00000004660](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000004660)

## Data

Gene col 49: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 49); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 49, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 49]; `tensor/DDL_lfc|DDL_z.npy` [49]; `embed/gene_vectors.npy` [49]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 49 or target_col == 49). Every well: [[CAMKK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAMKK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
