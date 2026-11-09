---
symbol: "ZNF26"
type: "gene"
col: 12583
ensembl_id: "ENSG00000198393"
name: "zinc finger protein 26"
location: "12q24.33"
module: 83
arm: "+"
pooled_cpm: 53.81
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# ZNF26

*zinc finger protein 26* — 12q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.49× (z +10.6, q 2e-23, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.547× (z -9.9, q 2e-20, down in 41 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 0.748× (z -3.3, q 0.092, down in 20 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (MIA PaCa-2 0.159×, NCI-H460 0.351×, J82 0.284×, A549 0.301×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H23 0.151×, A549 0.244×, hTERT-HPNE 0.200×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.147×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.489×); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1271 0.0908×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KANSL1L-AS1]] (+0.72, fdr 7e-06), [[TEX22]] (+0.71, fdr 7e-06), [[DHX34]] (+0.67, fdr 7e-06); moves opposite to [[CAT]] (-0.60, fdr 2e-05), [[ALAD]] (-0.58, fdr 4e-05), [[HMGN3]] (-0.58, fdr 5e-05).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TSPAN15]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12583.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.49×** | +10.6 | 2e-23 | 45/49 (COLO 205, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +8.5 | 4e-15 | 39/48 (Hs 766T, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.30×** | +7.1 | 3e-10 | 38/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +6.5 | 1e-08 | 33/48 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +6.0 | 3e-07 | 27/48 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +5.9 | 3e-07 | 29/48 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +4.3 | 0.002 | 20/48 (SNU-1, NCI-H2347, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.010 | 22/48 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.012 | 24/48 (NCI-H460, SHP-77, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.3 | 0.046 | 17/36 (NCI-H2030, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.21×** | +3.1 | 0.079 | 16/48 (NCI-H460, CHP-212, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.079 | 19/48 (SW480, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.086 | 12/48 (LOX-IMVI, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12583.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (MIA PaCa-2 0.159×, NCI-H460 0.351×, J82 0.284×, A549 0.301×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H23 0.151×, A549 0.244×, hTERT-HPNE 0.200×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.147×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.489×); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1271 0.0908×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.547×** | -9.9 | 2e-20 | 41/48 (MIA PaCa-2, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.604×** | -8.0 | 5e-13 | 28/42 (NCI-H23, A549, …) | two highest doses | cell-cycle shift (explains ~15% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.653×** | -6.7 | 3e-09 | 39/47 (MIA PaCa-2, BT-474, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **0.801×** | -3.6 | 0.038 | 22/48 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.748×** | -3.3 | 0.092 | 20/47 (SHP-77, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.874× | -3.1 | 0.16 | 15/48 (RKO, AsPC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12583. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 67.8 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.34× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 91.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.151× (z -20.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 85.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -16.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 42.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -10.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 64.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 42.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -12.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 46.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 13.3× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 50.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -9.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 40.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +11.6) | — |
| [[NCI-H1792 (line)]] | alt | 47.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -9.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 87.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.441× (z -9.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 138 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -10.9) |
| [[SNU-423 (line)]] | alt | 68.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -11.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 45.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -10.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 53.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -11.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 40.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 39.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -10.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 78.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -12.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -9.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 34.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.240× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 34.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 90.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 68.8 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0908× (z -8.9) |
| [[SW480 (line)]] | alt | 51.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.49× (z +9.0) | — |
| [[A-172 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 63.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 66.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12583), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KANSL1L-AS1]] | +0.72 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[TEX22]] | +0.71 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[DHX34]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[POLR1C]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ACAD9]] | +0.67 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[P2RY11]] | +0.66 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TRNT1]] | +0.65 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[HCG18]] | +0.65 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[PIGG]] | +0.64 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[MSANTD2]] | +0.64 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[ALG8]] | +0.64 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[UBAP1L]] | +0.64 | +0.58 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAT]] | -0.60 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[ALAD]] | -0.58 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[HMGN3]] | -0.58 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[HPF1]] | -0.57 | -0.37 / -0.44 | both halves | 9e-05 |  |
| [[MPP1]] | -0.56 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[TMEM14A]] | -0.56 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[OSBPL9]] | -0.55 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[PLEKHH3]] | -0.55 | -0.55 / -0.37 | both halves | 9e-05 |  |
| [[ROGDI]] | -0.54 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[MAPRE2]] | -0.54 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[CDC14B]] | -0.53 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[PAFAH1B3]] | -0.52 | -0.42 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN15]] | B | TSPAN15 activity lowers ZNF26's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 1.47× higher at baseline in the lines without TSPAN15 | 0.065 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ZNF26's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.668). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (18.2, -0.3); signed map (15.0, 1.1). **Vector** length 105, 27.1% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +8.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.6 | +10.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +6.5 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +1.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.6 | +1.9 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.2 | -6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -2.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -0.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.33 — chr12:132,986,365-133,032,952 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KOX20, FLJ20755 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P17031](https://www.uniprot.org/uniprotkb/P17031) (Zinc finger protein 26):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7574](https://www.ncbi.nlm.nih.gov/gene/7574):

> Predicted to enable DNA binding activity and zinc ion binding activity. Predicted to be involved in DNA-templated transcription and regulation of DNA-templated transcription. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13053](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13053) · Entrez [7574](https://www.ncbi.nlm.nih.gov/gene/7574) · UniProt [P17031](https://www.uniprot.org/uniprotkb/P17031) · Ensembl [ENSG00000198393](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198393)

## Data

Gene col 12583: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12583); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12583, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12583]; `tensor/DDL_lfc|DDL_z.npy` [12583]; `embed/gene_vectors.npy` [12583]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12583 or target_col == 12583). Every well: [[ZNF26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
