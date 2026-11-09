---
symbol: "ARMC6"
type: "gene"
col: 2643
ensembl_id: "ENSG00000105676"
name: "armadillo repeat containing 6"
location: "19p13.11"
module: 5
arm: "+"
pooled_cpm: 6.27
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ARMC6

*armadillo repeat containing 6* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.15× (z +10.4, q 9e-23, up in 22 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 1.45× (z +5.1, q 4e-05, up in 18 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.533× (z -8.6, q 5e-15, down in 27 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR4]] (+0.86, fdr 7e-06), [[PUS1]] (+0.81, fdr 7e-06), [[GRWD1]] (+0.79, fdr 7e-06); moves opposite to [[KBTBD3]] (-0.71, fdr 7e-06), [[RIOK3]] (-0.68, fdr 7e-06), [[ZCRB1]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[AT7519 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2643.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +10.4 | 9e-23 | 22/29 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +9.5 | 6e-19 | 13/17 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.82×** | +8.2 | 6e-14 | 30/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +6.5 | 8e-09 | 6/11 (A498, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +5.1 | 4e-05 | 18/46 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +4.5 | 5e-04 | 10/46 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.5 | 5e-04 | 12/33 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.88×** | +4.5 | 5e-04 | 5/42 (NCI-H460, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +4.4 | 9e-04 | 11/47 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **1.32×** | +3.7 | 0.012 | 8/34 (RPMI-7951, NCI-H2347, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.64×** | +3.5 | 0.021 | 7/43 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.62×** | +3.5 | 0.025 | 3/42 (A498, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **1.30×** | +3.4 | 0.026 | 2/47 (NCI-H2030, NCI-H1792) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.27×** | +3.2 | 0.048 | 6/47 (NCI-H460, SW 900, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.064 | 6/45 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2643.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.533×** | -8.6 | 5e-15 | 27/45 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.616×** | -6.6 | 1e-08 | 23/47 (NCI-H2030, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.741×** | -5.8 | 1e-06 | 17/47 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.659×** | -5.7 | 2e-06 | 13/47 (A-172, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.758×** | -3.8 | 0.017 | 14/46 (SNU-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.766×** | -3.6 | 0.026 | 10/47 (NCI-H2030, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.606×** | -3.6 | 0.028 | 7/46 (SNU-1, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.722× | -3.2 | 0.11 | 4/40 (A498, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.852× | -3.1 | 0.13 | 14/42 (LoVo, NCI-H23, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.811× | -3.0 | 0.13 | 5/47 (MIA PaCa-2, A-427, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2643. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.24 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.128× (z -8.6) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 9.62 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.106× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 8.85 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0689× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 7.16 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0885× (z -9.2) |
| [[SW480 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -8.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 9.87 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2643), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR4]] | +0.86 | +0.85 / +0.82 | both halves | 7e-06 |  |
| [[PUS1]] | +0.81 | +0.80 / +0.77 | both halves | 7e-06 |  |
| [[GRWD1]] | +0.79 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[WDR77]] | +0.78 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.77 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[DHX37]] | +0.77 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[CTPS1]] | +0.76 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[GNL3L]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[PFAS]] | +0.75 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.74 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[TRNT1]] | +0.74 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[LETM1]] | +0.74 | +0.73 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KBTBD3]] | -0.71 | -0.64 / -0.67 | both halves | 7e-06 |  |
| [[RIOK3]] | -0.68 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[ZCRB1]] | -0.67 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[AFTPH]] | -0.66 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[MXI1]] | -0.66 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[UBE2B]] | -0.65 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[AKAP1-DT]] | -0.65 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[VPS37D]] | -0.62 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[KDM5B]] | -0.62 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[MTIF3]] | -0.62 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[MINDY2]] | -0.61 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[KDM3A]] | -0.61 | -0.46 / -0.60 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ARMC6's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ARMC6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GBX2-AS1]] | B | GBX2-AS1 activity raises ARMC6's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 1.22× lower at baseline in the lines without GBX2-AS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B |
| [[DDIT4]] | C | DDIT4 activity lowers ARMC6's level | lines that do not express DDIT4 (3) vs lines expressing it (47) | 1.73× higher at baseline in the lines without DDIT4 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, TIMP1, UGDH; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[AT7519 (drug)]] 5 µM | C | ARMC6's natural level lowers the cells' numbers under AT7519 5 µM (makes them more sensitive) | ARMC6's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64 | 0.390 over the table, 0.077 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.799). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.9, -34.4); signed map (-1.3, -47.1). **Vector** length 65.9, 9.83% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.63 to 13); *rRNA processing* (reactome, mean cos +0.56 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.56 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +8.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +10.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +4.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.6 | -8.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.7 | -6.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | armadillo repeat containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:19,033,575-19,060,311 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC19595 |
| Gene groups (HGNC) | Armadillo repeat containing |
| Matched by | ensembl_id |

UniProt [Q6NXE6](https://www.uniprot.org/uniprotkb/Q6NXE6) carries no function annotation.

**Summary**, from NCBI Gene [93436](https://www.ncbi.nlm.nih.gov/gene/93436):

> The function of this gene's protein product has not been determined. A related protein in mouse suggests that this protein has a conserved function. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:25049](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25049) · Entrez [93436](https://www.ncbi.nlm.nih.gov/gene/93436) · UniProt [Q6NXE6](https://www.uniprot.org/uniprotkb/Q6NXE6) · Ensembl [ENSG00000105676](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105676)

## Data

Gene col 2643: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2643); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2643, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2643]; `tensor/DDL_lfc|DDL_z.npy` [2643]; `embed/gene_vectors.npy` [2643]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2643 or target_col == 2643). Every well: [[ARMC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARMC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
