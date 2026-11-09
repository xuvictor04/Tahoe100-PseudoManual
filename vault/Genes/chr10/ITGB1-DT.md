---
symbol: "ITGB1-DT"
type: "gene"
col: 13713
ensembl_id: "ENSG00000229656"
name: "ITGB1 divergent transcript"
location: "10p11.22"
module: 116
arm: "+"
pooled_cpm: 54.35
n_lines_expressing: 29
n_dd_up: 22
n_dd_down: 40
n_dd_up_clean: 15
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 3
direction_downstream: 21
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# ITGB1-DT

*ITGB1 divergent transcript* — 10p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.44× (z +11.7, q 5e-29, up in 19 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.352× (z -13.7, q 3e-40, down in 25 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADTRP]] (+0.75, fdr 7e-06), [[NAV3]] (+0.71, fdr 7e-06), [[ITGA2-AS1]] (+0.69, fdr 7e-06); moves opposite to [[SSBP2]] (-0.57, fdr 1e-05), [[PPP1R12B]] (-0.54, fdr 2e-05), [[MLLT10]] (-0.53, fdr 3e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 21 go from it, the strongest it → [[ELK3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13713.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.44×** | +11.7 | 5e-29 | 19/26 (HOP62, AsPC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +10.8 | 2e-24 | 10/25 (MIA PaCa-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +10.2 | 3e-22 | 12/25 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +9.6 | 1e-19 | 7/27 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +9.4 | 5e-19 | 12/27 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.94×** | +8.8 | 2e-16 | 21/27 (HepG2/C3A, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.79×** | +7.4 | 1e-11 | 19/26 (RPMI-7951, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +6.9 | 3e-10 | 12/27 (AsPC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.40×** | +6.3 | 2e-08 | 14/27 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.58×** | +6.0 | 1e-07 | 18/26 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.49×** | +5.2 | 8e-06 | 9/26 (SK-MEL-2, NCI-H2347, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.46×** | +5.0 | 3e-05 | 13/26 (SNU-423, SK-MEL-2, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **2.02×** | +4.9 | 5e-05 | 17/27 (AsPC-1, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.6 | 2e-04 | 12/27 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +4.4 | 4e-04 | 13/27 (NCI-H460, SNU-423, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.006 | 7/27 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.008 | 9/26 (NCI-H460, SNU-423, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.030 | 8/26 (AsPC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.25×** | +2.9 | 0.095 | 6/27 (NCI-H1573, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13713.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.352×** | -13.7 | 3e-40 | 25/27 (RKO, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.366×** | -13.2 | 2e-37 | 25/26 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.397×** | -12.2 | 1e-31 | 24/27 (RKO, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.612×** | -6.2 | 7e-08 | 21/26 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.628×** | -5.9 | 5e-07 | 17/26 (NCI-H23, RKO, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.718×** | -5.5 | 3e-06 | 17/27 (NCI-H23, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.647×** | -5.5 | 3e-06 | 18/26 (NCI-H23, J82, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.661×** | -5.4 | 4e-06 | 18/27 (NCI-H23, RKO, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.708×** | -5.3 | 9e-06 | 18/27 (RKO, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.671×** | -5.2 | 9e-06 | 15/26 (SNU-423, A549, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.661×** | -5.0 | 2e-05 | 18/26 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.766×** | -4.9 | 4e-05 | 17/27 (A549, A498, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.679×** | -4.9 | 4e-05 | 16/26 (NCI-H23, RKO, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.690×** | -4.9 | 4e-05 | 16/27 (LOX-IMVI, A498, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.670×** | -4.9 | 4e-05 | 17/26 (NCI-H23, RKO, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.702×** | -4.6 | 1e-04 | 16/26 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13713. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 689 | 0 | 25 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0435× (z -30.2) |
| [[NCI-H23 (line)]] | alt | 115 | 0 | 23 (6 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.456× (z -21.2) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.0763× (z -20.1) |
| [[A549 (line)]] | wt | 246 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0739× (z -19.1) |
| [[AsPC-1 (line)]] | alt | 136 | 1 | 5 | [[Auranofin (drug)]] 5 µM 3.18× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.129× (z -16.0) |
| [[HEC-1-A (line)]] | alt | 61.7 | 0 | 6 | — | [[Belinostat (drug)]] 0.5 µM 0.134× (z -14.1) |
| [[HepG2_C3A (line)]] | wt | 147 | 3 (3 ⚠) | 3 | [[Daptomycin (drug)]] 5 µM 4.83× (z +9.9) ⚠ unreliable plate only | [[Panobinostat (drug)]] 5 µM 0.135× (z -12.5) |
| [[HOP62 (line)]] | alt | 19.9 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +13.1) | [[Adagrasib (drug)]] 0.05 µM 0.636× (z -10.0) ⚠ position not correctable · without an alert: [[Clobetasol propionate (drug)]] 5 µM 0.257× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 66.1 | 3 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 7.69× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.18× (z +10.1) | [[Adagrasib (drug)]] 0.05 µM 0.489× (z -15.0) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.249× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 51.1 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0772× (z -15.8) |
| [[A-427 (line)]] | wt | 103 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.160× (z -14.1) |
| [[J82 (line)]] | alt | 57.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.107× (z -14.9) |
| [[NCI-H2347 (line)]] | alt | 29.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 24.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.210× (z -12.4) |
| [[PANC-1 (line)]] | alt | 24.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.210× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 90.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 61.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.160× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 60.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0996× (z -14.5) |
| [[SNU-423 (line)]] | alt | 86.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -12.1) |
| [[A498 (line)]] | wt | 53.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -8.9) |
| [[HS-578T (line)]] | alt | 35.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 49.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +10.5) | — |
| [[SW48 (line)]] | wt | 30.5 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0924× (z -9.3) |
| [[A-172 (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.78 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.09 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.38 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.94 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.92 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.64 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.91 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.90 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.47 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 13.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13713), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADTRP]] | +0.75 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[NAV3]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[ITGA2-AS1]] | +0.69 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[MARCHF4]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[MIR31HG]] | +0.67 | +0.58 / +0.71 | both halves | 8e-06 |  |
| [[LINC00513]] | +0.66 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[CORO2B]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[TOMM34]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[BMAL2]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[LTBP2]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[NEK10]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[CDCP1]] | +0.63 | +0.62 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSBP2]] | -0.57 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[PPP1R12B]] | -0.54 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[MLLT10]] | -0.53 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[TSC22D3]] | -0.53 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[EFNA4]] | -0.52 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[EFNA3]] | -0.52 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[RCOR3]] | -0.51 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[MED25]] | -0.51 | -0.51 / -0.38 | both halves | 6e-05 |  |
| [[PLEKHH3]] | -0.50 | -0.44 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers ITGB1-DT's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.9% of all compounds | 0.079 | ⚠ off-target possible; 3 compounds |
| [[BCL2A1]] | C | BCL2A1 activity raises ITGB1-DT's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.25× lower at baseline in the lines without BCL2A1 | 0.017 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1; co-absent with the target |
| [[TMEM156]] | C | TMEM156 activity raises ITGB1-DT's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 2.05× lower at baseline in the lines without TMEM156 | 0.060 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 17, C 4. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELK3]] | B | ITGB1-DT activity raises ELK3's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 2.76× lower at baseline in the lines without ITGB1-DT | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[NABP1]] | B | ITGB1-DT activity raises NABP1's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 2.48× lower at baseline in the lines without ITGB1-DT | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[PPP1R12B]] | B | ITGB1-DT activity lowers PPP1R12B's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 1.20× higher at baseline in the lines without ITGB1-DT | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[BCAR3]] | B | ITGB1-DT activity raises BCAR3's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 2.45× lower at baseline in the lines without ITGB1-DT | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[LINC00513]] | B | ITGB1-DT activity raises LINC00513's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 1.20× lower at baseline in the lines without ITGB1-DT | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[CYTOR]] | B | ITGB1-DT activity raises CYTOR's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 1.63× lower at baseline in the lines without ITGB1-DT | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[MIR31HG]] | B | ITGB1-DT activity raises MIR31HG's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 2.28× lower at baseline in the lines without ITGB1-DT | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[FOSL1]] | B | ITGB1-DT activity raises FOSL1's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 1.92× lower at baseline in the lines without ITGB1-DT | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[ASB1]] | B | ITGB1-DT activity raises ASB1's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 1.37× lower at baseline in the lines without ITGB1-DT | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[LUCAT1]] | B | ITGB1-DT activity raises LUCAT1's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 2.58× lower at baseline in the lines without ITGB1-DT | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[CTSL]] | B | ITGB1-DT activity raises CTSL's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 3.03× lower at baseline in the lines without ITGB1-DT | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[TNFRSF12A]] | B | ITGB1-DT activity raises TNFRSF12A's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 1.36× lower at baseline in the lines without ITGB1-DT | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.802). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.1, 10.9); signed map (14.1, 44.3). **Vector** length 128, 41.6% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.2 | +11.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +9.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +9.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.6 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +4.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.2 | -5.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -4.1 | -6.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -4.0 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -5.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -5.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.4 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | ITGB1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10p11.22 — chr10:32,958,437-33,082,409 (+) |
| Ensembl biotype | lncRNA |
| Also known as | LincIN |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53718](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53718) · Entrez [101929475](https://www.ncbi.nlm.nih.gov/gene/101929475) · Ensembl [ENSG00000229656](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229656)

## Data

Gene col 13713: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13713); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13713, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13713]; `tensor/DDL_lfc|DDL_z.npy` [13713]; `embed/gene_vectors.npy` [13713]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13713 or target_col == 13713). Every well: [[ITGB1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGB1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
