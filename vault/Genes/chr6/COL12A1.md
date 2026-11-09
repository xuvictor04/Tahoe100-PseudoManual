---
symbol: "COL12A1"
type: "gene"
col: 3283
ensembl_id: "ENSG00000111799"
name: "collagen type XII alpha 1 chain"
location: "6q13-q14.1"
module: 66
arm: "+"
pooled_cpm: 32.76
n_lines_expressing: 27
n_dd_up: 48
n_dd_down: 1
n_dd_up_clean: 36
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 16
direction_downstream: 7
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# COL12A1

*collagen type XII alpha 1 chain* — 6q13-q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 48 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 11.6× (z +44.6, q 0e+00, up in 25 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.804× (z -4.0, q 0.031, down in 8 of 25 measured lines) ⚠ cell-cycle shift, explains ~19% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.131×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFL2]] (+0.72, fdr 7e-06), [[ALPK2]] (+0.71, fdr 7e-06), [[THBS1]] (+0.68, fdr 7e-06); moves opposite to [[SS18L1]] (-0.60, fdr 3e-05), [[SMYD4]] (-0.59, fdr 3e-05), [[QPCTL]] (-0.56, fdr 2e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[PLCB4]] → it (grade B ⚠); 7 go from it, the strongest it → cells under [[Penfluridol (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 48 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3283.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **11.6×** | +44.6 | 0e+00 | 25/25 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.83×** | +22.7 | 0e+00 | 24/25 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.81×** | +16.5 | 0e+00 | 15/19 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.50×** | +16.1 | 0e+00 | 20/23 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.40×** | +15.9 | 0e+00 | 21/25 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **3.43×** | +15.3 | 0e+00 | 23/25 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.86×** | +12.5 | 8e-34 | 17/21 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +11.6 | 4e-29 | 15/25 (A-172, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.25×** | +10.4 | 1e-23 | 15/24 (HEC-1-A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.67×** | +10.4 | 2e-23 | 22/24 (BT-474, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.94×** | +8.5 | 1e-15 | 19/25 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.84×** | +7.8 | 3e-13 | 14/25 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.77×** | +6.8 | 3e-10 | 15/24 (BT-474, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.70×** | +6.8 | 3e-10 | 10/25 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.61×** | +6.1 | 4e-08 | 13/25 (A-427, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +6.1 | 4e-08 | 14/25 (NCI-H1792, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +5.4 | 2e-06 | 12/25 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +5.0 | 2e-05 | 14/23 (HOP62, J82, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3283.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.131×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.804×** | -4.0 | 0.031 | 8/25 (J82, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3283. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 25.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 45.9× (z +30.6) | — |
| [[A-172 (line)]] | wt | 21.9 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +23.7) | — |
| [[HEC-1-A (line)]] | alt | 18.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +22.4) | — |
| [[A-427 (line)]] | wt | 44.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +22.9) | — |
| [[HOP62 (line)]] | alt | 106 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +27.4) | — |
| [[HS-578T (line)]] | alt | 108 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +16.5) | — |
| [[A498 (line)]] | wt | 36.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.63× (z +19.4) | — |
| [[A549 (line)]] | wt | 9.24 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.7× (z +21.8) | — |
| [[LOX-IMVI (line)]] | wt | 67.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +24.4) | — |
| [[NCI-H2030 (line)]] | alt | 13.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 59.3× (z +28.1) | — |
| [[Panc 03.27 (line)]] | alt | 8.26 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.7× (z +16.7) | — |
| [[SK-MEL-2 (line)]] | alt | 62.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +17.3) | — |
| [[Hs 766T (line)]] | wt | 23.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.91× (z +15.5) | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.131× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 29.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +19.1) | — |
| [[SW 900 (line)]] | alt | 10.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +14.1) | — |
| [[BT-474 (line)]] | alt | 68.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +17.5) | — |
| [[H4 (line)]] | wt | 247 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 132 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +12.6) | — |
| [[J82 (line)]] | alt | 178 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.94× (z +18.1) | — |
| [[NCI-H1792 (line)]] | alt | 240 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.51× (z +10.6) ⚠ position not correctable | — |
| [[SNU-423 (line)]] | alt | 74.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +22.2) | — |
| [[SW 1088 (line)]] | alt | 81.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.24× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.96 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.37 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 51.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.15 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.41 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.81 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.34 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.51 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.00 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.11 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3283), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFL2]] | +0.72 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[ALPK2]] | +0.71 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[THBS1]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 529 |
| [[GFRA1]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[CALD1]] | +0.63 | +0.52 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[RBM24]] | +0.63 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[POSTN]] | +0.63 | +0.40 / +0.65 | both halves | 5e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 669 |
| [[TGFB2]] | +0.62 | +0.51 / +0.60 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[CDH2]] | +0.60 | +0.52 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[CAV1]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[CCDC50]] | +0.59 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[SYNE1]] | +0.59 | +0.62 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SS18L1]] | -0.60 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[SMYD4]] | -0.59 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[QPCTL]] | -0.56 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[RPP21]] | -0.55 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[C19orf25]] | -0.55 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[BAHD1]] | -0.55 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[NFATC3]] | -0.54 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[CCT6P3-1]] | -0.54 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[GPR89B]] | -0.54 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[UQCRH]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[MPG]] | -0.53 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[RABIF]] | -0.53 | -0.41 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 5, C 11. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLCB4]] | B | PLCB4 activity raises COL12A1's level | lines that do not express PLCB4 (13) vs lines expressing it (37) | 4.61× lower at baseline in the lines without PLCB4 | 0.061 | ⚠ within organs, on part of the lines; also absent: SLC39A8, ENSG00000248347, PKIA |
| [[TOP2A]] | B | TOP2A activity lowers COL12A1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLXDC2]] | B | PLXDC2 activity raises COL12A1's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 2.42× lower at baseline in the lines without PLXDC2 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent |
| [[KRT80]] | B | KRT80 activity lowers COL12A1's level | lines that do not express KRT80 (22) vs lines expressing it (28) | 3.13× higher at baseline in the lines without KRT80 | 0.093 | ⚠ within organs, on part of the lines; also absent: C19orf33, EPS8L2, SPNS2 |
| [[TRIM58]] | B | TRIM58 activity raises COL12A1's level | lines that do not express TRIM58 (31) vs lines expressing it (19) | 2.29× lower at baseline in the lines without TRIM58 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000235749, MME, FGF20 |
| [[ANGPT1]] | C | ANGPT1 activity raises COL12A1's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 5.31× lower at baseline in the lines without ANGPT1 | 0.006 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5; co-absent with the target |
| [[LUM]] | C | LUM activity raises COL12A1's level | lines that do not express LUM (34) vs lines expressing it (16) | 6.68× lower at baseline in the lines without LUM | 0.012 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2; co-absent with the target |
| [[GPR176]] | C | GPR176 activity raises COL12A1's level | lines that do not express GPR176 (18) vs lines expressing it (32) | 6.72× lower at baseline in the lines without GPR176 | 0.018 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, AFAP1L1; co-absent with the target |
| [[MAGI2-AS3]] | C | MAGI2-AS3 activity raises COL12A1's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 4.95× lower at baseline in the lines without MAGI2-AS3 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC; co-absent with the target |
| [[SYNPO]] | C | SYNPO activity raises COL12A1's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 3.98× lower at baseline in the lines without SYNPO | 0.051 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent; co-absent with the target |
| [[FBN2]] | C | FBN2 activity raises COL12A1's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 5.08× lower at baseline in the lines without FBN2 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent; co-absent with the target |
| [[RBMS3]] | C | RBMS3 activity raises COL12A1's level | lines that do not express RBMS3 (19) vs lines expressing it (31) | 6.29× lower at baseline in the lines without RBMS3 | 0.060 | ⚠ within organs, on part of the lines; also absent: RFTN1, PYGO1, LINC00472; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Penfluridol (drug)]] 5 µM | B | COL12A1 activity lowers the cells' numbers under Penfluridol 5 µM (makes them more sensitive) | lines that do not express COL12A1 (23) vs lines expressing it (25) | the lines without COL12A1: 1.23× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: RFTN1, FMN2, KIAA0408 |
| cells under [[c-Kit-IN-1 (drug)]] 0.05 µM | B | COL12A1 activity lowers the cells' numbers under c-Kit-IN-1 0.05 µM (makes them more sensitive) | lines that do not express COL12A1 (23) vs lines expressing it (25) | the lines without COL12A1: 1.49× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: RFTN1, FMN2, KIAA0408; cell counts less trustworthy |
| [[GPR176]] | C | COL12A1 activity raises GPR176's level | lines that do not express COL12A1 (23) vs lines expressing it (27) | 7.00× lower at baseline in the lines without COL12A1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: RFTN1, FMN2, KIAA0408; co-absent with the target |
| [[RBMS3]] | C | COL12A1 activity raises RBMS3's level | lines that do not express COL12A1 (23) vs lines expressing it (27) | 5.83× lower at baseline in the lines without COL12A1 | 0.019 | ⚠ within organs, on part of the lines; also absent: RFTN1, FMN2, KIAA0408; co-absent with the target |
| [[DSC3]] | C | COL12A1 activity raises DSC3's level | lines that do not express COL12A1 (23) vs lines expressing it (27) | 1.61× lower at baseline in the lines without COL12A1 | 0.060 | ⚠ within organs, on part of the lines; also absent: RFTN1, FMN2, KIAA0408; co-absent with the target |
| [[BDNF]] | C | COL12A1 activity raises BDNF's level | lines that do not express COL12A1 (23) vs lines expressing it (27) | 3.20× lower at baseline in the lines without COL12A1 | 0.072 | ⚠ within organs, on part of the lines; also absent: RFTN1, FMN2, KIAA0408; co-absent with the target |
| [[FSTL1]] | C | COL12A1 activity raises FSTL1's level | lines that do not express COL12A1 (23) vs lines expressing it (27) | 5.45× lower at baseline in the lines without COL12A1 | 0.090 | ⚠ within organs, on part of the lines; also absent: RFTN1, FMN2, KIAA0408; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.765). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.1, 21.2); signed map (44.3, 19.6). **Vector** length 88.2, 26.9% of its response variance represented; |z| ≥ 3 in 736 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NCAM1 interactions* (reactome, mean cos +0.50 to 5); *angiogenesis* (hallmark, mean cos +0.53 to 5); *NCAM signaling for neurite out-growth* (reactome, mean cos +0.50 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.6 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.3 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.2 | +16.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +15.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +44.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.2 | +4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.2 | +4.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -0.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -3.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.7 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | collagen type XII alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q13-q14.1 — chr6:75,084,326-75,206,267 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously COL12A1L |
| Gene groups (HGNC) | Fibronectin type III domain containing; Collagen proteoglycans; Fibril associated collagens with interrupted triple helices |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 7 pathways, smallest: Collagen chain trimerization; Collagen degradation; Assembly of collagen fibrils and other multimeric structures |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99715](https://www.uniprot.org/uniprotkb/Q99715) (Collagen alpha-1(XII) chain):

> Type XII collagen interacts with type I collagen-containing fibrils, the COL1 domain could be associated with the surface of the fibrils, and the COL2 and NC3 domains may be localized in the perifibrillar matrix.

**Summary**, from NCBI Gene [1303](https://www.ncbi.nlm.nih.gov/gene/1303):

> This gene encodes the alpha chain of type XII collagen, a member of the FACIT (fibril-associated collagens with interrupted triple helices) collagen family. Type XII collagen is a homotrimer found in association with type I collagen, an association that is thought to modify the interactions between collagen I fibrils and the surrounding matrix. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2188) · Entrez [1303](https://www.ncbi.nlm.nih.gov/gene/1303) · UniProt [Q99715](https://www.uniprot.org/uniprotkb/Q99715) · Ensembl [ENSG00000111799](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111799)

## Data

Gene col 3283: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3283); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3283, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3283]; `tensor/DDL_lfc|DDL_z.npy` [3283]; `embed/gene_vectors.npy` [3283]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3283 or target_col == 3283). Every well: [[COL12A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL12A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
