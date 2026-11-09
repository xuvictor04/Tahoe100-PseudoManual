---
symbol: "SLBP"
type: "gene"
col: 8821
ensembl_id: "ENSG00000163950"
name: "stem-loop histone mRNA binding protein"
location: "4p16.3"
module: 6
arm: "+"
pooled_cpm: 40.34
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# SLBP

*stem-loop histone mRNA binding protein* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.57× (z +14.7, q 0e+00, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.64× (z +7.7, q 1e-12, up in 35 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.234×; ⚠ cell-cycle shift, explains ~56% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.506×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pimozide (drug)]] 0.5 µM in 1 line (CHP-212 0.0943×; ⚠ transcription drop).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDT1]] (+0.62, fdr 1e-05), [[SHMT1]] (+0.60, fdr 1e-05), [[FN3KRP]] (+0.60, fdr 3e-05); moves opposite to [[AP4S1]] (-0.59, fdr 1e-04), [[CCDC90B-AS1]] (-0.55, fdr 2e-04), [[LINC02955]] (-0.55, fdr 2e-04).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8821.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.57×** | +14.7 | 0e+00 | 47/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.33×** | +13.2 | 4e-37 | 48/48 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.32×** | +13.1 | 6e-37 | 46/47 (LoVo, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +7.7 | 1e-12 | 35/47 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.67×** | +7.7 | 1e-12 | 37/47 (COLO 205, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.41×** | +7.6 | 3e-12 | 31/48 (NCI-H1792, COLO 205, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.58×** | +7.1 | 8e-11 | 32/47 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +6.9 | 4e-10 | 29/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.54×** | +6.7 | 1e-09 | 36/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.45×** | +5.8 | 5e-07 | 26/45 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +5.6 | 1e-06 | 29/47 (CFPAC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +5.0 | 3e-05 | 25/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +4.3 | 9e-04 | 25/48 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.001 | 23/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.30×** | +4.1 | 0.002 | 21/48 (PANC-1, H4, …) | rises with dose |  |
| [[Arbutin (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.006 | 15/47 (A498, J82, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.046 | 16/47 (CFPAC-1, PANC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.063 | 13/48 (CFPAC-1, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.072 | 7/48 (NCI-H460, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.074 | 12/48 (J82, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.22×** | +2.9 | 0.074 | 12/48 (CFPAC-1, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.42×** | +2.8 | 0.086 | 10/47 (NCI-H460, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.41×** | +2.8 | 0.095 | 11/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8821.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.234×; ⚠ cell-cycle shift, explains ~56% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HEC-1-A 0.506×; ⚠ cell-cycle shift, explains ~0% of this change); [[Pimozide (drug)]] 0.5 µM in 1 line (CHP-212 0.0943×; ⚠ transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.791× | -3.6 | 0.16 | 21/48 (hTERT-HPNE, LS 180, …) | two highest doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.806× | -3.3 | 0.22 | 10/48 (PANC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.861× | -3.3 | 0.22 | 18/48 (A-427, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8821. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 23.0 | 5 (5 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.02× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[COLO 205 (line)]] | alt | 27.9 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +10.7) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[NCI-H1573 (line)]] | alt | 24.7 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.19× (z +10.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SW480 (line)]] | alt | 43.2 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.68× (z +10.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[KATO III (line)]] | alt | 43.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.98× (z +10.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[LoVo (line)]] | wt | 28.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.18× (z +12.2) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[LOX-IMVI (line)]] | wt | 36.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.94× (z +11.5) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[CFPAC-1 (line)]] | alt | 40.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +10.5) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[HOP62 (line)]] | alt | 28.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.1) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[HT-29 (line)]] | alt | 43.2 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.14× (z +9.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1792 (line)]] | alt | 16.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +11.2) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[Panc 03.27 (line)]] | alt | 39.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +9.6) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[PANC-1 (line)]] | alt | 34.0 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.71× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[A549 (line)]] | wt | 21.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.18× (z +9.2) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[AN3 CA (line)]] | alt | 55.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -10.3) ⚠ cell-cycle shift, explains ~56% of this change |
| [[AsPC-1 (line)]] | alt | 44.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.04× (z +8.9) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[CHP-212 (line)]] | wt | 33.8 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0943× (z -8.5) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 52.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 29.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +10.0) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[SW1417 (line)]] | alt | 40.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +9.1) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[A-172 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 64.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8821), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDT1]] | +0.62 | +0.55 / +0.57 | both halves | 1e-05 | STRING 508 |
| [[SHMT1]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[FN3KRP]] | +0.60 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[RBL1]] | +0.60 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[GGCT]] | +0.59 | +0.43 / +0.51 | both halves | 4e-05 |  |
| [[GMNN]] | +0.59 | +0.51 / +0.59 | both halves | 1e-05 | STRING 591 |
| [[MSH2]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[NUP85]] | +0.57 | +0.32 / +0.55 | both halves | 2e-04 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 474 |
| [[TELO2]] | +0.57 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[RFC4]] | +0.56 | +0.47 / +0.54 | both halves | 2e-05 | STRING 539 |
| [[DSCC1]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS; STRING 560 |
| [[NPHP4]] | +0.56 | +0.35 / +0.41 | both halves | 1e-04 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP4S1]] | -0.59 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[CCDC90B-AS1]] | -0.55 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[LINC02955]] | -0.55 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[EYS]] | -0.54 | -0.28 / -0.37 | both halves | 3e-04 |  |
| [[HCG17]] | -0.53 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[ARRDC3-AS1]] | -0.53 | -0.26 / -0.31 | both halves | 3e-04 |  |
| [[AK9]] | -0.53 | -0.27 / -0.33 | both halves | 3e-04 |  |
| [[ZBED5]] | -0.52 | -0.32 / -0.32 | both halves | 2e-04 |  |
| [[MKLN1-AS]] | -0.51 | -0.24 / -0.38 | both halves | 5e-04 |  |
| [[CDK6-AS1]] | -0.51 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[BHLHE40-AS1]] | -0.50 | -0.18 / -0.44 | ⚠ not reproduced | 1e-03 |  |
| [[CCDC17]] | -0.50 | -0.27 / -0.33 | both halves | 3e-04 |  |
| [[SLC13A3]] | -0.50 | -0.28 / -0.26 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.510). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-29.2, -45.7); signed map (-36.0, -40.4). **Vector** length 82.4, 20.5% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.2 | +14.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.5 | +13.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.5 | +13.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +7.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +2.7 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.4 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.8 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -3.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.3 | -3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | +0.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | stem-loop histone mRNA binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:1,692,731-1,712,344 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HBP |
| Hallmark sets | E2F_TARGETS |
| Reactome | 8 pathways, smallest: SLBP Dependent Processing of Replication-Dependent Histone Pre-mRNAs; Processing of Capped Intronless Pre-mRNA; RNA Polymerase II Transcription Termination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14493](https://www.uniprot.org/uniprotkb/Q14493) (Histone RNA hairpin-binding protein):

> RNA-binding protein involved in the histone pre-mRNA processing. Binds the stem-loop structure of replication-dependent histone pre-mRNAs and contributes to efficient 3'-end processing by stabilizing the complex between histone pre-mRNA and U7 small nuclear ribonucleoprotein (snRNP), via the histone downstream element (HDE). Plays an important role in targeting mature histone mRNA from the nucleus to the cytoplasm and to the translation machinery. Stabilizes mature histone mRNA and could be …

**Summary**, from NCBI Gene [7884](https://www.ncbi.nlm.nih.gov/gene/7884):

> This gene encodes a protein that binds to the stem-loop structure in replication-dependent histone mRNAs. Histone mRNAs do not contain introns or polyadenylation signals, and are processed by endonucleolytic cleavage. The stem-loop structure is essential for efficient processing but this structure also controls the transport, translation and stability of histone mRNAs. Expression of the protein is regulated during the cell cycle, increasing more than 10-fold during the latter part of G1. …

**Accessions** — [HGNC:10904](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10904) · Entrez [7884](https://www.ncbi.nlm.nih.gov/gene/7884) · UniProt [Q14493](https://www.uniprot.org/uniprotkb/Q14493) · Ensembl [ENSG00000163950](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163950)

## Data

Gene col 8821: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8821); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8821, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8821]; `tensor/DDL_lfc|DDL_z.npy` [8821]; `embed/gene_vectors.npy` [8821]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8821 or target_col == 8821). Every well: [[SLBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
