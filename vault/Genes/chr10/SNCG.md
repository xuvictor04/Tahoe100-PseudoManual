---
symbol: "SNCG"
type: "gene"
col: 10365
ensembl_id: "ENSG00000173267"
name: "synuclein gamma"
location: "10q23.2"
module: 106
arm: "+"
pooled_cpm: 3.66
n_lines_expressing: 20
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 9
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# SNCG

*synuclein gamma* — 10q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.28× (z +10.4, q 2e-22, up in 8 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.71× (z +4.7, q 3e-04, up in 3 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.138×).
> Its strongest partners by |cos| (76 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZG16B]] (+0.53, fdr 1e-04), [[CAPG]] (+0.52, fdr 6e-05), [[GALK1]] (+0.48, fdr 4e-05); moves opposite to [[ZNG1C]] (-0.38, fdr 0.001, ⚠ not reproduced).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SERPINA5]] → it (grade C ⚠); 9 go from it, the strongest it → [[IL17RE]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10365.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.28×** | +10.4 | 2e-22 | 8/8 (A498, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.15×** | +9.8 | 2e-20 | 4/4 (A498, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.98×** | +6.3 | 6e-08 | 4/5 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.67×** | +6.1 | 1e-07 | 2/5 (MIA PaCa-2, A498) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.71×** | +4.7 | 3e-04 | 3/17 (HOP62, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +4.5 | 8e-04 | 1/14 (HOP62) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +4.4 | 0.001 | 1/7 (A498) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.009 | 1/15 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.66×** | +3.7 | 0.013 | 2/7 (A498, HT-29) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +3.6 | 0.018 | 3/12 (PANC-1, SW480, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.53×** | +3.5 | 0.023 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.75×** | +3.4 | 0.035 | 0/14 | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.96×** | +3.4 | 0.035 | 0/3 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10365.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.138×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.589× | -3.3 | 0.30 | 9/14 (SHP-77, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.570× | -3.3 | 0.30 | 3/17 (HCT15, CFPAC-1, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.607× | -3.1 | 0.31 | 0/17 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10365. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 6.01 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -8.8) |
| [[A-172 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.301 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.861 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.886 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.437 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.444 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.422 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.361 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.919 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.277 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.678 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.709 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.323 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.406 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.860 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10365), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 23 of them with an alert (⚠; 23 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZG16B]] | +0.53 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[CAPG]] | +0.52 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[GALK1]] | +0.48 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[MOGAT3]] | +0.47 | +0.23 / +0.53 | both halves | 5e-04 |  |
| [[SERPINA5]] | +0.47 | +0.49 / +0.30 | both halves | 2e-04 |  |
| [[PCDH1]] | +0.45 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[CCDC33]] | +0.44 | +0.36 / +0.37 | both halves | 1e-04 |  |
| [[HSD17B2]] | +0.44 | +0.40 / +0.38 | both halves | 6e-05 |  |
| [[TNFRSF10A-DT]] | +0.44 | +0.11 / +0.61 | ⚠ one half (not replicated) | 0.002 |  |
| [[KCNB1]] | +0.44 | +0.14 / +0.44 | ⚠ not reproduced | 0.002 |  |
| [[PPM1N]] | +0.44 | +0.17 / +0.54 | ⚠ one half (not replicated) | 0.001 |  |
| [[PER1]] | +0.44 | +0.22 / +0.45 | both halves | 6e-04 |  |
| [[GHDC]] | +0.43 | +0.32 / +0.54 | both halves | 1e-04 |  |
| [[CTNNB1]] | +0.43 | +0.34 / +0.38 | both halves | 1e-04 |  |
| [[RILP]] | +0.43 | +0.29 / +0.50 | both halves | 2e-04 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNG1C]] | -0.38 | -0.17 / -0.47 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINA5]] | C | SERPINA5 activity raises SNCG's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 1.60× lower at baseline in the lines without SERPINA5 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL17RE]] | B | SNCG activity raises IL17RE's level | lines that do not express SNCG (30) vs lines expressing it (20) | 2.15× lower at baseline in the lines without SNCG | 0.021 | ⚠ within organs, on part of the lines; also absent: CST6, ENSG00000286546, IGFL2-AS1 |
| [[LURAP1]] | B | SNCG activity raises LURAP1's level | lines that do not express SNCG (30) vs lines expressing it (20) | 1.52× lower at baseline in the lines without SNCG | 0.042 | ⚠ within organs, on part of the lines; also absent: CST6, ENSG00000286546, IGFL2-AS1 |
| [[PTK6]] | B | SNCG activity raises PTK6's level | lines that do not express SNCG (30) vs lines expressing it (20) | 2.41× lower at baseline in the lines without SNCG | 0.060 | ⚠ within organs, on part of the lines; also absent: CST6, ENSG00000286546, IGFL2-AS1 |
| [[TMEM63C]] | B | SNCG activity raises TMEM63C's level | lines that do not express SNCG (30) vs lines expressing it (20) | 1.21× lower at baseline in the lines without SNCG | 0.079 | ⚠ within organs, on part of the lines; also absent: CST6, ENSG00000286546, IGFL2-AS1 |
| [[GAMT]] | B | SNCG activity raises GAMT's level | lines that do not express SNCG (30) vs lines expressing it (20) | 1.37× lower at baseline in the lines without SNCG | 0.090 | ⚠ within organs, on part of the lines; also absent: CST6, ENSG00000286546, IGFL2-AS1 |
| [[RINL]] | B | SNCG activity raises RINL's level | lines that do not express SNCG (30) vs lines expressing it (20) | 1.53× lower at baseline in the lines without SNCG | 0.095 | ⚠ within organs, on part of the lines; also absent: CST6, ENSG00000286546, IGFL2-AS1 |
| [[EPS8L2]] | C | SNCG activity raises EPS8L2's level | lines that do not express SNCG (30) vs lines expressing it (20) | 3.46× lower at baseline in the lines without SNCG | 0.004 | ⚠ within organs, on part of the lines; also absent: CST6, ENSG00000286546, IGFL2-AS1; co-absent with the target |
| [[SCNN1A]] | C | SNCG activity raises SCNN1A's level | lines that do not express SNCG (30) vs lines expressing it (20) | 3.64× lower at baseline in the lines without SNCG | 0.045 | ⚠ within organs, on part of the lines; also absent: CST6, ENSG00000286546, IGFL2-AS1; co-absent with the target |
| [[KRT19]] | C | SNCG activity raises KRT19's level | lines that do not express SNCG (30) vs lines expressing it (20) | 3.22× lower at baseline in the lines without SNCG | 0.057 | ⚠ within organs, on part of the lines; also absent: CST6, ENSG00000286546, IGFL2-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.354). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.1, 56.4); signed map (-2.6, 39.2). **Vector** length 25.5, 4.33% of its response variance represented; |z| ≥ 3 in 350 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +10.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +3.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.8 | +0.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.0 | -0.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.9 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | synuclein gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.2 — chr10:86,958,599-86,963,258 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BCSG1, SR, persyn |
| Gene groups (HGNC) | Synuclein family |
| Hallmark sets | ADIPOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [O76070](https://www.uniprot.org/uniprotkb/O76070) (Gamma-synuclein):

> Plays a role in neurofilament network integrity. May be involved in modulating axonal architecture during development and in the adult. In vitro, increases the susceptibility of neurofilament-H to calcium-dependent proteases (By similarity). May also function in modulating the keratin network in skin. Activates the MAPK and Elk-1 signal transduction pathway (By similarity).

**Summary**, from NCBI Gene [6623](https://www.ncbi.nlm.nih.gov/gene/6623):

> This gene encodes a member of the synuclein family of proteins which are believed to be involved in the pathogenesis of neurodegenerative diseases. Mutations in this gene have also been associated with breast tumor development. [provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:11141](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11141) · Entrez [6623](https://www.ncbi.nlm.nih.gov/gene/6623) · UniProt [O76070](https://www.uniprot.org/uniprotkb/O76070) · Ensembl [ENSG00000173267](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173267)

## Data

Gene col 10365: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10365); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10365, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10365]; `tensor/DDL_lfc|DDL_z.npy` [10365]; `embed/gene_vectors.npy` [10365]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10365 or target_col == 10365). Every well: [[SNCG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNCG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
