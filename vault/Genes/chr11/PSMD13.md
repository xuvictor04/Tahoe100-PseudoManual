---
symbol: "PSMD13"
type: "gene"
col: 11705
ensembl_id: "ENSG00000185627"
name: "proteasome 26S subunit, non-ATPase 13"
location: "11p15.5"
module: 72
arm: "+"
pooled_cpm: 60.5
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# PSMD13

*proteasome 26S subunit, non-ATPase 13* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (13 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 3.38× (z +23.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.849× (z -4.6, q 0.003, down in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.261×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMB3]] (+0.71, fdr 7e-06), [[BABAM1]] (+0.68, fdr 7e-06), [[PLAA]] (+0.68, fdr 7e-06); moves opposite to [[SIRT1]] (-0.57, fdr 5e-05), [[BMI1]] (-0.53, fdr 4e-05), [[REL]] (-0.53, fdr 4e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11705.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.38×** | +23.5 | 0e+00 | 48/48 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.96×** | +20.9 | 0e+00 | 48/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.63×** | +17.6 | 0e+00 | 47/48 (LoVo, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.06×** | +13.9 | 6e-42 | 45/48 (HT-29, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.82×** | +8.2 | 2e-14 | 43/48 (LOX-IMVI, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **1.47×** | +7.4 | 1e-11 | 34/49 (MIA PaCa-2, A-172, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.12×** | +7.1 | 7e-11 | 37/45 (SNU-423, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.39×** | +6.3 | 2e-08 | 32/48 (SNU-423, MIA PaCa-2, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **1.34×** | +5.6 | 1e-06 | 32/47 (CFPAC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.34×** | +5.6 | 1e-06 | 29/48 (MIA PaCa-2, LoVo, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.32×** | +5.3 | 7e-06 | 27/48 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.32×** | +5.2 | 8e-06 | 25/48 (PANC-1, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +4.8 | 8e-05 | 27/48 (Hs 766T, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.28×** | +4.7 | 1e-04 | 26/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~65% of this change | **1.28×** | +4.5 | 2e-04 | 24/47 (LoVo, COLO 205, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.05 µM |  | **1.22×** | +3.8 | 0.005 | 17/48 (A-172, KATO III, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11705.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.261×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.849× | -4.6 | 0.003 | 17/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.815×** | -4.0 | 0.016 | 22/48 (H4, A498, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.685×** | -3.7 | 0.049 | 18/50 (H4, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.806×** | -3.6 | 0.052 | 15/49 (RKO, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | 0.790× | -3.3 | 0.10 | 6/48 (SW480, LS 180, …) | two highest doses | noisy plate (z scaled) |
| [[Afatinib (drug)]] 0.5 µM |  | 0.875× | -3.3 | 0.10 | 6/49 (LS 180, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.890× | -3.1 | 0.10 | 11/48 (SW 900, SK-MEL-2, …) | all doses, flat |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.848× | -3.1 | 0.10 | 14/49 (NCI-H1792, NCI-H2347, …) | top dose only | plate-row cell shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.853× | -3.1 | 0.10 | 12/48 (NCI-H2030, AN3 CA, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.854× | -3.1 | 0.10 | 17/48 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.856× | -3.1 | 0.11 | 6/48 (Panc 03.27, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11705. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 118 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.44× (z +15.6) | — |
| [[LoVo (line)]] | wt | 46.6 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.63× (z +15.9) | — |
| [[NCI-H460 (line)]] | wt | 39.6 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.41× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 43.6 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.50× (z +12.2) | — |
| [[HOP62 (line)]] | alt | 57.2 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.01× (z +14.5) | — |
| [[HT-29 (line)]] | alt | 67.6 | 4 | 0 | [[Auranofin (drug)]] 5 µM 4.38× (z +15.2) | — |
| [[LOX-IMVI (line)]] | wt | 51.3 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.23× (z +14.0) | — |
| [[NCI-H1573 (line)]] | alt | 38.5 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.78× (z +14.1) | — |
| [[SNU-423 (line)]] | alt | 62.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.32× (z +11.8) | — |
| [[SW480 (line)]] | alt | 70.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.35× (z +14.1) | — |
| [[A-172 (line)]] | wt | 80.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.76× (z +11.5) | — |
| [[A-427 (line)]] | wt | 71.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.17× (z +11.5) | — |
| [[C32 (line)]] | wt | 49.4 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.11× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 32.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.90× (z +11.6) | — |
| [[H4 (line)]] | wt | 92.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.97× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 36.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.85× (z +12.8) | — |
| [[hTERT-HPNE (line)]] | wt | 57.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.41× (z +9.7) | — |
| [[KATO III (line)]] | alt | 39.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.58× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 45.5 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.94× (z +12.0) | — |
| [[NCI-H1792 (line)]] | alt | 53.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.82× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 70.7 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.83× (z +11.7) | — |
| [[Panc 03.27 (line)]] | alt | 39.6 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.72× (z +11.4) | — |
| [[SNU-1 (line)]] | wt | 41.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.98× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 63.7 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.46× (z +9.6) | — |
| [[A549 (line)]] | wt | 52.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.69× (z +8.8) | — |
| [[C-33 A (line)]] | alt | 51.9 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.57× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 63.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.50× (z +9.3) | — |
| [[HepG2_C3A (line)]] | wt | 41.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.84× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 64.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.43× (z +11.6) | — |
| [[HS-578T (line)]] | alt | 71.5 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.58× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 71.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.51× (z +12.2) | — |
| [[RPMI-7951 (line)]] | alt | 68.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.94× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 54.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.48× (z +11.0) | — |
| [[SW48 (line)]] | wt | 59.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.87× (z +9.2) | — |
| [[A498 (line)]] | wt | 89.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.15× (z +8.8) | — |
| [[AsPC-1 (line)]] | alt | 68.0 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.19× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 31.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.55× (z +9.2) | — |
| [[J82 (line)]] | alt | 90.2 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.04× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 53.9 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.70× (z +8.8) | — |
| [[RKO (line)]] | wt | 76.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.62× (z +9.8) | — |
| [[AN3 CA (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11705), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMB3]] | +0.71 | +0.66 / +0.74 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[BABAM1]] | +0.68 | +0.66 / +0.72 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[PLAA]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[PSMC4]] | +0.67 | +0.71 / +0.69 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MTORC1_SIGNALING; STRING 999 |
| [[GDAP2]] | +0.66 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[PSMB2]] | +0.66 | +0.69 / +0.70 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[HSP90AA2P]] | +0.65 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[UFD1]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 | pathway: Cellular response to chemical stress; STRING 655 |
| [[ORC3]] | +0.64 | +0.68 / +0.51 | both halves | 1e-05 | pathway: Assembly of the pre-replicative complex |
| [[ANKRD39]] | +0.63 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[TALDO1]] | +0.63 | +0.63 / +0.57 | both halves | 1e-05 | pathway: Cellular response to chemical stress |
| [[PCYT1A]] | +0.63 | +0.66 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT1]] | -0.57 | -0.67 / -0.40 | both halves | 5e-05 | pathway: Adherens junctions interactions |
| [[BMI1]] | -0.53 | -0.49 / -0.42 | both halves | 4e-05 | pathway: Intracellular signaling by second messengers |
| [[REL]] | -0.53 | -0.54 / -0.42 | both halves | 4e-05 | pathway: Activation of NF-kappaB in B cells; STRING 409 |
| [[SYDE2]] | -0.52 | -0.58 / -0.39 | both halves | 6e-05 |  |
| [[FAM241A]] | -0.51 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[CHD2]] | -0.51 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[HIVEP2]] | -0.50 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[ZBTB10]] | -0.50 | -0.53 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.793). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.7, -9.3); signed map (-27.5, -26.1). **Vector** length 93.6, 25.7% of its response variance represented; |z| ≥ 3 in 904 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antigen processing: Ub, ATP-independent proteasomal degradation* (reactome, mean cos +0.59 to 7); *MYC targets v1* (hallmark, mean cos +0.59 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.8 | +17.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.6 | +23.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.3 | +20.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +13.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.0 | +7.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.2 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.2 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | +1.4 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | +1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | -4.2 | +5.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | -3.4 | +5.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.1 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -1.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -0.6 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit, non-ATPase 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:236,966-252,984 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p40.5, Rpn9 |
| Gene groups (HGNC) | Proteasome |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 170 pathways, smallest: Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC); Cross-presentation of soluble exogenous antigens (endosomes) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNM6](https://www.uniprot.org/uniprotkb/Q9UNM6) (26S proteasome non-ATPase regulatory subunit 13):

> Component of the 26S proteasome, a multiprotein complex involved in the ATP-dependent degradation of ubiquitinated proteins. This complex plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged proteins, which could impair cellular functions, and by removing proteins whose functions are no longer required. Therefore, the proteasome participates in numerous cellular processes, including cell cycle progression, apoptosis, or DNA damage repair.

**Summary**, from NCBI Gene [5719](https://www.ncbi.nlm.nih.gov/gene/5719):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9558](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9558) · Entrez [5719](https://www.ncbi.nlm.nih.gov/gene/5719) · UniProt [Q9UNM6](https://www.uniprot.org/uniprotkb/Q9UNM6) · Ensembl [ENSG00000185627](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185627)

## Data

Gene col 11705: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11705); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11705, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11705]; `tensor/DDL_lfc|DDL_z.npy` [11705]; `embed/gene_vectors.npy` [11705]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11705 or target_col == 11705). Every well: [[PSMD13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMD13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
