---
symbol: "UNC93B1"
type: "gene"
col: 3107
ensembl_id: "ENSG00000110057"
name: "unc-93B1 regulator of TLR signaling"
location: "11q13.2"
module: 32
arm: "+"
pooled_cpm: 17.76
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 51
n_dd_up_clean: 0
n_dd_down_clean: 40
in_vector_space: true
direction_upstream: 21
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# UNC93B1

*unc-93B1 regulator of TLR signaling* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.29× (z +3.8, q 0.097, up in 11 of 26 measured lines) ⚠ toxic; transcription drop.
> Pooled over the cell lines (median), lowered significantly by 51 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.343× (z -23.4, q 0e+00, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LY6E]] (+0.64, fdr 7e-06), [[LGALS9]] (+0.61, fdr 7e-06), [[SAMHD1]] (+0.60, fdr 3e-05); moves opposite to [[ST7]] (-0.49, fdr 6e-05), [[KIF21A]] (-0.48, fdr 6e-05), [[YARS2]] (-0.47, fdr 5e-04).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[PARP9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3107.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +3.8 | 0.097 | 11/26 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.26× | +3.5 | 0.11 | 14/33 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Posaconazole (drug)]] 5 µM |  | 1.25× | +3.4 | 0.14 | 3/46 (NCI-H2347, LoVo, …) | top dose only | plate-row cell shift |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.23× | +3.1 | 0.31 | 8/45 (Panc 03.27, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 51 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3107.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.343×** | -23.4 | 0e+00 | 43/46 (BT-474, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.455×** | -17.2 | 0e+00 | 40/44 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.355×** | -15.4 | 0e+00 | 39/45 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.379×** | -15.0 | 0e+00 | 35/43 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.381×** | -14.9 | 0e+00 | 38/44 (KATO III, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.437×** | -12.8 | 2e-35 | 40/46 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.455×** | -11.7 | 9e-30 | 29/39 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.516×** | -10.2 | 1e-22 | 39/46 (AsPC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.539×** | -9.6 | 8e-20 | 28/46 (COLO 205, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.670×** | -8.7 | 1e-16 | 28/47 (CFPAC-1, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.558×** | -8.5 | 9e-16 | 34/45 (Hs 766T, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.580×** | -8.4 | 2e-15 | 33/46 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.582×** | -8.4 | 3e-15 | 33/46 (Hs 766T, MIA PaCa-2, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.607×** | -7.7 | 5e-13 | 31/46 (COLO 205, NCI-H1573, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.603×** | -7.5 | 2e-12 | 23/45 (RKO, SW1417, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.622×** | -7.3 | 7e-12 | 25/45 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.617×** | -7.2 | 3e-11 | 27/45 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[EX229 (drug)]] 5 µM |  | **0.441×** | -6.6 | 1e-09 | 30/44 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3107. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 35.3 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0579× (z -24.2) |
| [[Hs 766T (line)]] | wt | 45.9 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -19.5) |
| [[MIA PaCa-2 (line)]] | alt | 25.3 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -17.5) |
| [[NCI-H23 (line)]] | alt | 28.5 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -22.4) |
| [[SW480 (line)]] | alt | 10.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -13.0) |
| [[LoVo (line)]] | wt | 16.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -13.4) |
| [[SNU-423 (line)]] | alt | 16.4 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.139× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 40.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 41.7 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.355× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 30.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0683× (z -19.0) |
| [[PANC-1 (line)]] | alt | 18.3 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -15.3) |
| [[A-172 (line)]] | wt | 21.6 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0840× (z -16.4) |
| [[A549 (line)]] | wt | 23.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -12.1) |
| [[COLO 205 (line)]] | alt | 24.1 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.129× (z -10.7) |
| [[KATO III (line)]] | alt | 29.3 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.287× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 5.53 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.100× (z -12.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.279× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 41.9 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.289× (z -12.4) |
| [[SW1417 (line)]] | alt | 24.8 | 0 | 3 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -10.7) |
| [[HOP62 (line)]] | alt | 8.83 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -11.0) |
| [[HT-29 (line)]] | alt | 17.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -13.7) |
| [[LOX-IMVI (line)]] | wt | 5.31 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0656× (z -10.9) |
| [[LS 180 (line)]] | wt | 13.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -9.7) |
| [[RKO (line)]] | wt | 15.5 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -11.1) |
| [[SW 900 (line)]] | alt | 13.4 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -9.1) |
| [[A-427 (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0980× (z -12.4) ⚠ toxic |
| [[A498 (line)]] | wt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -10.5) |
| [[HS-578T (line)]] | alt | 8.80 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.137× (z -9.3) |
| [[J82 (line)]] | alt | 21.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -13.5) |
| [[AN3 CA (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3107), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LY6E]] | +0.64 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[LGALS9]] | +0.61 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[SAMHD1]] | +0.60 | +0.43 / +0.69 | both halves | 3e-05 |  |
| [[SHFL]] | +0.60 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[TDRD7]] | +0.60 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[TRIM34]] | +0.60 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[STAT2]] | +0.60 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[PML]] | +0.59 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[STAT1]] | +0.59 | +0.39 / +0.68 | both halves | 5e-05 | STRING 444 |
| [[TRIM14]] | +0.59 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[GMPR]] | +0.59 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[MX1]] | +0.58 | +0.50 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST7]] | -0.49 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[KIF21A]] | -0.48 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[YARS2]] | -0.47 | -0.34 / -0.23 | both halves | 5e-04 |  |
| [[BFSP1]] | -0.45 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[STEAP1B]] | -0.45 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[KLHL42]] | -0.45 | -0.42 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[MYLK-AS1]] | -0.45 | -0.50 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 21, C 0. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARP9]] | B | PARP9 activity raises UNC93B1's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.04× lower at baseline in the lines without PARP9 | 0.001 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[BATF2]] | B | BATF2 activity raises UNC93B1's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without BATF2 | 0.001 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[PLSCR1]] | B | PLSCR1 activity raises UNC93B1's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without PLSCR1 | 0.006 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[IFI44L]] | B | IFI44L activity raises UNC93B1's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 1.38× lower at baseline in the lines without IFI44L | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[MX1]] | B | MX1 activity raises UNC93B1's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.53× lower at baseline in the lines without MX1 | 0.008 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[OAS1]] | B | OAS1 activity raises UNC93B1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.51× lower at baseline in the lines without OAS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[OAS2]] | B | OAS2 activity raises UNC93B1's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 1.44× lower at baseline in the lines without OAS2 | 0.012 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[ETV7]] | B | ETV7 activity raises UNC93B1's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 1.84× lower at baseline in the lines without ETV7 | 0.018 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[UBA7]] | B | UBA7 activity raises UNC93B1's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 1.87× lower at baseline in the lines without UBA7 | 0.018 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[CMPK2]] | B | CMPK2 activity raises UNC93B1's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 1.30× lower at baseline in the lines without CMPK2 | 0.028 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[IFI6]] | B | IFI6 activity raises UNC93B1's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 1.57× lower at baseline in the lines without IFI6 | 0.034 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[IFI44]] | B | IFI44 activity raises UNC93B1's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 1.46× lower at baseline in the lines without IFI44 | 0.038 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.515). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.5, 54.7); signed map (67.1, 32.4). **Vector** length 77.3, 16.9% of its response variance represented; |z| ≥ 3 in 1,306 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISG15 antiviral mechanism* (reactome, mean cos +0.52 to 11); *OAS antiviral response* (reactome, mean cos +0.51 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +5.2 | -3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +5.1 | -5.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +4.4 | -5.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.8 | +1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -5.0 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +1.1 | +2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.0 | +2.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.0 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.2 | -8.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.0 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.9 | -8.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.4 | -4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -17.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -3.0 | -4.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.0 | -3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | unc-93B1 regulator of TLR signaling |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:67,991,100-68,004,982 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UNC93, UNC-93B |
| Gene groups (HGNC) | Unc-93 related family |
| Reactome | 5 pathways, smallest: Trafficking and processing of endosomal TLR; Diseases associated with the TLR signaling cascade; Diseases of Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1C4](https://www.uniprot.org/uniprotkb/Q9H1C4) (Protein unc-93 homolog B1):

> Plays an important role in innate and adaptive immunity by regulating nucleotide-sensing Toll-like receptor (TLR) signaling. Required for the transport of a subset of TLRs (including TLR3, TLR7 and TLR9) from the endoplasmic reticulum to endolysosomes where they can engage pathogen nucleotides and activate signaling cascades. May play a role in autoreactive B-cells removal.

**Summary**, from NCBI Gene [81622](https://www.ncbi.nlm.nih.gov/gene/81622):

> This gene encodes a protein that is involved in innate and adaptive immune response by regulating toll-like receptor signaling. The encoded protein traffics nucleotide sensing toll-like receptors to the endolysosome from the endoplasmic reticulum. Deficiency of the encoded protein has been associated with herpes simplex encephalitis. [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:13481](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13481) · Entrez [81622](https://www.ncbi.nlm.nih.gov/gene/81622) · UniProt [Q9H1C4](https://www.uniprot.org/uniprotkb/Q9H1C4) · Ensembl [ENSG00000110057](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110057)

## Data

Gene col 3107: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3107); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3107, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3107]; `tensor/DDL_lfc|DDL_z.npy` [3107]; `embed/gene_vectors.npy` [3107]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3107 or target_col == 3107). Every well: [[UNC93B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UNC93B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
