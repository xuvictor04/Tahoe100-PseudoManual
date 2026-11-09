---
symbol: "SH3BGRL3"
type: "gene"
col: 6644
ensembl_id: "ENSG00000142669"
name: "SH3 domain binding glutamate rich protein like 3"
location: "1p36.11"
module: 184
arm: "+"
pooled_cpm: 71.48
n_lines_expressing: 48
n_dd_up: 3
n_dd_down: 5
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/184"]
generated_by: "tahoemap"
---

# SH3BGRL3

*SH3 domain binding glutamate rich protein like 3* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.74× (z +8.0, q 9e-13, up in 40 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SNU-423 7.13×, SW 900 5.97×, A-172 4.01×, NCI-H1792 7.03×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.431× (z -7.2, q 4e-10, down in 38 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[S100A16]] (+0.73, fdr 7e-06), [[CIB1]] (+0.72, fdr 7e-06), [[ARID3B]] (+0.69, fdr 1e-05); moves opposite to [[FUBP1]] (-0.66, fdr 2e-05), [[SAFB]] (-0.64, fdr 2e-05), [[NNT]] (-0.61, fdr 5e-05).
> It sits in the **+** arm of [[Module 184]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MMP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6644.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SNU-423 7.13×, SW 900 5.97×, A-172 4.01×, NCI-H1792 7.03×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.74×** | +8.0 | 9e-13 | 40/45 (SNU-423, SW 900, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.11×** | +6.6 | 1e-08 | 34/39 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.07×** | +4.1 | 0.009 | 32/42 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.79× | +3.4 | 0.10 | 33/45 (BT-474, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | 1.65× | +3.0 | 0.27 | 30/46 (COLO 205, SW480, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6644.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.431×** | -7.2 | 4e-10 | 38/45 (NCI-H2030, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.454×** | -3.9 | 0.032 | 32/48 (LoVo, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~21% here); noisy plate (z scaled); position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **0.289×** | -3.7 | 0.036 | 40/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.538×** | -3.5 | 0.065 | 34/46 (LoVo, SW48, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.318×** | -3.4 | 0.065 | 38/47 (HCT15, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.592× | -3.2 | 0.15 | 36/46 (H4, NCI-H460, …) | rises with dose | position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.361× | -3.1 | 0.18 | 34/47 (RPMI-7951, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 0.605× | -3.0 | 0.18 | 35/46 (H4, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.88 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6644. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 98.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HOP62 (line)]] | alt | 90.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -9.4) |
| [[LoVo (line)]] | wt | 76.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 71.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 44.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 60.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 66.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.03× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H2030 (line)]] | alt | 108 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 61.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 99.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 52.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -9.0) |
| [[SNU-1 (line)]] | wt | 36.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -11.6) |
| [[SNU-423 (line)]] | alt | 49.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.13× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SW 900 (line)]] | alt | 67.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.97× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-427 (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 224 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 181 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 94.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 87.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 40.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6644), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[S100A16]] | +0.73 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[CIB1]] | +0.72 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[ARID3B]] | +0.69 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[UBA6]] | +0.69 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[TIMP1]] | +0.69 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[PLIN3]] | +0.67 | +0.64 / +0.59 | both halves | 7e-06 | STRING 447 |
| [[LYPD3]] | +0.67 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[FAM89B]] | +0.66 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[EHD4]] | +0.65 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[PDLIM7]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[CSNK1E]] | +0.64 | +0.64 / +0.57 | both halves | 8e-06 |  |
| [[PSD3]] | +0.64 | +0.71 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUBP1]] | -0.66 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[SAFB]] | -0.64 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[NNT]] | -0.61 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[IQCH-AS1]] | -0.60 | -0.58 / -0.40 | both halves | 5e-05 |  |
| [[GOLGA2P5-1]] | -0.59 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[ADI1]] | -0.59 | -0.58 / -0.30 | both halves | 2e-04 |  |
| [[MCCC2]] | -0.58 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[LUC7L2]] | -0.58 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[RPRD2]] | -0.57 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[UBAP2L]] | -0.57 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[DUS3L]] | -0.56 | -0.37 / -0.39 | both halves | 9e-05 |  |
| [[QTRT1]] | -0.56 | -0.48 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP1]] | B | MMP1 activity raises SH3BGRL3's level | lines that do not express MMP1 (26) vs lines expressing it (24) | 1.54× lower at baseline in the lines without MMP1 | 0.034 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[IL1RAP]] | B | IL1RAP activity raises SH3BGRL3's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 1.85× lower at baseline in the lines without IL1RAP | 0.058 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[S100A6]] | B | S100A6 activity raises SH3BGRL3's level | lines that do not express S100A6 (5) vs lines expressing it (45) | 1.79× lower at baseline in the lines without S100A6 | 0.060 | ⚠ within organs, on part of the lines; also absent: GPRC5D-AS1, HLA-H, PRRG1; maybe low, not absent; its own permutation p |
| [[FAM107B]] | B | FAM107B activity raises SH3BGRL3's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 1.54× lower at baseline in the lines without FAM107B | 0.064 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[DENND2C]] | B | DENND2C activity raises SH3BGRL3's level | lines that do not express DENND2C (10) vs lines expressing it (40) | 1.73× lower at baseline in the lines without DENND2C | 0.067 | ⚠ within organs, on part of the lines; also absent: MSN, CAV1, RIMKLB |
| [[F3]] | B | F3 activity raises SH3BGRL3's level | lines that do not express F3 (24) vs lines expressing it (26) | 1.73× lower at baseline in the lines without F3 | 0.076 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[CD59]] | B | CD59 activity raises SH3BGRL3's level | lines that do not express CD59 (7) vs lines expressing it (43) | 2.15× lower at baseline in the lines without CD59 | 0.078 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[PIK3CB]] | B | PIK3CB activity raises SH3BGRL3's level | compounds that target PIK3CB: 2 of 3 lower it (Bimiralisib, GSK1059615) | 67% of the class's compounds vs 1.1% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 184]]; 20 genes; this gene is in the **+** arm (projection on the module's main direction 0.808). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (48.5, 1.3); signed map (-3.0, 46.9). **Vector** length 87.2, 38.7% of its response variance represented; |z| ≥ 3 in 657 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +0.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -0.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.5 | +0.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | -1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.4 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -3.1 | +4.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.0 | +0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.9 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.9 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -3.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.3 | -2.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.2 | -1.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | SH3 domain binding glutamate rich protein like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:26,280,086-26,281,522 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H299](https://www.uniprot.org/uniprotkb/Q9H299) (SH3 domain-binding glutamic acid-rich-like protein 3):

> Could act as a modulator of glutaredoxin biological activity (Probable). May play a role in cytoskeleton organization.

**Summary**, from NCBI Gene [83442](https://www.ncbi.nlm.nih.gov/gene/83442):

> Involved in cytoskeleton organization. Located in cytosol and ruffle membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15568](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15568) · Entrez [83442](https://www.ncbi.nlm.nih.gov/gene/83442) · UniProt [Q9H299](https://www.uniprot.org/uniprotkb/Q9H299) · Ensembl [ENSG00000142669](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142669)

## Data

Gene col 6644: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6644); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6644, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6644]; `tensor/DDL_lfc|DDL_z.npy` [6644]; `embed/gene_vectors.npy` [6644]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6644 or target_col == 6644). Every well: [[SH3BGRL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3BGRL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
