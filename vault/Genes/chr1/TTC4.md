---
symbol: "TTC4"
type: "gene"
col: 14375
ensembl_id: "ENSG00000243725"
name: "tetratricopeptide repeat domain 4"
location: "1p32.3"
module: 7
arm: "+"
pooled_cpm: 20.38
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 4
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TTC4

*tetratricopeptide repeat domain 4* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (7 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.37× (z +18.6, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.636× (z -9.8, q 6e-20, down in 28 of 42 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 0.325×, A-427 0.207×, HCT15 0.180×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H23 0.199×, SW1417 0.173×, PANC-1 0.458×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 0.255×, HEC-1-A 0.154×; ⚠ toxic; transcription drop); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (AsPC-1 0.165×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TATDN1]] (+0.73, fdr 7e-06), [[ABRAXAS2]] (+0.68, fdr 7e-06), [[DNTTIP2]] (+0.68, fdr 7e-06); moves opposite to [[SLC25A23]] (-0.60, fdr 1e-05), [[NPTN]] (-0.55, fdr 7e-06), [[AGPAT1]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SCML1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14375.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.37×** | +18.6 | 0e+00 | 42/48 (HOP62, KATO III, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.41×** | +17.9 | 0e+00 | 40/48 (HOP62, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.13×** | +16.3 | 0e+00 | 42/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.08×** | +15.7 | 0e+00 | 41/47 (KATO III, HOP62, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +11.1 | 1e-26 | 26/47 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +10.9 | 9e-26 | 31/44 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.65×** | +10.8 | 4e-25 | 38/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.57×** | +9.7 | 3e-20 | 31/48 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +9.1 | 7e-18 | 26/47 (A498, C32, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.21×** | +8.9 | 3e-17 | 29/40 (HOP62, KATO III, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +8.2 | 1e-14 | 26/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +7.9 | 1e-13 | 26/47 (NCI-H1573, SW 900, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +7.6 | 1e-12 | 26/47 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.39×** | +7.1 | 4e-11 | 23/48 (SW480, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +6.8 | 5e-10 | 18/48 (PANC-1, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +6.7 | 8e-10 | 23/47 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +6.3 | 1e-08 | 21/48 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.45×** | +5.7 | 3e-07 | 17/48 (HOP62, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.25×** | +4.7 | 6e-05 | 15/47 (A498, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14375.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 0.325×, A-427 0.207×, HCT15 0.180×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H23 0.199×, SW1417 0.173×, PANC-1 0.458×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (PANC-1 0.255×, HEC-1-A 0.154×; ⚠ toxic; transcription drop); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (AsPC-1 0.165×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.636×** | -9.8 | 6e-20 | 28/42 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.678×** | -8.1 | 1e-13 | 18/32 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.756×** | -5.6 | 4e-06 | 17/39 (NCI-H23, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.793×** | -5.0 | 6e-05 | 13/47 (hTERT-HPNE, SW 1088, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.953× | -3.8 | 0.014 | 2/48 (MIA PaCa-2, SW 1271) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14375. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 29.7 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.41× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.255× (z -16.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 14.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.76× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 22.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.45× (z +13.1) | — |
| [[KATO III (line)]] | alt | 18.8 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.93× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 15.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +10.3) | — |
| [[LoVo (line)]] | wt | 15.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.28× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 19.4 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +8.7) | — |
| [[A-427 (line)]] | wt | 25.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -13.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 10.9 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.165× (z -10.2) |
| [[C-33 A (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.206× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -10.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -14.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 12.3 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.60× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 14.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.22× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 34.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -13.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.138× (z -9.3) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 23.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.110× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -12.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14375), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TATDN1]] | +0.73 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[ABRAXAS2]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[DNTTIP2]] | +0.68 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[C12orf43]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[POLR3F]] | +0.66 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[ZC3HC1]] | +0.66 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[MRM3]] | +0.66 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[PSMD7]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[C19orf12]] | +0.64 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[SDHAF2]] | +0.63 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[ZNF197]] | +0.63 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[RPAP1]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A23]] | -0.60 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[NPTN]] | -0.55 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[AGPAT1]] | -0.55 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[PRKACA]] | -0.55 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[GGH]] | -0.54 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[TWSG1]] | -0.54 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[TXNDC16]] | -0.53 | -0.39 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCML1]] | C | SCML1 activity lowers TTC4's level | lines that do not express SCML1 (3) vs lines expressing it (47) | 1.66× higher at baseline in the lines without SCML1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: LHFPL2, SESTD1, HIPK2; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.578). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-42.1, 8.7); signed map (-3.8, -23.2). **Vector** length 95.2, 20.9% of its response variance represented; |z| ≥ 3 in 1,019 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.6 | +17.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.2 | +15.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.4 | +18.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.2 | +9.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.1 | +10.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.6 | +4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +9.1 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -1.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.8 | -9.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -3.5 | -0.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | +1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.7 | -0.8 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.6 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:54,715,861-54,742,657 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5097, FLJ41930, CNS1 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O95801](https://www.uniprot.org/uniprotkb/O95801) (Hsp70/Hsp90 co-chaperone CNS1 homolog):

> Co-chaperone that recruits molecular chaperones Hsp90 (HSC82 and HSP82) and Hsp70 (SSA1) to nascent polypeptides, facilitating their proper folding into functional proteins. Client proteins include eukaryotic elongation factor eEF2, a key player in cellular translation. Stimulates SSA1 ATPase activity, but not Hsp90 ATPase activity (By similarity). Promotes Sendai virus (SeV)-induced host cell innate immune responses.

**Summary**, from NCBI Gene [7268](https://www.ncbi.nlm.nih.gov/gene/7268):

> This gene encodes a protein that contains tetratricopeptide (TPR) repeats, which often mediate protein-protein interactions and chaperone activity. The encoded protein interacts with heat shock proteins 70 and 90. Alternative splicing results in multiple transcript variants. Naturally-occuring readthrough transcription occurs from upstream gene MROH (maestro heat-like repeat family member 7) to this gene. [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:12394](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12394) · Entrez [7268](https://www.ncbi.nlm.nih.gov/gene/7268) · UniProt [O95801](https://www.uniprot.org/uniprotkb/O95801) · Ensembl [ENSG00000243725](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243725)

## Data

Gene col 14375: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14375); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14375, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14375]; `tensor/DDL_lfc|DDL_z.npy` [14375]; `embed/gene_vectors.npy` [14375]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14375 or target_col == 14375). Every well: [[TTC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
