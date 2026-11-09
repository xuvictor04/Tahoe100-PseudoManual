---
symbol: "CLPB"
type: "gene"
col: 8483
ensembl_id: "ENSG00000162129"
name: "ClpB family mitochondrial disaggregase"
location: "11q13.4"
module: 4
arm: "+"
pooled_cpm: 33.42
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 15
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CLPB

*ClpB family mitochondrial disaggregase* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.32× (z +17.5, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.439× (z -24.3, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS27]] (+0.70, fdr 7e-06), [[NUDC]] (+0.69, fdr 7e-06), [[NAA25]] (+0.69, fdr 7e-06); moves opposite to [[LNX2]] (-0.74, fdr 7e-06), [[ARID4A]] (-0.71, fdr 7e-06), [[AAMDC]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8483.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.32×** | +17.5 | 0e+00 | 44/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.17×** | +15.2 | 0e+00 | 44/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.05×** | +15.0 | 0e+00 | 44/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.58×** | +9.5 | 3e-19 | 38/48 (MIA PaCa-2, PANC-1, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.96×** | +7.3 | 2e-11 | 35/43 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +7.2 | 5e-11 | 27/48 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +6.9 | 4e-10 | 23/46 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.71×** | +5.9 | 3e-07 | 22/48 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **1.31×** | +5.3 | 6e-06 | 21/41 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.43×** | +5.3 | 7e-06 | 23/48 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.29×** | +5.0 | 3e-05 | 18/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +5.0 | 3e-05 | 21/48 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +4.7 | 1e-04 | 21/48 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +4.7 | 1e-04 | 24/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.52×** | +4.5 | 2e-04 | 22/48 (NCI-H23, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.51×** | +4.5 | 2e-04 | 24/48 (A549, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.010 | 11/47 (LoVo, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.6 | 0.010 | 16/48 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.024 | 6/47 (SW1417, SW480, …) | rises with dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8483.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.439×** | -24.3 | 0e+00 | 47/48 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.410×** | -17.9 | 0e+00 | 39/47 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.584×** | -10.8 | 7e-25 | 36/48 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.622×** | -9.9 | 4e-21 | 32/48 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.737×** | -9.0 | 2e-17 | 34/48 (J82, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.680×** | -8.1 | 7e-14 | 27/48 (RKO, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.746×** | -6.1 | 7e-08 | 28/48 (NCI-H2030, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.775×** | -5.3 | 7e-06 | 23/48 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.8 | 0.009 | 17/48 (J82, HCT15, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.842× | -3.6 | 0.017 | 13/48 (NCI-H661, A549, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -3.5 | 0.023 | 16/47 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.891× | -3.4 | 0.027 | 12/48 (NCI-H2030, SNU-1, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.857× | -3.2 | 0.054 | 12/47 (KATO III, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8483. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 25.6 | 3 | 3 | [[Ixazomib citrate (drug)]] 0.5 µM 3.21× (z +9.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -12.9) |
| [[LoVo (line)]] | wt | 41.8 | 5 (2 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.86× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 24.3 | 2 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.46× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.30× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -13.8) |
| [[RKO (line)]] | wt | 54.0 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -18.6) |
| [[SW480 (line)]] | alt | 33.5 | 4 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.49× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.22× (z +10.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -13.3) |
| [[PANC-1 (line)]] | alt | 61.1 | 3 | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.77× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -17.8) |
| [[C-33 A (line)]] | alt | 79.5 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -11.8) |
| [[C32 (line)]] | wt | 61.4 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -19.4) |
| [[J82 (line)]] | alt | 43.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -13.1) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 50.1 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -19.7) |
| [[NCI-H23 (line)]] | alt | 83.2 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +9.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -26.1) |
| [[HOP62 (line)]] | alt | 17.9 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.58× (z +10.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.289× (z -9.5) |
| [[HS-578T (line)]] | alt | 30.1 | 1 | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.89× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -11.6) |
| [[KATO III (line)]] | alt | 30.3 | 2 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.15× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -9.4) |
| [[LS 180 (line)]] | wt | 22.2 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 4.32× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 28.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -22.2) |
| [[NCI-H1573 (line)]] | alt | 21.0 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.76× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -10.6) |
| [[SNU-1 (line)]] | wt | 53.5 | 0 | 3 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0790× (z -13.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -8.9) |
| [[SNU-423 (line)]] | alt | 28.9 | 1 | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.77× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -11.4) |
| [[SW 1271 (line)]] | alt | 59.1 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0663× (z -10.5) |
| [[A-427 (line)]] | wt | 37.7 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -12.2) |
| [[COLO 205 (line)]] | alt | 17.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.95× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 31.2 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -13.9) |
| [[hTERT-HPNE (line)]] | wt | 17.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.93× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 34.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 33.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -10.1) |
| [[NCI-H661 (line)]] | alt | 28.1 | 0 | 2 | — | [[Ritonavir (drug)]] 5 µM 0.130× (z -9.0) |
| [[SW48 (line)]] | wt | 44.9 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -9.8) |
| [[A-172 (line)]] | wt | 29.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -9.1) |
| [[CHP-212 (line)]] | wt | 44.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.121× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 26.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 27.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 37.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 37.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -10.0) |
| [[SHP-77 (line)]] | alt | 37.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -13.4) |
| [[SW1417 (line)]] | alt | 32.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -12.5) |
| [[A498 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8483), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS27]] | +0.70 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[NUDC]] | +0.69 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[NAA25]] | +0.69 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[SARS2]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[TRRAP]] | +0.68 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.67 | +0.70 / +0.66 | both halves | 7e-06 | STRING 434 |
| [[NAA15]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[PSMD1]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[HERC2]] | +0.66 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[GFM1]] | +0.65 | +0.59 / +0.68 | both halves | 7e-06 | STRING 438 |
| [[DCAF1]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[VWA8]] | +0.65 | +0.69 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LNX2]] | -0.74 | -0.72 / -0.70 | both halves | 7e-06 |  |
| [[ARID4A]] | -0.71 | -0.68 / -0.69 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.67 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[CERT1]] | -0.65 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.64 | -0.58 / -0.70 | both halves | 8e-06 |  |
| [[PLAG1]] | -0.64 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[TSC22D4]] | -0.62 | -0.49 / -0.67 | both halves | 2e-05 |  |
| [[KLHL28]] | -0.62 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[CDC14A]] | -0.60 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[MINDY2]] | -0.60 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[GRB7]] | -0.59 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[GPRC5C]] | -0.59 | -0.49 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CLPB's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises CLPB's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.742). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-7.9, -33.1); signed map (-11.6, -46.7). **Vector** length 112, 28.6% of its response variance represented; |z| ≥ 3 in 1,272 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.53 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.4 | +17.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.0 | +15.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.2 | +15.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.8 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | +6.5 | +5.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.0 | +5.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.7 | +5.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.9 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -24.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -17.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -10.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.3 | -9.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | -3.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.5 | -3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.9 | -1.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.8 | -1.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | ClpB family mitochondrial disaggregase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:72,285,495-72,434,680 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SKD3, FLJ13152, ANKCLP |
| Gene groups (HGNC) | Ankyrin repeat domain containing; AAA ATPases; Chaperonins |
| Hallmark sets | SPERMATOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H078](https://www.uniprot.org/uniprotkb/Q9H078) (Mitochondrial disaggregase):

> Functions as a regulatory ATPase and participates in secretion/protein trafficking process. Has ATP-dependent protein disaggregase activity and is required to maintain the solubility of key mitochondrial proteins. Involved in mitochondrial-mediated antiviral innate immunity, activates RIG-I-mediated signal transduction and production of IFNB1 and pro-inflammatory cytokine IL6. Plays a role in granulocyte differentiation.

**Summary**, from NCBI Gene [81570](https://www.ncbi.nlm.nih.gov/gene/81570):

> This gene belongs to the ATP-ases associated with diverse cellular activities (AAA+) superfamily. Members of this superfamily form ring-shaped homo-hexamers and have highly conserved ATPase domains that are involved in various processes including DNA replication, protein degradation and reactivation of misfolded proteins. All members of this family hydrolyze ATP through their AAA+ domains and use the energy generated through ATP hydrolysis to exert mechanical force on their substrates. In …

**Accessions** — [HGNC:30664](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30664) · Entrez [81570](https://www.ncbi.nlm.nih.gov/gene/81570) · UniProt [Q9H078](https://www.uniprot.org/uniprotkb/Q9H078) · Ensembl [ENSG00000162129](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162129)

## Data

Gene col 8483: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8483); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8483, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8483]; `tensor/DDL_lfc|DDL_z.npy` [8483]; `embed/gene_vectors.npy` [8483]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8483 or target_col == 8483). Every well: [[CLPB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLPB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
