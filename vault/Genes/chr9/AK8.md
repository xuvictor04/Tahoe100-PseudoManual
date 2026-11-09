---
symbol: "AK8"
type: "gene"
col: 9170
ensembl_id: "ENSG00000165695"
name: "adenylate kinase 8"
location: "9q34.13"
module: 10
arm: "+"
pooled_cpm: 4.86
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 15
n_dd_up_clean: 17
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# AK8

*adenylate kinase 8* — 9q34.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.10× (z +15.5, q 0e+00, up in 33 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.453× (z -7.6, q 1e-11, down in 27 of 43 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFCAB6]] (+0.73, fdr 7e-06), [[RABL2A]] (+0.68, fdr 7e-06), [[DRC3]] (+0.65, fdr 7e-06); moves opposite to [[KLHL8]] (-0.59, fdr 3e-05), [[POLR3G]] (-0.48, fdr 4e-05), [[MCOLN2]] (-0.47, fdr 4e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9170.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.10×** | +15.5 | 0e+00 | 33/35 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.57×** | +12.3 | 3e-32 | 44/45 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.48×** | +8.8 | 3e-16 | 34/45 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.41×** | +8.5 | 3e-15 | 32/44 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.49×** | +8.5 | 3e-15 | 3/7 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.70×** | +7.2 | 4e-11 | 26/46 (RKO, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.11×** | +7.2 | 4e-11 | 13/21 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +6.5 | 5e-09 | 17/37 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +6.0 | 9e-08 | 3/11 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +5.0 | 3e-05 | 15/32 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.65×** | +4.8 | 7e-05 | 17/43 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.49×** | +3.9 | 0.005 | 4/40 (A-172, NCI-H460, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.011 | 12/42 (SNU-1, PANC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.013 | 9/44 (SW480, LS 180, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.03×** | +3.6 | 0.013 | 6/41 (HT-29, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.020 | 1/40 (A-172) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.029 | 10/36 (SW480, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.033 | 9/37 (SW1417, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.038 | 5/46 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.044 | 7/42 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9170.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.453×** | -7.6 | 1e-11 | 27/43 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.464×** | -7.4 | 4e-11 | 24/34 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.485×** | -7.0 | 6e-10 | 23/46 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.559×** | -5.6 | 3e-06 | 17/41 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.746×** | -4.0 | 0.008 | 19/44 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.669×** | -3.7 | 0.016 | 10/45 (RPMI-7951, A549, …) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.670×** | -3.7 | 0.016 | 12/28 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.510×** | -3.4 | 0.048 | 16/41 (MIA PaCa-2, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.710×** | -3.3 | 0.061 | 13/44 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.705×** | -3.2 | 0.067 | 9/42 (PANC-1, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.721×** | -3.1 | 0.084 | 13/40 (SHP-77, C-33 A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.796×** | -3.1 | 0.085 | 9/43 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.725×** | -3.1 | 0.085 | 16/46 (CHP-212, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.729×** | -3.0 | 0.087 | 10/45 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.642×** | -3.0 | 0.087 | 8/45 (NCI-H460, NCI-H23, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9170. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 8.31 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.222× (z -8.8) |
| [[SW480 (line)]] | alt | 5.95 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.170× (z -9.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 5.56 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0846× (z -9.5) ⚠ toxic |
| [[A549 (line)]] | wt | 8.97 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.123× (z -9.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1573 (line)]] | alt | 4.29 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0858× (z -9.0) |
| [[A-172 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9170), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB6]] | +0.73 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[RABL2A]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[DRC3]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[RNF32]] | +0.64 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[LINC00663]] | +0.61 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[CFAP43]] | +0.60 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[FAM66C]] | +0.58 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[PIPOX]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[OSCP1]] | +0.57 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[DNAI7]] | +0.57 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[PSMG3-AS1]] | +0.56 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[CCDC191]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL8]] | -0.59 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[POLR3G]] | -0.48 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[MCOLN2]] | -0.47 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[RSAD1]] | -0.47 | -0.42 / -0.41 | both halves | 4e-05 | STRING 421 |
| [[WDR17]] | -0.46 | -0.02 / -0.50 | ⚠ one half (not replicated) | 0.007 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AK8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EFCAB6]] | B | EFCAB6 activity raises AK8's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 1.99× lower at baseline in the lines without EFCAB6 | 0.064 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.536). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (4.4, 20.5); signed map (30.2, -12.2). **Vector** length 53.8, 7.63% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +7.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +0.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.2 | +1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +1.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.5 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.2 | +3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -1.7 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | +3.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -3.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | adenylate kinase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.13 — chr9:132,725,578-132,878,777 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32704; previously C9orf98 |
| Gene groups (HGNC) | Adenylate kinases |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MA6](https://www.uniprot.org/uniprotkb/Q96MA6) (Adenylate kinase 8):

> Nucleoside monophosphate (NMP) kinase that catalyzes the reversible transfer of the terminal phosphate group between nucleoside triphosphates and monophosphates. Has highest activity toward AMP, and weaker activity toward dAMP, CMP and dCMP. Also displays broad nucleoside diphosphate kinase activity.

**Summary**, from NCBI Gene [158067](https://www.ncbi.nlm.nih.gov/gene/158067):

> Enables AMP binding activity and nucleobase-containing compound kinase activity. Predicted to be involved in nucleoside monophosphate phosphorylation. Predicted to act upstream of or within ventricular system development. Located in 9+2 motile cilium. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:26526](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26526) · Entrez [158067](https://www.ncbi.nlm.nih.gov/gene/158067) · UniProt [Q96MA6](https://www.uniprot.org/uniprotkb/Q96MA6) · Ensembl [ENSG00000165695](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165695)

## Data

Gene col 9170: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9170); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9170, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9170]; `tensor/DDL_lfc|DDL_z.npy` [9170]; `embed/gene_vectors.npy` [9170]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9170 or target_col == 9170). Every well: [[AK8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AK8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
