---
symbol: "LMNB1"
type: "gene"
col: 3455
ensembl_id: "ENSG00000113368"
name: "lamin B1"
location: "5q23.2"
module: 22
arm: "+"
pooled_cpm: 47.05
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 51
n_dd_up_clean: 0
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# LMNB1

*lamin B1* — 5q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.43× (z +13.6, q 2e-39, up in 37 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2030 4.27×, PANC-1 2.99×, HT-29 4.36×, NCI-H460 2.78×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H2030 5.12×, PANC-1 2.88×, HT-29 3.92×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 4.96×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change).
> Pooled over the cell lines (median), lowered significantly by 51 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.438× (z -17.6, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BUB1B]] (+0.88, fdr 7e-06), [[PBK]] (+0.86, fdr 7e-06), [[MAD2L1]] (+0.86, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3455.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H2030 4.27×, PANC-1 2.99×, HT-29 4.36×, NCI-H460 2.78×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H2030 5.12×, PANC-1 2.88×, HT-29 3.92×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 4.96×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.43×** | +13.6 | 2e-39 | 37/45 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.72×** | +8.0 | 4e-13 | 27/40 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.63×** | +6.9 | 8e-10 | 24/42 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.36×** | +6.6 | 4e-09 | 32/47 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.50×** | +6.2 | 6e-08 | 29/46 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~97% of this change | **1.38×** | +4.9 | 8e-05 | 24/46 (HT-29, HOP62, …) | all doses, flat | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~95% of this change | **1.28×** | +3.7 | 0.019 | 20/46 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.26×** | +3.6 | 0.026 | 20/47 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.23×** | +3.2 | 0.073 | 11/47 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | 1.22× | +3.1 | 0.11 | 14/47 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 5 µM |  | 1.15× | +3.1 | 0.11 | 14/47 (A498, PANC-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.24× | +3.0 | 0.11 | 17/47 (NCI-H460, HT-29, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 20 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 51 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3455.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.438×** | -17.6 | 0e+00 | 41/47 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.341×** | -16.3 | 0e+00 | 42/47 (SW48, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.489×** | -15.3 | 0e+00 | 39/47 (A498, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.461×** | -11.8 | 1e-29 | 39/47 (SK-MEL-2, AN3 CA, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.468×** | -11.5 | 1e-28 | 38/47 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.482×** | -10.6 | 2e-24 | 39/47 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.508×** | -10.3 | 9e-23 | 38/47 (SHP-77, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.532×** | -9.6 | 9e-20 | 34/47 (SHP-77, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.585×** | -8.1 | 3e-14 | 30/47 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.630×** | -7.0 | 2e-10 | 33/47 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.720×** | -7.0 | 2e-10 | 29/46 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.510×** | -7.0 | 2e-10 | 32/47 (H4, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.646×** | -6.6 | 2e-09 | 33/46 (A498, SW48, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.741×** | -6.4 | 7e-09 | 29/47 (SW480, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.665×** | -6.2 | 3e-08 | 25/47 (A-427, LS 180, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.693×** | -5.5 | 1e-06 | 27/47 (C-33 A, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **0.773×** | -5.5 | 2e-06 | 28/47 (A498, A-172, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.794×** | -4.9 | 3e-05 | 26/47 (HCT15, SK-MEL-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.716×** | -4.8 | 3e-05 | 24/46 (SK-MEL-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.738×** | -4.6 | 1e-04 | 21/47 (HEC-1-A, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3455. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 38.0 | 0 | 8 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.164× (z -20.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.355× (z -11.6) |
| [[A-427 (line)]] | wt | 90.0 | 0 | 7 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.244× (z -17.6) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.383× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 51.5 | 4 (4 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.31× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.397× (z -11.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.362× (z -9.1) |
| [[A-172 (line)]] | wt | 43.4 | 0 | 6 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.170× (z -19.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.231× (z -15.8) |
| [[C-33 A (line)]] | alt | 133 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -12.2) |
| [[H4 (line)]] | wt | 58.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0623× (z -20.2) |
| [[HEC-1-A (line)]] | alt | 94.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -11.9) |
| [[HOP62 (line)]] | alt | 55.9 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -16.2) |
| [[PANC-1 (line)]] | alt | 49.0 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -14.9) |
| [[SHP-77 (line)]] | alt | 119 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 72.9 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -19.6) |
| [[SW48 (line)]] | wt | 65.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0410× (z -21.2) |
| [[HT-29 (line)]] | alt | 36.3 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -11.6) |
| [[J82 (line)]] | alt | 71.8 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 39.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -13.1) |
| [[LS 180 (line)]] | wt | 44.4 | 0 | 4 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.201× (z -15.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.291× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 44.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.12× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -11.3) |
| [[SW480 (line)]] | alt | 57.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -15.2) |
| [[C32 (line)]] | wt | 54.5 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.296× (z -12.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.245× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 83.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -25.1) |
| [[NCI-H2347 (line)]] | alt | 42.4 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.432× (z -9.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.442× (z -9.1) |
| [[AN3 CA (line)]] | alt | 113 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.158× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 60.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -20.2) |
| [[SNU-1 (line)]] | wt | 42.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0688× (z -13.6) |
| [[BT-474 (line)]] | alt | 26.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -8.7) |
| [[HCT15 (line)]] | alt | 69.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -10.6) |
| [[Hs 766T (line)]] | wt | 29.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -11.3) |
| [[LoVo (line)]] | wt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.185× (z -11.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[Panc 03.27 (line)]] | alt | 36.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.252× (z -9.4) |
| [[RKO (line)]] | wt | 32.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -10.9) |
| [[A549 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3455), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BUB1B]] | +0.88 | +0.84 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 451 |
| [[PBK]] | +0.86 | +0.84 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[MAD2L1]] | +0.86 | +0.83 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[ARHGAP11B]] | +0.84 | +0.77 / +0.86 | both halves | 7e-06 |  |
| [[INCENP]] | +0.83 | +0.78 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[KIFC1]] | +0.83 | +0.82 / +0.82 | both halves | 7e-06 | STRING 477 |
| [[CIT]] | +0.83 | +0.80 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 418 |
| [[FOXM1]] | +0.82 | +0.81 / +0.83 | both halves | 7e-06 | STRING 429 |
| [[ARHGAP11A]] | +0.82 | +0.77 / +0.82 | both halves | 7e-06 |  |
| [[KIF15]] | +0.82 | +0.76 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 416 |
| [[NCAPH]] | +0.81 | +0.78 / +0.78 | both halves | 7e-06 | STRING 463 |
| [[AURKB]] | +0.81 | +0.79 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 511 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises LMNB1's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 8.7% of all compounds | 0.015 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[E2F8]] | B | E2F8 activity raises LMNB1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.45× lower at baseline in the lines without E2F8 | 0.023 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises LMNB1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.12× lower at baseline in the lines without AURKB | 0.013 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises LMNB1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.86× lower at baseline in the lines without PBK | 0.021 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[MELK]] | C | MELK activity raises LMNB1's level | lines that do not express MELK (3) vs lines expressing it (47) | 3.30× lower at baseline in the lines without MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[MYBL2]] | C | MYBL2 activity raises LMNB1's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 3.22× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[MCM3]] | C | MCM3 activity raises LMNB1's level | lines that do not express MCM3 (3) vs lines expressing it (47) | 3.14× lower at baseline in the lines without MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p |
| [[C21orf58]], [[SKA3]] | C | C21orf58, SKA3 activity raises LMNB1's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 2.95× lower at baseline in the lines without C21orf58, SKA3 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent genes |
| [[SAPCD2]], [[SHMT1]] | C | SAPCD2, SHMT1 activity raises LMNB1's level | lines that do not express SAPCD2, SHMT1 (3) vs lines expressing them (47) | 2.92× lower at baseline in the lines without SAPCD2, SHMT1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.3, -53.5); signed map (-46.9, -42.6). **Vector** length 148, 52.2% of its response variance represented; |z| ≥ 3 in 1,529 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.66 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.60 to 48); *Resolution of Sister Chromatid Cohesion* (reactome, mean cos +0.61 to 33).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | +6.1 | +6.2 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +4.6 | +6.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.3 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +2.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +3.1 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | -0.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +2.3 | +0.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -8.5 | -15.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.0 | -11.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -8.0 | -11.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.4 | -16.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | -6.6 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -6.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.9 | -4.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.7 | -2.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | lamin B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.2 — chr5:126,776,623-126,837,020 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Lamins |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE, E2F_TARGETS |
| Reactome | 37 pathways, smallest: Breakdown of the nuclear lamina; Depolymerization of the Nuclear Lamina; Formation of Senescence-Associated Heterochromatin Foci (SAHF) |
| Matched by | ensembl_id |

**Function**, from UniProt [P20700](https://www.uniprot.org/uniprotkb/P20700) (Lamin-B1):

> Lamins are intermediate filament proteins that assemble into a filamentous meshwork, and which constitute the major components of the nuclear lamina, a fibrous layer on the nucleoplasmic side of the inner nuclear membrane. Lamins provide a framework for the nuclear envelope, bridging the nuclear envelope and chromatin, thereby playing an important role in nuclear assembly, chromatin organization, nuclear membrane and telomere dynamics. The structural integrity of the lamina is strictly …

**Summary**, from NCBI Gene [4001](https://www.ncbi.nlm.nih.gov/gene/4001):

> This gene encodes one of the two B-type lamin proteins and is a component of the nuclear lamina. A duplication of this gene is associated with autosomal dominant adult-onset leukodystrophy (ADLD). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:6637](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6637) · Entrez [4001](https://www.ncbi.nlm.nih.gov/gene/4001) · UniProt [P20700](https://www.uniprot.org/uniprotkb/P20700) · Ensembl [ENSG00000113368](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113368)

## Data

Gene col 3455: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3455); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3455, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3455]; `tensor/DDL_lfc|DDL_z.npy` [3455]; `embed/gene_vectors.npy` [3455]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3455 or target_col == 3455). Every well: [[LMNB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMNB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
