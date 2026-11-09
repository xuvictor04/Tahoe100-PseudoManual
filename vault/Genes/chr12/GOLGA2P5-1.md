---
symbol: "GOLGA2P5-1"
type: "gene"
col: 16490
ensembl_id: "ENSG00000290571"
name: ""
location: ""
module: 46
arm: "+"
pooled_cpm: 5.72
n_lines_expressing: 42
n_dd_up: 11
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 8
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# GOLGA2P5-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.76× (z +14.1, q 2e-42, up in 26 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.219× (z -7.8, q 4e-12, down in 24 of 35 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGA2P5]] (+0.87, fdr 7e-06, ⚠ same locus), [[XNDC1N-ZNF705EP-ALG1L9P]] (+0.67, fdr 1e-05), [[SPINT1-AS1]] (+0.64, fdr 2e-05), [[HOTAIR]] (+0.62, fdr 4e-05); moves opposite to [[SH3BGRL3]] (-0.59, fdr 8e-05), [[FLNB]] (-0.54, fdr 2e-04), [[MRPL17]] (-0.52, fdr 7e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 8 go from it, the strongest it → [[COMMD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16490.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.76×** | +14.1 | 2e-42 | 26/31 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.97×** | +10.7 | 3e-24 | 20/21 (LoVo, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +8.3 | 3e-14 | 10/10 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +8.1 | 9e-14 | 11/13 (LS 180, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.34×** | +8.0 | 1e-13 | 19/27 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +5.6 | 3e-06 | 15/29 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.4 | 4e-06 | 16/38 (NCI-H23, SW1417, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +5.1 | 3e-05 | 13/23 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.017 | 10/38 (LoVo, KATO III, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.058 | 3/33 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.38×** | +3.1 | 0.087 | 4/38 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.36× | +3.0 | 0.12 | 7/39 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16490.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.219×** | -7.8 | 4e-12 | 24/35 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.486×** | -7.1 | 4e-10 | 21/39 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.523×** | -6.4 | 4e-08 | 20/37 (PANC-1, LoVo, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.298×** | -6.2 | 7e-08 | 20/30 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.555×** | -5.8 | 8e-07 | 21/38 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.563×** | -5.7 | 1e-06 | 20/31 (PANC-1, A-427, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.583×** | -5.3 | 9e-06 | 18/38 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.604×** | -5.0 | 5e-05 | 17/38 (COLO 205, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.590×** | -4.9 | 6e-05 | 17/33 (CFPAC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.603×** | -4.7 | 1e-04 | 15/35 (HEC-1-A, LS 180, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.719×** | -4.6 | 2e-04 | 16/37 (SW480, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.734×** | -4.3 | 8e-04 | 15/37 (SW480, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.700×** | -3.5 | 0.020 | 9/35 (COLO 205, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.711×** | -3.4 | 0.032 | 16/36 (HT-29, J82, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.717×** | -3.3 | 0.039 | 12/39 (LS 180, HT-29, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.722×** | -3.2 | 0.048 | 14/36 (PANC-1, HT-29, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.736×** | -3.0 | 0.085 | 4/37 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.658×** | -2.9 | 0.093 | 4/38 (LoVo, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.565×** | -2.9 | 0.093 | 10/30 (HT-29, LoVo, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16490. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.79 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.183× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -8.7) |
| [[HT-29 (line)]] | alt | 6.25 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0814× (z -10.5) ⚠ cell-cycle shift, explains ~5% of this change |
| [[A-427 (line)]] | wt | 4.95 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0848× (z -9.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 6.85 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0652× (z -10.9) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 1.63 | 0 | 1 | — | [[Anastrozole (drug)]] 0.5 µM 0.447× (z -9.3) |
| [[SW480 (line)]] | alt | 11.7 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0811× (z -8.7) |
| [[A-172 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.807 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.997 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.802 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.774 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.778 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16490), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 8 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA2P5]] | +0.87 | +0.86 / +0.85 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | +0.67 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[SPINT1-AS1]] | +0.64 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[HOTAIR]] | +0.62 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[OARD1]] | +0.62 | +0.63 / +0.39 | both halves | 6e-05 |  |
| [[ALG1L9P]] | +0.61 | +0.64 / +0.38 | both halves | 7e-05 |  |
| [[XNDC1N]] | +0.59 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[IQCH-AS1]] | +0.58 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[ITGA9-AS1]] | +0.58 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[ERICH2-DT]] | +0.58 | +0.62 / +0.33 | both halves | 1e-04 |  |
| [[EFCAB6]] | +0.57 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[VSIG10]] | +0.55 | +0.56 / +0.23 | both halves | 5e-04 |  |
| [[NEIL1]] | +0.55 | +0.41 / +0.49 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3BGRL3]] | -0.59 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[FLNB]] | -0.54 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[MRPL17]] | -0.52 | -0.52 / -0.20 | both halves | 7e-04 |  |
| [[MRGBP]] | -0.52 | -0.52 / -0.27 | both halves | 3e-04 |  |
| [[SH3PXD2B]] | -0.52 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[CBR1]] | -0.52 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[ACTG1]] | -0.51 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[PUS3]] | -0.51 | -0.33 / -0.26 | both halves | 4e-04 |  |
| [[EXTL3]] | -0.49 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[SBF2]] | -0.48 | -0.52 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[CCDC112]] | -0.48 | -0.21 / -0.31 | both halves | 7e-04 |  |
| [[COMMD2]] | -0.48 | -0.33 / -0.27 | both halves | 3e-04 |  |
| [[ABCC10]] | -0.47 | -0.39 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GOLGA2P5-1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ACTR3C]] | B | ACTR3C activity raises GOLGA2P5-1's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 1.90× lower at baseline in the lines without ACTR3C | 0.031 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[C11orf52]] | B | C11orf52 activity raises GOLGA2P5-1's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 1.91× lower at baseline in the lines without C11orf52 | 0.062 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[GOLGA2P5]] | C | GOLGA2P5 activity raises GOLGA2P5-1's level | lines that do not express GOLGA2P5 (6) vs lines expressing it (44) | 3.13× lower at baseline in the lines without GOLGA2P5 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000257489, GOLGA2P5-1, GRHL1; co-absent with the target; its own permutation p |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COMMD2]] | B | GOLGA2P5-1 activity raises COMMD2's level | lines that do not express GOLGA2P5-1 (8) vs lines expressing it (42) | 1.41× lower at baseline in the lines without GOLGA2P5-1 | 0.022 | ⚠ within organs, on part of the lines; also absent: GOLGA2P5, ENSG00000257489, KCNIP3; maybe low, not absent |
| [[FAM174B]] | B | GOLGA2P5-1 activity raises FAM174B's level | lines that do not express GOLGA2P5-1 (8) vs lines expressing it (42) | 1.87× lower at baseline in the lines without GOLGA2P5-1 | 0.023 | ⚠ within organs, on part of the lines; also absent: GOLGA2P5, ENSG00000257489, KCNIP3; maybe low, not absent |
| [[IQCH-AS1]] | B | GOLGA2P5-1 activity raises IQCH-AS1's level | lines that do not express GOLGA2P5-1 (8) vs lines expressing it (42) | 1.68× lower at baseline in the lines without GOLGA2P5-1 | 0.043 | ⚠ within organs, on part of the lines; also absent: GOLGA2P5, ENSG00000257489, KCNIP3; maybe low, not absent |
| [[RMI2]] | B | GOLGA2P5-1 activity raises RMI2's level | lines that do not express GOLGA2P5-1 (8) vs lines expressing it (42) | 1.61× lower at baseline in the lines without GOLGA2P5-1 | 0.050 | ⚠ within organs, on part of the lines; also absent: GOLGA2P5, ENSG00000257489, KCNIP3; maybe low, not absent |
| [[COMMD4]] | B | GOLGA2P5-1 activity raises COMMD4's level | lines that do not express GOLGA2P5-1 (8) vs lines expressing it (42) | 1.43× lower at baseline in the lines without GOLGA2P5-1 | 0.054 | ⚠ within organs, on part of the lines; also absent: GOLGA2P5, ENSG00000257489, KCNIP3; maybe low, not absent |
| [[BANK1]] | B | GOLGA2P5-1 activity raises BANK1's level | lines that do not express GOLGA2P5-1 (8) vs lines expressing it (42) | 2.18× lower at baseline in the lines without GOLGA2P5-1 | 0.063 | ⚠ within organs, on part of the lines; also absent: GOLGA2P5, ENSG00000257489, KCNIP3; maybe low, not absent |
| [[ACTR3C]] | B | GOLGA2P5-1 activity raises ACTR3C's level | lines that do not express GOLGA2P5-1 (8) vs lines expressing it (42) | 2.68× lower at baseline in the lines without GOLGA2P5-1 | 0.089 | ⚠ within organs, on part of the lines; also absent: GOLGA2P5, ENSG00000257489, KCNIP3; maybe low, not absent |
| [[GOLGA2P5]] | C | GOLGA2P5-1 activity raises GOLGA2P5's level | lines that do not express GOLGA2P5-1 (8) vs lines expressing it (42) | 2.55× lower at baseline in the lines without GOLGA2P5-1 | 0.003 | ⚠ within organs, on part of the lines; also absent: GOLGA2P5, ENSG00000257489, KCNIP3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.527). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (1.7, 28.5); signed map (37.3, -15.9). **Vector** length 62.9, 11.2% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +10.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +14.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +3.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.3 | +1.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.2 | -3.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -0.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.2 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +1.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -2.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.1 | -2.9 |

## What is on record

> [!warning] No registry record
> GOLGA2P5-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16490: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16490); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16490, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16490]; `tensor/DDL_lfc|DDL_z.npy` [16490]; `embed/gene_vectors.npy` [16490]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16490 or target_col == 16490). Every well: [[GOLGA2P5-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLGA2P5-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
