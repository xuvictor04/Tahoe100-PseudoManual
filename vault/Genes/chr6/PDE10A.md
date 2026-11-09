---
symbol: "PDE10A"
type: "gene"
col: 3377
ensembl_id: "ENSG00000112541"
name: "phosphodiesterase 10A"
location: "6q27"
module: 19
arm: "+"
pooled_cpm: 432.39
n_lines_expressing: 26
n_dd_up: 4
n_dd_down: 43
n_dd_up_clean: 4
n_dd_down_clean: 36
in_vector_space: true
direction_upstream: 13
direction_downstream: 12
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# PDE10A

*phosphodiesterase 10A* — 6q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.22× (z +5.4, q 4e-05, up in 7 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.390× (z -18.6, q 0e+00, down in 23 of 24 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE4B]] (+0.63, fdr 1e-05), [[ADARB2]] (+0.61, fdr 1e-05), [[MDGA2]] (+0.59, fdr 1e-05); moves opposite to [[GRAMD2B]] (-0.49, fdr 3e-05), [[OCLN]] (-0.47, fdr 6e-05), [[ARHGEF34P]] (-0.43, fdr 3e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[ARHGEF5]], [[ARHGEF34P]] → it (grade B ⚠); 12 go from it, the strongest it → [[HERC2P3-1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3377.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.4 | 4e-05 | 7/24 (RPMI-7951, BT-474, …) | top dose only |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.26×** | +4.3 | 0.004 | 12/24 (CHP-212, LS 180, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.013 | 1/25 (J82) | top dose only |  |
| [[Arbutin (drug)]] 0.5 µM |  | **1.20×** | +3.7 | 0.035 | 11/24 (C32, A549, …) | inconsistent across doses | position effect removed |
| [[Malotilate (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.13 | 0/24 | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.22 | 6/24 (MIA PaCa-2, C32, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 61 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3377.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.390×** | -18.6 | 0e+00 | 23/24 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.452×** | -15.6 | 0e+00 | 22/24 (HS-578T, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.496×** | -13.8 | 3e-41 | 23/24 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.577×** | -10.8 | 4e-25 | 22/24 (SNU-423, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.593×** | -10.3 | 9e-23 | 18/24 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.718×** | -8.8 | 1e-16 | 18/24 (NCI-H23, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.686×** | -7.0 | 2e-10 | 21/24 (C32, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.708×** | -6.8 | 9e-10 | 16/24 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.709×** | -6.5 | 6e-09 | 19/23 (J82, SHP-77, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.703×** | -6.4 | 9e-09 | 7/24 (MIA PaCa-2, LS 180, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.730×** | -6.2 | 3e-08 | 17/24 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.733×** | -6.1 | 5e-08 | 15/24 (HS-578T, SNU-1, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.735×** | -6.0 | 7e-08 | 20/24 (C32, NCI-H23, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.737×** | -6.0 | 9e-08 | 19/24 (LS 180, NCI-H23, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.739×** | -5.9 | 1e-07 | 11/24 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.741×** | -5.7 | 5e-07 | 12/26 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.598×** | -5.3 | 4e-06 | 16/24 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.770×** | -5.1 | 9e-06 | 18/24 (C32, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3377. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 1,079 | 1 | 24 (10 ⚠) | [[PH-797804 (drug)]] 5 µM 6.50× (z +10.5) | [[Panobinostat (drug)]] 0.5 µM 0.0628× (z -29.6) |
| [[HOP62 (line)]] | alt | 771 | 0 | 21 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.120× (z -18.6) |
| [[MIA PaCa-2 (line)]] | alt | 545 | 0 | 19 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0662× (z -23.0) |
| [[SNU-423 (line)]] | alt | 1,604 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0943× (z -21.2) |
| [[NCI-H23 (line)]] | alt | 502 | 1 (1 ⚠) | 10 (5 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.52× (z +8.6) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.0861× (z -19.4) |
| [[C32 (line)]] | wt | 627 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -16.1) |
| [[J82 (line)]] | alt | 310 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -20.3) |
| [[NCI-H460 (line)]] | wt | 2,260 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.236× (z -10.8) |
| [[PANC-1 (line)]] | alt | 710 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -20.2) |
| [[SHP-77 (line)]] | alt | 3,580 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.380× (z -9.0) |
| [[A549 (line)]] | wt | 1,532 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.109× (z -13.5) |
| [[A-172 (line)]] | wt | 286 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -17.6) |
| [[AN3 CA (line)]] | alt | 589 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -17.2) |
| [[H4 (line)]] | wt | 186 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.328× (z -9.4) |
| [[HT-29 (line)]] | alt | 250 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.189× (z -14.5) |
| [[LS 180 (line)]] | wt | 146 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.271× (z -11.4) |
| [[SNU-1 (line)]] | wt | 166 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 237 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -12.7) |
| [[SW48 (line)]] | wt | 189 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.284× (z -11.2) |
| [[BT-474 (line)]] | alt | 113 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.214× (z -8.8) |
| [[CHP-212 (line)]] | wt | 231 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 264 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.410× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 260 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -9.8) |
| [[A-427 (line)]] | wt | 31.4 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 27.4 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 35.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 41.1 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 34.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 33.6 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 82.3 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 34.7 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 36.2 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 58.9 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 32.2 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 32.0 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 58.6 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 45.0 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 27.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 414 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 525 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.1 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 74.9 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 36.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.0 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 80.0 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 33.0 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 33.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3377), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE4B]] | +0.63 | +0.66 / +0.55 | both halves | 1e-05 | same gene group |
| [[ADARB2]] | +0.61 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[MDGA2]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[PDE3A]] | +0.58 | +0.62 / +0.49 | both halves | 1e-05 | same gene group; pathway: G alpha (s) signalling events; STRING 407 |
| [[FBXL7]] | +0.55 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[STK32B]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[SGIP1]] | +0.54 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[TMEM178B]] | +0.54 | +0.40 / +0.53 | both halves | 5e-05 | **novel candidate** |
| [[SCUBE1]] | +0.54 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[TCF4]] | +0.54 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[TRIM9]] | +0.52 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[AFF3]] | +0.52 | +0.44 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRAMD2B]] | -0.49 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[OCLN]] | -0.47 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[ARHGEF34P]] | -0.43 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[ARHGEF5]] | -0.42 | -0.48 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 5, C 8. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF5]], [[ARHGEF34P]] | B | ARHGEF5, ARHGEF34P activity lowers PDE10A's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 3.18× higher at baseline in the lines without ARHGEF5, ARHGEF34P | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[TTC28]] | B | TTC28 activity raises PDE10A's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 3.48× lower at baseline in the lines without TTC28 | 0.074 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[RASSF8]] | B | RASSF8 activity raises PDE10A's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 3.87× lower at baseline in the lines without RASSF8 | 0.090 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1 |
| [[HERC2P3-1]] | B | HERC2P3-1 activity raises PDE10A's level | lines that do not express HERC2P3-1 (23) vs lines expressing it (27) | 2.87× lower at baseline in the lines without HERC2P3-1 | 0.096 | ⚠ within organs, on part of the lines; also absent: ZNF880, ENSG00000258732, ZNF829 |
| [[GPRIN3]] | B | GPRIN3 activity raises PDE10A's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 2.06× lower at baseline in the lines without GPRIN3 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031 |
| [[SPOCK1]] | C | SPOCK1 activity raises PDE10A's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 4.11× lower at baseline in the lines without SPOCK1 | 0.020 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |
| [[ADARB2]] | C | ADARB2 activity raises PDE10A's level | lines that do not express ADARB2 (39) vs lines expressing it (11) | 3.97× lower at baseline in the lines without ADARB2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, GSG1L2; co-absent with the target |
| [[UBE2QL1]] | C | UBE2QL1 activity raises PDE10A's level | lines that do not express UBE2QL1 (32) vs lines expressing it (18) | 4.64× lower at baseline in the lines without UBE2QL1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ZMAT4, NCAM1, FENDRR; co-absent with the target |
| [[NCKAP5-AS2]] | C | NCKAP5-AS2 activity raises PDE10A's level | lines that do not express NCKAP5-AS2 (31) vs lines expressing it (19) | 3.76× lower at baseline in the lines without NCKAP5-AS2 | 0.048 | ⚠ within organs, on part of the lines; also absent: MEG3, PDGFRB, UNC5D; co-absent with the target |
| [[MARCHF1]] | C | MARCHF1 activity raises PDE10A's level | lines that do not express MARCHF1 (33) vs lines expressing it (17) | 4.79× lower at baseline in the lines without MARCHF1 | 0.050 | ⚠ within organs, on part of the lines; also absent: UNC5D, DSCAM, LINC01266; maybe low, not absent; co-absent with the target |
| [[RARB]] | C | RARB activity raises PDE10A's level | lines that do not express RARB (28) vs lines expressing it (22) | 3.76× lower at baseline in the lines without RARB | 0.057 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, NEFM, PAPPA; co-absent with the target |
| [[TRPM8]] | C | TRPM8 activity raises PDE10A's level | lines that do not express TRPM8 (28) vs lines expressing it (22) | 2.81× lower at baseline in the lines without TRPM8 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC01320, LINC02335; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 7, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HERC2P3-1]] | B | PDE10A activity raises HERC2P3-1's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 2.12× lower at baseline in the lines without PDE10A | 0.044 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90 |
| [[SCUBE1]] | B | PDE10A activity raises SCUBE1's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 2.19× lower at baseline in the lines without PDE10A | 0.056 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90 |
| [[SNAP25]] | B | PDE10A activity raises SNAP25's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 2.99× lower at baseline in the lines without PDE10A | 0.060 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90 |
| [[STK32B]] | B | PDE10A activity raises STK32B's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 2.53× lower at baseline in the lines without PDE10A | 0.063 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90 |
| [[TRIM9]] | B | PDE10A activity raises TRIM9's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 2.54× lower at baseline in the lines without PDE10A | 0.068 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90 |
| [[GPRIN3]] | B | PDE10A activity raises GPRIN3's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 1.96× lower at baseline in the lines without PDE10A | 0.079 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90 |
| [[PYGL]] | B | PDE10A activity raises PYGL's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 1.72× lower at baseline in the lines without PDE10A | 0.089 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90 |
| [[TRPM8]] | C | PDE10A activity raises TRPM8's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 1.92× lower at baseline in the lines without PDE10A | 0.024 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90; co-absent with the target |
| [[UBE2QL1]] | C | PDE10A activity raises UBE2QL1's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 2.97× lower at baseline in the lines without PDE10A | 0.029 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90; co-absent with the target |
| [[SPOCK1]] | C | PDE10A activity raises SPOCK1's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 3.18× lower at baseline in the lines without PDE10A | 0.034 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90; co-absent with the target |
| [[ADARB2]] | C | PDE10A activity raises ADARB2's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 2.19× lower at baseline in the lines without PDE10A | 0.044 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90; co-absent with the target |
| [[MARCHF1]] | C | PDE10A activity raises MARCHF1's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 2.85× lower at baseline in the lines without PDE10A | 0.067 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.544). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.9, 30.6); signed map (37.4, 43.1). **Vector** length 95.9, 27.2% of its response variance represented; |z| ≥ 3 in 1,070 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +8.2 | -0.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.7 | +1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change | +7.4 | -3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.9 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | -3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +0.1 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.7 | -6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -3.7 | -4.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.3 | -4.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.2 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.2 | -2.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.7 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 10A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q27 — chr6:165,327,287-165,988,117 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phosphodiesterases |
| Reactome | 7 pathways, smallest: cGMP effects; Nitric oxide stimulates guanylate cyclase; Platelet homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y233](https://www.uniprot.org/uniprotkb/Q9Y233) (cAMP and cAMP-inhibited cGMP 3',5'-cyclic phosphodiesterase 10A):

> Plays a role in signal transduction by regulating the intracellular concentration of cyclic nucleotides. Can hydrolyze both cAMP and cGMP, but has higher affinity for cAMP and is more efficient with cAMP as substrate. May play a critical role in regulating cAMP and cGMP levels in the striatum, a region of the brain that contributes to the control of movement and cognition.

**Summary**, from NCBI Gene [10846](https://www.ncbi.nlm.nih.gov/gene/10846):

> The protein encoded by this gene belongs to the cyclic nucleotide phosphodiesterase family. It plays a role in signal transduction by regulating the intracellular concentration of cyclic nucleotides. This protein can hydrolyze both cAMP and cGMP to the corresponding nucleoside 5' monophosphate, but has higher affinity for cAMP, and is more efficient with cAMP as substrate. Alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:8772](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8772) · Entrez [10846](https://www.ncbi.nlm.nih.gov/gene/10846) · UniProt [Q9Y233](https://www.uniprot.org/uniprotkb/Q9Y233) · Ensembl [ENSG00000112541](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112541)

## Data

Gene col 3377: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3377); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3377, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3377]; `tensor/DDL_lfc|DDL_z.npy` [3377]; `embed/gene_vectors.npy` [3377]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3377 or target_col == 3377). Every well: [[PDE10A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE10A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
