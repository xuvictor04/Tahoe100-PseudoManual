---
symbol: "KDM4A"
type: "gene"
col: 819
ensembl_id: "ENSG00000066135"
name: "lysine demethylase 4A"
location: "1p34.2-p34.1"
module: 63
arm: "+"
pooled_cpm: 54.77
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# KDM4A

*lysine demethylase 4A* — 1p34.2-p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.42× (z +7.9, q 2e-12, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.535× (z -14.0, q 5e-42, down in 41 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.562× (z -12.9, q 8e-36, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHAC1]] (+0.69, fdr 1e-05), [[SESN2]] (+0.65, fdr 7e-06), [[MARS1]] (+0.65, fdr 7e-06); moves opposite to [[IFNGR2]] (-0.54, fdr 4e-05), [[SLC22A4]] (-0.50, fdr 6e-05), [[SPAG1]] (-0.49, fdr 2e-04).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 819.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +7.9 | 2e-12 | 30/48 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +7.1 | 4e-10 | 27/48 (SW1417, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.30×** | +5.5 | 8e-06 | 24/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.25×** | +5.0 | 9e-05 | 22/48 (MIA PaCa-2, J82, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.25×** | +4.9 | 9e-05 | 24/48 (C-33 A, HEC-1-A, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +4.6 | 3e-04 | 21/48 (C-33 A, NCI-H23, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.24×** | +4.2 | 0.002 | 17/48 (NCI-H2030, LoVo, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.20× | +4.1 | 0.003 | 19/48 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.19× | +3.9 | 0.005 | 16/48 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.37×** | +3.7 | 0.013 | 15/44 (NCI-H1792, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.7 | 0.013 | 10/48 (AsPC-1, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.094 | 12/47 (A-172, BT-474, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.15× | +3.0 | 0.10 | 6/48 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 819.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.535×** | -14.0 | 5e-42 | 41/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.562×** | -12.9 | 8e-36 | 40/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.706×** | -11.0 | 4e-26 | 31/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.656×** | -8.8 | 3e-16 | 31/44 (NCI-H2030, RKO, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.682×** | -8.6 | 9e-16 | 38/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.683×** | -8.6 | 9e-16 | 35/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.684×** | -8.2 | 2e-14 | 33/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.696×** | -8.1 | 3e-14 | 37/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.760×** | -6.2 | 5e-08 | 29/47 (NCI-H460, H4, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.620×** | -5.6 | 1e-06 | 17/36 (C32, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -5.5 | 3e-06 | 23/48 (SNU-1, A-427, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.676×** | -4.6 | 2e-04 | 21/49 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.823×** | -4.4 | 5e-04 | 20/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change | **0.819×** | -4.3 | 7e-04 | 20/42 (NCI-H460, PANC-1, …) | all doses, flat | composition shift |
| [[Arbutin (drug)]] 5 µM |  | 0.842× | -3.7 | 0.008 | 16/48 (RKO, LS 180, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.843× | -3.5 | 0.014 | 19/47 (RKO, A-427, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[vincristine (drug)]] 0.05 µM |  | 0.860× | -3.2 | 0.044 | 9/48 (CFPAC-1, NCI-H460, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 819. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 40.9 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.360× (z -12.5) |
| [[PANC-1 (line)]] | alt | 79.5 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -25.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -20.3) |
| [[BT-474 (line)]] | alt | 68.1 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.242× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.322× (z -10.7) |
| [[SW480 (line)]] | alt | 54.7 | 1 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.91× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.357× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.421× (z -11.7) |
| [[HT-29 (line)]] | alt | 70.6 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.371× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 92.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -15.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.442× (z -9.9) |
| [[A-427 (line)]] | wt | 85.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -11.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.453× (z -9.0) |
| [[H4 (line)]] | wt | 66.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -13.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.292× (z -8.7) |
| [[HS-578T (line)]] | alt | 62.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -13.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[J82 (line)]] | alt | 51.7 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.44× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -9.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[KATO III (line)]] | alt | 67.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.294× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.399× (z -9.6) |
| [[LoVo (line)]] | wt | 55.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[MIA PaCa-2 (line)]] | alt | 58.5 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.49× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 43.1 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.305× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 58.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -16.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 52.3 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.38× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.334× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[SNU-1 (line)]] | wt | 78.2 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 55.2 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.103× (z -11.2) ⚠ toxic |
| [[LS 180 (line)]] | wt | 61.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.320× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[RKO (line)]] | wt | 64.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.180× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.252× (z -12.8) |
| [[SW1417 (line)]] | alt | 59.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.24× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -11.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 81.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -8.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 55.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.310× (z -9.9) |
| [[HCT15 (line)]] | alt | 64.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -8.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 48.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -10.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 41.3 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0943× (z -11.0) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 63.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -8.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SNU-423 (line)]] | alt | 38.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[A-172 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 56.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 819), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHAC1]] | +0.69 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[SESN2]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[MARS1]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[AARS1]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[COASY]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[XPOT]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[TRIB3]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[GOT1]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[SEPHS2]] | +0.60 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[AAK1]] | +0.58 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[PSAT1]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[SARS1]] | +0.57 | +0.50 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFNGR2]] | -0.54 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[SLC22A4]] | -0.50 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[SPAG1]] | -0.49 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[ANKRD18A]] | -0.48 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[FAM81A]] | -0.48 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[TGIF2]] | -0.47 | -0.49 / -0.37 | both halves | 7e-05 |  |
| [[S100A4]] | -0.47 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[HIVEP1]] | -0.47 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[NEMP2-DT]] | -0.46 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[HIVEP2]] | -0.45 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[KAT2B]] | -0.44 | -0.39 / -0.31 | both halves | 2e-04 | pathway: Chromatin modifying enzymes; STRING 434 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers KDM4A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.9, 49.2); signed map (-13.0, 25.7). **Vector** length 105, 25.9% of its response variance represented; |z| ≥ 3 in 1,036 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.53 to 16); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.57 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.57 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.5 | +4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | +5.4 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.3 | +3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.0 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +2.8 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +3.0 | +1.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.7 | +2.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +2.6 | +1.2 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.3 | -8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.1 | -5.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.6 | -14.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.2 | -8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change | -5.1 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -4.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.8 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | +0.0 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -2.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | lysine demethylase 4A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2-p34.1 — chr1:43,650,149-43,705,518 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0677, JHDM3A, TDRD14A; previously JMJD2, JMJD2A |
| Gene groups (HGNC) | PHD finger proteins; Tudor domain containing; Lysine demethylase 4 family |
| Reactome | 10 pathways, smallest: HDMs demethylate histones; NR1H3 & NR1H2 regulate gene expression linked to cholesterol transport and efflux; NR1H2 and NR1H3-mediated signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O75164](https://www.uniprot.org/uniprotkb/O75164) (Lysine-specific demethylase 4A):

> Histone demethylase that specifically demethylates 'Lys-9' and 'Lys-36' residues of histone H3, thereby acting as a key regulator of nascent transcription. Does not demethylate histone H3 'Lys-4', H3 'Lys-27' nor H4 'Lys-20'. Demethylates trimethylated H3 'Lys-9' and H3 'Lys-36' residue, while it has no activity on mono- and dimethylated residues. Also able to demethylate histone H1-4 methylated at 'Lys-26' (H1.4K26me1, H1.4K26me2 and H1.4K26me3). Participates in transcriptional repression of …

**Summary**, from NCBI Gene [9682](https://www.ncbi.nlm.nih.gov/gene/9682):

> This gene is a member of the Jumonji domain 2 (JMJD2) family and encodes a protein containing a JmjN domain, a JmjC domain, a JD2H domain, two TUDOR domains, and two PHD-type zinc fingers. This nuclear protein functions as a trimethylation-specific demethylase, converting specific trimethylated histone residues to the dimethylated form, and as a transcriptional repressor. [provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:22978](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22978) · Entrez [9682](https://www.ncbi.nlm.nih.gov/gene/9682) · UniProt [O75164](https://www.uniprot.org/uniprotkb/O75164) · Ensembl [ENSG00000066135](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066135)

## Data

Gene col 819: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 819); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 819, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 819]; `tensor/DDL_lfc|DDL_z.npy` [819]; `embed/gene_vectors.npy` [819]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 819 or target_col == 819). Every well: [[KDM4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KDM4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
