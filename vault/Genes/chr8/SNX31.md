---
symbol: "SNX31"
type: "gene"
col: 10473
ensembl_id: "ENSG00000174226"
name: "sorting nexin 31"
location: "8q22.3"
module: 37
arm: "+"
pooled_cpm: 5.15
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 8
n_dd_up_clean: 30
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# SNX31

*sorting nexin 31* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 15.6× (z +32.2, q 0e+00, up in 39 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Belumosudil (drug)]] 5 µM: 0.534× (z -5.0, q 3e-04, down in 19 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CASS4]] (+0.81, fdr 7e-06), [[WDR49]] (+0.80, fdr 7e-06), [[TMEM225B]] (+0.80, fdr 7e-06); moves opposite to [[BRD7]] (-0.62, fdr 1e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[CASC20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10473.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **15.6×** | +32.2 | 0e+00 | 39/39 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **10.3×** | +27.3 | 0e+00 | 36/36 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **14.3×** | +22.0 | 0e+00 | 42/44 (SW480, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **7.11×** | +15.6 | 0e+00 | 33/36 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.76×** | +14.5 | 1e-45 | 36/39 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **6.12×** | +14.4 | 4e-45 | 35/40 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.25×** | +12.0 | 3e-31 | 41/47 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.42×** | +10.4 | 3e-23 | 26/46 (HOP62, HS-578T, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.35×** | +10.0 | 9e-22 | 29/37 (COLO 205, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **3.44×** | +9.8 | 5e-21 | 17/30 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.21×** | +9.6 | 3e-20 | 34/45 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.23×** | +9.4 | 2e-19 | 36/46 (HS-578T, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.11×** | +9.4 | 2e-19 | 31/47 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.23×** | +9.3 | 4e-19 | 19/26 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.84×** | +8.6 | 2e-16 | 31/45 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.69×** | +7.9 | 1e-13 | 24/42 (C32, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.58×** | +7.8 | 1e-13 | 25/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **4.62×** | +6.6 | 1e-09 | 25/41 (HEC-1-A, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10473.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.534×** | -5.0 | 3e-04 | 19/42 (C-33 A, LS 180, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.505×** | -4.9 | 3e-04 | 15/46 (MIA PaCa-2, LS 180, …) | all doses, flat | position effect removed |
| [[Berbamine (drug)]] 0.05 µM |  | **0.561×** | -4.1 | 0.008 | 16/46 (LS 180, LOX-IMVI, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 0.5 µM |  | **0.629×** | -3.8 | 0.018 | 12/43 (SHP-77, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -3.5 | 0.048 | 16/47 (SW 1271, HCT15, …) | all doses, flat | position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -3.4 | 0.061 | 5/46 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.665×** | -3.4 | 0.061 | 6/46 (NCI-H1573, HCT15, …) | two highest doses | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.477×** | -3.2 | 0.095 | 10/35 (HT-29, RKO, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 0.684× | -3.1 | 0.11 | 9/47 (SNU-1, RKO, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10473. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 9.97 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 67.6× (z +22.6) | — |
| [[NCI-H460 (line)]] | wt | 3.78 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 30.7× (z +16.7) | — |
| [[HOP62 (line)]] | alt | 7.10 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 23.0× (z +16.0) | — |
| [[C32 (line)]] | wt | 8.71 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 129× (z +20.3) | — |
| [[SW480 (line)]] | alt | 3.28 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +14.4) | — |
| [[HEC-1-A (line)]] | alt | 8.41 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.72× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[LoVo (line)]] | wt | 5.66 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.4× (z +16.6) | — |
| [[A498 (line)]] | wt | 10.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.8× (z +22.9) | — |
| [[PANC-1 (line)]] | alt | 2.53 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.6× (z +16.7) | — |
| [[CFPAC-1 (line)]] | alt | 3.10 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.7× (z +11.1) | — |
| [[COLO 205 (line)]] | alt | 5.63 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 60.1× (z +13.5) | — |
| [[HCT15 (line)]] | alt | 23.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +9.7) | [[Vilanterol (drug)]] 0.5 µM 0.0872× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 49.1× (z +15.9) | — |
| [[LOX-IMVI (line)]] | wt | 10.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.3× (z +15.5) | — |
| [[NCI-H2347 (line)]] | alt | 2.08 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.8× (z +10.0) | — |
| [[RKO (line)]] | wt | 5.87 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.6× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 2.45 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.1× (z +10.3) | — |
| [[SW 900 (line)]] | alt | 3.46 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.6× (z +10.0) | — |
| [[A-172 (line)]] | wt | 5.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.1× (z +10.0) | — |
| [[A549 (line)]] | wt | 2.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.5× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 1.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 70.2× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.64× (z +10.8) | — |
| [[HepG2_C3A (line)]] | wt | 3.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.9× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 2.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.0× (z +10.1) | — |
| [[J82 (line)]] | alt | 3.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 5.51 | 0 | 1 | — | [[Berbamine (drug)]] 0.05 µM 0.0575× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 7.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 3.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.2× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 1.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.3× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 4.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.3× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 6.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.76× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 2.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.5× (z +9.1) | — |
| [[SW48 (line)]] | wt | 14.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +11.7) | — |
| [[A-427 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10473), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASS4]] | +0.81 | +0.85 / +0.73 | both halves | 7e-06 |  |
| [[WDR49]] | +0.80 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[TMEM225B]] | +0.80 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[PIWIL2]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[CFAP53]] | +0.79 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.78 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[DCAF4L1]] | +0.78 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[LINC02646]] | +0.77 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[CCDC62]] | +0.77 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[ADCY10]] | +0.77 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[TMEM269]] | +0.77 | +0.84 / +0.70 | both halves | 7e-06 |  |
| [[KLRD1]] | +0.76 | +0.74 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRD7]] | -0.62 | -0.51 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASC20]] | B | CASC20 activity raises SNX31's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 1.66× lower at baseline in the lines without CASC20 | 0.032 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |
| [[HAND2-AS1]] | B | HAND2-AS1 activity raises SNX31's level | lines that do not express HAND2-AS1 (20) vs lines expressing it (30) | 1.62× lower at baseline in the lines without HAND2-AS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: LINC02269, NPTX1, VAT1L; maybe low, not absent |
| [[ANKRD7]] | B | ANKRD7 activity raises SNX31's level | lines that do not express ANKRD7 (11) vs lines expressing it (39) | 1.78× lower at baseline in the lines without ANKRD7 | 0.047 | ⚠ within organs, on part of the lines; also absent: PCDH15, LINC02398, ABCA12; maybe low, not absent |
| [[LINC01482]] | B | LINC01482 activity raises SNX31's level | lines that do not express LINC01482 (5) vs lines expressing it (45) | 2.05× lower at baseline in the lines without LINC01482 | 0.061 | ⚠ within organs, on part of the lines; also absent: MAP7D2, SLC35F4, ENSG00000226965; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SNX31's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IGSF11]] | B | IGSF11 activity raises SNX31's level | lines that do not express IGSF11 (10) vs lines expressing it (40) | 1.77× lower at baseline in the lines without IGSF11 | 0.077 | ⚠ within organs, on part of the lines; also absent: LINC02398, ANKRD7; maybe low, not absent |
| [[NPR3]] | B | NPR3 activity raises SNX31's level | lines that do not express NPR3 (7) vs lines expressing it (43) | 1.77× lower at baseline in the lines without NPR3 | 0.095 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.888). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.6, -17.3); signed map (11.5, 4.9). **Vector** length 83.1, 18.2% of its response variance represented; |z| ≥ 3 in 1,268 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.1 | +22.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +27.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +9.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +15.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +14.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +10.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.9 | +6.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.1 | +2.7 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -1.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.3 | +8.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -5.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.3 | +9.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.3 | -3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.1 | -4.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +2.1 |

## What is on record

|  |  |
|---|---|
| Name | sorting nexin 31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.3 — chr8:100,572,889-100,663,415 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC39715 |
| Gene groups (HGNC) | Sorting nexins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N9S9](https://www.uniprot.org/uniprotkb/Q8N9S9) (Sorting nexin-31):

> May be involved in protein trafficking.

**Summary**, from NCBI Gene [169166](https://www.ncbi.nlm.nih.gov/gene/169166):

> Predicted to enable phosphatidylinositol binding activity. Predicted to be involved in endocytic recycling and intracellular protein transport. Predicted to be part of protein-containing complex. Predicted to be active in early endosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28605](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28605) · Entrez [169166](https://www.ncbi.nlm.nih.gov/gene/169166) · UniProt [Q8N9S9](https://www.uniprot.org/uniprotkb/Q8N9S9) · Ensembl [ENSG00000174226](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174226)

## Data

Gene col 10473: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10473); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10473, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10473]; `tensor/DDL_lfc|DDL_z.npy` [10473]; `embed/gene_vectors.npy` [10473]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10473 or target_col == 10473). Every well: [[SNX31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNX31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
