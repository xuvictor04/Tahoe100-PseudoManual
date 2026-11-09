---
symbol: "CDH11"
type: "gene"
col: 6463
ensembl_id: "ENSG00000140937"
name: "cadherin 11"
location: "16q21"
module: 19
arm: "+"
pooled_cpm: 132.63
n_lines_expressing: 14
n_dd_up: 6
n_dd_down: 28
n_dd_up_clean: 3
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 20
direction_downstream: 10
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# CDH11

*cadherin 11* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.35× (z +10.0, q 5e-21, up in 1 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.32× (z +4.7, q 4e-04, up in 6 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.458× (z -9.2, q 3e-17, down in 8 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE7B]] (+0.77, fdr 7e-06), [[COL4A6]] (+0.77, fdr 7e-06), [[GLP2R]] (+0.73, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 10 go from it, the strongest it → [[LINC00922]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6463.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.35×** | +10.0 | 5e-21 | 1/13 (HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +7.2 | 1e-10 | 1/11 (HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +6.8 | 2e-09 | 1/11 (HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +4.7 | 4e-04 | 6/12 (LS 180, H4, …) | rises with dose |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.44×** | +4.3 | 0.002 | 0/13 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.61×** | +4.0 | 0.006 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.66× | +3.1 | 0.15 | 1/9 (HS-578T) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 4 with an alert ⚠; shown: the 15 strongest. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6463.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.458×** | -9.2 | 3e-17 | 8/12 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.519×** | -7.7 | 4e-12 | 10/12 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.523×** | -7.6 | 5e-12 | 10/12 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.537×** | -7.3 | 5e-11 | 10/12 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.693×** | -6.1 | 1e-07 | 9/12 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.593×** | -5.7 | 1e-06 | 2/12 (NCI-H23, Hs 766T) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.645×** | -5.1 | 2e-05 | 6/12 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.688×** | -4.4 | 8e-04 | 6/12 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.689×** | -4.3 | 0.001 | 4/14 (NCI-H596, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.705×** | -4.1 | 0.002 | 2/12 (Hs 766T, HOP62) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.706×** | -4.1 | 0.002 | 2/11 (NCI-H460, SW 900) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.706×** | -4.1 | 0.002 | 5/12 (Hs 766T, A498, …) | top dose only | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **0.786×** | -4.0 | 0.003 | 4/12 (Hs 766T, A498, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.786×** | -3.9 | 0.003 | 1/12 (Hs 766T) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.727×** | -3.7 | 0.007 | 3/12 (H4, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6463. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1,831 | 0 | 15 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0474× (z -26.0) |
| [[A-172 (line)]] | wt | 75.7 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +15.6) | [[Panobinostat (drug)]] 5 µM 0.241× (z -9.8) |
| [[SW 900 (line)]] | alt | 537 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -12.8) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.167× (z -11.6) |
| [[Hs 766T (line)]] | wt | 383 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -12.0) |
| [[LS 180 (line)]] | wt | 133 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.248× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 65.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -8.9) |
| [[HS-578T (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -11.1) ⚠ cell-cycle shift, explains ~66% of this change |
| [[A-427 (line)]] | wt | 9.87 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 68.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 28.3 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 25.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.98 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.1 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.13 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 13.0 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 27.9 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 16.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.78 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 17.9 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 8.85 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.60 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 22.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 27.6 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 21.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 286 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 24.5 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 15.4 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 18.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6463), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE7B]] | +0.77 | +0.66 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[COL4A6]] | +0.77 | +0.70 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[GLP2R]] | +0.73 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[LINC03000]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[CDH7]] | +0.70 | +0.62 / +0.62 | both halves | 7e-06 | same gene group; pathway: Adherens junctions interactions; STRING 715 |
| [[KCNK2]] | +0.70 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[GREM2]] | +0.67 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[SERPINB11]] | +0.67 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[PAK3]] | +0.67 | +0.60 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[ADGRD1]] | +0.65 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[PDE1A]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[P3H2]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 1, C 19. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers CDH11's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.0% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds |
| [[FENDRR]] | C | FENDRR activity raises CDH11's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 4.77× lower at baseline in the lines without FENDRR | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10; co-absent with the target |
| [[GREM2]] | C | GREM2 activity raises CDH11's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 5.16× lower at baseline in the lines without GREM2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[CTNND2]] | C | CTNND2 activity raises CDH11's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 5.45× lower at baseline in the lines without CTNND2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises CDH11's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 6.93× lower at baseline in the lines without GTF2I-AS1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[GSG1L2]] | C | GSG1L2 activity raises CDH11's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 8.01× lower at baseline in the lines without GSG1L2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[SHISAL1]] | C | SHISAL1 activity raises CDH11's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 3.83× lower at baseline in the lines without SHISAL1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises CDH11's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 3.56× lower at baseline in the lines without C5orf46 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[LINC01257]] | C | LINC01257 activity raises CDH11's level | lines that do not express LINC01257 (31) vs lines expressing it (19) | 2.86× lower at baseline in the lines without LINC01257 | 0.036 | ⚠ within organs, on part of the lines; also absent: MIR3667HG, LINC01446, NAA11; maybe low, not absent; co-absent with the target |
| [[SCARA5]] | C | SCARA5 activity raises CDH11's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 4.56× lower at baseline in the lines without SCARA5 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises CDH11's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 6.56× lower at baseline in the lines without LINC03000 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[MARCOL]], [[SPINK13]] | C | MARCOL, SPINK13 activity raises CDH11's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 5.95× lower at baseline in the lines without MARCOL, SPINK13 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00922]] | B | CDH11 activity raises LINC00922's level | lines that do not express CDH11 (36) vs lines expressing it (14) | 1.49× lower at baseline in the lines without CDH11 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX11, ENSG00000253693, ENSG00000238054 |
| [[PAK3]] | C | CDH11 activity raises PAK3's level | lines that do not express CDH11 (36) vs lines expressing it (14) | 3.31× lower at baseline in the lines without CDH11 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX11, ENSG00000253693, ENSG00000238054; co-absent with the target |
| [[SULF1]] | C | CDH11 activity raises SULF1's level | lines that do not express CDH11 (36) vs lines expressing it (14) | 2.69× lower at baseline in the lines without CDH11 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX11, ENSG00000253693, ENSG00000238054; co-absent with the target |
| [[FENDRR]] | C | CDH11 activity raises FENDRR's level | lines that do not express CDH11 (36) vs lines expressing it (14) | 2.39× lower at baseline in the lines without CDH11 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX11, ENSG00000253693, ENSG00000238054; co-absent with the target |
| [[GNG11]] | C | CDH11 activity raises GNG11's level | lines that do not express CDH11 (36) vs lines expressing it (14) | 3.95× lower at baseline in the lines without CDH11 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX11, ENSG00000253693, ENSG00000238054; co-absent with the target |
| [[ESM1]] | C | CDH11 activity raises ESM1's level | lines that do not express CDH11 (36) vs lines expressing it (14) | 2.23× lower at baseline in the lines without CDH11 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX11, ENSG00000253693, ENSG00000238054; co-absent with the target |
| [[C5orf46]] | C | CDH11 activity raises C5orf46's level | lines that do not express CDH11 (36) vs lines expressing it (14) | 2.28× lower at baseline in the lines without CDH11 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX11, ENSG00000253693, ENSG00000238054; co-absent with the target |
| [[PAX7]] | C | CDH11 activity raises PAX7's level | lines that do not express CDH11 (36) vs lines expressing it (14) | 1.87× lower at baseline in the lines without CDH11 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX11, ENSG00000253693, ENSG00000238054; co-absent with the target |
| [[BMPER]] | C | CDH11 activity raises BMPER's level | lines that do not express CDH11 (36) vs lines expressing it (14) | 2.57× lower at baseline in the lines without CDH11 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX11, ENSG00000253693, ENSG00000238054; co-absent with the target |
| [[COL4A6]] | C | CDH11 activity raises COL4A6's level | lines that do not express CDH11 (36) vs lines expressing it (14) | 3.14× lower at baseline in the lines without CDH11 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX11, ENSG00000253693, ENSG00000238054; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.805). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.2, 35.0); signed map (41.7, 44.2). **Vector** length 54.4, 21.2% of its response variance represented; |z| ≥ 3 in 311 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.51 to 18).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +3.5 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.1 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -5.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | cadherin 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:64,943,753-65,126,112 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OB, CAD11 |
| Gene groups (HGNC) | Type II classical cadherins |
| Hallmark sets | APICAL_JUNCTION, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 13 pathways, smallest: CDH11 homotypic and heterotypic interactions; Regulation of CDH11 gene transcription; Regulation of CDH11 mRNA translation by microRNAs |
| Matched by | ensembl_id |

**Function**, from UniProt [P55287](https://www.uniprot.org/uniprotkb/P55287) (Cadherin-11):

> Cadherins are calcium-dependent cell adhesion proteins. They preferentially interact with themselves in a homophilic manner in connecting cells; cadherins may thus contribute to the sorting of heterogeneous cell types. Required for proper focal adhesion assembly. Involved in the regulation of cell migration.

**Summary**, from NCBI Gene [1009](https://www.ncbi.nlm.nih.gov/gene/1009):

> This gene encodes a type II classical cadherin from the cadherin superfamily, integral membrane proteins that mediate calcium-dependent cell-cell adhesion. Mature cadherin proteins are composed of a large N-terminal extracellular domain, a single membrane-spanning domain, and a small, highly conserved C-terminal cytoplasmic domain. Type II (atypical) cadherins are defined based on their lack of a HAV cell adhesion recognition sequence specific to type I cadherins. Expression of this particular …

**Accessions** — [HGNC:1750](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1750) · Entrez [1009](https://www.ncbi.nlm.nih.gov/gene/1009) · UniProt [P55287](https://www.uniprot.org/uniprotkb/P55287) · Ensembl [ENSG00000140937](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140937)

## Data

Gene col 6463: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6463); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6463, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6463]; `tensor/DDL_lfc|DDL_z.npy` [6463]; `embed/gene_vectors.npy` [6463]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6463 or target_col == 6463). Every well: [[CDH11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDH11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
