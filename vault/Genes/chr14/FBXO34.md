---
symbol: "FBXO34"
type: "gene"
col: 10982
ensembl_id: "ENSG00000178974"
name: "F-box protein 34"
location: "14q22.3"
module: 40
arm: "+"
pooled_cpm: 140.35
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# FBXO34

*F-box protein 34* — 14q22.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 1.91×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.26×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.354× (z -18.5, q 0e+00, down in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.569× (z -10.1, q 1e-21, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB6A]] (+0.61, fdr 7e-06), [[SDHAP4-1]] (+0.60, fdr 7e-06), [[TMEM165]] (+0.58, fdr 1e-05); moves opposite to [[PCNX2]] (-0.59, fdr 1e-05), [[USP40]] (-0.58, fdr 1e-05), [[SLX4IP]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KCNK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10982.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 1.91×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.26×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.0 | 0.98 | 1/50 (HOP62) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10982.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.354×** | -18.5 | 0e+00 | 49/49 (RKO, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.411×** | -15.3 | 0e+00 | 40/44 (J82, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.470×** | -12.3 | 1e-32 | 45/45 (HS-578T, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.569×** | -10.1 | 1e-21 | 42/48 (AN3 CA, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.576×** | -9.5 | 3e-19 | 41/48 (SNU-423, NCI-H1792, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.729×** | -8.0 | 1e-13 | 34/48 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.685×** | -6.8 | 1e-09 | 41/48 (HS-578T, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.717×** | -5.9 | 2e-07 | 39/48 (SW480, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.486×** | -5.9 | 3e-07 | 37/49 (CFPAC-1, RPMI-7951, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.723×** | -5.8 | 4e-07 | 31/48 (COLO 205, NCI-H460, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.749×** | -5.0 | 4e-05 | 34/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.845× | -4.3 | 9e-04 | 20/48 (HOP62, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.792×** | -4.2 | 0.001 | 28/48 (COLO 205, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.802×** | -3.9 | 0.003 | 25/48 (AsPC-1, BT-474, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~59% of this change | **0.803×** | -3.8 | 0.006 | 26/47 (NCI-H1792, LS 180, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.816×** | -3.6 | 0.009 | 28/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.828×** | -3.4 | 0.021 | 23/48 (NCI-H1573, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.695×** | -3.0 | 0.082 | 15/49 (CFPAC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.697×** | -2.9 | 0.085 | 21/48 (LOX-IMVI, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10982. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 237 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.393× (z -10.2) |
| [[HS-578T (line)]] | alt | 89.8 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.192× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.412× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 179 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.426× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 277 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -13.9) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.379× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 201 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.305× (z -13.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 109 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.510× (z -8.9) |
| [[SW 900 (line)]] | alt | 209 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 79.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.408× (z -10.7) |
| [[SNU-423 (line)]] | alt | 105 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -17.1) ⚠ cell-cycle shift, explains ~60% of this change |
| [[A549 (line)]] | wt | 132 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[AsPC-1 (line)]] | alt | 142 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.387× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.413× (z -9.8) |
| [[C-33 A (line)]] | alt | 143 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[COLO 205 (line)]] | alt | 192 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.419× (z -8.8) |
| [[H4 (line)]] | wt | 183 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HEC-1-A (line)]] | alt | 164 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.522× (z -9.0) |
| [[HOP62 (line)]] | alt | 137 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[hTERT-HPNE (line)]] | wt | 128 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -12.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 159 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 148 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H460 (line)]] | wt | 99.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.493× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[RKO (line)]] | wt | 98.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -26.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[RPMI-7951 (line)]] | alt | 125 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 113 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.561× (z -9.1) |
| [[A-427 (line)]] | wt | 107 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.396× (z -10.9) |
| [[AN3 CA (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -13.9) |
| [[BT-474 (line)]] | alt | 176 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[HepG2_C3A (line)]] | wt | 109 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[Hs 766T (line)]] | wt | 105 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.327× (z -9.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 99.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.489× (z -8.8) |
| [[J82 (line)]] | alt | 121 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 197 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 205 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H2030 (line)]] | alt | 120 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H23 (line)]] | alt | 170 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[PANC-1 (line)]] | alt | 85.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.359× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 161 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW48 (line)]] | wt | 159 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.369× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[CHP-212 (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.343× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LOX-IMVI (line)]] | wt | 88.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.469× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 189 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.344× (z -11.8) |
| [[SHP-77 (line)]] | alt | 159 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SK-MEL-2 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SNU-1 (line)]] | wt | 109 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -8.6) |
| [[SW 1088 (line)]] | alt | 126 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 0.05 µM 0.0990× (z -9.2) |
| [[C32 (line)]] | wt | 95.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 141 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10982), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB6A]] | +0.61 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[SDHAP4-1]] | +0.60 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[TMEM165]] | +0.58 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[PIK3C2A]] | +0.58 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[TULP3]] | +0.57 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[CERS5]] | +0.57 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[APAF1]] | +0.57 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[SDHAP2]] | +0.56 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SLC37A3]] | +0.55 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[IFI27L1]] | +0.55 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | +0.54 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[KLHL7]] | +0.53 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX2]] | -0.59 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[USP40]] | -0.58 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[SLX4IP]] | -0.56 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[RRP15]] | -0.56 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[LDAH]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[BBS10]] | -0.54 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[N6AMT1]] | -0.53 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | -0.53 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[CEP41]] | -0.53 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[UTP20]] | -0.52 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[TRIM44]] | -0.52 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[ZKSCAN3]] | -0.52 | -0.54 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNK1]] | B | KCNK1 activity strengthens FBXO34's drug response | lines that do not express KCNK1 (23) vs lines expressing it (26) | the lines without KCNK1 respond 0.73× as strongly (z diff +1.49); strongest at Homoharringtonine 5 µM: 0.77x vs 0.61x (z diff +3.2) | 0.020 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132; target measured in part of the lines; artifact flags |
| [[KCNK1]] | B | KCNK1 activity raises FBXO34's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 1.34× lower at baseline in the lines without KCNK1 | 0.024 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.578). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (3.5, -18.9); signed map (-45.1, 12.6). **Vector** length 104, 33.8% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.1 | +1.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +1.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | -1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | +3.3 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.7 | +0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | -0.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +0.9 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -5.4 | -5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.9 | -9.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.8 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -4.3 | -8.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.0 | -1.9 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | -2.7 | -1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 34 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.3 — chr14:55,271,344-55,370,053 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20725, Fbx34 |
| Gene groups (HGNC) | F-boxes other |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWN3](https://www.uniprot.org/uniprotkb/Q9NWN3) (F-box only protein 34):

> Substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex promoting ubiquitination and proteasomal degradation of specific target proteins including HNRNPU. Regulates both the G2/M transition and anaphase entry in meiotic oocytes (By similarity).; (Microbial infection) Plays a positive role in latent HIV-1 activation. Mechanistically, promotes hnRNP U/HNRNPU ubiquitination, which leads to its degradation and abolishment of the interaction between …

**Summary**, from NCBI Gene [55030](https://www.ncbi.nlm.nih.gov/gene/55030):

> Members of the F-box protein family, such as FBXO34, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (MIM 601434), cullin (see CUL1; MIM 603134), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:20201](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20201) · Entrez [55030](https://www.ncbi.nlm.nih.gov/gene/55030) · UniProt [Q9NWN3](https://www.uniprot.org/uniprotkb/Q9NWN3) · Ensembl [ENSG00000178974](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178974)

## Data

Gene col 10982: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10982); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10982, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10982]; `tensor/DDL_lfc|DDL_z.npy` [10982]; `embed/gene_vectors.npy` [10982]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10982 or target_col == 10982). Every well: [[FBXO34 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO34.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
