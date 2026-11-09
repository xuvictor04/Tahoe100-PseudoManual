---
symbol: "SNRPA"
type: "gene"
col: 1183
ensembl_id: "ENSG00000077312"
name: "small nuclear ribonucleoprotein polypeptide A"
location: "19q13.2"
module: 6
arm: "+"
pooled_cpm: 33.52
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# SNRPA

*small nuclear ribonucleoprotein polypeptide A* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.50× (z +12.8, q 1e-34, up in 42 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.83× (z +8.4, q 6e-15, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.618× (z -9.6, q 6e-19, down in 33 of 48 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.750× (z -5.8, q 2e-06, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLD1]] (+0.69, fdr 7e-06), [[TOMM40]] (+0.69, fdr 7e-06), [[RBM14-RBM4]] (+0.66, fdr 7e-06); moves opposite to [[ZNF627]] (-0.62, fdr 7e-06), [[HHLA3]] (-0.62, fdr 1e-05), [[TRMT1L]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF433]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1183.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.50×** | +12.8 | 1e-34 | 42/45 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.31×** | +11.2 | 9e-27 | 33/38 (AsPC-1, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.07×** | +9.4 | 1e-18 | 37/43 (SW480, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +8.4 | 6e-15 | 39/47 (SW480, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.53×** | +5.9 | 4e-07 | 29/46 (LS 180, NCI-H460, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +5.4 | 8e-06 | 27/47 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.46×** | +5.2 | 1e-05 | 27/48 (PANC-1, A498, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.46×** | +5.1 | 3e-05 | 29/46 (NCI-H460, Panc 03.27, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.0 | 0.004 | 25/45 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.29×** | +3.6 | 0.020 | 17/48 (NCI-H460, J82, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.29×** | +3.5 | 0.021 | 21/47 (SW480, PANC-1, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.5 | 0.025 | 0/48 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.26×** | +3.3 | 0.049 | 16/46 (NCI-H1573, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.085 | 17/46 (SW480, NCI-H2347, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.0 | 0.088 | 8/31 (NCI-H2347, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1183.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.618×** | -9.6 | 6e-19 | 33/48 (A-427, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.660×** | -5.9 | 1e-06 | 31/48 (A-427, LS 180, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.750×** | -5.8 | 2e-06 | 29/48 (SW480, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.741×** | -4.2 | 0.003 | 22/48 (A-427, LS 180, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.731×** | -4.1 | 0.004 | 23/48 (SK-MEL-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.826×** | -3.8 | 0.012 | 23/48 (LS 180, HT-29, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.824×** | -3.8 | 0.012 | 12/48 (HEC-1-A, A-427, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.776×** | -3.6 | 0.023 | 19/47 (LS 180, SW48, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.786×** | -3.3 | 0.064 | 15/46 (A-427, NCI-H2030, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.788× | -3.1 | 0.10 | 14/47 (SW480, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1183. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 51.0 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.227× (z -18.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.502× (z -8.8) |
| [[SW480 (line)]] | alt | 47.4 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.57× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -19.0) |
| [[A498 (line)]] | wt | 37.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Selinexor (drug)]] 5 µM 0.440× (z -10.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A549 (line)]] | wt | 46.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HCT15 (line)]] | alt | 35.9 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.264× (z -11.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.6) |
| [[HT-29 (line)]] | alt | 53.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -8.8) |
| [[KATO III (line)]] | alt | 44.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.55× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 22.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Selinexor (drug)]] 5 µM 0.427× (z -8.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[RKO (line)]] | wt | 57.7 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.365× (z -11.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.381× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 23.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.34× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[C-33 A (line)]] | alt | 43.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 23.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[COLO 205 (line)]] | alt | 29.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[H4 (line)]] | wt | 30.0 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.165× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 17.3 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0720× (z -11.6) |
| [[Hs 766T (line)]] | wt | 25.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.310× (z -10.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[LoVo (line)]] | wt | 28.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.431× (z -8.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[LOX-IMVI (line)]] | wt | 29.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.431× (z -8.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[LS 180 (line)]] | wt | 36.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.276× (z -16.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[MIA PaCa-2 (line)]] | alt | 43.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.337× (z -11.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1573 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.208× (z -13.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1792 (line)]] | alt | 21.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H23 (line)]] | alt | 37.8 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.325× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1183), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLD1]] | +0.69 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[TOMM40]] | +0.69 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[RBM14-RBM4]] | +0.66 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[CDC45]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[FANCA]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[POLA1]] | +0.63 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ATAD3A]] | +0.62 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[GGCT]] | +0.62 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[BRI3BP]] | +0.61 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[MSH2]] | +0.61 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[MCM8]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[WDR76]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF627]] | -0.62 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[HHLA3]] | -0.62 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[TRMT1L]] | -0.61 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[COMMD3]] | -0.60 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[CHMP2B]] | -0.60 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[SDSL]] | -0.59 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[TAB3]] | -0.59 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[OTUD7B]] | -0.58 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[TCEAL4]] | -0.58 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[ZNF44]] | -0.58 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[WAC-AS1]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[CLN5]] | -0.56 | -0.56 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF433]] | B | ZNF433 activity weakens SNRPA's drug response | lines that do not express ZNF433 (8) vs lines expressing it (40) | the lines without ZNF433 respond 1.22× as strongly (z diff -0.39); strongest at Dinaciclib 5 µM: 2.94x vs 1.99x (z diff -3.0) | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF563, ZNF442; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.559). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-28.9, -41.3); signed map (-34.3, -40.7). **Vector** length 80.1, 18.3% of its response variance represented; |z| ≥ 3 in 923 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F mediated regulation of DNA replication* (reactome, mean cos +0.51 to 9); *DNA replication initiation* (reactome, mean cos +0.53 to 6); *Inhibition of replication initiation of damaged DNA by RB1/E2F1* (reactome, mean cos +0.50 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.7 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.1 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +2.7 | +9.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +2.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.6 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +5.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +1.7 |
|  | [[EX229 (drug)]] 5 µM |  | +1.3 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -7.4 | -9.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | +0.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -4.5 | -5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein polypeptide A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:40,750,637-40,765,389 (+) |
| Ensembl biotype | protein_coding |
| Also known as | U1A, U1-A, Mud1 |
| Gene groups (HGNC) | RNA binding motif containing; U1 small nuclear ribonucleoprotein |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 6 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P09012](https://www.uniprot.org/uniprotkb/P09012) (U1 small nuclear ribonucleoprotein A):

> Component of the spliceosomal U1 snRNP, which is essential for recognition of the pre-mRNA 5' splice-site and the subsequent assembly of the spliceosome. U1 snRNP is the first snRNP to interact with pre-mRNA. This interaction is required for the subsequent binding of U2 snRNP and the U4/U6/U5 tri-snRNP. SNRPA binds stem loop II of U1 snRNA. In a snRNP-free form (SF-A) may be involved in coupled pre-mRNA splicing and polyadenylation process. May bind preferentially to the 5'-UGCAC-3' motif on …

**Summary**, from NCBI Gene [6626](https://www.ncbi.nlm.nih.gov/gene/6626):

> The protein encoded by this gene associates with stem loop II of the U1 small nuclear ribonucleoprotein, which binds the 5' splice site of precursor mRNAs and is required for splicing. The encoded protein autoregulates itself by polyadenylation inhibition of its own pre-mRNA via dimerization and has been implicated in the coupling of splicing and polyadenylation. [provided by RefSeq, Oct 2010]

**Accessions** — [HGNC:11151](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11151) · Entrez [6626](https://www.ncbi.nlm.nih.gov/gene/6626) · UniProt [P09012](https://www.uniprot.org/uniprotkb/P09012) · Ensembl [ENSG00000077312](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077312)

## Data

Gene col 1183: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1183); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1183, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1183]; `tensor/DDL_lfc|DDL_z.npy` [1183]; `embed/gene_vectors.npy` [1183]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1183 or target_col == 1183). Every well: [[SNRPA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRPA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
