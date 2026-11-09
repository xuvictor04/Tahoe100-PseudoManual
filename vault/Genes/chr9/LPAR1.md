---
symbol: "LPAR1"
type: "gene"
col: 12534
ensembl_id: "ENSG00000198121"
name: "lysophosphatidic acid receptor 1"
location: "9q31.3"
module: 104
arm: "+"
pooled_cpm: 33.52
n_lines_expressing: 35
n_dd_up: 0
n_dd_down: 39
n_dd_up_clean: 0
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 13
direction_downstream: 5
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# LPAR1

*lysophosphatidic acid receptor 1* — 9q31.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 14.8×; ⚠ cell-cycle shift, explains ~25% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 12.8×).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.266× (z -26.7, q 0e+00, down in 27 of 33 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.210× (z -22.2, q 0e+00, down in 30 of 33 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSD11B1]] (+0.66, fdr 7e-06), [[IRAK3]] (+0.62, fdr 1e-05), [[PID1]] (+0.60, fdr 1e-05); moves opposite to [[VIM]] (-0.48, fdr 1e-04), [[TNFRSF9]] (-0.42, fdr 5e-05), [[UCHL1]] (-0.42, fdr 1e-04).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[CCBE1]] → it (grade B ⚠); 5 go from it, the strongest it → [[CCBE1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12534.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 14.8×; ⚠ cell-cycle shift, explains ~25% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 12.8×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.27× | +3.4 | 0.23 | 11/33 (RPMI-7951, HS-578T, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.27× | +3.3 | 0.23 | 13/33 (HOP62, RPMI-7951, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 1.26× | +3.2 | 0.23 | 11/33 (RPMI-7951, HS-578T, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.26× | +3.0 | 0.34 | 10/32 (RPMI-7951, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 18 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12534.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.266×** | -26.7 | 0e+00 | 27/33 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.210×** | -22.2 | 0e+00 | 30/33 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.224×** | -21.3 | 0e+00 | 28/33 (Hs 766T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.293×** | -17.5 | 0e+00 | 29/33 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.366×** | -13.8 | 5e-41 | 27/33 (A549, NCI-H1573, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.427×** | -12.1 | 6e-32 | 21/29 (NCI-H1792, A498, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.436×** | -11.8 | 2e-30 | 24/33 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.414×** | -11.6 | 2e-29 | 19/23 (NCI-H2030, J82, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.474×** | -10.6 | 1e-24 | 25/33 (COLO 205, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.490×** | -9.8 | 8e-21 | 24/29 (SW 900, SW48, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.516×** | -9.4 | 2e-19 | 26/33 (COLO 205, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.556×** | -8.4 | 2e-15 | 22/33 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.569×** | -8.0 | 4e-14 | 24/33 (RPMI-7951, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.583×** | -7.7 | 6e-13 | 23/33 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.602×** | -7.0 | 1e-10 | 21/29 (NCI-H2030, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.623×** | -6.7 | 6e-10 | 21/33 (SW 900, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.629×** | -6.6 | 1e-09 | 20/33 (CFPAC-1, hTERT-HPNE, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.441×** | -6.1 | 3e-08 | 20/32 (RPMI-7951, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.669×** | -5.7 | 3e-07 | 18/33 (HOP62, A549, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.703×** | -5.0 | 1e-05 | 14/33 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.711×** | -4.9 | 3e-05 | 18/33 (SNU-423, SW 900, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.737×** | -4.3 | 3e-04 | 15/32 (H4, SNU-423, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.737×** | -4.1 | 8e-04 | 15/33 (NCI-H2030, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12534. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 48.6 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -21.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0789× (z -20.5) |
| [[NCI-H2030 (line)]] | alt | 91.5 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0826× (z -31.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.162× (z -16.2) |
| [[NCI-H1792 (line)]] | alt | 150 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0677× (z -29.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0478× (z -23.4) |
| [[SW 900 (line)]] | alt | 92.0 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -20.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.130× (z -15.7) |
| [[SNU-423 (line)]] | alt | 88.8 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0811× (z -19.3) |
| [[A549 (line)]] | wt | 77.0 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0719× (z -27.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0806× (z -18.4) |
| [[HOP62 (line)]] | alt | 23.9 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -16.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.163× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 42.0 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0423× (z -30.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.119× (z -14.4) |
| [[Panc 03.27 (line)]] | alt | 47.4 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -17.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.141× (z -16.4) |
| [[RPMI-7951 (line)]] | alt | 117 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -16.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.127× (z -14.6) |
| [[COLO 205 (line)]] | alt | 49.9 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0280× (z -22.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.103× (z -14.3) |
| [[NCI-H2347 (line)]] | alt | 56.9 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -17.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.159× (z -15.0) |
| [[LoVo (line)]] | wt | 19.6 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0916× (z -23.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.210× (z -10.6) |
| [[A-427 (line)]] | wt | 30.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -17.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.259× (z -10.4) |
| [[Hs 766T (line)]] | wt | 157 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0608× (z -20.5) |
| [[HS-578T (line)]] | alt | 48.1 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 10.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0856× (z -14.1) |
| [[A-172 (line)]] | wt | 14.2 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +20.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 12.8× (z +13.9) | [[Belinostat (drug)]] 5 µM 0.189× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 58.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -13.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.197× (z -13.0) |
| [[hTERT-HPNE (line)]] | wt | 93.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -14.4) |
| [[J82 (line)]] | alt | 46.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -16.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.328× (z -8.5) |
| [[LS 180 (line)]] | wt | 9.55 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -11.1) |
| [[PANC-1 (line)]] | alt | 14.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -15.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW48 (line)]] | wt | 16.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -10.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0819× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[AN3 CA (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 5.64 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.83 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.11 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.28 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12534), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSD11B1]] | +0.66 | +0.64 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[IRAK3]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[PID1]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[LINC02015]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[DCN]] | +0.56 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[HS3ST3B1]] | +0.56 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[CD38]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[GAB3]] | +0.52 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[TBXAS1]] | +0.51 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[DNER]] | +0.50 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[ITGA10]] | +0.48 | +0.34 / +0.49 | both halves | 1e-04 |  |
| [[SLCO2A1]] | +0.47 | +0.46 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VIM]] | -0.48 | -0.32 / -0.43 | both halves | 1e-04 |  |
| [[TNFRSF9]] | -0.42 | -0.47 / -0.40 | both halves | 5e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[UCHL1]] | -0.42 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[CREB5]] | -0.40 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[JUN]] | -0.37 | -0.31 / -0.38 | both halves | 2e-04 | STRING 454 |
| [[LINC02509]] | -0.37 | -0.34 / -0.35 | both halves | 1e-04 |  |
| [[CD151]] | -0.37 | -0.14 / -0.37 | ⚠ not reproduced | 0.002 |  |
| [[LINC01748]] | -0.37 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[BAMBI]] | -0.37 | -0.28 / -0.35 | both halves | 3e-04 |  |
| [[SSBP3]] | -0.36 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[KLF2]] | -0.36 | -0.24 / -0.39 | both halves | 5e-04 |  |
| [[NIHCOLE]] | -0.35 | -0.27 / -0.35 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 9, C 4. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCBE1]] | B | CCBE1 activity raises LPAR1's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 5.37× lower at baseline in the lines without CCBE1 | 0.002 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[LOX]] | B | LOX activity raises LPAR1's level | lines that do not express LOX (31) vs lines expressing it (19) | 3.96× lower at baseline in the lines without LOX | 0.010 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[TREM1]] | B | TREM1 activity raises LPAR1's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 3.77× lower at baseline in the lines without TREM1 | 0.033 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[BICC1]] | B | BICC1 activity raises LPAR1's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 3.51× lower at baseline in the lines without BICC1 | 0.045 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[PTGFR]] | B | PTGFR activity raises LPAR1's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 3.45× lower at baseline in the lines without PTGFR | 0.060 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX |
| [[RHCG]] | B | RHCG activity raises LPAR1's level | lines that do not express RHCG (33) vs lines expressing it (17) | 3.67× lower at baseline in the lines without RHCG | 0.086 | ⚠ within organs, on part of the lines; also absent: RSPO3, CRLF2, ANXA10 |
| [[HTRA3]] | B | HTRA3 activity raises LPAR1's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 3.30× lower at baseline in the lines without HTRA3 | 0.089 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[HIPK2]] | B | HIPK2 activity raises LPAR1's level | lines that do not express HIPK2 (5) vs lines expressing it (45) | 2.25× lower at baseline in the lines without HIPK2 | 0.094 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| [[ABLIM3]] | B | ABLIM3 activity raises LPAR1's level | lines that do not express ABLIM3 (15) vs lines expressing it (35) | 2.90× lower at baseline in the lines without ABLIM3 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |
| [[TLR2]] | C | TLR2 activity raises LPAR1's level | lines that do not express TLR2 (26) vs lines expressing it (24) | 4.58× lower at baseline in the lines without TLR2 | 0.002 | ⚠ within organs, on part of the lines; also absent: FYB1, DDIT4L, EDNRA; co-absent with the target |
| [[SVEP1]] | C | SVEP1 activity raises LPAR1's level | lines that do not express SVEP1 (15) vs lines expressing it (35) | 4.91× lower at baseline in the lines without SVEP1 | 0.032 | ⚠ within organs, on part of the lines; also absent: LPAR1, CDH8, ENSG00000253100; maybe low, not absent; co-absent with the target |
| [[PAPSS2]] | C | PAPSS2 activity raises LPAR1's level | lines that do not express PAPSS2 (15) vs lines expressing it (35) | 5.02× lower at baseline in the lines without PAPSS2 | 0.042 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, A4GALT, NT5E; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCBE1]] | B | LPAR1 activity raises CCBE1's level | lines that do not express LPAR1 (15) vs lines expressing it (35) | 4.12× lower at baseline in the lines without LPAR1 | 0.073 | ⚠ within organs, on part of the lines; also absent: SVEP1, PAPSS2, TOX2 |
| [[LOX]] | B | LPAR1 activity raises LOX's level | lines that do not express LPAR1 (15) vs lines expressing it (35) | 4.83× lower at baseline in the lines without LPAR1 | 0.078 | ⚠ within organs, on part of the lines; also absent: SVEP1, PAPSS2, TOX2 |
| [[TREM1]] | B | LPAR1 activity raises TREM1's level | lines that do not express LPAR1 (15) vs lines expressing it (35) | 2.17× lower at baseline in the lines without LPAR1 | 0.094 | ⚠ within organs, on part of the lines; also absent: SVEP1, PAPSS2, TOX2 |
| [[SVEP1]] | C | LPAR1 activity raises SVEP1's level | lines that do not express LPAR1 (15) vs lines expressing it (35) | 2.20× lower at baseline in the lines without LPAR1 | 0.056 | ⚠ within organs, on part of the lines; also absent: SVEP1, PAPSS2, TOX2; co-absent with the target |
| [[TLR2]] | C | LPAR1 activity raises TLR2's level | lines that do not express LPAR1 (15) vs lines expressing it (35) | 2.60× lower at baseline in the lines without LPAR1 | 0.066 | ⚠ within organs, on part of the lines; also absent: SVEP1, PAPSS2, TOX2; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.608). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.2, 16.7); signed map (18.6, 33.0). **Vector** length 98.4, 26.5% of its response variance represented; |z| ≥ 3 in 1,126 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.4 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.5 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | -3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | +3.3 | -6.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.1 | +1.5 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.9 | +1.9 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.8 | +1.4 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -5.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -4.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -6.6 |

## What is on record

|  |  |
|---|---|
| Name | lysophosphatidic acid receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.3 — chr9:110,873,263-111,038,470 (-) |
| Ensembl biotype | protein_coding |
| Also known as | edg-2, rec.1.3, vzg-1, Gpcr26, Mrec1.3, LPA1; previously EDG2 |
| Gene groups (HGNC) | Lysophosphatidic acid receptors |
| Hallmark sets | INFLAMMATORY_RESPONSE, UV_RESPONSE_DN |
| Reactome | 7 pathways, smallest: Lysosphingolipid and LPA receptors; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92633](https://www.uniprot.org/uniprotkb/Q92633) (Lysophosphatidic acid receptor 1):

> Receptor for lysophosphatidic acid (LPA). Plays a role in the reorganization of the actin cytoskeleton, cell migration, differentiation and proliferation, and thereby contributes to the responses to tissue damage and infectious agents. Activates downstream signaling cascades via the G(i)/G(o), G(12)/G(13), and G(q) families of heteromeric G proteins. Signaling inhibits adenylyl cyclase activity and decreases cellular cAMP levels. Signaling triggers an increase of cytoplasmic Ca(2+) levels. …

**Summary**, from NCBI Gene [1902](https://www.ncbi.nlm.nih.gov/gene/1902):

> The integral membrane protein encoded by this gene is a lysophosphatidic acid (LPA) receptor from a group known as EDG receptors. These receptors are members of the G protein-coupled receptor superfamily. Utilized by LPA for cell signaling, EDG receptors mediate diverse biologic functions, including proliferation, platelet aggregation, smooth muscle contraction, inhibition of neuroblastoma cell differentiation, chemotaxis, and tumor cell invasion. Many transcript variants encoding a few …

**Accessions** — [HGNC:3166](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3166) · Entrez [1902](https://www.ncbi.nlm.nih.gov/gene/1902) · UniProt [Q92633](https://www.uniprot.org/uniprotkb/Q92633) · Ensembl [ENSG00000198121](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198121)

## Data

Gene col 12534: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12534); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12534, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12534]; `tensor/DDL_lfc|DDL_z.npy` [12534]; `embed/gene_vectors.npy` [12534]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12534 or target_col == 12534). Every well: [[LPAR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LPAR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
