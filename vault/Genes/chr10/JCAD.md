---
symbol: "JCAD"
type: "gene"
col: 9181
ensembl_id: "ENSG00000165757"
name: "junctional cadherin 5 associated"
location: "10p11.23"
module: 104
arm: "+"
pooled_cpm: 26.34
n_lines_expressing: 30
n_dd_up: 29
n_dd_down: 13
n_dd_up_clean: 20
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 9
direction_downstream: 8
tags: ["gene", "module/104"]
generated_by: "tahoemap"
---

# JCAD

*junctional cadherin 5 associated* — 10p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.78× (z +13.0, q 4e-36, up in 19 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.591× (z -8.5, q 1e-14, down in 15 of 28 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3RF3]] (+0.67, fdr 7e-06), [[IL18R1]] (+0.63, fdr 7e-06), [[ABLIM3]] (+0.59, fdr 1e-05); moves opposite to [[PTPRB]] (-0.46, fdr 3e-05), [[PTPRR]] (-0.44, fdr 3e-05), [[MAF]] (-0.44, fdr 2e-04).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[RGS17]] → it (grade B ⚠); 8 go from it, the strongest it → [[LAMB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9181.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +13.0 | 4e-36 | 19/28 (J82, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.01×** | +11.2 | 1e-26 | 13/28 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.76×** | +9.0 | 3e-17 | 12/27 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.70×** | +8.5 | 3e-15 | 11/28 (J82, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +7.4 | 2e-11 | 11/28 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.49×** | +6.4 | 2e-08 | 6/22 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +6.1 | 7e-08 | 10/25 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.45×** | +6.0 | 1e-07 | 13/27 (LoVo, NCI-H2347, …) | two highest doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.45×** | +5.9 | 2e-07 | 12/26 (A-172, HOP62, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.44×** | +5.4 | 4e-06 | 6/20 (NCI-H2347, PANC-1, …) | inconsistent across doses | composition shift; position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.37×** | +5.1 | 2e-05 | 13/27 (HOP62, A-172, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.37×** | +5.0 | 2e-05 | 10/27 (LoVo, CFPAC-1, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.35×** | +4.9 | 5e-05 | 8/26 (CFPAC-1, Panc 03.27, …) | two highest doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.33×** | +4.6 | 2e-04 | 11/27 (HOP62, H4, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.32×** | +4.4 | 3e-04 | 11/26 (HOP62, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +4.2 | 0.001 | 10/28 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +4.1 | 0.001 | 10/26 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.003 | 13/27 (HOP62, A-172, …) | two highest doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.29×** | +3.8 | 0.004 | 9/26 (A-172, NCI-H1792, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.004 | 9/26 (J82, PANC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.008 | 11/26 (HOP62, A-172, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9181.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.591×** | -8.5 | 1e-14 | 15/28 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.692×** | -5.9 | 8e-07 | 15/25 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.780×** | -5.7 | 3e-06 | 18/27 (A549, NCI-H460, …) | rises with dose | composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.754×** | -5.4 | 7e-06 | 12/28 (HS-578T, A549, …) | two highest doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.727×** | -5.1 | 3e-05 | 11/26 (A-172, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.769×** | -4.2 | 0.002 | 11/26 (SNU-1, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.761×** | -4.2 | 0.002 | 13/28 (A549, NCI-H460, …) | top dose only | composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **0.744×** | -4.1 | 0.002 | 13/28 (SW48, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.783×** | -4.0 | 0.005 | 10/26 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.788×** | -3.9 | 0.007 | 9/28 (SW48, HS-578T, …) | all doses, flat |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.846× | -3.8 | 0.007 | 8/28 (A549, PANC-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.798×** | -3.5 | 0.022 | 12/25 (SW48, HS-578T, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.682×** | -3.2 | 0.056 | 8/23 (HOP62, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.820×** | -3.1 | 0.081 | 9/25 (hTERT-HPNE, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 5 µM |  | 0.875× | -3.0 | 0.088 | 6/28 (A549, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9181. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 79.1 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0706× (z -32.2) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.346× (z -9.2) |
| [[A-172 (line)]] | wt | 91.3 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 22.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0854× (z -17.8) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.148× (z -9.8) |
| [[H4 (line)]] | wt | 15.2 | 0 | 2 (1 ⚠) | — | [[Radotinib (drug)]] 0.5 µM 0.0834× (z -9.5) |
| [[HOP62 (line)]] | alt | 92.0 | 2 | 0 | [[Clobetasol propionate (drug)]] 5 µM 2.86× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 112 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[hTERT-HPNE (line)]] | wt | 31.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.121× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -8.8) |
| [[PANC-1 (line)]] | alt | 63.7 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 24.0 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0694× (z -10.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.252× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 15.6 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.207× (z -8.5) |
| [[SNU-423 (line)]] | alt | 22.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +8.8) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[A-427 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.56 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.96 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.58 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.99 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.28 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9181), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3RF3]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[IL18R1]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[ABLIM3]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[GAB3]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[DNER]] | +0.57 | +0.36 / +0.62 | both halves | 9e-05 |  |
| [[FOXC2]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[FOXL1]] | +0.56 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[STEAP3]] | +0.56 | +0.60 / +0.46 | both halves | 2e-05 |  |
| [[SLC45A1]] | +0.54 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[AMPH]] | +0.54 | +0.32 / +0.62 | both halves | 2e-04 |  |
| [[TOX2]] | +0.54 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[EHD3]] | +0.53 | +0.47 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRB]] | -0.46 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[PTPRR]] | -0.44 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[MAF]] | -0.44 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[NPPB]] | -0.44 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[FAM151B-DT]] | -0.42 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[SATB1]] | -0.41 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[HOXA-AS2]] | -0.41 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[TRIML2]] | -0.41 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[EPB41]] | -0.41 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[NAA38]] | -0.41 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[ZSCAN31]] | -0.40 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[EDIL3-DT]] | -0.40 | -0.41 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RGS17]] | B | RGS17 activity raises JCAD's level | lines that do not express RGS17 (15) vs lines expressing it (35) | 3.03× lower at baseline in the lines without RGS17 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: WDR17, CFAP20DC, AFAP1L1 |
| [[MAP2K1]] | B | MAP2K1 activity raises JCAD's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[PID1]] | B | PID1 activity raises JCAD's level | lines that do not express PID1 (22) vs lines expressing it (28) | 2.58× lower at baseline in the lines without PID1 | 0.059 | ⚠ within organs, on part of the lines; also absent: TRPA1, DOCK10, ENSG00000289600 |
| [[NR3C1]] | B | NR3C1 activity raises JCAD's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[BCAR3]] | B | BCAR3 activity raises JCAD's level | lines that do not express BCAR3 (9) vs lines expressing it (41) | 2.57× lower at baseline in the lines without BCAR3 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, CD59, C11orf91; maybe low, not absent |
| [[TOX2]] | B | TOX2 activity raises JCAD's level | lines that do not express TOX2 (18) vs lines expressing it (32) | 2.41× lower at baseline in the lines without TOX2 | 0.098 | ⚠ within organs, on part of the lines; also absent: TWIST2, OLFM1, PLEKHG4B |
| [[FOXC2]] | C | FOXC2 activity raises JCAD's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 3.48× lower at baseline in the lines without FOXC2 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT; co-absent with the target |
| [[FOXL1]] | C | FOXL1 activity raises JCAD's level | lines that do not express FOXL1 (25) vs lines expressing it (25) | 3.38× lower at baseline in the lines without FOXL1 | 0.033 | ⚠ within organs, on part of the lines; also absent: SIRLNT, PTHLH, WNT5A; co-absent with the target |
| [[FHL1]] | C | FHL1 activity raises JCAD's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 3.55× lower at baseline in the lines without FHL1 | 0.090 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMB1]] | B | JCAD activity raises LAMB1's level | lines that do not express JCAD (20) vs lines expressing it (30) | 1.91× lower at baseline in the lines without JCAD | 0.010 | ⚠ within organs, on part of the lines; also absent: ANKRD33B, FAT4, EFEMP1 |
| [[AFAP1L1]] | B | JCAD activity raises AFAP1L1's level | lines that do not express JCAD (20) vs lines expressing it (30) | 2.34× lower at baseline in the lines without JCAD | 0.027 | ⚠ within organs, on part of the lines; also absent: ANKRD33B, FAT4, EFEMP1 |
| [[ITPRIP]] | B | JCAD activity raises ITPRIP's level | lines that do not express JCAD (20) vs lines expressing it (30) | 1.75× lower at baseline in the lines without JCAD | 0.046 | ⚠ within organs, on part of the lines; also absent: ANKRD33B, FAT4, EFEMP1 |
| cells under [[Cobimetinib (drug)]] 5 µM | B | JCAD activity lowers the cells' numbers under Cobimetinib 5 µM (makes them more sensitive) | lines that do not express JCAD (20) vs lines expressing it (28) | the lines without JCAD: 1.14× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ANKRD33B, FAT4, EFEMP1 |
| [[GAB3]] | B | JCAD activity raises GAB3's level | lines that do not express JCAD (20) vs lines expressing it (30) | 1.78× lower at baseline in the lines without JCAD | 0.082 | ⚠ within organs, on part of the lines; also absent: ANKRD33B, FAT4, EFEMP1 |
| [[RGS17]] | B | JCAD activity raises RGS17's level | lines that do not express JCAD (20) vs lines expressing it (30) | 2.93× lower at baseline in the lines without JCAD | 0.085 | ⚠ within organs, on part of the lines; also absent: ANKRD33B, FAT4, EFEMP1 |
| [[ITGA5]] | B | JCAD activity raises ITGA5's level | lines that do not express JCAD (20) vs lines expressing it (30) | 2.56× lower at baseline in the lines without JCAD | 0.094 | ⚠ within organs, on part of the lines; also absent: ANKRD33B, FAT4, EFEMP1 |
| [[FHL1]] | C | JCAD activity raises FHL1's level | lines that do not express JCAD (20) vs lines expressing it (30) | 4.58× lower at baseline in the lines without JCAD | 0.079 | ⚠ within organs, on part of the lines; also absent: ANKRD33B, FAT4, EFEMP1; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.605). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.8, 14.3); signed map (17.2, 35.5). **Vector** length 80.2, 18.8% of its response variance represented; |z| ≥ 3 in 900 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +13.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.1 | +6.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.7 | +4.1 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.7 | +5.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.5 | +4.6 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -8.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.1 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | junctional cadherin 5 associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.23 — chr10:30,012,803-30,115,494 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA1462 |
| Matched by | ensembl_id |

UniProt [Q9P266](https://www.uniprot.org/uniprotkb/Q9P266) carries no function annotation.

**Summary**, from NCBI Gene [57608](https://www.ncbi.nlm.nih.gov/gene/57608):

> This gene encodes an endothelial cell-to-cell junction protein. Naturally occurring mutations in this gene are associated with coronary artery disease, late onset alzheimer disease, and emphysema distribution. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:29283](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29283) · Entrez [57608](https://www.ncbi.nlm.nih.gov/gene/57608) · UniProt [Q9P266](https://www.uniprot.org/uniprotkb/Q9P266) · Ensembl [ENSG00000165757](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165757)

## Data

Gene col 9181: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9181); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9181, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9181]; `tensor/DDL_lfc|DDL_z.npy` [9181]; `embed/gene_vectors.npy` [9181]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9181 or target_col == 9181). Every well: [[JCAD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JCAD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
