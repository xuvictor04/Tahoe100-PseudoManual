---
symbol: "ANAPC1P4"
type: "gene"
col: 13946
ensembl_id: "ENSG00000234231"
name: "ANAPC1 pseudogene 4"
location: "2p11.2"
module: 151
arm: "+"
pooled_cpm: 3.66
n_lines_expressing: 46
n_dd_up: 21
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# ANAPC1P4

*ANAPC1 pseudogene 4* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.93× (z +14.1, q 2e-42, up in 23 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.305× (z -11.0, q 1e-25, down in 30 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR4435-2HG]] (+0.88, fdr 7e-06), [[CYTOR]] (+0.76, fdr 7e-06), [[BACH1]] (+0.65, fdr 7e-06); moves opposite to [[SEC61A2]] (-0.56, fdr 2e-05), [[SRP54-AS1]] (-0.56, fdr 2e-05), [[SESN1]] (-0.55, fdr 2e-05).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[APCDD1L-DT]] → it (grade B ⚠); 7 go from it, the strongest it → [[RPTOR]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13946.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.93×** | +14.1 | 2e-42 | 23/31 (SW48, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.31×** | +11.1 | 4e-26 | 28/36 (A-172, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.71×** | +9.2 | 5e-18 | 17/27 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.39×** | +7.8 | 1e-12 | 3/7 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.47×** | +7.3 | 4e-11 | 22/34 (PANC-1, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.66×** | +6.3 | 3e-08 | 14/26 (A-172, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +5.6 | 2e-06 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.87×** | +5.6 | 2e-06 | 19/37 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +4.7 | 1e-04 | 5/21 (NCI-H1573, A-172, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.61×** | +4.2 | 0.002 | 11/38 (HS-578T, RPMI-7951, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +4.0 | 0.003 | 16/41 (C32, SW48, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +3.8 | 0.007 | 11/35 (A-172, HS-578T, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.50×** | +3.7 | 0.009 | 5/41 (C32, SNU-423, …) | two highest doses | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.48×** | +3.6 | 0.014 | 11/38 (NCI-H2030, SNU-423, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +3.5 | 0.019 | 1/5 (PANC-1) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.034 | 11/37 (SNU-1, A498, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.038 | 9/40 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.044 | 0/42 | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.39×** | +2.9 | 0.097 | 5/37 (NCI-H1573, HS-578T, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13946.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.305×** | -11.0 | 1e-25 | 30/41 (SW480, J82, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.450×** | -10.5 | 2e-23 | 23/30 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.451×** | -7.1 | 2e-10 | 16/16 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.663×** | -3.8 | 0.017 | 13/39 (hTERT-HPNE, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.689×** | -3.5 | 0.056 | 9/41 (KATO III, SNU-1, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.693×** | -3.4 | 0.058 | 12/38 (A-172, PANC-1, …) | two highest doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.697×** | -3.4 | 0.059 | 13/37 (SW1417, HS-578T, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.707×** | -3.3 | 0.071 | 8/43 (SW480, CHP-212, …) | rises with dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Irinotecan (drug)]] 5 µM |  | 0.526× | -3.1 | 0.11 | 3/39 (RPMI-7951, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | 0.712× | -3.1 | 0.12 | 4/40 (C32, H4, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13946. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.68 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0661× (z -15.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 4.34 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -11.2) |
| [[HOP62 (line)]] | alt | 4.41 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0722× (z -9.4) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -10.8) |
| [[KATO III (line)]] | alt | 3.85 | 0 | 1 | — | [[Cabozantinib (S-malate) (drug)]] 0.05 µM 0.0544× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 1.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +8.5) | — |
| [[SW48 (line)]] | wt | 2.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.2× (z +9.2) | — |
| [[A-172 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.864 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.842 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.598 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.915 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13946), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR4435-2HG]] | +0.88 | +0.83 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[CYTOR]] | +0.76 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[BACH1]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[TTN-AS1]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[CFAP299]] | +0.62 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[EGFR]] | +0.59 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[TRIO]] | +0.58 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[PHEX]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ETS1]] | +0.57 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[BICD1]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[LINC02516]] | +0.56 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[NF2]] | +0.55 | +0.59 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC61A2]] | -0.56 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[SRP54-AS1]] | -0.56 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[SESN1]] | -0.55 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[CNNM2]] | -0.55 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[CDC42SE2]] | -0.53 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[TBC1D22A-DT]] | -0.53 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[GAB1]] | -0.52 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[MAPKAPK5-AS1]] | -0.52 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[POMZP3]] | -0.52 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[TAF5]] | -0.52 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[TMEM50B]] | -0.52 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[KCTD7]] | -0.51 | -0.51 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APCDD1L-DT]] | B | APCDD1L-DT activity raises ANAPC1P4's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 1.52× lower at baseline in the lines without APCDD1L-DT | 0.040 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[LTBP2]] | B | LTBP2 activity raises ANAPC1P4's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 1.62× lower at baseline in the lines without LTBP2 | 0.052 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPTOR]] | C | ANAPC1P4 activity raises RPTOR's level | lines that do not express ANAPC1P4 (4) vs lines expressing it (46) | 2.27× lower at baseline in the lines without ANAPC1P4 | 0.007 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP19, MIR4435-2HG, MSX1; maybe low, not absent |
| [[RANBP6]] | C | ANAPC1P4 activity raises RANBP6's level | lines that do not express ANAPC1P4 (4) vs lines expressing it (46) | 1.88× lower at baseline in the lines without ANAPC1P4 | 0.034 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP19, MIR4435-2HG, MSX1; maybe low, not absent |
| [[ZKSCAN2]] | C | ANAPC1P4 activity raises ZKSCAN2's level | lines that do not express ANAPC1P4 (4) vs lines expressing it (46) | 1.78× lower at baseline in the lines without ANAPC1P4 | 0.074 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP19, MIR4435-2HG, MSX1; maybe low, not absent |
| [[ATXN3]] | C | ANAPC1P4 activity raises ATXN3's level | lines that do not express ANAPC1P4 (4) vs lines expressing it (46) | 1.32× lower at baseline in the lines without ANAPC1P4 | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP19, MIR4435-2HG, MSX1; maybe low, not absent |
| [[SLC35D1]] | C | ANAPC1P4 activity raises SLC35D1's level | lines that do not express ANAPC1P4 (4) vs lines expressing it (46) | 1.91× lower at baseline in the lines without ANAPC1P4 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP19, MIR4435-2HG, MSX1; maybe low, not absent |
| [[CDK6]] | C | ANAPC1P4 activity raises CDK6's level | lines that do not express ANAPC1P4 (4) vs lines expressing it (46) | 2.13× lower at baseline in the lines without ANAPC1P4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP19, MIR4435-2HG, MSX1; maybe low, not absent |
| [[PCNX2]] | C | ANAPC1P4 activity raises PCNX2's level | lines that do not express ANAPC1P4 (4) vs lines expressing it (46) | 2.34× lower at baseline in the lines without ANAPC1P4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP19, MIR4435-2HG, MSX1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.6, 10.0); signed map (11.5, 40.9). **Vector** length 72.3, 12.6% of its response variance represented; |z| ≥ 3 in 1,119 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.0 | +11.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +14.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +5.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +6.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.2 | -7.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.0 | -11.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.1 | -10.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.5 | -3.3 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.5 | -3.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ANAPC1 pseudogene 4 |
| Locus type | pseudogene |
| Location | 2p11.2 — chr2:87,700,984-87,738,105 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54710](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54710) · Entrez [730268](https://www.ncbi.nlm.nih.gov/gene/730268) · Ensembl [ENSG00000234231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234231)

## Data

Gene col 13946: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13946); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13946, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13946]; `tensor/DDL_lfc|DDL_z.npy` [13946]; `embed/gene_vectors.npy` [13946]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13946 or target_col == 13946). Every well: [[ANAPC1P4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANAPC1P4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
