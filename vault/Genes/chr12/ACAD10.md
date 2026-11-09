---
symbol: "ACAD10"
type: "gene"
col: 3213
ensembl_id: "ENSG00000111271"
name: "acyl-CoA dehydrogenase family member 10"
location: "12q24.12"
module: 54
arm: "+"
pooled_cpm: 33.42
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 27
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# ACAD10

*acyl-CoA dehydrogenase family member 10* — 12q24.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.55× (z +6.4, q 7e-08, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (16 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.378× (z -14.1, q 2e-42, down in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.498× (z -10.1, q 5e-22, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2J4]] (+0.69, fdr 7e-06), [[KIAA0319L]] (+0.68, fdr 7e-06), [[MRPL23]] (+0.64, fdr 1e-05); moves opposite to [[SEPTIN11]] (-0.64, fdr 1e-05), [[FAM171B]] (-0.63, fdr 2e-05), [[STK26]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3213.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +6.4 | 7e-08 | 31/48 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.46×** | +5.5 | 1e-05 | 33/48 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +4.3 | 0.003 | 24/48 (SW 900, HOP62, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.040 | 20/48 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.061 | 16/48 (SW 900, NCI-H2347, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.065 | 11/48 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.073 | 20/48 (SNU-423, NCI-H1792, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.2 | 0.089 | 10/48 (SW480, NCI-H1792, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.23× | +3.1 | 0.14 | 15/48 (LS 180, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3213.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.378×** | -14.1 | 2e-42 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.396×** | -13.5 | 7e-39 | 40/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.391×** | -13.1 | 6e-37 | 42/47 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.591×** | -10.8 | 7e-25 | 38/47 (SNU-423, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.498×** | -10.1 | 5e-22 | 43/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.488×** | -10.0 | 1e-21 | 40/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.513×** | -9.7 | 3e-20 | 38/45 (NCI-H23, A-427, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.505×** | -9.2 | 4e-18 | 33/41 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.545×** | -8.8 | 8e-17 | 42/48 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.581×** | -7.6 | 2e-12 | 34/46 (COLO 205, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.619×** | -7.0 | 2e-10 | 34/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.634×** | -6.6 | 2e-09 | 32/48 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.636×** | -6.5 | 3e-09 | 31/47 (A549, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.440×** | -6.2 | 2e-08 | 36/49 (PANC-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.653×** | -6.2 | 3e-08 | 28/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.680×** | -5.6 | 9e-07 | 25/48 (H4, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.497×** | -5.3 | 4e-06 | 29/47 (C32, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.716×** | -4.6 | 2e-04 | 23/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.797×** | -3.3 | 0.026 | 16/48 (NCI-H2030, HepG2/C3A, …) | rises with dose |  |
| [[Asciminib (drug)]] 0.05 µM |  | **0.800×** | -3.1 | 0.047 | 15/48 (Panc 03.27, A-172, …) | inconsistent across doses |  |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.809×** | -2.9 | 0.071 | 10/48 (LOX-IMVI, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3213. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 41.4 | 0 | 14 (12 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -16.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.274× (z -12.4) |
| [[PANC-1 (line)]] | alt | 49.5 | 0 | 12 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -18.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.235× (z -15.1) |
| [[H4 (line)]] | wt | 51.0 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -11.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.158× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 48.1 | 0 | 7 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.163× (z -13.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 36.6 | 0 | 6 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.233× (z -12.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 44.7 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.232× (z -12.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.306× (z -10.3) |
| [[SNU-423 (line)]] | alt | 31.0 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -14.8) ⚠ cell-cycle shift, explains ~60% of this change |
| [[SW480 (line)]] | alt | 35.4 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -17.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.196× (z -16.8) |
| [[A549 (line)]] | wt | 36.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -14.3) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.228× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 34.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0846× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[LoVo (line)]] | wt | 39.5 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -15.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.279× (z -12.1) |
| [[SHP-77 (line)]] | alt | 39.7 | 0 | 4 (3 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0750× (z -10.1) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.262× (z -10.0) |
| [[SW1417 (line)]] | alt | 25.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -11.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 31.8 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -9.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.260× (z -9.5) |
| [[CHP-212 (line)]] | wt | 46.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0422× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0741× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 32.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -13.1) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.380× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 55.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[A-172 (line)]] | wt | 27.1 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.230× (z -10.2) ⚠ toxic |
| [[C32 (line)]] | wt | 19.0 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0572× (z -8.7) |
| [[COLO 205 (line)]] | alt | 56.0 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.123× (z -15.4) ⚠ toxic |
| [[HCT15 (line)]] | alt | 39.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[J82 (line)]] | alt | 23.2 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.265× (z -9.9) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.305× (z -9.2) |
| [[KATO III (line)]] | alt | 51.2 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -11.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 41.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.218× (z -13.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -12.0) ⚠ toxic |
| [[SW 900 (line)]] | alt | 23.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -12.3) ⚠ cell-cycle shift, explains ~60% of this change |
| [[A-427 (line)]] | wt | 39.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[A498 (line)]] | wt | 25.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -14.2) ⚠ cell-cycle shift, explains ~60% of this change |
| [[AsPC-1 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -12.4) ⚠ cell-cycle shift, explains ~60% of this change |
| [[C-33 A (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.167× (z -11.1) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 23.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.237× (z -9.4) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 27.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.177× (z -9.4) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 30.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -9.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[RKO (line)]] | wt | 18.5 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0843× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3213), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2J4]] | +0.69 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[KIAA0319L]] | +0.68 | +0.66 / +0.63 | both halves | 7e-06 | STRING 560 |
| [[MRPL23]] | +0.64 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[CBY1]] | +0.62 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[ANKS3]] | +0.61 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[LUC7L]] | +0.60 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[PRKRIP1]] | +0.60 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[PIBF1]] | +0.59 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[TMEM258]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SF3B6]] | +0.59 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[ATG4B]] | +0.58 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[ZCCHC7]] | +0.58 | +0.38 / +0.55 | both halves | 6e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN11]] | -0.64 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[FAM171B]] | -0.63 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[STK26]] | -0.62 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[PGRMC1]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[YWHAZ]] | -0.54 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.53 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[MOB1A]] | -0.53 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[SEPTIN8]] | -0.52 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[OXCT1]] | -0.51 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[MAPRE1]] | -0.50 | -0.31 / -0.55 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.542). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.3, -14.1); signed map (-17.7, 0.6). **Vector** length 74.3, 18.3% of its response variance represented; |z| ≥ 3 in 1,154 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +5.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.2 | +6.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.8 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +0.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | +1.7 | +1.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | +0.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.6 | -9.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.4 | -0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -2.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA dehydrogenase family member 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.12 — chr12:111,686,053-111,757,107 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5601 |
| Gene groups (HGNC) | Acyl-CoA dehydrogenase family; Flavoproteins |
| Reactome | 3 pathways, smallest: Mitochondrial Fatty Acid Beta-Oxidation; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6JQN1](https://www.uniprot.org/uniprotkb/Q6JQN1) (Acyl-CoA dehydrogenase family member 10):

> Functions as an atypical mitochondrial acyl-CoA dehydrogenase (ACAD) that contributes to the catabolism of 4-hydroxy fatty acyl-CoAs by catalyzing their conversion into 4-hydroxy-trans-2-enoyl-CoA intermediates compatible with beta-oxidation. The underlying mechanism is proposed to involve sequential enzymatic steps including ATP-dependent phosphorylation of the 4-hydroxy group to form 4-phosphohydroxyacyl-CoA (such as 4-phosphohexanoyl-CoA), and subsequent conversion into trans-2-enoyl-CoAs …

**Summary**, from NCBI Gene [80724](https://www.ncbi.nlm.nih.gov/gene/80724):

> This gene encodes a member of the acyl-CoA dehydrogenase family of enzymes (ACADs), which participate in the beta-oxidation of fatty acids in mitochondria. The encoded enzyme contains a hydrolase domain at the N-terminal portion, a serine/threonine protein kinase catlytic domain in the central region, and a conserved ACAD domain at the C-terminus. Several alternatively spliced transcript variants of this gene have been described, but the full-length nature of some of these variants has not been …

**Accessions** — [HGNC:21597](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21597) · Entrez [80724](https://www.ncbi.nlm.nih.gov/gene/80724) · UniProt [Q6JQN1](https://www.uniprot.org/uniprotkb/Q6JQN1) · Ensembl [ENSG00000111271](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111271)

## Data

Gene col 3213: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3213); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3213, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3213]; `tensor/DDL_lfc|DDL_z.npy` [3213]; `embed/gene_vectors.npy` [3213]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3213 or target_col == 3213). Every well: [[ACAD10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACAD10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
