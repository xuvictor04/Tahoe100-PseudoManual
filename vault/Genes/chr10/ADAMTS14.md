---
symbol: "ADAMTS14"
type: "gene"
col: 6153
ensembl_id: "ENSG00000138316"
name: "ADAM metallopeptidase with thrombospondin type 1 motif 14"
location: "10q22.1"
module: 13
arm: "+"
pooled_cpm: 15.6
n_lines_expressing: 19
n_dd_up: 10
n_dd_down: 24
n_dd_up_clean: 6
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 27
direction_downstream: 30
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# ADAMTS14

*ADAM metallopeptidase with thrombospondin type 1 motif 14* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.95× (z +7.4, q 4e-11, up in 1 of 13 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.47× (z +6.0, q 4e-07, up in 3 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 0.652× (z -6.7, q 2e-08, down in 15 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYNDIG1]] (+0.70, fdr 7e-06), [[VSTM4]] (+0.67, fdr 7e-06), [[EDNRA]] (+0.67, fdr 8e-06); moves opposite to [[SRGN]] (-0.56, fdr 2e-05), [[MIR3936HG]] (-0.47, fdr 2e-04), [[NEXN]] (-0.47, fdr 4e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[PRRX1]] → it (grade C ⚠); 30 go from it, the strongest it → [[ARL4C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6153.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.95×** | +7.4 | 4e-11 | 1/13 (SW 900) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +7.4 | 4e-11 | 1/10 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +6.0 | 4e-07 | 3/17 (SW480, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.62×** | +4.9 | 1e-04 | 0/12 | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +4.3 | 0.002 | 9/16 (SW480, A498, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.54×** | +3.4 | 0.062 | 3/16 (Panc 03.27, SNU-423, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.76×** | +3.3 | 0.081 | 3/14 (SNU-423, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +3.3 | 0.081 | 12/16 (A-172, Panc 03.27, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.36×** | +3.1 | 0.100 | 4/16 (SW480, CHP-212, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.48×** | +3.1 | 0.100 | 4/16 (Panc 03.27, A-172, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 1.32× | +3.1 | 0.11 | 4/16 (CFPAC-1, SW 900, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.47× | +3.0 | 0.11 | 0/15 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, none with an alert; shown: the 15 strongest. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6153.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.652×** | -6.7 | 2e-08 | 15/17 (SNU-423, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.591×** | -5.8 | 2e-06 | 13/15 (NCI-H1792, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.604×** | -5.5 | 6e-06 | 10/16 (NCI-H1792, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.609×** | -5.2 | 2e-05 | 13/16 (NCI-H1792, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.635×** | -5.0 | 5e-05 | 11/17 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.652×** | -4.7 | 2e-04 | 11/16 (SNU-423, SW1417, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.658×** | -4.6 | 3e-04 | 6/16 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.456×** | -4.5 | 4e-04 | 9/16 (SW480, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.669×** | -4.4 | 6e-04 | 8/16 (RPMI-7951, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.473×** | -4.3 | 9e-04 | 9/15 (SNU-423, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.686×** | -4.1 | 0.002 | 5/16 (RPMI-7951, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.778×** | -3.9 | 0.005 | 12/15 (NCI-H1792, SNU-423, …) | two highest doses | cell-cycle shift (explains ~6% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.762×** | -3.6 | 0.012 | 12/17 (A-427, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.739×** | -3.3 | 0.034 | 4/16 (SNU-423, A-172, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.739×** | -3.3 | 0.034 | 9/16 (hTERT-HPNE, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6153. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 67.5 | 0 | 16 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.00897× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0455× (z -14.7) |
| [[NCI-H1792 (line)]] | alt | 238 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0435× (z -29.9) |
| [[SNU-423 (line)]] | alt | 136 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0526× (z -24.6) |
| [[RPMI-7951 (line)]] | alt | 57.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0629× (z -15.5) |
| [[SW1417 (line)]] | alt | 81.7 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -16.5) ⚠ cell-cycle shift, explains ~91% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.302× (z -12.6) |
| [[A-172 (line)]] | wt | 20.5 | 1 (1 ⚠) | 3 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 6.88× (z +8.8) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.5 µM 0.0485× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.212× (z -10.0) |
| [[HS-578T (line)]] | alt | 25.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0420× (z -12.6) |
| [[SW480 (line)]] | alt | 23.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.438× (z -8.6) |
| [[COLO 205 (line)]] | alt | 9.45 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.05 µM 0.0562× (z -9.1) |
| [[Hs 766T (line)]] | wt | 5.68 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.5 µM 0.0647× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 6.24 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 15.4× (z +8.5) ⚠ unreliable plate only | — |
| [[A-427 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.21 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6153), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNDIG1]] | +0.70 | +0.65 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[VSTM4]] | +0.67 | +0.70 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[EDNRA]] | +0.67 | +0.75 / +0.58 | both halves | 8e-06 | **novel candidate** |
| [[NAV1]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[LINC01411]] | +0.66 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[GPR173]] | +0.63 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[KCNK3]] | +0.62 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[TNS1]] | +0.61 | +0.53 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[CARMN]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ITGA11]] | +0.61 | +0.66 / +0.53 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[STRA6]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[SEMA5A]] | +0.60 | +0.57 / +0.64 | both halves | 9e-06 | pathway: Defective B3GALTL causes PpS |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGN]] | -0.56 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[MIR3936HG]] | -0.47 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[NEXN]] | -0.47 | -0.46 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 0, C 27. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRRX1]] | C | PRRX1 activity raises ADAMTS14's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 3.49× lower at baseline in the lines without PRRX1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises ADAMTS14's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 5.05× lower at baseline in the lines without LINC01411 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[EDNRA]] | C | EDNRA activity raises ADAMTS14's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 3.44× lower at baseline in the lines without EDNRA | 0.009 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12; co-absent with the target |
| [[ADAMTS16]] | C | ADAMTS16 activity raises ADAMTS14's level | lines that do not express ADAMTS16 (25) vs lines expressing it (25) | 2.68× lower at baseline in the lines without ADAMTS16 | 0.012 | ⚠ within organs, on part of the lines; also absent: PLAU, ADAMTS12, GBP5; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises ADAMTS14's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 3.19× lower at baseline in the lines without COL5A1 | 0.012 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises ADAMTS14's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 3.60× lower at baseline in the lines without ITGA11 | 0.015 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[GPR173]] | C | GPR173 activity raises ADAMTS14's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 2.88× lower at baseline in the lines without GPR173 | 0.016 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2; co-absent with the target |
| [[RFX8]] | C | RFX8 activity raises ADAMTS14's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.98× lower at baseline in the lines without RFX8 | 0.024 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises ADAMTS14's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 3.23× lower at baseline in the lines without APCDD1L | 0.030 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[DKK3]] | C | DKK3 activity raises ADAMTS14's level | lines that do not express DKK3 (29) vs lines expressing it (21) | 3.05× lower at baseline in the lines without DKK3 | 0.035 | ⚠ within organs, on part of the lines; also absent: COL5A1, ABI3BP, IDO1; co-absent with the target |
| [[NAV1]] | C | NAV1 activity raises ADAMTS14's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 2.51× lower at baseline in the lines without NAV1 | 0.036 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent; co-absent with the target |
| [[SAMD3]] | C | SAMD3 activity raises ADAMTS14's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 2.71× lower at baseline in the lines without SAMD3 | 0.037 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11; co-absent with the target |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 9, C 21. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARL4C]] | B | ADAMTS14 activity raises ARL4C's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 2.72× lower at baseline in the lines without ADAMTS14 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411 |
| [[SYTL3]] | B | ADAMTS14 activity raises SYTL3's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 2.73× lower at baseline in the lines without ADAMTS14 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411 |
| [[THEMIS2]] | B | ADAMTS14 activity raises THEMIS2's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 2.59× lower at baseline in the lines without ADAMTS14 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411 |
| [[ADAM19]] | B | ADAMTS14 activity raises ADAM19's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 2.92× lower at baseline in the lines without ADAMTS14 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411 |
| [[SYNJ2]] | B | ADAMTS14 activity raises SYNJ2's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 2.00× lower at baseline in the lines without ADAMTS14 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411 |
| [[GSDME]] | B | ADAMTS14 activity raises GSDME's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 2.35× lower at baseline in the lines without ADAMTS14 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411 |
| [[OXR1]] | B | ADAMTS14 activity raises OXR1's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 1.87× lower at baseline in the lines without ADAMTS14 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411 |
| cells under [[c-Kit-IN-1 (drug)]] 0.05 µM | B | ADAMTS14 activity lowers the cells' numbers under c-Kit-IN-1 0.05 µM (makes them more sensitive) | lines that do not express ADAMTS14 (31) vs lines expressing it (17) | the lines without ADAMTS14: 1.44× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411; cell counts less trustworthy |
| [[TGFB1]] | B | ADAMTS14 activity strengthens TGFB1's drug response | lines that do not express ADAMTS14 (25) vs lines expressing it (15) | the lines without ADAMTS14 respond 0.64× as strongly (z diff +1.51); strongest at Topotecan (hydrochloride) 5 µM: 0.87x vs 0.57x (z diff +3.7) | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411; target measured in part of the lines; artifact flags |
| [[PRRX1]] | C | ADAMTS14 activity raises PRRX1's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 4.17× lower at baseline in the lines without ADAMTS14 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411; co-absent with the target |
| [[ADAMTS16]] | C | ADAMTS14 activity raises ADAMTS16's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 4.18× lower at baseline in the lines without ADAMTS14 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411; co-absent with the target |
| [[PTGFR]] | C | ADAMTS14 activity raises PTGFR's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 3.45× lower at baseline in the lines without ADAMTS14 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.5, 16.8); signed map (24.2, 47.8). **Vector** length 68.3, 21.5% of its response variance represented; |z| ≥ 3 in 585 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +3.3 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +6.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.4 | +3.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.2 | +2.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[EX229 (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[EX229 (drug)]] 0.5 µM |  | +1.5 | +3.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -3.7 | -6.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -2.6 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -2.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.9 | -5.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase with thrombospondin type 1 motif 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:70,672,506-70,762,441 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ADAM metallopeptidases with thrombospondin type 1 motif |
| Reactome | 9 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXS8](https://www.uniprot.org/uniprotkb/Q8WXS8) (A disintegrin and metalloproteinase with thrombospondin motifs 14):

> Has aminoprocollagen type I processing activity in the absence of ADAMTS2. Seems to be synthesized as a latent enzyme that requires activation to display aminoprocollagen peptidase activity. Cleaves lysyl oxidase LOX at a site downstream of its propeptide cleavage site to produce a short LOX form.

**Summary**, from NCBI Gene [140766](https://www.ncbi.nlm.nih.gov/gene/140766):

> This gene encodes a member of the ADAMTS (a disintegrin and metalloproteinase with thrombospondin motif) protein family. Members of the family share several distinct protein modules, including a propeptide region, a metalloproteinase domain, a disintegrin-like domain, and a thrombospondin type 1 (TS) motif. Individual members of this family differ in the number of C-terminal TS motifs, and some have unique C-terminal domains. The encoded preproprotein is proteolytically processed to generate …

**Accessions** — [HGNC:14899](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14899) · Entrez [140766](https://www.ncbi.nlm.nih.gov/gene/140766) · UniProt [Q8WXS8](https://www.uniprot.org/uniprotkb/Q8WXS8) · Ensembl [ENSG00000138316](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138316)

## Data

Gene col 6153: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6153); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6153, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6153]; `tensor/DDL_lfc|DDL_z.npy` [6153]; `embed/gene_vectors.npy` [6153]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6153 or target_col == 6153). Every well: [[ADAMTS14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTS14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
