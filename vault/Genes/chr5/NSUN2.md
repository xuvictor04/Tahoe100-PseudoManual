---
symbol: "NSUN2"
type: "gene"
col: 442
ensembl_id: "ENSG00000037474"
name: "NOP2/Sun RNA methyltransferase 2"
location: "5p15.31"
module: 33
arm: "+"
pooled_cpm: 94.76
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 10
n_dd_up_clean: 19
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# NSUN2

*NOP2/Sun RNA methyltransferase 2* — 5p15.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.63× (z +13.8, q 2e-40, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.727× (z -4.7, q 8e-04, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[URB1]] (+0.80, fdr 7e-06), [[RNPS1]] (+0.77, fdr 7e-06), [[WDR3]] (+0.72, fdr 7e-06); moves opposite to [[GABARAP]] (-0.66, fdr 7e-06, ⚠ GABARAP in the vector space only through flagged drug-doses), [[MICU1]] (-0.63, fdr 7e-06), [[EIF1B]] (-0.63, fdr 7e-06), [[PNRC1]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 442.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.63×** | +13.8 | 2e-40 | 48/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.94×** | +12.7 | 9e-35 | 46/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.87×** | +9.5 | 3e-19 | 45/48 (CFPAC-1, NCI-H460, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +8.1 | 7e-14 | 37/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +6.3 | 5e-08 | 29/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.17×** | +6.2 | 5e-08 | 31/38 (NCI-H1573, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +6.2 | 5e-08 | 38/47 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +5.8 | 4e-07 | 41/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +5.7 | 7e-07 | 33/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.27×** | +5.1 | 2e-05 | 25/48 (A549, NCI-H460, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.81×** | +4.7 | 1e-04 | 34/48 (Hs 766T, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +4.6 | 2e-04 | 29/45 (NCI-H1792, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +4.6 | 2e-04 | 29/48 (HT-29, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.5 | 3e-04 | 26/48 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.34×** | +4.4 | 4e-04 | 28/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.50×** | +4.4 | 4e-04 | 31/48 (NCI-H460, NCI-H1792, …) | two highest doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.004 | 23/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.56×** | +3.6 | 0.012 | 23/48 (NCI-H1792, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.014 | 22/48 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +3.4 | 0.018 | 21/49 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.022 | 21/48 (LoVo, CFPAC-1, …) | all doses, flat |  |
| [[Volasertib (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.022 | 20/48 (SW480, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 442.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.727×** | -4.7 | 8e-04 | 28/47 (RKO, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.767×** | -4.7 | 8e-04 | 33/48 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.758×** | -4.3 | 0.004 | 26/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.753×** | -4.2 | 0.004 | 33/48 (LoVo, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.765×** | -4.1 | 0.005 | 29/48 (NCI-H23, H4, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.767×** | -4.1 | 0.005 | 29/49 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.712×** | -3.7 | 0.016 | 24/48 (HS-578T, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.843× | -3.6 | 0.022 | 16/49 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.811×** | -3.5 | 0.034 | 17/49 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.855× | -3.4 | 0.041 | 19/48 (SW480, HOP62, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.837× | -3.3 | 0.050 | 22/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.814×** | -3.2 | 0.075 | 21/48 (CHP-212, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.870× | -3.0 | 0.100 | 16/48 (J82, NCI-H2347, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.808×** | -3.0 | 0.100 | 20/47 (SW48, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 442. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 119 | 7 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.43× (z +13.4) | — |
| [[NCI-H1792 (line)]] | alt | 69.3 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.25× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 47.6 | 3 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.37× (z +10.6) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 66.9 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 18.3× (z +12.1) | — |
| [[HEC-1-A (line)]] | alt | 56.7 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.99× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 125 | 3 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.16× (z +9.7) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 95.4 | 3 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 7.89× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 43.6 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.64× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 84.9 | 3 (3 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.72× (z +10.4) ⚠ unreliable plate only | — |
| [[PANC-1 (line)]] | alt | 104 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.84× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 48.7 | 2 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.85× (z +9.2) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 7.02× (z +8.9) | — |
| [[KATO III (line)]] | alt | 43.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.77× (z +9.7) | — |
| [[LoVo (line)]] | wt | 116 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.05× (z +11.6) | — |
| [[LS 180 (line)]] | wt | 67.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.77× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 85.8 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.95× (z +9.9) | — |
| [[RKO (line)]] | wt | 132 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 7.19× (z +10.1) | — |
| [[A-427 (line)]] | wt | 136 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.82× (z +8.6) | — |
| [[A549 (line)]] | wt | 96.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +11.4) ⚠ cell-cycle shift, explains ~13% of this change | — |
| [[BT-474 (line)]] | alt | 112 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.49× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 76.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 85.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.23× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 95.2 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.27× (z +8.5) ⚠ unreliable plate only | — |
| [[NCI-H596 (line)]] | alt | 94.3 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.275× (z -8.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-1 (line)]] | wt | 97.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1088 (line)]] | alt | 110 | 0 | 1 | — | [[Talc (drug)]] 0.05 µM 0.0796× (z -9.6) |
| [[SW 1271 (line)]] | alt | 87.0 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0843× (z -10.3) |
| [[SW1417 (line)]] | alt | 116 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.21× (z +9.1) | — |
| [[SW48 (line)]] | wt | 96.7 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.53× (z +10.6) | — |
| [[A-172 (line)]] | wt | 64.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 175 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 63.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 81.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 125 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 442), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[URB1]] | +0.80 | +0.72 / +0.84 | both halves | 7e-06 |  |
| [[RNPS1]] | +0.77 | +0.78 / +0.77 | both halves | 7e-06 |  |
| [[WDR3]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 | STRING 458 |
| [[EIF3B]] | +0.72 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.72 | +0.74 / +0.65 | both halves | 7e-06 | STRING 635 |
| [[DCAF13]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[MTRR]] | +0.71 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[GCN1]] | +0.70 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[UTP18]] | +0.69 | +0.71 / +0.71 | both halves | 7e-06 | STRING 540 |
| [[BEND3]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[TRAP1]] | +0.69 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[WDR4]] | +0.68 | +0.59 / +0.73 | both halves | 7e-06 | pathway: tRNA modification in the nucleus and cytosol; STRING 794 |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABARAP]] ⚠ | -0.66 | -0.60 / -0.64 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[MICU1]] | -0.63 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[EIF1B]] | -0.63 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[PNRC1]] | -0.62 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[ANKRD12]] | -0.62 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[WBP4]] | -0.62 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[CHD2]] | -0.61 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[JUND]] | -0.61 | -0.58 / -0.69 | both halves | 7e-06 |  |
| [[DAAM1]] | -0.60 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[ATP6V0C]] | -0.60 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[GABARAPL2]] | -0.60 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[KMT2A]] | -0.59 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[GABARAPL1]] | -0.59 | -0.50 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises NSUN2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[MAP2K2]] | B | MAP2K2 activity raises NSUN2's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.675). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.3, -38.5); signed map (-6.1, -51.0). **Vector** length 94.8, 30.3% of its response variance represented; |z| ≥ 3 in 1,170 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.55 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.55 to 10); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.65 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +9.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +12.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.8 | +4.7 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +3.4 | +6.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.3 | +13.8 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.0 | +2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.8 | +3.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.8 | +8.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | +1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -5.1 | +4.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | +6.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.3 | +5.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.9 | -4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -3.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.4 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | NOP2/Sun RNA methyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.31 — chr5:6,599,239-6,633,291 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20303, TRM4, Misu, SAKI; previously MRT5 |
| Gene groups (HGNC) | NOP2/Sun RNA methyltransferase family; DNA/RNA methyltransferases |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08J23](https://www.uniprot.org/uniprotkb/Q08J23) (RNA cytosine C(5)-methyltransferase NSUN2):

> RNA cytosine C(5)-methyltransferase that methylates cytosine to 5-methylcytosine (m5C) in various RNAs, such as tRNAs, mRNAs and some long non-coding RNAs (lncRNAs). Involved in various processes, such as epidermal stem cell differentiation, testis differentiation and maternal to zygotic transition during early development: acts by increasing protein synthesis; cytosine C(5)-methylation promoting tRNA stability and preventing mRNA decay. Methylates cytosine to 5-methylcytosine (m5C) at …

**Summary**, from NCBI Gene [54888](https://www.ncbi.nlm.nih.gov/gene/54888):

> This gene encodes a methyltransferase that catalyzes the methylation of cytosine to 5-methylcytosine (m5C) at position 34 of intron-containing tRNA(Leu)(CAA) precursors. This modification is necessary to stabilize the anticodon-codon pairing and correctly translate the mRNA. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene.[provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:25994](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25994) · Entrez [54888](https://www.ncbi.nlm.nih.gov/gene/54888) · UniProt [Q08J23](https://www.uniprot.org/uniprotkb/Q08J23) · Ensembl [ENSG00000037474](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000037474)

## Data

Gene col 442: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 442); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 442, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 442]; `tensor/DDL_lfc|DDL_z.npy` [442]; `embed/gene_vectors.npy` [442]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 442 or target_col == 442). Every well: [[NSUN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSUN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
