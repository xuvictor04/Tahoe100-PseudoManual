---
symbol: "CYP2U1"
type: "gene"
col: 7862
ensembl_id: "ENSG00000155016"
name: "cytochrome P450 family 2 subfamily U member 1"
location: "4q25"
module: 28
arm: "+"
pooled_cpm: 3.19
n_lines_expressing: 46
n_dd_up: 35
n_dd_down: 12
n_dd_up_clean: 30
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 7
direction_downstream: 5
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# CYP2U1

*cytochrome P450 family 2 subfamily U member 1* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.40× (z +16.6, q 0e+00, up in 30 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.464× (z -7.4, q 9e-11, down in 22 of 42 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPLD1]] (+0.60, fdr 7e-06), [[TAB2]] (+0.58, fdr 3e-05), [[BDH2]] (+0.58, fdr 1e-05); moves opposite to [[FBH1]] (-0.61, fdr 1e-05), [[UBE2M]] (-0.59, fdr 1e-05), [[ZCCHC17]] (-0.59, fdr 5e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SYNM]] → it (grade B ⚠); 5 go from it, the strongest it → [[CFL2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7862.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.40×** | +16.6 | 0e+00 | 30/34 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.39×** | +11.8 | 1e-29 | 35/42 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.39×** | +11.7 | 3e-29 | 36/42 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.15×** | +11.0 | 6e-26 | 21/32 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.01×** | +10.6 | 5e-24 | 34/42 (PANC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.98×** | +9.7 | 4e-20 | 5/8 (J82, A498, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.58×** | +9.1 | 1e-17 | 16/18 (J82, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.41×** | +8.4 | 3e-15 | 28/42 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.38×** | +8.3 | 6e-15 | 30/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.37×** | +8.3 | 7e-15 | 23/38 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.44×** | +8.2 | 1e-14 | 3/6 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.79×** | +7.9 | 2e-13 | 18/42 (J82, C32, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +6.6 | 1e-09 | 11/17 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.90×** | +6.1 | 4e-08 | 18/43 (J82, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +5.4 | 3e-06 | 14/38 (HOP62, SNU-423, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.78×** | +5.1 | 1e-05 | 11/40 (PANC-1, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +5.1 | 1e-05 | 9/32 (A-172, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.56×** | +4.3 | 6e-04 | 10/41 (J82, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +4.3 | 6e-04 | 9/32 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7862.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.464×** | -7.4 | 9e-11 | 22/42 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.546×** | -5.8 | 2e-06 | 19/42 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.552×** | -5.7 | 2e-06 | 18/39 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.570×** | -5.4 | 1e-05 | 21/43 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.598×** | -4.9 | 9e-05 | 11/28 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.587×** | -4.8 | 1e-04 | 15/39 (SW1417, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.646×** | -4.2 | 0.002 | 11/42 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.654×** | -4.1 | 0.003 | 16/42 (PANC-1, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.666×** | -3.9 | 0.006 | 18/42 (PANC-1, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.714×** | -3.2 | 0.069 | 10/40 (SW 900, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.532×** | -3.2 | 0.078 | 8/38 (A-172, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.637×** | -3.1 | 0.094 | 2/42 (MIA PaCa-2, SW1417) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7862. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 2.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 1.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +8.6) | — |
| [[LoVo (line)]] | wt | 3.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 2.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.87× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 1.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 2.67 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.119× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 8.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 6.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +11.8) | — |
| [[A-172 (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.560 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.941 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7862), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPLD1]] | +0.60 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[TAB2]] | +0.58 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[BDH2]] | +0.58 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[VEZF1]] | +0.57 | +0.66 / +0.34 | both halves | 1e-04 |  |
| [[CLCN4]] | +0.55 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[KLF11]] | +0.55 | +0.51 / +0.36 | both halves | 9e-05 |  |
| [[STK33]] | +0.54 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[ZNF776]] | +0.54 | +0.65 / +0.37 | both halves | 8e-05 |  |
| [[TSPAN2]] | +0.53 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[ZNF608]] | +0.53 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[KATNAL2]] | +0.53 | +0.69 / +0.46 | both halves | 2e-05 |  |
| [[ZFHX2]] | +0.53 | +0.70 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBH1]] | -0.61 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[UBE2M]] | -0.59 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[ZCCHC17]] | -0.59 | -0.69 / -0.39 | both halves | 5e-05 |  |
| [[RABEP2]] | -0.57 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[SNHG30]] | -0.56 | -0.70 / -0.26 | both halves | 4e-04 |  |
| [[VPS53]] | -0.55 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[TMEM11-DT]] | -0.55 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[WDR20]] | -0.55 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[SS18L1]] | -0.54 | -0.74 / -0.20 | both halves | 7e-04 |  |
| [[TUSC2]] | -0.54 | -0.59 / -0.39 | both halves | 6e-05 |  |
| [[PITPNA]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[CERS5]] | -0.53 | -0.65 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYNM]] | B | SYNM activity raises CYP2U1's level | lines that do not express SYNM (14) vs lines expressing it (36) | 1.71× lower at baseline in the lines without SYNM | 0.015 | ⚠ within organs, on part of the lines; also absent: AKR1B1, GAMT, FHL1; maybe low, not absent |
| [[KATNAL2]] | B | KATNAL2 activity raises CYP2U1's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.92× lower at baseline in the lines without KATNAL2 | 0.034 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[NPTXR]] | B | NPTXR activity raises CYP2U1's level | lines that do not express NPTXR (11) vs lines expressing it (39) | 1.51× lower at baseline in the lines without NPTXR | 0.040 | ⚠ within organs, on part of the lines; also absent: WNT9A, RAB6B, MAPK8IP2; maybe low, not absent |
| [[FAM171B]] | B | FAM171B activity raises CYP2U1's level | lines that do not express FAM171B (7) vs lines expressing it (43) | 1.97× lower at baseline in the lines without FAM171B | 0.044 | ⚠ within organs, on part of the lines; also absent: NXPE3, GXYLT2, TMOD2; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises CYP2U1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[APBB1]] | B | APBB1 activity raises CYP2U1's level | lines that do not express APBB1 (11) vs lines expressing it (39) | 1.68× lower at baseline in the lines without APBB1 | 0.096 | ⚠ within organs, on part of the lines; also absent: C14orf132, WNT9A, TTC7B; maybe low, not absent |
| [[CFL2]] | C | CFL2 activity raises CYP2U1's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 2.43× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFL2]] | C | CYP2U1 activity raises CFL2's level | lines that do not express CYP2U1 (4) vs lines expressing it (46) | 3.33× lower at baseline in the lines without CYP2U1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent; its own permutation p |
| [[C12orf29]] | C | CYP2U1 activity raises C12orf29's level | lines that do not express CYP2U1 (4) vs lines expressing it (46) | 1.66× lower at baseline in the lines without CYP2U1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent; its own permutation p |
| [[AIG1]] | C | CYP2U1 activity raises AIG1's level | lines that do not express CYP2U1 (4) vs lines expressing it (46) | 1.57× lower at baseline in the lines without CYP2U1 | 0.085 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CCDC102A, SPDL1, ASIC1; maybe low, not absent |
| cells under [[Doxycycline (monohydrate) (drug)]] 5 µM | C | CYP2U1's natural level raises the cells' numbers under Doxycycline (monohydrate) 5 µM (protects the cells) | CYP2U1's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.71 | 0.285 over the table, 0.038 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | CYP2U1's natural level raises the cells' numbers under Bendamustine 0.5 µM (protects the cells) | CYP2U1's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.61 | 0.491 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.408). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.6, -1.5); signed map (9.7, -25.0). **Vector** length 55.1, 7.62% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +16.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +11.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +8.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +6.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +3.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.3 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.4 | -4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.2 | -4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -3.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | +3.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.2 | -2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 2 subfamily U member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:107,931,549-107,953,461 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPG49; previously SPG56 |
| Gene groups (HGNC) | Cytochrome P450 family 2 |
| Reactome | 9 pathways, smallest: Miscellaneous substrates; Metabolic disorders of biological oxidation enzymes; Cytochrome P450 - arranged by substrate type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z449](https://www.uniprot.org/uniprotkb/Q7Z449) (Cytochrome P450 2U1):

> A cytochrome P450 monooxygenase involved in the metabolism of arachidonic acid and its conjugates. Mechanistically, uses molecular oxygen inserting one oxygen atom into a substrate, and reducing the second into a water molecule, with two electrons provided by NADPH via cytochrome P450 reductase (CPR; NADPH-ferrihemoprotein reductase). Acts as an omega and omega-1 hydroxylase for arachidonic acid and possibly for other long chain fatty acids. May modulate the arachidonic acid signaling pathway …

**Summary**, from NCBI Gene [113612](https://www.ncbi.nlm.nih.gov/gene/113612):

> This gene encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. This enzyme is a hydroxylase that metabolizes arachidonic acid, docosahexaenoic acid, and other long chain fatty acids. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20582](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20582) · Entrez [113612](https://www.ncbi.nlm.nih.gov/gene/113612) · UniProt [Q7Z449](https://www.uniprot.org/uniprotkb/Q7Z449) · Ensembl [ENSG00000155016](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155016)

## Data

Gene col 7862: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7862); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7862, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7862]; `tensor/DDL_lfc|DDL_z.npy` [7862]; `embed/gene_vectors.npy` [7862]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7862 or target_col == 7862). Every well: [[CYP2U1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP2U1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
