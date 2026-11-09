---
symbol: "SLC38A6"
type: "gene"
col: 6361
ensembl_id: "ENSG00000139974"
name: "solute carrier family 38 member 6"
location: "14q23.1"
module: 64
arm: "+"
pooled_cpm: 54.99
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 18
n_dd_up_clean: 9
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# SLC38A6

*solute carrier family 38 member 6* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.54× (z +12.7, q 4e-34, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.543× (z -8.3, q 7e-14, down in 38 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.802× (z -4.2, q 0.002, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TYW3]] (+0.68, fdr 7e-06), [[ANKRD23]] (+0.67, fdr 7e-06), [[FTX]] (+0.65, fdr 1e-05); moves opposite to [[ACBD7]] (-0.50, fdr 4e-05), [[UGCG]] (-0.50, fdr 3e-05), [[FAM234A]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6361.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.54×** | +12.7 | 4e-34 | 44/48 (LoVo, NCI-H1573, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.57×** | +12.1 | 3e-31 | 42/48 (COLO 205, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.21×** | +10.8 | 7e-25 | 41/48 (NCI-H1573, LoVo, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.91×** | +8.8 | 2e-16 | 45/48 (C32, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.33×** | +5.5 | 5e-06 | 28/48 (NCI-H2347, LoVo, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +4.2 | 0.002 | 27/47 (C32, SW480, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.004 | 27/48 (H4, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.045 | 17/48 (COLO 205, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.054 | 24/49 (C32, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.073 | 23/47 (C32, RKO, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.26×** | +3.2 | 0.074 | 20/48 (C32, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6361.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.543×** | -8.3 | 7e-14 | 38/49 (SNU-1, Hs 766T, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.610×** | -6.5 | 3e-08 | 31/47 (Panc 03.27, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.660×** | -5.4 | 1e-05 | 27/43 (A-427, SNU-423, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.471×** | -5.4 | 1e-05 | 31/49 (Panc 03.27, NCI-H2030, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.683×** | -4.8 | 2e-04 | 28/45 (SNU-1, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~76% of this change | **0.722×** | -4.4 | 9e-04 | 32/48 (NCI-H1792, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.802×** | -4.2 | 0.002 | 27/48 (SNU-423, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.805×** | -4.2 | 0.002 | 26/48 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **0.756×** | -3.8 | 0.009 | 23/48 (PANC-1, KATO III, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.779×** | -3.4 | 0.035 | 22/48 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.771×** | -3.4 | 0.035 | 24/48 (MIA PaCa-2, hTERT-HPNE, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **0.628×** | -3.3 | 0.043 | 19/46 (SNU-1, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.778×** | -3.3 | 0.043 | 24/48 (NCI-H2030, A498, …) | rises with dose | composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.786×** | -3.3 | 0.043 | 23/47 (MIA PaCa-2, A-172, …) | two highest doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.790×** | -3.2 | 0.050 | 18/47 (H4, MIA PaCa-2, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.731×** | -3.0 | 0.078 | 16/48 (SK-MEL-2, NCI-H1792, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.660×** | -3.0 | 0.099 | 21/48 (MIA PaCa-2, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6361. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 31.5 | 6 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.39× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[NCI-H1573 (line)]] | alt | 64.0 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.81× (z +13.8) | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -11.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 59.7 | 4 | 0 | [[Auranofin (drug)]] 5 µM 4.69× (z +12.2) | — |
| [[NCI-H23 (line)]] | alt | 99.1 | 2 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.73× (z +9.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.404× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 45.4 | 1 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.02× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A549 (line)]] | wt | 46.6 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.67× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 49.7 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 6.66× (z +12.4) | — |
| [[HepG2_C3A (line)]] | wt | 35.3 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.98× (z +9.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.151× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 52.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.15× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 134 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.393× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 59.7 | 2 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.71× (z +10.0) | [[Docetaxel (drug)]] 0.05 µM 0.342× (z -8.9) ⚠ transcription drop; cell-cycle shift, explains ~76% of this change |
| [[NCI-H460 (line)]] | wt | 64.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.26× (z +12.1) | — |
| [[PANC-1 (line)]] | alt | 38.5 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.323× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[SNU-1 (line)]] | wt | 66.6 | 1 | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.95× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 109 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW480 (line)]] | alt | 46.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.57× (z +10.8) | — |
| [[A-172 (line)]] | wt | 46.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[AN3 CA (line)]] | alt | 90.9 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0903× (z -10.3) ⚠ toxic |
| [[BT-474 (line)]] | alt | 26.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.01× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 46.2 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.16× (z +10.6) | — |
| [[KATO III (line)]] | alt | 35.8 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.81× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.341× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[LS 180 (line)]] | wt | 24.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.54× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 34.9 | 1 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.68× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -9.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 74.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[Hs 766T (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HT-29 (line)]] | alt | 27.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.12× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 75.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -11.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 84.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 51.4 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.48× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 70.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.307× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[RKO (line)]] | wt | 52.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 83.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.345× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~76% of this change |
| [[SHP-77 (line)]] | alt | 50.3 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.50× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 48.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A498 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6361), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYW3]] | +0.68 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[ANKRD23]] | +0.67 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[FTX]] | +0.65 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[BABAM1]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[COA6]] | +0.62 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[PSMB4]] | +0.62 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[SLC25A17]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[RHBDD3]] | +0.61 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[LINC01278]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[PSMB5]] | +0.61 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[DNAJC7]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[GATB]] | +0.61 | +0.51 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACBD7]] | -0.50 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[UGCG]] | -0.50 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[FAM234A]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[LFNG]] | -0.49 | -0.43 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers SLC38A6's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.687). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-16.6, -9.1); signed map (-25.8, -25.6). **Vector** length 117, 35.6% of its response variance represented; |z| ≥ 3 in 1,142 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Vif-mediated degradation of APOBEC3G* (reactome, mean cos +0.51 to 9); *Hedgehog 'on' state* (reactome, mean cos +0.51 to 10); *Regulation of activated PAK-2p34 by proteasome mediated degradation* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +12.7 | +10.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +12.7 | +12.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +12.5 | +12.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +10.8 | +8.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +5.1 | +5.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.9 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +2.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.4 | -4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | -1.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | +0.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | +0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.9 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 38 member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.1 — chr14:60,981,114-61,114,316 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NAT-1, SNAT6 |
| Gene groups (HGNC) | Solute carrier family 38 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZM9](https://www.uniprot.org/uniprotkb/Q8IZM9) (Solute carrier family 38 member 6):

> Amino acid transporter with an apparent selectivity for L-glutamine and L-glutamate. May facilitate glutamine uptake in excitatory neurons. The transport mechanism remains to be elucidated.

**Summary**, from NCBI Gene [145389](https://www.ncbi.nlm.nih.gov/gene/145389):

> Predicted to enable L-glutamate transmembrane transporter activity and L-glutamine transmembrane transporter activity. Predicted to be involved in L-glutamine transport and amino acid transmembrane transport. Predicted to be located in membrane and synapse. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19863](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19863) · Entrez [145389](https://www.ncbi.nlm.nih.gov/gene/145389) · UniProt [Q8IZM9](https://www.uniprot.org/uniprotkb/Q8IZM9) · Ensembl [ENSG00000139974](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139974)

## Data

Gene col 6361: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6361); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6361, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6361]; `tensor/DDL_lfc|DDL_z.npy` [6361]; `embed/gene_vectors.npy` [6361]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6361 or target_col == 6361). Every well: [[SLC38A6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC38A6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
