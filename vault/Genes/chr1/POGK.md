---
symbol: "POGK"
type: "gene"
col: 6686
ensembl_id: "ENSG00000143157"
name: "pogo transposable element derived with KRAB domain"
location: "1q24.1"
module: 1
arm: "+"
pooled_cpm: 27.85
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# POGK

*pogo transposable element derived with KRAB domain* — 1q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.42× (z +6.7, q 1e-08, up in 31 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.31× (z +4.9, q 3e-04, up in 19 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.453× (z -21.1, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFRD2]] (+0.76, fdr 7e-06), [[COA7]] (+0.76, fdr 7e-06), [[RIOX2]] (+0.76, fdr 7e-06); moves opposite to [[NARF]] (-0.68, fdr 7e-06), [[ZNF654]] (-0.68, fdr 9e-06), [[SAP30-DT]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6686.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +6.7 | 1e-08 | 31/47 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +4.9 | 3e-04 | 19/48 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +4.3 | 0.003 | 19/48 (BT-474, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.2 | 0.004 | 0/48 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.27×** | +4.1 | 0.004 | 13/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.25×** | +4.0 | 0.007 | 17/45 (LOX-IMVI, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.009 | 9/46 (A498, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.015 | 14/47 (NCI-H460, NCI-H2347, …) | top dose only |  |
| [[Erlotinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.14 | 8/47 (COLO 205, SW480, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.14 | 1/48 (MIA PaCa-2) | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.14 | 10/47 (RPMI-7951, PANC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6686.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.453×** | -21.1 | 0e+00 | 45/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.472×** | -14.2 | 3e-43 | 38/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.551×** | -11.3 | 3e-27 | 36/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.551×** | -11.3 | 3e-27 | 33/46 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.595×** | -9.8 | 1e-20 | 31/47 (KATO III, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.595×** | -9.4 | 3e-19 | 30/46 (MIA PaCa-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.619×** | -9.0 | 1e-17 | 38/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.628×** | -8.5 | 2e-15 | 31/48 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.665×** | -7.7 | 8e-13 | 27/47 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.515×** | -6.6 | 3e-09 | 26/48 (PANC-1, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.732×** | -5.9 | 2e-07 | 29/48 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.741×** | -5.7 | 6e-07 | 25/47 (SW480, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.773×** | -4.9 | 5e-05 | 22/48 (SW1417, HT-29, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.789×** | -4.5 | 3e-04 | 19/47 (NCI-H460, RKO, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.849× | -4.4 | 4e-04 | 20/48 (A-427, Hs 766T, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.834× | -3.4 | 0.022 | 8/47 (MIA PaCa-2, LS 180, …) | inconsistent across doses | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **0.729×** | -3.1 | 0.055 | 11/45 (SNU-423, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | 0.849× | -3.1 | 0.059 | 9/47 (SW48, COLO 205, …) | inconsistent across doses |  |
| [[Silodosin (drug)]] 5 µM |  | 0.849× | -3.0 | 0.078 | 12/46 (SW48, NCI-H661, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6686. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 50.3 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.63× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.180× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -13.8) |
| [[RKO (line)]] | wt | 33.6 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -12.4) |
| [[SW480 (line)]] | alt | 25.0 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -13.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.305× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 33.5 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.406× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 28.8 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -15.3) |
| [[KATO III (line)]] | alt | 21.1 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.223× (z -10.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.250× (z -9.9) |
| [[LoVo (line)]] | wt | 26.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -14.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 41.0 | 0 | 3 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -17.8) |
| [[PANC-1 (line)]] | alt | 36.8 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -22.3) |
| [[A-172 (line)]] | wt | 36.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -12.3) |
| [[A498 (line)]] | wt | 40.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -12.7) |
| [[A549 (line)]] | wt | 27.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -8.6) |
| [[BT-474 (line)]] | alt | 36.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.273× (z -10.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 38.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -13.0) |
| [[HT-29 (line)]] | alt | 26.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -10.2) |
| [[LOX-IMVI (line)]] | wt | 16.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -12.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 30.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 27.6 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0907× (z -17.5) |
| [[SNU-1 (line)]] | wt | 39.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 40.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 17.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -11.8) |
| [[CHP-212 (line)]] | wt | 25.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0537× (z -10.2) |
| [[COLO 205 (line)]] | alt | 24.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.108× (z -9.3) |
| [[HOP62 (line)]] | alt | 18.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -14.4) |
| [[Hs 766T (line)]] | wt | 22.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -15.0) |
| [[HS-578T (line)]] | alt | 17.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -10.6) |
| [[J82 (line)]] | alt | 28.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 25.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 26.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -11.5) |
| [[SW48 (line)]] | wt | 32.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -8.9) |
| [[AN3 CA (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6686), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFRD2]] | +0.76 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[COA7]] | +0.76 | +0.67 / +0.79 | both halves | 7e-06 |  |
| [[RIOX2]] | +0.76 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[BYSL]] | +0.72 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[RAD51D]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[MAK16]] | +0.72 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[MGA]] | +0.72 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[ATIC]] | +0.72 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[IMP4]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[PDCD2]] | +0.70 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[ZNF202]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 | same gene group |
| [[ZBTB24]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NARF]] | -0.68 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[ZNF654]] | -0.68 | -0.74 / -0.57 | both halves | 9e-06 |  |
| [[SAP30-DT]] | -0.66 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[ZNHIT1]] | -0.65 | -0.62 / -0.57 | both halves | 8e-06 |  |
| [[TMEM59]] | -0.64 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[GNAS]] | -0.64 | -0.65 / -0.70 | both halves | 7e-06 |  |
| [[NDUFA2]] | -0.64 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[KDM2A]] | -0.63 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[OST4]] | -0.63 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[MPC2]] | -0.62 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[HELZ]] | -0.62 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[KDELR1]] | -0.61 | -0.52 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises POGK's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[OXR1]] | C | OXR1 activity lowers POGK's level | lines that do not express OXR1 (4) vs lines expressing it (46) | 1.55× higher at baseline in the lines without OXR1 | 0.085 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.807). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.0, -37.9); signed map (-0.4, -41.0). **Vector** length 95.8, 21.8% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.51 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.54 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.54 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.0 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.9 | +0.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.4 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +4.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.3 | +3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.2 | +3.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -21.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -8.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -9.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -11.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -4.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | pogo transposable element derived with KRAB domain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.1 — chr1:166,839,447-166,856,359 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA15131, LST003, BASS2, KRBOX2 |
| Gene groups (HGNC) | Helix-turn-helix CENPB type domain family; KRAB domain containing |
| Matched by | ensembl_id |

UniProt [Q9P215](https://www.uniprot.org/uniprotkb/Q9P215) carries no function annotation.

**Summary**, from NCBI Gene [57645](https://www.ncbi.nlm.nih.gov/gene/57645):

> The exact function of the protein encoded by this gene is not known. However, this gene product contains a KRAB domain (which is involved in protein-protein interactions) at the N-terminus, and a transposase domain at the C-terminus, suggesting that it may belong to the family of DNA-mediated transposons in human. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18800](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18800) · Entrez [57645](https://www.ncbi.nlm.nih.gov/gene/57645) · UniProt [Q9P215](https://www.uniprot.org/uniprotkb/Q9P215) · Ensembl [ENSG00000143157](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143157)

## Data

Gene col 6686: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6686); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6686, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6686]; `tensor/DDL_lfc|DDL_z.npy` [6686]; `embed/gene_vectors.npy` [6686]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6686 or target_col == 6686). Every well: [[POGK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POGK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
