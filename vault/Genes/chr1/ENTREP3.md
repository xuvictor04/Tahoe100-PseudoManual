---
symbol: "ENTREP3"
type: "gene"
col: 8378
ensembl_id: "ENSG00000160767"
name: "endosomal transmembrane epsin interactor 3"
location: "1q22"
module: 50
arm: "+"
pooled_cpm: 13.2
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 19
n_dd_up_clean: 1
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# ENTREP3

*endosomal transmembrane epsin interactor 3* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.53× (z +12.2, q 3e-31, up in 17 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Osimertinib (mesylate) (drug)]] 5 µM: 1.32× (z +3.8, q 0.012, up in 10 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 2.87×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.306× (z -22.8, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLB1]] (+0.68, fdr 7e-06), [[PPT2]] (+0.66, fdr 1e-05), [[ZDHHC8]] (+0.65, fdr 7e-06); moves opposite to [[H3-3B]] (-0.53, fdr 1e-05), [[LINC02340]] (-0.52, fdr 1e-05), [[XIAP]] (-0.52, fdr 7e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8378.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 2.87×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.53×** | +12.2 | 3e-31 | 17/19 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +11.6 | 1e-28 | 31/38 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +6.6 | 6e-09 | 26/42 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +6.3 | 4e-08 | 20/29 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.35×** | +5.8 | 8e-07 | 27/48 (A498, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.42×** | +4.8 | 2e-04 | 22/47 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.6 | 4e-04 | 3/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.012 | 10/47 (A-172, C-33 A, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.2 | 0.079 | 5/28 (MIA PaCa-2, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.26×** | +3.2 | 0.079 | 9/48 (PANC-1, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8378.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.306×** | -22.8 | 0e+00 | 42/47 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.247×** | -18.3 | 0e+00 | 45/46 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.292×** | -16.8 | 0e+00 | 41/44 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.470×** | -10.3 | 1e-22 | 33/46 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.482×** | -9.9 | 3e-21 | 34/46 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.496×** | -9.5 | 1e-19 | 34/47 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.518×** | -9.0 | 3e-17 | 35/47 (RKO, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.535×** | -8.5 | 1e-15 | 33/46 (SNU-423, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.370×** | -7.1 | 1e-10 | 29/46 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.632×** | -6.2 | 2e-08 | 26/47 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.449×** | -5.7 | 6e-07 | 26/43 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.698×** | -4.9 | 5e-05 | 24/46 (A498, C32, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.690×** | -4.8 | 6e-05 | 23/45 (NCI-H23, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.711×** | -4.6 | 1e-04 | 21/47 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.791×** | -4.5 | 3e-04 | 17/45 (SK-MEL-2, RKO, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.734×** | -4.2 | 9e-04 | 17/47 (NCI-H23, SW1417, …) | rises with dose | cell-cycle shift (explains ~19% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8378. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 33.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -28.2) |
| [[NCI-H460 (line)]] | wt | 14.9 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -18.2) |
| [[RKO (line)]] | wt | 22.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -18.6) |
| [[NCI-H2030 (line)]] | alt | 28.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -21.4) |
| [[A-427 (line)]] | wt | 25.1 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.162× (z -12.3) |
| [[A498 (line)]] | wt | 19.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -16.4) |
| [[NCI-H23 (line)]] | alt | 27.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -10.5) |
| [[PANC-1 (line)]] | alt | 14.9 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -21.0) |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -13.4) |
| [[LOX-IMVI (line)]] | wt | 12.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 21.6 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.108× (z -13.7) |
| [[NCI-H2347 (line)]] | alt | 9.46 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -13.6) |
| [[SW 900 (line)]] | alt | 11.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0338× (z -16.5) |
| [[A549 (line)]] | wt | 6.73 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0903× (z -15.1) |
| [[AsPC-1 (line)]] | alt | 6.39 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0259× (z -14.4) |
| [[COLO 205 (line)]] | alt | 9.00 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -11.1) |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0867× (z -13.9) |
| [[J82 (line)]] | alt | 10.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 8.75 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -11.8) |
| [[SNU-1 (line)]] | wt | 12.6 | 0 | 2 | — | [[Bergenin (drug)]] 0.5 µM 0.0851× (z -9.5) |
| [[SW1417 (line)]] | alt | 8.79 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -13.8) |
| [[SW48 (line)]] | wt | 22.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -14.1) |
| [[BT-474 (line)]] | alt | 5.84 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -8.8) |
| [[C-33 A (line)]] | alt | 22.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -11.7) |
| [[C32 (line)]] | wt | 9.17 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -8.5) |
| [[CHP-212 (line)]] | wt | 17.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0331× (z -10.1) |
| [[H4 (line)]] | wt | 11.0 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 0.05 µM 0.0678× (z -9.9) |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0286× (z -14.3) |
| [[LoVo (line)]] | wt | 11.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.211× (z -9.4) |
| [[LS 180 (line)]] | wt | 7.72 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 7.74 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -11.5) |
| [[SNU-423 (line)]] | alt | 7.42 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.102× (z -10.3) |
| [[SW480 (line)]] | alt | 9.17 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -11.2) |
| [[AN3 CA (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8378), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLB1]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[PPT2]] | +0.66 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[ZDHHC8]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[PLBD2]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[PIK3R2]] | +0.61 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[TMUB1]] | +0.61 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[COLGALT1]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[CNPY3]] | +0.60 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[TMEM183A]] | +0.59 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[DFFB]] | +0.58 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[GTPBP3]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[TRAF7]] | +0.57 | +0.68 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H3-3B]] | -0.53 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[LINC02340]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[XIAP]] | -0.52 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[UTP3]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[HELQ]] | -0.52 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[PFN1]] | -0.52 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[LENG1]] | -0.52 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[METTL23]] | -0.51 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[NOTCH2NLB]] | -0.51 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[NEPRO-AS1]] | -0.51 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[TUT7]] | -0.51 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[ERCC6L2]] | -0.51 | -0.56 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.549). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.9, -20.2); signed map (-47.4, -9.0). **Vector** length 76.9, 15.3% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +6.5 | +5.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +12.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +2.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.9 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +11.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.5 | +2.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.0 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.1 | -16.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.0 | -9.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -18.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -22.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.1 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | endosomal transmembrane epsin interactor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,247,205-155,255,483 (-) |
| Ensembl biotype | protein_coding |
| Also known as | cote1; previously C1orf2, FAM189B |
| Matched by | ensembl_id |

UniProt [P81408](https://www.uniprot.org/uniprotkb/P81408) carries no function annotation.

**Summary**, from NCBI Gene [10712](https://www.ncbi.nlm.nih.gov/gene/10712):

> This gene is located near the gene for the lysosomal enzyme glucosylceramidase; a deficiency in this enzyme is associated with Gaucher disease. The encoded protein has been identified as a potential binding partner of a WW domain-containing protein which is involved in apoptosis and tumor suppression. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:1233](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1233) · Entrez [10712](https://www.ncbi.nlm.nih.gov/gene/10712) · UniProt [P81408](https://www.uniprot.org/uniprotkb/P81408) · Ensembl [ENSG00000160767](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160767)

## Data

Gene col 8378: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8378); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8378, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8378]; `tensor/DDL_lfc|DDL_z.npy` [8378]; `embed/gene_vectors.npy` [8378]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8378 or target_col == 8378). Every well: [[ENTREP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENTREP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
