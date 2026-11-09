---
symbol: "ADAMTS19"
type: "gene"
col: 7028
ensembl_id: "ENSG00000145808"
name: "ADAM metallopeptidase with thrombospondin type 1 motif 19"
location: "5q23.3"
module: 90
arm: "+"
pooled_cpm: 3.38
n_lines_expressing: 39
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 2
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# ADAMTS19

*ADAM metallopeptidase with thrombospondin type 1 motif 19* — 5q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.98× (z +21.2, q 0e+00, up in 16 of 18 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.152×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CHP-212 0.0912×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 0.243×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DKK2]] (+0.70, fdr 7e-06), [[ENTREP2]] (+0.66, fdr 7e-06), [[ENTPD1]] (+0.65, fdr 2e-05).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PSG1]] → it (grade B ⚠); 2 go from it, the strongest it → [[ADGRL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7028.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.98×** | +21.2 | 0e+00 | 16/18 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.15×** | +13.7 | 2e-40 | 4/7 (H4, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.31×** | +11.7 | 1e-29 | 1/3 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.87×** | +10.5 | 2e-23 | 1/3 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.00×** | +8.2 | 2e-14 | 15/29 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +8.0 | 1e-13 | 7/20 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.55×** | +7.5 | 4e-12 | 6/22 (NCI-H460, A498, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.42×** | +7.1 | 7e-11 | 5/12 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.05×** | +6.0 | 1e-07 | 6/26 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.93×** | +5.5 | 2e-06 | 7/21 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.81×** | +5.0 | 3e-05 | 3/20 (HOP62, CFPAC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.0 | 3e-05 | 2/31 (HEC-1-A, A498) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.67×** | +4.3 | 8e-04 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +3.9 | 0.003 | 0/7 | top dose only | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.64×** | +3.9 | 0.004 | 7/18 (LoVo, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +3.6 | 0.013 | 7/28 (NCI-H2030, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +3.4 | 0.020 | 5/30 (H4, LoVo, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +3.4 | 0.020 | 2/18 (HEC-1-A, NCI-H2030) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.68×** | +3.1 | 0.048 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.45×** | +3.1 | 0.048 | 3/15 (H4, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.152×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (CHP-212 0.0912×); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 0.243×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7028. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 107 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -10.7) |
| [[A498 (line)]] | wt | 1.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.2× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 0.988 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +9.6) | — |
| [[SW480 (line)]] | alt | 30.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -8.9) |
| [[A-172 (line)]] | wt | 0.888 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.782 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.766 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.874 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.979 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.847 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.872 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.943 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.858 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.883 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.923 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.842 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.702 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.782 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.913 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.827 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.845 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.928 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.890 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.811 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.976 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7028), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DKK2]] | +0.70 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[ENTREP2]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ENTPD1]] | +0.65 | +0.47 / +0.65 | both halves | 2e-05 | **novel candidate** |
| [[HS3ST5]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[RALYL]] | +0.63 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[ISM1]] | +0.63 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[OPCML]] | +0.62 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[CNBD1]] | +0.62 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[KIF26B]] | +0.62 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[HUNK]] | +0.61 | +0.56 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[LINC01980]] | +0.61 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[NCALD]] | +0.61 | +0.51 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSG1]] | B | PSG1 activity raises ADAMTS19's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 2.15× lower at baseline in the lines without PSG1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB |
| [[ROBO2]] | B | ROBO2 activity raises ADAMTS19's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 2.75× lower at baseline in the lines without ROBO2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205 |
| [[HS3ST5]] | B | HS3ST5 activity raises ADAMTS19's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.85× lower at baseline in the lines without HS3ST5 | 0.009 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |
| [[SLC25A24P1]] | B | SLC25A24P1 activity raises ADAMTS19's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 1.32× lower at baseline in the lines without SLC25A24P1 | 0.020 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2 |
| [[RUNX1T1]] | B | RUNX1T1 activity raises ADAMTS19's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.88× lower at baseline in the lines without RUNX1T1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4 |
| [[TOP2A]] | B | TOP2A activity lowers ADAMTS19's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NELL2]] | B | NELL2 activity raises ADAMTS19's level | lines that do not express NELL2 (28) vs lines expressing it (22) | 1.69× lower at baseline in the lines without NELL2 | 0.064 | ⚠ within organs, on part of the lines; also absent: SOX2, FREM2, PTH2R; maybe low, not absent |
| [[FGF13]] | B | FGF13 activity raises ADAMTS19's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 1.90× lower at baseline in the lines without FGF13 | 0.089 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11 |
| [[CSMD3]] | B | CSMD3 activity raises ADAMTS19's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 1.72× lower at baseline in the lines without CSMD3 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRL2]] | B | ADAMTS19 activity raises ADGRL2's level | lines that do not express ADAMTS19 (11) vs lines expressing it (39) | 3.02× lower at baseline in the lines without ADAMTS19 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000287943, FAM13C, ABCA12; maybe low, not absent |
| [[GRIP2]] | B | ADAMTS19 activity lowers GRIP2's level | lines that do not express ADAMTS19 (11) vs lines expressing it (39) | 1.62× higher at baseline in the lines without ADAMTS19 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000287943, FAM13C, ABCA12; maybe low, not absent |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.2, 36.7); signed map (36.5, 18.1). **Vector** length 34.4, 4.82% of its response variance represented; |z| ≥ 3 in 731 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +21.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +13.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +11.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.1 | +0.9 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase with thrombospondin type 1 motif 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.3 — chr5:129,460,281-129,738,683 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ADAM metallopeptidases with thrombospondin type 1 motif |
| Reactome | 6 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

UniProt [Q8TE59](https://www.uniprot.org/uniprotkb/Q8TE59) carries no function annotation.

**Summary**, from NCBI Gene [171019](https://www.ncbi.nlm.nih.gov/gene/171019):

> This gene encodes a member of the ADAMTS (a disintegrin and metalloproteinase with thrombospondin motif) protein family. Members of the family share several distinct protein modules, including a propeptide region, a metalloproteinase domain, a disintegrin-like domain, and a thrombospondin type 1 (TS) motif. Individual members of this family differ in the number of C-terminal TS motifs, and some have unique C-terminal domains. The protein encoded by this gene has high sequence similarity to the …

**Accessions** — [HGNC:17111](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17111) · Entrez [171019](https://www.ncbi.nlm.nih.gov/gene/171019) · UniProt [Q8TE59](https://www.uniprot.org/uniprotkb/Q8TE59) · Ensembl [ENSG00000145808](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145808)

## Data

Gene col 7028: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7028); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7028, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7028]; `tensor/DDL_lfc|DDL_z.npy` [7028]; `embed/gene_vectors.npy` [7028]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7028 or target_col == 7028). Every well: [[ADAMTS19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTS19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
