---
symbol: "DUSP11"
type: "gene"
col: 6840
ensembl_id: "ENSG00000144048"
name: "dual specificity phosphatase 11"
location: "2p13.1"
module: 65
arm: "+"
pooled_cpm: 32.71
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 26
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# DUSP11

*dual specificity phosphatase 11* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 1.99× (z +4.7, q 7e-04, up in 29 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 1 line (A498 6.21×).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.413× (z -11.1, q 7e-26, down in 32 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.705× (z -6.4, q 2e-08, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRIG2]] (+0.71, fdr 7e-06), [[ALG9]] (+0.70, fdr 7e-06), [[PRMT9]] (+0.69, fdr 7e-06); moves opposite to [[NPIPB4]] (-0.64, fdr 1e-05), [[CUX1]] (-0.63, fdr 1e-05), [[NPIPB5]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6840.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 1 line (A498 6.21×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.99×** | +4.7 | 7e-04 | 29/47 (NCI-H2030, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.99×** | +4.7 | 7e-04 | 28/49 (A498, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6840.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.413×** | -11.1 | 7e-26 | 32/35 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.444×** | -10.6 | 1e-23 | 36/45 (LS 180, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.655×** | -7.8 | 1e-12 | 30/47 (AsPC-1, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.705×** | -6.4 | 2e-08 | 27/48 (AsPC-1, A-172, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.615×** | -6.3 | 3e-08 | 38/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.628×** | -5.6 | 2e-06 | 26/41 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.685×** | -4.9 | 7e-05 | 28/48 (SW 1088, AsPC-1, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.666×** | -4.6 | 3e-04 | 24/48 (AsPC-1, RKO, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.720×** | -4.3 | 0.001 | 27/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.799×** | -4.1 | 0.002 | 28/48 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.818×** | -3.7 | 0.011 | 20/48 (NCI-H2347, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.755×** | -3.6 | 0.013 | 22/48 (NCI-H2347, SW480, …) | rises with dose |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.759×** | -3.6 | 0.015 | 18/48 (CFPAC-1, SW1417, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.757×** | -3.5 | 0.020 | 20/47 (hTERT-HPNE, HS-578T, …) | rises with dose | composition shift |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.835× | -3.3 | 0.036 | 17/48 (HEC-1-A, RKO, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.837× | -3.3 | 0.038 | 20/48 (RPMI-7951, LOX-IMVI, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.782×** | -3.2 | 0.046 | 17/48 (AsPC-1, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.794×** | -3.0 | 0.083 | 18/48 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.727×** | -3.0 | 0.085 | 14/48 (HS-578T, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.797×** | -2.9 | 0.085 | 8/48 (KATO III, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.656×** | -2.9 | 0.094 | 16/48 (H4, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.803×** | -2.8 | 0.094 | 13/48 (HEC-1-A, C32, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.803×** | -2.8 | 0.094 | 15/48 (CHP-212, C32, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.804×** | -2.8 | 0.096 | 14/48 (NCI-H661, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6840. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 31.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -8.8) |
| [[HOP62 (line)]] | alt | 42.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 44.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 46.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.21× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.352× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[AsPC-1 (line)]] | alt | 44.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -18.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 44.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A-427 (line)]] | wt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A549 (line)]] | wt | 46.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[CFPAC-1 (line)]] | alt | 33.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -10.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HEC-1-A (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HS-578T (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[hTERT-HPNE (line)]] | wt | 36.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -11.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 27.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[LS 180 (line)]] | wt | 33.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0276× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[MIA PaCa-2 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 40.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 25.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[Panc 03.27 (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[RPMI-7951 (line)]] | alt | 43.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SNU-1 (line)]] | wt | 46.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SNU-423 (line)]] | alt | 29.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -17.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW 1088 (line)]] | alt | 52.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0415× (z -9.1) ⚠ cell-cycle shift, explains ~51% of this change |
| [[SW48 (line)]] | wt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0851× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[AN3 CA (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 32.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6840), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRIG2]] | +0.71 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[ALG9]] | +0.70 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[PRMT9]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[BAG4]] | +0.68 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[COPS4]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[ABHD10]] | +0.66 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[FAM8A1]] | +0.65 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.64 | +0.82 / +0.53 | both halves | 1e-05 |  |
| [[YIPF2]] | +0.64 | +0.78 / +0.50 | both halves | 1e-05 |  |
| [[MINDY3]] | +0.64 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[FRG1DP]] | +0.64 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[TGDS]] | +0.63 | +0.57 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPIPB4]] | -0.64 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[CUX1]] | -0.63 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[NPIPB5]] | -0.62 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[EIF3J]] | -0.60 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[COMMD10]] | -0.58 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[ASAP1]] | -0.58 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[CCDC144CP]] | -0.57 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[SMARCA4]] | -0.57 | -0.46 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.748). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-2.9, -10.9); signed map (-31.4, -10.5). **Vector** length 90.1, 21.3% of its response variance represented; |z| ≥ 3 in 867 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.4 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.7 | +0.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.8 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +1.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.2 | +0.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.6 | +0.8 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.6 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.8 | -7.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -4.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -3.2 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | +0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -2.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.1 | -2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -0.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:73,761,782-73,780,132 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PIR1 |
| Gene groups (HGNC) | Atypical dual specificity phosphatases |
| Matched by | ensembl_id |

**Function**, from UniProt [O75319](https://www.uniprot.org/uniprotkb/O75319) (RNA/RNP complex-1-interacting phosphatase):

> Possesses RNA 5'-triphosphatase and diphosphatase activities, but displays a poor protein-tyrosine phosphatase activity. In addition, has phosphatase activity with ATP, ADP and O-methylfluorescein phosphate (in vitro). Binds to RNA. May participate in nuclear mRNA metabolism.

**Summary**, from NCBI Gene [8446](https://www.ncbi.nlm.nih.gov/gene/8446):

> The protein encoded by this gene is a member of the dual specificity protein phosphatase subfamily. These phosphatases inactivate their target kinases by dephosphorylating both the phosphoserine/threonine and phosphotyrosine residues. They negatively regulate members of the mitogen-activated protein (MAP) kinase superfamily (MAPK/ERK, SAPK/JNK, p38), which is associated with cellular proliferation and differentiation. Different members of the family of dual specificity phosphatases show …

**Accessions** — [HGNC:3066](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3066) · Entrez [8446](https://www.ncbi.nlm.nih.gov/gene/8446) · UniProt [O75319](https://www.uniprot.org/uniprotkb/O75319) · Ensembl [ENSG00000144048](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144048)

## Data

Gene col 6840: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6840); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6840, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6840]; `tensor/DDL_lfc|DDL_z.npy` [6840]; `embed/gene_vectors.npy` [6840]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6840 or target_col == 6840). Every well: [[DUSP11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
