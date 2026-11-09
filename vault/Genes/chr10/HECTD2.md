---
symbol: "HECTD2"
type: "gene"
col: 9109
ensembl_id: "ENSG00000165338"
name: "HECT domain E3 ubiquitin protein ligase 2"
location: "10q23.32"
module: 10
arm: "+"
pooled_cpm: 32.17
n_lines_expressing: 45
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 6
direction_downstream: 12
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# HECTD2

*HECT domain E3 ubiquitin protein ligase 2* — 10q23.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.95× (z +11.6, q 1e-28, up in 31 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.575× (z -9.7, q 2e-19, down in 25 of 32 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.684× (z -6.9, q 1e-09, down in 29 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (hTERT-HPNE 0.0868×, Panc 03.27 0.174×, A-427 0.245×, C32 0.214×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (RKO 0.216×, A-172 0.355×, HepG2/C3A 0.214×, NCI-H2030 0.328×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (SNU-423 0.396×, A-172 0.462×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (COLO 205 0.0654×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (H4 0.193×).
> Its strongest partners by |cos| (76 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUTM2E]] (+0.64, fdr 5e-05), [[WAC-AS1]] (+0.64, fdr 9e-05), [[ATE1OSP]] (+0.63, fdr 3e-04); moves opposite to [[RAB3A]] (-0.63, fdr 9e-05), [[DNAAF3]] (-0.61, fdr 2e-04), [[P4HB]] (-0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[GCNT4]] → it (grade B ⚠); 12 go from it, the strongest it → [[MR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9109.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **1.95×** | +11.6 | 1e-28 | 31/43 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +8.5 | 5e-15 | 26/43 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +8.2 | 4e-14 | 27/43 (RKO, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.35×** | +7.7 | 3e-12 | 29/43 (PANC-1, CFPAC-1, …) | top dose only | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +6.2 | 7e-08 | 22/43 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +6.2 | 7e-08 | 24/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.7 | 1e-06 | 21/42 (A498, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +4.8 | 1e-04 | 20/43 (LOX-IMVI, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +4.5 | 5e-04 | 18/42 (PANC-1, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.011 | 15/43 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.037 | 15/43 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.10 | 8/43 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.18× | +3.0 | 0.10 | 10/43 (A-172, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9109.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (hTERT-HPNE 0.0868×, Panc 03.27 0.174×, A-427 0.245×, C32 0.214×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (RKO 0.216×, A-172 0.355×, HepG2/C3A 0.214×, NCI-H2030 0.328×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (SNU-423 0.396×, A-172 0.462×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (COLO 205 0.0654×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (H4 0.193×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.575×** | -9.7 | 2e-19 | 25/32 (hTERT-HPNE, Panc 03.27, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.684×** | -6.9 | 1e-09 | 29/43 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.693×** | -6.7 | 5e-09 | 28/43 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.716×** | -6.1 | 2e-07 | 24/39 (RKO, A-172, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.744×** | -5.4 | 9e-06 | 24/43 (H4, SNU-423, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **0.767×** | -4.8 | 1e-04 | 19/41 (H4, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 0.877× | -3.4 | 0.057 | 15/43 (SK-MEL-2, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9109. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 63.3 | 8 (3 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.64× (z +16.5) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.223× (z -8.7) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 36.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.1) | — |
| [[A-172 (line)]] | wt | 70.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.462× (z -8.8) |
| [[H4 (line)]] | wt | 55.7 | 0 | 3 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.182× (z -11.7) ⚠ transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.193× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 42.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[NCI-H1573 (line)]] | alt | 34.5 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 8.12× (z +17.0) | — |
| [[NCI-H2030 (line)]] | alt | 44.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A549 (line)]] | wt | 34.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 34.5 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.86× (z +10.6) | [[Bortezomib (drug)]] 5 µM 0.125× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 32.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[RKO (line)]] | wt | 50.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SHP-77 (line)]] | alt | 17.9 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0719× (z -14.2) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Palmatine (chloride) (drug)]] 0.5 µM 0.193× (z -9.2) |
| [[SNU-423 (line)]] | alt | 66.2 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.396× (z -9.0) |
| [[A-427 (line)]] | wt | 41.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 46.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[COLO 205 (line)]] | alt | 14.2 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0654× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.336× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 49.1 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.75× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 25.4 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.24× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 37.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0868× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 18.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 26.3 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.79× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW 900 (line)]] | alt | 33.3 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 4.49× (z +10.6) | — |
| [[A498 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.67 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.24 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.13 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9109), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 23 of them with an alert (⚠; 23 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUTM2E]] | +0.64 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[WAC-AS1]] | +0.64 | +0.46 / +0.36 | both halves | 9e-05 |  |
| [[ATE1OSP]] | +0.63 | +0.48 / +0.27 | both halves | 3e-04 |  |
| [[RNF146]] | +0.63 | +0.46 / +0.39 | both halves | 6e-05 |  |
| [[PPP3CB-AS1]] | +0.63 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[THBS4]] | +0.63 | +0.51 / +0.24 | both halves | 4e-04 |  |
| [[GCNT4]] | +0.62 | +0.44 / +0.24 | both halves | 4e-04 |  |
| [[PATL2]] | +0.62 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[RBM26-AS1]] | +0.62 | +0.49 / +0.37 | both halves | 7e-05 |  |
| [[PBLD]] | +0.61 | +0.39 / +0.20 | ⚠ not reproduced | 8e-04 |  |
| [[BCDIN3D]] | +0.60 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[TTC32]] | +0.60 | +0.43 / +0.35 | both halves | 1e-04 |  |
| [[PBDC1]] | +0.60 | +0.48 / +0.29 | both halves | 2e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3A]] | -0.63 | -0.42 / -0.37 | both halves | 9e-05 |  |
| [[DNAAF3]] | -0.61 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[P4HB]] | -0.56 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[GNAI2]] | -0.56 | -0.36 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[ATRN]] | -0.55 | -0.42 / -0.36 | both halves | 1e-04 |  |
| [[GLG1]] | -0.54 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[ANKRD27]] | -0.53 | -0.37 / -0.25 | both halves | 4e-04 |  |
| [[GMCL1]] | -0.53 | -0.41 / -0.37 | both halves | 9e-05 |  |
| [[IFT172]] | -0.53 | -0.35 / -0.27 | both halves | 3e-04 |  |
| [[MPND]] | -0.53 | -0.25 / -0.31 | both halves | 4e-04 |  |
| [[CAMK2G]] | -0.53 | -0.31 / -0.32 | both halves | 2e-04 |  |
| [[RNF41]] | -0.52 | -0.35 / -0.23 | both halves | 5e-04 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GCNT4]] | B | GCNT4 activity raises HECTD2's level | lines that do not express GCNT4 (10) vs lines expressing it (40) | 1.90× lower at baseline in the lines without GCNT4 | 0.025 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers HECTD2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises HECTD2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PYGO1]] | B | PYGO1 activity raises HECTD2's level | lines that do not express PYGO1 (16) vs lines expressing it (34) | 2.62× lower at baseline in the lines without PYGO1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A; also absent: MIR130AHG, RBMS3, TCF7L1 |
| [[FLRT2]] | B | FLRT2 activity raises HECTD2's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 1.79× lower at baseline in the lines without FLRT2 | 0.099 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| [[DPH6-DT]] | C | DPH6-DT activity raises HECTD2's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 1.68× lower at baseline in the lines without DPH6-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MR1]] | B | HECTD2 activity raises MR1's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 3.45× lower at baseline in the lines without HECTD2 | 0.035 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[TRAM2-AS1]] | B | HECTD2 activity raises TRAM2-AS1's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 1.59× lower at baseline in the lines without HECTD2 | 0.050 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[PCED1A]] | B | HECTD2 activity raises PCED1A's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 2.17× lower at baseline in the lines without HECTD2 | 0.065 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[N4BP2L1]] | B | HECTD2 activity raises N4BP2L1's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 1.77× lower at baseline in the lines without HECTD2 | 0.071 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[POU6F1]] | B | HECTD2 activity raises POU6F1's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 1.96× lower at baseline in the lines without HECTD2 | 0.073 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[ZKSCAN7-AS1]] | B | HECTD2 activity raises ZKSCAN7-AS1's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 1.52× lower at baseline in the lines without HECTD2 | 0.077 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[LHFPL6]] | B | HECTD2 activity raises LHFPL6's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 7.05× lower at baseline in the lines without HECTD2 | 0.079 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[CATSPERE]] | B | HECTD2 activity raises CATSPERE's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 1.88× lower at baseline in the lines without HECTD2 | 0.087 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[RXYLT1]] | B | HECTD2 activity raises RXYLT1's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 1.81× lower at baseline in the lines without HECTD2 | 0.090 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[MAD2L1-DT]] | B | HECTD2 activity raises MAD2L1-DT's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 2.14× lower at baseline in the lines without HECTD2 | 0.091 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[SEPTIN7-DT]] | B | HECTD2 activity raises SEPTIN7-DT's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 2.13× lower at baseline in the lines without HECTD2 | 0.098 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[HDGFL3]] | C | HECTD2 activity raises HDGFL3's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 8.85× lower at baseline in the lines without HECTD2 | 0.096 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.562). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (3.7, 13.2); signed map (23.8, -14.9). **Vector** length 90.2, 19.0% of its response variance represented; |z| ≥ 3 in 882 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +8.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +5.5 | +7.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.1 | +2.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +11.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +3.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | +1.6 | +0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | -0.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.3 | -6.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.8 | -6.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.3 | -5.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -0.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | HECT domain E3 ubiquitin protein ligase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.32 — chr10:91,409,280-91,514,829 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37306 |
| Gene groups (HGNC) | HECT domain E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5U5R9](https://www.uniprot.org/uniprotkb/Q5U5R9) (Probable E3 ubiquitin-protein ligase HECTD2):

> E3 ubiquitin-protein ligase which accepts ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfers the ubiquitin to targeted substrates.; (Microbial infection) Catalyzes ubiquitination of Botulinum neurotoxin A light chain (LC) of C.botulinum neurotoxin type A (BoNT/A).

**Summary**, from NCBI Gene [143279](https://www.ncbi.nlm.nih.gov/gene/143279):

> Predicted to enable ubiquitin protein ligase activity. Predicted to be involved in protein polyubiquitination. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26736](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26736) · Entrez [143279](https://www.ncbi.nlm.nih.gov/gene/143279) · UniProt [Q5U5R9](https://www.uniprot.org/uniprotkb/Q5U5R9) · Ensembl [ENSG00000165338](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165338)

## Data

Gene col 9109: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9109); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9109, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9109]; `tensor/DDL_lfc|DDL_z.npy` [9109]; `embed/gene_vectors.npy` [9109]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9109 or target_col == 9109). Every well: [[HECTD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HECTD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
