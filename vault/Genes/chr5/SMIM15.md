---
symbol: "SMIM15"
type: "gene"
col: 12042
ensembl_id: "ENSG00000188725"
name: "small integral membrane protein 15"
location: "5q12.1"
module: 7
arm: "+"
pooled_cpm: 47.51
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SMIM15

*small integral membrane protein 15* — 5q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.97× (z +11.0, q 2e-25, up in 40 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.70× (z +8.6, q 1e-15, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.674× (z -6.4, q 1e-07, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJA2]] (+0.66, fdr 7e-06), [[ZNF260]] (+0.66, fdr 1e-05), [[ZBTB33]] (+0.65, fdr 1e-05); moves opposite to [[GNRH1]] (-0.70, fdr 7e-06), [[STK32C]] (-0.65, fdr 1e-05), [[RAB40C]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12042.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.97×** | +11.0 | 2e-25 | 40/48 (A549, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.02×** | +11.0 | 2e-25 | 34/39 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +8.6 | 1e-15 | 43/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.61×** | +7.1 | 1e-10 | 33/45 (KATO III, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +7.0 | 3e-10 | 34/48 (A549, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +6.4 | 1e-08 | 38/48 (A549, PANC-1, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.44×** | +5.7 | 9e-07 | 32/48 (A549, A-172, …) | two highest doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +5.5 | 3e-06 | 30/47 (PANC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.36×** | +5.0 | 4e-05 | 27/48 (CFPAC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.35×** | +4.9 | 5e-05 | 27/48 (A549, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.32×** | +4.5 | 4e-04 | 25/48 (NCI-H2030, SW480, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.31×** | +4.4 | 4e-04 | 27/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +4.2 | 0.001 | 24/48 (A549, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.28×** | +4.1 | 0.002 | 22/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.59×** | +3.9 | 0.003 | 22/48 (NCI-H460, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.041 | 16/48 (NCI-H2030, HS-578T, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.047 | 13/48 (NCI-H1792, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.45×** | +3.1 | 0.051 | 14/48 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12042.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.674×** | -6.4 | 1e-07 | 30/48 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.753×** | -4.6 | 0.001 | 26/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.777×** | -4.1 | 0.009 | 24/48 (AsPC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.790×** | -3.8 | 0.020 | 22/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.861× | -3.4 | 0.071 | 20/48 (H4, NCI-H2347, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.752×** | -3.3 | 0.097 | 14/48 (HCT15, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.823× | -3.1 | 0.14 | 14/48 (A498, LoVo, …) | inconsistent across doses |  |
| [[Clofarabine (drug)]] 0.5 µM |  | 0.830× | -3.0 | 0.18 | 13/47 (KATO III, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12042. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 51.8 | 4 (3 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 2.97× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.427× (z -9.3) |
| [[A549 (line)]] | wt | 38.6 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.64× (z +8.5) | — |
| [[KATO III (line)]] | alt | 55.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 2.53× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Panobinostat (drug)]] 5 µM 0.291× (z -12.3) |
| [[A498 (line)]] | wt | 46.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.59× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[AsPC-1 (line)]] | alt | 81.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.367× (z -10.5) |
| [[HCT15 (line)]] | alt | 54.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Ipatasertib (drug)]] 0.5 µM 0.175× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 42.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 53.6 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.70× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 28.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 45.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.16× (z +8.5) | — |
| [[A-427 (line)]] | wt | 61.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[H4 (line)]] | wt | 51.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.41× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HT-29 (line)]] | alt | 40.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[LoVo (line)]] | wt | 70.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.413× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 25.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H23 (line)]] | alt | 37.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[SHP-77 (line)]] | alt | 45.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.16× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SNU-423 (line)]] | alt | 35.5 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.283× (z -9.9) |
| [[A-172 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 66.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12042), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJA2]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[ZNF260]] | +0.66 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[ZBTB33]] | +0.65 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[ZNF770]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[TRMT5]] | +0.63 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[LIG4]] | +0.62 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[CENPBD1P]] | +0.62 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[TFAM]] | +0.61 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[C17orf80]] | +0.60 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[ZNF518B]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[ZNF460]] | +0.59 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[UBQLN2]] | +0.59 | +0.46 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 9 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNRH1]] | -0.70 | -0.64 / -0.67 | both halves | 7e-06 |  |
| [[STK32C]] | -0.65 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[RAB40C]] | -0.63 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[MPND]] | -0.61 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[RPL37A]] ⚠ | -0.61 | -0.53 / -0.61 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL21]] ⚠ | -0.61 | -0.58 / -0.60 | both halves | 8e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPLP2]] | -0.60 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[KMT5C]] | -0.60 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[MAP3K3]] | -0.59 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[EFCAB14-AS1]] | -0.58 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[RPS3]] ⚠ | -0.58 | -0.47 / -0.56 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EEF1D]] | -0.58 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[RPL36]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[RPS21]] | -0.58 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[METRN]] | -0.57 | -0.37 / -0.55 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SMIM15's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.508). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-32.1, 13.9); signed map (2.9, -31.2). **Vector** length 85.0, 20.2% of its response variance represented; |z| ≥ 3 in 877 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.8 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +8.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +0.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.0 | +2.4 |
| fall | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -3.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.4 | -6.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.3 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.0 | -3.8 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.0 | -1.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | small integral membrane protein 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.1 — chr5:61,157,704-61,162,468 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP686E2158; previously C5orf43 |
| Matched by | ensembl_id |

UniProt [Q7Z3B0](https://www.uniprot.org/uniprotkb/Q7Z3B0) carries no function annotation.

**Summary**, from NCBI Gene [643155](https://www.ncbi.nlm.nih.gov/gene/643155):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33861](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33861) · Entrez [643155](https://www.ncbi.nlm.nih.gov/gene/643155) · UniProt [Q7Z3B0](https://www.uniprot.org/uniprotkb/Q7Z3B0) · Ensembl [ENSG00000188725](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188725)

## Data

Gene col 12042: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12042); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12042, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12042]; `tensor/DDL_lfc|DDL_z.npy` [12042]; `embed/gene_vectors.npy` [12042]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12042 or target_col == 12042). Every well: [[SMIM15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMIM15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
