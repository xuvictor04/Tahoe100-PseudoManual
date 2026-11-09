---
symbol: "LAYN"
type: "gene"
col: 12861
ensembl_id: "ENSG00000204381"
name: "layilin"
location: "11q23.1"
module: 13
arm: "+"
pooled_cpm: 4.87
n_lines_expressing: 19
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 30
direction_downstream: 20
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# LAYN

*layilin* — 11q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.56× (z +11.7, q 6e-29, up in 6 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.85× (z +6.9, q 6e-10, up in 12 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.536× (z -5.0, q 3e-04, down in 14 of 17 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPEG]] (+0.58, fdr 2e-05), [[DKK3]] (+0.56, fdr 1e-05), [[CARMN]] (+0.55, fdr 1e-04); moves opposite to [[RMI2]] (-0.39, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[SPARC]] → it (grade C ⚠); 20 go from it, the strongest it → [[GXYLT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12861.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.56×** | +11.7 | 6e-29 | 6/13 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.68×** | +10.5 | 3e-23 | 7/15 (J82, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.08×** | +7.4 | 3e-11 | 6/14 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +6.9 | 6e-10 | 12/17 (NCI-H1792, PANC-1, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.39×** | +4.1 | 0.005 | 0/12 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.005 | 4/17 (A-172, SW 900, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +4.0 | 0.006 | 9/17 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +3.7 | 0.017 | 5/17 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.45×** | +3.6 | 0.023 | 1/8 (J82) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.027 | 8/17 (A-172, SW 900, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.4 | 0.030 | 1/16 (HS-578T) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.4 | 0.030 | 4/14 (NCI-H2347, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +3.4 | 0.030 | 0/15 | top dose only | cell-cycle shift (explains ~13% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.049 | 5/16 (A-172, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.51×** | +3.1 | 0.062 | 10/16 (A-172, H4, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12861.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.536×** | -5.0 | 3e-04 | 14/17 (NCI-H1792, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.556×** | -4.7 | 6e-04 | 15/17 (SW 1088, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.603×** | -4.1 | 0.008 | 12/17 (H4, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.871× | -3.8 | 0.024 | 8/17 (A-172, NCI-H23, …) | inconsistent across doses |  |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.654× | -3.3 | 0.11 | 2/17 (SW 1088, SW 900) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.765× | -3.1 | 0.20 | 4/17 (H4, hTERT-HPNE, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.689× | -3.0 | 0.21 | 7/17 (H4, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12861. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 19.5 | 0 | 2 | — | [[Digitoxin (drug)]] 0.05 µM 0.115× (z -8.7) |
| [[J82 (line)]] | alt | 8.78 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.39× (z +8.7) ⚠ toxic; transcription drop | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0422× (z -14.2) |
| [[CHP-212 (line)]] | wt | 67.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 64.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.905 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.842 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.422 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.539 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.399 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.518 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.438 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.344 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.620 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.336 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.360 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12861), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPEG]] | +0.58 | +0.52 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_APICAL_JUNCTION |
| [[DKK3]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[CARMN]] | +0.55 | +0.60 / +0.33 | both halves | 1e-04 |  |
| [[ZNF883]] | +0.55 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[SLIT3]] | +0.54 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[CALD1]] | +0.53 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[PDGFRB]] | +0.53 | +0.66 / +0.34 | both halves | 1e-04 |  |
| [[NID2]] | +0.52 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[MEG3]] | +0.52 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[MEG8]] | +0.51 | +0.54 / +0.38 | both halves | 6e-05 |  |
| [[ADAMTS12]] | +0.50 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[ANXA6]] | +0.50 | +0.46 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RMI2]] | -0.39 | -0.34 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 0, C 30. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPARC]] | C | SPARC activity raises LAYN's level | lines that do not express SPARC (34) vs lines expressing it (16) | 5.09× lower at baseline in the lines without SPARC | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[ITGA4]] | C | ITGA4 activity raises LAYN's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 4.78× lower at baseline in the lines without ITGA4 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises LAYN's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 5.77× lower at baseline in the lines without LINC01411 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[EVC2]] | C | EVC2 activity raises LAYN's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 3.75× lower at baseline in the lines without EVC2 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |
| [[ZNF677]] | C | ZNF677 activity raises LAYN's level | lines that do not express ZNF677 (39) vs lines expressing it (11) | 8.22× lower at baseline in the lines without ZNF677 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL11A1, COL3A1, GCG; co-absent with the target |
| [[MMP2]] | C | MMP2 activity raises LAYN's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 5.25× lower at baseline in the lines without MMP2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L; co-absent with the target |
| [[DKK3]] | C | DKK3 activity raises LAYN's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 4.76× lower at baseline in the lines without DKK3 | 0.006 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises LAYN's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 4.81× lower at baseline in the lines without COL5A1 | 0.009 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises LAYN's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 6.33× lower at baseline in the lines without PDGFRB | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[MOXD1]] | C | MOXD1 activity raises LAYN's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 3.45× lower at baseline in the lines without MOXD1 | 0.012 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1; co-absent with the target |
| [[PRR16]] | C | PRR16 activity raises LAYN's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 4.19× lower at baseline in the lines without PRR16 | 0.013 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises LAYN's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 5.50× lower at baseline in the lines without APCDD1L | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 2, C 18. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GXYLT2]] | B | LAYN activity raises GXYLT2's level | lines that do not express LAYN (31) vs lines expressing it (19) | 2.07× lower at baseline in the lines without LAYN | 0.055 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM |
| [[HEG1]] | B | LAYN activity raises HEG1's level | lines that do not express LAYN (31) vs lines expressing it (19) | 2.83× lower at baseline in the lines without LAYN | 0.091 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM |
| [[MMP2]] | C | LAYN activity raises MMP2's level | lines that do not express LAYN (31) vs lines expressing it (19) | 9.01× lower at baseline in the lines without LAYN | 0.003 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM; co-absent with the target |
| [[GLIS1]] | C | LAYN activity raises GLIS1's level | lines that do not express LAYN (31) vs lines expressing it (19) | 3.62× lower at baseline in the lines without LAYN | 0.004 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM; co-absent with the target |
| [[PDGFRB]] | C | LAYN activity raises PDGFRB's level | lines that do not express LAYN (31) vs lines expressing it (19) | 6.93× lower at baseline in the lines without LAYN | 0.007 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM; co-absent with the target |
| [[ZNF677]] | C | LAYN activity raises ZNF677's level | lines that do not express LAYN (31) vs lines expressing it (19) | 3.44× lower at baseline in the lines without LAYN | 0.011 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM; co-absent with the target |
| [[EVC2]] | C | LAYN activity raises EVC2's level | lines that do not express LAYN (31) vs lines expressing it (19) | 3.30× lower at baseline in the lines without LAYN | 0.012 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM; co-absent with the target |
| [[SPARC]] | C | LAYN activity raises SPARC's level | lines that do not express LAYN (31) vs lines expressing it (19) | 6.98× lower at baseline in the lines without LAYN | 0.013 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM; co-absent with the target |
| [[POPDC3]] | C | LAYN activity raises POPDC3's level | lines that do not express LAYN (31) vs lines expressing it (19) | 3.36× lower at baseline in the lines without LAYN | 0.018 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM; co-absent with the target |
| [[ITGA4]] | C | LAYN activity raises ITGA4's level | lines that do not express LAYN (31) vs lines expressing it (19) | 3.85× lower at baseline in the lines without LAYN | 0.019 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM; co-absent with the target |
| [[LINC01411]] | C | LAYN activity raises LINC01411's level | lines that do not express LAYN (31) vs lines expressing it (19) | 5.54× lower at baseline in the lines without LAYN | 0.019 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM; co-absent with the target |
| [[COL1A2]] | C | LAYN activity raises COL1A2's level | lines that do not express LAYN (31) vs lines expressing it (19) | 5.67× lower at baseline in the lines without LAYN | 0.023 | ⚠ within organs, on part of the lines; also absent: COL1A1, ITGA11, LUM; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.455). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (54.1, 19.9); signed map (25.8, 43.9). **Vector** length 38.5, 9.02% of its response variance represented; |z| ≥ 3 in 364 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +11.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +3.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.5 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.4 | +3.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -5.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.8 | -2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.4 | -4.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.4 | -3.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.0 | -2.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | layilin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.1 — chr11:111,540,280-111,561,745 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30977, FLJ31092 |
| Gene groups (HGNC) | C-type lectin domain containing |
| Hallmark sets | APICAL_JUNCTION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UX15](https://www.uniprot.org/uniprotkb/Q6UX15) (Layilin):

> Receptor for hyaluronate.

**Summary**, from NCBI Gene [143903](https://www.ncbi.nlm.nih.gov/gene/143903):

> Enables hyaluronic acid binding activity. Located in focal adhesion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29471](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29471) · Entrez [143903](https://www.ncbi.nlm.nih.gov/gene/143903) · UniProt [Q6UX15](https://www.uniprot.org/uniprotkb/Q6UX15) · Ensembl [ENSG00000204381](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204381)

## Data

Gene col 12861: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12861); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12861, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12861]; `tensor/DDL_lfc|DDL_z.npy` [12861]; `embed/gene_vectors.npy` [12861]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12861 or target_col == 12861). Every well: [[LAYN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAYN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
