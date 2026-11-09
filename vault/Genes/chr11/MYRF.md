---
symbol: "MYRF"
type: "gene"
col: 4581
ensembl_id: "ENSG00000124920"
name: "myelin regulatory factor"
location: "11q12.2"
module: 31
arm: "+"
pooled_cpm: 18.06
n_lines_expressing: 41
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 17
direction_downstream: 1
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# MYRF

*myelin regulatory factor* — 11q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.26× (z +4.6, q 0.003, up in 13 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (SW480 3.64×).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.343× (z -21.4, q 0e+00, down in 30 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA3F]] (+0.64, fdr 1e-05), [[ARHGEF16]] (+0.62, fdr 1e-05), [[ANXA11]] (+0.60, fdr 1e-05); moves opposite to [[IFT74]] (-0.56, fdr 3e-05), [[DNAJC27]] (-0.51, fdr 6e-05), [[ACAD11]] (-0.51, fdr 9e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[INAVA]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NCOR2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4581.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (SW480 3.64×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.6 | 0.003 | 13/38 (PANC-1, HCT15, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.30×** | +3.7 | 0.038 | 9/35 (PANC-1, A498, …) | rises with dose | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.038 | 11/35 (NCI-H23, PANC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4581.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.343×** | -21.4 | 0e+00 | 30/34 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.454×** | -15.8 | 0e+00 | 31/34 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.369×** | -13.6 | 1e-39 | 30/36 (NCI-H2030, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.460×** | -11.0 | 6e-26 | 24/31 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.395×** | -6.9 | 7e-10 | 26/35 (COLO 205, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.629×** | -6.3 | 2e-08 | 19/34 (HT-29, CFPAC-1, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.627×** | -6.3 | 3e-08 | 18/37 (H4, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.698×** | -5.1 | 2e-05 | 18/38 (HT-29, SW1417, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.707×** | -4.9 | 6e-05 | 19/38 (HT-29, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.713×** | -4.8 | 1e-04 | 17/37 (HT-29, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.736×** | -4.2 | 0.002 | 17/33 (HT-29, RKO, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.579×** | -4.0 | 0.003 | 11/35 (HT-29, KATO III, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.774×** | -3.6 | 0.013 | 11/37 (NCI-H2030, hTERT-HPNE, …) | all doses, flat | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.794×** | -3.3 | 0.044 | 8/36 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.857× | -3.1 | 0.076 | 12/38 (HOP62, SW 900, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.666×** | -3.0 | 0.093 | 10/33 (LS 180, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4581. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 21.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -16.6) |
| [[HT-29 (line)]] | alt | 62.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -20.4) |
| [[LS 180 (line)]] | wt | 35.4 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.247× (z -15.2) |
| [[SW480 (line)]] | alt | 42.9 | 1 | 4 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.64× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 55.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -22.0) |
| [[HEC-1-A (line)]] | alt | 24.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -13.9) |
| [[LoVo (line)]] | wt | 27.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -20.6) |
| [[NCI-H2030 (line)]] | alt | 9.40 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 33.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -13.8) |
| [[SW1417 (line)]] | alt | 56.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -10.3) |
| [[A-427 (line)]] | wt | 11.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.154× (z -10.1) |
| [[COLO 205 (line)]] | alt | 24.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -14.3) |
| [[KATO III (line)]] | alt | 41.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -13.8) |
| [[PANC-1 (line)]] | alt | 5.30 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.329× (z -8.5) |
| [[A549 (line)]] | wt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 41.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -12.5) |
| [[H4 (line)]] | wt | 7.88 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0499× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 24.3 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.191× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 7.21 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0750× (z -8.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 5.19 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 16.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -15.5) |
| [[SW 900 (line)]] | alt | 6.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -11.1) |
| [[SW48 (line)]] | wt | 37.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -15.8) |
| [[A-172 (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.00 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.69 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4581), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA3F]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ARHGEF16]] | +0.62 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[ANXA11]] | +0.60 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[TINAGL1]] | +0.58 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[NBEAL2]] | +0.57 | +0.65 / +0.36 | both halves | 9e-05 |  |
| [[SH3BP1]] | +0.57 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[MPRIP]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[CCDC120]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[TMC6]] | +0.56 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[ARHGAP8]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[CRYBG2]] | +0.54 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[UNC5A]] | +0.54 | +0.36 / +0.52 | both halves | 1e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT74]] | -0.56 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[DNAJC27]] | -0.51 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[ACAD11]] | -0.51 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[SCGB2B2]] | -0.50 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[ASH1L]] | -0.49 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[POLI]] | -0.48 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[MFF-DT]] | -0.47 | -0.58 / -0.24 | both halves | 5e-04 |  |
| [[WHAMMP3]] | -0.47 | -0.50 / -0.25 | both halves | 4e-04 |  |
| [[GTF2IRD2B]] | -0.47 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[ZFY]] | -0.46 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[ANKRD26]] | -0.46 | -0.52 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 16, C 1. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INAVA]] | B | INAVA activity raises MYRF's level | lines that do not express INAVA (29) vs lines expressing it (21) | 3.67× lower at baseline in the lines without INAVA | 6e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[B3GNT3]] | B | B3GNT3 activity raises MYRF's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.40× lower at baseline in the lines without B3GNT3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[PADI1]] | B | PADI1 activity raises MYRF's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 3.33× lower at baseline in the lines without PADI1 | 0.002 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[KLK11]] | B | KLK11 activity raises MYRF's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 4.26× lower at baseline in the lines without KLK11 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ |
| [[EPS8L3]] | B | EPS8L3 activity raises MYRF's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 4.13× lower at baseline in the lines without EPS8L3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[PRSS3]] | B | PRSS3 activity raises MYRF's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 3.03× lower at baseline in the lines without PRSS3 | 0.016 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[SPINT1]] | B | SPINT1 activity raises MYRF's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 2.97× lower at baseline in the lines without SPINT1 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |
| [[TINAGL1]] | B | TINAGL1 activity raises MYRF's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.88× lower at baseline in the lines without TINAGL1 | 0.032 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[SEMA3B]] | B | SEMA3B activity raises MYRF's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.75× lower at baseline in the lines without SEMA3B | 0.033 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[CRYBG2]] | B | CRYBG2 activity raises MYRF's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 2.65× lower at baseline in the lines without CRYBG2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[MYO5B]] | B | MYO5B activity raises MYRF's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 2.68× lower at baseline in the lines without MYO5B | 0.054 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[EPS8L1]] | B | EPS8L1 activity raises MYRF's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 1.92× lower at baseline in the lines without EPS8L1 | 0.057 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCOR2]] | B | MYRF activity lowers NCOR2's level | lines that do not express MYRF (9) vs lines expressing it (41) | 1.20× higher at baseline in the lines without MYRF | 0.060 | ⚠ within organs, on part of the lines; also absent: EPB41L4B, IL23A; its own permutation p |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.584). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.6, 56.6); signed map (-14.5, 35.7). **Vector** length 76.1, 16.2% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.1 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.5 | -0.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +3.3 | +3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.0 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | -0.2 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.4 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +0.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.0 | -6.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.3 | -13.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -11.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.3 | -21.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -4.0 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | myelin regulatory factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.2 — chr11:61,752,636-61,788,518 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Ndt80, pqn-47, MRF; previously C11orf9 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2G1](https://www.uniprot.org/uniprotkb/Q9Y2G1) (Myelin regulatory factor):

> [Myelin regulatory factor]: Constitutes a precursor of the transcription factor. Mediates the autocatalytic cleavage that releases the Myelin regulatory factor, N-terminal component that specifically activates transcription of central nervous system (CNS) myelin genes.; [Myelin regulatory factor, C-terminal]: Membrane-bound part that has no transcription factor activity and remains attached to the endoplasmic reticulum membrane following cleavage.; [Myelin regulatory factor, N-terminal]: …

**Summary**, from NCBI Gene [745](https://www.ncbi.nlm.nih.gov/gene/745):

> This gene encodes a transcription factor that is required for central nervous system myelination and may regulate oligodendrocyte differentiation. It is thought to act by increasing the expression of genes that effect myelin production but may also directly promote myelin gene expression. Loss of a similar gene in mouse models results in severe demyelination. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2014]

**Accessions** — [HGNC:1181](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1181) · Entrez [745](https://www.ncbi.nlm.nih.gov/gene/745) · UniProt [Q9Y2G1](https://www.uniprot.org/uniprotkb/Q9Y2G1) · Ensembl [ENSG00000124920](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124920)

## Data

Gene col 4581: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4581); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4581, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4581]; `tensor/DDL_lfc|DDL_z.npy` [4581]; `embed/gene_vectors.npy` [4581]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4581 or target_col == 4581). Every well: [[MYRF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYRF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
