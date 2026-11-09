---
symbol: "NHP2"
type: "gene"
col: 7041
ensembl_id: "ENSG00000145912"
name: "NHP2 ribonucleoprotein"
location: "5q35.3"
module: 23
arm: "-"
pooled_cpm: 38.88
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# NHP2

*NHP2 ribonucleoprotein* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.05× (z +10.4, q 1e-22, up in 44 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (NCI-H1573 13.1×, HOP62 8.38×, NCI-H460 6.91×, SW480 7.11×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 7.87×, LOX-IMVI 6.27×, HOP62 6.37×, MIA PaCa-2 7.30×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.530× (z -6.2, q 3e-07, down in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (RKO 0.169×, SK-MEL-2 0.303×, SW480 0.323×, NCI-H2030 0.346×).
> Its strongest partners by |cos| (62 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 39 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C20orf27]] (+0.70, fdr 3e-04), [[TUFM]] (+0.70, fdr 1e-05), [[SNRPD2]] (+0.69, fdr 4e-05); moves opposite to [[ATE1OSP]] (-0.68, fdr 9e-04, ⚠ one half only (not replicated)), [[ZNF764]] (-0.67, fdr 9e-04, ⚠ one half only (not replicated)), [[ATF5]] (-0.66, fdr 4e-04), [[EIF5]] (-0.66, fdr 8e-05), [[NQO1-DT]] (-0.65, fdr 3e-04).
> It sits in the **-** arm of [[Module 023]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 10 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7041.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (NCI-H1573 13.1×, HOP62 8.38×, NCI-H460 6.91×, SW480 7.11×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 7.87×, LOX-IMVI 6.27×, HOP62 6.37×, MIA PaCa-2 7.30×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **5.05×** | +10.4 | 1e-22 | 44/44 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **4.12×** | +9.4 | 1e-18 | 39/39 (LoVo, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.82×** | +6.7 | 5e-09 | 40/42 (HOP62, LS 180, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.91×** | +4.5 | 9e-04 | 41/48 (NCI-H1573, HOP62, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **1.85×** | +4.3 | 0.002 | 33/46 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~66% of this change | **1.77×** | +4.0 | 0.007 | 37/46 (HOP62, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~59% of this change | **1.76×** | +3.8 | 0.013 | 36/47 (NCI-H1573, C32, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.70×** | +3.7 | 0.016 | 32/48 (NCI-H1573, SNU-423, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.5 | 0.025 | 33/46 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.68×** | +3.5 | 0.031 | 27/48 (LOX-IMVI, SNU-423, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 1.58× | +3.1 | 0.11 | 31/48 (HS-578T, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7041.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (RKO 0.169×, SK-MEL-2 0.303×, SW480 0.323×, NCI-H2030 0.346×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.530×** | -6.2 | 3e-07 | 39/48 (RKO, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | 0.403× | -3.3 | 0.29 | 37/47 (NCI-H23, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.580× | -3.1 | 0.39 | 25/48 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, +0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7041. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 30.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.47× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HCT15 (line)]] | alt | 29.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.75× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HEC-1-A (line)]] | alt | 49.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.06× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HOP62 (line)]] | alt | 25.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.38× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HT-29 (line)]] | alt | 28.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.92× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[KATO III (line)]] | alt | 35.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[LoVo (line)]] | wt | 31.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.87× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[LOX-IMVI (line)]] | wt | 37.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.97× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 35.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.13× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H460 (line)]] | wt | 36.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.91× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[PANC-1 (line)]] | alt | 52.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.58× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 66.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.55× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -10.7) |
| [[SW480 (line)]] | alt | 37.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.11× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -9.1) |
| [[A498 (line)]] | wt | 48.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[AsPC-1 (line)]] | alt | 26.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[C32 (line)]] | wt | 19.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.12× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[Hs 766T (line)]] | wt | 42.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.38× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[HS-578T (line)]] | alt | 52.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[LS 180 (line)]] | wt | 36.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.29× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H1573 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.1× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H1792 (line)]] | alt | 17.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.6× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H2030 (line)]] | alt | 48.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 49.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.77× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H2347 (line)]] | alt | 47.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 52.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[RKO (line)]] | wt | 43.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -12.9) |
| [[SNU-423 (line)]] | alt | 24.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.76× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SW 900 (line)]] | alt | 58.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.95× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SW1417 (line)]] | alt | 48.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[A-172 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7041), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*29 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C20orf27]] | +0.70 | +0.64 / +0.27 | both halves | 3e-04 |  |
| [[TUFM]] | +0.70 | +0.71 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 424 |
| [[SNRPD2]] | +0.69 | +0.64 / +0.42 | both halves | 4e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 745 |
| [[PRELID1]] | +0.68 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[LSM4]] | +0.67 | +0.70 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 505 |
| [[CENPX]] | +0.65 | +0.55 / +0.41 | both halves | 4e-05 | pathway: Chromosome Maintenance |
| [[TMEM160]] | +0.65 | +0.51 / +0.35 | both halves | 1e-04 |  |
| [[NME2]] | +0.64 | +0.74 / +0.47 | both halves | 2e-05 |  |
| [[TMEM147]] | +0.64 | +0.60 / +0.47 | both halves | 2e-05 | STRING 449 |
| [[METAP1]] | +0.63 | +0.61 / +0.33 | both halves | 1e-04 | STRING 482 |
| [[SMYD3]] | +0.62 | +0.49 / +0.26 | both halves | 4e-04 |  |
| [[ANAPC11]] | +0.62 | +0.47 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*71 of its nearest partners move opposite, 37 of them with an alert (⚠; 37 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATE1OSP]] | -0.68 | -0.64 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[ZNF764]] | -0.67 | -0.63 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[ATF5]] | -0.66 | -0.56 / -0.25 | both halves | 4e-04 |  |
| [[EIF5]] | -0.66 | -0.47 / -0.37 | both halves | 8e-05 | STRING 628 |
| [[THAP2]] | -0.66 | -0.62 / -0.04 | ⚠ one half (not replicated) | 0.006 |  |
| [[NQO1-DT]] | -0.65 | -0.60 / -0.27 | both halves | 3e-04 |  |
| [[TMEM202-AS1]] | -0.65 | -0.49 / -0.24 | both halves | 5e-04 |  |
| [[OXA1L-DT]] | -0.65 | -0.52 / -0.27 | both halves | 3e-04 |  |
| [[PPP1R12A-AS2]] | -0.65 | -0.55 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[C19orf54]] | -0.64 | -0.55 / -0.25 | both halves | 4e-04 |  |
| [[KCNMB3]] | -0.64 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[ZNF181]] | -0.63 | -0.61 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[NEB]] | -0.62 | -0.52 / -0.24 | both halves | 5e-04 |  |
| [[FAM120AOS]] | -0.62 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[CDK3]] | -0.62 | -0.63 / -0.29 | both halves | 3e-04 |  |
| [[LPXN]] | -0.61 | -0.49 / -0.20 | both halves | 7e-04 |  |
| [[AKT1S1]] | -0.61 | -0.51 / -0.24 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.645). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-51.0, -20.0); signed map (-51.4, -19.5). **Vector** length 57.4, 18.0% of its response variance represented; |z| ≥ 3 in 629 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +3.6 | +3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +3.6 | +4.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.6 | +0.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.3 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | -0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +0.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | +0.9 | +0.7 |
|  | [[Lopinavir (drug)]] 5 µM |  | +0.7 | +0.3 |
|  | [[8-Hydroxyquinoline (drug)]] 5 µM |  | +0.6 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.9 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | +1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.6 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.1 | +1.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | NHP2 ribonucleoprotein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:178,149,463-178,153,894 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20479; previously NOLA2 |
| Gene groups (HGNC) | H/ACA ribonucleoprotein complex; Telomerase holoenzyme subunits |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, MYC_TARGETS_V1 |
| Reactome | 9 pathways, smallest: Telomere Extension By Telomerase; Extension of Telomeres; rRNA modification in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX24](https://www.uniprot.org/uniprotkb/Q9NX24) (H/ACA ribonucleoprotein complex subunit 2):

> Required for ribosome biogenesis and telomere maintenance. Part of the H/ACA small nucleolar ribonucleoprotein (H/ACA snoRNP) complex, which catalyzes pseudouridylation of rRNA. This involves the isomerization of uridine such that the ribose is subsequently attached to C5, instead of the normal N1. Each rRNA can contain up to 100 pseudouridine ('psi') residues, which may serve to stabilize the conformation of rRNAs. May also be required for correct processing or intranuclear trafficking of …

**Summary**, from NCBI Gene [55651](https://www.ncbi.nlm.nih.gov/gene/55651):

> This gene is a member of the H/ACA snoRNPs (small nucleolar ribonucleoproteins) gene family. snoRNPs are involved in various aspects of rRNA processing and modification and have been classified into two families: C/D and H/ACA. The H/ACA snoRNPs also include the DKC1, NOLA1 and NOLA3 proteins. These four H/ACA snoRNP proteins localize to the dense fibrillar components of nucleoli and to coiled (Cajal) bodies in the nucleus. Both 18S rRNA production and rRNA pseudouridylation are impaired if any …

**Accessions** — [HGNC:14377](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14377) · Entrez [55651](https://www.ncbi.nlm.nih.gov/gene/55651) · UniProt [Q9NX24](https://www.uniprot.org/uniprotkb/Q9NX24) · Ensembl [ENSG00000145912](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145912)

## Data

Gene col 7041: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7041); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7041, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7041]; `tensor/DDL_lfc|DDL_z.npy` [7041]; `embed/gene_vectors.npy` [7041]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7041 or target_col == 7041). Every well: [[NHP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NHP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
