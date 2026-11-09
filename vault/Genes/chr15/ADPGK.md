---
symbol: "ADPGK"
type: "gene"
col: 8244
ensembl_id: "ENSG00000159322"
name: "ADP dependent glucokinase"
location: "15q24.1"
module: 226
arm: "+"
pooled_cpm: 45.0
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/226"]
generated_by: "tahoemap"
---

# ADPGK

*ADP dependent glucokinase* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.38× (z +6.5, q 4e-08, up in 30 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.65× (z +5.3, q 2e-05, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.537× (z -17.9, q 0e+00, down in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.715× (z -9.7, q 1e-19, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPUSD4]] (+0.68, fdr 7e-06), [[ANAPC10]] (+0.66, fdr 8e-06), [[WDR5]] (+0.65, fdr 7e-06); moves opposite to [[CCDC148]] (-0.68, fdr 7e-06), [[NBPF10]] (-0.66, fdr 7e-06), [[N4BP3]] (-0.65, fdr 7e-06).
> It is in [[Module 226]], a single-armed module (NOTCH2 Activation and Transmission of Signal to the Nucleus).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8244.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +6.5 | 4e-08 | 30/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.36×** | +6.3 | 1e-07 | 31/48 (NCI-H460, HOP62, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.37×** | +6.0 | 3e-07 | 29/48 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +5.3 | 2e-05 | 30/48 (SW1417, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +4.7 | 3e-04 | 23/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.49×** | +4.2 | 0.002 | 22/49 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.0 | 0.005 | 21/48 (HOP62, HT-29, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +3.9 | 0.006 | 19/47 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Gallic acid (drug)]] 5 µM |  | 1.13× | +3.4 | 0.042 | 3/48 (SW48, HS-578T, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.044 | 19/48 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.12× | +3.3 | 0.044 | 16/48 (SW1417, HT-29, …) | rises with dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.2 | 0.062 | 18/48 (NCI-H1573, SW480, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.2 | 0.062 | 19/48 (SW480, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8244.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.537×** | -17.9 | 0e+00 | 46/48 (HOP62, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.715×** | -9.7 | 1e-19 | 39/48 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.619×** | -9.4 | 1e-18 | 40/48 (A-172, AN3 CA, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.650×** | -8.8 | 3e-16 | 33/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.733×** | -6.3 | 3e-08 | 30/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.762×** | -5.5 | 3e-06 | 34/48 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.780×** | -5.1 | 3e-05 | 27/48 (KATO III, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.777×** | -4.8 | 1e-04 | 25/44 (HepG2/C3A, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.838× | -3.6 | 0.019 | 17/48 (A-172, A498, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8244. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 36.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -20.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.314× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 58.2 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -11.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[C32 (line)]] | wt | 47.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -15.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 67.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -11.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HS-578T (line)]] | alt | 24.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -9.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[hTERT-HPNE (line)]] | wt | 41.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -11.0) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.301× (z -8.8) |
| [[KATO III (line)]] | alt | 59.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -12.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 60.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -17.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SNU-1 (line)]] | wt | 40.1 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.125× (z -9.8) ⚠ toxic |
| [[SW48 (line)]] | wt | 44.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.216× (z -10.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 49.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.136× (z -9.5) ⚠ cell-cycle shift, explains ~35% of this change |
| [[AsPC-1 (line)]] | alt | 40.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.347× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[CFPAC-1 (line)]] | alt | 47.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -9.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[CHP-212 (line)]] | wt | 51.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.100× (z -11.1) |
| [[HCT15 (line)]] | alt | 44.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -9.3) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HEC-1-A (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.397× (z -8.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 29.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.111× (z -13.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 42.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -20.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[Hs 766T (line)]] | wt | 30.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[J82 (line)]] | alt | 43.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -13.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[LOX-IMVI (line)]] | wt | 38.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -10.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[MIA PaCa-2 (line)]] | alt | 36.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -8.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H1792 (line)]] | alt | 58.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -10.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H460 (line)]] | wt | 42.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -11.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H661 (line)]] | alt | 46.5 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0986× (z -8.9) |
| [[PANC-1 (line)]] | alt | 42.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.599× (z -9.9) ⚠ cell-cycle shift, explains ~34% of this change |
| [[RKO (line)]] | wt | 46.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -11.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[RPMI-7951 (line)]] | alt | 53.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -11.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SK-MEL-2 (line)]] | alt | 47.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SNU-423 (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -13.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW1417 (line)]] | alt | 50.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.384× (z -8.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 49.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[A-427 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8244), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPUSD4]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[ANAPC10]] | +0.66 | +0.67 / +0.57 | both halves | 8e-06 |  |
| [[WDR5]] | +0.65 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[PHB2]] | +0.65 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[SNHG30]] | +0.65 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[ARHGEF7]] | +0.64 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[GLB1]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[TMEM248]] | +0.62 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[C1orf216]] | +0.62 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[RNF4]] | +0.62 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[NAGPA]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[AHSA1]] | +0.61 | +0.60 / +0.57 | both halves | 8e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC148]] | -0.68 | -0.71 / -0.65 | both halves | 7e-06 |  |
| [[NBPF10]] | -0.66 | -0.72 / -0.60 | both halves | 7e-06 |  |
| [[N4BP3]] | -0.65 | -0.59 / -0.69 | both halves | 7e-06 |  |
| [[NOTCH2NLB]] | -0.62 | -0.70 / -0.49 | both halves | 1e-05 |  |
| [[ZFHX2]] | -0.61 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[PIM3]] | -0.61 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[LMNA]] | -0.61 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[LINC02901]] | -0.60 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[NR1D1]] | -0.59 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[BTG1]] | -0.59 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[MARCKS]] | -0.58 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[APLF]] | -0.58 | -0.65 / -0.63 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ADPGK's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[OXTR]] | B | OXTR activity raises ADPGK's level | lines that do not express OXTR (5) vs lines expressing it (45) | 1.12× lower at baseline in the lines without OXTR | 0.089 | ⚠ within organs, on part of the lines; also absent: IPCEF1, SSUH2, OPN3; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity lowers ADPGK's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 226]] — NOTCH2 Activation and Transmission of Signal to the Nucleus; 9 genes; every member is in the + arm (projection on the module's main direction -0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.8, -13.8); signed map (-42.1, -13.0). **Vector** length 101, 23.3% of its response variance represented; |z| ≥ 3 in 835 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.3 | +6.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.4 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +5.4 | +6.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.3 | +6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.9 | +2.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.5 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -11.0 | -17.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -8.3 | -9.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -8.1 | -9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.9 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.7 | -8.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.7 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ADP dependent glucokinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.1 — chr15:72,751,294-72,785,846 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434B195, ADP-GK |
| Gene groups (HGNC) | Carbohydrate kinases |
| Reactome | 3 pathways, smallest: Glycolysis; Glucose metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRR6](https://www.uniprot.org/uniprotkb/Q9BRR6) (ADP-dependent glucokinase):

> Catalyzes the phosphorylation of D-glucose to D-glucose 6-phosphate using ADP as the phosphate donor. GDP and CDP can replace ADP, but with reduced efficiency.

**Summary**, from NCBI Gene [83440](https://www.ncbi.nlm.nih.gov/gene/83440):

> ADPGK (EC 2.7.1.147) catalyzes the ADP-dependent phosphorylation of glucose to glucose-6-phosphate and may play a role in glycolysis, possibly during ischemic conditions (Ronimus and Morgan, 2004 [PubMed 14975750]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:25250](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25250) · Entrez [83440](https://www.ncbi.nlm.nih.gov/gene/83440) · UniProt [Q9BRR6](https://www.uniprot.org/uniprotkb/Q9BRR6) · Ensembl [ENSG00000159322](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159322)

## Data

Gene col 8244: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8244); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8244, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8244]; `tensor/DDL_lfc|DDL_z.npy` [8244]; `embed/gene_vectors.npy` [8244]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8244 or target_col == 8244). Every well: [[ADPGK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADPGK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
