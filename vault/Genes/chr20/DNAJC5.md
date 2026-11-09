---
symbol: "DNAJC5"
type: "gene"
col: 2080
ensembl_id: "ENSG00000101152"
name: "DnaJ heat shock protein family (Hsp40) member C5"
location: "20q13.33"
module: 134
arm: "+"
pooled_cpm: 113.38
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# DNAJC5

*DnaJ heat shock protein family (Hsp40) member C5* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.32× (z +5.4, q 3e-05, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.320× (z -21.0, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.663× (z -7.6, q 4e-12, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPG]] (+0.74, fdr 7e-06), [[CSNK1E]] (+0.72, fdr 7e-06), [[MYO9B]] (+0.72, fdr 7e-06); moves opposite to [[ZNF644]] (-0.71, fdr 7e-06), [[CC2D2A]] (-0.69, fdr 1e-05), [[ZNF280D]] (-0.66, fdr 7e-06).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2080.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +5.4 | 3e-05 | 38/48 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.27×** | +4.6 | 0.001 | 26/48 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +4.4 | 0.002 | 20/49 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.25×** | +4.3 | 0.003 | 29/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.005 | 30/48 (CFPAC-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.027 | 20/48 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.20×** | +3.6 | 0.029 | 23/48 (NCI-H1573, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2080.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.320×** | -21.0 | 0e+00 | 42/44 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.389×** | -18.1 | 0e+00 | 47/49 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.551×** | -10.6 | 8e-24 | 42/45 (SW 900, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.689×** | -10.1 | 1e-21 | 36/48 (J82, CFPAC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.663×** | -7.6 | 4e-12 | 37/48 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.708×** | -6.4 | 2e-08 | 34/47 (C-33 A, C32, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.728×** | -6.1 | 9e-08 | 33/48 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -4.9 | 8e-05 | 3/50 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.801×** | -4.2 | 0.001 | 27/48 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -4.2 | 0.002 | 18/48 (NCI-H2347, J82, …) | top dose only | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.862× | -4.0 | 0.003 | 12/48 (LoVo, NCI-H460, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.680×** | -3.9 | 0.005 | 27/47 (HCT15, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **0.817×** | -3.9 | 0.005 | 26/48 (HCT15, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.818×** | -3.8 | 0.005 | 24/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.842× | -3.3 | 0.040 | 19/48 (LOX-IMVI, C-33 A, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.844× | -3.2 | 0.044 | 14/48 (NCI-H1792, A549, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.845× | -3.2 | 0.045 | 17/48 (KATO III, J82, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.851× | -3.1 | 0.063 | 18/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.851× | -3.1 | 0.063 | 14/47 (A498, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2080. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 85.7 | 0 | 9 (8 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.363× (z -13.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.365× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 157 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.279× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 149 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.314× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 133 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -15.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 150 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -16.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[J82 (line)]] | alt | 139 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -21.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 107 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.268× (z -13.7) |
| [[AsPC-1 (line)]] | alt | 345 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0973× (z -25.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.307× (z -12.9) |
| [[NCI-H2030 (line)]] | alt | 163 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -14.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 87.2 | 1 (1 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.7) ⚠ cell-cycle shift, explains ~17% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.427× (z -10.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 96.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.335× (z -9.6) |
| [[HOP62 (line)]] | alt | 103 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -12.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 95.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -11.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HT-29 (line)]] | alt | 132 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.345× (z -13.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 90.5 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.93× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.418× (z -10.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 81.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.476× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 112 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.08× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -9.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 82.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.356× (z -10.0) |
| [[SNU-423 (line)]] | alt | 99.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -14.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SW 1088 (line)]] | alt | 96.4 | 0 | 3 | — | [[Fenofibrate (drug)]] 0.5 µM 0.0856× (z -9.5) |
| [[SW480 (line)]] | alt | 79.5 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.23× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -19.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 110 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -14.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 86.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -25.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -20.6) |
| [[A549 (line)]] | wt | 86.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -18.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 197 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.218× (z -15.1) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 78.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.61× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -11.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 88.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -12.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 125 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -17.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 74.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -10.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.486× (z -9.1) |
| [[Hs 766T (line)]] | wt | 182 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -13.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 81.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -9.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 78.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0799× (z -26.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 136 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.281× (z -13.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 80.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.406× (z -11.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 117 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -17.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -19.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -14.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 160 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.311× (z -17.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 175 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -11.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -9.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 80.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -11.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 98.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 89.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2080), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPG]] | +0.74 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[CSNK1E]] | +0.72 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[MYO9B]] | +0.72 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[TMEM184B]] | +0.71 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[MAP2K1]] | +0.70 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[UBA6]] | +0.68 | +0.75 / +0.49 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.67 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[KDM4B]] | +0.67 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[SLC35E1]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[EEF1AKMT4]] | +0.66 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[PIGF]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[GUK1]] | +0.66 | +0.68 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF644]] | -0.71 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[CC2D2A]] | -0.69 | -0.74 / -0.51 | both halves | 1e-05 |  |
| [[ZNF280D]] | -0.66 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[BCLAF1]] | -0.65 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[ATF7IP]] | -0.65 | -0.68 / -0.48 | both halves | 2e-05 |  |
| [[MED12]] | -0.63 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[TAPBPL]] | -0.63 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[SCAF8]] | -0.62 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[C11orf58]] | -0.62 | -0.65 / -0.43 | both halves | 3e-05 |  |
| [[ZNF776]] | -0.62 | -0.62 / -0.57 | both halves | 8e-06 |  |
| [[ATRX]] | -0.62 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[ZNF608]] | -0.62 | -0.59 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers DNAJC5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (4.2, 1.6); signed map (-34.1, 19.1). **Vector** length 129, 41.0% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.2 | +5.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.0 | +4.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.6 | +4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.0 | +4.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.8 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.1 | +2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.3 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -10.6 | -10.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.6 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.4 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.8 | -10.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.3 | -21.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | -0.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.1 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.1 | -3.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.0 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member C5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:63,895,126-63,936,031 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00118, FLJ13070, DNAJC5A; previously CLN4 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins; MicroRNA protein coding host genes |
| Reactome | 9 pathways, smallest: GABA synthesis, release, reuptake and degradation; Neurotransmitter release cycle; Sensory processing of sound by inner hair cells of the cochlea |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H3Z4](https://www.uniprot.org/uniprotkb/Q9H3Z4) (DnaJ homolog subfamily C member 5):

> Acts as a general chaperone in regulated exocytosis (By similarity). Acts as a co-chaperone for the SNARE protein SNAP-25 (By similarity). Involved in the calcium-mediated control of a late stage of exocytosis (By similarity). May have an important role in presynaptic function. May be involved in calcium-dependent neurotransmitter release at nerve endings (By similarity).

**Summary**, from NCBI Gene [80331](https://www.ncbi.nlm.nih.gov/gene/80331):

> This gene is a member of the J protein family. J proteins function in many cellular processes by regulating the ATPase activity of 70 kDa heat shock proteins. The encoded protein plays a role in membrane trafficking and protein folding, and has been shown to have anti-neurodegenerative properties. The encoded protein is known to play a role in cystic fibrosis and Huntington's disease. A pseudogene of this gene is located on the short arm of chromosome 8. [provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:16235](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16235) · Entrez [80331](https://www.ncbi.nlm.nih.gov/gene/80331) · UniProt [Q9H3Z4](https://www.uniprot.org/uniprotkb/Q9H3Z4) · Ensembl [ENSG00000101152](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101152)

## Data

Gene col 2080: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2080); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2080, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2080]; `tensor/DDL_lfc|DDL_z.npy` [2080]; `embed/gene_vectors.npy` [2080]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2080 or target_col == 2080). Every well: [[DNAJC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
