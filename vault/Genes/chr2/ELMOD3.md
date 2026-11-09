---
symbol: "ELMOD3"
type: "gene"
col: 3678
ensembl_id: "ENSG00000115459"
name: "ELMO domain containing 3"
location: "2p11.2"
module: 89
arm: "+"
pooled_cpm: 24.17
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# ELMOD3

*ELMO domain containing 3* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.78× (z +12.2, q 2e-31, up in 34 of 43 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.37× (z +7.0, q 5e-10, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.561× (z -17.9, q 0e+00, down in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.628× (z -10.2, q 4e-22, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A17]] (+0.69, fdr 7e-06), [[TRAPPC13]] (+0.67, fdr 7e-06), [[APTX]] (+0.66, fdr 1e-05); moves opposite to [[NAB1]] (-0.58, fdr 7e-06), [[CSRP1]] (-0.58, fdr 1e-05), [[YWHAZ]] (-0.58, fdr 1e-05).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EPHB1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3678.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +12.2 | 2e-31 | 34/43 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.44×** | +7.5 | 1e-11 | 26/48 (PANC-1, HOP62, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +7.0 | 5e-10 | 22/48 (A498, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.31×** | +5.9 | 5e-07 | 22/47 (HOP62, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +5.4 | 7e-06 | 19/47 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +5.4 | 8e-06 | 19/48 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +5.0 | 4e-05 | 17/48 (BT-474, LS 180, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.22×** | +4.4 | 8e-04 | 14/47 (SW1417, BT-474, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.19× | +3.9 | 0.007 | 7/47 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +3.7 | 0.010 | 10/48 (SW1417, HT-29, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.12× | +3.5 | 0.025 | 7/48 (SW480, C32, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.17× | +3.3 | 0.045 | 7/47 (BT-474, A-427, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.15× | +3.2 | 0.063 | 4/48 (SK-MEL-2, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.15× | +3.1 | 0.077 | 3/47 (RKO, C32, …) | top dose only |  |
| [[Neratinib (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.077 | 7/47 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.077 | 5/48 (SW480, C-33 A, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.11× | +3.0 | 0.079 | 5/48 (SW480, RPMI-7951, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.080 | 7/47 (A549, AsPC-1, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.080 | 5/48 (SW1417, NCI-H2030, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.14× | +2.9 | 0.084 | 13/46 (hTERT-HPNE, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.10× | +2.9 | 0.084 | 1/48 (SNU-1) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3678.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.561×** | -17.9 | 0e+00 | 36/47 (NCI-H460, NCI-H1792, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.588×** | -11.6 | 8e-29 | 27/43 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.628×** | -10.2 | 4e-22 | 27/47 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.644×** | -9.6 | 9e-20 | 33/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.639×** | -9.4 | 5e-19 | 28/48 (LOX-IMVI, NCI-H460, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.772×** | -8.0 | 1e-13 | 26/48 (NCI-H460, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.703×** | -7.7 | 1e-12 | 27/48 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.551×** | -6.8 | 6e-10 | 22/48 (SNU-423, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.759×** | -6.0 | 1e-07 | 22/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.600×** | -5.8 | 3e-07 | 20/47 (C32, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.782×** | -5.2 | 1e-05 | 23/47 (SK-MEL-2, H4, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.792×** | -5.1 | 2e-05 | 24/48 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.785×** | -5.1 | 2e-05 | 16/34 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.851× | -3.5 | 0.018 | 16/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | 0.841× | -3.5 | 0.019 | 12/41 (NCI-H1792, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3678. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 36.2 | 0 | 15 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -22.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -16.7) |
| [[HOP62 (line)]] | alt | 24.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -12.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.343× (z -9.5) |
| [[H4 (line)]] | wt | 25.0 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.145× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[NCI-H1792 (line)]] | alt | 40.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -18.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 23.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[A-172 (line)]] | wt | 35.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -13.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.411× (z -8.6) |
| [[A549 (line)]] | wt | 26.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -12.6) ⚠ cell-cycle shift, explains ~31% of this change |
| [[AN3 CA (line)]] | alt | 26.4 | 0 | 2 | — | [[Malotilate (drug)]] 0.5 µM 0.0867× (z -9.5) |
| [[C32 (line)]] | wt | 21.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[KATO III (line)]] | alt | 22.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.76× (z +9.9) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LOX-IMVI (line)]] | wt | 29.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 9.85 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -11.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.196× (z -9.9) ⚠ toxic; unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -12.7) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HEC-1-A (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[HT-29 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -8.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[hTERT-HPNE (line)]] | wt | 24.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -10.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 34.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[NCI-H2030 (line)]] | alt | 37.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.289× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.401× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[RKO (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0951× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -10.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SHP-77 (line)]] | alt | 14.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.186× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.206× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~39% of this change |
| [[SW1417 (line)]] | alt | 22.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.307× (z -9.0) |
| [[SW48 (line)]] | wt | 23.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3678), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A17]] | +0.69 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[TRAPPC13]] | +0.67 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[APTX]] | +0.66 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[VPS45]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[COA6]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[PPP2R2D]] | +0.65 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[TEFM]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[C8orf76]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[GUCA1B]] | +0.62 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[RWDD3]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[MAFIP]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[ZCCHC10]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAB1]] | -0.58 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[CSRP1]] | -0.58 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[YWHAZ]] | -0.58 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[JUNB]] | -0.58 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[EPB41L2]] | -0.58 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[EGR2]] | -0.57 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[ACTB]] | -0.57 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[EGR3]] | -0.57 | -0.68 / -0.42 | both halves | 4e-05 |  |
| [[COTL1]] | -0.56 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[VCL]] | -0.55 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[MYH9]] | -0.53 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[PLEC]] | -0.53 | -0.53 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPHB1]] | B | EPHB1 activity raises ELMOD3's level | lines that do not express EPHB1 (16) vs lines expressing it (34) | 1.35× lower at baseline in the lines without EPHB1 | 0.035 | ⚠ within organs, on part of the lines; also absent: KCNG1, DOCK2, GLIS1; maybe low, not absent |
| [[EPB41L2]] | B | EPB41L2 activity raises ELMOD3's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without EPB41L2 | 0.081 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.8, 21.1); signed map (0.2, -3.2). **Vector** length 99.9, 22.6% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +8.7 | +12.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | +6.5 | +7.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +6.1 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.5 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +7.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +5.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.9 | +2.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.9 | +2.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.6 | -8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.2 | -17.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -4.3 | -9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -4.3 | -11.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -3.2 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.5 | -0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.5 | -2.6 |
|  | [[Pimozide (drug)]] 5 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ELMO domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:85,354,394-85,391,752 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21977; previously RBM29, RBED1, DFNB88 |
| Gene groups (HGNC) | RNA binding motif containing; ELMO domain containing |
| Hallmark sets | ADIPOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FG2](https://www.uniprot.org/uniprotkb/Q96FG2) (ELMO domain-containing protein 3):

> Acts as a GTPase-activating protein (GAP) for ARL2 with low specific activity.

**Summary**, from NCBI Gene [84173](https://www.ncbi.nlm.nih.gov/gene/84173):

> This gene encodes a member of the engulfment and cell motility family of GTPase-activating proteins that regulate Arf GTPase proteins. Members of this family are defined by a conserved engulfment and cell motility domain. In rat cochlea, the encoded protein is found in stereocilia, kinocilia and cuticular plate of developing hair cells suggesting a function for this protein in cochlear sensory cells. An allelic variant of this family has been associated with autosomal recessive nonsyndromic …

**Accessions** — [HGNC:26158](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26158) · Entrez [84173](https://www.ncbi.nlm.nih.gov/gene/84173) · UniProt [Q96FG2](https://www.uniprot.org/uniprotkb/Q96FG2) · Ensembl [ENSG00000115459](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115459)

## Data

Gene col 3678: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3678); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3678, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3678]; `tensor/DDL_lfc|DDL_z.npy` [3678]; `embed/gene_vectors.npy` [3678]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3678 or target_col == 3678). Every well: [[ELMOD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELMOD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
