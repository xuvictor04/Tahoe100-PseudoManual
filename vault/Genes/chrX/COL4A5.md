---
symbol: "COL4A5"
type: "gene"
col: 11979
ensembl_id: "ENSG00000188153"
name: "collagen type IV alpha 5 chain"
location: "Xq22.3"
module: 19
arm: "+"
pooled_cpm: 95.26
n_lines_expressing: 24
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 9
direction_downstream: 3
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# COL4A5

*collagen type IV alpha 5 chain* — Xq22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.41× (z +7.0, q 2e-09, up in 12 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.564× (z -11.6, q 3e-28, down in 17 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL4A6]] (+0.69, fdr 7e-06, ⚠ same locus), [[HORMAD1]] (+0.61, fdr 1e-05), [[PDE4B]] (+0.59, fdr 1e-05), [[ZFHX4]] (+0.59, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TXLNGY]] → it (grade B ⚠); 3 go from it, the strongest it → [[COL4A6]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11979.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +7.0 | 2e-09 | 12/22 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.1 | 2e-07 | 2/22 (J82, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +5.8 | 1e-06 | 3/20 (HOP62, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.43×** | +5.1 | 6e-05 | 13/23 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.0 | 8e-05 | 15/22 (A498, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.005 | 1/24 (A498) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.044 | 11/22 (NCI-H1792, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.044 | 10/21 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | 1.27× | +3.1 | 0.11 | 3/20 (HOP62, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Busulfan (drug)]] 0.05 µM |  | 1.25× | +3.1 | 0.11 | 6/23 (NCI-H1573, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11979.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.564×** | -11.6 | 3e-28 | 17/22 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.646×** | -6.2 | 1e-07 | 10/22 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.675×** | -5.6 | 4e-06 | 13/22 (NCI-H460, CHP-212, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.718×** | -4.7 | 3e-04 | 14/22 (NCI-H460, CHP-212, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.719×** | -4.5 | 6e-04 | 11/22 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.746×** | -4.2 | 0.003 | 12/22 (NCI-H460, CHP-212, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.748×** | -4.1 | 0.003 | 16/22 (NCI-H460, AN3 CA, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.749×** | -4.1 | 0.003 | 5/22 (C32, Hs 766T, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.830×** | -3.8 | 0.010 | 10/22 (NCI-H2030, hTERT-HPNE, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.782×** | -3.5 | 0.024 | 15/20 (CHP-212, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.785×** | -3.5 | 0.026 | 7/22 (C32, SW 1088, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.786×** | -3.4 | 0.026 | 1/21 (Panc 03.27) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.803×** | -3.1 | 0.073 | 7/22 (AN3 CA, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.800×** | -3.1 | 0.083 | 3/22 (C-33 A, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11979. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1,019 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -25.1) |
| [[CHP-212 (line)]] | wt | 485 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -14.9) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.216× (z -9.1) |
| [[AN3 CA (line)]] | alt | 274 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -16.6) |
| [[C32 (line)]] | wt | 106 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -23.5) |
| [[A-427 (line)]] | wt | 83.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +12.5) | — |
| [[A498 (line)]] | wt | 51.7 | 2 (1 ⚠) | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +9.9) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.31× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -16.2) |
| [[A549 (line)]] | wt | 124 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 86.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0866× (z -26.8) |
| [[NCI-H1792 (line)]] | alt | 96.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -14.0) |
| [[HOP62 (line)]] | alt | 91.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -10.9) |
| [[Hs 766T (line)]] | wt | 206 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 83.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -12.4) |
| [[SW 1271 (line)]] | alt | 54.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0537× (z -9.2) |
| [[A-172 (line)]] | wt | 17.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.69 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.6 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.62 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.04 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 82.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.55 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 20.5 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.39 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.05 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.09 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.91 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.79 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 82.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.7 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.08 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.65 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.54 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 20.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 7.34 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.37 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11979), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL4A6]] | +0.69 | +0.62 / +0.76 | both halves | 7e-06 | same gene group; pathway: Anchoring fibril formation; STRING 982; ⚠ same locus (0.3 kb: neighbours can correlate without regulation) |
| [[HORMAD1]] | +0.61 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[PDE4B]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ZFHX4]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[PALMD]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[GASK1B-AS1]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[LAMB4]] | +0.58 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[HERC2P3-1]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[NCKAP5]] | +0.58 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[THSD7A]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[PDE7B]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[NRG1]] | +0.56 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[GLP2R]] | +0.56 | +0.50 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TXLNGY]] | B | TXLNGY activity raises COL4A5's level | lines that do not express TXLNGY (30) vs lines expressing it (20) | 1.82× lower at baseline in the lines without TXLNGY | 0.077 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |
| [[COL4A6]] | C | COL4A6 activity raises COL4A5's level | lines that do not express COL4A6 (36) vs lines expressing it (14) | 6.08× lower at baseline in the lines without COL4A6 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX7, ENSG00000238054, LINC01035; co-absent with the target |
| [[PDE4B]] | C | PDE4B activity raises COL4A5's level | lines that do not express PDE4B (24) vs lines expressing it (26) | 2.92× lower at baseline in the lines without PDE4B | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCSK2, MAPK4, UNC5D; co-absent with the target |
| [[MAPK4]] | C | MAPK4 activity raises COL4A5's level | lines that do not express MAPK4 (35) vs lines expressing it (15) | 4.05× lower at baseline in the lines without MAPK4 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000289418, SLC15A5, LHFPL3-AS1; co-absent with the target |
| [[HMCN1]] | C | HMCN1 activity raises COL4A5's level | lines that do not express HMCN1 (26) vs lines expressing it (24) | 3.48× lower at baseline in the lines without HMCN1 | 0.059 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent; co-absent with the target |
| [[FAT4]] | C | FAT4 activity raises COL4A5's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 5.35× lower at baseline in the lines without FAT4 | 0.062 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11; co-absent with the target |
| [[COL5A2]] | C | COL5A2 activity raises COL4A5's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 3.19× lower at baseline in the lines without COL5A2 | 0.069 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2; co-absent with the target |
| [[FBXL7]] | C | FBXL7 activity raises COL4A5's level | lines that do not express FBXL7 (27) vs lines expressing it (23) | 3.34× lower at baseline in the lines without FBXL7 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, HS3ST3A1, FAM133A; co-absent with the target |
| [[KCNJ6]] | C | KCNJ6 activity raises COL4A5's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 3.72× lower at baseline in the lines without KCNJ6 | 0.092 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL4A6]] | C | COL4A5 activity raises COL4A6's level | lines that do not express COL4A5 (26) vs lines expressing it (24) | 3.61× lower at baseline in the lines without COL4A5 | 0.029 | ⚠ within organs, on part of the lines; also absent: COL4A6, ADAM23, GJA1; co-absent with the target |
| [[FBXL7]] | C | COL4A5 activity raises FBXL7's level | lines that do not express COL4A5 (26) vs lines expressing it (24) | 3.26× lower at baseline in the lines without COL4A5 | 0.086 | ⚠ within organs, on part of the lines; also absent: COL4A6, ADAM23, GJA1; co-absent with the target |
| [[HMCN1]] | C | COL4A5 activity raises HMCN1's level | lines that do not express COL4A5 (26) vs lines expressing it (24) | 2.63× lower at baseline in the lines without COL4A5 | 0.089 | ⚠ within organs, on part of the lines; also absent: COL4A6, ADAM23, GJA1; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.9, 36.8); signed map (40.1, 42.6). **Vector** length 75.3, 24.2% of its response variance represented; |z| ≥ 3 in 577 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.9 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.5 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | +7.5 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +0.3 |
|  | [[Vitamin K4 (drug)]] 0.05 µM |  | +1.9 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +3.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -2.1 | -4.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -1.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.0 | -5.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -0.8 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.7 | -1.4 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | collagen type IV alpha 5 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.3 — chrX:108,439,838-108,697,545 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ASLN, ATS |
| Gene groups (HGNC) | Network forming collagens |
| Reactome | 26 pathways, smallest: Anchoring fibril formation; Crosslinking of collagen fibrils; Fibronectin matrix formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P29400](https://www.uniprot.org/uniprotkb/P29400) (Collagen alpha-5(IV) chain):

> Type IV collagen is the major structural component of glomerular basement membranes (GBM), forming a 'chicken-wire' meshwork together with laminins, proteoglycans and entactin/nidogen.

**Summary**, from NCBI Gene [1287](https://www.ncbi.nlm.nih.gov/gene/1287):

> This gene encodes one of the six subunits of type IV collagen, the major structural component of basement membranes. Mutations in this gene are associated with X-linked Alport syndrome, also known as hereditary nephritis. Like the other members of the type IV collagen gene family, this gene is organized in a head-to-head conformation with another type IV collagen gene so that each gene pair shares a common promoter. Alternatively spliced transcript variants have been identified for this gene. …

**Accessions** — [HGNC:2207](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2207) · Entrez [1287](https://www.ncbi.nlm.nih.gov/gene/1287) · UniProt [P29400](https://www.uniprot.org/uniprotkb/P29400) · Ensembl [ENSG00000188153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188153)

## Data

Gene col 11979: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11979); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11979, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11979]; `tensor/DDL_lfc|DDL_z.npy` [11979]; `embed/gene_vectors.npy` [11979]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11979 or target_col == 11979). Every well: [[COL4A5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL4A5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
