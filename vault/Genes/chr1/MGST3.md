---
symbol: "MGST3"
type: "gene"
col: 6696
ensembl_id: "ENSG00000143198"
name: "microsomal glutathione S-transferase 3"
location: "1q24.1"
module: 30
arm: "+"
pooled_cpm: 45.22
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 16
n_dd_up_clean: 14
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# MGST3

*microsomal glutathione S-transferase 3* — 1q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.98× (z +8.1, q 3e-13, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.391× (z -15.5, q 0e+00, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC45A]] (+0.76, fdr 7e-06), [[RRAS]] (+0.76, fdr 7e-06), [[ANKRD27]] (+0.74, fdr 7e-06); moves opposite to [[ST7L]] (-0.74, fdr 7e-06), [[SRCAP]] (-0.70, fdr 7e-06), [[ZC3H4]] (-0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TSPAN33]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 1 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6696.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.98×** | +8.1 | 3e-13 | 34/47 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +8.0 | 3e-13 | 38/47 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +6.2 | 9e-08 | 33/47 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +5.0 | 8e-05 | 31/47 (SW1417, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +5.0 | 8e-05 | 30/47 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.32×** | +4.7 | 2e-04 | 32/47 (AsPC-1, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +4.1 | 0.004 | 27/47 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.67×** | +4.0 | 0.004 | 33/45 (H4, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.65×** | +3.9 | 0.005 | 29/47 (LoVo, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.011 | 27/47 (SW1417, C32, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.36×** | +3.7 | 0.011 | 24/44 (NCI-H460, A549, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.57×** | +3.5 | 0.019 | 26/46 (J82, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.029 | 25/47 (LS 180, LoVo, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.49×** | +3.2 | 0.063 | 22/47 (Hs 766T, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.089 | 23/47 (LOX-IMVI, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6696.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.391×** | -15.5 | 0e+00 | 43/46 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.479×** | -8.6 | 2e-15 | 40/46 (SW 900, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.518×** | -7.7 | 3e-12 | 39/47 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.542×** | -6.9 | 8e-10 | 34/47 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.599×** | -6.0 | 3e-07 | 41/47 (LoVo, A-172, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.664×** | -4.8 | 2e-04 | 34/47 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.461×** | -4.7 | 2e-04 | 30/48 (LS 180, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.673×** | -4.6 | 3e-04 | 31/47 (A-172, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.696×** | -4.2 | 0.002 | 28/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.705×** | -4.1 | 0.003 | 28/46 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.719×** | -3.8 | 0.007 | 26/47 (MIA PaCa-2, H4, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.712×** | -3.7 | 0.009 | 27/46 (A-172, SW 900, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.576×** | -3.4 | 0.034 | 24/47 (LS 180, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.741×** | -3.3 | 0.034 | 21/46 (SNU-423, COLO 205, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.758×** | -3.2 | 0.050 | 23/47 (A-172, SW 900, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.760×** | -3.2 | 0.052 | 19/47 (NCI-H2030, A549, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6696. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 49.4 | 2 | 3 | [[Panobinostat (drug)]] 0.5 µM 2.55× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -18.8) |
| [[SW 900 (line)]] | alt | 81.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -17.5) |
| [[A-172 (line)]] | wt | 82.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -14.1) |
| [[A498 (line)]] | wt | 56.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -14.2) |
| [[HS-578T (line)]] | alt | 62.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -12.0) |
| [[A-427 (line)]] | wt | 56.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -15.2) |
| [[AsPC-1 (line)]] | alt | 42.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -11.2) |
| [[HOP62 (line)]] | alt | 44.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -15.5) |
| [[Hs 766T (line)]] | wt | 43.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -14.9) |
| [[RPMI-7951 (line)]] | alt | 51.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -16.6) |
| [[A549 (line)]] | wt | 49.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -10.5) |
| [[BT-474 (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 28.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 53.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -12.8) |
| [[HCT15 (line)]] | alt | 68.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 64.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -12.6) |
| [[J82 (line)]] | alt | 40.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -11.4) |
| [[LoVo (line)]] | wt | 50.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 30.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 41.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.199× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 30.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 32.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 38.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -17.1) |
| [[NCI-H23 (line)]] | alt | 23.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -15.8) |
| [[NCI-H2347 (line)]] | alt | 73.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -15.8) |
| [[NCI-H661 (line)]] | alt | 31.2 | 0 | 1 | — | [[Bexarotene (drug)]] 0.5 µM 0.0581× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 43.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -9.9) |
| [[PANC-1 (line)]] | alt | 32.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -11.2) |
| [[SHP-77 (line)]] | alt | 28.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -10.4) |
| [[SNU-423 (line)]] | alt | 55.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -11.2) |
| [[SW 1088 (line)]] | alt | 68.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -8.9) |
| [[SW480 (line)]] | alt | 30.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -8.7) |
| [[AN3 CA (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 62.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6696), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC45A]] | +0.76 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[RRAS]] | +0.76 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[ANKRD27]] | +0.74 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[CARD19]] | +0.74 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[SLC27A1]] | +0.73 | +0.63 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_ADIPOGENESIS |
| [[PLD3]] | +0.72 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[LCMT1]] | +0.72 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[DPY30]] | +0.71 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[STX7]] | +0.71 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[TBCB]] | +0.71 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.71 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[KLHL7]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST7L]] | -0.74 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[SRCAP]] | -0.70 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[ZC3H4]] | -0.69 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[CYREN]] | -0.68 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[CPSF2]] | -0.66 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.66 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[TASOR]] | -0.66 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[LEKR1]] | -0.65 | -0.62 / -0.40 | both halves | 4e-05 |  |
| [[RGS5]] | -0.65 | -0.66 / -0.46 | both halves | 2e-05 |  |
| [[PSME3IP1]] | -0.65 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[ZFP91]] | -0.64 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.64 | -0.49 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN33]] | B | TSPAN33 activity lowers MGST3's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.33× higher at baseline in the lines without TSPAN33 | 0.059 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[SFXN3]] | C | SFXN3 activity raises MGST3's level | lines that do not express SFXN3 (3) vs lines expressing it (47) | 2.45× lower at baseline in the lines without SFXN3 | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, GULP1, SMAD7 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.795). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (2.0, -4.4); signed map (-29.7, 16.2). **Vector** length 124, 40.0% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.9 | +8.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.3 | +5.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +8.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.8 | +4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.8 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.5 | +3.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.0 | -15.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -2.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.8 | -2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | microsomal glutathione S-transferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.1 — chr1:165,631,213-165,661,796 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GST-III |
| Gene groups (HGNC) | Microsomal glutathione S-transferases; MAPEG superfamily |
| Hallmark sets | HEME_METABOLISM, ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: Aflatoxin activation and detoxification; Glutathione conjugation; Phase II - Conjugation of compounds |
| Matched by | ensembl_id |

**Function**, from UniProt [O14880](https://www.uniprot.org/uniprotkb/O14880) (Glutathione S-transferase 3, mitochondrial):

> Displays both glutathione S-transferase and glutathione peroxidase activities toward oxyeicosanoids, as part of cellular detoxification as well as synthesis of bioactive metabolites. Catalyzes conjugate addition of reduced glutathione to the alpha, beta-unsaturated C=C carbonyl group of eisosanoids such as leukotriene A4 and 15-deoxy-Delta12,14-prostaglandin J2 to form GSH adducts relevant to the inflammatory response. Catalyzes glutathione-dependent reduction of eicosanoid peroxides to yield …

**Summary**, from NCBI Gene [4259](https://www.ncbi.nlm.nih.gov/gene/4259):

> This gene encodes a member of the MAPEG (Membrane Associated Proteins in Eicosanoid and Glutathione metabolism) protein family. Members of this family are involved in the production of leukotrienes and prostaglandin E, important mediators of inflammation. This gene encodes an enzyme which catalyzes the conjugation of leukotriene A4 and reduced glutathione to produce leukotriene C4. This enzyme also demonstrates glutathione-dependent peroxidase activity towards lipid hydroperoxides.[provided by …

**Accessions** — [HGNC:7064](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7064) · Entrez [4259](https://www.ncbi.nlm.nih.gov/gene/4259) · UniProt [O14880](https://www.uniprot.org/uniprotkb/O14880) · Ensembl [ENSG00000143198](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143198)

## Data

Gene col 6696: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6696); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6696, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6696]; `tensor/DDL_lfc|DDL_z.npy` [6696]; `embed/gene_vectors.npy` [6696]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6696 or target_col == 6696). Every well: [[MGST3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MGST3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
