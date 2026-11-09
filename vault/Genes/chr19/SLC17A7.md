---
symbol: "SLC17A7"
type: "gene"
col: 2518
ensembl_id: "ENSG00000104888"
name: "solute carrier family 17 member 7"
location: "19q13.33"
module: 1
arm: "-"
pooled_cpm: 2.14
n_lines_expressing: 41
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 25
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SLC17A7

*solute carrier family 17 member 7* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 11.6× (z +20.8, q 0e+00, up in 31 of 32 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (RPMI-7951 0.146×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.168×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDRG1]] (+0.72, fdr 1e-05), [[TNNI3]] (+0.68, fdr 3e-05), [[KLC3]] (+0.66, fdr 2e-05); moves opposite to [[DNAJC11]] (-0.70, fdr 7e-06), [[ALG8]] (-0.67, fdr 1e-05), [[ZNF507]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[NOVA2]] → it (grade B ⚠); 25 go from it, the strongest it → [[EPM2A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2518.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **11.6×** | +20.8 | 0e+00 | 31/32 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **10.6×** | +20.0 | 0e+00 | 34/35 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **7.60×** | +17.2 | 0e+00 | 27/31 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.45×** | +14.8 | 0e+00 | 15/20 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.32×** | +14.4 | 8e-45 | 24/33 (HT-29, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.70×** | +13.1 | 3e-37 | 31/33 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.81×** | +11.1 | 1e-26 | 22/26 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **3.16×** | +9.7 | 1e-20 | 19/23 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.18×** | +9.4 | 3e-19 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **4.83×** | +7.0 | 2e-10 | 19/27 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +5.8 | 3e-07 | 8/20 (SW480, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.58×** | +5.5 | 2e-06 | 8/33 (A-172, H4, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +5.4 | 2e-06 | 2/8 (PANC-1, A498) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +5.1 | 2e-05 | 9/24 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +4.9 | 4e-05 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.59×** | +3.9 | 0.003 | 7/31 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.025 | 7/33 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.038 | 3/33 (PANC-1, A-172, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.040 | 1/17 (C-33 A) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2518.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (RPMI-7951 0.146×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RPMI-7951 0.168×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.646× | -3.7 | 0.10 | 13/29 (SW480, A-427, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2518. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 1.51 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 20.1× (z +9.7) | — |
| [[SW480 (line)]] | alt | 3.83 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 19.3× (z +11.9) | — |
| [[A549 (line)]] | wt | 2.86 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 23.1× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 17.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -8.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 1.94 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 41.4× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 0.935 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 43.2× (z +8.7) | — |
| [[A-172 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.686 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.964 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.932 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.872 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.536 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.590 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.744 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.941 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2518), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG1]] | +0.72 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[TNNI3]] | +0.68 | +0.43 / +0.74 | both halves | 3e-05 |  |
| [[KLC3]] | +0.66 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[AHDC1]] | +0.66 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[RRAS]] | +0.65 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[DNAAF3]] | +0.65 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[FOXO6]] | +0.65 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[C14orf132]] | +0.65 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[SYP]] | +0.63 | +0.43 / +0.60 | both halves | 3e-05 | STRING 880 |
| [[SLC29A4]] | +0.62 | +0.44 / +0.66 | both halves | 3e-05 | pathway: SLC-mediated transmembrane transport |
| [[NXPH4]] | +0.62 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[RNF24]] | +0.61 | +0.51 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC11]] | -0.70 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[ALG8]] | -0.67 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[ZNF507]] | -0.65 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[UTP20]] | -0.65 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.63 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[ENOX2]] | -0.63 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[PSME3IP1]] | -0.62 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[MTHFSD]] | -0.62 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[UTP15]] | -0.62 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[MCCC2]] | -0.61 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[MAPKAPK5]] | -0.61 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[ST7L]] | -0.61 | -0.41 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOVA2]] | B | NOVA2 activity raises SLC17A7's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 1.83× lower at baseline in the lines without NOVA2 | 0.006 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[NXPH4]] | B | NXPH4 activity raises SLC17A7's level | lines that do not express NXPH4 (13) vs lines expressing it (37) | 1.61× lower at baseline in the lines without NXPH4 | 0.036 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent |
| [[C14orf132]] | B | C14orf132 activity raises SLC17A7's level | lines that do not express C14orf132 (19) vs lines expressing it (31) | 1.57× lower at baseline in the lines without C14orf132 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC22A17, ZFP28, ADAMTS7 |
| [[NDRG1]] | B | NDRG1 activity lowers SLC17A7's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.41× higher at baseline in the lines without NDRG1 | 0.071 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[C1QL1]] | B | C1QL1 activity raises SLC17A7's level | lines that do not express C1QL1 (22) vs lines expressing it (28) | 1.63× lower at baseline in the lines without C1QL1 | 0.087 | ⚠ within organs, on part of the lines; also absent: CPEB1, PDZD4, BARX1 |
| [[SUSD4]] | C | SUSD4 activity raises SLC17A7's level | lines that do not express SUSD4 (11) vs lines expressing it (39) | 1.84× lower at baseline in the lines without SUSD4 | 0.050 | ⚠ within organs, on part of the lines; also absent: SLC17A7, LINC00595, EBF4; maybe low, not absent; co-absent with the target |
| [[SLC2A1]] | C | SLC2A1 activity lowers SLC17A7's level | lines that do not express SLC2A1 (4) vs lines expressing it (46) | 1.50× higher at baseline in the lines without SLC2A1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 24, C 1. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPM2A]] | B | SLC17A7 activity raises EPM2A's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 2.05× lower at baseline in the lines without SLC17A7 | 0.007 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[FBXO30]] | B | SLC17A7 activity raises FBXO30's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 2.77× lower at baseline in the lines without SLC17A7 | 0.008 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[DPH5-DT]] | B | SLC17A7 activity raises DPH5-DT's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 1.45× lower at baseline in the lines without SLC17A7 | 0.015 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[ST7L]] | B | SLC17A7 activity raises ST7L's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 1.51× lower at baseline in the lines without SLC17A7 | 0.018 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[F11R]] | B | SLC17A7 activity lowers F11R's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 3.58× higher at baseline in the lines without SLC17A7 | 0.019 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[ABCF2]] | B | SLC17A7 activity raises ABCF2's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 1.58× lower at baseline in the lines without SLC17A7 | 0.027 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[SLC9B2]] | B | SLC17A7 activity raises SLC9B2's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 2.05× lower at baseline in the lines without SLC17A7 | 0.031 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[METAP1D]] | B | SLC17A7 activity raises METAP1D's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 1.74× lower at baseline in the lines without SLC17A7 | 0.037 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[MAST1]] | B | SLC17A7 activity raises MAST1's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 2.38× lower at baseline in the lines without SLC17A7 | 0.042 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[STK32C]] | B | SLC17A7 activity strengthens STK32C's drug response | lines that do not express SLC17A7 (8) vs lines expressing it (39) | the lines without SLC17A7 respond 0.81× as strongly (z diff +0.74); strongest at Homoharringtonine 5 µM: 1.31x vs 0.68x (z diff +5.1) | 0.048 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[VPS26C]] | B | SLC17A7 activity raises VPS26C's level | lines that do not express SLC17A7 (9) vs lines expressing it (41) | 1.34× lower at baseline in the lines without SLC17A7 | 0.060 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent |
| [[SLC9B2]] | B | SLC17A7 activity strengthens SLC9B2's drug response | lines that do not express SLC17A7 (8) vs lines expressing it (37) | the lines without SLC17A7 respond 0.53× as strongly (z diff +2.01); strongest at Panobinostat 5 µM: 0.76x vs 0.36x (z diff +5.3) | 0.063 | ⚠ within organs, on part of the lines; also absent: GXYLT2, ITGA10, NT5M; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.595). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (7.1, -3.5); signed map (-29.3, 20.4). **Vector** length 56.8, 10.5% of its response variance represented; |z| ≥ 3 in 884 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +14.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +11.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +20.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +20.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +13.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +7.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.1 | -0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +0.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -1.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 17 member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,429,401-49,442,360 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BNPI, VGLUT1 |
| Gene groups (HGNC) | Solute carrier family 17 |
| Reactome | 7 pathways, smallest: SLC-mediated transport of neurotransmitters; Glutamate Neurotransmitter Release Cycle; Neurotransmitter release cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2U7](https://www.uniprot.org/uniprotkb/Q9P2U7) (Vesicular glutamate transporter 1):

> Multifunctional transporter that transports L-glutamate as well as multiple ions such as chloride, proton, potassium, sodium and phosphate. At the synaptic vesicle membrane, mainly functions as an uniporter which transports preferentially L-glutamate but also phosphate from the cytoplasm into synaptic vesicles at presynaptic nerve terminals of excitatory neural cells (By similarity). The L-glutamate or phosphate uniporter activity is electrogenic and is driven by the proton electrochemical …

**Summary**, from NCBI Gene [57030](https://www.ncbi.nlm.nih.gov/gene/57030):

> The protein encoded by this gene is a vesicle-bound, sodium-dependent phosphate transporter that is specifically expressed in the neuron-rich regions of the brain. It is preferentially associated with the membranes of synaptic vesicles and functions in glutamate transport. The protein shares 82% identity with the differentiation-associated Na-dependent inorganic phosphate cotransporter and they appear to form a distinct class within the Na+/Pi cotransporter family. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16704](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16704) · Entrez [57030](https://www.ncbi.nlm.nih.gov/gene/57030) · UniProt [Q9P2U7](https://www.uniprot.org/uniprotkb/Q9P2U7) · Ensembl [ENSG00000104888](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104888)

## Data

Gene col 2518: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2518); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2518, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2518]; `tensor/DDL_lfc|DDL_z.npy` [2518]; `embed/gene_vectors.npy` [2518]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2518 or target_col == 2518). Every well: [[SLC17A7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC17A7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
