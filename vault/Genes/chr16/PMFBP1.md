---
symbol: "PMFBP1"
type: "gene"
col: 4003
ensembl_id: "ENSG00000118557"
name: "polyamine modulated factor 1 binding protein 1"
location: "16q22.2"
module: 26
arm: "+"
pooled_cpm: 6.13
n_lines_expressing: 42
n_dd_up: 8
n_dd_down: 17
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 9
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# PMFBP1

*polyamine modulated factor 1 binding protein 1* — 16q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.92× (z +8.6, q 4e-15, up in 3 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.80× (z +7.0, q 6e-10, up in 19 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.277× (z -10.7, q 4e-24, down in 32 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRGUK]] (+0.65, fdr 7e-06), [[TAPT1-AS1]] (+0.63, fdr 7e-06), [[FSIP2-AS1]] (+0.63, fdr 7e-06); moves opposite to [[NDUFAF7]] (-0.51, fdr 3e-05), [[UNC119]] (-0.51, fdr 3e-05), [[ISCA1]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FSIP2-AS1]] → it (grade C ⚠); 9 go from it, the strongest it → [[LINC01572]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4003.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.92×** | +8.6 | 4e-15 | 3/7 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.41×** | +7.3 | 6e-11 | 11/18 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.80×** | +7.0 | 6e-10 | 19/34 (C32, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.19×** | +6.1 | 2e-07 | 5/9 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +4.2 | 0.003 | 14/39 (A498, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.59×** | +3.9 | 0.010 | 11/36 (A498, NCI-H1573, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.053 | 18/37 (LoVo, C32, …) | top dose only | cell-cycle shift (explains ~22% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.50×** | +3.4 | 0.054 | 8/38 (LS 180, SW48, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM |  | 1.31× | +3.1 | 0.11 | 8/38 (NCI-H2030, SW48, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 1.44× | +3.1 | 0.13 | 12/32 (C32, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.44× | +3.0 | 0.13 | 3/35 (HT-29, SW 900, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4003.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.277×** | -10.7 | 4e-24 | 32/39 (SW480, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.485×** | -6.1 | 4e-07 | 23/39 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.609×** | -5.9 | 8e-07 | 22/38 (RKO, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.499×** | -5.8 | 8e-07 | 25/39 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.508×** | -5.7 | 2e-06 | 18/34 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.545×** | -5.1 | 3e-05 | 21/39 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.535×** | -5.0 | 4e-05 | 19/26 (SW480, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.323×** | -4.9 | 5e-05 | 21/32 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.565×** | -4.8 | 1e-04 | 16/39 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.554×** | -4.7 | 2e-04 | 20/36 (LOX-IMVI, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Artesunate (drug)]] 5 µM |  | **0.712×** | -4.0 | 0.003 | 15/39 (SHP-77, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.629×** | -3.9 | 0.005 | 13/39 (HEC-1-A, SNU-1, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.421×** | -3.8 | 0.007 | 13/29 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.646×** | -3.7 | 0.010 | 15/39 (LOX-IMVI, SW48, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.446×** | -3.5 | 0.015 | 14/36 (SW480, HCT15, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.661×** | -3.5 | 0.018 | 15/38 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.675×** | -3.3 | 0.033 | 20/37 (SW480, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4003. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 15.1 | 0 | 5 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.116× (z -12.7) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.135× (z -12.3) |
| [[COLO 205 (line)]] | alt | 20.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -9.4) |
| [[C32 (line)]] | wt | 3.94 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.8× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 27.0 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 0.05 µM 0.198× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 5.76 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0665× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 8.51 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.25× (z +10.4) | [[Penfluridol (drug)]] 5 µM 0.0660× (z -10.5) |
| [[C-33 A (line)]] | alt | 12.4 | 0 | 1 | — | [[Mozavaptan (drug)]] 5 µM 0.0541× (z -9.5) |
| [[HOP62 (line)]] | alt | 11.5 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.112× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 2.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +10.0) | — |
| [[A-172 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.787 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.932 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.892 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4003), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRGUK]] | +0.65 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[TAPT1-AS1]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[FSIP2-AS1]] | +0.63 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[TMEM232]] | +0.62 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[C1QTNF3]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[LINC01572]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[SEMA6A-AS1]] | +0.60 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[STAC3]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[SLC38A4-AS1]] | +0.59 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[ASPM]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[CEP112]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 | STRING 623 |
| [[PRR4]] | +0.58 | +0.47 / +0.68 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFAF7]] | -0.51 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[UNC119]] | -0.51 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[ISCA1]] | -0.50 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[FBXO44]] | -0.50 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[ZSCAN2]] | -0.50 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[FLYWCH1]] | -0.49 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[DENND10]] | -0.48 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[TMEM68]] | -0.48 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[FGD1]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[RNPEP]] | -0.48 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[SLC18B1]] | -0.48 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[KLHL7]] | -0.48 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSIP2-AS1]] | C | FSIP2-AS1 activity raises PMFBP1's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 2.85× lower at baseline in the lines without FSIP2-AS1 | 0.008 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent; co-absent with the target |
| [[TPRG1]] | C | TPRG1 activity raises PMFBP1's level | lines that do not express TPRG1 (10) vs lines expressing it (40) | 1.86× lower at baseline in the lines without TPRG1 | 0.050 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SYCP2L; maybe low, not absent; co-absent with the target |
| [[ITPR2-AS1]] | C | ITPR2-AS1 activity raises PMFBP1's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 2.53× lower at baseline in the lines without ITPR2-AS1 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17 |
| [[SPATA17]] | C | SPATA17 activity raises PMFBP1's level | lines that do not express SPATA17 (3) vs lines expressing it (47) | 3.09× lower at baseline in the lines without SPATA17 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ITPR2-AS1, ITPR2, SYCP2L; maybe low, not absent; its own permutation p |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01572]] | B | PMFBP1 activity raises LINC01572's level | lines that do not express PMFBP1 (8) vs lines expressing it (42) | 2.62× lower at baseline in the lines without PMFBP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: GALNT16, FSIP2-AS1, ENSG00000237356; maybe low, not absent |
| [[LRGUK]] | B | PMFBP1 activity raises LRGUK's level | lines that do not express PMFBP1 (8) vs lines expressing it (42) | 2.50× lower at baseline in the lines without PMFBP1 | 0.009 | ⚠ within organs, on part of the lines; also absent: GALNT16, FSIP2-AS1, ENSG00000237356; maybe low, not absent |
| [[ITPR2-AS1]] | B | PMFBP1 activity raises ITPR2-AS1's level | lines that do not express PMFBP1 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without PMFBP1 | 0.027 | ⚠ within organs, on part of the lines; also absent: GALNT16, FSIP2-AS1, ENSG00000237356; maybe low, not absent |
| [[PRH1]] | B | PMFBP1 activity raises PRH1's level | lines that do not express PMFBP1 (8) vs lines expressing it (42) | 2.15× lower at baseline in the lines without PMFBP1 | 0.031 | ⚠ within organs, on part of the lines; also absent: GALNT16, FSIP2-AS1, ENSG00000237356; maybe low, not absent |
| [[PRR4]] | B | PMFBP1 activity raises PRR4's level | lines that do not express PMFBP1 (8) vs lines expressing it (42) | 1.90× lower at baseline in the lines without PMFBP1 | 0.032 | ⚠ within organs, on part of the lines; also absent: GALNT16, FSIP2-AS1, ENSG00000237356; maybe low, not absent |
| [[WARS2-AS1]] | B | PMFBP1 activity raises WARS2-AS1's level | lines that do not express PMFBP1 (8) vs lines expressing it (42) | 1.63× lower at baseline in the lines without PMFBP1 | 0.045 | ⚠ within organs, on part of the lines; also absent: GALNT16, FSIP2-AS1, ENSG00000237356; maybe low, not absent |
| [[SPATA17]] | B | PMFBP1 activity raises SPATA17's level | lines that do not express PMFBP1 (8) vs lines expressing it (42) | 1.84× lower at baseline in the lines without PMFBP1 | 0.049 | ⚠ within organs, on part of the lines; also absent: GALNT16, FSIP2-AS1, ENSG00000237356; maybe low, not absent |
| [[PNPLA3]] | B | PMFBP1 activity raises PNPLA3's level | lines that do not express PMFBP1 (8) vs lines expressing it (42) | 1.91× lower at baseline in the lines without PMFBP1 | 0.098 | ⚠ within organs, on part of the lines; also absent: GALNT16, FSIP2-AS1, ENSG00000237356; maybe low, not absent |
| [[FSIP2-AS1]] | C | PMFBP1 activity raises FSIP2-AS1's level | lines that do not express PMFBP1 (8) vs lines expressing it (42) | 3.04× lower at baseline in the lines without PMFBP1 | 0.018 | ⚠ within organs, on part of the lines; also absent: GALNT16, FSIP2-AS1, ENSG00000237356; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.385). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-22.4, 32.7); signed map (41.5, -12.1). **Vector** length 72.5, 14.2% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +3.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.4 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +1.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.9 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +1.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.4 | +3.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.4 | +2.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.5 | -5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.7 | -10.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.1 | -5.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.6 | -4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | -3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.3 | -2.4 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.3 | -1.5 |
|  | [[Piroxicam (drug)]] 0.05 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | polyamine modulated factor 1 binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.2 — chr16:72,112,157-72,176,878 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBY8](https://www.uniprot.org/uniprotkb/Q8TBY8) (Polyamine-modulated factor 1-binding protein 1):

> Required for normal spermatogenesis. It functions as a scaffold protein that attaches the sperm head-tail connecting piece to the nuclear envelope, thus maintaining sperm head and tail integrity. May also be involved in the general organization of cellular cytoskeleton (By similarity).

**Summary**, from NCBI Gene [83449](https://www.ncbi.nlm.nih.gov/gene/83449):

> Involved in spermatogenesis. Located in sperm head-tail coupling apparatus; sperm midpiece; and sperm principal piece. Implicated in spermatogenic failure 31. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17728](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17728) · Entrez [83449](https://www.ncbi.nlm.nih.gov/gene/83449) · UniProt [Q8TBY8](https://www.uniprot.org/uniprotkb/Q8TBY8) · Ensembl [ENSG00000118557](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118557)

## Data

Gene col 4003: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4003); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4003, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4003]; `tensor/DDL_lfc|DDL_z.npy` [4003]; `embed/gene_vectors.npy` [4003]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4003 or target_col == 4003). Every well: [[PMFBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PMFBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
