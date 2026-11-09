---
symbol: "WASHC5"
type: "gene"
col: 9043
ensembl_id: "ENSG00000164961"
name: "WASH complex subunit 5"
location: "8q24.13"
module: 122
arm: "+"
pooled_cpm: 69.06
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# WASHC5

*WASH complex subunit 5* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.46× (z +7.9, q 1e-12, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.691× (z -10.7, q 9e-24, down in 35 of 49 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COMMD9]] (+0.64, fdr 7e-06), [[VPS11]] (+0.61, fdr 7e-06), [[VPS41]] (+0.60, fdr 9e-06); moves opposite to [[LINC00862]] (-0.52, fdr 3e-05), [[SIX4]] (-0.48, fdr 1e-04), [[CLOCK]] (-0.48, fdr 8e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9043.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.46×** | +7.9 | 1e-12 | 39/48 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +7.4 | 4e-11 | 37/48 (NCI-H2030, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +6.6 | 8e-09 | 34/48 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +6.1 | 2e-07 | 31/48 (PANC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.22×** | +5.7 | 2e-06 | 27/48 (HT-29, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.27×** | +5.0 | 5e-05 | 24/48 (LS 180, LOX-IMVI, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +4.6 | 3e-04 | 22/48 (A498, J82, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.21×** | +4.0 | 0.004 | 20/48 (HS-578T, HT-29, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.005 | 21/48 (LS 180, SW48, …) | rises with dose |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.5 | 0.023 | 13/48 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.67×** | +3.5 | 0.027 | 17/49 (A498, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.12× | +3.3 | 0.045 | 7/48 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | 1.18× | +3.3 | 0.049 | 20/47 (NCI-H2030, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.078 | 18/41 (A-427, LS 180, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.0 | 0.085 | 19/48 (NCI-H1573, NCI-H460, …) | top dose only | composition shift |
| [[Rapamycin (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.085 | 10/49 (NCI-H1573, A549, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9043.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.691×** | -10.7 | 9e-24 | 35/49 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.644×** | -9.3 | 6e-18 | 31/48 (SNU-423, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -7.2 | 1e-10 | 35/48 (A549, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.715×** | -6.8 | 2e-09 | 32/47 (C-33 A, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.737×** | -6.2 | 7e-08 | 28/48 (A549, C32, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.769×** | -5.3 | 9e-06 | 27/50 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.795×** | -4.7 | 3e-04 | 27/48 (SNU-423, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.805×** | -4.6 | 4e-04 | 26/48 (C32, HEC-1-A, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.829×** | -4.0 | 0.005 | 21/49 (CHP-212, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.880× | -3.7 | 0.015 | 18/48 (HS-578T, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~79% of this change | 0.857× | -3.3 | 0.059 | 20/47 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **0.812×** | -3.1 | 0.080 | 9/49 (PANC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.854× | -3.1 | 0.087 | 17/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9043. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 63.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.289× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 70.3 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 44.9 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +14.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-172 (line)]] | wt | 56.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -11.3) |
| [[A549 (line)]] | wt | 77.4 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.249× (z -14.5) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.295× (z -13.2) |
| [[HS-578T (line)]] | alt | 86.6 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 69.3 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -13.8) |
| [[HOP62 (line)]] | alt | 55.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -10.9) |
| [[Hs 766T (line)]] | wt | 119 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 68.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.02× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 107 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -14.2) |
| [[SNU-423 (line)]] | alt | 66.1 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.229× (z -15.3) |
| [[A-427 (line)]] | wt | 42.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.94× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 81.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.625× (z -8.8) |
| [[AN3 CA (line)]] | alt | 95.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -12.6) ⚠ cell-cycle shift, explains ~65% of this change |
| [[COLO 205 (line)]] | alt | 101 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HEC-1-A (line)]] | alt | 51.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.569× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 161 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.439× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 46.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -10.7) |
| [[J82 (line)]] | alt | 74.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +12.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 69.7 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LOX-IMVI (line)]] | wt | 90.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 58.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 83.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.379× (z -10.8) |
| [[RKO (line)]] | wt | 111 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -8.7) |
| [[SHP-77 (line)]] | alt | 83.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 61.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.383× (z -13.5) |
| [[BT-474 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 64.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 58.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9043), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD9]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[VPS11]] | +0.61 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[VPS41]] | +0.60 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[CLN3]] | +0.59 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[VPS50]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[NAGPA]] | +0.58 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[CEP162]] | +0.58 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[GNPTG]] | +0.56 | +0.60 / +0.39 | both halves | 6e-05 |  |
| [[GLMP]] | +0.53 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[SPNS1]] | +0.52 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[HSPBP1]] | +0.52 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[PLBD2]] | +0.52 | +0.44 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00862]] | -0.52 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[SIX4]] | -0.48 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[CLOCK]] | -0.48 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[TSBP1-AS1]] | -0.46 | -0.29 / -0.46 | both halves | 3e-04 |  |
| [[CHST7]] | -0.45 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[SMIM14]] | -0.42 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[LINC02362]] | -0.42 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[SPESP1]] | -0.42 | -0.30 / -0.32 | both halves | 2e-04 |  |
| [[PYCR2]] | -0.42 | -0.42 / -0.25 | both halves | 4e-04 |  |
| [[NFKBID]] | -0.41 | -0.37 / -0.33 | both halves | 1e-04 |  |
| [[ZBED5]] | -0.41 | -0.23 / -0.47 | both halves | 5e-04 |  |
| [[LINC01301]] | -0.41 | -0.17 / -0.47 | ⚠ not reproduced | 0.001 |  |
| [[ZNF425]] | -0.41 | -0.32 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises WASHC5's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity lowers WASHC5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.640). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-19.2, 13.3); signed map (-10.8, -20.0). **Vector** length 112, 28.8% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.9 | +5.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +4.6 | +5.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +3.9 |
|  | [[EX229 (drug)]] 5 µM |  | +4.2 | +2.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +0.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -10.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.4 | -7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.3 | -9.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -4.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.3 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | WASH complex subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:125,024,260-125,091,819 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SPG8, KIAA0196 |
| Gene groups (HGNC) | WASH complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12768](https://www.uniprot.org/uniprotkb/Q12768) (WASH complex subunit 5):

> Acts as a component of the WASH core complex that functions as a nucleation-promoting factor (NPF) at the surface of endosomes, where it recruits and activates the Arp2/3 complex to induce actin polymerization, playing a key role in the fission of tubules that serve as transport intermediates during endosome sorting. May be involved in axonal outgrowth. Involved in cellular localization of ADRB2. Involved in cellular trafficking of BLOC-1 complex cargos such as ATP7A and VAMP7.

**Summary**, from NCBI Gene [9897](https://www.ncbi.nlm.nih.gov/gene/9897):

> This gene encodes a 134 kDa protein named strumpellin that is predicted to have multiple transmembrane domains and a spectrin-repeat-containing domain. This ubiquitously expressed gene has its highest expression in skeletal muscle. The protein is named for Strumpell disease; a form of hereditary spastic paraplegia (HSP). Spastic paraplegias are a diverse group of disorders in which the autosomal dominant forms are characterized by progressive, lower extremity spasticity caused by axonal …

**Accessions** — [HGNC:28984](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28984) · Entrez [9897](https://www.ncbi.nlm.nih.gov/gene/9897) · UniProt [Q12768](https://www.uniprot.org/uniprotkb/Q12768) · Ensembl [ENSG00000164961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164961)

## Data

Gene col 9043: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9043); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9043, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9043]; `tensor/DDL_lfc|DDL_z.npy` [9043]; `embed/gene_vectors.npy` [9043]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9043 or target_col == 9043). Every well: [[WASHC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WASHC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
