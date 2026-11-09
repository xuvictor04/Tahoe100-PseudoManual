---
symbol: "ENTPD3-AS1"
type: "gene"
col: 13365
ensembl_id: "ENSG00000223797"
name: "ENTPD3, EIF1B and MYRIP antisense RNA 1"
location: "3p22.1"
module: 23
arm: "+"
pooled_cpm: 10.11
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 22
n_dd_up_clean: 21
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# ENTPD3-AS1

*ENTPD3, EIF1B and MYRIP antisense RNA 1* — 3p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.95× (z +9.2, q 1e-17, up in 26 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.446× (z -7.6, q 1e-11, down in 26 of 38 measured lines) ⚠ toxic; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.500× (z -6.8, q 3e-09, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEXIM2-AS1]] (+0.82, fdr 7e-06), [[ANKRD17-DT]] (+0.78, fdr 1e-05), [[DNAI4]] (+0.78, fdr 1e-05); moves opposite to [[NAPG]] (-0.61, fdr 2e-04), [[SH3PXD2B]] (-0.61, fdr 1e-04), [[GPRIN1]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13365.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +9.2 | 1e-17 | 26/45 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.79×** | +5.7 | 3e-06 | 30/45 (KATO III, LS 180, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.60×** | +4.3 | 0.004 | 19/46 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.36×** | +4.2 | 0.004 | 18/47 (A549, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.38×** | +4.2 | 0.004 | 16/47 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.56×** | +3.9 | 0.007 | 21/47 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +3.9 | 0.009 | 13/42 (HT-29, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.011 | 12/46 (SW480, C32, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.012 | 16/47 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.012 | 14/46 (SW480, C32, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.012 | 16/45 (KATO III, A-427, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +3.7 | 0.012 | 14/47 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +3.5 | 0.021 | 13/46 (LS 180, C-33 A, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.021 | 16/47 (SW480, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.025 | 9/46 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.025 | 14/45 (SW480, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13365.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.446×** | -7.6 | 1e-11 | 26/38 (NCI-H460, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.500×** | -6.8 | 3e-09 | 31/46 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.512×** | -6.6 | 8e-09 | 29/46 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.518×** | -6.5 | 1e-08 | 26/45 (C32, RPMI-7951, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.333×** | -5.7 | 2e-06 | 24/45 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.363×** | -5.2 | 2e-05 | 27/42 (NCI-H460, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.625×** | -4.6 | 3e-04 | 24/44 (KATO III, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.636×** | -4.5 | 6e-04 | 21/46 (SW1417, NCI-H1573, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.629×** | -4.3 | 0.001 | 21/45 (HEC-1-A, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.653×** | -4.2 | 0.002 | 20/46 (SNU-1, MIA PaCa-2, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.646×** | -4.1 | 0.002 | 22/44 (NCI-H460, RPMI-7951, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.764×** | -3.7 | 0.008 | 17/47 (NCI-H460, SW48, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.675×** | -3.7 | 0.008 | 16/37 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.592×** | -3.7 | 0.009 | 12/47 (NCI-H661, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.500×** | -3.6 | 0.014 | 14/45 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.716×** | -3.3 | 0.036 | 14/46 (C32, NCI-H661, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.706×** | -3.2 | 0.040 | 17/47 (H4, SW 1088, …) | all doses, flat |  |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | **0.726×** | -3.2 | 0.051 | 12/46 (HCT15, SW 1271, …) | two highest doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.551×** | -3.1 | 0.065 | 11/41 (NCI-H460, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.739×** | -3.0 | 0.080 | 11/46 (COLO 205, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13365. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 17.5 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.170× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0709× (z -8.6) |
| [[KATO III (line)]] | alt | 11.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change · without an alert: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.128× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 28.8 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.151× (z -9.2) |
| [[C32 (line)]] | wt | 12.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0427× (z -13.4) |
| [[HCT15 (line)]] | alt | 9.77 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0753× (z -8.9) |
| [[RKO (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0907× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~27% of this change |
| [[SHP-77 (line)]] | alt | 5.04 | 0 | 1 | — | [[Terfenadine (drug)]] 0.05 µM 0.0651× (z -8.9) |
| [[SW 900 (line)]] | alt | 5.14 | 0 | 1 | — | [[Macitentan (drug)]] 0.05 µM 0.0530× (z -8.5) |
| [[A-172 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13365), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEXIM2-AS1]] | +0.82 | +0.81 / +0.63 | both halves | 7e-06 | same gene group |
| [[ANKRD17-DT]] | +0.78 | +0.81 / +0.51 | both halves | 1e-05 |  |
| [[DNAI4]] | +0.78 | +0.76 / +0.49 | both halves | 1e-05 |  |
| [[NIFK-AS1]] | +0.77 | +0.73 / +0.61 | both halves | 7e-06 | same gene group |
| [[CHD1-DT]] | +0.75 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[BDNF-AS]] | +0.74 | +0.74 / +0.51 | both halves | 1e-05 | same gene group |
| [[PRANCR]] | +0.74 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[MFF-DT]] | +0.73 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[SPESP1]] | +0.71 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[OXA1L-DT]] | +0.71 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[DICER1-AS1]] | +0.71 | +0.69 / +0.50 | both halves | 1e-05 | same gene group |
| [[AHI1-DT]] | +0.71 | +0.68 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAPG]] | -0.61 | -0.62 / -0.29 | both halves | 2e-04 |  |
| [[SH3PXD2B]] | -0.61 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[GPRIN1]] | -0.60 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[WASF3]] | -0.59 | -0.53 / -0.21 | both halves | 6e-04 |  |
| [[TWF2]] | -0.59 | -0.54 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers ENTPD3-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[TMEM9B-AS1]] | B | TMEM9B-AS1 activity raises ENTPD3-AS1's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 1.64× lower at baseline in the lines without TMEM9B-AS1 | 0.081 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |
| [[DPH6-DT]] | C | DPH6-DT activity raises ENTPD3-AS1's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 2.07× lower at baseline in the lines without DPH6-DT | 0.096 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.761). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.4, 17.4); signed map (27.1, -8.0). **Vector** length 79.4, 16.0% of its response variance represented; |z| ≥ 3 in 1,058 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.1 | -1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +3.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | -1.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -4.1 | -4.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.5 | -3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -3.3 | -4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -0.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | ENTPD3, EIF1B and MYRIP antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p22.1 |
| Also known as | FLJ36665; previously EIF1B-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26710](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26710) · Entrez [285266](https://www.ncbi.nlm.nih.gov/gene/285266) · Ensembl [ENSG00000223797](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223797)

## Data

Gene col 13365: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13365); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13365, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13365]; `tensor/DDL_lfc|DDL_z.npy` [13365]; `embed/gene_vectors.npy` [13365]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13365 or target_col == 13365). Every well: [[ENTPD3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENTPD3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
