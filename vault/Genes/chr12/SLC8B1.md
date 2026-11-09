---
symbol: "SLC8B1"
type: "gene"
col: 1566
ensembl_id: "ENSG00000089060"
name: "solute carrier family 8 member B1"
location: "12q24.13"
module: 192
arm: "+"
pooled_cpm: 26.02
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 14
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/192"]
generated_by: "tahoemap"
---

# SLC8B1

*solute carrier family 8 member B1* — 12q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.14× (z +23.4, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.583× (z -11.0, q 3e-25, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PBX4]] (+0.68, fdr 1e-05), [[DOCK6]] (+0.64, fdr 1e-05), [[RTN2]] (+0.64, fdr 1e-05); moves opposite to [[UFL1-AS1]] (-0.63, fdr 9e-05), [[MCTS1]] (-0.61, fdr 3e-05), [[SLC12A2-DT]] (-0.58, fdr 2e-04).
> It is in [[Module 192]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1566.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.14×** | +23.4 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.91×** | +21.8 | 0e+00 | 47/48 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.34×** | +17.3 | 0e+00 | 46/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +13.5 | 3e-39 | 35/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +11.7 | 9e-30 | 39/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +8.5 | 2e-15 | 29/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.43×** | +7.0 | 3e-10 | 25/47 (BT-474, HS-578T, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +6.5 | 5e-09 | 24/47 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +6.4 | 1e-08 | 23/47 (BT-474, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.29×** | +5.2 | 1e-05 | 18/47 (NCI-H2347, BT-474, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +5.1 | 2e-05 | 15/48 (A-427, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.38×** | +4.6 | 2e-04 | 9/45 (SW480, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.24×** | +4.2 | 0.001 | 12/45 (SW 900, SW1417, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.15× | +4.0 | 0.002 | 16/47 (NCI-H460, hTERT-HPNE, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.44×** | +3.9 | 0.003 | 14/41 (BT-474, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.010 | 14/45 (SNU-423, SHP-77, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.050 | 11/48 (BT-474, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1566.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.583×** | -11.0 | 3e-25 | 28/47 (LoVo, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.585×** | -10.9 | 3e-25 | 33/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.654×** | -8.6 | 1e-15 | 30/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.658×** | -7.9 | 4e-13 | 21/38 (NCI-H1792, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.707×** | -7.1 | 2e-10 | 27/47 (J82, LOX-IMVI, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.596×** | -5.5 | 3e-06 | 23/49 (A-172, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.767×** | -5.4 | 6e-06 | 18/48 (HOP62, J82, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.845× | -4.9 | 9e-05 | 18/48 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.798×** | -4.6 | 3e-04 | 15/48 (HS-578T, CHP-212, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.800×** | -4.6 | 3e-04 | 20/48 (SW48, LoVo, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.677×** | -4.2 | 0.002 | 17/47 (A-172, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.824×** | -4.0 | 0.004 | 19/47 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.828×** | -3.7 | 0.010 | 15/47 (A549, SW480, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.718×** | -3.5 | 0.017 | 12/46 (H4, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.849× | -3.3 | 0.033 | 10/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.855× | -3.2 | 0.044 | 13/48 (SNU-1, A498, …) | inconsistent across doses |  |
| [[crizotinib (drug)]] 5 µM |  | 0.853× | -3.1 | 0.055 | 7/48 (A-172, A-427, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.864× | -3.0 | 0.077 | 13/47 (AN3 CA, J82, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1566. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 25.9 | 2 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.30× (z +9.3) | [[Harringtonine (drug)]] 0.5 µM 0.236× (z -11.2) |
| [[A-427 (line)]] | wt | 19.9 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.46× (z +10.2) | [[Lonafarnib (drug)]] 5 µM 0.0824× (z -8.8) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 26.3 | 3 | 2 | [[Panobinostat (drug)]] 0.5 µM 3.97× (z +13.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.371× (z -9.9) |
| [[SW480 (line)]] | alt | 18.1 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 3.91× (z +12.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.329× (z -9.8) |
| [[J82 (line)]] | alt | 28.8 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.68× (z +10.3) | [[Digitoxin (drug)]] 5 µM 0.239× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -9.1) |
| [[A-172 (line)]] | wt | 31.8 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.51× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -11.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 32.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.17× (z +9.6) | — |
| [[A549 (line)]] | wt | 32.3 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.179× (z -10.1) |
| [[BT-474 (line)]] | alt | 37.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.09× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.0567× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[HOP62 (line)]] | alt | 17.1 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 20.3 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 4.18× (z +9.1) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.236× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 24.8 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.69× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.166× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.283× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 25.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 34.3 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.96× (z +10.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.84× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 30.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.35× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SW1417 (line)]] | alt | 25.4 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.84× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -9.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.87× (z +9.0) | — |
| [[LoVo (line)]] | wt | 53.3 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.50× (z +9.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.330× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 19.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.53× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 28.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.47× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 15.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.54× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 67.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -15.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[C-33 A (line)]] | alt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 46.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.379× (z -8.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 26.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.234× (z -8.9) |
| [[H4 (line)]] | wt | 28.6 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.5 µM 0.0590× (z -10.4) |
| [[HS-578T (line)]] | alt | 17.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[KATO III (line)]] | alt | 26.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.313× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 22.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.161× (z -14.0) |
| [[RKO (line)]] | wt | 29.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.38× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[AN3 CA (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1566), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBX4]] | +0.68 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[DOCK6]] | +0.64 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[RTN2]] | +0.64 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[GIPR]] | +0.63 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[CYTH1]] | +0.63 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[PTPRS]] | +0.61 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[TSPAN9]] | +0.60 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[RAB39A]] | +0.60 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[MAST3]] | +0.60 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[PWWP3A]] | +0.59 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[FLNB-AS1]] | +0.59 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[FLNB]] | +0.59 | +0.43 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UFL1-AS1]] | -0.63 | -0.47 / -0.37 | both halves | 9e-05 |  |
| [[MCTS1]] | -0.61 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[SLC12A2-DT]] | -0.58 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[FBXL17]] | -0.57 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[DNAI4]] | -0.57 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[BDNF-AS]] | -0.57 | -0.41 / -0.28 | both halves | 3e-04 |  |
| [[NAALADL2]] | -0.57 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[ZFP91]] | -0.56 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[C5orf15]] | -0.55 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[CRPPA]] | -0.54 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[ENTPD3-AS1]] | -0.54 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[GALNT7]] | -0.54 | -0.43 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 192]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.50; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.2, 1.6); signed map (-23.7, 22.7). **Vector** length 95.5, 22.0% of its response variance represented; |z| ≥ 3 in 1,229 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.5 | +21.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.2 | +23.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +13.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.9 | +17.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +4.8 | +5.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.4 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +4.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.2 | -11.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.0 | -8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | +0.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 8 member B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.13 — chr12:113,298,759-113,359,493 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22233, NCKX6, NCLX; previously SLC24A6 |
| Gene groups (HGNC) | Solute carrier family 8 |
| Reactome | 5 pathways, smallest: Sodium/Calcium exchangers; Mitochondrial calcium ion transport; Metal ion SLC transporters |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6J4K2](https://www.uniprot.org/uniprotkb/Q6J4K2) (Mitochondrial sodium/calcium exchanger protein):

> Mitochondrial sodium/calcium antiporter that mediates sodium-dependent calcium efflux from mitochondrion, by mediating the exchange of 3 sodium ions per 1 calcium ion. Plays a central role in mitochondrial calcium homeostasis by mediating mitochondrial calcium extrusion: calcium efflux is essential for mitochondrial function and cell survival, notably in cardiomyocytes (By similarity). Mitochondrial calcium export is ph-dependent (By similarity). Regulates rates of glucose-dependent insulin …

**Summary**, from NCBI Gene [80024](https://www.ncbi.nlm.nih.gov/gene/80024):

> SLC24A6 belongs to a family of potassium-dependent sodium/calcium exchangers that maintain cellular calcium homeostasis through the electrogenic countertransport of 4 sodium ions for 1 calcium ion and 1 potassium ion (Cai and Lytton, 2004 [PubMed 14625281]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:26175](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26175) · Entrez [80024](https://www.ncbi.nlm.nih.gov/gene/80024) · UniProt [Q6J4K2](https://www.uniprot.org/uniprotkb/Q6J4K2) · Ensembl [ENSG00000089060](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089060)

## Data

Gene col 1566: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1566); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1566, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1566]; `tensor/DDL_lfc|DDL_z.npy` [1566]; `embed/gene_vectors.npy` [1566]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1566 or target_col == 1566). Every well: [[SLC8B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC8B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
