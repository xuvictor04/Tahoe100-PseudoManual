---
symbol: "PSMB9"
type: "gene"
col: 14224
ensembl_id: "ENSG00000240065"
name: "proteasome 20S subunit beta 9"
location: "6p21.32"
module: 70
arm: "+"
pooled_cpm: 18.51
n_lines_expressing: 48
n_dd_up: 11
n_dd_down: 19
n_dd_up_clean: 9
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 53
direction_downstream: 1
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# PSMB9

*proteasome 20S subunit beta 9* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.87× (z +4.9, q 4e-04, up in 29 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.476× (z -5.8, q 4e-06, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2L6]] (+0.86, fdr 7e-06), [[GBP4]] (+0.84, fdr 7e-06), [[TAP1]] (+0.84, fdr 7e-06, ⚠ same locus), [[IFI35]] (+0.82, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 53 arrows point to it, the strongest [[EPSTI1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[BTN3A1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14224.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.87×** | +4.9 | 4e-04 | 29/45 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.75×** | +4.2 | 0.006 | 28/44 (NCI-H23, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +4.1 | 0.007 | 29/43 (RPMI-7951, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.1 | 0.007 | 22/43 (LS 180, SHP-77, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.64×** | +3.7 | 0.020 | 25/45 (NCI-H23, AsPC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.020 | 25/46 (NCI-H23, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.59×** | +3.7 | 0.020 | 15/34 (J82, NCI-H2030, …) | inconsistent across doses | composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.54×** | +3.4 | 0.048 | 22/45 (NCI-H23, AsPC-1, …) | two highest doses | noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 5 µM |  | **2.28×** | +3.4 | 0.048 | 18/42 (MIA PaCa-2, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.28×** | +3.3 | 0.062 | 18/40 (KATO III, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.51×** | +3.2 | 0.062 | 19/46 (NCI-H23, AsPC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.32× | +3.1 | 0.10 | 17/46 (NCI-H23, AsPC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14224.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.476×** | -5.8 | 4e-06 | 35/46 (H4, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.599×** | -5.7 | 4e-06 | 28/45 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.495×** | -5.5 | 7e-06 | 30/45 (LoVo, KATO III, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.619×** | -5.3 | 2e-05 | 28/46 (BT-474, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.530×** | -5.0 | 8e-05 | 31/46 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.537×** | -4.6 | 4e-04 | 25/44 (H4, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.577×** | -4.3 | 0.001 | 24/46 (A-172, H4, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.589×** | -4.1 | 0.003 | 24/45 (KATO III, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.630×** | -3.6 | 0.020 | 27/44 (NCI-H661, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.732×** | -3.4 | 0.036 | 23/46 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.738×** | -3.3 | 0.042 | 21/46 (MIA PaCa-2, H4, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.441×** | -3.3 | 0.042 | 17/36 (A-427, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.657×** | -3.3 | 0.046 | 22/46 (LoVo, SW 1088, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.665×** | -3.2 | 0.061 | 21/46 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.460×** | -3.2 | 0.061 | 21/45 (SK-MEL-2, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.465×** | -3.1 | 0.067 | 21/41 (A-427, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14224. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 52.8 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.212× (z -10.9) |
| [[LoVo (line)]] | wt | 28.3 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.112× (z -12.1) |
| [[HS-578T (line)]] | alt | 37.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 17.2 | 1 (1 ⚠) | 2 | [[Adagrasib (drug)]] 0.05 µM 1.88× (z +9.0) ⚠ position not correctable | [[Ixazomib citrate (drug)]] 5 µM 0.117× (z -9.0) |
| [[KATO III (line)]] | alt | 31.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -11.4) |
| [[A498 (line)]] | wt | 32.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -12.1) |
| [[A549 (line)]] | wt | 21.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -10.2) |
| [[BT-474 (line)]] | alt | 9.11 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.149× (z -9.9) |
| [[COLO 205 (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0412× (z -15.4) ⚠ toxic |
| [[H4 (line)]] | wt | 27.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.119× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 19.4 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.92× (z +10.8) ⚠ position not correctable | — |
| [[Panc 03.27 (line)]] | alt | 39.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.170× (z -9.5) |
| [[RKO (line)]] | wt | 9.54 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0636× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 38.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -9.2) |
| [[A-427 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.51 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14224), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2L6]] | +0.86 | +0.77 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 856 |
| [[GBP4]] | +0.84 | +0.83 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 497 |
| [[TAP1]] | +0.84 | +0.79 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 981; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[PSMB8]] | +0.83 | +0.74 / +0.89 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 999; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[IFI35]] | +0.82 | +0.77 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 736 |
| [[OAS1]] | +0.82 | +0.74 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 659 |
| [[ISG15]] | +0.82 | +0.70 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 623 |
| [[IFIH1]] | +0.81 | +0.73 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 492 |
| [[TRIM5]] | +0.81 | +0.75 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFI27]] | +0.80 | +0.70 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFITM3]] | +0.80 | +0.68 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[PSME2]] | +0.80 | +0.68 / +0.85 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 990 |
| [[GBP1]] | +0.80 | +0.82 / +0.78 | both halves | 7e-06 | STRING 745 |
| [[HLA-F]] | +0.79 | +0.69 / +0.82 | both halves | 7e-06 | pathway: Antigen processing-Cross presentation; STRING 723 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 32, C 21. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPSTI1]] | B | EPSTI1 activity raises PSMB9's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 1.95× lower at baseline in the lines without EPSTI1 | 0.011 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[LMO2]] | B | LMO2 activity raises PSMB9's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 1.95× lower at baseline in the lines without LMO2 | 0.019 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[SAMD9]] | B | SAMD9 activity raises PSMB9's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 2.21× lower at baseline in the lines without SAMD9 | 0.024 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[MX1]] | B | MX1 activity raises PSMB9's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.40× lower at baseline in the lines without MX1 | 0.027 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[GBP1]] | B | GBP1 activity raises PSMB9's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.98× lower at baseline in the lines without GBP1 | 0.029 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[IFI44L]] | B | IFI44L activity raises PSMB9's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 1.75× lower at baseline in the lines without IFI44L | 0.033 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[IFI44]] | B | IFI44 activity raises PSMB9's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 1.90× lower at baseline in the lines without IFI44 | 0.033 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[PLAAT4]] | B | PLAAT4 activity raises PSMB9's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.07× lower at baseline in the lines without PLAAT4 | 0.037 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[BATF2]] | B | BATF2 activity raises PSMB9's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.64× lower at baseline in the lines without BATF2 | 0.037 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[RSAD2]] | B | RSAD2 activity raises PSMB9's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.73× lower at baseline in the lines without RSAD2 | 0.039 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[SP110]] | B | SP110 activity raises PSMB9's level | lines that do not express SP110 (5) vs lines expressing it (45) | 2.43× lower at baseline in the lines without SP110 | 0.042 | ⚠ within organs, on part of the lines; also absent: IFIT1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers PSMB9's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.5% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BTN3A1]] | C | PSMB9's natural level strengthens BTN3A1's drug response | PSMB9's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.63; direction not clear | 0.027 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.901). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.5, 51.1); signed map (63.3, 29.0). **Vector** length 115, 36.6% of its response variance represented; |z| ≥ 3 in 849 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon gamma signaling* (reactome, mean cos +0.69 to 13); *Endosomal/Vacuolar pathway* (reactome, mean cos +0.64 to 8); *Antigen Presentation: Folding, assembly and peptide loading of class I MHC* (reactome, mean cos +0.65 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.1 | +4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.6 | +4.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.4 | +3.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.1 | +3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.0 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.8 | +3.7 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -6.1 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -5.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.5 | -1.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.3 | -3.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.2 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 20S subunit beta 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:32,844,136-32,859,851 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RING12, beta1i, PSMB6i; previously LMP2 |
| Gene groups (HGNC) | Proteasome |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, COMPLEMENT, INTERFERON_GAMMA_RESPONSE |
| Reactome | 7 pathways, smallest: Antigen processing: Ub, ATP-independent proteasomal degradation; Cross-presentation of soluble exogenous antigens (endosomes); Proteasome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P28065](https://www.uniprot.org/uniprotkb/P28065) (Proteasome subunit beta type-9):

> The proteasome is a multicatalytic proteinase complex which is characterized by its ability to cleave peptides with Arg, Phe, Tyr, Leu, and Glu adjacent to the leaving group at neutral or slightly basic pH. The proteasome has an ATP-dependent proteolytic activity. This subunit is involved in antigen processing to generate class I binding peptides. Replacement of PSMB6 by PSMB9 increases the capacity of the immunoproteasome to cleave model peptides after hydrophobic and basic residues.

**Summary**, from NCBI Gene [5698](https://www.ncbi.nlm.nih.gov/gene/5698):

> The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent process in a non-lysosomal pathway. An essential function of a modified proteasome, the …

**Accessions** — [HGNC:9546](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9546) · Entrez [5698](https://www.ncbi.nlm.nih.gov/gene/5698) · UniProt [P28065](https://www.uniprot.org/uniprotkb/P28065) · Ensembl [ENSG00000240065](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240065)

## Data

Gene col 14224: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14224); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14224, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14224]; `tensor/DDL_lfc|DDL_z.npy` [14224]; `embed/gene_vectors.npy` [14224]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14224 or target_col == 14224). Every well: [[PSMB9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMB9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
