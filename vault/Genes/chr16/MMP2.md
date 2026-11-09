---
symbol: "MMP2"
type: "gene"
col: 1491
ensembl_id: "ENSG00000087245"
name: "matrix metallopeptidase 2"
location: "16q12.2"
module: 50
arm: "+"
pooled_cpm: 22.31
n_lines_expressing: 16
n_dd_up: 17
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 21
direction_downstream: 35
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# MMP2

*matrix metallopeptidase 2* — 16q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.95× (z +19.1, q 0e+00, up in 11 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.94× (z +10.0, q 2e-21, up in 9 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.497× (z -7.5, q 3e-11, down in 12 of 14 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPARC]] (+0.78, fdr 7e-06), [[NID2]] (+0.70, fdr 7e-06), [[COL3A1]] (+0.69, fdr 7e-06); moves opposite to [[METTL2A]] (-0.55, fdr 3e-05), [[EIF5B]] (-0.53, fdr 3e-05), [[BRIX1]] (-0.53, fdr 3e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[MYL9]] → it (grade B ⚠); 35 go from it, the strongest it → [[COL18A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1491.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.95×** | +19.1 | 0e+00 | 11/12 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.14×** | +16.9 | 0e+00 | 11/11 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.08×** | +13.9 | 8e-42 | 7/11 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +10.0 | 2e-21 | 9/14 (HOP62, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +5.7 | 2e-06 | 0/14 | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.59×** | +5.3 | 9e-06 | 5/10 (HS-578T, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +5.2 | 1e-05 | 2/14 (HOP62, PANC-1) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +4.9 | 8e-05 | 9/14 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.46×** | +4.1 | 0.003 | 0/14 | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.004 | 7/13 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Malotilate (drug)]] 0.05 µM |  | **1.44×** | +3.9 | 0.006 | 2/14 (C32, NCI-H1792) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.016 | 4/14 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.020 | 2/14 (HOP62, A-172) | top dose only | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.58×** | +3.3 | 0.036 | 0/14 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.34×** | +3.1 | 0.071 | 1/14 (SK-MEL-2) | inconsistent across doses | low cells (technical?) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.073 | 2/13 (HS-578T, HOP62) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1491.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.497×** | -7.5 | 3e-11 | 12/14 (LOX-IMVI, SW 1088, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.626×** | -7.1 | 3e-10 | 13/14 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.507×** | -7.0 | 4e-10 | 9/14 (LOX-IMVI, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.578×** | -5.9 | 5e-07 | 9/14 (LOX-IMVI, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Delamanid (drug)]] 0.05 µM |  | **0.695×** | -3.9 | 0.011 | 0/14 | inconsistent across doses | position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.691×** | -3.7 | 0.019 | 0/14 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.711×** | -3.7 | 0.019 | 10/14 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.694×** | -3.6 | 0.019 | 0/14 | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **0.792×** | -3.6 | 0.024 | 1/14 (PANC-1) | rises with dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.709×** | -3.4 | 0.035 | 1/14 (PANC-1) | inconsistent across doses | position effect removed |
| [[Vortioxetine (drug)]] 0.5 µM |  | **0.749×** | -3.1 | 0.094 | 0/14 | inconsistent across doses | position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.733×** | -3.1 | 0.094 | 0/14 | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.581×** | -3.1 | 0.099 | 0/14 | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1491. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.6 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 5.33× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -23.9) |
| [[HOP62 (line)]] | alt | 30.5 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -15.3) |
| [[LOX-IMVI (line)]] | wt | 31.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0200× (z -25.2) |
| [[H4 (line)]] | wt | 94.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -20.7) |
| [[SNU-423 (line)]] | alt | 129 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -10.4) |
| [[SW 1088 (line)]] | alt | 177 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0225× (z -16.0) |
| [[HS-578T (line)]] | alt | 78.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.40× (z +11.1) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 417 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -10.4) |
| [[CHP-212 (line)]] | wt | 214 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -15.0) |
| [[hTERT-HPNE (line)]] | wt | 152 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.213× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 123 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.19× (z +12.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.07 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.60 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1491), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPARC]] | +0.78 | +0.77 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_COAGULATION; STRING 701 |
| [[NID2]] | +0.70 | +0.64 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[COL3A1]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 799 |
| [[COL6A1]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 | pathway: Collagen degradation; STRING 695 |
| [[FSTL1]] | +0.67 | +0.57 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 430 |
| [[ECM1]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[TGFBI]] | +0.64 | +0.64 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_APICAL_JUNCTION; STRING 621 |
| [[DKK3]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[GM2A]] | +0.63 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[GNS]] | +0.63 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ITM2C]] | +0.63 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[PSAP]] | +0.63 | +0.57 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL2A]] | -0.55 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[EIF5B]] | -0.53 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[BRIX1]] | -0.53 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[SDHAF2]] | -0.52 | -0.43 / -0.44 | both halves | 4e-05 |  |
| [[CCDC137]] | -0.51 | -0.41 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 1, C 20. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYL9]] | B | MYL9 activity raises MMP2's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 2.23× lower at baseline in the lines without MYL9 | 0.077 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[ITGA4]] | C | ITGA4 activity raises MMP2's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 13.19× lower at baseline in the lines without ITGA4 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[LAYN]] | C | LAYN activity raises MMP2's level | lines that do not express LAYN (31) vs lines expressing it (19) | 9.01× lower at baseline in the lines without LAYN | 0.003 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM; co-absent with the target |
| [[DKK3]] | C | DKK3 activity raises MMP2's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 8.11× lower at baseline in the lines without DKK3 | 0.004 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises MMP2's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 11.84× lower at baseline in the lines without PDGFRB | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[SPARC]] | C | SPARC activity raises MMP2's level | lines that do not express SPARC (34) vs lines expressing it (16) | 11.70× lower at baseline in the lines without SPARC | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[COL1A1]] | C | COL1A1 activity raises MMP2's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 8.17× lower at baseline in the lines without COL1A1 | 0.006 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[POSTN]] | C | POSTN activity raises MMP2's level | lines that do not express POSTN (38) vs lines expressing it (12) | 7.09× lower at baseline in the lines without POSTN | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[NID2]] | C | NID2 activity raises MMP2's level | lines that do not express NID2 (32) vs lines expressing it (18) | 5.97× lower at baseline in the lines without NID2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1; co-absent with the target |
| [[FBN1]] | C | FBN1 activity raises MMP2's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 5.52× lower at baseline in the lines without FBN1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; co-absent with the target |
| [[THY1]] | C | THY1 activity raises MMP2's level | lines that do not express THY1 (38) vs lines expressing it (12) | 12.22× lower at baseline in the lines without THY1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |
| [[ARHGEF6]] | C | ARHGEF6 activity raises MMP2's level | lines that do not express ARHGEF6 (20) vs lines expressing it (30) | 5.75× lower at baseline in the lines without ARHGEF6 | 0.031 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 9, C 26. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL18A1]] | B | MMP2 activity raises COL18A1's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 2.99× lower at baseline in the lines without MMP2 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L |
| [[IGF2R]] | B | MMP2 activity raises IGF2R's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 1.20× lower at baseline in the lines without MMP2 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L |
| [[SMPD1]] | B | MMP2 activity raises SMPD1's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 2.19× lower at baseline in the lines without MMP2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L |
| [[TIMP2]] | B | MMP2 activity weakens TIMP2's drug response | lines that do not express MMP2 (30) vs lines expressing it (15) | the lines without MMP2 respond 1.03× as strongly (z diff -0.20); strongest at Harringtonine 5 µM: 0.35x vs 0.54x (z diff -2.3) | 0.079 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L; target measured in part of the lines; both ways; artifact flags |
| [[CTSF]] | B | MMP2 activity raises CTSF's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 2.24× lower at baseline in the lines without MMP2 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L |
| [[CTSD]] | B | MMP2 activity raises CTSD's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 1.80× lower at baseline in the lines without MMP2 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L |
| [[GANAB]] | B | MMP2 activity raises GANAB's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 1.20× lower at baseline in the lines without MMP2 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L |
| [[P3H1]] | B | MMP2 activity raises P3H1's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 2.15× lower at baseline in the lines without MMP2 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L |
| [[P3H3]] | B | MMP2 activity raises P3H3's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 2.10× lower at baseline in the lines without MMP2 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L |
| [[ITGA4]] | C | MMP2 activity raises ITGA4's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 10.22× lower at baseline in the lines without MMP2 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L; co-absent with the target |
| [[ARHGEF6]] | C | MMP2 activity raises ARHGEF6's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 4.10× lower at baseline in the lines without MMP2 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L; co-absent with the target |
| [[SPARC]] | C | MMP2 activity raises SPARC's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 18.09× lower at baseline in the lines without MMP2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L; co-absent with the target |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (56.2, 22.1); signed map (25.5, 42.7). **Vector** length 47.7, 16.0% of its response variance represented; |z| ≥ 3 in 246 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glycosphingolipid catabolism* (reactome, mean cos +0.51 to 5); *Glycosphingolipid metabolism* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +16.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +19.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +10.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | -0.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.1 | -0.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -7.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.8 | -7.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.1 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.9 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -0.9 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | matrix metallopeptidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.2 — chr16:55,389,700-55,506,691 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MMP-2, TBE-1; previously CLG4, CLG4A |
| Gene groups (HGNC) | M10 matrix metallopeptidases; Elastases |
| Hallmark sets | COAGULATION, APOPTOSIS, APICAL_JUNCTION, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 17 pathways, smallest: Activation of Matrix Metalloproteinases; Collagen degradation; EPH-ephrin mediated repulsion of cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P08253](https://www.uniprot.org/uniprotkb/P08253) (72 kDa type IV collagenase):

> Ubiquitinous metalloproteinase that is involved in diverse functions such as remodeling of the vasculature, angiogenesis, tissue repair, tumor invasion, inflammation, and atherosclerotic plaque rupture. As well as degrading extracellular matrix proteins, can also act on several nonmatrix proteins such as big endothelial 1 and beta-type CGRP promoting vasoconstriction. Also cleaves KISS at a Gly-|-Leu bond. Appears to have a role in myocardial cell death pathways. Contributes to myocardial …

**Summary**, from NCBI Gene [4313](https://www.ncbi.nlm.nih.gov/gene/4313):

> This gene is a member of the matrix metalloproteinase (MMP) gene family, that are zinc-dependent enzymes capable of cleaving components of the extracellular matrix and molecules involved in signal transduction. The protein encoded by this gene is a gelatinase A, type IV collagenase, that contains three fibronectin type II repeats in its catalytic site that allow binding of denatured type IV and V collagen and elastin. Unlike most MMP family members, activation of this protein can occur on the …

**Accessions** — [HGNC:7166](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7166) · Entrez [4313](https://www.ncbi.nlm.nih.gov/gene/4313) · UniProt [P08253](https://www.uniprot.org/uniprotkb/P08253) · Ensembl [ENSG00000087245](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087245)

## Data

Gene col 1491: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1491); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1491, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1491]; `tensor/DDL_lfc|DDL_z.npy` [1491]; `embed/gene_vectors.npy` [1491]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1491 or target_col == 1491). Every well: [[MMP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
