---
symbol: "P2RX4"
type: "gene"
col: 5659
ensembl_id: "ENSG00000135124"
name: "purinergic receptor P2X 4"
location: "12q24.31"
module: 36
arm: "-"
pooled_cpm: 22.34
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# P2RX4

*purinergic receptor P2X 4* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.95× (z +15.5, q 0e+00, up in 24 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.39× (z +7.0, q 5e-10, up in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (NCI-H2030 8.43×, HOP62 7.84×, RPMI-7951 16.6×, HEC-1-A 5.54×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HEC-1-A 5.55×, HOP62 3.94×, SHP-77 5.59×, NCI-H2030 3.67×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 4.23×, A-172 4.29×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.626× (z -9.8, q 8e-20, down in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.589× (z -7.8, q 1e-12, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BBS7]] (+0.62, fdr 7e-06), [[ETFRF1]] (+0.59, fdr 1e-05), [[ITSN2]] (+0.57, fdr 1e-05); moves opposite to [[SLC25A10]] (-0.58, fdr 3e-05), [[TOMM70]] (-0.57, fdr 2e-05), [[RNGTT]] (-0.56, fdr 1e-05).
> It sits in the **-** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5659.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (NCI-H2030 8.43×, HOP62 7.84×, RPMI-7951 16.6×, HEC-1-A 5.54×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HEC-1-A 5.55×, HOP62 3.94×, SHP-77 5.59×, NCI-H2030 3.67×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (J82 4.23×, A-172 4.29×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.95×** | +15.5 | 0e+00 | 24/31 (NCI-H2030, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +9.8 | 3e-20 | 27/42 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +7.0 | 5e-10 | 31/48 (AsPC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.38×** | +4.8 | 2e-04 | 25/46 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 1.17× | +3.3 | 0.097 | 16/48 (CFPAC-1, SW 900, …) | top dose only |  |
| [[Resveratrol (drug)]] 5 µM |  | 1.17× | +3.3 | 0.097 | 7/48 (NCI-H1573, Hs 766T, …) | top dose only |  |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.097 | 7/47 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.23× | +3.1 | 0.15 | 11/48 (HOP62, RKO, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5659.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.626×** | -9.8 | 8e-20 | 37/47 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.575×** | -8.2 | 9e-14 | 29/47 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.589×** | -7.8 | 1e-12 | 34/47 (KATO III, A-172, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.377×** | -7.5 | 7e-12 | 37/48 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.627×** | -6.9 | 6e-10 | 29/47 (SNU-423, SW480, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.423×** | -6.6 | 3e-09 | 29/45 (NCI-H2347, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.639×** | -6.6 | 3e-09 | 28/47 (NCI-H1792, MIA PaCa-2, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.650×** | -6.4 | 1e-08 | 28/48 (CFPAC-1, HCT15, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.691×** | -5.4 | 3e-06 | 26/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.711×** | -4.7 | 1e-04 | 19/47 (SW1417, HEC-1-A, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -4.6 | 2e-04 | 3/48 (C32, NCI-H661, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.549×** | -4.6 | 2e-04 | 22/45 (SK-MEL-2, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.736×** | -4.5 | 3e-04 | 24/48 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.731×** | -4.4 | 4e-04 | 22/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.646×** | -3.4 | 0.029 | 15/44 (SW 900, PANC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.851× | -3.3 | 0.031 | 18/48 (MIA PaCa-2, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.59 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5659. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 44.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -11.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.156× (z -8.8) |
| [[J82 (line)]] | alt | 15.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +12.4) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.342× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 34.2 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -13.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 14.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +12.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CFPAC-1 (line)]] | alt | 46.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -9.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 19.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.55× (z +12.9) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 17.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.84× (z +13.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 16.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.43× (z +14.3) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 37.9 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.305× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 20.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.27× (z +11.9) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 43.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.384× (z -8.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Hs 766T (line)]] | wt | 6.23 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0715× (z -9.1) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -10.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H460 (line)]] | wt | 21.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.49× (z +9.8) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 19.1 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0671× (z -9.0) |
| [[PANC-1 (line)]] | alt | 14.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +9.2) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 14.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 16.6× (z +12.8) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 19.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.59× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 33.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.96× (z +12.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 20.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.373× (z -8.5) |
| [[A-427 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5659), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBS7]] | +0.62 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[ETFRF1]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ITSN2]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ABCA5]] | +0.56 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ZNF385C]] | +0.55 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[WBP4]] | +0.55 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[NFKBIB]] | +0.53 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[KPNA5]] | +0.53 | +0.39 / +0.55 | both halves | 5e-05 |  |
| [[XPA]] | +0.53 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[UPF3B]] | +0.52 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[XIAP]] | +0.52 | +0.60 / +0.38 | both halves | 6e-05 |  |
| [[BTG3]] | +0.52 | +0.48 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A10]] | -0.58 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[TOMM70]] | -0.57 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[RNGTT]] | -0.56 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[NAT10]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[PREP]] | -0.54 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[DOK3]] | -0.54 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[TOMM40]] | -0.53 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[KLHL18]] | -0.52 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[HDAC4]] | -0.51 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[NSUN2]] | -0.51 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[MTFR2]] | -0.50 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[ICE1]] | -0.50 | -0.41 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **-** arm (projection on the module's main direction -0.398). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-1.0, -27.8); signed map (4.3, -12.0). **Vector** length 101, 23.4% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.8 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.8 | +15.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.0 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.3 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.7 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +1.2 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -4.6 | -6.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.0 | -7.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.0 | -7.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.7 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -6.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -4.7 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -2.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | purinergic receptor P2X 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:121,210,065-121,234,106 (+) |
| Ensembl biotype | protein_coding |
| Also known as | P2X4 |
| Gene groups (HGNC) | Purinergic receptors P2X |
| Hallmark sets | INFLAMMATORY_RESPONSE, IL2_STAT5_SIGNALING |
| Reactome | 8 pathways, smallest: Elevation of cytosolic Ca2+ levels; Platelet calcium homeostasis; Cell recruitment (pro-inflammatory response) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99571](https://www.uniprot.org/uniprotkb/Q99571) (P2X purinoceptor 4):

> ATP-gated nonselective transmembrane cation channel permeable to potassium, sodium and calcium. CTP, but not GTP or UTP, functions as a weak affinity agonist for P2RX4 (By similarity). Activated by extracellularly released ATP, it plays multiple role in immunity and central nervous system physiology. Plays a key role in initial steps of T-cell activation and Ca(2+) microdomain formation (By similarity). Also participates in basal T-cell activity without TCR/CD3 stimulation (By similarity). …

**Summary**, from NCBI Gene [5025](https://www.ncbi.nlm.nih.gov/gene/5025):

> The product of this gene belongs to the family of purinoceptors for ATP. This receptor functions as a ligand-gated ion channel with high calcium permeability. The main pharmacological distinction between the members of the purinoceptor family is the relative sensitivity to the antagonists suramin and PPADS. The product of this gene has the lowest sensitivity for these antagonists. Multiple alternatively spliced transcript variants, some protein-coding and some not protein-coding, have been …

**Accessions** — [HGNC:8535](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8535) · Entrez [5025](https://www.ncbi.nlm.nih.gov/gene/5025) · UniProt [Q99571](https://www.uniprot.org/uniprotkb/Q99571) · Ensembl [ENSG00000135124](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135124)

## Data

Gene col 5659: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5659); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5659, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5659]; `tensor/DDL_lfc|DDL_z.npy` [5659]; `embed/gene_vectors.npy` [5659]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5659 or target_col == 5659). Every well: [[P2RX4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/P2RX4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
