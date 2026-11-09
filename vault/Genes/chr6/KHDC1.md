---
symbol: "KHDC1"
type: "gene"
col: 5678
ensembl_id: "ENSG00000135314"
name: "KH domain containing 1"
location: "6q13"
module: 15
arm: "+"
pooled_cpm: 16.13
n_lines_expressing: 35
n_dd_up: 9
n_dd_down: 21
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# KHDC1

*KH domain containing 1* — 6q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +14.8, q 0e+00, up in 26 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.506× (z -12.7, q 6e-34, down in 16 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.684× (z -7.3, q 2e-11, down in 17 of 32 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCOLCE2]] (+0.55, fdr 5e-05), [[FGD1]] (+0.55, fdr 3e-05), [[PHTF1]] (+0.54, fdr 2e-05); moves opposite to [[ZBTB20]] (-0.56, fdr 8e-05), [[TMEM14C]] (-0.54, fdr 6e-05), [[SNX12]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[IFTAP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5678.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +14.8 | 0e+00 | 26/32 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.42×** | +9.6 | 3e-19 | 21/33 (J82, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +8.6 | 1e-15 | 16/30 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.39×** | +6.1 | 1e-07 | 14/29 (HOP62, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +5.8 | 7e-07 | 17/32 (SNU-423, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.29×** | +5.0 | 6e-05 | 10/32 (NCI-H2347, J82, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +4.0 | 0.006 | 11/32 (NCI-H2347, J82, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.9 | 0.007 | 9/33 (A-427, SNU-423, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.21×** | +3.7 | 0.013 | 9/33 (J82, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.20×** | +3.6 | 0.017 | 6/33 (CFPAC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.082 | 4/31 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.082 | 6/32 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5678.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.506×** | -12.7 | 6e-34 | 16/20 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.516×** | -12.3 | 3e-32 | 24/32 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.614×** | -9.4 | 9e-19 | 21/27 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.621×** | -8.8 | 1e-16 | 19/28 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.637×** | -8.7 | 3e-16 | 22/33 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.676×** | -7.5 | 4e-12 | 19/30 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.684×** | -7.3 | 2e-11 | 17/32 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.708×** | -6.7 | 2e-09 | 15/32 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.794×** | -6.3 | 2e-08 | 15/32 (PANC-1, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.760×** | -5.3 | 7e-06 | 15/33 (Panc 03.27, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.761×** | -5.3 | 7e-06 | 14/32 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **0.772×** | -5.0 | 3e-05 | 13/28 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.799×** | -4.3 | 7e-04 | 14/32 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.804×** | -4.2 | 0.001 | 12/33 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.739×** | -4.2 | 0.001 | 11/31 (Hs 766T, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.805×** | -4.0 | 0.002 | 11/31 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.820×** | -3.7 | 0.007 | 11/30 (C-33 A, SW 900, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.821×** | -3.6 | 0.008 | 5/32 (KATO III, RPMI-7951, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.841× | -3.3 | 0.024 | 11/32 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | 0.848× | -3.2 | 0.040 | 5/32 (SW 900, AN3 CA, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.733×** | -3.1 | 0.044 | 9/28 (J82, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.800×** | -3.1 | 0.052 | 6/31 (SW 1088, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5678. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 21.2 | 1 | 8 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +11.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -13.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.273× (z -12.3) |
| [[PANC-1 (line)]] | alt | 35.4 | 1 | 6 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -15.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 35.5 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +8.9) | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 20.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 30.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -13.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 15.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.291× (z -10.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 8.10 | 0 | 2 | — | [[Flumatinib (mesylate) (drug)]] 5 µM 0.0755× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 26.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 48.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -17.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 9.35 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0589× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 20.6 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.117× (z -10.7) |
| [[HOP62 (line)]] | alt | 22.3 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -8.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0757× (z -14.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 33.0 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.99× (z +8.6) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[KATO III (line)]] | alt | 9.77 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.118× (z -11.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H2030 (line)]] | alt | 32.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 44.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.347× (z -9.0) |
| [[SW 900 (line)]] | alt | 13.4 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0544× (z -14.0) |
| [[A549 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.51 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5678), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCOLCE2]] | +0.55 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[FGD1]] | +0.55 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[PHTF1]] | +0.54 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[DBR1]] | +0.54 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[GLUD1P3]] | +0.53 | +0.39 / +0.45 | both halves | 6e-05 |  |
| [[SYCE1L]] | +0.53 | +0.36 / +0.55 | both halves | 1e-04 |  |
| [[ZNF418]] | +0.52 | +0.30 / +0.56 | both halves | 2e-04 |  |
| [[SYCE2]] | +0.52 | +0.30 / +0.54 | both halves | 2e-04 |  |
| [[KCNG3]] | +0.52 | +0.33 / +0.54 | both halves | 1e-04 |  |
| [[PKN3]] | +0.51 | +0.27 / +0.44 | both halves | 3e-04 |  |
| [[ZNF668]] | +0.51 | +0.30 / +0.43 | both halves | 2e-04 |  |
| [[ZNF816-ZNF321P]] | +0.50 | +0.31 / +0.61 | both halves | 2e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB20]] | -0.56 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[TMEM14C]] | -0.54 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[SNX12]] | -0.52 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[USP9X]] | -0.50 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[TEX261]] | -0.50 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[POLR2E]] | -0.49 | -0.25 / -0.39 | both halves | 4e-04 |  |
| [[PIP4P1]] | -0.49 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[PABIR1]] | -0.49 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[PNPLA2]] | -0.48 | -0.25 / -0.42 | both halves | 4e-04 |  |
| [[MOSPD2]] | -0.47 | -0.39 / -0.29 | both halves | 2e-04 |  |
| [[BCL7B]] | -0.47 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[CIAO1]] | -0.47 | -0.31 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFTAP]] | B | KHDC1 activity raises IFTAP's level | lines that do not express KHDC1 (15) vs lines expressing it (35) | 1.28× lower at baseline in the lines without KHDC1 | 0.089 | ⚠ within organs, on part of the lines; also absent: KHDC1-AS1, MAP9, C15orf48 |
| [[BCL7B]] | B | KHDC1 activity lowers BCL7B's level | lines that do not express KHDC1 (15) vs lines expressing it (35) | 1.08× higher at baseline in the lines without KHDC1 | 0.093 | ⚠ within organs, on part of the lines; also absent: KHDC1-AS1, MAP9, C15orf48 |
| [[TMEM171]] | B | KHDC1 activity raises TMEM171's level | lines that do not express KHDC1 (15) vs lines expressing it (35) | 1.90× lower at baseline in the lines without KHDC1 | 0.093 | ⚠ within organs, on part of the lines; also absent: KHDC1-AS1, MAP9, C15orf48 |
| [[ORC2]] | B | KHDC1 activity lowers ORC2's level | lines that do not express KHDC1 (15) vs lines expressing it (35) | 1.17× higher at baseline in the lines without KHDC1 | 0.095 | ⚠ within organs, on part of the lines; also absent: KHDC1-AS1, MAP9, C15orf48 |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.373). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.5, 19.3); signed map (3.7, -0.7). **Vector** length 67.7, 13.5% of its response variance represented; |z| ≥ 3 in 802 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +14.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | +4.4 | +6.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.7 | +9.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +3.5 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +3.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +1.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.1 | -12.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.7 | -4.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.5 | -5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.5 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | KH domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q13 — chr6:73,241,314-73,310,365 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10818, bA257K9.4, NDG1, Em:AC019205.8; previously C6orf148, C6orf147 |
| Matched by | ensembl_id |

UniProt [Q4VXA5](https://www.uniprot.org/uniprotkb/Q4VXA5) carries no function annotation.

**Summary**, from NCBI Gene [80759](https://www.ncbi.nlm.nih.gov/gene/80759):

> Predicted to enable identical protein binding activity and poly(U) RNA binding activity. Predicted to be located in membrane. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21366](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21366) · Entrez [80759](https://www.ncbi.nlm.nih.gov/gene/80759) · UniProt [Q4VXA5](https://www.uniprot.org/uniprotkb/Q4VXA5) · Ensembl [ENSG00000135314](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135314)

## Data

Gene col 5678: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5678); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5678, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5678]; `tensor/DDL_lfc|DDL_z.npy` [5678]; `embed/gene_vectors.npy` [5678]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5678 or target_col == 5678). Every well: [[KHDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KHDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
