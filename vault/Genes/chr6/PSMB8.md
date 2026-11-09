---
symbol: "PSMB8"
type: "gene"
col: 12840
ensembl_id: "ENSG00000204264"
name: "proteasome 20S subunit beta 8"
location: "6p21.32"
module: 32
arm: "+"
pooled_cpm: 16.65
n_lines_expressing: 46
n_dd_up: 8
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 56
direction_downstream: 63
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# PSMB8

*proteasome 20S subunit beta 8* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.94× (z +6.3, q 2e-07, up in 35 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.320× (z -10.7, q 3e-24, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NMI]] (+0.86, fdr 7e-06), [[IFIH1]] (+0.84, fdr 7e-06), [[TAP1]] (+0.84, fdr 7e-06, ⚠ same locus), [[PARP14]] (+0.83, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 56 arrows point to it, the strongest [[GBP1]] → it (grade B ⚠); 63 go from it, the strongest it → [[GSDMD]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12840.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.94×** | +6.3 | 2e-07 | 35/44 (PANC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.79×** | +5.6 | 8e-06 | 30/41 (SNU-423, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +3.8 | 0.022 | 21/44 (HS-578T, PANC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.022 | 18/44 (CFPAC-1, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.023 | 18/44 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.061 | 19/41 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.068 | 20/44 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.43×** | +3.3 | 0.071 | 10/27 (NCI-H1792, J82, …) | rises with dose | composition shift; position effect removed |
| [[Arbutin (drug)]] 5 µM |  | 1.40× | +3.1 | 0.11 | 14/42 (SNU-423, A498, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.40× | +3.1 | 0.11 | 19/42 (NCI-H1573, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 1 with an alert ⚠; shown: the 15 strongest. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12840.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.320×** | -10.7 | 3e-24 | 42/44 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.322×** | -10.7 | 3e-24 | 42/44 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.365×** | -9.5 | 4e-19 | 38/43 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.537×** | -5.9 | 7e-07 | 30/44 (HS-578T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.574×** | -5.2 | 2e-05 | 29/44 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.697×** | -4.7 | 2e-04 | 27/44 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.634×** | -4.3 | 0.001 | 25/41 (LOX-IMVI, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.646×** | -4.1 | 0.003 | 23/43 (KATO III, LoVo, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.646×** | -4.1 | 0.003 | 23/43 (MIA PaCa-2, COLO 205, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.652×** | -4.0 | 0.003 | 23/42 (LoVo, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.642×** | -3.9 | 0.004 | 22/42 (COLO 205, A549, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.667×** | -3.8 | 0.007 | 22/42 (LoVo, A549, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.674×** | -3.7 | 0.009 | 19/42 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.675×** | -3.7 | 0.009 | 23/43 (NCI-H23, A549, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.756×** | -3.6 | 0.011 | 23/44 (H4, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12840. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 35.4 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.193× (z -10.9) |
| [[LoVo (line)]] | wt | 27.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -13.6) |
| [[A-172 (line)]] | wt | 32.8 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.116× (z -13.6) |
| [[COLO 205 (line)]] | alt | 32.5 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.161× (z -9.8) |
| [[A498 (line)]] | wt | 32.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -8.6) |
| [[HS-578T (line)]] | alt | 23.0 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.167× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 41.8 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.425× (z -8.7) |
| [[HT-29 (line)]] | alt | 9.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 9.03 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0854× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 26.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.306× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -9.4) |
| [[SW1417 (line)]] | alt | 17.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.210× (z -8.6) |
| [[A-427 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12840), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMI]] | +0.86 | +0.80 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 566 |
| [[IFIH1]] | +0.84 | +0.79 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 496 |
| [[TAP1]] | +0.84 | +0.72 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 973; ⚠ same locus (0.5 kb, same strand: neighbours can correlate without regulation) |
| [[PARP14]] | +0.83 | +0.79 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[PSMB9]] | +0.83 | +0.74 / +0.89 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 999; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[IFIT3]] | +0.82 | +0.77 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 519 |
| [[GBP1]] | +0.82 | +0.80 / +0.82 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 641 |
| [[APOL6]] | +0.81 | +0.72 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[TLR3]] | +0.81 | +0.75 / +0.79 | both halves | 7e-06 |  |
| [[TRANK1]] | +0.81 | +0.82 / +0.78 | both halves | 7e-06 |  |
| [[TRIM21]] | +0.81 | +0.68 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 418 |
| [[DTX3L]] | +0.80 | +0.74 / +0.80 | both halves | 7e-06 |  |
| [[PSMB10]] | +0.80 | +0.69 / +0.79 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 999 |
| [[PARP9]] | +0.79 | +0.69 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 444 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*56 arrows, 56 of them with an alert ⚠; grade A 0, B 38, C 18. Shown: the 12 strongest; 44 more arrows (44 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP1]] | B | GBP1 activity raises PSMB8's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.57× lower at baseline in the lines without GBP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[IFI44]] | B | IFI44 activity raises PSMB8's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.72× lower at baseline in the lines without IFI44 | 0.006 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[GBP4]] | B | GBP4 activity raises PSMB8's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.31× lower at baseline in the lines without GBP4 | 0.011 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[HLA-F]] | B | HLA-F activity raises PSMB8's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 2.21× lower at baseline in the lines without HLA-F | 0.011 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[IFI44L]] | B | IFI44L activity raises PSMB8's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 2.20× lower at baseline in the lines without IFI44L | 0.011 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[IL15]] | B | IL15 activity raises PSMB8's level | lines that do not express IL15 (10) vs lines expressing it (40) | 3.14× lower at baseline in the lines without IL15 | 0.012 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[SAMD9]] | B | SAMD9 activity raises PSMB8's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 2.93× lower at baseline in the lines without SAMD9 | 0.014 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[HCP5]] | B | HCP5 activity raises PSMB8's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 1.97× lower at baseline in the lines without HCP5 | 0.015 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[HERC6]] | B | HERC6 activity raises PSMB8's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 2.62× lower at baseline in the lines without HERC6 | 0.016 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[EPSTI1]] | B | EPSTI1 activity raises PSMB8's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.29× lower at baseline in the lines without EPSTI1 | 0.020 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[CXCL3]] | B | CXCL3 activity raises PSMB8's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 2.49× lower at baseline in the lines without CXCL3 | 0.024 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[OAS1]] | B | OAS1 activity raises PSMB8's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.57× lower at baseline in the lines without OAS1 | 0.027 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |

### Downstream of this gene

*63 arrows, 63 of them with an alert ⚠; grade A 0, B 0, C 63. Shown: the 12 strongest; 51 more arrows (51 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GSDMD]] | C | PSMB8 activity raises GSDMD's level | lines that do not express PSMB8 (4) vs lines expressing it (46) | 4.44× lower at baseline in the lines without PSMB8 | 1e-03 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52; co-absent with the target |
| [[CEBPD]] | C | PSMB8 activity raises CEBPD's level | lines that do not express PSMB8 (4) vs lines expressing it (46) | 4.88× lower at baseline in the lines without PSMB8 | 0.004 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52; co-absent with the target |
| cells under [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM | C | PSMB8 activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 0.71× the cells of the other lines | 0.004 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM | C | PSMB8 activity raises the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (protects the cells) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 0.75× the cells of the other lines | 0.004 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | C | PSMB8 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 0.73× the cells of the other lines | 0.004 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | PSMB8 activity raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 0.70× the cells of the other lines | 0.008 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| cells under [[Sulfatinib (drug)]] 5 µM | C | PSMB8 activity raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 0.69× the cells of the other lines | 0.008 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| cells under [[Pentoxifylline (drug)]] 0.5 µM | C | PSMB8 activity raises the cells' numbers under Pentoxifylline 0.5 µM (protects the cells) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 0.73× the cells of the other lines | 0.013 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| cells under [[Entecavir (monohydrate) (drug)]] 0.5 µM | C | PSMB8 activity raises the cells' numbers under Entecavir (monohydrate) 0.5 µM (protects the cells) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 0.68× the cells of the other lines | 0.015 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | PSMB8 activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 0.76× the cells of the other lines | 0.015 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| [[PHF11]] | C | PSMB8 activity raises PHF11's level | lines that do not express PSMB8 (4) vs lines expressing it (46) | 3.29× lower at baseline in the lines without PSMB8 | 0.016 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| [[IFIH1]] | C | PSMB8 activity raises IFIH1's level | lines that do not express PSMB8 (4) vs lines expressing it (46) | 2.96× lower at baseline in the lines without PSMB8 | 0.016 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.828). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.3, 52.3); signed map (62.4, 30.1). **Vector** length 107, 31.1% of its response variance represented; |z| ≥ 3 in 879 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.73 to 23); *Interferon gamma signaling* (reactome, mean cos +0.67 to 17); *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.73 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.3 | +6.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.4 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +2.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.8 | +3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.6 | +3.1 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -4.9 | -4.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.2 | -3.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.1 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.9 | -3.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 20S subunit beta 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:32,840,717-32,844,679 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RING10, D6S216E, PSMB5i, beta5i; previously LMP7 |
| Gene groups (HGNC) | Proteasome |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, KRAS_SIGNALING_UP, INTERFERON_GAMMA_RESPONSE |
| Reactome | 10 pathways, smallest: Antigen processing: Ub, ATP-independent proteasomal degradation; Cross-presentation of soluble exogenous antigens (endosomes); Proteasome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P28062](https://www.uniprot.org/uniprotkb/P28062) (Proteasome subunit beta type-8):

> The proteasome is a multicatalytic proteinase complex which is characterized by its ability to cleave peptides with Arg, Phe, Tyr, Leu, and Glu adjacent to the leaving group at neutral or slightly basic pH. The proteasome has an ATP-dependent proteolytic activity. This subunit is involved in antigen processing to generate class I binding peptides. Replacement of PSMB5 by PSMB8 increases the capacity of the immunoproteasome to cleave model peptides after hydrophobic and basic residues. Involved …

**Summary**, from NCBI Gene [5696](https://www.ncbi.nlm.nih.gov/gene/5696):

> The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent process in a non-lysosomal pathway. An essential function of a modified proteasome, the …

**Accessions** — [HGNC:9545](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9545) · Entrez [5696](https://www.ncbi.nlm.nih.gov/gene/5696) · UniProt [P28062](https://www.uniprot.org/uniprotkb/P28062) · Ensembl [ENSG00000204264](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204264)

## Data

Gene col 12840: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12840); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12840, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12840]; `tensor/DDL_lfc|DDL_z.npy` [12840]; `embed/gene_vectors.npy` [12840]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12840 or target_col == 12840). Every well: [[PSMB8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMB8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
