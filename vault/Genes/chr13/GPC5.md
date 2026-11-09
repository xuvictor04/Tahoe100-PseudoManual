---
symbol: "GPC5"
type: "gene"
col: 11029
ensembl_id: "ENSG00000179399"
name: "glypican 5"
location: "13q31.3"
module: 37
arm: "+"
pooled_cpm: 32.59
n_lines_expressing: 42
n_dd_up: 34
n_dd_down: 14
n_dd_up_clean: 29
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# GPC5

*glypican 5* — 13q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.68× (z +20.5, q 0e+00, up in 33 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Pyridoxine (hydrochloride) (drug)]] 5 µM: 0.642× (z -5.3, q 7e-05, down in 28 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX31]] (+0.69, fdr 7e-06), [[PIWIL2]] (+0.63, fdr 7e-06), [[ZNNT1]] (+0.62, fdr 1e-05); moves opposite to [[USP54]] (-0.51, fdr 6e-05), [[LCLAT1]] (-0.51, fdr 3e-05), [[ELP6]] (-0.50, fdr 4e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[FAM184B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11029.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.68×** | +20.5 | 0e+00 | 33/37 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **10.7×** | +19.9 | 0e+00 | 38/39 (NCI-H2347, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.96×** | +16.3 | 0e+00 | 32/39 (NCI-H2030, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **6.31×** | +15.5 | 0e+00 | 33/40 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.32×** | +14.2 | 1e-43 | 37/40 (C32, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.41×** | +12.4 | 1e-33 | 30/40 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.35×** | +10.1 | 3e-22 | 29/39 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.44×** | +9.9 | 2e-21 | 33/41 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.33×** | +9.7 | 2e-20 | 31/39 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.28×** | +9.2 | 2e-18 | 23/32 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.95×** | +9.1 | 7e-18 | 29/40 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.80×** | +8.5 | 9e-16 | 29/36 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.59×** | +7.9 | 2e-13 | 29/39 (C32, J82, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.95×** | +7.8 | 2e-13 | 26/40 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.33×** | +7.1 | 5e-11 | 27/40 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **4.03×** | +6.1 | 3e-08 | 28/39 (J82, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11029.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.642×** | -5.3 | 7e-05 | 28/40 (NCI-H1573, PANC-1, …) | all doses, flat | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.551×** | -5.0 | 1e-04 | 23/40 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.553×** | -5.0 | 1e-04 | 19/40 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.573×** | -4.7 | 4e-04 | 26/40 (NCI-H1573, LoVo, …) | all doses, flat | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **0.615×** | -4.1 | 0.005 | 17/41 (A498, PANC-1, …) | all doses, flat | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.621×** | -4.0 | 0.005 | 23/39 (SW48, CHP-212, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.645×** | -3.7 | 0.017 | 20/40 (HOP62, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.652×** | -3.6 | 0.021 | 16/40 (NCI-H1573, AN3 CA, …) | inconsistent across doses |  |
| [[Furosemide (drug)]] 5 µM |  | **0.747×** | -3.5 | 0.030 | 16/40 (COLO 205, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.654×** | -3.5 | 0.031 | 15/36 (SHP-77, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Adenine (drug)]] 5 µM |  | **0.754×** | -3.4 | 0.037 | 7/40 (COLO 205, NCI-H1573, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.675×** | -3.3 | 0.040 | 15/40 (SW48, BT-474, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.676×** | -3.3 | 0.040 | 15/41 (hTERT-HPNE, LoVo, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.672×** | -3.2 | 0.049 | 13/40 (SW48, PANC-1, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11029. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.9 | 9 | 0 | [[Tucidinostat (drug)]] 5 µM 8.39× (z +15.5) | — |
| [[J82 (line)]] | alt | 42.7 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 10.2× (z +15.4) | — |
| [[NCI-H23 (line)]] | alt | 29.9 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 23.0× (z +13.5) | — |
| [[C32 (line)]] | wt | 20.0 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 26.4× (z +18.0) | — |
| [[CFPAC-1 (line)]] | alt | 12.5 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.11× (z +13.8) | — |
| [[NCI-H2030 (line)]] | alt | 14.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.5× (z +16.3) | — |
| [[SW 900 (line)]] | alt | 45.5 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 9.75× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 54.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +12.1) | — |
| [[NCI-H2347 (line)]] | alt | 9.28 | 5 | 0 | [[Auranofin (drug)]] 5 µM 36.8× (z +15.7) | — |
| [[NCI-H460 (line)]] | wt | 31.9 | 5 | 0 | [[Auranofin (drug)]] 5 µM 30.1× (z +14.1) | — |
| [[SNU-423 (line)]] | alt | 9.92 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +13.5) | — |
| [[A-172 (line)]] | wt | 21.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 14.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.2× (z +12.2) | — |
| [[HT-29 (line)]] | alt | 9.24 | 3 | 0 | [[Auranofin (drug)]] 5 µM 21.0× (z +10.6) | — |
| [[LoVo (line)]] | wt | 17.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +12.0) | — |
| [[NCI-H1792 (line)]] | alt | 11.6 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 16.4× (z +9.4) | — |
| [[A-427 (line)]] | wt | 10.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 11.4× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 11.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 40.4× (z +18.1) | — |
| [[HOP62 (line)]] | alt | 104 | 2 | 0 | [[Auranofin (drug)]] 5 µM 13.6× (z +13.4) | — |
| [[SHP-77 (line)]] | alt | 261 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -9.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 16.8 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 26.7× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0649× (z -8.6) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 285 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0513× (z -9.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 28.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 38.3× (z +12.4) | — |
| [[HCT15 (line)]] | alt | 43.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.7× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 21.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.3× (z +13.5) | — |
| [[hTERT-HPNE (line)]] | wt | 16.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 17.1× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 10.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.42× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 71.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.5× (z +12.8) | — |
| [[PANC-1 (line)]] | alt | 23.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 41.3× (z +9.5) | — |
| [[SW48 (line)]] | wt | 133 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0992× (z -8.5) ⚠ toxic |
| [[A498 (line)]] | wt | 68.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.05 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 93.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.13 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 7.03 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.98 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.02 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.38 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.64 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11029), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX31]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[PIWIL2]] | +0.63 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[ZNNT1]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[LINC02646]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[CORIN]] | +0.59 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[CFAP53]] | +0.58 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[UPP2]] | +0.58 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[H2AZ1-DT]] | +0.57 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[TMEM269]] | +0.57 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[LVRN]] | +0.56 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[CCDC62]] | +0.56 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[WDR49]] | +0.56 | +0.45 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP54]] | -0.51 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[LCLAT1]] | -0.51 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ELP6]] | -0.50 | -0.43 / -0.47 | both halves | 4e-05 |  |
| [[SHMT1]] | -0.49 | -0.41 / -0.33 | both halves | 1e-04 | same gene group; pathway: Metabolism of vitamins and cofactors |
| [[POLD3]] | -0.48 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[SNAP47]] | -0.48 | -0.42 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GPC5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01579]] | B | LINC01579 activity raises GPC5's level | lines that do not express LINC01579 (13) vs lines expressing it (37) | 2.33× lower at baseline in the lines without LINC01579 | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, CNTNAP2, CACNA1C; maybe low, not absent |
| [[CASC20]] | B | CASC20 activity raises GPC5's level | lines that do not express CASC20 (20) vs lines expressing it (30) | 2.29× lower at baseline in the lines without CASC20 | 0.058 | ⚠ within organs, on part of the lines; also absent: PPFIA2, IL19, ENPP2; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM184B]] | B | GPC5 activity raises FAM184B's level | lines that do not express GPC5 (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without GPC5 | 0.036 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MGAM]] | B | GPC5 activity raises MGAM's level | lines that do not express GPC5 (8) vs lines expressing it (42) | 1.84× lower at baseline in the lines without GPC5 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC02936]] | B | GPC5 activity raises LINC02936's level | lines that do not express GPC5 (8) vs lines expressing it (42) | 1.68× lower at baseline in the lines without GPC5 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.2, -16.7); signed map (12.0, 4.4). **Vector** length 94.4, 21.7% of its response variance represented; |z| ≥ 3 in 1,198 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.7 | +19.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +9.3 | +14.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +20.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.7 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.4 | +9.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.6 | +1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.0 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +3.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.3 | -4.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.8 | -4.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -2.7 | -4.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.6 | -5.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.4 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | glypican 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q31.3 — chr13:91,398,621-92,873,682 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Glypicans; MicroRNA protein coding host genes |
| Reactome | 37 pathways, smallest: Release of Hh-Np from the secreting cell; Defective EXT1 causes exostoses 1, TRPS2 and CHDS; Defective EXT2 causes exostoses 2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P78333](https://www.uniprot.org/uniprotkb/P78333) (Glypican-5):

> Cell surface proteoglycan that bears heparan sulfate.

**Summary**, from NCBI Gene [2262](https://www.ncbi.nlm.nih.gov/gene/2262):

> Cell surface heparan sulfate proteoglycans are composed of a membrane-associated protein core substituted with a variable number of heparan sulfate chains. Members of the glypican-related integral membrane proteoglycan family (GRIPS) contain a core protein anchored to the cytoplasmic membrane via a glycosyl phosphatidylinositol linkage. These proteins may play a role in the control of cell division and growth regulation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4453](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4453) · Entrez [2262](https://www.ncbi.nlm.nih.gov/gene/2262) · UniProt [P78333](https://www.uniprot.org/uniprotkb/P78333) · Ensembl [ENSG00000179399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179399)

## Data

Gene col 11029: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11029); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11029, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11029]; `tensor/DDL_lfc|DDL_z.npy` [11029]; `embed/gene_vectors.npy` [11029]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11029 or target_col == 11029). Every well: [[GPC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
