---
symbol: "MIDN"
type: "gene"
col: 9470
ensembl_id: "ENSG00000167470"
name: "midnolin"
location: "19p13.3"
module: 192
arm: "+"
pooled_cpm: 77.62
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/192"]
generated_by: "tahoemap"
---

# MIDN

*midnolin* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +8.9, q 3e-16, up in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~78% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.67× (z +5.0, q 6e-05, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.590× (z -7.5, q 5e-11, down in 44 of 47 measured lines) ⚠ cell-cycle shift, explains ~58% of this change. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.638× (z -4.1, q 0.005, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB7A]] (+0.75, fdr 7e-06), [[PLIN3]] (+0.66, fdr 1e-05), [[SPATA2L]] (+0.65, fdr 1e-05); moves opposite to [[NNT]] (-0.67, fdr 1e-05), [[UBQLN1]] (-0.66, fdr 7e-06), [[EIF2D]] (-0.66, fdr 2e-05).
> It is in [[Module 192]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SH2D3A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9470.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.89×** | +8.9 | 3e-16 | 36/47 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.36×** | +8.4 | 2e-14 | 40/47 (SW480, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +5.7 | 2e-06 | 23/49 (HT-29, Panc 03.27, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.75×** | +5.3 | 2e-05 | 30/47 (PANC-1, HEC-1-A, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +5.0 | 6e-05 | 32/47 (HEC-1-A, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.62×** | +4.7 | 2e-04 | 34/46 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.52×** | +4.1 | 0.003 | 31/47 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~80% of this change | **1.48×** | +3.9 | 0.007 | 32/47 (CFPAC-1, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.012 | 25/47 (HCT15, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.46×** | +3.7 | 0.012 | 26/47 (SW480, HepG2/C3A, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.44×** | +3.6 | 0.017 | 27/47 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.017 | 30/47 (MIA PaCa-2, C-33 A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.43×** | +3.4 | 0.034 | 24/46 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.081 | 26/47 (HCT15, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.090 | 26/48 (NCI-H23, SHP-77, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9470.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.590×** | -7.5 | 5e-11 | 44/47 (SW48, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.623×** | -4.7 | 7e-04 | 32/47 (NCI-H1792, A498, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.638×** | -4.1 | 0.005 | 36/47 (SW480, SW48, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.662×** | -4.1 | 0.005 | 34/47 (RKO, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.664×** | -4.0 | 0.007 | 32/47 (KATO III, HT-29, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.674×** | -3.7 | 0.017 | 27/47 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.680×** | -3.7 | 0.017 | 24/43 (A-172, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.693×** | -3.5 | 0.033 | 28/49 (SW48, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.721×** | -3.1 | 0.098 | 23/48 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.713×** | -3.1 | 0.098 | 26/47 (RKO, LS 180, …) | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 5 µM |  | 0.530× | -3.1 | 0.11 | 25/46 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.807× | -3.0 | 0.11 | 25/48 (HT-29, SW1417, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.72 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9470. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 68.8 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +15.1) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.24× (z +10.9) | — |
| [[HepG2_C3A (line)]] | wt | 127 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.55× (z +16.0) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[AsPC-1 (line)]] | alt | 167 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +14.1) ⚠ cell-cycle shift, explains ~78% of this change | [[Selinexor (drug)]] 5 µM 0.373× (z -11.2) ⚠ cell-cycle shift, explains ~58% of this change |
| [[SW480 (line)]] | alt | 69.6 | 5 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 10.4× (z +17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.24× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 73.1 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.73× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[PANC-1 (line)]] | alt | 54.4 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +15.4) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[HOP62 (line)]] | alt | 55.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +10.9) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 69.2 | 1 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.19× (z +9.3) ⚠ cell-cycle shift, explains ~71% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -12.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 81.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0650× (z -20.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 78.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.5) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[HT-29 (line)]] | alt | 112 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[MIA PaCa-2 (line)]] | alt | 43.8 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.17× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.39× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 72.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 67.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +12.4) ⚠ cell-cycle shift, explains ~78% of this change | [[Selinexor (drug)]] 5 µM 0.338× (z -9.8) ⚠ cell-cycle shift, explains ~58% of this change |
| [[NCI-H2347 (line)]] | alt | 62.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.56× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.290× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 48.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +11.6) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[SW48 (line)]] | wt | 121 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.72× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Selinexor (drug)]] 5 µM 0.276× (z -12.0) ⚠ cell-cycle shift, explains ~58% of this change |
| [[A-427 (line)]] | wt | 64.8 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.50× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A498 (line)]] | wt | 90.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +11.7) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[HS-578T (line)]] | alt | 68.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.7) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[LOX-IMVI (line)]] | wt | 68.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 72.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +10.7) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[NCI-H23 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 118 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.9) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[A549 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 77.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 68.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 109 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 108 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 76.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 83.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9470), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB7A]] | +0.75 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[PLIN3]] | +0.66 | +0.49 / +0.70 | both halves | 1e-05 |  |
| [[SPATA2L]] | +0.65 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[ID1]] | +0.64 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[IER2]] | +0.63 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[IER5]] | +0.63 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[AREG]] | +0.63 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ATG2A]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[HES1]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[NTMT1]] | +0.61 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[SERTAD1]] | +0.60 | +0.66 / +0.59 | both halves | 7e-06 | STRING 478 |
| [[DUSP6]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NNT]] | -0.67 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[UBQLN1]] | -0.66 | -0.70 / -0.59 | both halves | 7e-06 |  |
| [[EIF2D]] | -0.66 | -0.48 / -0.71 | both halves | 2e-05 |  |
| [[DNAJC13]] | -0.64 | -0.57 / -0.68 | both halves | 1e-05 |  |
| [[CIAO2A]] | -0.64 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[RAB11FIP2]] | -0.60 | -0.39 / -0.69 | both halves | 5e-05 |  |
| [[PGRMC1]] | -0.59 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[EEF1A1P5]] | -0.59 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[PRDX3]] | -0.59 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[MANEA]] | -0.58 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[STRADB]] | -0.58 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[CRYZ]] | -0.58 | -0.62 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SH2D3A]] | B | SH2D3A activity raises MIDN's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 1.43× lower at baseline in the lines without SH2D3A | 0.028 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[TRIM15]] | B | TRIM15 activity raises MIDN's level | lines that do not express TRIM15 (34) vs lines expressing it (16) | 1.49× lower at baseline in the lines without TRIM15 | 0.034 | ⚠ within organs, on part of the lines; also absent: TMEM45B, EPS8L3, ENSG00000225680 |
| [[KLF5]] | B | KLF5 activity raises MIDN's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 1.41× lower at baseline in the lines without KLF5 | 0.044 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 192]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.50; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.1, 1.6); signed map (4.3, 25.6). **Vector** length 145, 51.1% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.4 | +3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +5.2 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +4.2 | +5.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +4.2 | +8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.6 | +2.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +3.1 | +2.6 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -11.5 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -11.0 | -1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -9.5 | -0.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -9.5 | -7.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.6 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.9 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.6 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | midnolin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,248,553-1,259,143 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Stx |
| Matched by | ensembl_id |

**Function**, from UniProt [Q504T8](https://www.uniprot.org/uniprotkb/Q504T8) (Midnolin):

> Facilitates the ubiquitin-independent proteasomal degradation of stimulus-induced transcription factors such as FOSB, EGR1, NR4A1, and IRF4 to the proteasome for degradation. Promotes also the degradation of other substrates such as CBX4 (By similarity). Plays a role in inhibiting the activity of glucokinase GCK and both glucose-induced and basal insulin secretion.

**Summary**, from NCBI Gene [90007](https://www.ncbi.nlm.nih.gov/gene/90007):

> Enables molecular adaptor activity. Involved in proteasomal ubiquitin-independent protein catabolic process. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16298](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16298) · Entrez [90007](https://www.ncbi.nlm.nih.gov/gene/90007) · UniProt [Q504T8](https://www.uniprot.org/uniprotkb/Q504T8) · Ensembl [ENSG00000167470](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167470)

## Data

Gene col 9470: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9470); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9470, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9470]; `tensor/DDL_lfc|DDL_z.npy` [9470]; `embed/gene_vectors.npy` [9470]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9470 or target_col == 9470). Every well: [[MIDN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIDN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
