---
symbol: "STC2"
type: "gene"
col: 3498
ensembl_id: "ENSG00000113739"
name: "stanniocalcin 2"
location: "5q35.2"
module: 63
arm: "+"
pooled_cpm: 115.32
n_lines_expressing: 37
n_dd_up: 9
n_dd_down: 20
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# STC2

*stanniocalcin 2* — 5q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.76× (z +7.5, q 5e-11, up in 27 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.454× (z -14.8, q 0e+00, down in 26 of 35 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LONP1]] (+0.62, fdr 1e-05), [[GPT2]] (+0.57, fdr 2e-05), [[ABCB6]] (+0.55, fdr 2e-05); moves opposite to [[CMTM6]] (-0.41, fdr 3e-04), [[SMURF1]] (-0.40, fdr 4e-04), [[SUMO2]] (-0.38, fdr 3e-04).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CLGN]] → it (grade B ⚠); 2 go from it, the strongest it → [[KLHL29]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3498.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +7.5 | 5e-11 | 27/35 (Panc 03.27, NCI-H2347, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.63×** | +6.5 | 3e-08 | 27/35 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | **1.30×** | +4.9 | 2e-04 | 21/35 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.37×** | +4.2 | 0.004 | 24/35 (SW480, NCI-H2030, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.37×** | +4.1 | 0.004 | 21/35 (HEC-1-A, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.72×** | +3.8 | 0.017 | 17/35 (A549, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.65×** | +3.5 | 0.044 | 20/35 (NCI-H2030, A498, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.044 | 17/36 (LS 180, H4, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.60×** | +3.2 | 0.077 | 16/35 (NCI-H2347, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3498.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.454×** | -14.8 | 0e+00 | 26/35 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.453×** | -10.1 | 2e-21 | 27/35 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.498×** | -9.2 | 6e-18 | 33/35 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.522×** | -8.6 | 1e-15 | 31/35 (PANC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.549×** | -7.9 | 3e-13 | 21/34 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.597×** | -6.6 | 5e-09 | 21/31 (CHP-212, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.622×** | -6.3 | 3e-08 | 25/35 (PANC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.639×** | -5.7 | 9e-07 | 21/33 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.709×** | -4.5 | 3e-04 | 20/35 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.700×** | -4.5 | 3e-04 | 23/34 (H4, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.792×** | -4.4 | 7e-04 | 18/35 (SK-MEL-2, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.737×** | -4.0 | 0.003 | 20/35 (hTERT-HPNE, SNU-423, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.745×** | -3.7 | 0.008 | 20/36 (J82, SNU-423, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.591×** | -3.6 | 0.011 | 18/35 (LOX-IMVI, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | **0.832×** | -3.4 | 0.022 | 15/35 (A549, SW480, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.773×** | -3.4 | 0.023 | 13/34 (C-33 A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[8-Hydroxyquinoline (drug)]] 5 µM |  | 0.846× | -3.1 | 0.057 | 12/35 (LS 180, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.638×** | -3.1 | 0.057 | 18/36 (HEC-1-A, SNU-423, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3498. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 169 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0622× (z -38.8) |
| [[SW1417 (line)]] | alt | 195 | 1 | 6 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.70× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 135 | 2 | 4 | [[Artesunate (drug)]] 5 µM 2.16× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -19.0) |
| [[SW480 (line)]] | alt | 117 | 1 | 5 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.52× (z +10.4) | [[Harringtonine (drug)]] 5 µM 0.281× (z -13.8) |
| [[SW 900 (line)]] | alt | 644 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -11.8) |
| [[H4 (line)]] | wt | 172 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 188 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -22.1) |
| [[hTERT-HPNE (line)]] | wt | 213 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 129 | 1 | 2 | [[Auranofin (drug)]] 5 µM 3.10× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 141 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 54.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -11.6) |
| [[A498 (line)]] | wt | 37.5 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.43× (z +9.7) | — |
| [[C-33 A (line)]] | alt | 31.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -15.6) |
| [[C32 (line)]] | wt | 37.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -11.6) |
| [[J82 (line)]] | alt | 280 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 146 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 54.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -17.8) |
| [[NCI-H460 (line)]] | wt | 226 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -16.2) |
| [[SHP-77 (line)]] | alt | 55.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -10.1) |
| [[SNU-423 (line)]] | alt | 321 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -17.0) |
| [[A549 (line)]] | wt | 60.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -8.6) |
| [[AN3 CA (line)]] | alt | 47.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.105× (z -8.9) ⚠ toxic |
| [[BT-474 (line)]] | alt | 52.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.1) |
| [[CHP-212 (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0835× (z -11.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 263 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.365× (z -9.0) |
| [[LS 180 (line)]] | wt | 95.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.19× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 56.3 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.07× (z +9.9) ⚠ unreliable plate only | — |
| [[NCI-H2030 (line)]] | alt | 202 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -14.4) |
| [[Panc 03.27 (line)]] | alt | 121 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.75× (z +11.3) | — |
| [[A-172 (line)]] | wt | 9.84 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.58 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.60 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.42 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 19.1 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.69 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.6 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3498), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LONP1]] | +0.62 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[GPT2]] | +0.57 | +0.46 / +0.69 | both halves | 2e-05 |  |
| [[ABCB6]] | +0.55 | +0.48 / +0.61 | both halves | 2e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[EIF2S2]] | +0.55 | +0.37 / +0.64 | both halves | 8e-05 |  |
| [[GARS1]] | +0.53 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[CARS1]] | +0.52 | +0.38 / +0.60 | both halves | 7e-05 |  |
| [[SLC7A5]] | +0.51 | +0.49 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[BNIP3]] | +0.51 | +0.40 / +0.60 | both halves | 4e-05 |  |
| [[DDIT4]] | +0.51 | +0.42 / +0.60 | both halves | 4e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[AARS1]] | +0.51 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[CHAC1]] | +0.50 | +0.37 / +0.60 | both halves | 8e-05 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[YARS1]] | +0.50 | +0.45 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMTM6]] | -0.41 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[SMURF1]] | -0.40 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[SUMO2]] | -0.38 | -0.28 / -0.40 | both halves | 3e-04 |  |
| [[RAB11A]] | -0.37 | -0.32 / -0.39 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLGN]] | B | CLGN activity raises STC2's level | lines that do not express CLGN (17) vs lines expressing it (33) | 2.83× lower at baseline in the lines without CLGN | 0.045 | ⚠ within organs, on part of the lines; also absent: RPS6KA6, VWDE, CLDN1; maybe low, not absent |
| [[VLDLR]] | B | VLDLR activity raises STC2's level | lines that do not express VLDLR (8) vs lines expressing it (42) | 3.90× lower at baseline in the lines without VLDLR | 0.067 | ⚠ within organs, on part of the lines; also absent: NEURL3, ALK, ENSG00000258989 |
| [[BNIP3]] | C | BNIP3 activity raises STC2's level | lines that do not express BNIP3 (11) vs lines expressing it (39) | 5.04× lower at baseline in the lines without BNIP3 | 0.057 | ⚠ within organs, on part of the lines; also absent: SPART, PRKD1, SPART-AS1; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLHL29]] | B | STC2 activity raises KLHL29's level | lines that do not express STC2 (13) vs lines expressing it (37) | 1.22× lower at baseline in the lines without STC2 | 0.068 | ⚠ within organs, on part of the lines; also absent: CHST10, PEG10, ZNF606 |
| [[BNIP3]] | C | STC2 activity raises BNIP3's level | lines that do not express STC2 (13) vs lines expressing it (37) | 5.48× lower at baseline in the lines without STC2 | 0.074 | ⚠ within organs, on part of the lines; also absent: CHST10, PEG10, ZNF606; co-absent with the target |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.514). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.3, 49.4); signed map (-13.9, 26.1). **Vector** length 110, 29.0% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.2 | +7.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.4 | +6.5 |
|  | [[Artesunate (drug)]] 5 µM |  | +4.0 | +4.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.6 | +3.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +3.1 | +4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.0 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.7 | +2.0 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.4 | -6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.1 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -6.9 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.8 | -10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -14.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -2.2 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -1.8 | -1.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | stanniocalcin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:173,314,723-173,328,447 (-) |
| Ensembl biotype | protein_coding |
| Also known as | STC-2 |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, MYOGENESIS, GLYCOLYSIS, HYPOXIA, ESTROGEN_RESPONSE_EARLY |
| Reactome | 2 pathways, smallest: Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [O76061](https://www.uniprot.org/uniprotkb/O76061) (Stanniocalcin-2):

> Has an anti-hypocalcemic action on calcium and phosphate homeostasis.

**Summary**, from NCBI Gene [8614](https://www.ncbi.nlm.nih.gov/gene/8614):

> This gene encodes a secreted, homodimeric glycoprotein that is expressed in a wide variety of tissues and may have autocrine or paracrine functions. The encoded protein has 10 of its 15 cysteine residues conserved among stanniocalcin family members and is phosphorylated by casein kinase 2 exclusively on its serine residues. Its C-terminus contains a cluster of histidine residues which may interact with metal ions. The protein may play a role in the regulation of renal and intestinal calcium and …

**Accessions** — [HGNC:11374](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11374) · Entrez [8614](https://www.ncbi.nlm.nih.gov/gene/8614) · UniProt [O76061](https://www.uniprot.org/uniprotkb/O76061) · Ensembl [ENSG00000113739](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113739)

## Data

Gene col 3498: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3498); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3498, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3498]; `tensor/DDL_lfc|DDL_z.npy` [3498]; `embed/gene_vectors.npy` [3498]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3498 or target_col == 3498). Every well: [[STC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
