---
symbol: "SEMA3E"
type: "gene"
col: 9943
ensembl_id: "ENSG00000170381"
name: "semaphorin 3E"
location: "7q21.11"
module: 9
arm: "+"
pooled_cpm: 11.55
n_lines_expressing: 24
n_dd_up: 35
n_dd_down: 0
n_dd_up_clean: 29
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SEMA3E

*semaphorin 3E* — 7q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.99× (z +16.2, q 0e+00, up in 11 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.57× (z +15.7, q 0e+00, up in 5 of 18 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.279×, BT-474 0.410×); [[Panobinostat (drug)]] 5 µM in 2 lines (HT-29 0.208×, SHP-77 0.281×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (HT-29 0.202×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPK10]] (+0.63, fdr 8e-06), [[MID1]] (+0.63, fdr 1e-05), [[THSD7A]] (+0.61, fdr 1e-05); moves opposite to [[ANKRD13D]] (-0.52, fdr 2e-05), [[GLE1]] (-0.51, fdr 4e-05), [[MAP2K1]] (-0.48, fdr 4e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[FOXP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9943.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.99×** | +16.2 | 0e+00 | 11/16 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.57×** | +15.7 | 0e+00 | 5/18 (Panc 03.27, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.95×** | +15.5 | 0e+00 | 8/11 (J82, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.53×** | +15.4 | 0e+00 | 16/19 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.32×** | +9.1 | 7e-18 | 7/14 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +8.5 | 1e-15 | 14/21 (NCI-H1792, NCI-H2347, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.94×** | +7.8 | 6e-13 | 9/20 (SK-MEL-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +7.1 | 9e-11 | 12/20 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.76×** | +6.6 | 2e-09 | 14/20 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +6.5 | 6e-09 | 15/20 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.65×** | +5.6 | 8e-07 | 9/20 (J82, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +5.6 | 8e-07 | 14/21 (J82, C32, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.1 | 2e-05 | 6/21 (C32, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +4.6 | 1e-04 | 8/20 (SW 900, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +4.5 | 2e-04 | 6/17 (C32, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +4.5 | 3e-04 | 11/19 (C32, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.38×** | +4.1 | 0.001 | 8/20 (NCI-H1573, J82, …) | two highest doses | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.003 | 5/21 (C32, J82, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.003 | 11/19 (NCI-H1573, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9943.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.279×, BT-474 0.410×); [[Panobinostat (drug)]] 5 µM in 2 lines (HT-29 0.208×, SHP-77 0.281×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (HT-29 0.202×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | 0.735× | -3.6 | 0.16 | 9/21 (BT-474, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9943. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 50.2 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +14.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -8.5) |
| [[HT-29 (line)]] | alt | 72.2 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -12.2) |
| [[J82 (line)]] | alt | 21.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +9.4) | — |
| [[NCI-H1573 (line)]] | alt | 25.8 | 1 | 0 | [[Cobimetinib (drug)]] 5 µM 6.76× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 8.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.72× (z +11.9) | — |
| [[NCI-H2347 (line)]] | alt | 7.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.02× (z +12.9) | — |
| [[SHP-77 (line)]] | alt | 90.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 341 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.45 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9943), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK10]] | +0.63 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[MID1]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[THSD7A]] | +0.61 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[EPHA5-AS1]] | +0.61 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[SCN2A]] | +0.60 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[RASEF]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[LRP1B]] | +0.60 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[KCNH7]] | +0.60 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[EPHA5]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[NKAIN2]] | +0.59 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[SLCO2B1]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ABLIM1]] | +0.59 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD13D]] | -0.52 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[GLE1]] | -0.51 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[MAP2K1]] | -0.48 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[MTMR14]] | -0.48 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[FBH1]] | -0.48 | -0.47 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FOXP2]] | B | FOXP2 activity raises SEMA3E's level | lines that do not express FOXP2 (26) vs lines expressing it (24) | 2.07× lower at baseline in the lines without FOXP2 | 0.045 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6 |
| [[TOP2A]] | B | TOP2A activity lowers SEMA3E's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2]] | B | MAP2 activity raises SEMA3E's level | lines that do not express MAP2 (15) vs lines expressing it (35) | 3.16× lower at baseline in the lines without MAP2 | 0.091 | ⚠ within organs, on part of the lines; also absent: LRRC7, ANKRD6, DSEL; maybe low, not absent |
| [[MAPK10]] | B | MAPK10 activity raises SEMA3E's level | lines that do not express MAPK10 (11) vs lines expressing it (39) | 3.23× lower at baseline in the lines without MAPK10 | 0.095 | ⚠ within organs, on part of the lines; also absent: PTPN13, HDGFL3, EML1; maybe low, not absent |
| [[VIPR2]] | C | VIPR2 activity raises SEMA3E's level | lines that do not express VIPR2 (32) vs lines expressing it (18) | 3.54× lower at baseline in the lines without VIPR2 | 0.034 | ⚠ within organs, on part of the lines; also absent: DPP10, KCNH5, ASXL3; maybe low, not absent; co-absent with the target |
| [[SOX2]] | C | SOX2 activity raises SEMA3E's level | lines that do not express SOX2 (35) vs lines expressing it (15) | 2.49× lower at baseline in the lines without SOX2 | 0.079 | ⚠ within organs, on part of the lines; also absent: SNTG1, SCG3, CGA; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.8, 33.0); signed map (49.0, 19.0). **Vector** length 62.8, 16.9% of its response variance represented; |z| ≥ 3 in 600 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.4 | +16.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.0 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +15.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +8.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +6.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.1 | +4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.9 | +5.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +2.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -2.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.7 | +2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.6 | +1.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | semaphorin 3E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.11 — chr7:83,363,238-83,649,139 (-) |
| Ensembl biotype | protein_coding |
| Also known as | M-SemaK, KIAA0331, coll-5; previously SEMAH |
| Gene groups (HGNC) | Immunoglobulin like domain containing; Semaphorins |
| Reactome | 4 pathways, smallest: Other semaphorin interactions; Semaphorin interactions; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [O15041](https://www.uniprot.org/uniprotkb/O15041) (Semaphorin-3E):

> Plays an important role in signaling via the cell surface receptor PLXND1. Mediates reorganization of the actin cytoskeleton, leading to the retraction of cell projections. Promotes focal adhesion disassembly and inhibits adhesion of endothelial cells to the extracellular matrix. Regulates angiogenesis, both during embryogenesis and after birth. Can down-regulate sprouting angiogenesis. Required for normal vascular patterning during embryogenesis. Plays an important role in ensuring the …

**Summary**, from NCBI Gene [9723](https://www.ncbi.nlm.nih.gov/gene/9723):

> Semaphorins are a large family of conserved secreted and membrane associated proteins which possess a semaphorin (Sema) domain and a PSI domain (found in plexins, semaphorins and integrins) in the N-terminal extracellular portion. Based on sequence and structural similarities, semaphorins are put into eight classes: invertebrates contain classes 1 and 2, viruses have class V, and vertebrates contain classes 3-7. Semaphorins serve as axon guidance ligands via multimeric receptor complexes, some …

**Accessions** — [HGNC:10727](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10727) · Entrez [9723](https://www.ncbi.nlm.nih.gov/gene/9723) · UniProt [O15041](https://www.uniprot.org/uniprotkb/O15041) · Ensembl [ENSG00000170381](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170381)

## Data

Gene col 9943: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9943); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9943, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9943]; `tensor/DDL_lfc|DDL_z.npy` [9943]; `embed/gene_vectors.npy` [9943]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9943 or target_col == 9943). Every well: [[SEMA3E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEMA3E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
