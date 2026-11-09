---
symbol: "HERC2P3-1"
type: "gene"
col: 16471
ensembl_id: "ENSG00000290376"
name: ""
location: ""
module: 19
arm: "+"
pooled_cpm: 32.26
n_lines_expressing: 27
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 11
direction_downstream: 3
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# HERC2P3-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.26× (z +9.8, q 6e-20, up in 9 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 1.40× (z +4.2, q 0.003, up in 12 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.566× (z -10.1, q 4e-21, down in 20 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01035]] (+0.64, fdr 7e-06), [[COL4A6]] (+0.61, fdr 1e-05), [[SNCA]] (+0.59, fdr 2e-05); moves opposite to [[FZD5]] (-0.44, fdr 5e-05), [[SMPD3]] (-0.43, fdr 1e-04), [[ACTN2]] (-0.42, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TTC28]] → it (grade B ⚠); 3 go from it, the strongest it → [[ZNF605]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16471.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +9.8 | 6e-20 | 9/19 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.18×** | +9.7 | 6e-20 | 9/24 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +6.6 | 8e-09 | 6/21 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.40×** | +4.2 | 0.003 | 12/24 (NCI-H460, PANC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16471.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.566×** | -10.1 | 4e-21 | 20/25 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.469×** | -9.1 | 2e-17 | 21/24 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.569×** | -7.0 | 3e-10 | 12/24 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.640×** | -5.6 | 3e-06 | 19/24 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.671×** | -5.0 | 7e-05 | 16/24 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.477×** | -4.8 | 1e-04 | 16/24 (HS-578T, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.681×** | -4.8 | 1e-04 | 13/24 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.485×** | -4.7 | 2e-04 | 19/24 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.709×** | -4.3 | 0.001 | 8/24 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.743×** | -3.7 | 0.011 | 19/24 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.747×** | -3.7 | 0.012 | 7/24 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -3.7 | 0.012 | 1/25 (NCI-H661) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.775×** | -3.1 | 0.092 | 5/25 (A549, NCI-H23, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16471. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 289 | 0 | 20 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0184× (z -37.2) |
| [[PANC-1 (line)]] | alt | 34.7 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -16.6) |
| [[NCI-H23 (line)]] | alt | 31.6 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.366× (z -9.8) |
| [[BT-474 (line)]] | alt | 128 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.238× (z -9.4) |
| [[C-33 A (line)]] | alt | 96.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -15.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 18.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -11.9) |
| [[SHP-77 (line)]] | alt | 55.7 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -12.5) |
| [[A-427 (line)]] | wt | 26.9 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.252× (z -9.1) |
| [[A498 (line)]] | wt | 20.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -11.9) |
| [[HOP62 (line)]] | alt | 36.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -9.9) |
| [[SW 900 (line)]] | alt | 30.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0753× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.240× (z -8.8) |
| [[A549 (line)]] | wt | 27.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -10.4) |
| [[AN3 CA (line)]] | alt | 106 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 74.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0260× (z -27.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 40.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.194× (z -11.3) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 36.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.207× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -12.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.66 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.24 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.97 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.22 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.40 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.76 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.30 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.99 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.39 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.74 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.41 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16471), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01035]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[COL4A6]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[SNCA]] | +0.59 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[GREM2]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[COL4A5]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[DPP10]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[LINC02864]] | +0.57 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[KCNK2]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[LINC03000]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[NCKAP5-AS2]] | +0.55 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[RTN1]] | +0.54 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[CHL1]] | +0.54 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FZD5]] | -0.44 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[SMPD3]] | -0.43 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[ACTN2]] | -0.42 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[ERICH2-DT]] | -0.42 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[TPM2]] | -0.41 | -0.44 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC28]] | B | TTC28 activity raises HERC2P3-1's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 3.48× lower at baseline in the lines without TTC28 | 0.020 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[PDE10A]] | B | PDE10A activity raises HERC2P3-1's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 2.12× lower at baseline in the lines without PDE10A | 0.044 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90 |
| [[DPP10]] | C | DPP10 activity raises HERC2P3-1's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 3.83× lower at baseline in the lines without DPP10 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[GASK1B-AS1]] | C | GASK1B-AS1 activity raises HERC2P3-1's level | lines that do not express GASK1B-AS1 (37) vs lines expressing it (13) | 2.94× lower at baseline in the lines without GASK1B-AS1 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B, GCG, NPPB; co-absent with the target |
| [[LINC01035]] | C | LINC01035 activity raises HERC2P3-1's level | lines that do not express LINC01035 (43) vs lines expressing it (7) | 3.80× lower at baseline in the lines without LINC01035 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, CALCA, GSG1L2; co-absent with the target |
| [[FENDRR]] | C | FENDRR activity raises HERC2P3-1's level | lines that do not express FENDRR (39) vs lines expressing it (11) | 1.93× lower at baseline in the lines without FENDRR | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000238054, LINC03000, DPP10; co-absent with the target |
| [[HECW2]] | C | HECW2 activity raises HERC2P3-1's level | lines that do not express HECW2 (21) vs lines expressing it (29) | 2.80× lower at baseline in the lines without HECW2 | 0.079 | ⚠ within organs, on part of the lines; also absent: FMN2, GNB4, LINC03041; co-absent with the target |
| [[CDH7]] | C | CDH7 activity raises HERC2P3-1's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 3.54× lower at baseline in the lines without CDH7 | 0.079 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises HERC2P3-1's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 3.81× lower at baseline in the lines without GTF2I-AS1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[CADM2]] | C | CADM2 activity raises HERC2P3-1's level | lines that do not express CADM2 (31) vs lines expressing it (19) | 4.20× lower at baseline in the lines without CADM2 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000263551, KCNH5, KIF1A; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises HERC2P3-1's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 3.93× lower at baseline in the lines without LINC03000 | 0.0997 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF605]] | B | HERC2P3-1 activity raises ZNF605's level | lines that do not express HERC2P3-1 (23) vs lines expressing it (27) | 2.35× lower at baseline in the lines without HERC2P3-1 | 0.090 | ⚠ within organs, on part of the lines; also absent: ZNF880, ENSG00000258732, ZNF829 |
| [[PDE10A]] | B | HERC2P3-1 activity raises PDE10A's level | lines that do not express HERC2P3-1 (23) vs lines expressing it (27) | 2.87× lower at baseline in the lines without HERC2P3-1 | 0.096 | ⚠ within organs, on part of the lines; also absent: ZNF880, ENSG00000258732, ZNF829 |
| [[CADM2]] | C | HERC2P3-1 activity raises CADM2's level | lines that do not express HERC2P3-1 (23) vs lines expressing it (27) | 4.53× lower at baseline in the lines without HERC2P3-1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ZNF880, ENSG00000258732, ZNF829; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.3, 36.7); signed map (41.3, 43.1). **Vector** length 62.2, 16.3% of its response variance represented; |z| ≥ 3 in 528 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +6.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.1 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +1.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.6 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | -0.2 |
|  | [[Vitamin K4 (drug)]] 0.05 µM |  | +1.3 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | -1.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.2 | -9.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.5 | -4.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -0.9 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.1 |

## What is on record

> [!warning] No registry record
> HERC2P3-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16471: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16471); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16471, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16471]; `tensor/DDL_lfc|DDL_z.npy` [16471]; `embed/gene_vectors.npy` [16471]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16471 or target_col == 16471). Every well: [[HERC2P3-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HERC2P3-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
