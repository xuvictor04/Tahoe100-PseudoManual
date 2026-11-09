---
symbol: "EFNB1"
type: "gene"
col: 1637
ensembl_id: "ENSG00000090776"
name: "ephrin B1"
location: "Xq13.1"
module: 31
arm: "+"
pooled_cpm: 14.15
n_lines_expressing: 44
n_dd_up: 21
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 15
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# EFNB1

*ephrin B1* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.41× (z +14.3, q 2e-43, up in 29 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.652× (z -4.9, q 6e-04, down in 22 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NECTIN1]] (+0.65, fdr 7e-06), [[PLK3]] (+0.63, fdr 7e-06), [[SULF2]] (+0.59, fdr 1e-05); moves opposite to [[SYMPK]] (-0.49, fdr 3e-05), [[NUP42]] (-0.48, fdr 4e-05), [[IFT81]] (-0.46, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[SERPINB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1637.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.41×** | +14.3 | 2e-43 | 29/37 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +10.5 | 4e-23 | 20/37 (Panc 03.27, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.07×** | +8.3 | 1e-14 | 27/42 (SW1417, PANC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +7.6 | 5e-12 | 17/32 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +7.3 | 2e-11 | 21/35 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.71×** | +5.9 | 3e-07 | 18/36 (NCI-H460, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.66×** | +5.8 | 5e-07 | 19/42 (SW1417, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +5.5 | 3e-06 | 18/41 (PANC-1, NCI-H2347, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.59×** | +5.3 | 8e-06 | 15/41 (SW1417, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +5.1 | 2e-05 | 14/39 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.8 | 7e-05 | 19/42 (RKO, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +4.7 | 1e-04 | 18/35 (A-427, SNU-423, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +4.6 | 2e-04 | 14/42 (HOP62, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +4.5 | 2e-04 | 9/42 (NCI-H460, LOX-IMVI, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.50×** | +4.5 | 3e-04 | 14/40 (HS-578T, Panc 03.27, …) | inconsistent across doses | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.08×** | +4.4 | 4e-04 | 16/39 (Hs 766T, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +3.9 | 0.003 | 14/40 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.007 | 13/40 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.77×** | +3.4 | 0.017 | 9/36 (LS 180, COLO 205, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1637.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.652×** | -4.9 | 6e-04 | 22/42 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.674×** | -4.5 | 0.002 | 19/40 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.669×** | -4.4 | 0.002 | 17/39 (AN3 CA, AsPC-1, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.671×** | -4.4 | 0.002 | 14/16 (LS 180, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.686×** | -4.3 | 0.002 | 20/41 (Hs 766T, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.732×** | -3.6 | 0.033 | 12/40 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.745×** | -3.2 | 0.095 | 15/40 (LOX-IMVI, CFPAC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -3.1 | 0.12 | 3/42 (HOP62, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1637. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 57.2 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.240× (z -11.7) |
| [[HT-29 (line)]] | alt | 41.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -9.7) |
| [[Hs 766T (line)]] | wt | 66.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.235× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 4.97 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.90× (z +8.6) | [[Cobimetinib (drug)]] 5 µM 0.0651× (z -10.0) |
| [[LS 180 (line)]] | wt | 37.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -15.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 4.21 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.58× (z +11.8) | — |
| [[CFPAC-1 (line)]] | alt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +8.5) | — |
| [[KATO III (line)]] | alt | 56.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -8.8) |
| [[LoVo (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 4.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.47× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 19.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +11.3) | — |
| [[PANC-1 (line)]] | alt | 6.75 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.186× (z -9.4) |
| [[RKO (line)]] | wt | 8.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.17× (z +8.9) | — |
| [[A-172 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1637), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NECTIN1]] | +0.65 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[PLK3]] | +0.63 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[SULF2]] | +0.59 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[CYP2S1]] | +0.58 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[FA2H]] | +0.57 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[TMC6]] | +0.56 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[ARHGAP27]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[KIAA0040]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[NGEF]] | +0.55 | +0.49 / +0.56 | both halves | 1e-05 | pathway: EPH-Ephrin signaling; STRING 644 |
| [[RNF19B]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[IL2RG]] | +0.54 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[SEMA3F]] | +0.54 | +0.50 / +0.60 | both halves | 1e-05 | STRING 473 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYMPK]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[NUP42]] | -0.48 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[IFT81]] | -0.46 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[APIP]] | -0.45 | -0.48 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINB5]] | B | SERPINB5 activity raises EFNB1's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 2.56× lower at baseline in the lines without SERPINB5 | 0.011 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[CEACAM1]] | B | CEACAM1 activity raises EFNB1's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 1.92× lower at baseline in the lines without CEACAM1 | 0.018 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[TOP2A]] | B | TOP2A activity lowers EFNB1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TFF2]] | B | TFF2 activity raises EFNB1's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 3.14× lower at baseline in the lines without TFF2 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |
| [[IL2RG]] | B | IL2RG activity raises EFNB1's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 1.77× lower at baseline in the lines without IL2RG | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[HSD17B2]] | B | HSD17B2 activity raises EFNB1's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 2.22× lower at baseline in the lines without HSD17B2 | 0.060 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2 |
| [[SULF2]] | B | SULF2 activity raises EFNB1's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 2.24× lower at baseline in the lines without SULF2 | 0.062 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |
| [[DGKA]] | B | DGKA activity raises EFNB1's level | lines that do not express DGKA (6) vs lines expressing it (44) | 2.20× lower at baseline in the lines without DGKA | 0.063 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PRSS3]] | B | PRSS3 activity raises EFNB1's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 2.47× lower at baseline in the lines without PRSS3 | 0.071 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[LYPD3]] | B | LYPD3 activity raises EFNB1's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 1.65× lower at baseline in the lines without LYPD3 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[CYP3A5]] | B | CYP3A5 activity raises EFNB1's level | lines that do not express CYP3A5 (32) vs lines expressing it (18) | 2.13× lower at baseline in the lines without CYP3A5 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HHLA2, GCNT3, HNF4A |
| [[MMP28]] | B | MMP28 activity raises EFNB1's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.82× lower at baseline in the lines without MMP28 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.590). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.8, 49.5); signed map (6.0, 32.8). **Vector** length 91.5, 21.1% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +14.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +7.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +10.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.9 | +1.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -5.4 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.2 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.9 | -4.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.5 | -2.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.8 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ephrin B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:68,829,021-68,842,160 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LERK2, Elk-L; previously EPLG2, CFNS |
| Gene groups (HGNC) | Ephrins |
| Reactome | 6 pathways, smallest: Ephrin signaling; EPHB-mediated forward signaling; EPH-ephrin mediated repulsion of cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P98172](https://www.uniprot.org/uniprotkb/P98172) (Ephrin-B1):

> Cell surface transmembrane ligand for Eph receptors, a family of receptor tyrosine kinases which are crucial for migration, repulsion and adhesion during neuronal, vascular and epithelial development. Binding to Eph receptors residing on adjacent cells leads to contact-dependent bidirectional signaling into neighboring cells. Shows high affinity for the receptor tyrosine kinase EPHB1/ELK. Can also bind EPHB2 and EPHB3. Binds to, and induces collapse of, commissural axons/growth cones in vitro …

**Summary**, from NCBI Gene [1947](https://www.ncbi.nlm.nih.gov/gene/1947):

> The protein encoded by this gene is a type I membrane protein and a ligand of Eph-related receptor tyrosine kinases. It may play a role in cell adhesion and function in the development or maintenance of the nervous system. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3226](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3226) · Entrez [1947](https://www.ncbi.nlm.nih.gov/gene/1947) · UniProt [P98172](https://www.uniprot.org/uniprotkb/P98172) · Ensembl [ENSG00000090776](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090776)

## Data

Gene col 1637: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1637); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1637, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1637]; `tensor/DDL_lfc|DDL_z.npy` [1637]; `embed/gene_vectors.npy` [1637]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1637 or target_col == 1637). Every well: [[EFNB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFNB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
