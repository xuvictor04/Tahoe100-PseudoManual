---
symbol: "POLG"
type: "gene"
col: 6423
ensembl_id: "ENSG00000140521"
name: "DNA polymerase gamma, catalytic subunit"
location: "15q26.1"
module: 52
arm: "+"
pooled_cpm: 47.74
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# POLG

*DNA polymerase gamma, catalytic subunit* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.48× (z +9.8, q 4e-20, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.471× (z -13.4, q 3e-38, down in 42 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.804× (z -5.5, q 5e-06, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SKI]] (+0.64, fdr 9e-06), [[SHPK]] (+0.63, fdr 1e-05), [[SLC25A19]] (+0.59, fdr 1e-05); moves opposite to [[ATP6V1C1]] (-0.60, fdr 1e-05), [[HINT3]] (-0.58, fdr 3e-05), [[VPS41]] (-0.53, fdr 1e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SLC1A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6423.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +9.8 | 4e-20 | 35/48 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +9.0 | 9e-17 | 33/48 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +8.6 | 1e-15 | 38/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +7.4 | 2e-11 | 35/48 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.31×** | +4.8 | 2e-04 | 27/48 (SW480, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +4.4 | 0.001 | 24/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.2 | 0.002 | 0/49 | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.5 | 0.035 | 17/48 (HS-578T, AsPC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.38× | +3.0 | 0.16 | 13/49 (NCI-H2030, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6423.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.471×** | -13.4 | 3e-38 | 42/49 (RKO, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.471×** | -12.9 | 9e-36 | 33/40 (RPMI-7951, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.469×** | -12.5 | 2e-33 | 39/44 (HCT15, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.804×** | -5.5 | 5e-06 | 25/48 (NCI-H1792, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.762×** | -4.7 | 3e-04 | 23/47 (NCI-H1573, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.769×** | -4.5 | 6e-04 | 24/48 (NCI-H1573, SW 1271, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.775×** | -4.4 | 9e-04 | 23/47 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.783×** | -4.4 | 9e-04 | 21/47 (NCI-H1573, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.796×** | -4.1 | 0.003 | 21/48 (NCI-H1573, A498, …) | two highest doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.828×** | -3.4 | 0.041 | 14/48 (SNU-423, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -3.2 | 0.064 | 16/48 (SW 900, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6423. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 68.3 | 14 | 3 (3 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 3.96× (z +13.7) | [[Digitoxin (drug)]] 5 µM 0.308× (z -11.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 64.1 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.155× (z -18.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 47.1 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.425× (z -9.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 69.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +18.5) | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -12.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 42.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 47.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.377× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 42.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -10.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 61.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -13.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 44.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -12.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 60.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -19.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 55.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.223× (z -13.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 50.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 61.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 33.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -10.5) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 45.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -13.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 55.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -14.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 73.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0421× (z -26.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 50.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -12.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 34.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.287× (z -9.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 37.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -11.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 38.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -10.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 42.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.277× (z -10.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 46.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -12.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 46.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.3) | — |
| [[CHP-212 (line)]] | wt | 35.7 | 0 | 1 | — | [[Saquinavir (drug)]] 5 µM 0.197× (z -9.2) |
| [[H4 (line)]] | wt | 47.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -9.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 51.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0838× (z -17.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 53.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -8.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 56.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -9.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 36.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 39.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +12.1) | — |
| [[SNU-423 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -8.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 47.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -9.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 59.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -10.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 70.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6423), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKI]] | +0.64 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[SHPK]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[SLC25A19]] | +0.59 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[NDEL1]] | +0.59 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[SMIM41]] | +0.57 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[SLC10A3]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[A3GALT2]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ZNF275]] | +0.57 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[ATG101]] | +0.56 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[SLC16A3]] | +0.56 | +0.48 / +0.55 | both halves | 2e-05 | same gene group |
| [[PYGM]] | +0.56 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SAP30BP]] | +0.55 | +0.60 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1C1]] | -0.60 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[HINT3]] | -0.58 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[VPS41]] | -0.53 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[CHIC1]] | -0.52 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[RBM41]] | -0.52 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[BBOX1-AS1]] | -0.51 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[CEBPZOS]] | -0.51 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[LRP1B]] | -0.51 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ZNF326]] | -0.50 | -0.31 / -0.61 | both halves | 2e-04 |  |
| [[RPS6KA6]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[NTPCR]] | -0.49 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[TMEM126B]] | -0.49 | -0.37 / -0.49 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC1A1]] | B | SLC1A1 activity raises POLG's level | lines that do not express SLC1A1 (11) vs lines expressing it (39) | 1.30× lower at baseline in the lines without SLC1A1 | 0.058 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent |
| [[MYO1E]] | B | MYO1E activity raises POLG's level | lines that do not express MYO1E (5) vs lines expressing it (45) | 1.33× lower at baseline in the lines without MYO1E | 0.068 | ⚠ within organs, on part of the lines; also absent: FLNB, SMOX, TRIM38; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers POLG's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ATP8B3]] | B | ATP8B3 activity raises POLG's level | lines that do not express ATP8B3 (5) vs lines expressing it (45) | 1.19× lower at baseline in the lines without ATP8B3 | 0.088 | ⚠ within organs, on part of the lines; also absent: CEP85L, PARP3, SOAT1; maybe low, not absent |
| [[NIBAN2]] | B | NIBAN2 activity raises POLG's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 1.25× lower at baseline in the lines without NIBAN2 | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[RPS6KA6]] | B | RPS6KA6 activity raises POLG's level | lines that do not express RPS6KA6 (21) vs lines expressing it (29) | 1.08× lower at baseline in the lines without RPS6KA6 | 0.097 | ⚠ within organs, on part of the lines; also absent: VWDE, SCN9A, MIR9-3HG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.571). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (18.9, -16.3); signed map (-21.5, 41.7). **Vector** length 108, 28.1% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +9.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.4 | +2.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +8.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.1 | +4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | +9.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.3 | +2.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.3 | +1.2 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.0 | +2.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.4 | -12.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.0 | -5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.6 | -13.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.5 | -4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -12.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.1 | -4.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.4 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -2.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase gamma, catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:89,305,198-89,334,861 (-) |
| Ensembl biotype | protein_coding |
| Also known as | POLG1, POLGA |
| Gene groups (HGNC) | DNA polymerases; MicroRNA protein coding host genes |
| Reactome | 9 pathways, smallest: Strand-asynchronous mitochondrial DNA replication; TBC/RABGAPs; Potential therapeutics for SARS |
| Matched by | ensembl_id |

**Function**, from UniProt [P54098](https://www.uniprot.org/uniprotkb/P54098) (DNA polymerase subunit gamma-1):

> Catalytic subunit of DNA polymerase gamma solely responsible for replication of mitochondrial DNA (mtDNA). Replicates both heavy and light strands of the circular mtDNA genome using a single-stranded DNA template, RNA primers and the four deoxyribonucleoside triphosphates as substrates. Has 5' -> 3' polymerase activity. Functionally interacts with TWNK and SSBP1 at the replication fork to form a highly processive replisome, where TWNK unwinds the double-stranded DNA template prior to …

**Summary**, from NCBI Gene [5428](https://www.ncbi.nlm.nih.gov/gene/5428):

> Mitochondrial DNA polymerase is heterotrimeric, consisting of a homodimer of accessory subunits plus a catalytic subunit. The protein encoded by this gene is the catalytic subunit of mitochondrial DNA polymerase. The encoded protein contains a polyglutamine tract near its N-terminus that may be polymorphic. Defects in this gene are a cause of progressive external ophthalmoplegia with mitochondrial DNA deletions 1 (PEOA1), sensory ataxic neuropathy dysarthria and ophthalmoparesis (SANDO), …

**Accessions** — [HGNC:9179](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9179) · Entrez [5428](https://www.ncbi.nlm.nih.gov/gene/5428) · UniProt [P54098](https://www.uniprot.org/uniprotkb/P54098) · Ensembl [ENSG00000140521](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140521)

## Data

Gene col 6423: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6423); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6423, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6423]; `tensor/DDL_lfc|DDL_z.npy` [6423]; `embed/gene_vectors.npy` [6423]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6423 or target_col == 6423). Every well: [[POLG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
