---
symbol: "TMTC4"
type: "gene"
col: 4596
ensembl_id: "ENSG00000125247"
name: "transmembrane O-mannosyltransferase targeting cadherins 4"
location: "13q32.3"
module: 18
arm: "+"
pooled_cpm: 16.73
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 27
n_dd_up_clean: 3
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# TMTC4

*transmembrane O-mannosyltransferase targeting cadherins 4* — 13q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.07× (z +11.3, q 1e-26, up in 18 of 27 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.38× (z +5.2, q 4e-05, up in 18 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.174× (z -39.1, q 0e+00, down in 43 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UCK2]] (+0.75, fdr 7e-06), [[GART]] (+0.74, fdr 7e-06), [[ADCY3]] (+0.70, fdr 7e-06); moves opposite to [[TOX4]] (-0.64, fdr 1e-05), [[PI4KB]] (-0.60, fdr 1e-05), [[USP8]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[RANBP17]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4596.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +11.3 | 1e-26 | 18/27 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +10.1 | 2e-21 | 27/39 (NCI-H1573, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +5.2 | 4e-05 | 18/46 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +4.8 | 2e-04 | 18/32 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.028 | 10/46 (A549, hTERT-HPNE, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.16× | +3.4 | 0.068 | 6/47 (SW480, KATO III, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.075 | 9/44 (A-427, SK-MEL-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.22× | +3.1 | 0.13 | 10/46 (NCI-H1573, LS 180, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.21× | +3.0 | 0.15 | 7/46 (BT-474, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4596.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.174×** | -39.1 | 0e+00 | 43/43 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.185×** | -26.1 | 0e+00 | 41/45 (RKO, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.198×** | -26.0 | 0e+00 | 42/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.414×** | -14.2 | 2e-43 | 34/45 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.465×** | -12.3 | 1e-32 | 38/46 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.491×** | -11.4 | 3e-28 | 34/46 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.552×** | -9.5 | 1e-19 | 29/46 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.337×** | -9.1 | 5e-18 | 34/46 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.403×** | -7.6 | 2e-12 | 30/44 (NCI-H2030, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.631×** | -7.4 | 8e-12 | 25/46 (AN3 CA, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.634×** | -7.3 | 1e-11 | 25/46 (BT-474, SW48, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.650×** | -6.9 | 2e-10 | 27/46 (SW48, SW480, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.660×** | -6.7 | 1e-09 | 25/46 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.665×** | -6.5 | 2e-09 | 23/46 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.670×** | -6.1 | 5e-08 | 24/46 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.704×** | -5.6 | 6e-07 | 22/46 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4596. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 15.0 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0579× (z -34.1) |
| [[BT-474 (line)]] | alt | 35.3 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0913× (z -24.1) |
| [[SW480 (line)]] | alt | 19.6 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -24.9) |
| [[J82 (line)]] | alt | 27.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0637× (z -29.0) |
| [[C32 (line)]] | wt | 14.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0993× (z -16.8) |
| [[NCI-H1573 (line)]] | alt | 19.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0541× (z -22.4) |
| [[NCI-H460 (line)]] | wt | 16.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0760× (z -24.7) |
| [[SW48 (line)]] | wt | 35.2 | 0 | 5 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0736× (z -14.0) |
| [[A-427 (line)]] | wt | 20.6 | 0 | 4 | — | [[Harringtonine (drug)]] 0.5 µM 0.156× (z -13.4) |
| [[A498 (line)]] | wt | 24.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -17.8) |
| [[A549 (line)]] | wt | 16.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0849× (z -21.5) |
| [[HEC-1-A (line)]] | alt | 26.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -24.6) |
| [[LoVo (line)]] | wt | 16.6 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.30× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -19.2) |
| [[LOX-IMVI (line)]] | wt | 17.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0641× (z -24.4) |
| [[SHP-77 (line)]] | alt | 48.8 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.239× (z -12.6) |
| [[SNU-1 (line)]] | wt | 32.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0894× (z -13.1) |
| [[SW1417 (line)]] | alt | 17.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0867× (z -21.5) |
| [[A-172 (line)]] | wt | 9.88 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -13.5) |
| [[LS 180 (line)]] | wt | 21.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -19.5) |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0924× (z -20.6) |
| [[RKO (line)]] | wt | 25.7 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0241× (z -19.5) |
| [[HOP62 (line)]] | alt | 9.24 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -14.2) |
| [[HS-578T (line)]] | alt | 5.90 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -10.4) |
| [[HT-29 (line)]] | alt | 18.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -18.5) |
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.126× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 16.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 15.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0539× (z -23.3) |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0228× (z -18.6) |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0634× (z -21.6) |
| [[SW 900 (line)]] | alt | 12.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -14.1) |
| [[AsPC-1 (line)]] | alt | 6.00 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -10.6) |
| [[CHP-212 (line)]] | wt | 15.2 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0460× (z -8.5) |
| [[COLO 205 (line)]] | alt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0856× (z -14.1) |
| [[HepG2_C3A (line)]] | wt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -10.1) |
| [[Hs 766T (line)]] | wt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -15.1) |
| [[KATO III (line)]] | alt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -10.9) |
| [[RPMI-7951 (line)]] | alt | 6.14 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -9.6) |
| [[AN3 CA (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4596), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UCK2]] | +0.75 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[GART]] | +0.74 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[ADCY3]] | +0.70 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[NUDT3]] | +0.70 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[GMPS]] | +0.70 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[HACD3]] | +0.68 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[FAM20B]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[XPO5]] | +0.67 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[NAE1]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[LRRC20]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[PALS2]] | +0.65 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOX4]] | -0.64 | -0.74 / -0.49 | both halves | 1e-05 |  |
| [[PI4KB]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[USP8]] | -0.60 | -0.69 / -0.45 | both halves | 3e-05 |  |
| [[GOLGB1]] | -0.58 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[CCDC174]] | -0.58 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[SNRNP27]] | -0.58 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[CREB3]] | -0.58 | -0.59 / -0.58 | both halves | 8e-06 |  |
| [[ZNF585A]] | -0.57 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[THAP1]] | -0.57 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[ZNF44]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[MFAP1]] | -0.56 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[NECAP2]] | -0.56 | -0.50 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RANBP17]] | B | RANBP17 activity lowers TMTC4's level | lines that do not express RANBP17 (10) vs lines expressing it (40) | 1.10× higher at baseline in the lines without RANBP17 | 0.064 | ⚠ within organs, on part of the lines |
| [[CRACD]] | B | CRACD activity raises TMTC4's level | lines that do not express CRACD (12) vs lines expressing it (38) | 1.87× lower at baseline in the lines without CRACD | 0.066 | ⚠ within organs, on part of the lines; also absent: NFIA, TSPAN33, PCAT7; maybe low, not absent |
| [[PDE3B]] | B | PDE3B activity raises TMTC4's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 1.53× lower at baseline in the lines without PDE3B | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[LRRC8D]] | C | LRRC8D activity raises TMTC4's level | lines that do not express LRRC8D (3) vs lines expressing it (47) | 2.73× lower at baseline in the lines without LRRC8D | 0.061 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PPFIBP2, USP31, EID2; maybe low, not absent |
| [[IRAK1]] | C | IRAK1's natural level strengthens TMTC4's drug response | IRAK1's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.01; direction clear | 0.064 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.805). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-8.4, -37.0); signed map (-3.9, -53.4). **Vector** length 82.0, 17.9% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.53 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | +3.3 | -3.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | -0.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +1.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +2.6 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.4 | +2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +0.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.7 | +0.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.2 | -26.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -11.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.1 | -26.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | -39.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -6.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.8 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane O-mannosyltransferase targeting cadherins 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.3 — chr13:100,603,625-100,675,093 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14624, FLJ22153 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Transmembrane O-mannosyltransferase targeting cadherins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T4D3](https://www.uniprot.org/uniprotkb/Q5T4D3) (Protein O-mannosyl-transferase TMTC4):

> Transfers mannosyl residues to the hydroxyl group of serine or threonine residues. The 4 members of the TMTC family are O-mannosyl-transferases dedicated primarily to the cadherin superfamily, each member seems to have a distinct role in decorating the cadherin domains with O-linked mannose glycans at specific regions. Also acts as O-mannosyl-transferase on other proteins such as PDIA3.

**Summary**, from NCBI Gene [84899](https://www.ncbi.nlm.nih.gov/gene/84899):

> This gene encodes a transmembrane protein that belongs to family of proteins containing an N-terminal transmembrane domain and a C-terminal tetratricopeptide repeat (TPR) domain. TPR domains mediate protein-protein interactions in various cellular processes, such as synaptic vesicle fusion, protein folding, and protein translocation. A pseudogene of this gene has been defined on chromosome 5. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:25904](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25904) · Entrez [84899](https://www.ncbi.nlm.nih.gov/gene/84899) · UniProt [Q5T4D3](https://www.uniprot.org/uniprotkb/Q5T4D3) · Ensembl [ENSG00000125247](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125247)

## Data

Gene col 4596: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4596); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4596, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4596]; `tensor/DDL_lfc|DDL_z.npy` [4596]; `embed/gene_vectors.npy` [4596]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4596 or target_col == 4596). Every well: [[TMTC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMTC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
