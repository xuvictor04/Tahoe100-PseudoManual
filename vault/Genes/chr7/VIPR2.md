---
symbol: "VIPR2"
type: "gene"
col: 2708
ensembl_id: "ENSG00000106018"
name: "vasoactive intestinal peptide receptor 2"
location: "7q36.3"
module: 9
arm: "+"
pooled_cpm: 3.07
n_lines_expressing: 18
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 10
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# VIPR2

*vasoactive intestinal peptide receptor 2* — 7q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 12.7× (z +22.1, q 0e+00, up in 4 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.212×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNH7]] (+0.64, fdr 7e-06), [[ASXL3]] (+0.62, fdr 1e-05), [[PGR]] (+0.58, fdr 5e-05); moves opposite to [[METTL15]] (-0.45, fdr 2e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FGF13]] → it (grade C ⚠); 10 go from it, the strongest it → [[ATP2A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2708.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **12.7×** | +22.1 | 0e+00 | 4/6 (HT-29, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.28×** | +12.2 | 7e-32 | 3/3 (BT-474, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.19×** | +9.7 | 4e-20 | 1/2 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.83×** | +9.0 | 2e-17 | 1/7 (NCI-H1573) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.95×** | +7.0 | 4e-10 | 2/2 (NCI-H460, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.76×** | +6.2 | 4e-08 | 2/5 (BT-474, SW 900) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.82×** | +5.2 | 2e-05 | 7/12 (A-427, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.81×** | +5.1 | 2e-05 | 0/12 | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **2.04×** | +4.4 | 8e-04 | 2/9 (A-427, C-33 A) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.48×** | +4.0 | 0.004 | 1/2 (BT-474) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +3.9 | 0.005 | 5/8 (C-33 A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +3.5 | 0.025 | 0/7 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.19×** | +3.4 | 0.026 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.71×** | +3.3 | 0.039 | 2/6 (NCI-H460, A-427) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.64×** | +3.1 | 0.068 | 1/2 (BT-474) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.64×** | +3.0 | 0.077 | 0/10 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2708.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (BT-474 0.212×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.857× | -3.5 | 0.29 | 2/15 (BT-474, SHP-77) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2708. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 114 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.212× (z -9.5) |
| [[A-172 (line)]] | wt | 0.562 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.354 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.346 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.560 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.547 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.909 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.506 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.557 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.648 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.618 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.443 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.426 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.528 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.814 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.525 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2708), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNH7]] | +0.64 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[ASXL3]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[PGR]] | +0.58 | +0.55 / +0.40 | both halves | 5e-05 | **novel candidate** |
| [[GLRA3]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[CASC15]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[NKAIN2]] | +0.57 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[KHDRBS2]] | +0.56 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[AGBL1]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[GRIA2]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[CELF4]] | +0.55 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[SCUBE1]] | +0.55 | +0.49 / +0.39 | both halves | 6e-05 |  |
| [[XIRP2]] | +0.55 | +0.39 / +0.55 | both halves | 6e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL15]] | -0.45 | -0.31 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGF13]] | C | FGF13 activity raises VIPR2's level | lines that do not express FGF13 (31) vs lines expressing it (19) | 1.92× lower at baseline in the lines without FGF13 | 0.033 | ⚠ within organs, on part of the lines; also absent: NCAM1, ENSG00000237268, SOX11; co-absent with the target |
| [[RAB3C]] | C | RAB3C activity raises VIPR2's level | lines that do not express RAB3C (31) vs lines expressing it (19) | 1.65× lower at baseline in the lines without RAB3C | 0.046 | ⚠ within organs, on part of the lines; also absent: VGF, SCG3, CDH10; maybe low, not absent; co-absent with the target |
| [[NKAIN2]] | C | NKAIN2 activity raises VIPR2's level | lines that do not express NKAIN2 (32) vs lines expressing it (18) | 1.40× lower at baseline in the lines without NKAIN2 | 0.054 | ⚠ within organs, on part of the lines; also absent: GREM2, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[CACNB2]] | C | CACNB2 activity raises VIPR2's level | lines that do not express CACNB2 (31) vs lines expressing it (19) | 1.63× lower at baseline in the lines without CACNB2 | 0.063 | ⚠ within organs, on part of the lines; also absent: SFTA3-1, DPP10, LINC01035; maybe low, not absent; co-absent with the target |
| [[RIMS1]] | C | RIMS1 activity raises VIPR2's level | lines that do not express RIMS1 (18) vs lines expressing it (32) | 1.83× lower at baseline in the lines without RIMS1 | 0.099 | ⚠ within organs, on part of the lines; also absent: ELOVL4, GLRB, RNF150; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP2A3]] | B | VIPR2 activity raises ATP2A3's level | lines that do not express VIPR2 (32) vs lines expressing it (18) | 2.40× lower at baseline in the lines without VIPR2 | 0.083 | ⚠ within organs, on part of the lines; also absent: DPP10, KCNH5, ASXL3; maybe low, not absent |
| [[RIMS1]] | C | VIPR2 activity raises RIMS1's level | lines that do not express VIPR2 (32) vs lines expressing it (18) | 2.16× lower at baseline in the lines without VIPR2 | 0.006 | ⚠ within organs, on part of the lines; also absent: DPP10, KCNH5, ASXL3; maybe low, not absent; co-absent with the target |
| [[CADM2]] | C | VIPR2 activity raises CADM2's level | lines that do not express VIPR2 (32) vs lines expressing it (18) | 5.52× lower at baseline in the lines without VIPR2 | 0.008 | ⚠ within organs, on part of the lines; also absent: DPP10, KCNH5, ASXL3; maybe low, not absent; co-absent with the target |
| [[SEMA3E]] | C | VIPR2 activity raises SEMA3E's level | lines that do not express VIPR2 (32) vs lines expressing it (18) | 3.54× lower at baseline in the lines without VIPR2 | 0.034 | ⚠ within organs, on part of the lines; also absent: DPP10, KCNH5, ASXL3; maybe low, not absent; co-absent with the target |
| [[ADARB2]] | C | VIPR2 activity raises ADARB2's level | lines that do not express VIPR2 (32) vs lines expressing it (18) | 3.33× lower at baseline in the lines without VIPR2 | 0.036 | ⚠ within organs, on part of the lines; also absent: DPP10, KCNH5, ASXL3; maybe low, not absent; co-absent with the target |
| [[FGF13]] | C | VIPR2 activity raises FGF13's level | lines that do not express VIPR2 (32) vs lines expressing it (18) | 2.45× lower at baseline in the lines without VIPR2 | 0.052 | ⚠ within organs, on part of the lines; also absent: DPP10, KCNH5, ASXL3; maybe low, not absent; co-absent with the target |
| [[COLEC12]] | C | VIPR2 activity raises COLEC12's level | lines that do not express VIPR2 (32) vs lines expressing it (18) | 2.12× lower at baseline in the lines without VIPR2 | 0.057 | ⚠ within organs, on part of the lines; also absent: DPP10, KCNH5, ASXL3; maybe low, not absent; co-absent with the target |
| [[MARCHF1]] | C | VIPR2 activity raises MARCHF1's level | lines that do not express VIPR2 (32) vs lines expressing it (18) | 2.28× lower at baseline in the lines without VIPR2 | 0.057 | ⚠ within organs, on part of the lines; also absent: DPP10, KCNH5, ASXL3; maybe low, not absent; co-absent with the target |
| [[ASXL3]] | C | VIPR2 activity raises ASXL3's level | lines that do not express VIPR2 (32) vs lines expressing it (18) | 2.95× lower at baseline in the lines without VIPR2 | 0.071 | ⚠ within organs, on part of the lines; also absent: DPP10, KCNH5, ASXL3; maybe low, not absent; co-absent with the target |
| [[DOK6]] | C | VIPR2 activity raises DOK6's level | lines that do not express VIPR2 (32) vs lines expressing it (18) | 2.65× lower at baseline in the lines without VIPR2 | 0.080 | ⚠ within organs, on part of the lines; also absent: DPP10, KCNH5, ASXL3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.542). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.9, 35.4); signed map (42.2, 37.3). **Vector** length 18.3, 3.36% of its response variance represented; |z| ≥ 3 in 243 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +7.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +22.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.8 | +0.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.7 | +0.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.9 | -3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -1.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.7 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -0.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.7 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | vasoactive intestinal peptide receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.3 — chr7:159,028,175-159,144,867 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VPAC2, VPAC2R |
| Gene groups (HGNC) | Vasoactive intestinal peptide family receptors |
| Reactome | 6 pathways, smallest: Glucagon-type ligand receptors; Class B/2 (Secretin family receptors); G alpha (s) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P41587](https://www.uniprot.org/uniprotkb/P41587) (Vasoactive intestinal polypeptide receptor 2):

> G protein-coupled receptor activated by the neuropeptides vasoactive intestinal peptide (VIP) and pituitary adenylate cyclase-activating polypeptide (ADCYAP1/PACAP). Binds VIP and both PACAP27 and PACAP38 bioactive peptides with the following order of potency PACAP38 = VIP > PACAP27. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors. Activates cAMP-dependent pathway. May be …

**Summary**, from NCBI Gene [7434](https://www.ncbi.nlm.nih.gov/gene/7434):

> This gene encodes a receptor for vasoactive intestinal peptide, a small neuropeptide. Vasoactive intestinal peptide is involved in smooth muscle relaxation, exocrine and endocrine secretion, and water and ion flux in lung and intestinal epithelia. Its actions are effected through integral membrane receptors associated with a guanine nucleotide binding protein which activates adenylate cyclase. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:12695](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12695) · Entrez [7434](https://www.ncbi.nlm.nih.gov/gene/7434) · UniProt [P41587](https://www.uniprot.org/uniprotkb/P41587) · Ensembl [ENSG00000106018](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106018)

## Data

Gene col 2708: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2708); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2708, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2708]; `tensor/DDL_lfc|DDL_z.npy` [2708]; `embed/gene_vectors.npy` [2708]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2708 or target_col == 2708). Every well: [[VIPR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VIPR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
