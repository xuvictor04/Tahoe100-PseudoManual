---
symbol: "CHAMP1"
type: "gene"
col: 12692
ensembl_id: "ENSG00000198824"
name: "chromosome alignment maintaining phosphoprotein 1"
location: "13q34"
module: 16
arm: "+"
pooled_cpm: 18.47
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# CHAMP1

*chromosome alignment maintaining phosphoprotein 1* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.00× (z +25.4, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.648× (z -5.3, q 5e-05, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADO]] (+0.71, fdr 7e-06), [[PYM1]] (+0.71, fdr 7e-06), [[ZNF816]] (+0.68, fdr 7e-06); moves opposite to [[FTL]] (-0.68, fdr 7e-06), [[KDELR1]] (-0.63, fdr 7e-06), [[ALDH2]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ZNF239]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12692.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.00×** | +25.4 | 0e+00 | 44/46 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.43×** | +16.0 | 0e+00 | 44/46 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.47×** | +15.5 | 0e+00 | 44/46 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.57×** | +12.2 | 3e-32 | 44/48 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.42×** | +11.5 | 2e-28 | 42/47 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.41×** | +11.4 | 3e-28 | 45/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +9.9 | 5e-21 | 34/43 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.13×** | +9.8 | 6e-21 | 43/47 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.50×** | +7.4 | 1e-11 | 35/46 (PANC-1, KATO III, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +6.1 | 7e-08 | 28/47 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.59×** | +6.0 | 9e-08 | 27/47 (J82, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +5.7 | 7e-07 | 27/48 (J82, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.14×** | +5.2 | 1e-05 | 26/47 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +4.9 | 3e-05 | 20/47 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.8 | 5e-05 | 23/48 (SW480, RKO, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.002 | 18/48 (HOP62, J82, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.032 | 11/46 (NCI-H2347, NCI-H1573, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.0 | 0.058 | 10/48 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +2.9 | 0.083 | 6/48 (HT-29, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12692.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.648×** | -5.3 | 5e-05 | 28/47 (Hs 766T, LoVo, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.699×** | -4.7 | 9e-04 | 23/47 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.567×** | -3.9 | 0.017 | 19/38 (LoVo, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.661×** | -3.9 | 0.017 | 18/48 (SW480, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Clotrimazole (drug)]] 5 µM |  | **0.818×** | -3.7 | 0.023 | 13/48 (H4, Panc 03.27, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.758×** | -3.6 | 0.029 | 20/47 (A498, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12692. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 50.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +11.8) | — |
| [[A549 (line)]] | wt | 15.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +15.6) | — |
| [[HEC-1-A (line)]] | alt | 19.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +14.2) | — |
| [[NCI-H1573 (line)]] | alt | 17.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.90× (z +15.8) | — |
| [[NCI-H460 (line)]] | wt | 16.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +14.2) | — |
| [[A-172 (line)]] | wt | 17.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 15.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.120× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 25.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +18.1) | — |
| [[Panc 03.27 (line)]] | alt | 15.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +12.4) | — |
| [[PANC-1 (line)]] | alt | 14.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +13.9) | — |
| [[A-427 (line)]] | wt | 36.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.266× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[BT-474 (line)]] | alt | 21.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +13.5) | — |
| [[C32 (line)]] | wt | 21.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +11.4) | — |
| [[HOP62 (line)]] | alt | 12.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.83× (z +15.2) | — |
| [[Hs 766T (line)]] | wt | 16.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +14.3) | — |
| [[LS 180 (line)]] | wt | 14.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +13.0) | — |
| [[NCI-H2347 (line)]] | alt | 8.67 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +13.5) | — |
| [[AsPC-1 (line)]] | alt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 7.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.15× (z +12.9) | — |
| [[COLO 205 (line)]] | alt | 8.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +9.6) | — |
| [[HCT15 (line)]] | alt | 28.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.57× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +13.1) | — |
| [[NCI-H2030 (line)]] | alt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 24.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +14.2) | — |
| [[RPMI-7951 (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 41.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 28.3 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.24× (z +10.3) | — |
| [[SW 900 (line)]] | alt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +11.2) | — |
| [[A498 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12692), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADO]] | +0.71 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[PYM1]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ZNF816]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 | same gene group |
| [[TRMT5]] | +0.66 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[UMPS]] | +0.65 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[DDX20]] | +0.65 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[POLR2D]] | +0.65 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[POLI]] | +0.64 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[MRM2]] | +0.63 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[ZNF510]] | +0.63 | +0.72 / +0.56 | both halves | 1e-05 | same gene group |
| [[ZKSCAN2]] | +0.63 | +0.68 / +0.57 | both halves | 1e-05 | same gene group |
| [[ZNF620]] | +0.63 | +0.68 / +0.60 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FTL]] | -0.68 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[KDELR1]] | -0.63 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[ALDH2]] | -0.62 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[SNX3]] | -0.62 | -0.67 / -0.59 | both halves | 7e-06 |  |
| [[RTN3]] | -0.62 | -0.71 / -0.41 | both halves | 4e-05 |  |
| [[UBE4B]] | -0.61 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[BCO2]] | -0.61 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[HSPA1B]] | -0.59 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[RAB6A]] | -0.59 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[TALAM1]] | -0.58 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[ST13]] | -0.58 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[RPS20]] | -0.57 | -0.57 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF239]] | B | ZNF239 activity lowers CHAMP1's level | lines that do not express ZNF239 (8) vs lines expressing it (42) | 1.60× higher at baseline in the lines without ZNF239 | 0.015 | ⚠ within organs, on part of the lines |
| [[RPL39L]] | B | RPL39L activity lowers CHAMP1's level | lines that do not express RPL39L (16) vs lines expressing it (34) | 1.50× higher at baseline in the lines without RPL39L | 0.026 | ⚠ within organs, on part of the lines; also absent: ANKRD6, RNF150, EVL |
| [[TOP2A]] | B | TOP2A activity lowers CHAMP1's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises CHAMP1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PTP4A3]] | B | PTP4A3 activity raises CHAMP1's level | lines that do not express PTP4A3 (7) vs lines expressing it (43) | 1.72× lower at baseline in the lines without PTP4A3 | 0.046 | ⚠ within organs, on part of the lines; also absent: RHOF, RHPN1, JAG2; maybe low, not absent |
| [[WHRN]] | C | WHRN activity raises CHAMP1's level | lines that do not express WHRN (4) vs lines expressing it (46) | 1.44× lower at baseline in the lines without WHRN | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, NKAIN1, KIAA1549; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.656). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-35.5, 13.9); signed map (3.2, -37.2). **Vector** length 95.1, 22.6% of its response variance represented; |z| ≥ 3 in 1,120 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.3 | +16.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.9 | +11.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.4 | +15.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +25.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.6 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.5 | +6.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.3 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +2.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.2 | +3.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -6.2 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.9 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.3 | -3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.1 | -3.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.7 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -1.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.1 | -2.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | chromosome alignment maintaining phosphoprotein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:114,314,482-114,337,626 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAMP, CHAMP; previously C13orf8, ZNF828 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JM3](https://www.uniprot.org/uniprotkb/Q96JM3) (Chromosome alignment-maintaining phosphoprotein 1):

> Required for proper alignment of chromosomes at metaphase and their accurate segregation during mitosis. Involved in the maintenance of spindle microtubules attachment to the kinetochore during sister chromatid biorientation. May recruit CENPE and CENPF to the kinetochore.

**Summary**, from NCBI Gene [283489](https://www.ncbi.nlm.nih.gov/gene/283489):

> This gene encodes a zinc finger protein that functions as a regulator of chromosome segregation in mitosis. The encoded protein is required for correct alignment of chromosomes on the metaphase plate, and plays a role in maintaining the attachment of sister kinetochores to microtubules from opposite spindle poles. Mutations in this gene are associated with an autosomal dominant form of intellectual disability. [provided by RefSeq, Jul 2017]

**Accessions** — [HGNC:20311](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20311) · Entrez [283489](https://www.ncbi.nlm.nih.gov/gene/283489) · UniProt [Q96JM3](https://www.uniprot.org/uniprotkb/Q96JM3) · Ensembl [ENSG00000198824](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198824)

## Data

Gene col 12692: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12692); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12692, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12692]; `tensor/DDL_lfc|DDL_z.npy` [12692]; `embed/gene_vectors.npy` [12692]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12692 or target_col == 12692). Every well: [[CHAMP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHAMP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
