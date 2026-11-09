---
symbol: "MID1"
type: "gene"
col: 2183
ensembl_id: "ENSG00000101871"
name: "midline 1"
location: "Xp22.2"
module: 9
arm: "+"
pooled_cpm: 103.93
n_lines_expressing: 44
n_dd_up: 26
n_dd_down: 8
n_dd_up_clean: 24
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# MID1

*midline 1* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.64× (z +7.7, q 6e-12, up in 30 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.781× (z -5.7, q 6e-06, down in 27 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PBX1]] (+0.64, fdr 7e-06), [[EPHA5]] (+0.63, fdr 7e-06), [[SEMA3E]] (+0.63, fdr 1e-05); moves opposite to [[IL17RA]] (-0.56, fdr 1e-05), [[ARHGAP1]] (-0.51, fdr 1e-05), [[TBCCD1]] (-0.50, fdr 6e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[FUT9]] → it (grade B ⚠); 2 go from it, the strongest it → [[CERS5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2183.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.64×** | +7.7 | 6e-12 | 30/41 (J82, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.47×** | +6.2 | 2e-07 | 26/41 (A549, J82, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +5.7 | 1e-06 | 25/42 (NCI-H1792, J82, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.41×** | +5.7 | 1e-06 | 24/44 (A-427, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.39×** | +5.5 | 5e-06 | 26/43 (A-427, J82, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +5.0 | 4e-05 | 22/42 (BT-474, A-427, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +5.0 | 5e-05 | 21/42 (NCI-H1792, BT-474, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.34×** | +4.8 | 1e-04 | 19/42 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.6 | 2e-04 | 17/42 (SNU-423, J82, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.23×** | +4.6 | 2e-04 | 17/43 (SHP-77, HT-29, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +4.4 | 5e-04 | 21/42 (J82, NCI-H1573, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **1.32×** | +4.3 | 7e-04 | 17/37 (A549, PANC-1, …) | top dose only | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.32×** | +4.2 | 0.001 | 21/42 (A549, A-427, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.001 | 19/42 (A-172, C32, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +4.1 | 0.001 | 22/42 (BT-474, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.002 | 21/43 (NCI-H1573, J82, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2183.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **0.781×** | -5.7 | 6e-06 | 27/42 (KATO III, SHP-77, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.805×** | -5.0 | 2e-04 | 23/43 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.742×** | -4.9 | 2e-04 | 25/42 (A-427, J82, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.770×** | -4.1 | 0.005 | 20/40 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.619×** | -4.1 | 0.005 | 21/41 (HT-29, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.802×** | -3.6 | 0.030 | 14/42 (A498, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.804×** | -3.6 | 0.030 | 17/41 (SHP-77, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.806×** | -3.5 | 0.030 | 18/42 (SNU-423, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.862× | -3.4 | 0.037 | 20/42 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.873× | -3.1 | 0.097 | 11/43 (NCI-H1573, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2183. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 125 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -15.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -11.2) |
| [[A-427 (line)]] | wt | 655 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.312× (z -13.5) |
| [[LS 180 (line)]] | wt | 232 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.337× (z -11.8) |
| [[SNU-423 (line)]] | alt | 299 | 2 (1 ⚠) | 5 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.11× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -17.4) |
| [[C32 (line)]] | wt | 42.1 | 5 (4 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.82× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 9.37× (z +8.5) | — |
| [[J82 (line)]] | alt | 113 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +16.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.13× (z +11.0) | — |
| [[KATO III (line)]] | alt | 197 | 1 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.35× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 169 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -20.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.326× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 107 | 3 (2 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 3.15× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.76× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 211 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -16.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -14.9) |
| [[Hs 766T (line)]] | wt | 71.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 149 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 135 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +19.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HEC-1-A (line)]] | alt | 67.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.400× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 69.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 177 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -9.4) |
| [[NCI-H596 (line)]] | alt | 107 | 1 | 0 | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 3.73× (z +10.7) | — |
| [[NCI-H661 (line)]] | alt | 471 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -9.9) |
| [[A-172 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 97.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 81.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.8 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 24.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.9 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.4 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 63.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 183 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2183), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBX1]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[EPHA5]] | +0.63 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[SEMA3E]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[VAV3]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[NFIB]] | +0.59 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[LRP1B]] | +0.58 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ATF7IP]] | +0.58 | +0.59 / +0.58 | both halves | 7e-06 | same gene group |
| [[FIGN]] | +0.58 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[DIO2]] | +0.57 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[AKR1C3]] | +0.55 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[ERBB4]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[PCDH9]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL17RA]] | -0.56 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[ARHGAP1]] | -0.51 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[TBCCD1]] | -0.50 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[ZNF550]] | -0.49 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[TEP1]] | -0.49 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[ZNF25]] | -0.49 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[POLG]] | -0.48 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[KATNA1]] | -0.48 | -0.48 / -0.44 | both halves | 3e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[SEC14L2]] | -0.48 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[CRYGS]] | -0.48 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[MEIS3]] | -0.47 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[ZNF415]] | -0.47 | -0.32 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FUT9]] | B | FUT9 activity raises MID1's level | lines that do not express FUT9 (40) vs lines expressing it (10) | 2.46× lower at baseline in the lines without FUT9 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG |
| [[KLHL13]] | B | KLHL13 activity strengthens MID1's drug response | lines that do not express KLHL13 (19) vs lines expressing it (25) | the lines without KLHL13 respond 0.62× as strongly (z diff +1.34); strongest at Trametinib 5 µM: 1.21x vs 1.63x (z diff +2.4) | 0.059 | ⚠ within organs, on part of the lines; also absent: IQGAP2, ANKRD20A11P, MAPK4; target measured in part of the lines; artifact flags |
| [[FSTL5]] | B | FSTL5 activity raises MID1's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 1.88× lower at baseline in the lines without FSTL5 | 0.075 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2 |
| [[FUT9]] | B | FUT9 activity strengthens MID1's drug response | lines that do not express FUT9 (34) vs lines expressing it (10) | the lines without FUT9 respond 0.76× as strongly (z diff +1.81); strongest at Trametinib 5 µM: 1.33x vs 1.85x (z diff +3.2) | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, KCNH7, GCG; target measured in part of the lines; the reference differs; artifact flags |
| [[CSRNP3]] | B | CSRNP3 activity raises MID1's level | lines that do not express CSRNP3 (24) vs lines expressing it (26) | 1.73× lower at baseline in the lines without CSRNP3 | 0.093 | ⚠ within organs, on part of the lines; also absent: FAM149A, ENSG00000286133, VIPR2 |
| [[MAP2K1]] | B | MAP2K1 activity lowers MID1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CERS5]] | B | MID1 activity lowers CERS5's level | lines that do not express MID1 (6) vs lines expressing it (44) | 1.34× higher at baseline in the lines without MID1 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with NF1; also absent: TLE6, ENSG00000132832, ENSG00000243944; maybe low, not absent |
| [[CA8]] | B | MID1 activity raises CA8's level | lines that do not express MID1 (6) vs lines expressing it (44) | 4.04× lower at baseline in the lines without MID1 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with NF1; also absent: TLE6, ENSG00000132832, ENSG00000243944; maybe low, not absent |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.8, 33.2); signed map (49.0, 19.0). **Vector** length 124, 33.9% of its response variance represented; |z| ≥ 3 in 1,264 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +6.6 | +7.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.0 | +0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +5.8 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.6 | -0.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.5 | +1.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.1 | +4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.6 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +4.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.5 | +5.5 |
| fall | [[Artesunate (drug)]] 5 µM |  | -4.3 | -5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.1 | -3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.0 | -4.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.7 | -2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.4 | -1.9 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -2.7 | -3.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.6 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | midline 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:10,445,310-10,833,654 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OS, FXY, TRIM18, RNF59 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; Fibronectin type III domain containing; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 3 pathways, smallest: Interferon gamma signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [O15344](https://www.uniprot.org/uniprotkb/O15344) (E3 ubiquitin-protein ligase MID1):

> E3 ubiquitin-protein ligase that promotes the monoubiquitination of IGBP1, which results in deprotection of the catalytic subunit of protein phosphatase PP2A, and its subsequent degradation by polyubiquitination.

**Summary**, from NCBI Gene [4281](https://www.ncbi.nlm.nih.gov/gene/4281):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family, also known as the 'RING-B box-coiled coil' (RBCC) subgroup of RING finger proteins. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. This protein forms homodimers which associate with microtubules in the cytoplasm. The protein is likely involved in the formation of multiprotein structures acting as anchor points to microtubules. Mutations in …

**Accessions** — [HGNC:7095](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7095) · Entrez [4281](https://www.ncbi.nlm.nih.gov/gene/4281) · UniProt [O15344](https://www.uniprot.org/uniprotkb/O15344) · Ensembl [ENSG00000101871](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101871)

## Data

Gene col 2183: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2183); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2183, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2183]; `tensor/DDL_lfc|DDL_z.npy` [2183]; `embed/gene_vectors.npy` [2183]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2183 or target_col == 2183). Every well: [[MID1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MID1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
