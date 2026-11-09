---
symbol: "SVIL-AS1-1"
type: "gene"
col: 16579
ensembl_id: "ENSG00000291093"
name: ""
location: ""
module: 221
arm: "+"
pooled_cpm: 50.93
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 8
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/221"]
generated_by: "tahoemap"
---

# SVIL-AS1-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.29× (z +4.8, q 7e-04, up in 28 of 47 measured lines) ⚠ cell-cycle shift, explains ~18% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.24× (z +4.3, q 0.006, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.722× (z -9.0, q 9e-17, down in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~71% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.825× (z -5.3, q 1e-05, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (A-172 0.283×, NCI-H1792 0.254×, NCI-H1573 0.288×, RPMI-7951 0.301×, …; ⚠ cell-cycle shift, explains ~71% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-1 0.132×, LS 180 0.112×, KATO III 0.244×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.170×, NCI-H1573 0.178×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (HOP62 0.481×, SNU-1 0.466×); [[Auranofin (drug)]] 5 µM in 1 line (A-172 0.438×); [[Malotilate (drug)]] 0.05 µM in 1 line (SW 1088 0.0777×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC15A4]] (+0.62, fdr 1e-05), [[EIF4E3]] (+0.61, fdr 1e-05), [[SGPP1]] (+0.60, fdr 1e-05); moves opposite to [[NR4A3]] (-0.58, fdr 2e-05), [[HES1]] (-0.56, fdr 1e-05), [[ATP7A]] (-0.52, fdr 3e-05).
> It is in [[Module 221]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC27A4]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16579.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.29×** | +4.8 | 7e-04 | 28/47 (C-33 A, RKO, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +4.3 | 0.006 | 24/47 (RKO, RPMI-7951, …) | rises with dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.9 | 0.021 | 12/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.030 | 17/48 (C-33 A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.20×** | +3.6 | 0.033 | 16/48 (CFPAC-1, LS 180, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.5 | 0.046 | 11/49 (HepG2/C3A, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.19× | +3.4 | 0.064 | 18/48 (MIA PaCa-2, HepG2/C3A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.12× | +3.2 | 0.11 | 11/48 (CFPAC-1, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.11 | 8/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.19× | +3.0 | 0.14 | 16/49 (SW480, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16579.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (A-172 0.283×, NCI-H1792 0.254×, NCI-H1573 0.288×, RPMI-7951 0.301×, …; ⚠ cell-cycle shift, explains ~71% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-1 0.132×, LS 180 0.112×, KATO III 0.244×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.170×, NCI-H1573 0.178×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 2 lines (HOP62 0.481×, SNU-1 0.466×); [[Auranofin (drug)]] 5 µM in 1 line (A-172 0.438×); [[Malotilate (drug)]] 0.05 µM in 1 line (SW 1088 0.0777×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.722×** | -9.0 | 9e-17 | 28/48 (A-172, NCI-H1792, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.701×** | -7.0 | 1e-09 | 28/48 (BT-474, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.710×** | -6.2 | 1e-07 | 25/44 (RKO, NCI-H1573, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.825×** | -5.3 | 1e-05 | 24/48 (SNU-1, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.596×** | -5.3 | 1e-05 | 27/49 (A-172, SK-MEL-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.668×** | -4.1 | 0.003 | 23/48 (A-172, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.866× | -4.0 | 0.006 | 18/48 (SNU-1, RPMI-7951, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | **0.827×** | -3.6 | 0.026 | 21/41 (SNU-1, LS 180, …) | all doses, flat | composition shift |
| [[Thymol (drug)]] 5 µM |  | 0.882× | -3.5 | 0.034 | 10/48 (Panc 03.27, Hs 766T, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | 0.883× | -3.4 | 0.034 | 11/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.835× | -3.4 | 0.035 | 22/48 (AN3 CA, A-172, …) | top dose only | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.724×** | -3.3 | 0.045 | 16/47 (CFPAC-1, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~67% of this change | 0.840× | -3.3 | 0.045 | 18/47 (A549, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16579. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 93.7 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -21.0) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.438× (z -9.7) |
| [[HOP62 (line)]] | alt | 56.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -12.7) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.481× (z -10.2) |
| [[J82 (line)]] | alt | 74.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -9.7) ⚠ cell-cycle shift, explains ~71% of this change |
| [[RPMI-7951 (line)]] | alt | 93.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -15.6) ⚠ cell-cycle shift, explains ~71% of this change |
| [[SNU-1 (line)]] | wt | 133 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.466× (z -10.2) |
| [[A498 (line)]] | wt | 28.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -8.9) ⚠ cell-cycle shift, explains ~71% of this change |
| [[A549 (line)]] | wt | 85.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -15.6) ⚠ cell-cycle shift, explains ~71% of this change |
| [[HS-578T (line)]] | alt | 74.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -14.0) ⚠ cell-cycle shift, explains ~71% of this change |
| [[NCI-H1573 (line)]] | alt | 37.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -16.2) ⚠ cell-cycle shift, explains ~71% of this change |
| [[NCI-H1792 (line)]] | alt | 69.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -19.6) ⚠ cell-cycle shift, explains ~71% of this change |
| [[NCI-H460 (line)]] | wt | 46.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -14.0) ⚠ cell-cycle shift, explains ~71% of this change |
| [[AN3 CA (line)]] | alt | 66.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.108× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 75.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[C-33 A (line)]] | alt | 44.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[HepG2_C3A (line)]] | wt | 85.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change |
| [[KATO III (line)]] | alt | 43.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change |
| [[LOX-IMVI (line)]] | wt | 46.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -9.5) ⚠ cell-cycle shift, explains ~71% of this change |
| [[LS 180 (line)]] | wt | 38.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change |
| [[RKO (line)]] | wt | 71.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SK-MEL-2 (line)]] | alt | 80.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -10.9) ⚠ cell-cycle shift, explains ~71% of this change |
| [[SW 1088 (line)]] | alt | 90.0 | 0 | 1 | — | [[Malotilate (drug)]] 0.05 µM 0.0777× (z -8.9) |
| [[SW1417 (line)]] | alt | 61.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.418× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A-427 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 52.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 45.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16579), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC15A4]] | +0.62 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[EIF4E3]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[SGPP1]] | +0.60 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[KLC1]] | +0.59 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[FSD1L]] | +0.59 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[UBE2Q2P1]] | +0.59 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[BVES]] | +0.58 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[RECK]] | +0.58 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[CRLF3]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[RNF14]] | +0.57 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[NDFIP1]] | +0.56 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[PRELID3A]] | +0.56 | +0.53 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR4A3]] | -0.58 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[HES1]] | -0.56 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[ATP7A]] | -0.52 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[FOS]] | -0.52 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[SCG2]] | -0.51 | -0.55 / -0.40 | both halves | 4e-05 |  |
| [[PLEKHG2]] | -0.51 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[SLC12A2]] | -0.51 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[NSUN6]] | -0.51 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[NASP]] | -0.50 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[EXTL2]] | -0.49 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[ARL5B]] | -0.48 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[MAML2]] | -0.48 | -0.42 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC27A4]] | C | SLC27A4's natural level strengthens SVIL-AS1-1's drug response | SLC27A4's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse -0.16; direction not clear | 0.091 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 221]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.8, -1.1); signed map (-37.8, -4.7). **Vector** length 99.6, 23.4% of its response variance represented; |z| ≥ 3 in 861 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.9 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.6 | +3.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.3 | +3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +4.1 | +4.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +4.1 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.7 | +1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.6 | +1.5 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.4 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -6.3 | -9.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.2 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -4.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -3.3 | -3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.9 | -2.2 |
|  | [[Estrone sulfate (potassium) (drug)]] 5 µM |  | -1.6 | -1.5 |

## What is on record

> [!warning] No registry record
> SVIL-AS1-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16579: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16579); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16579, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16579]; `tensor/DDL_lfc|DDL_z.npy` [16579]; `embed/gene_vectors.npy` [16579]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16579 or target_col == 16579). Every well: [[SVIL-AS1-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SVIL-AS1-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
