---
symbol: "PAEP"
type: "gene"
col: 4322
ensembl_id: "ENSG00000122133"
name: "progestagen associated endometrial protein"
location: "9q34.3"
module: 84
arm: "+"
pooled_cpm: 4.68
n_lines_expressing: 17
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 10
direction_downstream: 13
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# PAEP

*progestagen associated endometrial protein* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.61× (z +7.2, q 3e-10, up in 7 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.423× (z -4.8, q 9e-04, down in 9 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAC2]] (+0.71, fdr 7e-06), [[LINC02813]] (+0.69, fdr 7e-06), [[SHANK1]] (+0.69, fdr 7e-06); moves opposite to [[MGST1]] (-0.54, fdr 1e-05), [[TLK1]] (-0.51, fdr 5e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[KCNN4]] → it (grade B ⚠); 13 go from it, the strongest it → [[BACE2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4322.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.61×** | +7.2 | 3e-10 | 7/13 (Panc 03.27, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.88×** | +7.0 | 1e-09 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **3.58×** | +4.6 | 9e-04 | 2/8 (SK-MEL-2, NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **2.30×** | +4.3 | 0.003 | 4/11 (SHP-77, A549, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +4.1 | 0.005 | 1/6 (Panc 03.27) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +3.4 | 0.070 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | 1.80× | +3.1 | 0.15 | 1/11 (Panc 03.27) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 2.34× | +3.1 | 0.16 | 2/8 (CFPAC-1, Panc 03.27) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | 2.32× | +3.0 | 0.16 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4322.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.423×** | -4.8 | 9e-04 | 9/13 (SHP-77, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.426×** | -4.6 | 0.001 | 10/13 (Panc 03.27, HOP62, …) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.411×** | -4.4 | 0.002 | 10/13 (SHP-77, CFPAC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.519×** | -4.3 | 0.003 | 10/12 (SHP-77, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.591×** | -4.0 | 0.009 | 8/13 (SHP-77, CFPAC-1, …) | all doses, flat |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.506×** | -3.4 | 0.062 | 4/13 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.525×** | -3.3 | 0.062 | 6/9 (HOP62, SHP-77, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.520×** | -3.3 | 0.062 | 8/11 (SHP-77, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Encorafenib (drug)]] 5 µM |  | **0.309×** | -3.3 | 0.062 | 3/13 (CFPAC-1, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.547×** | -3.2 | 0.066 | 10/13 (SHP-77, HOP62, …) | all doses, flat |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.552×** | -3.2 | 0.071 | 0/13 | inconsistent across doses | position effect removed |
| [[RMC-6236 (drug)]] 5 µM |  | 0.337× | -3.1 | 0.10 | 4/11 (SHP-77, Panc 03.27, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.667× | -3.0 | 0.10 | 7/13 (SHP-77, CFPAC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4322. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 18.2 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0587× (z -9.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.0555× (z -9.0) |
| [[SHP-77 (line)]] | alt | 122 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0974× (z -13.7) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 2.80 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0387× (z -9.4) ⚠ cell-cycle shift, explains ~74% of this change |
| [[Panc 03.27 (line)]] | alt | 36.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -11.1) ⚠ cell-cycle shift, explains ~74% of this change |
| [[A-172 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.343 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.422 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.646 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.810 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.696 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.658 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.647 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.430 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.704 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.552 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.730 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.540 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.579 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.958 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.850 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.712 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.853 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4322), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAC2]] | +0.71 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[LINC02813]] | +0.69 | +0.64 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[SHANK1]] | +0.69 | +0.61 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SHC4]] | +0.68 | +0.57 / +0.73 | both halves | 1e-05 | **novel candidate** |
| [[PTGS1]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[KCNK3]] | +0.66 | +0.68 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[STX1A]] | +0.65 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[STC1]] | +0.65 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[ITGA11]] | +0.63 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[COL22A1]] | +0.63 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[SEMA7A]] | +0.62 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[TMEM158]] | +0.62 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGST1]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[TLK1]] | -0.51 | -0.40 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNN4]] | B | KCNN4 activity lowers PAEP's level | lines that do not express KCNN4 (12) vs lines expressing it (38) | 1.12× higher at baseline in the lines without KCNN4 | 0.026 | ⚠ within organs, on part of the lines; also absent: RP1, GSPT2, GALC |
| [[MAP2K2]] | B | MAP2K2 activity raises PAEP's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[TRBC2]] | C | TRBC2 activity raises PAEP's level | lines that do not express TRBC2 (39) vs lines expressing it (11) | 3.39× lower at baseline in the lines without TRBC2 | 0.011 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1; co-absent with the target |
| [[PTGS1]] | C | PTGS1 activity raises PAEP's level | lines that do not express PTGS1 (26) vs lines expressing it (24) | 2.22× lower at baseline in the lines without PTGS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: C2CD4A, ARHGEF38, ILDR1; co-absent with the target |
| [[LAPTM5]] | C | LAPTM5 activity raises PAEP's level | lines that do not express LAPTM5 (31) vs lines expressing it (19) | 2.35× lower at baseline in the lines without LAPTM5 | 0.040 | ⚠ within organs, on part of the lines; also absent: CD74, LINC02742, IRAG2; co-absent with the target |
| [[COL22A1]] | C | COL22A1 activity raises PAEP's level | lines that do not express COL22A1 (31) vs lines expressing it (19) | 2.60× lower at baseline in the lines without COL22A1 | 0.041 | ⚠ within organs, on part of the lines; also absent: EYA2, PAK3, CRLF2; co-absent with the target |
| [[LINC02970]] | C | LINC02970 activity raises PAEP's level | lines that do not express LINC02970 (24) vs lines expressing it (26) | 1.92× lower at baseline in the lines without LINC02970 | 0.041 | ⚠ within organs, on part of the lines; also absent: TOX, MXRA5, ENSG00000255595; co-absent with the target |
| [[SIGLEC15]] | C | SIGLEC15 activity raises PAEP's level | lines that do not express SIGLEC15 (27) vs lines expressing it (23) | 1.99× lower at baseline in the lines without SIGLEC15 | 0.053 | ⚠ within organs, on part of the lines; also absent: LINC01615, ZNF257, NLRP1; co-absent with the target |
| [[CCDC152]] | C | CCDC152 activity raises PAEP's level | lines that do not express CCDC152 (30) vs lines expressing it (20) | 2.25× lower at baseline in the lines without CCDC152 | 0.055 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent; co-absent with the target |
| [[NES]] | C | NES activity raises PAEP's level | lines that do not express NES (26) vs lines expressing it (24) | 2.48× lower at baseline in the lines without NES | 0.073 | ⚠ within organs, on part of the lines; also absent: LAPTM5, CSPG4, ENSG00000230490; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 5, C 8. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BACE2]] | B | PAEP activity raises BACE2's level | lines that do not express PAEP (33) vs lines expressing it (17) | 2.00× lower at baseline in the lines without PAEP | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GREM2, UNC5D |
| [[KIF21B]] | B | PAEP activity raises KIF21B's level | lines that do not express PAEP (33) vs lines expressing it (17) | 1.58× lower at baseline in the lines without PAEP | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GREM2, UNC5D |
| [[CACNA2D4]] | B | PAEP activity raises CACNA2D4's level | lines that do not express PAEP (33) vs lines expressing it (17) | 1.52× lower at baseline in the lines without PAEP | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GREM2, UNC5D |
| [[PLXNA4]] | B | PAEP activity raises PLXNA4's level | lines that do not express PAEP (33) vs lines expressing it (17) | 2.09× lower at baseline in the lines without PAEP | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GREM2, UNC5D |
| [[DUSP4]] | B | PAEP activity raises DUSP4's level | lines that do not express PAEP (33) vs lines expressing it (17) | 1.55× lower at baseline in the lines without PAEP | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GREM2, UNC5D |
| [[CCDC152]] | C | PAEP activity raises CCDC152's level | lines that do not express PAEP (33) vs lines expressing it (17) | 1.93× lower at baseline in the lines without PAEP | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GREM2, UNC5D; co-absent with the target |
| [[COL22A1]] | C | PAEP activity raises COL22A1's level | lines that do not express PAEP (33) vs lines expressing it (17) | 2.76× lower at baseline in the lines without PAEP | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GREM2, UNC5D; co-absent with the target |
| [[TREM1]] | C | PAEP activity raises TREM1's level | lines that do not express PAEP (33) vs lines expressing it (17) | 2.36× lower at baseline in the lines without PAEP | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GREM2, UNC5D; co-absent with the target |
| [[TRBC2]] | C | PAEP activity raises TRBC2's level | lines that do not express PAEP (33) vs lines expressing it (17) | 1.89× lower at baseline in the lines without PAEP | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GREM2, UNC5D; co-absent with the target |
| [[SHC4]] | C | PAEP activity raises SHC4's level | lines that do not express PAEP (33) vs lines expressing it (17) | 2.67× lower at baseline in the lines without PAEP | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GREM2, UNC5D; co-absent with the target |
| [[SLC16A6]] | C | PAEP activity raises SLC16A6's level | lines that do not express PAEP (33) vs lines expressing it (17) | 2.74× lower at baseline in the lines without PAEP | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GREM2, UNC5D; co-absent with the target |
| [[LINC02970]] | C | PAEP activity raises LINC02970's level | lines that do not express PAEP (33) vs lines expressing it (17) | 2.00× lower at baseline in the lines without PAEP | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GREM2, UNC5D; co-absent with the target |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (50.4, 8.7); signed map (10.1, 51.4). **Vector** length 42.6, 13.2% of its response variance represented; |z| ≥ 3 in 390 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +4.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +3.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.0 | +2.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -4.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.2 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -3.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.7 | -3.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.7 | -4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | progestagen associated endometrial protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:135,561,756-135,566,955 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PEP, PP14, GdA, GdS, GdF, PAEG, GD, MGC138509 |
| Gene groups (HGNC) | Lipocalins |
| Matched by | ensembl_id |

**Function**, from UniProt [P09466](https://www.uniprot.org/uniprotkb/P09466) (Glycodelin):

> Glycoprotein that regulates critical steps during fertilization and also has immunomonomodulatory effects. Four glycoforms, namely glycodelin-S, -A, -F and -C have been identified in reproductive tissues that differ in glycosylation and biological activity. Glycodelin-A has contraceptive and immunosuppressive activities. Glycodelin-C stimulates binding of spermatozoa to the zona pellucida. Glycodelin-F inhibits spermatozoa-zona pellucida binding and significantly suppresses progesterone-induced …

**Summary**, from NCBI Gene [5047](https://www.ncbi.nlm.nih.gov/gene/5047):

> This gene is a member of the kernel lipocalin superfamily whose members share relatively low sequence similarity but have highly conserved exon/intron structure and three-dimensional protein folding. Most lipocalins are clustered on the long arm of chromosome 9. The encoded glycoprotein has been previously referred to as pregnancy-associated endometrial alpha-2-globulin, placental protein 14, and glycodelin, but has been officially named progestagen-associated endometrial protein. Three …

**Accessions** — [HGNC:8573](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8573) · Entrez [5047](https://www.ncbi.nlm.nih.gov/gene/5047) · UniProt [P09466](https://www.uniprot.org/uniprotkb/P09466) · Ensembl [ENSG00000122133](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122133)

## Data

Gene col 4322: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4322); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4322, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4322]; `tensor/DDL_lfc|DDL_z.npy` [4322]; `embed/gene_vectors.npy` [4322]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4322 or target_col == 4322). Every well: [[PAEP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAEP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
