---
symbol: "RP1"
type: "gene"
col: 2432
ensembl_id: "ENSG00000104237"
name: "RP1 axonemal microtubule associated"
location: "8q11.23-q12.1"
module: 10
arm: "+"
pooled_cpm: 5.44
n_lines_expressing: 31
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# RP1

*RP1 axonemal microtubule associated* — 8q11.23-q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.03× (z +16.1, q 0e+00, up in 17 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.425× (z -8.8, q 7e-16, down in 21 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD31]] (+0.73, fdr 7e-06), [[AGA-DT]] (+0.72, fdr 2e-05), [[PCNX4-DT]] (+0.66, fdr 4e-05); moves opposite to [[RAB40B]] (-0.62, fdr 2e-05), [[DCUN1D2]] (-0.60, fdr 2e-05), [[MTM1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF655]] → it (grade B ⚠); 3 go from it, the strongest it → [[MTM1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2432.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.03×** | +16.1 | 0e+00 | 17/26 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.76×** | +10.4 | 6e-23 | 18/27 (Panc 03.27, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.80×** | +10.2 | 5e-22 | 1/7 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +9.3 | 2e-18 | 6/27 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.52×** | +8.8 | 2e-16 | 4/10 (CFPAC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.27×** | +8.4 | 4e-15 | 14/25 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +7.9 | 2e-13 | 5/18 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +6.7 | 1e-09 | 12/29 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.3 | 2e-08 | 4/29 (NCI-H2030, AsPC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +6.1 | 7e-08 | 11/27 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.80×** | +6.0 | 8e-08 | 3/28 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +5.5 | 2e-06 | 11/26 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +5.2 | 1e-05 | 11/28 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.56×** | +4.5 | 2e-04 | 10/27 (C32, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.33×** | +4.1 | 0.002 | 10/28 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.003 | 8/28 (HT-29, PANC-1, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.96×** | +3.6 | 0.010 | 3/20 (AsPC-1, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.45×** | +3.5 | 0.012 | 7/24 (C32, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.40×** | +3.5 | 0.016 | 3/26 (A549, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2432.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.425×** | -8.8 | 7e-16 | 21/28 (SNU-423, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.525×** | -6.6 | 8e-09 | 18/28 (SNU-423, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.557×** | -6.0 | 3e-07 | 14/28 (AsPC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.604×** | -5.2 | 3e-05 | 14/28 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.613×** | -5.0 | 5e-05 | 15/28 (HT-29, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.443×** | -4.4 | 0.001 | 11/28 (SW 900, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.705×** | -3.6 | 0.025 | 5/28 (NCI-H2030, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.541×** | -3.3 | 0.067 | 9/22 (hTERT-HPNE, LS 180, …) | rises with dose | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2432. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.58 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 26.2× (z +16.9) | [[Verapamil (drug)]] 5 µM 0.0553× (z -10.2) |
| [[AsPC-1 (line)]] | alt | 19.6 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0978× (z -10.9) |
| [[SNU-423 (line)]] | alt | 35.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0592× (z -15.5) |
| [[SW 900 (line)]] | alt | 37.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -10.4) |
| [[C32 (line)]] | wt | 27.2 | 1 | 1 | [[Harringtonine (drug)]] 0.5 µM 12.7× (z +9.6) | [[Belinostat (drug)]] 5 µM 0.110× (z -8.5) |
| [[SW480 (line)]] | alt | 3.05 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +10.4) | [[Digitoxin (drug)]] 0.5 µM 0.0426× (z -12.5) |
| [[Hs 766T (line)]] | wt | 2.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 2.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.61× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 4.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +8.8) | — |
| [[A-427 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.729 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.968 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.920 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.828 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.808 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.866 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.929 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2432), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD31]] | +0.73 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[AGA-DT]] | +0.72 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[PCNX4-DT]] | +0.66 | +0.66 / +0.41 | both halves | 4e-05 |  |
| [[LINC01933]] | +0.66 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[LINC00882]] | +0.63 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[HULC]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[IPCEF1]] | +0.63 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[GUCY1A2]] | +0.62 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[LINC03002]] | +0.62 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NEB]] | +0.62 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[LINC02516]] | +0.62 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ZBTB38]] | +0.62 | +0.64 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB40B]] | -0.62 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[DCUN1D2]] | -0.60 | -0.64 / -0.46 | both halves | 2e-05 |  |
| [[MTM1]] | -0.59 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[TMEM50B]] | -0.57 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[DHTKD1]] | -0.56 | -0.37 / -0.41 | both halves | 7e-05 |  |
| [[TRIM62]] | -0.55 | -0.53 / -0.37 | both halves | 7e-05 |  |
| [[SLC9A6]] | -0.55 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[RALGPS1]] | -0.55 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[PDXP]] | -0.54 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[GET1]] | -0.54 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[ATRN]] | -0.54 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[KMT5C]] | -0.54 | -0.46 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF655]] | B | ZNF655 activity lowers RP1's level | lines that do not express ZNF655 (7) vs lines expressing it (43) | 1.17× higher at baseline in the lines without ZNF655 | 0.068 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SRSF12 |
| [[HDAC6]] | B | HDAC6 activity raises RP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTM1]] | B | RP1 activity raises MTM1's level | lines that do not express RP1 (19) vs lines expressing it (31) | 1.45× lower at baseline in the lines without RP1 | 0.015 | ⚠ within organs, on part of the lines; also absent: CYB5R2, KIAA1549L, KCNN4; maybe low, not absent |
| [[TG]] | B | RP1 activity raises TG's level | lines that do not express RP1 (19) vs lines expressing it (31) | 1.27× lower at baseline in the lines without RP1 | 0.066 | ⚠ within organs, on part of the lines; also absent: CYB5R2, KIAA1549L, KCNN4; maybe low, not absent |
| [[SVEP1]] | B | RP1 activity raises SVEP1's level | lines that do not express RP1 (19) vs lines expressing it (31) | 1.67× lower at baseline in the lines without RP1 | 0.073 | ⚠ within organs, on part of the lines; also absent: CYB5R2, KIAA1549L, KCNN4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.600). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (19.0, 19.6); signed map (32.9, -10.2). **Vector** length 60.8, 12.3% of its response variance represented; |z| ≥ 3 in 749 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +16.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +10.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.1 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +4.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +3.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.7 | -6.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.1 | -6.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.6 | -8.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -4.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | RP1 axonemal microtubule associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q11.23-q12.1 — chr8:54,509,422-54,871,720 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DCDC4A, ORP1 |
| Gene groups (HGNC) | Doublecortin superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [P56715](https://www.uniprot.org/uniprotkb/P56715) (Oxygen-regulated protein 1):

> Microtubule-associated protein regulating the stability and length of the microtubule-based axoneme of photoreceptors. Required for the differentiation of photoreceptor cells, it plays a role in the organization of the outer segment of rod and cone photoreceptors ensuring the correct orientation and higher-order stacking of outer segment disks along the photoreceptor axoneme (By similarity).

**Summary**, from NCBI Gene [6101](https://www.ncbi.nlm.nih.gov/gene/6101):

> This gene encodes a member of the doublecortin family. The protein encoded by this gene contains two doublecortin domains, which bind microtubules and regulate microtubule polymerization. The encoded protein is a photoreceptor microtubule-associated protein and is required for correct stacking of outer segment disc. This protein and the RP1L1 protein, another retinal-specific protein, play essential and synergistic roles in affecting photosensitivity and outer segment morphogenesis of rod …

**Accessions** — [HGNC:10263](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10263) · Entrez [6101](https://www.ncbi.nlm.nih.gov/gene/6101) · UniProt [P56715](https://www.uniprot.org/uniprotkb/P56715) · Ensembl [ENSG00000104237](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104237)

## Data

Gene col 2432: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2432); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2432, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2432]; `tensor/DDL_lfc|DDL_z.npy` [2432]; `embed/gene_vectors.npy` [2432]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2432 or target_col == 2432). Every well: [[RP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
