---
symbol: "ZFAND1"
type: "gene"
col: 2431
ensembl_id: "ENSG00000104231"
name: "zinc finger AN1-type containing 1"
location: "8q21.13"
module: 63
arm: "+"
pooled_cpm: 29.12
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 18
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# ZFAND1

*zinc finger AN1-type containing 1* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.68× (z +10.6, q 1e-23, up in 29 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.45× (z +7.6, q 3e-12, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.644× (z -9.1, q 7e-17, down in 30 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 0.05 µM: 0.708× (z -6.7, q 6e-09, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCEA1]] (+0.82, fdr 7e-06), [[XPOT]] (+0.79, fdr 7e-06), [[TUBE1]] (+0.72, fdr 7e-06); moves opposite to [[SNRPB]] (-0.60, fdr 1e-05), [[TUBB4B]] (-0.55, fdr 1e-05), [[POLR2L]] (-0.52, fdr 2e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SYTL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2431.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +10.6 | 1e-23 | 29/42 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +9.3 | 5e-18 | 21/35 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +7.7 | 2e-12 | 23/39 (HepG2/C3A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +7.6 | 3e-12 | 32/48 (SW480, BT-474, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM |  | **1.26×** | +6.5 | 1e-08 | 23/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +6.4 | 1e-08 | 25/47 (HS-578T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.37×** | +6.0 | 1e-07 | 21/48 (LoVo, NCI-H2347, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.32×** | +5.6 | 1e-06 | 24/48 (AsPC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.31×** | +5.5 | 2e-06 | 23/48 (AsPC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.20×** | +5.3 | 5e-06 | 15/48 (LoVo, A-427, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +5.2 | 1e-05 | 17/48 (KATO III, SW 900, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +4.9 | 4e-05 | 22/47 (SHP-77, NCI-H2347, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.24×** | +4.4 | 5e-04 | 16/48 (SW480, RKO, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.50×** | +4.3 | 6e-04 | 14/48 (NCI-H2347, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +4.3 | 7e-04 | 10/48 (HT-29, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +4.2 | 8e-04 | 15/47 (A498, CFPAC-1, …) | two highest doses |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.20×** | +3.7 | 0.006 | 13/47 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.18× | +3.3 | 0.021 | 14/47 (RKO, HEC-1-A, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.12× | +3.3 | 0.026 | 9/49 (PANC-1, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2431.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.644×** | -9.1 | 7e-17 | 30/46 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.708×** | -6.7 | 6e-09 | 24/47 (RKO, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.752×** | -5.9 | 8e-07 | 22/47 (PANC-1, RKO, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.758×** | -5.7 | 2e-06 | 22/47 (PANC-1, SW480, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -5.0 | 6e-05 | 18/47 (RKO, NCI-H23, …) | top dose only | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **0.818×** | -4.1 | 0.003 | 11/48 (RKO, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.819×** | -4.1 | 0.003 | 21/48 (PANC-1, RKO, …) | two highest doses | composition shift |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.870× | -4.0 | 0.004 | 8/48 (Hs 766T, A-427, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.693×** | -4.0 | 0.004 | 13/45 (SW48, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | 0.873× | -3.9 | 0.004 | 16/47 (HT-29, Panc 03.27, …) | inconsistent across doses | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.874× | -3.9 | 0.005 | 14/48 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.887× | -3.5 | 0.025 | 9/48 (RPMI-7951, LS 180, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.848× | -3.4 | 0.029 | 7/47 (A498, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.838× | -3.4 | 0.030 | 15/47 (HepG2/C3A, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.852× | -3.3 | 0.034 | 12/47 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.856× | -3.2 | 0.042 | 8/48 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 5 µM |  | 0.898× | -3.1 | 0.059 | 10/48 (HT-29, A498, …) | rises with dose | position effect removed |
| [[Demeclocycline (drug)]] 5 µM |  | 0.903× | -3.0 | 0.085 | 5/48 (MIA PaCa-2, A498, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.759×** | -3.0 | 0.085 | 14/45 (C32, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2431. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +11.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 71.0 | 1 | 1 (1 ⚠) | [[Artesunate (drug)]] 5 µM 1.96× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 45.2 | 1 | 1 (1 ⚠) | [[Artesunate (drug)]] 5 µM 1.78× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.447× (z -10.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.161× (z -9.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 21.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0752× (z -12.6) |
| [[HOP62 (line)]] | alt | 21.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 61.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -14.0) ⚠ cell-cycle shift, explains ~95% of this change |
| [[LoVo (line)]] | wt | 47.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -9.8) ⚠ cell-cycle shift, explains ~95% of this change |
| [[Panc 03.27 (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -9.9) ⚠ cell-cycle shift, explains ~95% of this change |
| [[PANC-1 (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.452× (z -9.5) ⚠ cell-cycle shift, explains ~20% of this change |
| [[A-172 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 53.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2431), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCEA1]] | +0.82 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[XPOT]] | +0.79 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[TUBE1]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[AARS1]] | +0.72 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[RSL24D1]] | +0.71 | +0.70 / +0.65 | both halves | 7e-06 | STRING 434 |
| [[IARS1]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[PSAT1]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[GARS1]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[EPRS1]] | +0.69 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[PHGDH]] | +0.69 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[MTHFD2]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[CEBPG]] | +0.68 | +0.67 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPB]] | -0.60 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[TUBB4B]] | -0.55 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[POLR2L]] | -0.52 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[CFL1]] | -0.51 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[LUZP1]] | -0.50 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[PKNOX1]] | -0.49 | -0.46 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYTL1]] | B | SYTL1 activity raises ZFAND1's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 1.56× lower at baseline in the lines without SYTL1 | 0.023 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[FAM83F]] | B | FAM83F activity raises ZFAND1's level | lines that do not express FAM83F (32) vs lines expressing it (18) | 1.81× lower at baseline in the lines without FAM83F | 0.037 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TRIM15, TMEM45B |
| [[ESRP1]] | B | ESRP1 activity raises ZFAND1's level | lines that do not express ESRP1 (31) vs lines expressing it (19) | 1.79× lower at baseline in the lines without ESRP1 | 0.072 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[ERICH2]] | B | ERICH2 activity strengthens ZFAND1's drug response | lines that do not express ERICH2 (11) vs lines expressing it (37) | the lines without ERICH2 respond 0.99× as strongly (z diff +0.05); rises at some drug-doses, falls at others (57% from rises): Artesunate 5 µM: 1.11x vs 1.33x (z diff +2.0); Digitoxin 0.5 µM: 0.85x vs 0.70x (z diff +1.6); Ponatinib 5 µM: 1.30x vs 1.50x (z diff +1.3) | 0.081 | ⚠ within organs, on part of the lines; also absent: ERICH2-DT, DMBX1, GAD1; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |
| [[LINC00662]] | C | LINC00662 activity lowers ZFAND1's level | lines that do not express LINC00662 (3) vs lines expressing it (47) | 2.16× higher at baseline in the lines without LINC00662 | 0.073 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: NME4, ZFP14, ZNF221 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.769). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.2, 47.2); signed map (-14.6, 24.1). **Vector** length 103, 23.5% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.58 to 16); *mTORC1 signaling* (hallmark, mean cos +0.57 to 20); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.66 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.8 | +7.6 |
|  | [[Artesunate (drug)]] 5 µM |  | +5.1 | +6.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.8 | +5.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +10.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.5 | +5.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +2.4 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.3 | +3.2 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -3.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -9.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -3.7 | -5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | -5.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -3.4 | -5.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.3 | -6.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.0 | -4.1 |
|  | [[Thymol (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger AN1-type containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.13 — chr8:81,701,334-81,732,903 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14007 |
| Gene groups (HGNC) | Zinc fingers AN1-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCF1](https://www.uniprot.org/uniprotkb/Q8TCF1) (AN1-type zinc finger protein 1):

> Plays a role in the regulation of cytoplasmic stress granules (SGs) turnover. SGs are dynamic and transient cytoplasmic ribonucleoprotein assemblies important for cellular protein homeostasis when protein production is suspended after acute exogenous stress. Associates with SGs and is involved in the efficient and specific arsenite-induced clearance process of SGs through the recruitment of the ubiquitin-selective ATPase VCP and the 26S proteasome. This process requires both complexes for …

**Summary**, from NCBI Gene [79752](https://www.ncbi.nlm.nih.gov/gene/79752):

> Enables proteasome binding activity. Involved in cellular response to arsenite ion; positive regulation of intracellular protein transport; and stress granule disassembly. Located in cytoplasmic stress granule. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25858) · Entrez [79752](https://www.ncbi.nlm.nih.gov/gene/79752) · UniProt [Q8TCF1](https://www.uniprot.org/uniprotkb/Q8TCF1) · Ensembl [ENSG00000104231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104231)

## Data

Gene col 2431: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2431); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2431, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2431]; `tensor/DDL_lfc|DDL_z.npy` [2431]; `embed/gene_vectors.npy` [2431]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2431 or target_col == 2431). Every well: [[ZFAND1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFAND1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
