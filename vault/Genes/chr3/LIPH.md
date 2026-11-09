---
symbol: "LIPH"
type: "gene"
col: 8802
ensembl_id: "ENSG00000163898"
name: "lipase H"
location: "3q27.2"
module: 31
arm: "+"
pooled_cpm: 49.25
n_lines_expressing: 23
n_dd_up: 18
n_dd_down: 15
n_dd_up_clean: 15
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 106
direction_downstream: 117
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# LIPH

*lipase H* — 3q27.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.70× (z +17.1, q 0e+00, up in 6 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.85× (z +11.8, q 6e-30, up in 13 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.467× (z -10.3, q 4e-22, down in 21 of 21 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.623× (z -6.4, q 5e-08, down in 16 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYP3A5]] (+0.74, fdr 7e-06), [[TMPRSS4]] (+0.74, fdr 7e-06), [[CLDN4]] (+0.68, fdr 7e-06); moves opposite to [[ZNF25]] (-0.53, fdr 3e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 106 arrows point to it, the strongest [[GPRC5A]] → it (grade B ⚠); 117 go from it, the strongest it → [[RDH13]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8802.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.70×** | +17.1 | 0e+00 | 6/19 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.89×** | +14.4 | 1e-44 | 6/22 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +11.8 | 6e-30 | 13/21 (BT-474, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.35×** | +10.8 | 8e-25 | 2/19 (HEC-1-A, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +7.3 | 4e-11 | 16/22 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +6.4 | 2e-08 | 7/21 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +5.6 | 2e-06 | 13/21 (BT-474, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +5.2 | 2e-05 | 8/21 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +4.9 | 5e-05 | 11/21 (AsPC-1, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +4.6 | 3e-04 | 5/21 (HEC-1-A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.56×** | +4.3 | 9e-04 | 2/21 (HEC-1-A, LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +4.2 | 0.001 | 5/21 (NCI-H460, BT-474, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.37×** | +4.2 | 0.001 | 0/22 | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.001 | 3/21 (NCI-H460, BT-474, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.007 | 6/21 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.013 | 0/21 | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.021 | 5/21 (HEC-1-A, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 1.18× | +3.2 | 0.036 | 3/22 (Panc 03.27, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8802.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.467×** | -10.3 | 4e-22 | 21/21 (NCI-H460, CFPAC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.623×** | -6.4 | 5e-08 | 16/21 (PANC-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.497×** | -4.9 | 1e-04 | 18/21 (CFPAC-1, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.787×** | -4.5 | 9e-04 | 7/21 (LoVo, NCI-H1792, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.548×** | -4.3 | 0.002 | 18/21 (KATO III, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.716×** | -4.2 | 0.003 | 8/21 (LoVo, PANC-1, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.730×** | -4.1 | 0.004 | 16/21 (HT-29, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.568×** | -4.0 | 0.004 | 14/21 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.744×** | -4.0 | 0.004 | 15/21 (NCI-H1573, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.758×** | -3.7 | 0.010 | 15/21 (COLO 205, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.759×** | -3.7 | 0.010 | 11/21 (LS 180, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.926× | -3.7 | 0.010 | 1/22 (NCI-H1792) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.824×** | -3.7 | 0.010 | 21/22 (HT-29, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.770×** | -3.7 | 0.010 | 12/22 (NCI-H1792, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.689×** | -3.6 | 0.013 | 10/21 (NCI-H460, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.768×** | -3.3 | 0.035 | 0/21 | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.845× | -3.1 | 0.066 | 11/21 (NCI-H460, LoVo, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8802. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 208 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -15.0) |
| [[CFPAC-1 (line)]] | alt | 251 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 231 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -16.8) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.193× (z -14.7) |
| [[COLO 205 (line)]] | alt | 240 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -21.7) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 34.3 | 5 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.54× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 2.18× (z +9.0) | [[Lonafarnib (drug)]] 5 µM 0.125× (z -8.8) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 190 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -27.4) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.312× (z -10.2) |
| [[LS 180 (line)]] | wt | 180 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.295× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 29.0 | 1 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.39× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.120× (z -15.5) ⚠ unreliable plate only · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -11.3) |
| [[SW48 (line)]] | wt | 88.9 | 0 | 5 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0646× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -11.4) |
| [[KATO III (line)]] | alt | 239 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.235× (z -11.9) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 69.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -10.5) |
| [[PANC-1 (line)]] | alt | 28.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.289× (z -9.1) |
| [[A549 (line)]] | wt | 45.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 71.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -10.0) |
| [[BT-474 (line)]] | alt | 36.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.14× (z +10.8) | — |
| [[NCI-H2347 (line)]] | alt | 46.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.333× (z -8.8) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 42.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.284× (z -9.1) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 5.13 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.34 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.90 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.49 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.33 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.18 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.95 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.66 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.27 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.32 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.46 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.91 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.17 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.89 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.90 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.31 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.12 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.67 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.40 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.33 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.15 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8802), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP3A5]] | +0.74 | +0.62 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[TMPRSS4]] | +0.74 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[CLDN4]] | +0.68 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[EPS8L1]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[TMEM45B]] | +0.68 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[CDH1]] | +0.67 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[JUP]] | +0.67 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[SDR16C5]] | +0.66 | +0.62 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[INAVA]] | +0.65 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[CLIC5]] | +0.65 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[C1orf116]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[RDH13]] | +0.64 | +0.67 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF25]] | -0.53 | -0.55 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*106 arrows, 106 of them with an alert ⚠; grade A 0, B 12, C 94. Shown: the 12 strongest; 94 more arrows (94 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRC5A]] | B | GPRC5A activity raises LIPH's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 4.47× lower at baseline in the lines without GPRC5A | 0.015 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[PLEKHG1]] | B | PLEKHG1 activity raises LIPH's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 3.34× lower at baseline in the lines without PLEKHG1 | 0.019 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[NOSTRIN]] | B | NOSTRIN activity raises LIPH's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 3.71× lower at baseline in the lines without NOSTRIN | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[RAB27B]] | B | RAB27B activity raises LIPH's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 3.51× lower at baseline in the lines without RAB27B | 0.025 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[LINC00589]] | B | LINC00589 activity raises LIPH's level | lines that do not express LINC00589 (28) vs lines expressing it (22) | 2.83× lower at baseline in the lines without LINC00589 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00520, ENSG00000267881, TSPAN8 |
| [[TNFRSF21]] | B | TNFRSF21 activity raises LIPH's level | lines that do not express TNFRSF21 (15) vs lines expressing it (35) | 3.97× lower at baseline in the lines without TNFRSF21 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000256982, SORL1, THRB; maybe low, not absent |
| [[BICDL2]] | B | BICDL2 activity raises LIPH's level | lines that do not express BICDL2 (22) vs lines expressing it (28) | 3.11× lower at baseline in the lines without BICDL2 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRYBG2, MAL2, TNNT2; maybe low, not absent |
| [[CD55]] | B | CD55 activity raises LIPH's level | lines that do not express CD55 (16) vs lines expressing it (34) | 3.47× lower at baseline in the lines without CD55 | 0.040 | ⚠ within organs, on part of the lines; also absent: IL32, IL2RG, ENSG00000271933; maybe low, not absent |
| [[PCDH1]] | B | PCDH1 activity raises LIPH's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 3.12× lower at baseline in the lines without PCDH1 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[GAREM1]] | B | GAREM1 activity raises LIPH's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 3.99× lower at baseline in the lines without GAREM1 | 0.044 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[MYO1D]] | B | MYO1D activity raises LIPH's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 2.45× lower at baseline in the lines without MYO1D | 0.087 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[SDCBP2]] | B | SDCBP2 activity raises LIPH's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 3.42× lower at baseline in the lines without SDCBP2 | 0.091 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |

### Downstream of this gene

*117 arrows, 117 of them with an alert ⚠; grade A 0, B 39, C 78. Shown: the 12 strongest; 105 more arrows (105 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RDH13]] | B | LIPH activity raises RDH13's level | lines that do not express LIPH (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without LIPH | 7e-04 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[GPRC5A]] | B | LIPH activity raises GPRC5A's level | lines that do not express LIPH (27) vs lines expressing it (23) | 4.66× lower at baseline in the lines without LIPH | 0.001 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[EPS8L1]] | B | LIPH activity raises EPS8L1's level | lines that do not express LIPH (27) vs lines expressing it (23) | 3.50× lower at baseline in the lines without LIPH | 0.001 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[TNFRSF21]] | B | LIPH activity raises TNFRSF21's level | lines that do not express LIPH (27) vs lines expressing it (23) | 3.55× lower at baseline in the lines without LIPH | 0.004 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[TCF7L2]] | B | LIPH activity raises TCF7L2's level | lines that do not express LIPH (27) vs lines expressing it (23) | 2.09× lower at baseline in the lines without LIPH | 0.011 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[BAIAP2L1]] | B | LIPH activity raises BAIAP2L1's level | lines that do not express LIPH (27) vs lines expressing it (23) | 2.83× lower at baseline in the lines without LIPH | 0.011 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[CD55]] | B | LIPH activity raises CD55's level | lines that do not express LIPH (27) vs lines expressing it (23) | 3.36× lower at baseline in the lines without LIPH | 0.012 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[GAREM1]] | B | LIPH activity raises GAREM1's level | lines that do not express LIPH (27) vs lines expressing it (23) | 2.86× lower at baseline in the lines without LIPH | 0.014 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[NOSTRIN]] | B | LIPH activity raises NOSTRIN's level | lines that do not express LIPH (27) vs lines expressing it (23) | 2.75× lower at baseline in the lines without LIPH | 0.014 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[BICDL2]] | B | LIPH activity raises BICDL2's level | lines that do not express LIPH (27) vs lines expressing it (23) | 3.34× lower at baseline in the lines without LIPH | 0.015 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[UBE2H]] | B | LIPH activity raises UBE2H's level | lines that do not express LIPH (27) vs lines expressing it (23) | 1.56× lower at baseline in the lines without LIPH | 0.018 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[EZR]] | B | LIPH activity raises EZR's level | lines that do not express LIPH (27) vs lines expressing it (23) | 2.57× lower at baseline in the lines without LIPH | 0.018 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.726). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.8, 55.8); signed map (57.4, 8.2). **Vector** length 96.1, 34.1% of its response variance represented; |z| ≥ 3 in 718 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.3 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +14.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +17.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +10.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +0.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.9 | +3.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.2 | -10.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.0 | -4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -4.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.9 | -4.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | lipase H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.2 — chr3:185,506,262-185,552,588 (-) |
| Ensembl biotype | protein_coding |
| Also known as | mPA-PLA1, PLA1B, mPA-PLA1alpha, LPDLR |
| Gene groups (HGNC) | Lipases |
| Reactome | 4 pathways, smallest: Synthesis of PA; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWY8](https://www.uniprot.org/uniprotkb/Q8WWY8) (Lipase member H):

> Hydrolyzes specifically phosphatidic acid (PA) to produce 2-acyl lysophosphatidic acid (LPA; a potent bioactive lipid mediator) and fatty acid. Does not hydrolyze other phospholipids, like phosphatidylserine (PS), phosphatidylcholine (PC) and phosphatidylethanolamine (PE) or triacylglycerol (TG).

**Summary**, from NCBI Gene [200879](https://www.ncbi.nlm.nih.gov/gene/200879):

> This gene encodes a membrane-bound member of the mammalian triglyceride lipase family. It catalyzes the production of 2-acyl lysophosphatidic acid (LPA), which is a lipid mediator with diverse biological properties that include platelet aggregation, smooth muscle contraction, and stimulation of cell proliferation and motility. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18483](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18483) · Entrez [200879](https://www.ncbi.nlm.nih.gov/gene/200879) · UniProt [Q8WWY8](https://www.uniprot.org/uniprotkb/Q8WWY8) · Ensembl [ENSG00000163898](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163898)

## Data

Gene col 8802: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8802); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8802, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8802]; `tensor/DDL_lfc|DDL_z.npy` [8802]; `embed/gene_vectors.npy` [8802]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8802 or target_col == 8802). Every well: [[LIPH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIPH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
