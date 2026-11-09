---
symbol: "DKK2"
type: "gene"
col: 7861
ensembl_id: "ENSG00000155011"
name: "dickkopf Wnt signaling pathway inhibitor 2"
location: "4q25"
module: 75
arm: "+"
pooled_cpm: 3.16
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# DKK2

*dickkopf Wnt signaling pathway inhibitor 2* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.74× (z +24.8, q 0e+00, up in 21 of 23 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (SW480 0.0277×); [[Belinostat (drug)]] 5 µM in 1 line (SW480 0.0449×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 0.0494×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SW480 0.132×); [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.138×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRM8]] (+0.79, fdr 7e-06), [[LINC03042]] (+0.71, fdr 7e-06), [[LINC01226]] (+0.70, fdr 7e-06); moves opposite to [[STIMATE]] (-0.57, fdr 1e-04), [[ACAD8]] (-0.56, fdr 5e-04).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[PSG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7861.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.74×** | +24.8 | 0e+00 | 21/23 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.63×** | +11.9 | 2e-30 | 1/3 (CHP-212) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.83×** | +11.9 | 2e-30 | 18/27 (A-172, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.46×** | +10.1 | 1e-21 | 4/8 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.04×** | +9.0 | 2e-17 | 23/38 (NCI-H1792, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.91×** | +7.4 | 1e-11 | 18/40 (RPMI-7951, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.45×** | +7.2 | 3e-11 | 15/25 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.62×** | +7.2 | 4e-11 | 2/3 (CHP-212, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.75×** | +6.4 | 9e-09 | 9/41 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **2.12×** | +6.1 | 7e-08 | 13/34 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +5.0 | 3e-05 | 8/27 (HOP62, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +4.5 | 3e-04 | 3/17 (HEC-1-A, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +4.3 | 9e-04 | 8/31 (RPMI-7951, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.59×** | +3.7 | 0.008 | 2/10 (A-427, HOP62) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.029 | 6/37 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7861.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 1 line (SW480 0.0277×); [[Belinostat (drug)]] 5 µM in 1 line (SW480 0.0449×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 0.0494×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SW480 0.132×); [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.138×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | 0.643× | -3.6 | 0.11 | 9/30 (SW480, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.646× | -3.6 | 0.11 | 7/43 (NCI-H1792, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7861. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.4 | 0 | 9 (7 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0277× (z -16.2) |
| [[A-172 (line)]] | wt | 1.56 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.9× (z +9.2) | — |
| [[CHP-212 (line)]] | wt | 119 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 1.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.0× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 1.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 30.1× (z +12.0) | — |
| [[hTERT-HPNE (line)]] | wt | 2.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.1× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 1.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.8× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 1.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 0.829 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +8.7) | — |
| [[A-427 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.812 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.937 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.980 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.878 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.930 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.969 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.853 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.810 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.772 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.870 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.975 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.908 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.826 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7861), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRM8]] | +0.79 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[LINC03042]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[LINC01226]] | +0.70 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[NPAS3]] | +0.70 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[ADAMTS19]] | +0.70 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[ANGPT2]] | +0.68 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[LYPLAL1-AS1]] | +0.68 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[CACNA1E]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[LINC02254]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[KIF26B]] | +0.67 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[LINC00861]] | +0.67 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[HAS2-AS1]] | +0.67 | +0.64 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STIMATE]] | -0.57 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[ACAD8]] | -0.56 | -0.23 / -0.49 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSG1]] | B | PSG1 activity raises DKK2's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 2.01× lower at baseline in the lines without PSG1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB |
| [[ROBO2]] | B | ROBO2 activity raises DKK2's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 2.68× lower at baseline in the lines without ROBO2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205 |
| [[SLC25A24P1]] | B | SLC25A24P1 activity raises DKK2's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 1.81× lower at baseline in the lines without SLC25A24P1 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2 |
| [[TOP2A]] | B | TOP2A activity lowers DKK2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CSMD3]] | B | CSMD3 activity raises DKK2's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 2.26× lower at baseline in the lines without CSMD3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486 |
| [[LINC00491]] | B | LINC00491 activity raises DKK2's level | lines that do not express LINC00491 (33) vs lines expressing it (17) | 1.87× lower at baseline in the lines without LINC00491 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APCDD1L, LINC01905, ADGRG7 |
| [[JAKMIP2-AS1]] | B | JAKMIP2-AS1 activity raises DKK2's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 2.31× lower at baseline in the lines without JAKMIP2-AS1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[HS3ST5]] | B | HS3ST5 activity raises DKK2's level | lines that do not express HS3ST5 (29) vs lines expressing it (21) | 1.73× lower at baseline in the lines without HS3ST5 | 0.025 | ⚠ within organs, on part of the lines; also absent: NOL4, ESRRG, RUNX1T1; maybe low, not absent |
| [[ANO4]] | B | ANO4 activity raises DKK2's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 1.89× lower at baseline in the lines without ANO4 | 0.028 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent |
| [[SHISA9]] | B | SHISA9 activity raises DKK2's level | lines that do not express SHISA9 (38) vs lines expressing it (12) | 1.46× lower at baseline in the lines without SHISA9 | 0.032 | ⚠ within organs, on part of the lines; also absent: LHFPL3-AS1, S100A1, LINC01456; maybe low, not absent |
| [[LINC02466]] | B | LINC02466 activity raises DKK2's level | lines that do not express LINC02466 (21) vs lines expressing it (29) | 1.66× lower at baseline in the lines without LINC02466 | 0.072 | ⚠ within organs, on part of the lines; also absent: MME, ENSG00000227088, GABRA3; maybe low, not absent |
| [[LINC01980]] | B | LINC01980 activity raises DKK2's level | lines that do not express LINC01980 (22) vs lines expressing it (28) | 1.81× lower at baseline in the lines without LINC01980 | 0.077 | ⚠ within organs, on part of the lines; also absent: KCNMB2, LINC00698, PAPPA2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.9, 36.4); signed map (36.7, 18.4). **Vector** length 52.0, 7.42% of its response variance represented; |z| ≥ 3 in 941 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +24.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.9 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +6.4 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.0 | +3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.9 | -0.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.8 | -1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.3 | -1.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -2.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | dickkopf Wnt signaling pathway inhibitor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:106,921,802-107,283,806 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Dickkopf family |
| Reactome | 10 pathways, smallest: Signaling by LRP5 mutants; Negative regulation of TCF-dependent signaling by WNT ligand antagonists; CHD6, CHD7, CHD8, CHD9 subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBU2](https://www.uniprot.org/uniprotkb/Q9UBU2) (Dickkopf-related protein 2):

> Antagonizes canonical Wnt signaling by inhibiting LRP5/6 interaction with Wnt and by forming a ternary complex with the transmembrane protein KREMEN that promotes internalization of LRP5/6. DKKs play an important role in vertebrate development, where they locally inhibit Wnt regulated processes such as antero-posterior axial patterning, limb development, somitogenesis and eye formation. In the adult, Dkks are implicated in bone formation and bone disease, cancer and Alzheimer disease (By …

**Summary**, from NCBI Gene [27123](https://www.ncbi.nlm.nih.gov/gene/27123):

> This gene encodes a protein that is a member of the dickkopf family. The secreted protein contains two cysteine rich regions and is involved in embryonic development through its interactions with the Wnt signaling pathway. It can act as either an agonist or antagonist of Wnt/beta-catenin signaling, depending on the cellular context and the presence of the co-factor kremen 2. Activity of this protein is also modulated by binding to the Wnt co-receptor LDL-receptor related protein 6 (LRP6). …

**Accessions** — [HGNC:2892](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2892) · Entrez [27123](https://www.ncbi.nlm.nih.gov/gene/27123) · UniProt [Q9UBU2](https://www.uniprot.org/uniprotkb/Q9UBU2) · Ensembl [ENSG00000155011](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155011)

## Data

Gene col 7861: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7861); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7861, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7861]; `tensor/DDL_lfc|DDL_z.npy` [7861]; `embed/gene_vectors.npy` [7861]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7861 or target_col == 7861). Every well: [[DKK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DKK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
