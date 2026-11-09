---
symbol: "ALDH1L2"
type: "gene"
col: 5799
ensembl_id: "ENSG00000136010"
name: "aldehyde dehydrogenase 1 family member L2"
location: "12q23.3"
module: 63
arm: "+"
pooled_cpm: 15.5
n_lines_expressing: 27
n_dd_up: 32
n_dd_down: 13
n_dd_up_clean: 26
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# ALDH1L2

*aldehyde dehydrogenase 1 family member L2* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.55× (z +24.1, q 0e+00, up in 12 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.591× (z -7.1, q 6e-10, down in 17 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHGDH]] (+0.71, fdr 7e-06), [[PCK2]] (+0.71, fdr 7e-06), [[SARS1]] (+0.71, fdr 7e-06); moves opposite to [[NFAT5]] (-0.46, fdr 1e-04), [[TCF7L2]] (-0.46, fdr 9e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BCAT1]] → it (grade C ⚠); 2 go from it, the strongest it → [[NFAT5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5799.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.55×** | +24.1 | 0e+00 | 12/24 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.23×** | +10.8 | 1e-24 | 4/20 (SW480, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.89×** | +8.6 | 2e-15 | 20/24 (NCI-H460, SHP-77, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.51×** | +7.8 | 1e-12 | 19/25 (NCI-H460, NCI-H1792, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.77×** | +7.7 | 1e-12 | 22/25 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +7.5 | 7e-12 | 10/25 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +6.9 | 3e-10 | 3/13 (NCI-H460, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (drug)]] 5 µM |  | **1.61×** | +6.4 | 9e-09 | 14/25 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +6.4 | 1e-08 | 3/22 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +6.3 | 2e-08 | 11/25 (SHP-77, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +6.1 | 6e-08 | 8/24 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +6.0 | 8e-08 | 2/16 (HS-578T, A549) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +5.9 | 2e-07 | 7/24 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +5.8 | 2e-07 | 13/25 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.53×** | +5.7 | 5e-07 | 20/24 (NCI-H460, A498, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM |  | **1.30×** | +5.0 | 2e-05 | 17/25 (SHP-77, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +4.8 | 4e-05 | 3/25 (SW480, A549, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.8 | 6e-05 | 4/24 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.42×** | +4.7 | 6e-05 | 13/25 (SHP-77, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5799.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.591×** | -7.1 | 6e-10 | 17/25 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.618×** | -6.3 | 1e-07 | 17/24 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.648×** | -5.9 | 8e-07 | 16/25 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.668×** | -5.5 | 6e-06 | 15/24 (H4, KATO III, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.690×** | -5.0 | 5e-05 | 18/25 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.720×** | -4.5 | 8e-04 | 9/24 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.728×** | -4.3 | 0.001 | 13/25 (KATO III, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.740×** | -4.1 | 0.003 | 12/25 (PANC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.724×** | -4.1 | 0.003 | 12/23 (A-172, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.737×** | -3.9 | 0.005 | 13/24 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.754×** | -3.8 | 0.006 | 19/24 (NCI-H1792, A-172, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -3.6 | 0.017 | 2/25 (A-172, CHP-212) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.780×** | -3.4 | 0.032 | 14/23 (A498, HS-578T, …) | inconsistent across doses |  |
| [[crizotinib (drug)]] 5 µM |  | **0.786×** | -3.1 | 0.067 | 6/25 (Panc 03.27, A498, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.852× | -3.1 | 0.073 | 4/25 (KATO III, CFPAC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5799. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 36.1 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -15.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0988× (z -12.5) |
| [[PANC-1 (line)]] | alt | 15.4 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -17.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.169× (z -12.2) |
| [[H4 (line)]] | wt | 37.1 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -16.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.126× (z -10.8) |
| [[HS-578T (line)]] | alt | 83.2 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -16.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.273× (z -10.7) |
| [[LoVo (line)]] | wt | 38.5 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -19.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.138× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 26.6 | 3 | 3 (1 ⚠) | [[Neratinib (maleate) (drug)]] 5 µM 2.79× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -11.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.232× (z -9.5) |
| [[A498 (line)]] | wt | 83.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -19.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.305× (z -11.1) |
| [[A-172 (line)]] | wt | 5.68 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.0727× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.103× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 42.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.164× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.257× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 63.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0796× (z -23.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.207× (z -10.5) |
| [[A549 (line)]] | wt | 8.52 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.139× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5799), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHGDH]] | +0.71 | +0.64 / +0.78 | both halves | 7e-06 | STRING 535 |
| [[PCK2]] | +0.71 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[SARS1]] | +0.71 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[GARS1]] | +0.70 | +0.64 / +0.79 | both halves | 7e-06 |  |
| [[ASNS]] | +0.69 | +0.63 / +0.78 | both halves | 7e-06 | STRING 439 |
| [[SLC6A9]] | +0.69 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[MTHFD2]] | +0.68 | +0.59 / +0.77 | both halves | 7e-06 | pathway: Metabolism of folate and pterines; STRING 975 |
| [[IARS1]] | +0.68 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[XPOT]] | +0.67 | +0.57 / +0.76 | both halves | 1e-05 |  |
| [[AARS1]] | +0.67 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[SLC1A4]] | +0.67 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[CARS1]] | +0.67 | +0.60 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFAT5]] | -0.46 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[TCF7L2]] | -0.46 | -0.36 / -0.46 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAT1]] | C | BCAT1 activity raises ALDH1L2's level | lines that do not express BCAT1 (25) vs lines expressing it (25) | 2.82× lower at baseline in the lines without BCAT1 | 0.008 | ⚠ within organs, on part of the lines; also absent: C5orf46, LOX, TOX; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFAT5]] | B | ALDH1L2 activity lowers NFAT5's level | lines that do not express ALDH1L2 (23) vs lines expressing it (27) | 1.31× higher at baseline in the lines without ALDH1L2 | 0.083 | ⚠ within organs, on part of the lines; also absent: SLC8A1, ENSG00000230490, GPR173 |
| [[BCAT1]] | C | ALDH1L2 activity raises BCAT1's level | lines that do not express ALDH1L2 (23) vs lines expressing it (27) | 3.00× lower at baseline in the lines without ALDH1L2 | 0.095 | ⚠ within organs, on part of the lines; also absent: SLC8A1, ENSG00000230490, GPR173; co-absent with the target |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.739). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.0, 47.9); signed map (-13.2, 24.2). **Vector** length 81.3, 22.6% of its response variance represented; |z| ≥ 3 in 734 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mTORC1 signaling* (hallmark, mean cos +0.56 to 20); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.65 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.65 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +24.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +7.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.7 | +7.8 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.6 | +6.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -5.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -7.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.2 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -5.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.1 | -2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -4.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.8 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | aldehyde dehydrogenase 1 family member L2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:105,019,784-105,107,643 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38508, mtFDH |
| Gene groups (HGNC) | Aldehyde dehydrogenases |
| Reactome | 3 pathways, smallest: Metabolism of folate and pterines; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3SY69](https://www.uniprot.org/uniprotkb/Q3SY69) (Mitochondrial 10-formyltetrahydrofolate dehydrogenase):

> Mitochondrial 10-formyltetrahydrofolate dehydrogenase that catalyzes the NADP(+)-dependent conversion of 10-formyltetrahydrofolate to tetrahydrofolate and carbon dioxide.

**Summary**, from NCBI Gene [160428](https://www.ncbi.nlm.nih.gov/gene/160428):

> This gene encodes a member of both the aldehyde dehydrogenase superfamily and the formyl transferase superfamily. This member is the mitochondrial form of 10-formyltetrahydrofolate dehydrogenase (FDH), which converts 10-formyltetrahydrofolate to tetrahydrofolate and CO2 in an NADP(+)-dependent reaction, and plays an essential role in the distribution of one-carbon groups between the cytosolic and mitochondrial compartments of the cell. Alternatively spliced transcript variants have been found …

**Accessions** — [HGNC:26777](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26777) · Entrez [160428](https://www.ncbi.nlm.nih.gov/gene/160428) · UniProt [Q3SY69](https://www.uniprot.org/uniprotkb/Q3SY69) · Ensembl [ENSG00000136010](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136010)

## Data

Gene col 5799: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5799); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5799, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5799]; `tensor/DDL_lfc|DDL_z.npy` [5799]; `embed/gene_vectors.npy` [5799]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5799 or target_col == 5799). Every well: [[ALDH1L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDH1L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
