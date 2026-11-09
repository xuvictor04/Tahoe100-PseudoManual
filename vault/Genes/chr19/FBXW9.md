---
symbol: "FBXW9"
type: "gene"
col: 5267
ensembl_id: "ENSG00000132004"
name: "F-box and WD repeat domain containing 9"
location: "19p13.13"
module: 51
arm: "+"
pooled_cpm: 3.37
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# FBXW9

*F-box and WD repeat domain containing 9* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.52× (z +15.3, q 0e+00, up in 34 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.623× (z -7.8, q 3e-12, down in 23 of 45 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC41]] (+0.72, fdr 3e-05), [[TRMT1]] (+0.67, fdr 1e-05), [[POLR1C]] (+0.63, fdr 1e-05); moves opposite to [[HMGN3]] (-0.54, fdr 3e-05), [[HLTF]] (-0.54, fdr 1e-04), [[TMOD2]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5267.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.52×** | +15.3 | 0e+00 | 34/36 (BT-474, A549, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +7.8 | 2e-12 | 17/37 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +7.6 | 6e-12 | 14/21 (HS-578T, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +6.2 | 8e-08 | 9/37 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.2 | 2e-05 | 13/45 (RPMI-7951, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.57×** | +5.1 | 4e-05 | 12/33 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.54×** | +4.6 | 3e-04 | 1/8 (PANC-1) | all doses, flat | composition shift |
| [[Thymol (drug)]] 0.5 µM |  | **1.45×** | +4.3 | 0.001 | 5/32 (PANC-1, HS-578T, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +4.3 | 0.001 | 5/44 (HS-578T, SW1417, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.43×** | +4.0 | 0.003 | 2/5 (PANC-1, A498) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.41×** | +4.0 | 0.003 | 9/46 (LoVo, NCI-H1573, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +3.9 | 0.005 | 7/42 (SK-MEL-2, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +3.8 | 0.006 | 4/45 (NCI-H2030, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.38×** | +3.8 | 0.007 | 8/44 (HS-578T, HepG2/C3A, …) | rises with dose |  |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.39×** | +3.6 | 0.013 | 3/33 (HS-578T, PANC-1, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.035 | 3/30 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.036 | 5/39 (NCI-H1573, H4, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.69×** | +3.2 | 0.038 | 5/29 (MIA PaCa-2, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.62×** | +2.9 | 0.082 | 2/30 (A-427, A498) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.60×** | +2.9 | 0.092 | 1/32 (PANC-1) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5267.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.623×** | -7.8 | 3e-12 | 23/45 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.621×** | -5.6 | 7e-06 | 21/42 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.741×** | -3.5 | 0.081 | 8/45 (SW48, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.747×** | -3.4 | 0.091 | 8/44 (H4, NCI-H23, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5267. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.52 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0698× (z -10.0) |
| [[SHP-77 (line)]] | alt | 7.52 | 0 | 2 | — | [[Rapamycin (drug)]] 0.5 µM 0.0531× (z -11.8) |
| [[SK-MEL-2 (line)]] | alt | 5.56 | 0 | 2 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0828× (z -8.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Pyridoxine (drug)]] 0.5 µM 0.0992× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 3.03 | 0 | 1 | — | [[Fenofibrate (drug)]] 0.5 µM 0.0578× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 3.78 | 0 | 1 | — | [[Sildenafil (drug)]] 0.05 µM 0.0415× (z -8.9) |
| [[A-427 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5267), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC41]] | +0.72 | +0.45 / +0.68 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[TRMT1]] | +0.67 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[POLR1C]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[DUS2]] | +0.62 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[DHX37]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ARMC5]] | +0.59 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[LINS1]] | +0.58 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[PRCC]] | +0.58 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[RABL2A]] | +0.58 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[LANCL2]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[TNPO2]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 | ⚠ **readthrough risk**: this gene lies 2.6 kb 3′ of TNPO2 on the same strand (can correlate by spillover, not regulation) |
| [[KCNJ14]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[KIAA0753]] | +0.57 | +0.36 / +0.54 | both halves | 9e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGN3]] | -0.54 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[HLTF]] | -0.54 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[TMOD2]] | -0.54 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[SSX2IP]] | -0.53 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[RGS9]] | -0.53 | -0.36 / -0.52 | both halves | 9e-05 | pathway: Chaperonin-mediated protein folding |
| [[MOCS2]] | -0.51 | -0.16 / -0.52 | ⚠ one half (not replicated) | 0.001 |  |
| [[GDE1]] | -0.51 | -0.17 / -0.57 | ⚠ one half (not replicated) | 0.001 |  |
| [[SVIP]] | -0.49 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[SNPH]] | -0.49 | -0.18 / -0.49 | ⚠ not reproduced | 1e-03 |  |
| [[RADX]] | -0.49 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[PRKAR2B]] | -0.49 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[VWA5A]] | -0.48 | -0.20 / -0.50 | ⚠ not reproduced | 8e-04 |  |
| [[TMEM170B]] | -0.48 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[SPAG9]] | -0.48 | -0.45 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises FBXW9's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[TOP2A]] | B | TOP2A activity lowers FBXW9's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HLTF]] | B | HLTF activity raises FBXW9's level | lines that do not express HLTF (8) vs lines expressing it (42) | 1.40× lower at baseline in the lines without HLTF | 0.045 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.216). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-50.0, 11.8); signed map (9.7, -43.3). **Vector** length 46.5, 5.15% of its response variance represented; |z| ≥ 3 in 957 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +15.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +7.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.5 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +5.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.1 | +4.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.6 | +3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.3 | +2.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.2 | +2.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.1 | +2.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.2 | -5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.7 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.0 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | F-box and WD repeat domain containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,688,053-12,696,631 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10870, Fbw9, MEC-15 |
| Gene groups (HGNC) | WD repeat domain containing; F-box and WD repeat domain containing |
| Reactome | 7 pathways, smallest: Association of TriC/CCT with target proteins during biosynthesis; Chaperonin-mediated protein folding; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5XUX1](https://www.uniprot.org/uniprotkb/Q5XUX1) (F-box/WD repeat-containing protein 9):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex.

**Summary**, from NCBI Gene [84261](https://www.ncbi.nlm.nih.gov/gene/84261):

> Members of the F-box protein family, such as FBXW9, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (MIM 601434), cullin (see CUL1; MIM 603034), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:28136](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28136) · Entrez [84261](https://www.ncbi.nlm.nih.gov/gene/84261) · UniProt [Q5XUX1](https://www.uniprot.org/uniprotkb/Q5XUX1) · Ensembl [ENSG00000132004](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132004)

## Data

Gene col 5267: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5267); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5267, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5267]; `tensor/DDL_lfc|DDL_z.npy` [5267]; `embed/gene_vectors.npy` [5267]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5267 or target_col == 5267). Every well: [[FBXW9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXW9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
