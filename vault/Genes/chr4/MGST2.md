---
symbol: "MGST2"
type: "gene"
col: 1444
ensembl_id: "ENSG00000085871"
name: "microsomal glutathione S-transferase 2"
location: "4q31.1"
module: 55
arm: "+"
pooled_cpm: 18.87
n_lines_expressing: 40
n_dd_up: 7
n_dd_down: 32
n_dd_up_clean: 6
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 23
direction_downstream: 11
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# MGST2

*microsomal glutathione S-transferase 2* — 4q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.60× (z +7.4, q 1e-10, up in 27 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.234× (z -22.8, q 0e+00, down in 34 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXB3]] (+0.60, fdr 2e-05), [[ADD3-AS1]] (+0.57, fdr 3e-05), [[HNMT]] (+0.57, fdr 1e-05); moves opposite to [[RSU1]] (-0.59, fdr 4e-05), [[GPSM1]] (-0.51, fdr 6e-05), [[MFSD12]] (-0.49, fdr 5e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[TMPRSS3]] → it (grade B ⚠); 11 go from it, the strongest it → [[FRK]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1444.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.60×** | +7.4 | 1e-10 | 27/38 (Hs 766T, HOP62, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +5.7 | 4e-06 | 17/38 (RKO, LS 180, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.40×** | +5.3 | 2e-05 | 15/37 (LoVo, HOP62, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.74×** | +4.5 | 0.001 | 9/34 (AsPC-1, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 0.003 | 13/37 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.8 | 0.016 | 9/33 (J82, A498, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.073 | 10/38 (NCI-H1573, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.23× | +3.2 | 0.11 | 4/23 (PANC-1, A498, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Arbutin (drug)]] 5 µM |  | 1.22× | +3.0 | 0.14 | 6/36 (A-172, J82, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | 1.23× | +3.0 | 0.14 | 8/36 (NCI-H2347, HCT15, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.31× | +3.0 | 0.14 | 7/36 (AsPC-1, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1444.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.234×** | -22.8 | 0e+00 | 34/37 (LS 180, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.305×** | -18.6 | 0e+00 | 35/37 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.445×** | -17.9 | 0e+00 | 32/38 (Hs 766T, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.344×** | -16.7 | 0e+00 | 35/37 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.444×** | -12.7 | 6e-35 | 33/37 (HepG2/C3A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.448×** | -12.6 | 3e-34 | 28/35 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.551×** | -9.3 | 8e-19 | 27/36 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.555×** | -9.2 | 2e-18 | 28/37 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.562×** | -8.7 | 2e-16 | 26/37 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.699×** | -7.9 | 1e-13 | 26/38 (HepG2/C3A, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.640×** | -7.0 | 1e-10 | 24/37 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.640×** | -7.0 | 1e-10 | 25/37 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.631×** | -6.9 | 2e-10 | 19/34 (HepG2/C3A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.658×** | -6.5 | 2e-09 | 20/37 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.687×** | -5.9 | 2e-07 | 19/37 (HepG2/C3A, NCI-H460, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.697×** | -5.7 | 5e-07 | 21/37 (SNU-423, SW1417, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.690×** | -5.6 | 7e-07 | 23/37 (HepG2/C3A, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1444. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 45.2 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0806× (z -19.9) |
| [[NCI-H460 (line)]] | wt | 26.1 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -20.2) |
| [[Hs 766T (line)]] | wt | 102 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -27.5) |
| [[HepG2_C3A (line)]] | wt | 82.4 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -14.1) |
| [[LS 180 (line)]] | wt | 80.4 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -21.7) |
| [[Panc 03.27 (line)]] | alt | 25.1 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -12.8) |
| [[COLO 205 (line)]] | alt | 42.5 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -20.3) |
| [[HEC-1-A (line)]] | alt | 27.1 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.169× (z -16.2) |
| [[LoVo (line)]] | wt | 28.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -18.4) |
| [[SW480 (line)]] | alt | 21.8 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -18.0) |
| [[AsPC-1 (line)]] | alt | 18.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 25.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 26.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.166× (z -12.0) |
| [[A498 (line)]] | wt | 13.6 | 1 (1 ⚠) | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -11.8) |
| [[HOP62 (line)]] | alt | 12.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -11.2) |
| [[HT-29 (line)]] | alt | 19.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.244× (z -9.1) |
| [[A-172 (line)]] | wt | 9.26 | 0 | 1 | — | [[Irinotecan (hydrochloride) (drug)]] 0.05 µM 0.0414× (z -14.8) |
| [[NCI-H2030 (line)]] | alt | 7.91 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.165× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -9.5) |
| [[RKO (line)]] | wt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -9.2) |
| [[SW1417 (line)]] | alt | 14.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -9.2) |
| [[A-427 (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.66 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.40 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.04 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1444), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXB3]] | +0.60 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[ADD3-AS1]] | +0.57 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[HNMT]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[HSD17B2]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[PARP8]] | +0.57 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[MANSC1]] | +0.57 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[IL20RA]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[HOXB6]] | +0.55 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[CHN2]] | +0.54 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[ST6GALNAC1]] | +0.54 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[SULF2]] | +0.54 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[CLRN3]] | +0.53 | +0.47 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSU1]] | -0.59 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[GPSM1]] | -0.51 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[MFSD12]] | -0.49 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[R3HDM4]] | -0.49 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[DLGAP4]] | -0.46 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[MAP1B]] | -0.46 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[ZNF598]] | -0.46 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[L1CAM]] | -0.45 | -0.42 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 23, C 0. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMPRSS3]] | B | TMPRSS3 activity strengthens MGST2's drug response | lines that do not express TMPRSS3 (21) vs lines expressing it (17) | the lines without TMPRSS3 respond 0.55× as strongly (z diff +2.72); strongest at Panobinostat 0.5 µM: 0.35x vs 0.18x (z diff +4.1) | 0.006 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2; target measured in part of the lines; artifact flags |
| [[TSPAN8]] | B | TSPAN8 activity raises MGST2's level | lines that do not express TSPAN8 (34) vs lines expressing it (16) | 2.81× lower at baseline in the lines without TSPAN8 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000267881, SERPINB5, CDH17 |
| [[PRR15]] | B | PRR15 activity raises MGST2's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.79× lower at baseline in the lines without PRR15 | 0.010 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[TMPRSS3]] | B | TMPRSS3 activity raises MGST2's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.57× lower at baseline in the lines without TMPRSS3 | 0.010 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[ST6GALNAC1]] | B | ST6GALNAC1 activity raises MGST2's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 3.35× lower at baseline in the lines without ST6GALNAC1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4 |
| [[CHN2]] | B | CHN2 activity strengthens MGST2's drug response | lines that do not express CHN2 (15) vs lines expressing it (23) | the lines without CHN2 respond 0.62× as strongly (z diff +2.10); strongest at Panobinostat 5 µM: 0.43x vs 0.22x (z diff +3.9) | 0.019 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15; target measured in part of the lines; artifact flags |
| [[HNMT]] | B | HNMT activity raises MGST2's level | lines that do not express HNMT (17) vs lines expressing it (33) | 2.07× lower at baseline in the lines without HNMT | 0.028 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[IGFL2-AS1]] | B | IGFL2-AS1 activity raises MGST2's level | lines that do not express IGFL2-AS1 (36) vs lines expressing it (14) | 2.61× lower at baseline in the lines without IGFL2-AS1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, CLRN3, LINC01559 |
| [[TFF3]] | B | TFF3 activity raises MGST2's level | lines that do not express TFF3 (38) vs lines expressing it (12) | 2.42× lower at baseline in the lines without TFF3 | 0.040 | ⚠ within organs, on part of the lines; also absent: CEACAM5, MUC17, AGR3 |
| [[IL20RA]] | B | IL20RA activity raises MGST2's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 2.90× lower at baseline in the lines without IL20RA | 0.048 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10 |
| [[CASP10]] | B | CASP10 activity raises MGST2's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.43× lower at baseline in the lines without CASP10 | 0.057 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[THRB]] | B | THRB activity raises MGST2's level | lines that do not express THRB (21) vs lines expressing it (29) | 2.00× lower at baseline in the lines without THRB | 0.059 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRK]] | B | MGST2 activity raises FRK's level | lines that do not express MGST2 (10) vs lines expressing it (40) | 3.65× lower at baseline in the lines without MGST2 | 0.037 | ⚠ within organs, on part of the lines; also absent: LGALS3BP, TUBA4A, TNK1 |
| [[P4HTM]] | B | MGST2 activity raises P4HTM's level | lines that do not express MGST2 (10) vs lines expressing it (40) | 1.67× lower at baseline in the lines without MGST2 | 0.044 | ⚠ within organs, on part of the lines; also absent: LGALS3BP, TUBA4A, TNK1 |
| [[THRB]] | B | MGST2 activity raises THRB's level | lines that do not express MGST2 (10) vs lines expressing it (40) | 3.51× lower at baseline in the lines without MGST2 | 0.050 | ⚠ within organs, on part of the lines; also absent: LGALS3BP, TUBA4A, TNK1 |
| [[MR1]] | B | MGST2 activity raises MR1's level | lines that do not express MGST2 (10) vs lines expressing it (40) | 1.56× lower at baseline in the lines without MGST2 | 0.062 | ⚠ within organs, on part of the lines; also absent: LGALS3BP, TUBA4A, TNK1 |
| cells under [[Methylprednisolone succinate (drug)]] 0.5 µM | B | MGST2 activity lowers the cells' numbers under Methylprednisolone succinate 0.5 µM (makes them more sensitive) | lines that do not express MGST2 (10) vs lines expressing it (38) | the lines without MGST2: 1.39× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: LGALS3BP, TUBA4A, TNK1 |
| [[CASP10]] | B | MGST2 activity raises CASP10's level | lines that do not express MGST2 (10) vs lines expressing it (40) | 4.13× lower at baseline in the lines without MGST2 | 0.089 | ⚠ within organs, on part of the lines; also absent: LGALS3BP, TUBA4A, TNK1 |
| cells under [[Pimitespib (drug)]] 5 µM | B | MGST2 activity lowers the cells' numbers under Pimitespib 5 µM (makes them more sensitive) | lines that do not express MGST2 (10) vs lines expressing it (38) | the lines without MGST2: 1.29× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: LGALS3BP, TUBA4A, TNK1 |
| cells under [[Methylprednisolone succinate (drug)]] 5 µM | B | MGST2 activity lowers the cells' numbers under Methylprednisolone succinate 5 µM (makes them more sensitive) | lines that do not express MGST2 (10) vs lines expressing it (38) | the lines without MGST2: 1.32× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: LGALS3BP, TUBA4A, TNK1 |
| cells under [[Brivudine (drug)]] 5 µM | B | MGST2 activity raises the cells' numbers under Brivudine 5 µM (protects the cells) | lines that do not express MGST2 (10) vs lines expressing it (38) | the lines without MGST2: 0.70× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: LGALS3BP, TUBA4A, TNK1 |
| cells under [[TAK-901 (drug)]] 5 µM | B | MGST2 activity raises the cells' numbers under TAK-901 5 µM (protects the cells) | lines that do not express MGST2 (10) vs lines expressing it (38) | the lines without MGST2: 0.49× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: LGALS3BP, TUBA4A, TNK1 |
| [[LINC00205]] | B | MGST2 activity strengthens LINC00205's drug response | lines that do not express MGST2 (10) vs lines expressing it (36) | the lines without MGST2 respond 0.95× as strongly (z diff -0.44); strongest at Dinaciclib 0.5 µM: 1.00x vs 2.34x (z diff +3.1) | 0.099 | ⚠ within organs, on part of the lines; also absent: LGALS3BP, TUBA4A, TNK1; target measured in part of the lines; both ways; artifact flags |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.535). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.5, 50.3); signed map (65.0, -0.9). **Vector** length 80.4, 18.7% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +0.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.3 | +5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.1 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | -0.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | -0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +1.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +5.3 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -5.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.0 | -5.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -7.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | -22.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -7.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.2 | -5.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.8 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | microsomal glutathione S-transferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.1 — chr4:139,665,768-139,740,745 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGST-II |
| Gene groups (HGNC) | Microsomal glutathione S-transferases; MAPEG superfamily |
| Reactome | 4 pathways, smallest: Aflatoxin activation and detoxification; Glutathione conjugation; Phase II - Conjugation of compounds |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99735](https://www.uniprot.org/uniprotkb/Q99735) (Microsomal glutathione S-transferase 2):

> Catalyzes several different glutathione-dependent reactions. Catalyzes the glutathione-dependent reduction of lipid hydroperoxides, such as 5-HPETE. Has glutathione transferase activity, toward xenobiotic electrophiles, such as 1-chloro-2, 4-dinitrobenzene (CDNB). Also catalyzes the conjugation of leukotriene A4 with reduced glutathione to form leukotriene C4 (LTC4). Involved in oxidative DNA damage induced by ER stress and anticancer agents by activating LTC4 biosynthetic machinery in …

**Summary**, from NCBI Gene [4258](https://www.ncbi.nlm.nih.gov/gene/4258):

> The MAPEG (Membrane Associated Proteins in Eicosanoid and Glutathione metabolism) family consists of six human proteins, several of which are involved in the production of leukotrienes and prostaglandin E, important mediators of inflammation. This gene encodes a protein which catalyzes the conjugation of leukotriene A4 and reduced glutathione to produce leukotriene C4. Alternatively spliced transcript variants encoding different isoforms have been identified in this gene. [provided by RefSeq, …

**Accessions** — [HGNC:7063](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7063) · Entrez [4258](https://www.ncbi.nlm.nih.gov/gene/4258) · UniProt [Q99735](https://www.uniprot.org/uniprotkb/Q99735) · Ensembl [ENSG00000085871](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085871)

## Data

Gene col 1444: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1444); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1444, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1444]; `tensor/DDL_lfc|DDL_z.npy` [1444]; `embed/gene_vectors.npy` [1444]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1444 or target_col == 1444). Every well: [[MGST2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MGST2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
