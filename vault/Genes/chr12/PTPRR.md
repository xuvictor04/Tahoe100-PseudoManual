---
symbol: "PTPRR"
type: "gene"
col: 7704
ensembl_id: "ENSG00000153233"
name: "protein tyrosine phosphatase receptor type R"
location: "12q15"
module: 8
arm: "+"
pooled_cpm: 83.17
n_lines_expressing: 18
n_dd_up: 17
n_dd_down: 24
n_dd_up_clean: 14
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 60
direction_downstream: 89
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# PTPRR

*protein tyrosine phosphatase receptor type R* — 12q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.5 µM: 1.45× (z +5.0, q 3e-04, up in 13 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.491× (z -8.4, q 2e-14, down in 16 of 16 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.553× (z -6.7, q 4e-09, down in 12 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRB]] (+0.87, fdr 7e-06, ⚠ same locus), [[GCNT3]] (+0.69, fdr 7e-06), [[UGT1A6]] (+0.69, fdr 7e-06), [[UGT1A9]] (+0.68, fdr 7e-06); moves opposite to [[CROCCP3-1]] (-0.58, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 60 arrows point to it, the strongest [[ARHGAP42]] → it (grade B ⚠); 89 go from it, the strongest it → [[ST3GAL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7704.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **1.45×** | +5.0 | 3e-04 | 13/16 (NCI-H1573, AsPC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +4.7 | 5e-04 | 0/15 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +4.6 | 5e-04 | 1/16 (A-172) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.45×** | +4.6 | 5e-04 | 10/17 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.6 | 5e-04 | 2/16 (CFPAC-1, H4) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **2.01×** | +4.4 | 0.001 | 13/15 (NCI-H1792, AsPC-1, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.40×** | +3.8 | 0.013 | 0/15 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.021 | 7/15 (HT-29, SW1417, …) | top dose only |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.031 | 1/16 (H4) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.034 | 12/15 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.038 | 8/16 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.056 | 0/17 | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.056 | 1/16 (LOX-IMVI) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.056 | 0/16 | rises with dose | position effect removed |
| [[MK-3903 (drug)]] 5 µM |  | **1.64×** | +3.1 | 0.071 | 4/16 (AsPC-1, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.41×** | +3.0 | 0.099 | 3/16 (AsPC-1, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.099 | 0/15 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7704.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.491×** | -8.4 | 2e-14 | 16/16 (LoVo, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.553×** | -6.7 | 4e-09 | 12/16 (NCI-H1792, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.592×** | -6.2 | 1e-07 | 15/16 (LoVo, LS 180, …) | all doses, flat | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.633×** | -5.4 | 9e-06 | 15/16 (LoVo, LS 180, …) | all doses, flat | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.641×** | -5.2 | 2e-05 | 5/15 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.662×** | -4.9 | 1e-04 | 5/15 (Hs 766T, AsPC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.674×** | -4.7 | 3e-04 | 10/15 (SW 900, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.678×** | -4.6 | 3e-04 | 15/16 (LS 180, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~22% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.690×** | -4.4 | 7e-04 | 10/15 (KATO III, CFPAC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.690×** | -4.4 | 7e-04 | 14/16 (LS 180, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.693×** | -4.3 | 8e-04 | 11/16 (NCI-H1792, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.694×** | -4.3 | 8e-04 | 14/15 (AsPC-1, LS 180, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.695×** | -4.3 | 8e-04 | 7/15 (SW 900, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.700×** | -4.2 | 0.001 | 10/16 (AsPC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **0.705×** | -4.1 | 0.001 | 6/15 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.743×** | -3.5 | 0.016 | 6/16 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.740×** | -3.3 | 0.026 | 0/16 | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.759×** | -3.2 | 0.036 | 9/16 (AsPC-1, Hs 766T, …) | top dose only | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.768×** | -3.1 | 0.051 | 2/16 (SW 1088, H4) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.55 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7704. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 508 | 0 | 23 (15 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0134× (z -32.7) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -21.6) |
| [[AsPC-1 (line)]] | alt | 479 | 0 | 20 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0326× (z -27.5) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0268× (z -19.8) |
| [[CFPAC-1 (line)]] | alt | 96.6 | 0 | 20 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -17.1) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 248 | 0 | 20 (13 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0280× (z -25.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.0280× (z -24.8) |
| [[LoVo (line)]] | wt | 1,081 | 0 | 15 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0144× (z -38.8) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -17.8) |
| [[KATO III (line)]] | alt | 114 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0768× (z -26.5) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.104× (z -16.5) |
| [[SW1417 (line)]] | alt | 80.6 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -19.2) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -13.0) |
| [[Panc 03.27 (line)]] | alt | 106 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0531× (z -16.9) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0743× (z -14.4) |
| [[Hs 766T (line)]] | wt | 43.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -12.9) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -9.6) |
| [[HT-29 (line)]] | alt | 21.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -10.8) ⚠ cell-cycle shift, explains ~64% of this change |
| [[A-172 (line)]] | wt | 32.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +15.6) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.03× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 37.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -9.4) ⚠ cell-cycle shift, explains ~64% of this change |
| [[H4 (line)]] | wt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -9.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 5.50 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.71 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.06 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.83 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.57 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 18.6 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 18.7 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.62 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.96 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.58 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.04 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.72 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.02 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.95 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.15 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.92 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.87 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.00 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.11 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.28 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7704), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRB]] | +0.87 | +0.88 / +0.84 | both halves | 7e-06 | same gene group; ⚠ same locus (0.6 kb, same strand: neighbours can correlate without regulation) |
| [[GCNT3]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[UGT1A6]] | +0.69 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[UGT1A9]] | +0.68 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[CLIC5]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[ADGRF1]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[TMPRSS3]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SLC44A4]] | +0.65 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[RBM47]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[TC2N]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[IKZF2]] | +0.64 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[UGT1A1]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[UGT1A8]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP3-1]] | -0.58 | -0.52 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*60 arrows, 60 of them with an alert ⚠; grade A 0, B 8, C 52. Shown: the 12 strongest; 48 more arrows (48 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP42]] | B | ARHGAP42 activity raises PTPRR's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 2.75× lower at baseline in the lines without ARHGAP42 | 0.044 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[IKZF2]] | B | IKZF2 activity raises PTPRR's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 2.45× lower at baseline in the lines without IKZF2 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[BDKRB2]] | B | BDKRB2 activity raises PTPRR's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 2.79× lower at baseline in the lines without BDKRB2 | 0.056 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[MAP2K1]] | B | MAP2K1 activity lowers PTPRR's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[GNA14]] | B | GNA14 activity raises PTPRR's level | lines that do not express GNA14 (5) vs lines expressing it (45) | 3.63× lower at baseline in the lines without GNA14 | 0.080 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[MTUS1]] | B | MTUS1 activity raises PTPRR's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.24× lower at baseline in the lines without MTUS1 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[RBM47]] | B | RBM47 activity raises PTPRR's level | lines that do not express RBM47 (20) vs lines expressing it (30) | 2.34× lower at baseline in the lines without RBM47 | 0.092 | ⚠ within organs, on part of the lines; also absent: FA2H, MISP, ELF3 |
| [[MECOM]] | B | MECOM activity raises PTPRR's level | lines that do not express MECOM (18) vs lines expressing it (32) | 2.41× lower at baseline in the lines without MECOM | 0.095 | ⚠ within organs, on part of the lines; also absent: STYK1, IKZF2, TSTD1; maybe low, not absent |
| [[UGT1A1]] | C | UGT1A1 activity raises PTPRR's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 6.09× lower at baseline in the lines without UGT1A1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; co-absent with the target |
| [[PTPRB]] | C | PTPRB activity raises PTPRR's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 4.89× lower at baseline in the lines without PTPRB | 0.001 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4; co-absent with the target |
| [[UGT1A6]] | C | UGT1A6 activity raises PTPRR's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 5.44× lower at baseline in the lines without UGT1A6 | 0.001 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1; co-absent with the target |
| [[TTC22]] | C | TTC22 activity raises PTPRR's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 5.23× lower at baseline in the lines without TTC22 | 0.001 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5; co-absent with the target |

### Downstream of this gene

*89 arrows, 89 of them with an alert ⚠; grade A 0, B 21, C 68. Shown: the 12 strongest; 77 more arrows (77 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST3GAL3]] | B | PTPRR activity lowers ST3GAL3's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 1.71× higher at baseline in the lines without PTPRR | 0.009 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2 |
| [[THRB]] | B | PTPRR activity raises THRB's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 2.55× lower at baseline in the lines without PTPRR | 0.011 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2 |
| [[MUC12]] | B | PTPRR activity raises MUC12's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 1.85× lower at baseline in the lines without PTPRR | 0.013 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2 |
| [[ST3GAL3]] | B | PTPRR activity weakens ST3GAL3's drug response | lines that do not express PTPRR (31) vs lines expressing it (16) | the lines without PTPRR respond 1.98× as strongly (z diff -2.92); strongest at Panobinostat 0.5 µM: 0.66x vs 1.27x (z diff -6.1) | 0.013 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2; target measured in part of the lines; artifact flags |
| [[BAG1]] | B | PTPRR activity raises BAG1's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 1.38× lower at baseline in the lines without PTPRR | 0.017 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2 |
| [[RBM47]] | B | PTPRR activity raises RBM47's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 2.78× lower at baseline in the lines without PTPRR | 0.022 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2 |
| [[CTNND1]] | B | PTPRR activity raises CTNND1's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 1.68× lower at baseline in the lines without PTPRR | 0.022 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2 |
| [[HOMER2]] | B | PTPRR activity lowers HOMER2's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 1.82× higher at baseline in the lines without PTPRR | 0.027 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2 |
| [[ULK2]] | B | PTPRR activity lowers ULK2's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 2.05× higher at baseline in the lines without PTPRR | 0.030 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2 |
| [[MECOM]] | B | PTPRR activity raises MECOM's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 2.59× lower at baseline in the lines without PTPRR | 0.034 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2 |
| [[ARHGAP42]] | B | PTPRR activity raises ARHGAP42's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 2.35× lower at baseline in the lines without PTPRR | 0.042 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2 |
| [[UBE2H]] | B | PTPRR activity raises UBE2H's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 1.58× lower at baseline in the lines without PTPRR | 0.047 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.701). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.5, 54.4); signed map (63.6, 3.4). **Vector** length 95.2, 36.2% of its response variance represented; |z| ≥ 3 in 730 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +4.5 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | -0.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +4.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -3.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -5.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.0 | -4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -4.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase receptor type R |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q15 — chr12:70,638,073-70,920,738 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PTPBR7, PTP-SL, EC-PTP, PCPTP1; previously PTPRQ |
| Gene groups (HGNC) | Protein tyrosine phosphatases receptor type |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15256](https://www.uniprot.org/uniprotkb/Q15256) (Receptor-type tyrosine-protein phosphatase R):

> Sequesters mitogen-activated protein kinases (MAPKs) such as MAPK1, MAPK3 and MAPK14 in the cytoplasm in an inactive form. The MAPKs bind to a dephosphorylated kinase interacting motif, phosphorylation of which by the protein kinase A complex releases the MAPKs for activation and translocation into the nucleus (By similarity).

**Summary**, from NCBI Gene [5801](https://www.ncbi.nlm.nih.gov/gene/5801):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP possesses an extracellular region, a single transmembrane region, and a single intracellular catalytic domain, and thus represents a receptor-type PTP. Silencing of this gene has been associated with colorectal cancer. …

**Accessions** — [HGNC:9680](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9680) · Entrez [5801](https://www.ncbi.nlm.nih.gov/gene/5801) · UniProt [Q15256](https://www.uniprot.org/uniprotkb/Q15256) · Ensembl [ENSG00000153233](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153233)

## Data

Gene col 7704: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7704); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7704, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7704]; `tensor/DDL_lfc|DDL_z.npy` [7704]; `embed/gene_vectors.npy` [7704]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7704 or target_col == 7704). Every well: [[PTPRR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPRR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
