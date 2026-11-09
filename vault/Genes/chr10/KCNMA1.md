---
symbol: "KCNMA1"
type: "gene"
col: 7949
ensembl_id: "ENSG00000156113"
name: "potassium calcium-activated channel subfamily M alpha 1"
location: "10q22.3"
module: 13
arm: "+"
pooled_cpm: 433.25
n_lines_expressing: 24
n_dd_up: 14
n_dd_down: 28
n_dd_up_clean: 10
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 30
direction_downstream: 93
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# KCNMA1

*potassium calcium-activated channel subfamily M alpha 1* — 10q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Verteporfin (drug)]] 5 µM: 1.41× (z +6.4, q 1e-07, up in 1 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.372× (z -19.1, q 0e+00, down in 22 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AFF3]] (+0.69, fdr 7e-06), [[VEGFC]] (+0.63, fdr 7e-06), [[MEG3]] (+0.63, fdr 1e-05); moves opposite to [[FGD4]] (-0.59, fdr 1e-05), [[CCND3]] (-0.54, fdr 1e-05), [[CAVIN2]] (-0.51, fdr 1e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[ADGRG2]] → it (grade B ⚠); 93 go from it, the strongest it → [[MSANTD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7949.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **1.41×** | +6.4 | 1e-07 | 1/23 (NCI-H460) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +6.1 | 4e-07 | 1/23 (NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **1.21×** | +5.3 | 2e-05 | 10/23 (NCI-H1792, Hs 766T, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +5.3 | 2e-05 | 6/22 (Hs 766T, NCI-H1792, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.41×** | +4.8 | 2e-04 | 0/22 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.41×** | +4.7 | 2e-04 | 4/22 (CHP-212, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.58×** | +4.6 | 3e-04 | 17/22 (Hs 766T, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.6 | 3e-04 | 17/22 (A498, SNU-423, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.17× | +4.4 | 7e-04 | 4/23 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.25×** | +4.3 | 8e-04 | 0/23 | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.24×** | +4.1 | 0.002 | 10/22 (NCI-H1792, Hs 766T, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.15× | +3.8 | 0.007 | 14/22 (PANC-1, SNU-423, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.007 | 6/22 (SNU-423, SW 1271, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.007 | 4/23 (SW 1271, A549, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.21×** | +3.5 | 0.017 | 3/22 (A498, H4, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.035 | 4/22 (CHP-212, A549, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.18× | +3.2 | 0.035 | 17/21 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.053 | 6/23 (NCI-H2030, A549, …) | top dose only | plate-row cell shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.060 | 12/21 (H4, NCI-H460, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7949.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.372×** | -19.1 | 0e+00 | 22/22 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.415×** | -16.9 | 0e+00 | 22/22 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.427×** | -16.4 | 0e+00 | 22/22 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **0.609×** | -13.5 | 3e-39 | 22/22 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.588×** | -10.2 | 2e-22 | 22/22 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.577×** | -10.2 | 3e-22 | 19/22 (RPMI-7951, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.631×** | -8.9 | 6e-17 | 21/22 (HS-578T, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Clobetasol propionate (drug)]] 5 µM | ⚠ position correction uncertain | **0.667×** | -7.8 | 5e-13 | 18/22 (A549, HOP62, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.678×** | -7.2 | 5e-11 | 21/21 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.777×** | -6.8 | 4e-10 | 14/22 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.702×** | -6.8 | 5e-10 | 13/22 (A549, NCI-H1573, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.510×** | -6.8 | 6e-10 | 22/23 (PANC-1, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.705×** | -6.7 | 8e-10 | 18/22 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.706×** | -6.7 | 9e-10 | 17/22 (A549, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.693×** | -6.5 | 3e-09 | 5/22 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.713×** | -6.5 | 3e-09 | 15/22 (H4, A549, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.719×** | -6.3 | 8e-09 | 11/22 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.707×** | -6.2 | 2e-08 | 15/21 (A549, NCI-H1573, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7949. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 1,555 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -26.5) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.0914× (z -20.6) |
| [[A549 (line)]] | wt | 404 | 0 | 15 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -21.3) |
| [[RPMI-7951 (line)]] | alt | 910 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -22.8) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.101× (z -20.0) |
| [[NCI-H1573 (line)]] | alt | 549 | 4 (3 ⚠) | 10 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 5.40× (z +12.8) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.47× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.248× (z -10.6) |
| [[PANC-1 (line)]] | alt | 1,806 | 0 | 13 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0617× (z -30.0) |
| [[NCI-H23 (line)]] | alt | 439 | 0 | 12 (5 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.561× (z -18.8) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.217× (z -14.1) |
| [[SNU-423 (line)]] | alt | 1,010 | 0 | 12 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0850× (z -21.4) |
| [[HS-578T (line)]] | alt | 1,169 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0785× (z -27.7) |
| [[A-172 (line)]] | wt | 1,493 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0692× (z -20.8) |
| [[A498 (line)]] | wt | 1,000 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.114× (z -20.8) |
| [[H4 (line)]] | wt | 909 | 2 (1 ⚠) | 7 (3 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.85× (z +10.3) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.34× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.0842× (z -19.5) |
| [[MIA PaCa-2 (line)]] | alt | 482 | 0 | 9 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0841× (z -21.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.0931× (z -21.1) |
| [[NCI-H1792 (line)]] | alt | 506 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -24.9) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.247× (z -13.0) |
| [[hTERT-HPNE (line)]] | wt | 903 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -18.3) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.120× (z -16.3) |
| [[Hs 766T (line)]] | wt | 666 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.123× (z -16.6) |
| [[LOX-IMVI (line)]] | wt | 500 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -15.7) |
| [[NCI-H460 (line)]] | wt | 131 | 2 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 3.20× (z +11.9) ⚠ position correction uncertain | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -18.9) ⚠ position correction uncertain · without an alert: [[Belinostat (drug)]] 5 µM 0.299× (z -12.2) |
| [[SW 1088 (line)]] | alt | 942 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0923× (z -13.6) |
| [[SW 900 (line)]] | alt | 545 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -17.5) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.199× (z -12.8) |
| [[SW 1271 (line)]] | alt | 443 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.202× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 302 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -19.6) ⚠ position correction uncertain · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.331× (z -9.8) |
| [[NCI-H596 (line)]] | alt | 335 | 0 | 3 (2 ⚠) | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.350× (z -11.5) |
| [[CHP-212 (line)]] | wt | 225 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.236× (z -8.6) ⚠ toxic |
| [[A-427 (line)]] | wt | 20.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 55.4 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 32.6 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 79.9 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 38.8 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 40.2 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 29.1 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 28.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 36.1 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 30.1 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 29.9 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 33.3 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 102 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 26.9 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 26.9 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 29.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.9 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 39.3 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 24.2 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 28.9 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 56.6 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 35.9 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 25.7 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 36.8 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 44.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7949), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AFF3]] | +0.69 | +0.59 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[VEGFC]] | +0.63 | +0.67 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[MEG3]] | +0.63 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[LINC01411]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[GJA1]] | +0.62 | +0.72 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[MIR493HG]] | +0.62 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[KIRREL3]] | +0.60 | +0.60 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[MEG8]] | +0.60 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[VSTM4]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[SPOCK1]] | +0.59 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[ADAMTS16]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[LOXL2]] | +0.58 | +0.61 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FGD4]] | -0.59 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[CCND3]] | -0.54 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[CAVIN2]] | -0.51 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[ADGRG2]] | -0.51 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[SRGN]] | -0.51 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[STOM]] | -0.48 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[EPS8]] | -0.48 | -0.52 / -0.49 | both halves | 1e-05 | pathway: Sensory Perception |
| [[SHROOM3]] | -0.48 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[RBMS2]] | -0.47 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[SLC7A2]] | -0.46 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[MAOA]] | -0.45 | -0.47 / -0.46 | both halves | 3e-05 | pathway: Neuronal System |
| [[SAA2]] | -0.45 | -0.49 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 6, C 24. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRG2]] | B | ADGRG2 activity raises KCNMA1's level | lines that do not express ADGRG2 (10) vs lines expressing it (40) | 4.40× lower at baseline in the lines without ADGRG2 | 0.009 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |
| [[LRRC49]] | B | LRRC49 activity raises KCNMA1's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 5.84× lower at baseline in the lines without LRRC49 | 0.027 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers KCNMA1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[HRH1]] | B | HRH1 activity raises KCNMA1's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 3.70× lower at baseline in the lines without HRH1 | 0.077 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[TPBG]] | B | TPBG activity raises KCNMA1's level | lines that do not express TPBG (10) vs lines expressing it (40) | 2.92× lower at baseline in the lines without TPBG | 0.091 | ⚠ within organs, on part of the lines |
| [[LRRC8C]] | B | LRRC8C activity raises KCNMA1's level | lines that do not express LRRC8C (8) vs lines expressing it (42) | 4.28× lower at baseline in the lines without LRRC8C | 0.098 | ⚠ within organs, on part of the lines; also absent: ZNF474, ACOT12, PPP4R4; maybe low, not absent |
| [[SRGN]] | C | SRGN activity raises KCNMA1's level | lines that do not express SRGN (30) vs lines expressing it (20) | 10.91× lower at baseline in the lines without SRGN | 0.001 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises KCNMA1's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 8.71× lower at baseline in the lines without INSYN2B | 0.002 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[SIRLNT]] | C | SIRLNT activity raises KCNMA1's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 10.27× lower at baseline in the lines without SIRLNT | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1; co-absent with the target |
| [[KIRREL3]] | C | KIRREL3 activity raises KCNMA1's level | lines that do not express KIRREL3 (36) vs lines expressing it (14) | 10.22× lower at baseline in the lines without KIRREL3 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN; co-absent with the target |
| [[VEGFC]] | C | VEGFC activity raises KCNMA1's level | lines that do not express VEGFC (22) vs lines expressing it (28) | 9.93× lower at baseline in the lines without VEGFC | 0.007 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises KCNMA1's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 6.99× lower at baseline in the lines without FRMD4A | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |

### Downstream of this gene

*93 arrows, 93 of them with an alert ⚠; grade A 0, B 70, C 23. Shown: the 12 strongest; 81 more arrows (81 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSANTD3]] | B | KCNMA1 activity raises MSANTD3's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 2.12× lower at baseline in the lines without KCNMA1 | 0.001 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[SLC6A6]] | B | KCNMA1 activity raises SLC6A6's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 2.73× lower at baseline in the lines without KCNMA1 | 0.004 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[CD44]] | B | KCNMA1 activity raises CD44's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 4.25× lower at baseline in the lines without KCNMA1 | 0.004 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[FGD4]] | B | KCNMA1 activity lowers FGD4's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 2.82× higher at baseline in the lines without KCNMA1 | 0.007 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[LINC01119]] | B | KCNMA1 activity raises LINC01119's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 2.35× lower at baseline in the lines without KCNMA1 | 0.008 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[LRRC49]] | B | KCNMA1 activity raises LRRC49's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 3.28× lower at baseline in the lines without KCNMA1 | 0.008 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[ATP13A3]] | B | KCNMA1 activity raises ATP13A3's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 1.72× lower at baseline in the lines without KCNMA1 | 0.011 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[LRRC8C]] | B | KCNMA1 activity raises LRRC8C's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 2.23× lower at baseline in the lines without KCNMA1 | 0.015 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| cells under [[Ouabain (Octahydrate) (drug)]] 0.5 µM | B | KCNMA1 activity lowers the cells' numbers under Ouabain (Octahydrate) 0.5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.48× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| cells under [[Ivermectin (drug)]] 0.5 µM | B | KCNMA1 activity lowers the cells' numbers under Ivermectin 0.5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.22× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[TPBG]] | B | KCNMA1 activity raises TPBG's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 2.86× lower at baseline in the lines without KCNMA1 | 0.024 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[TMEFF1]] | B | KCNMA1 activity raises TMEFF1's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 2.24× lower at baseline in the lines without KCNMA1 | 0.028 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.616). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.2, 16.2); signed map (22.2, 49.2). **Vector** length 123, 43.7% of its response variance represented; |z| ≥ 3 in 1,144 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.7 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | -0.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +2.8 |
| fall | [[Clobetasol propionate (drug)]] 5 µM | ⚠ position correction uncertain | -4.5 | -7.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.3 | -6.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.0 | -6.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM | ⚠ position correction uncertain | -3.9 | -5.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.8 | -6.7 |

## What is on record

|  |  |
|---|---|
| Name | potassium calcium-activated channel subfamily M alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.3 — chr10:76,869,601-77,638,369 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KCa1.1, mSLO1; previously SLO |
| Gene groups (HGNC) | Potassium calcium-activated channels |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 12 pathways, smallest: Acetylcholine inhibits contraction of outer hair cells; Ca2+ activated K+ channels; cGMP effects |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12791](https://www.uniprot.org/uniprotkb/Q12791) (Calcium-activated potassium channel subunit alpha-1):

> Potassium channel activated by both membrane depolarization or increase in cytosolic Ca(2+) that mediates export of K(+). It is also activated by the concentration of cytosolic Mg(2+). Its activation dampens the excitatory events that elevate the cytosolic Ca(2+) concentration and/or depolarize the cell membrane. It therefore contributes to repolarization of the membrane potential. Plays a key role in controlling excitability in a number of systems, such as regulation of the contraction of …

**Summary**, from NCBI Gene [3778](https://www.ncbi.nlm.nih.gov/gene/3778):

> This gene encodes the alpha subunit of calcium-activated BK channel. The encoded protein is involved in several physiological processes including smooth muscle contraction, neurotransmitter release and neuronal excitability. Mutations in this gene are associated with a spectrum of neurological disorders including Paroxysmal Nonkinesigenic Dyskinesia 3, Idiopathic Generalized Epilepsy 16 and Liang-Wang syndrome. [provided by RefSeq, Aug 2022]

**Accessions** — [HGNC:6284](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6284) · Entrez [3778](https://www.ncbi.nlm.nih.gov/gene/3778) · UniProt [Q12791](https://www.uniprot.org/uniprotkb/Q12791) · Ensembl [ENSG00000156113](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156113)

## Data

Gene col 7949: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7949); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7949, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7949]; `tensor/DDL_lfc|DDL_z.npy` [7949]; `embed/gene_vectors.npy` [7949]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7949 or target_col == 7949). Every well: [[KCNMA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNMA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
