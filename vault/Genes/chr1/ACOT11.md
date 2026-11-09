---
symbol: "ACOT11"
type: "gene"
col: 8508
ensembl_id: "ENSG00000162390"
name: "acyl-CoA thioesterase 11"
location: "1p32.3"
module: 31
arm: "+"
pooled_cpm: 19.48
n_lines_expressing: 39
n_dd_up: 3
n_dd_down: 42
n_dd_up_clean: 2
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 49
direction_downstream: 12
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ACOT11

*acyl-CoA thioesterase 11* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.32× (z +3.8, q 0.080, up in 5 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 1.29× (z +3.6, q 0.080, up in 9 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Betamethasone dipropionate (drug)]] 0.5 µM in 1 line (NCI-H1573 3.30×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H1573 3.18×); [[Dexamethasone (drug)]] 0.05 µM in 1 line (NCI-H1573 3.16×).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.316× (z -22.9, q 0e+00, down in 30 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNS4]] (+0.69, fdr 7e-06), [[MROH7]] (+0.68, fdr 7e-06, ⚠ same locus), [[B3GNT3]] (+0.68, fdr 1e-05), [[LCK]] (+0.62, fdr 1e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 49 arrows point to it, the strongest [[B3GNT3]] → it (grade B ⚠); 12 go from it, the strongest it → [[LMTK3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8508.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Betamethasone dipropionate (drug)]] 0.5 µM in 1 line (NCI-H1573 3.30×); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (NCI-H1573 3.18×); [[Dexamethasone (drug)]] 0.05 µM in 1 line (NCI-H1573 3.16×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +3.8 | 0.080 | 5/21 (AsPC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.080 | 9/36 (NCI-H1573, SK-MEL-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.086 | 13/36 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.3 | 0.13 | 15/37 (LS 180, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8508.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.316×** | -22.9 | 0e+00 | 30/37 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.311×** | -14.9 | 0e+00 | 33/36 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.393×** | -13.1 | 4e-37 | 30/34 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.376×** | -12.4 | 2e-33 | 31/36 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.441×** | -11.1 | 2e-26 | 30/36 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.451×** | -10.8 | 5e-25 | 29/35 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.471×** | -10.6 | 2e-24 | 29/36 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.512×** | -9.4 | 4e-19 | 29/36 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.283×** | -9.3 | 1e-18 | 26/37 (HT-29, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -8.7 | 2e-16 | 21/36 (LS 180, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.524×** | -8.2 | 1e-14 | 24/36 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.583×** | -6.9 | 3e-10 | 25/36 (HT-29, NCI-H23, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.395×** | -6.8 | 4e-10 | 20/35 (LS 180, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.588×** | -6.8 | 6e-10 | 21/36 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.719×** | -6.5 | 2e-09 | 20/37 (HT-29, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.631×** | -6.5 | 3e-09 | 20/36 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.664×** | -5.7 | 3e-07 | 19/36 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8508. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 48.8 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -22.6) |
| [[LoVo (line)]] | wt | 46.3 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -19.5) |
| [[NCI-H1573 (line)]] | alt | 43.0 | 4 | 7 (3 ⚠) | [[Betamethasone dipropionate (drug)]] 0.5 µM 3.30× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.0731× (z -27.6) |
| [[SW480 (line)]] | alt | 36.2 | 0 | 10 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.279× (z -15.4) |
| [[A-172 (line)]] | wt | 30.8 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0932× (z -20.4) |
| [[H4 (line)]] | wt | 28.6 | 0 | 8 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0263× (z -17.9) |
| [[HT-29 (line)]] | alt | 55.7 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -19.3) |
| [[NCI-H23 (line)]] | alt | 43.3 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -22.4) |
| [[COLO 205 (line)]] | alt | 65.3 | 0 | 7 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.00788× (z -29.9) |
| [[HEC-1-A (line)]] | alt | 38.2 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -14.7) |
| [[HOP62 (line)]] | alt | 17.4 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -14.4) |
| [[CFPAC-1 (line)]] | alt | 22.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -14.0) |
| [[CHP-212 (line)]] | wt | 56.3 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0409× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -9.0) |
| [[KATO III (line)]] | alt | 30.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -15.4) |
| [[Panc 03.27 (line)]] | alt | 18.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.149× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 11.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0363× (z -16.4) |
| [[AsPC-1 (line)]] | alt | 23.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -16.2) |
| [[HCT15 (line)]] | alt | 36.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 7.71 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0339× (z -14.8) |
| [[PANC-1 (line)]] | alt | 7.65 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.124× (z -11.8) |
| [[RKO (line)]] | wt | 6.08 | 0 | 2 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0654× (z -9.8) |
| [[SW1417 (line)]] | alt | 38.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -12.5) |
| [[A-427 (line)]] | wt | 27.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 6.75 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0631× (z -16.0) |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 1 | — | [[crizotinib (drug)]] 0.05 µM 0.0815× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 19.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 8.84 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -8.5) |
| [[A498 (line)]] | wt | 4.20 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.84 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8508), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNS4]] | +0.69 | +0.59 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[MROH7]] | +0.68 | +0.64 / +0.72 | both halves | 7e-06 | ⚠ same locus (2.6 kb, same strand: neighbours can correlate without regulation) |
| [[B3GNT3]] | +0.68 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[LCK]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SLC5A1]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[SLC52A3]] | +0.61 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[ATP2C2]] | +0.60 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[ONECUT3]] | +0.60 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[TLDC2]] | +0.59 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[CRYBG2]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[LINC00659]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[ANO1]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[AFAP1L2]] | +0.57 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 48, C 1. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B3GNT3]] | B | B3GNT3 activity raises ACOT11's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.26× lower at baseline in the lines without B3GNT3 | 8e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[CBLC]] | B | CBLC activity raises ACOT11's level | lines that do not express CBLC (31) vs lines expressing it (19) | 3.40× lower at baseline in the lines without CBLC | 0.001 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises ACOT11's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.19× lower at baseline in the lines without TMPRSS4 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[SLC52A3]] | B | SLC52A3 activity raises ACOT11's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.93× lower at baseline in the lines without SLC52A3 | 0.003 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[ZNF860]] | B | ZNF860 activity raises ACOT11's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 2.69× lower at baseline in the lines without ZNF860 | 0.003 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[SH2D3A]] | B | SH2D3A activity raises ACOT11's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 2.67× lower at baseline in the lines without SH2D3A | 0.003 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[RAPGEF5]] | B | RAPGEF5 activity raises ACOT11's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 3.03× lower at baseline in the lines without RAPGEF5 | 0.004 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[CRYBG2]] | B | CRYBG2 activity raises ACOT11's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 2.38× lower at baseline in the lines without CRYBG2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[GPR35]] | B | GPR35 activity raises ACOT11's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 3.03× lower at baseline in the lines without GPR35 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[TMC6]] | B | TMC6 activity raises ACOT11's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 3.03× lower at baseline in the lines without TMC6 | 0.007 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[SLC5A1]] | B | SLC5A1 activity raises ACOT11's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 3.60× lower at baseline in the lines without SLC5A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[SGPP2]] | B | SGPP2 activity raises ACOT11's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 2.93× lower at baseline in the lines without SGPP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMTK3]] | B | ACOT11 activity raises LMTK3's level | lines that do not express ACOT11 (11) vs lines expressing it (39) | 2.87× lower at baseline in the lines without ACOT11 | 0.013 | ⚠ within organs, on part of the lines; also absent: GALM, GALNT6, MROH7; maybe low, not absent |
| [[VASP]] | B | ACOT11 activity raises VASP's level | lines that do not express ACOT11 (11) vs lines expressing it (39) | 1.58× lower at baseline in the lines without ACOT11 | 0.026 | ⚠ within organs, on part of the lines; also absent: GALM, GALNT6, MROH7; maybe low, not absent |
| [[ZNF860]] | B | ACOT11 activity raises ZNF860's level | lines that do not express ACOT11 (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without ACOT11 | 0.046 | ⚠ within organs, on part of the lines; also absent: GALM, GALNT6, MROH7; maybe low, not absent |
| [[TMC6]] | B | ACOT11 activity raises TMC6's level | lines that do not express ACOT11 (11) vs lines expressing it (39) | 2.95× lower at baseline in the lines without ACOT11 | 0.067 | ⚠ within organs, on part of the lines; also absent: GALM, GALNT6, MROH7; maybe low, not absent |
| [[EPHA2-AS1]] | B | ACOT11 activity raises EPHA2-AS1's level | lines that do not express ACOT11 (11) vs lines expressing it (39) | 2.03× lower at baseline in the lines without ACOT11 | 0.078 | ⚠ within organs, on part of the lines; also absent: GALM, GALNT6, MROH7; maybe low, not absent |
| [[CRYBG2]] | B | ACOT11 activity raises CRYBG2's level | lines that do not express ACOT11 (11) vs lines expressing it (39) | 2.44× lower at baseline in the lines without ACOT11 | 0.080 | ⚠ within organs, on part of the lines; also absent: GALM, GALNT6, MROH7; maybe low, not absent |
| [[FBLIM1]] | B | ACOT11 activity raises FBLIM1's level | lines that do not express ACOT11 (11) vs lines expressing it (39) | 2.37× lower at baseline in the lines without ACOT11 | 0.088 | ⚠ within organs, on part of the lines; also absent: GALM, GALNT6, MROH7; maybe low, not absent |
| [[ITPKC]] | B | ACOT11 activity raises ITPKC's level | lines that do not express ACOT11 (11) vs lines expressing it (39) | 1.96× lower at baseline in the lines without ACOT11 | 0.091 | ⚠ within organs, on part of the lines; also absent: GALM, GALNT6, MROH7; maybe low, not absent |
| [[B3GNT3]] | B | ACOT11 activity raises B3GNT3's level | lines that do not express ACOT11 (11) vs lines expressing it (39) | 3.14× lower at baseline in the lines without ACOT11 | 0.092 | ⚠ within organs, on part of the lines; also absent: GALM, GALNT6, MROH7; maybe low, not absent |
| [[CBLC]] | B | ACOT11 activity raises CBLC's level | lines that do not express ACOT11 (11) vs lines expressing it (39) | 3.14× lower at baseline in the lines without ACOT11 | 0.097 | ⚠ within organs, on part of the lines; also absent: GALM, GALNT6, MROH7; maybe low, not absent |
| [[PRAG1]] | B | ACOT11 activity raises PRAG1's level | lines that do not express ACOT11 (11) vs lines expressing it (39) | 2.79× lower at baseline in the lines without ACOT11 | 0.098 | ⚠ within organs, on part of the lines; also absent: GALM, GALNT6, MROH7; maybe low, not absent |
| [[MROH7]] | C | ACOT11 activity raises MROH7's level | lines that do not express ACOT11 (11) vs lines expressing it (39) | 2.53× lower at baseline in the lines without ACOT11 | 0.055 | ⚠ within organs, on part of the lines; also absent: GALM, GALNT6, MROH7; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.620). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.1, 52.2); signed map (60.9, 10.7). **Vector** length 86.5, 20.1% of its response variance represented; |z| ≥ 3 in 1,181 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.4 | +0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +0.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | -1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +0.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.5 | +3.6 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.5 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -6.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.3 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA thioesterase 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:54,542,257-54,639,192 (+) |
| Ensembl biotype | protein_coding |
| Also known as | STARD14, BFIT, KIAA0707, BFIT1, THEM1; previously THEA |
| Gene groups (HGNC) | Acyl-CoA thioesterases; StAR related lipid transfer domain containing; Thioester hydrolases |
| Reactome | 3 pathways, smallest: Mitochondrial Fatty Acid Beta-Oxidation; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXI4](https://www.uniprot.org/uniprotkb/Q8WXI4) (Acyl-coenzyme A thioesterase 11):

> Has an acyl-CoA thioesterase activity with a preference for the long chain fatty acyl-CoA thioesters hexadecanoyl-CoA/palmitoyl-CoA and tetradecanoyl-CoA/myristoyl-CoA which are the main substrates in the mitochondrial beta-oxidation pathway.

**Summary**, from NCBI Gene [26027](https://www.ncbi.nlm.nih.gov/gene/26027):

> This gene encodes a member of the acyl-CoA thioesterase family which catalyse the conversion of activated fatty acids to the corresponding non-esterified fatty acid and coenzyme A. Expression of a mouse homolog in brown adipose tissue is induced by low temperatures and repressed by warm temperatures. Higher levels of expression of the mouse homolog has been found in obesity-resistant mice compared with obesity-prone mice, suggesting a role of acyl-CoA thioesterase 11 in obesity. Alternative …

**Accessions** — [HGNC:18156](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18156) · Entrez [26027](https://www.ncbi.nlm.nih.gov/gene/26027) · UniProt [Q8WXI4](https://www.uniprot.org/uniprotkb/Q8WXI4) · Ensembl [ENSG00000162390](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162390)

## Data

Gene col 8508: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8508); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8508, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8508]; `tensor/DDL_lfc|DDL_z.npy` [8508]; `embed/gene_vectors.npy` [8508]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8508 or target_col == 8508). Every well: [[ACOT11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACOT11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
