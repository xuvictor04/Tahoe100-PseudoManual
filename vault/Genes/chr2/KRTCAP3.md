---
symbol: "KRTCAP3"
type: "gene"
col: 8121
ensembl_id: "ENSG00000157992"
name: "keratinocyte associated protein 3"
location: "2p23.3"
module: 73
arm: "+"
pooled_cpm: 5.49
n_lines_expressing: 43
n_dd_up: 5
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 10
direction_downstream: 1
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# KRTCAP3

*keratinocyte associated protein 3* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.70× (z +8.6, q 5e-15, up in 6 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +6.3, q 7e-08, up in 9 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.595× (z -4.5, q 0.004, down in 16 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLK7]] (+0.59, fdr 1e-05), [[S100A14]] (+0.57, fdr 1e-05), [[HYAL1]] (+0.56, fdr 1e-05); moves opposite to [[EID1]] (-0.52, fdr 1e-05), [[ZNF532]] (-0.51, fdr 3e-05), [[MBTPS2]] (-0.49, fdr 2e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[RAB25]] → it (grade B ⚠); 1 goes from it, the strongest it → [[COX6C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8121.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +8.6 | 5e-15 | 6/8 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.43×** | +8.0 | 4e-13 | 15/15 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +6.3 | 7e-08 | 9/28 (HEC-1-A, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.02×** | +5.8 | 1e-06 | 6/8 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.3 | 0.097 | 4/31 (NCI-H2030, SW 900, …) | inconsistent across doses | position effect removed |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | 1.45× | +3.2 | 0.11 | 9/22 (SW48, HT-29, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.69× | +3.0 | 0.19 | 3/29 (LoVo, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8121.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.595×** | -4.5 | 0.004 | 16/34 (KATO III, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.664×** | -3.7 | 0.064 | 13/39 (SW 900, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.675×** | -3.5 | 0.076 | 15/37 (LOX-IMVI, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.682×** | -3.4 | 0.082 | 14/28 (KATO III, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8121. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.39 | 0 | 2 | — | [[Mozavaptan (drug)]] 0.5 µM 0.0479× (z -10.5) |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 42.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 4.09 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0906× (z -8.6) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.918 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8121), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLK7]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[S100A14]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[HYAL1]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[RHOQ-AS1]] | +0.55 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[UBE2R2]] | +0.55 | +0.38 / +0.47 | both halves | 6e-05 |  |
| [[EFCAB14-AS1]] | +0.54 | +0.36 / +0.50 | both halves | 1e-04 |  |
| [[TMEM54]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[MSLN]] | +0.54 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[RBP1]] | +0.53 | +0.39 / +0.58 | both halves | 6e-05 |  |
| [[TFF1]] | +0.53 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[TFF2]] | +0.53 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[KLK11]] | +0.52 | +0.62 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EID1]] | -0.52 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ZNF532]] | -0.51 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[MBTPS2]] | -0.49 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[SCRN1]] | -0.48 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[EIF4G2]] | -0.47 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[ALG10]] | -0.47 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[ALG10B]] | -0.46 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[AKAP11]] | -0.46 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[SLC35A5]] | -0.45 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[TMEM106B]] | -0.45 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[ERLIN2]] | -0.45 | -0.45 / -0.37 | both halves | 9e-05 |  |
| [[PRKAR1A]] | -0.44 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB25]] | B | RAB25 activity raises KRTCAP3's level | lines that do not express RAB25 (33) vs lines expressing it (17) | 3.45× lower at baseline in the lines without RAB25 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, TMEM30B, PRSS8 |
| [[S100A14]] | B | S100A14 activity raises KRTCAP3's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 2.97× lower at baseline in the lines without S100A14 | 0.001 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |
| [[AP1M2]] | B | AP1M2 activity raises KRTCAP3's level | lines that do not express AP1M2 (24) vs lines expressing it (26) | 2.41× lower at baseline in the lines without AP1M2 | 0.002 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7 |
| [[KLK10]] | B | KLK10 activity raises KRTCAP3's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 2.95× lower at baseline in the lines without KLK10 | 0.013 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[EPCAM]] | B | EPCAM activity raises KRTCAP3's level | lines that do not express EPCAM (28) vs lines expressing it (22) | 2.52× lower at baseline in the lines without EPCAM | 0.024 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[KLK11]] | B | KLK11 activity raises KRTCAP3's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 3.14× lower at baseline in the lines without KLK11 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ |
| [[TFF2]] | B | TFF2 activity raises KRTCAP3's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 2.70× lower at baseline in the lines without TFF2 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |
| [[SPINT2]] | B | SPINT2 activity raises KRTCAP3's level | lines that do not express SPINT2 (24) vs lines expressing it (26) | 2.24× lower at baseline in the lines without SPINT2 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, ENTPD2 |
| [[MSLN]] | B | MSLN activity raises KRTCAP3's level | lines that do not express MSLN (33) vs lines expressing it (17) | 2.22× lower at baseline in the lines without MSLN | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR |
| [[EID1]] | C | EID1 activity lowers KRTCAP3's level | lines that do not express EID1 (3) vs lines expressing it (47) | 3.56× higher at baseline in the lines without EID1 | 0.043 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: MNS1, ENSG00000283491, AGK |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COX6C]] | B | KRTCAP3 activity lowers COX6C's level | lines that do not express KRTCAP3 (7) vs lines expressing it (43) | 1.28× higher at baseline in the lines without KRTCAP3 | 0.051 | ⚠ within organs, on part of the lines; also absent: RNF103-CHMP3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.305). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.3, 60.3); signed map (70.4, 9.3). **Vector** length 42.2, 5.76% of its response variance represented; |z| ≥ 3 in 654 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +5.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.3 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +2.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.2 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -1.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.6 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.3 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | keratinocyte associated protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:27,442,366-27,446,481 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KCP3 |
| Matched by | ensembl_id |

UniProt [Q53RY4](https://www.uniprot.org/uniprotkb/Q53RY4) carries no function annotation.

**Summary**, from NCBI Gene [200634](https://www.ncbi.nlm.nih.gov/gene/200634):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28943](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28943) · Entrez [200634](https://www.ncbi.nlm.nih.gov/gene/200634) · UniProt [Q53RY4](https://www.uniprot.org/uniprotkb/Q53RY4) · Ensembl [ENSG00000157992](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157992)

## Data

Gene col 8121: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8121); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8121, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8121]; `tensor/DDL_lfc|DDL_z.npy` [8121]; `embed/gene_vectors.npy` [8121]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8121 or target_col == 8121). Every well: [[KRTCAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRTCAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
