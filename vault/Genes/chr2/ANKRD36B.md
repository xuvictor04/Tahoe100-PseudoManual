---
symbol: "ANKRD36B"
type: "gene"
col: 12301
ensembl_id: "ENSG00000196912"
name: "ankyrin repeat domain 36B"
location: "2q11.2"
module: 175
arm: "+"
pooled_cpm: 58.28
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 36
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# ANKRD36B

*ankyrin repeat domain 36B* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.34× (z +4.2, q 0.016, up in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 1.50×, NCI-H23 1.44×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.292× (z -23.0, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD36]] (+0.83, fdr 7e-06), [[KATNAL1]] (+0.65, fdr 7e-06), [[HACE1]] (+0.64, fdr 1e-05); moves opposite to [[DDX5]] (-0.55, fdr 2e-05), [[MED13]] (-0.54, fdr 4e-05), [[PTPRK]] (-0.54, fdr 4e-05).
> It is in [[Module 175]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12301.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 1.50×, NCI-H23 1.44×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.016 | 29/48 (RKO, NCI-H1573, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.63×** | +3.6 | 0.079 | 24/48 (LoVo, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.26× | +3.3 | 0.21 | 17/48 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.21 | 16/48 (AsPC-1, HOP62, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.18× | +3.1 | 0.21 | 14/48 (Hs 766T, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12301.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.292×** | -23.0 | 0e+00 | 46/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.311×** | -16.0 | 0e+00 | 45/48 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.356×** | -14.7 | 0e+00 | 44/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.427×** | -12.1 | 2e-31 | 44/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.544×** | -11.3 | 2e-27 | 42/48 (C32, J82, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.489×** | -10.2 | 3e-22 | 39/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.502×** | -9.8 | 1e-20 | 40/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.509×** | -9.6 | 5e-20 | 40/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.527×** | -9.1 | 6e-18 | 39/48 (HOP62, SW 1271, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.308×** | -8.8 | 1e-16 | 42/49 (NCI-H460, Hs 766T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.544×** | -8.6 | 3e-16 | 43/48 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.532×** | -8.5 | 1e-15 | 40/48 (HOP62, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.553×** | -8.4 | 2e-15 | 35/48 (HEC-1-A, SNU-423, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.573×** | -7.9 | 1e-13 | 33/48 (SNU-423, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.574×** | -7.9 | 1e-13 | 41/48 (HOP62, H4, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.689×** | -6.6 | 2e-09 | 35/48 (A-172, HOP62, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.522×** | -4.8 | 3e-05 | 24/48 (HOP62, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.727×** | -4.5 | 1e-04 | 27/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.680×** | -3.8 | 0.003 | 20/48 (MIA PaCa-2, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.776×** | -3.6 | 0.006 | 23/48 (J82, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12301. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 80.0 | 0 | 18 (9 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0771× (z -22.7) |
| [[A-172 (line)]] | wt | 87.7 | 0 | 16 (8 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0884× (z -20.9) |
| [[SNU-423 (line)]] | alt | 114 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0932× (z -21.1) |
| [[NCI-H460 (line)]] | wt | 55.8 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -20.0) |
| [[MIA PaCa-2 (line)]] | alt | 90.4 | 1 (1 ⚠) | 9 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.50× (z +10.7) ⚠ position not correctable | [[Harringtonine (drug)]] 5 µM 0.188× (z -12.7) |
| [[C32 (line)]] | wt | 69.2 | 0 | 9 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -15.8) |
| [[PANC-1 (line)]] | alt | 57.5 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -22.5) |
| [[HEC-1-A (line)]] | alt | 132 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -14.1) |
| [[LOX-IMVI (line)]] | wt | 41.7 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -12.3) |
| [[H4 (line)]] | wt | 65.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -19.8) |
| [[Hs 766T (line)]] | wt | 58.0 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -18.2) |
| [[HS-578T (line)]] | alt | 51.4 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -15.0) |
| [[J82 (line)]] | alt | 61.0 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -16.2) |
| [[RPMI-7951 (line)]] | alt | 74.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -17.9) |
| [[NCI-H1792 (line)]] | alt | 77.8 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -21.1) |
| [[SNU-1 (line)]] | wt | 187 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.237× (z -10.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.260× (z -9.3) |
| [[SW480 (line)]] | alt | 45.2 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.298× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 26.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -11.1) |
| [[A549 (line)]] | wt | 50.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -18.5) |
| [[NCI-H2030 (line)]] | alt | 34.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -13.3) |
| [[NCI-H2347 (line)]] | alt | 34.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -14.6) |
| [[AsPC-1 (line)]] | alt | 36.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -14.5) |
| [[CFPAC-1 (line)]] | alt | 49.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -15.6) |
| [[HCT15 (line)]] | alt | 66.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0641× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.222× (z -13.8) |
| [[hTERT-HPNE (line)]] | wt | 53.9 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.138× (z -11.8) |
| [[LS 180 (line)]] | wt | 64.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.328× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.360× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 174 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -16.8) |
| [[SK-MEL-2 (line)]] | alt | 35.7 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.101× (z -15.3) |
| [[A-427 (line)]] | wt | 50.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -16.2) |
| [[A498 (line)]] | wt | 19.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.6) |
| [[LoVo (line)]] | wt | 51.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.377× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.486× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 40.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -14.3) |
| [[SW 1088 (line)]] | alt | 71.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0333× (z -15.5) |
| [[C-33 A (line)]] | alt | 85.6 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.294× (z -8.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[COLO 205 (line)]] | alt | 35.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.227× (z -8.5) |
| [[HT-29 (line)]] | alt | 24.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -9.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 61.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.307× (z -8.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW 1271 (line)]] | alt | 66.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0463× (z -11.4) |
| [[SW 900 (line)]] | alt | 41.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -14.8) |
| [[SW48 (line)]] | wt | 76.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.292× (z -8.6) |
| [[AN3 CA (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12301), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD36]] | +0.83 | +0.86 / +0.80 | both halves | 7e-06 | STRING 983 |
| [[KATNAL1]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[HACE1]] | +0.64 | +0.70 / +0.57 | both halves | 1e-05 | same gene group |
| [[SRD5A1]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[DDHD2]] | +0.61 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[USP48]] | +0.60 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[MRI1]] | +0.60 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[HSPB11]] | +0.60 | +0.66 / +0.46 | both halves | 2e-05 |  |
| [[MMS19]] | +0.59 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[SMYD2]] | +0.59 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ANAPC4]] | +0.58 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[PRMT7]] | +0.58 | +0.51 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX5]] | -0.55 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[MED13]] | -0.54 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[PTPRK]] | -0.54 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[KYNU]] | -0.52 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[SON]] | -0.52 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[GARIN1B]] | -0.52 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[HIVEP2-DT]] | -0.52 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[LINC02284]] | -0.51 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[NFE2L2]] | -0.51 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[TRIP12]] | -0.50 | -0.56 / -0.32 | both halves | 2e-04 |  |
| [[CHMP1B]] | -0.50 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[STYXL1]] | -0.49 | -0.56 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ANKRD36B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CARD6]] | B | CARD6 activity lowers ANKRD36B's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 1.48× higher at baseline in the lines without CARD6 | 0.071 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU |
| [[HACE1]] | C | HACE1 activity raises ANKRD36B's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.74× lower at baseline in the lines without HACE1 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.673). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.6, -10.3); signed map (-36.7, -10.5). **Vector** length 84.0, 25.4% of its response variance represented; |z| ≥ 3 in 1,378 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +4.8 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +3.2 | -7.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +2.5 | -7.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.5 | -3.2 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.4 | +1.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.4 | +0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +0.9 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -10.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.2 | -16.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.7 | +2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.6 | -3.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.6 | -1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -1.8 |
|  | [[Thymol (drug)]] 5 µM |  | -2.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 36B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:97,492,663-97,589,877 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21281; previously KIAA1641 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q8N2N9](https://www.uniprot.org/uniprotkb/Q8N2N9) carries no function annotation.

**Summary**, from NCBI Gene [57730](https://www.ncbi.nlm.nih.gov/gene/57730):

> Enables identical protein binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29333](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29333) · Entrez [57730](https://www.ncbi.nlm.nih.gov/gene/57730) · UniProt [Q8N2N9](https://www.uniprot.org/uniprotkb/Q8N2N9) · Ensembl [ENSG00000196912](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196912)

## Data

Gene col 12301: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12301); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12301, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12301]; `tensor/DDL_lfc|DDL_z.npy` [12301]; `embed/gene_vectors.npy` [12301]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12301 or target_col == 12301). Every well: [[ANKRD36B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD36B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
