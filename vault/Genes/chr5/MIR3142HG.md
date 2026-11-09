---
symbol: "MIR3142HG"
type: "gene"
col: 14810
ensembl_id: "ENSG00000253522"
name: "MIR3142 host gene"
location: "5q33.3"
module: 112
arm: "+"
pooled_cpm: 13.37
n_lines_expressing: 24
n_dd_up: 23
n_dd_down: 16
n_dd_up_clean: 18
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 18
direction_downstream: 21
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# MIR3142HG

*MIR3142 host gene* — 5q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.46× (z +11.2, q 2e-26, up in 11 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.576× (z -4.9, q 5e-04, down in 10 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSF2]] (+0.75, fdr 7e-06), [[TRAF1]] (+0.62, fdr 9e-06), [[LIF]] (+0.61, fdr 1e-05); moves opposite to [[RUBCN]] (-0.45, fdr 4e-05), [[CMKLR2]] (-0.45, fdr 4e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 21 go from it, the strongest it → [[ITSN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14810.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.46×** | +11.2 | 2e-26 | 11/22 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.69×** | +8.4 | 1e-14 | 16/21 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +7.8 | 1e-12 | 10/20 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.42×** | +7.2 | 1e-10 | 2/16 (SK-MEL-2, C32) | inconsistent across doses | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.71×** | +6.6 | 3e-09 | 12/22 (NCI-H2347, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +5.9 | 4e-07 | 14/22 (SW 900, C32, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.87×** | +5.5 | 3e-06 | 12/21 (SW 900, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.3 | 8e-06 | 4/21 (NCI-H2030, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.87×** | +5.3 | 8e-06 | 12/20 (HS-578T, SK-MEL-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.74×** | +4.6 | 2e-04 | 10/20 (HS-578T, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.68×** | +4.6 | 2e-04 | 14/20 (SW 900, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.68×** | +4.6 | 2e-04 | 11/20 (NCI-H1792, SW 900, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +4.3 | 7e-04 | 10/20 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.3 | 7e-04 | 11/20 (HS-578T, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.0 | 0.002 | 6/19 (NCI-H2347, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.58×** | +3.8 | 0.004 | 6/20 (HepG2/C3A, SW 900, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +3.7 | 0.009 | 8/20 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.013 | 9/20 (SW 900, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.46×** | +3.3 | 0.026 | 8/20 (HOP62, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14810.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.576×** | -4.9 | 5e-04 | 10/22 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.604×** | -4.5 | 0.002 | 8/20 (H4, RPMI-7951, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.587×** | -4.4 | 0.002 | 12/20 (H4, RPMI-7951, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.621×** | -4.2 | 0.003 | 13/20 (NCI-H2030, LOX-IMVI, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.633×** | -4.1 | 0.006 | 8/21 (H4, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.638×** | -4.0 | 0.006 | 15/21 (SK-MEL-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.662×** | -3.7 | 0.020 | 8/21 (H4, RPMI-7951, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.668×** | -3.6 | 0.024 | 11/20 (H4, Panc 03.27, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.895× | -3.5 | 0.025 | 3/22 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.669×** | -3.4 | 0.033 | 7/20 (HOP62, SW 900, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.681×** | -3.4 | 0.033 | 5/20 (H4, SNU-423, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.683×** | -3.4 | 0.033 | 9/20 (H4, NCI-H1792, …) | all doses, flat |  |
| [[Hesperidin (drug)]] 0.05 µM |  | **0.666×** | -3.3 | 0.037 | 10/20 (NCI-H2347, SNU-423, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.729×** | -3.3 | 0.043 | 12/22 (A498, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.770×** | -3.3 | 0.043 | 5/22 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.516×** | -3.1 | 0.078 | 4/22 (HOP62, SW 900, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14810. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 39.7 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0595× (z -11.0) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0775× (z -10.0) |
| [[C32 (line)]] | wt | 67.8 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0746× (z -12.8) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.114× (z -10.7) |
| [[RPMI-7951 (line)]] | alt | 83.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0117× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.140× (z -9.0) |
| [[H4 (line)]] | wt | 25.7 | 0 | 3 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0353× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 202 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.108× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.32× (z +10.3) | — |
| [[HEC-1-A (line)]] | alt | 7.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 31.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 5.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 4.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +10.4) | — |
| [[SW 900 (line)]] | alt | 76.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -8.9) |
| [[A-172 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.910 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.44 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14810), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSF2]] | +0.75 | +0.80 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[TRAF1]] | +0.62 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[LIF]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[MIR155HG]] | +0.61 | +0.65 / +0.57 | both halves | 1e-05 | same gene group |
| [[IL1A]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[SLC43A3]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[LINC00973]] | +0.60 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[IRAK2]] | +0.60 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[GATM]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[LIF-AS2]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[CXCL8]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[CLEC2D]] | +0.59 | +0.40 / +0.64 | both halves | 5e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RUBCN]] | -0.45 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[CMKLR2]] | -0.45 | -0.42 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 2, C 16. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers MIR3142HG's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.8% of all compounds | 0.028 | ⚠ off-target possible; 3 compounds |
| [[CA8]] | B | CA8 activity raises MIR3142HG's level | lines that do not express CA8 (27) vs lines expressing it (23) | 2.12× lower at baseline in the lines without CA8 | 0.064 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[EVA1A]] | C | EVA1A activity raises MIR3142HG's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 4.37× lower at baseline in the lines without EVA1A | 0.009 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2; co-absent with the target |
| [[BCL2A1]] | C | BCL2A1 activity raises MIR3142HG's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 3.95× lower at baseline in the lines without BCL2A1 | 0.023 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1; co-absent with the target |
| [[RDUR]] | C | RDUR activity raises MIR3142HG's level | lines that do not express RDUR (28) vs lines expressing it (22) | 4.15× lower at baseline in the lines without RDUR | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LNCOG, ENSG00000287622, GYPC; co-absent with the target |
| [[PLAU]] | C | PLAU activity raises MIR3142HG's level | lines that do not express PLAU (26) vs lines expressing it (24) | 2.08× lower at baseline in the lines without PLAU | 0.029 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3; co-absent with the target |
| [[PLPP4]] | C | PLPP4 activity raises MIR3142HG's level | lines that do not express PLPP4 (31) vs lines expressing it (19) | 3.62× lower at baseline in the lines without PLPP4 | 0.031 | ⚠ within organs, on part of the lines; also absent: GYPC, LINC02930, TNFAIP6; co-absent with the target |
| [[HMGN2P46]] | C | HMGN2P46 activity raises MIR3142HG's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 2.82× lower at baseline in the lines without HMGN2P46 | 0.033 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC; co-absent with the target |
| [[ITGA1]] | C | ITGA1 activity raises MIR3142HG's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 3.49× lower at baseline in the lines without ITGA1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973; co-absent with the target |
| [[TNFRSF9]] | C | TNFRSF9 activity raises MIR3142HG's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 2.66× lower at baseline in the lines without TNFRSF9 | 0.040 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2; co-absent with the target |
| [[SLC43A3]] | C | SLC43A3 activity raises MIR3142HG's level | lines that do not express SLC43A3 (28) vs lines expressing it (22) | 3.52× lower at baseline in the lines without SLC43A3 | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261; co-absent with the target |
| [[ROR1-AS1]] | C | ROR1-AS1 activity raises MIR3142HG's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 3.00× lower at baseline in the lines without ROR1-AS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 9, C 12. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITSN1]] | B | MIR3142HG activity lowers ITSN1's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 1.23× higher at baseline in the lines without MIR3142HG | 0.013 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130 |
| [[SMAD3]] | B | MIR3142HG activity raises SMAD3's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 2.15× lower at baseline in the lines without MIR3142HG | 0.016 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130 |
| [[DUSP10]] | B | MIR3142HG activity raises DUSP10's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 2.87× lower at baseline in the lines without MIR3142HG | 0.020 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130 |
| [[LINC02605]] | B | MIR3142HG activity raises LINC02605's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 2.35× lower at baseline in the lines without MIR3142HG | 0.026 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130 |
| [[CLEC2D]] | B | MIR3142HG activity raises CLEC2D's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 2.27× lower at baseline in the lines without MIR3142HG | 0.030 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130 |
| [[ZNF697]] | B | MIR3142HG activity raises ZNF697's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 2.00× lower at baseline in the lines without MIR3142HG | 0.045 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130 |
| [[CD82]] | B | MIR3142HG activity raises CD82's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 2.35× lower at baseline in the lines without MIR3142HG | 0.058 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130 |
| [[IRAK2]] | B | MIR3142HG activity raises IRAK2's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 2.18× lower at baseline in the lines without MIR3142HG | 0.062 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130 |
| [[CXCL3]] | B | MIR3142HG activity raises CXCL3's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 1.78× lower at baseline in the lines without MIR3142HG | 0.084 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130 |
| [[CSF2]] | C | MIR3142HG activity raises CSF2's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 3.22× lower at baseline in the lines without MIR3142HG | 0.003 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130; co-absent with the target |
| [[ITGA1]] | C | MIR3142HG activity raises ITGA1's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 3.51× lower at baseline in the lines without MIR3142HG | 0.005 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130; co-absent with the target |
| [[HMGN2P46]] | C | MIR3142HG activity raises HMGN2P46's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 3.29× lower at baseline in the lines without MIR3142HG | 0.007 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130; co-absent with the target |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.709). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.9, 1.1); signed map (41.4, 13.0). **Vector** length 68.9, 19.9% of its response variance represented; |z| ≥ 3 in 583 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.55 to 11); *Interleukin-10 signaling* (reactome, mean cos +0.61 to 5); *KRAS signaling up* (hallmark, mean cos +0.55 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.8 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +6.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.4 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +7.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | -0.3 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -4.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.2 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -3.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -1.9 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | MIR3142 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q33.3 — chr5:160,438,594-160,487,426 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [107075116](https://www.ncbi.nlm.nih.gov/gene/107075116):

> Predicted to be involved in miRNA-mediated post-transcriptional gene silencing. Predicted to be part of RISC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:51944](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51944) · Entrez [107075116](https://www.ncbi.nlm.nih.gov/gene/107075116) · Ensembl [ENSG00000253522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253522)

## Data

Gene col 14810: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14810); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14810, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14810]; `tensor/DDL_lfc|DDL_z.npy` [14810]; `embed/gene_vectors.npy` [14810]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14810 or target_col == 14810). Every well: [[MIR3142HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR3142HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
