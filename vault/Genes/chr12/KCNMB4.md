---
symbol: "KCNMB4"
type: "gene"
col: 5737
ensembl_id: "ENSG00000135643"
name: "potassium calcium-activated channel subfamily M regulatory beta subunit 4"
location: "12q15"
module: 53
arm: "+"
pooled_cpm: 24.87
n_lines_expressing: 45
n_dd_up: 16
n_dd_down: 23
n_dd_up_clean: 16
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# KCNMB4

*potassium calcium-activated channel subfamily M regulatory beta subunit 4* — 12q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.72× (z +13.6, q 1e-39, up in 36 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.513× (z -11.9, q 4e-30, down in 32 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.553× (z -10.6, q 1e-23, down in 28 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RGS2]] (+0.59, fdr 1e-05), [[PRKCG]] (+0.57, fdr 1e-05), [[ITGA2B]] (+0.56, fdr 1e-05); moves opposite to [[TMCO4]] (-0.50, fdr 4e-05), [[CNDP2]] (-0.49, fdr 3e-05), [[ATXN10]] (-0.48, fdr 5e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[ADRA1B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, none with an alert; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5737.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +13.6 | 1e-39 | 36/43 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +12.1 | 3e-31 | 22/42 (NCI-H1792, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.81×** | +10.6 | 8e-24 | 25/43 (CFPAC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.81×** | +10.5 | 8e-24 | 25/42 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +10.2 | 2e-22 | 27/43 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +9.9 | 3e-21 | 26/43 (HT-29, A498, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +9.5 | 1e-19 | 28/41 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +7.3 | 1e-11 | 24/42 (HT-29, AsPC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +6.6 | 2e-09 | 19/41 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +5.6 | 1e-06 | 18/42 (HS-578T, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.34×** | +5.2 | 8e-06 | 12/43 (RKO, AsPC-1, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.75×** | +5.0 | 2e-05 | 12/40 (LS 180, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +4.3 | 6e-04 | 11/43 (SW480, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +4.0 | 0.003 | 11/42 (LoVo, A549, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.4 | 0.022 | 8/43 (HOP62, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5737.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.513×** | -11.9 | 4e-30 | 32/41 (Hs 766T, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.553×** | -10.6 | 1e-23 | 28/43 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.565×** | -10.2 | 4e-22 | 26/42 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.613×** | -8.8 | 3e-16 | 25/42 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.634×** | -8.2 | 4e-14 | 27/42 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.647×** | -7.8 | 6e-13 | 22/43 (NCI-H460, LS 180, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.643×** | -7.6 | 2e-12 | 21/30 (A-427, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.649×** | -7.4 | 8e-12 | 24/42 (MIA PaCa-2, NCI-H1792, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.685×** | -6.8 | 8e-10 | 23/42 (NCI-H460, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.687×** | -6.7 | 1e-09 | 21/42 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.701×** | -6.3 | 1e-08 | 17/42 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.694×** | -6.3 | 2e-08 | 23/39 (A-427, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.687×** | -6.2 | 2e-08 | 20/33 (Panc 03.27, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.708×** | -6.2 | 3e-08 | 18/43 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.588×** | -4.8 | 7e-05 | 20/40 (H4, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.612×** | -4.4 | 4e-04 | 15/41 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.854× | -4.0 | 0.002 | 10/43 (NCI-H460, HCT15, …) | all doses, flat |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.798×** | -3.8 | 0.004 | 12/41 (MIA PaCa-2, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.806×** | -3.7 | 0.006 | 15/42 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5737. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 80.5 | 0 | 20 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -14.5) |
| [[Hs 766T (line)]] | wt | 25.6 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -9.8) |
| [[A-427 (line)]] | wt | 42.7 | 0 | 5 (5 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -16.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 41.1 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.187× (z -10.8) |
| [[LoVo (line)]] | wt | 33.3 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.304× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 25.7 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -11.5) |
| [[LS 180 (line)]] | wt | 39.6 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.303× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.322× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 18.1 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.35× (z +8.6) | [[Docetaxel (drug)]] 0.05 µM 0.302× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~10% of this change |
| [[NCI-H1573 (line)]] | alt | 21.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -10.7) |
| [[SW480 (line)]] | alt | 27.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.238× (z -12.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 80.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0605× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 8.47 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +10.7) | — |
| [[J82 (line)]] | alt | 34.2 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 15.9 | 0 | 2 | — | [[Belumosudil (drug)]] 5 µM 0.112× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 14.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.17× (z +14.1) | [[Digitoxin (drug)]] 0.5 µM 0.146× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 51.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -13.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 45.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.366× (z -8.6) |
| [[SNU-423 (line)]] | alt | 25.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.137× (z -11.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -9.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 18.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -9.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 13.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +12.0) | — |
| [[HT-29 (line)]] | alt | 17.3 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.89× (z +8.6) | — |
| [[KATO III (line)]] | alt | 7.22 | 0 | 1 | — | [[Decitabine (drug)]] 5 µM 0.0506× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 18.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.68× (z +15.0) | — |
| [[NCI-H2347 (line)]] | alt | 37.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.00× (z +9.0) | — |
| [[RKO (line)]] | wt | 17.5 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.0600× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 18.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -10.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.58 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.23 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5737), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGS2]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[PRKCG]] | +0.57 | +0.59 / +0.56 | both halves | 1e-05 | pathway: Neuronal System |
| [[ITGA2B]] | +0.56 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[TNFRSF10D]] | +0.55 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[FSCN1]] | +0.53 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[PTGER4]] | +0.53 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[GLRX]] | +0.52 | +0.37 / +0.49 | both halves | 7e-05 |  |
| [[LRRC23]] | +0.51 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PDGFA]] | +0.50 | +0.47 / +0.35 | both halves | 1e-04 |  |
| [[CCDC28B]] | +0.50 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[BCORL1]] | +0.50 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[NEFM]] | +0.50 | +0.46 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMCO4]] | -0.50 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[CNDP2]] | -0.49 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ATXN10]] | -0.48 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[SELENOI]] | -0.46 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[SLC35F6]] | -0.46 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[ATR]] | -0.46 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[RUFY3]] | -0.44 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[KCTD13]] | -0.42 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[NAA50]] | -0.41 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[LRRK1]] | -0.41 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[ABCF2]] | -0.41 | -0.28 / -0.41 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADRA1B]] | B | KCNMB4 activity lowers ADRA1B's level | lines that do not express KCNMB4 (5) vs lines expressing it (45) | 1.82× higher at baseline in the lines without KCNMB4 | 0.029 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CNDP2]] | B | KCNMB4 activity lowers CNDP2's level | lines that do not express KCNMB4 (5) vs lines expressing it (45) | 1.64× higher at baseline in the lines without KCNMB4 | 0.043 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.397). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.3, -17.5); signed map (14.6, 18.8). **Vector** length 91.0, 19.4% of its response variance represented; |z| ≥ 3 in 1,229 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +12.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +13.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +9.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +10.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +4.0 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -4.4 | -7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -7.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.1 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.1 | -8.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -1.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.6 | -4.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.5 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | potassium calcium-activated channel subfamily M regulatory beta subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q15 — chr12:70,366,290-70,434,292 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Potassium calcium-activated channel subfamily M regulatory beta subunits |
| Reactome | 7 pathways, smallest: Ca2+ activated K+ channels; cGMP effects; Nitric oxide stimulates guanylate cyclase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86W47](https://www.uniprot.org/uniprotkb/Q86W47) (Calcium-activated potassium channel subunit beta-4):

> Regulatory subunit of the calcium activated potassium KCNMA1 (maxiK) channel. Modulates the calcium sensitivity and gating kinetics of KCNMA1, thereby contributing to KCNMA1 channel diversity. Decreases the gating kinetics and calcium sensitivity of the KCNMA1 channel, but with fast deactivation kinetics. May decrease KCNMA1 channel openings at low calcium concentrations but increases channel openings at high calcium concentrations. Makes KCNMA1 channel resistant to 100 nM charybdotoxin (CTX) …

**Summary**, from NCBI Gene [27345](https://www.ncbi.nlm.nih.gov/gene/27345):

> MaxiK channels are large conductance, voltage and calcium-sensitive potassium channels which are fundamental to the control of smooth muscle tone and neuronal excitability. MaxiK channels can be formed by 2 subunits: the pore-forming alpha subunit and the modulatory beta subunit. The protein encoded by this gene is an auxiliary beta subunit which slows activation kinetics, leads to steeper calcium sensitivity, and shifts the voltage range of current activation to more negative potentials than …

**Accessions** — [HGNC:6289](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6289) · Entrez [27345](https://www.ncbi.nlm.nih.gov/gene/27345) · UniProt [Q86W47](https://www.uniprot.org/uniprotkb/Q86W47) · Ensembl [ENSG00000135643](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135643)

## Data

Gene col 5737: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5737); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5737, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5737]; `tensor/DDL_lfc|DDL_z.npy` [5737]; `embed/gene_vectors.npy` [5737]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5737 or target_col == 5737). Every well: [[KCNMB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNMB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
