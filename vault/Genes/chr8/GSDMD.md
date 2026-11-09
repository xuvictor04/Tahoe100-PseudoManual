---
symbol: "GSDMD"
type: "gene"
col: 2469
ensembl_id: "ENSG00000104518"
name: "gasdermin D"
location: "8q24.3"
module: 70
arm: "+"
pooled_cpm: 8.32
n_lines_expressing: 43
n_dd_up: 1
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 11
direction_downstream: 12
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# GSDMD

*gasdermin D* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.64× (z +4.1, q 0.026, up in 21 of 34 measured lines) ⚠ transcription drop.
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.448× (z -9.2, q 1e-17, down in 28 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OGFR]] (+0.74, fdr 2e-05), [[PSMB9]] (+0.72, fdr 2e-05), [[PSMB10]] (+0.72, fdr 1e-05); moves opposite to [[MSN]] (-0.54, fdr 5e-05), [[DCBLD2]] (-0.53, fdr 3e-05), [[DPYSL2]] (-0.53, fdr 5e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[MX1]] → it (grade B ⚠); 12 go from it, the strongest it → [[UBE2Z]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2469.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.64×** | +4.1 | 0.026 | 21/34 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.53× | +3.3 | 0.17 | 5/14 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Thymol (drug)]] 0.5 µM |  | 1.50× | +3.3 | 0.17 | 15/36 (Hs 766T, HS-578T, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.48× | +3.2 | 0.17 | 12/39 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.50× | +3.2 | 0.17 | 13/38 (SNU-423, HOP62, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | 1.31× | +3.1 | 0.17 | 17/39 (A-172, KATO III, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2469.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.448×** | -9.2 | 1e-17 | 28/35 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.428×** | -6.9 | 1e-09 | 27/40 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.454×** | -6.4 | 2e-08 | 30/40 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.239×** | -6.1 | 2e-07 | 26/37 (LS 180, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.475×** | -6.1 | 2e-07 | 23/37 (A549, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.501×** | -5.6 | 2e-06 | 25/39 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.271×** | -5.6 | 2e-06 | 28/38 (Panc 03.27, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.506×** | -5.5 | 2e-06 | 29/39 (HT-29, PANC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.519×** | -5.3 | 6e-06 | 24/39 (SW480, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.540×** | -5.0 | 3e-05 | 24/40 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.572×** | -4.5 | 3e-04 | 25/38 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.734×** | -3.5 | 0.019 | 18/38 (NCI-H2347, HCT15, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.667×** | -3.3 | 0.042 | 15/37 (SW480, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.657×** | -3.3 | 0.042 | 18/37 (A549, J82, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.678×** | -3.2 | 0.059 | 15/40 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2469. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 8.00 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -12.3) |
| [[SW480 (line)]] | alt | 6.29 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -10.1) |
| [[HT-29 (line)]] | alt | 8.66 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0472× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 4.53 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0512× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 16.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0259× (z -9.2) |
| [[PANC-1 (line)]] | alt | 7.78 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -10.1) |
| [[A-427 (line)]] | wt | 8.70 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.116× (z -9.1) |
| [[A498 (line)]] | wt | 14.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.232× (z -8.7) |
| [[C32 (line)]] | wt | 7.23 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0610× (z -10.0) |
| [[LoVo (line)]] | wt | 6.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 11.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.107× (z -9.9) |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 4.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -8.8) |
| [[A-172 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.694 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.920 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.589 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2469), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OGFR]] | +0.74 | +0.48 / +0.81 | both halves | 2e-05 | **novel candidate** |
| [[PSMB9]] | +0.72 | +0.48 / +0.82 | both halves | 2e-05 |  |
| [[PSMB10]] | +0.72 | +0.53 / +0.77 | both halves | 1e-05 |  |
| [[PSMB8]] | +0.71 | +0.59 / +0.79 | both halves | 7e-06 |  |
| [[DHX58]] | +0.68 | +0.40 / +0.79 | both halves | 5e-05 |  |
| [[UBE2L6]] | +0.67 | +0.46 / +0.74 | both halves | 2e-05 |  |
| [[TAP1]] | +0.67 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[PSME2]] | +0.66 | +0.43 / +0.78 | both halves | 3e-05 |  |
| [[FBXO6]] | +0.66 | +0.40 / +0.79 | both halves | 5e-05 |  |
| [[ZNFX1]] | +0.65 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[ISG15]] | +0.65 | +0.38 / +0.77 | both halves | 6e-05 |  |
| [[IRF7]] | +0.63 | +0.33 / +0.77 | both halves | 1e-04 | pathway: Toll-like Receptor Cascades; STRING 630 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSN]] | -0.54 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[DCBLD2]] | -0.53 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[DPYSL2]] | -0.53 | -0.39 / -0.59 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 6, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MX1]] | B | MX1 activity raises GSDMD's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.76× lower at baseline in the lines without MX1 | 0.028 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[HLA-F]] | B | HLA-F activity raises GSDMD's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 1.77× lower at baseline in the lines without HLA-F | 0.032 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[IFI44L]] | B | IFI44L activity raises GSDMD's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 1.81× lower at baseline in the lines without IFI44L | 0.032 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[IFI16]] | B | IFI16 activity raises GSDMD's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 1.66× lower at baseline in the lines without IFI16 | 0.037 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[IFI44]] | B | IFI44 activity raises GSDMD's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.11× lower at baseline in the lines without IFI44 | 0.071 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[CFB]] | B | CFB activity raises GSDMD's level | lines that do not express CFB (20) vs lines expressing it (30) | 1.79× lower at baseline in the lines without CFB | 0.0996 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[PSMB8]] | C | PSMB8 activity raises GSDMD's level | lines that do not express PSMB8 (4) vs lines expressing it (46) | 4.44× lower at baseline in the lines without PSMB8 | 1e-03 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52; co-absent with the target |
| [[PHF11]] | C | PHF11 activity raises GSDMD's level | lines that do not express PHF11 (3) vs lines expressing it (47) | 4.44× lower at baseline in the lines without PHF11 | 0.014 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| [[IL15]] | C | IL15 activity raises GSDMD's level | lines that do not express IL15 (10) vs lines expressing it (40) | 2.71× lower at baseline in the lines without IL15 | 0.031 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent; co-absent with the target |
| [[GBP3]] | C | GBP3 activity raises GSDMD's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 2.82× lower at baseline in the lines without GBP3 | 0.034 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3; co-absent with the target |
| [[IRF7]] | C | IRF7 activity raises GSDMD's level | lines that do not express IRF7 (11) vs lines expressing it (39) | 2.16× lower at baseline in the lines without IRF7 | 0.083 | ⚠ within organs, on part of the lines; also absent: PLSCR4, GSDMD, LRRK1; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBE2Z]] | B | GSDMD activity raises UBE2Z's level | lines that do not express GSDMD (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without GSDMD | 0.017 | ⚠ within organs, on part of the lines; co-absent genes; also absent: TGFBR2, VDR, IL1RAP |
| [[HLA-F]] | B | GSDMD activity raises HLA-F's level | lines that do not express GSDMD (7) vs lines expressing it (43) | 2.90× lower at baseline in the lines without GSDMD | 0.034 | ⚠ within organs, on part of the lines; co-absent genes; also absent: TGFBR2, VDR, IL1RAP |
| [[MX1]] | B | GSDMD activity raises MX1's level | lines that do not express GSDMD (7) vs lines expressing it (43) | 4.53× lower at baseline in the lines without GSDMD | 0.051 | ⚠ within organs, on part of the lines; co-absent genes; also absent: TGFBR2, VDR, IL1RAP |
| [[TYMP]] | B | GSDMD activity raises TYMP's level | lines that do not express GSDMD (7) vs lines expressing it (43) | 2.72× lower at baseline in the lines without GSDMD | 0.056 | ⚠ within organs, on part of the lines; co-absent genes; also absent: TGFBR2, VDR, IL1RAP |
| [[PHF11]] | B | GSDMD activity raises PHF11's level | lines that do not express GSDMD (7) vs lines expressing it (43) | 2.77× lower at baseline in the lines without GSDMD | 0.074 | ⚠ within organs, on part of the lines; co-absent genes; also absent: TGFBR2, VDR, IL1RAP |
| [[NMI]] | B | GSDMD activity raises NMI's level | lines that do not express GSDMD (7) vs lines expressing it (43) | 2.59× lower at baseline in the lines without GSDMD | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: TGFBR2, VDR, IL1RAP |
| [[IL15RA]] | B | GSDMD activity raises IL15RA's level | lines that do not express GSDMD (7) vs lines expressing it (43) | 1.82× lower at baseline in the lines without GSDMD | 0.097 | ⚠ within organs, on part of the lines; co-absent genes; also absent: TGFBR2, VDR, IL1RAP |
| [[ASPH]] | B | GSDMD activity raises ASPH's level | lines that do not express GSDMD (7) vs lines expressing it (43) | 2.45× lower at baseline in the lines without GSDMD | 0.0997 | ⚠ within organs, on part of the lines; co-absent genes; also absent: TGFBR2, VDR, IL1RAP |
| [[IL15]] | C | GSDMD activity raises IL15's level | lines that do not express GSDMD (7) vs lines expressing it (43) | 3.93× lower at baseline in the lines without GSDMD | 0.014 | ⚠ within organs, on part of the lines; co-absent genes; also absent: TGFBR2, VDR, IL1RAP; co-absent with the target |
| [[IRF7]] | C | GSDMD activity raises IRF7's level | lines that do not express GSDMD (7) vs lines expressing it (43) | 4.68× lower at baseline in the lines without GSDMD | 0.033 | ⚠ within organs, on part of the lines; co-absent genes; also absent: TGFBR2, VDR, IL1RAP; co-absent with the target |
| [[GBP3]] | C | GSDMD activity raises GBP3's level | lines that do not express GSDMD (7) vs lines expressing it (43) | 4.57× lower at baseline in the lines without GSDMD | 0.036 | ⚠ within organs, on part of the lines; co-absent genes; also absent: TGFBR2, VDR, IL1RAP; co-absent with the target |
| [[PSMB8]] | C | GSDMD activity raises PSMB8's level | lines that do not express GSDMD (7) vs lines expressing it (43) | 3.61× lower at baseline in the lines without GSDMD | 0.061 | ⚠ within organs, on part of the lines; co-absent genes; also absent: TGFBR2, VDR, IL1RAP; co-absent with the target |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.709). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.1, 51.1); signed map (62.9, 29.1). **Vector** length 59.6, 12.5% of its response variance represented; |z| ≥ 3 in 670 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.54 to 25); *interferon alpha response* (hallmark, mean cos +0.53 to 19); *Antigen processing-Cross presentation* (reactome, mean cos +0.52 to 14).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.1 | +3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +1.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.1 | +1.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.0 | +4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.5 | -5.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.8 | +0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -6.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.6 | -5.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | gasdermin D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,553,207-143,563,062 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12150, DF5L; previously GSDMDC1 |
| Gene groups (HGNC) | Gasdermins |
| Reactome | 22 pathways, smallest: CASP5-mediated substrate cleavage; CASP4-mediated substrate cleavage; Release of apoptotic factors from the mitochondria |
| Matched by | ensembl_id |

**Function**, from UniProt [P57764](https://www.uniprot.org/uniprotkb/P57764) (Gasdermin-D):

> [Gasdermin-D]: Precursor of a pore-forming protein that plays a key role in host defense against pathogen infection and danger signals. This form constitutes the precursor of the pore-forming protein: upon cleavage, the released N-terminal moiety (Gasdermin-D, N-terminal) binds to membranes and forms pores, triggering pyroptosis.; [Gasdermin-D, N-terminal]: Promotes pyroptosis in response to microbial infection and danger signals. Produced by the cleavage of gasdermin-D by inflammatory caspases …

**Summary**, from NCBI Gene [79792](https://www.ncbi.nlm.nih.gov/gene/79792):

> Gasdermin D is a member of the gasdermin family. Members of this family appear to play a role in regulation of epithelial proliferation. Gasdermin D has been suggested to act as a tumor suppressor. Alternatively spliced transcript variants have been described. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:25697](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25697) · Entrez [79792](https://www.ncbi.nlm.nih.gov/gene/79792) · UniProt [P57764](https://www.uniprot.org/uniprotkb/P57764) · Ensembl [ENSG00000104518](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104518)

## Data

Gene col 2469: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2469); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2469, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2469]; `tensor/DDL_lfc|DDL_z.npy` [2469]; `embed/gene_vectors.npy` [2469]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2469 or target_col == 2469). Every well: [[GSDMD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSDMD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
