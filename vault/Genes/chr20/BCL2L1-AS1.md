---
symbol: "BCL2L1-AS1"
type: "gene"
col: 14086
ensembl_id: "ENSG00000236559"
name: "BCL2L1 antisense RNA 1"
location: "20q11.21"
module: 141
arm: "+"
pooled_cpm: 10.77
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 29
direction_downstream: 0
tags: ["gene", "module/141"]
generated_by: "tahoemap"
---

# BCL2L1-AS1

*BCL2L1 antisense RNA 1* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.68× (z +6.9, q 3e-09, up in 19 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.25× (z +4.2, q 0.004, up in 12 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.845× (z -7.7, q 7e-12, down in 18 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.738× (z -5.6, q 5e-06, down in 20 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCL2L1]] (+0.70, fdr 7e-06, ⚠ same locus), [[EPHA2-AS1]] (+0.69, fdr 7e-06), [[B3GNT3]] (+0.64, fdr 7e-06), [[EPHA2]] (+0.63, fdr 7e-06); moves opposite to [[HOOK1]] (-0.45, fdr 1e-04).
> It is in [[Module 141]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 29 arrows point to it, the strongest [[TNS4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14086.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +6.9 | 3e-09 | 19/35 (NCI-H1573, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +6.1 | 2e-07 | 7/21 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +4.7 | 4e-04 | 12/30 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +4.3 | 0.002 | 17/41 (A498, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.2 | 0.004 | 12/47 (RKO, A498, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.77×** | +3.9 | 0.008 | 12/46 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.011 | 13/46 (SNU-423, NCI-H23, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.040 | 8/44 (BT-474, HS-578T, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14086.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.845× | -7.7 | 7e-12 | 18/48 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.738×** | -5.6 | 5e-06 | 20/44 (SK-MEL-2, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.681×** | -4.6 | 8e-04 | 17/47 (SW480, AsPC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.711×** | -4.5 | 0.001 | 18/48 (SW1417, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.719×** | -4.3 | 0.002 | 15/47 (CHP-212, SW480, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.727×** | -4.0 | 0.006 | 19/43 (SNU-423, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.777×** | -3.5 | 0.038 | 16/48 (HepG2/C3A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.814×** | -3.4 | 0.041 | 15/48 (NCI-H2347, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.766×** | -3.4 | 0.049 | 15/46 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.777×** | -3.3 | 0.053 | 16/46 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.786×** | -3.1 | 0.085 | 14/42 (H4, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.822× | -3.1 | 0.10 | 13/47 (CFPAC-1, KATO III, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14086. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 9.66 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0988× (z -11.9) |
| [[H4 (line)]] | wt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0900× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 15.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0989× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 7.84 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0630× (z -8.9) |
| [[KATO III (line)]] | alt | 17.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 5.54 | 0 | 1 | — | [[Ferulic acid (drug)]] 5 µM 0.0565× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 25.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -14.1) |
| [[SW1417 (line)]] | alt | 28.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -8.9) |
| [[SW480 (line)]] | alt | 16.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -8.5) |
| [[A-427 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14086), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL2L1]] | +0.70 | +0.70 / +0.71 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[EPHA2-AS1]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 | same gene group |
| [[B3GNT3]] | +0.64 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[EPHA2]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[LEMD1]] | +0.61 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SH2D3A]] | +0.59 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[ITGB4]] | +0.59 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[INPP5D]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[GJB3]] | +0.59 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[PADI1]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ARHGAP27P1-BPTFP1-KPNA2P3]] | +0.59 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[KIAA0040]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[LINC02320]] | +0.58 | +0.60 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOOK1]] | -0.45 | -0.48 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 29, C 0. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNS4]] | B | TNS4 activity raises BCL2L1-AS1's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 1.44× lower at baseline in the lines without TNS4 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[FOXQ1]] | B | FOXQ1 activity raises BCL2L1-AS1's level | lines that do not express FOXQ1 (30) vs lines expressing it (20) | 1.49× lower at baseline in the lines without FOXQ1 | 0.008 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[INAVA]], [[MROH3P]] | B | INAVA, MROH3P activity raises BCL2L1-AS1's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 1.47× lower at baseline in the lines without INAVA, MROH3P | 0.009 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[HSD17B2]] | B | HSD17B2 activity raises BCL2L1-AS1's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 1.53× lower at baseline in the lines without HSD17B2 | 0.010 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |
| [[PSORS1C1]] | B | PSORS1C1 activity raises BCL2L1-AS1's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 1.55× lower at baseline in the lines without PSORS1C1 | 0.010 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[C1orf116]] | B | C1orf116 activity raises BCL2L1-AS1's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 1.42× lower at baseline in the lines without C1orf116 | 0.010 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[TGFA]] | B | TGFA activity raises BCL2L1-AS1's level | lines that do not express TGFA (17) vs lines expressing it (33) | 1.42× lower at baseline in the lines without TGFA | 0.012 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[C6orf132]] | B | C6orf132 activity raises BCL2L1-AS1's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 1.42× lower at baseline in the lines without C6orf132 | 0.015 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1 |
| [[ITGB4]] | B | ITGB4 activity raises BCL2L1-AS1's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 1.38× lower at baseline in the lines without ITGB4 | 0.024 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[ALS2CL]] | B | ALS2CL activity raises BCL2L1-AS1's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 1.41× lower at baseline in the lines without ALS2CL | 0.024 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[MAP2K1]] | B | MAP2K1 activity raises BCL2L1-AS1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds |
| [[LINC02320]] | B | LINC02320 activity raises BCL2L1-AS1's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 1.42× lower at baseline in the lines without LINC02320 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 141]] — TNF-alpha signaling via NF-kB; 33 genes; every member is in the + arm (projection on the module's main direction 0.606). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.1, 51.5); signed map (4.3, 38.8). **Vector** length 67.7, 11.0% of its response variance represented; |z| ≥ 3 in 795 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.6 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +0.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.6 | -4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | BCL2L1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20q11.21 — chr20:31,686,216-31,716,825 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40095](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40095) · Entrez [105372589](https://www.ncbi.nlm.nih.gov/gene/105372589) · Ensembl [ENSG00000236559](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236559)

## Data

Gene col 14086: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14086); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14086, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14086]; `tensor/DDL_lfc|DDL_z.npy` [14086]; `embed/gene_vectors.npy` [14086]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14086 or target_col == 14086). Every well: [[BCL2L1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL2L1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
