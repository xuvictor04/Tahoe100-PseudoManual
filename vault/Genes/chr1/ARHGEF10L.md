---
symbol: "ARHGEF10L"
type: "gene"
col: 1096
ensembl_id: "ENSG00000074964"
name: "Rho guanine nucleotide exchange factor 10 like"
location: "1p36.13"
module: 148
arm: "-"
pooled_cpm: 43.65
n_lines_expressing: 47
n_dd_up: 5
n_dd_down: 30
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# ARHGEF10L

*Rho guanine nucleotide exchange factor 10 like* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.32× (z +4.5, q 0.004, up in 20 of 43 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.22× (z +3.9, q 0.033, up in 16 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (17 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.356× (z -28.0, q 0e+00, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEMA4D]] (+0.62, fdr 1e-05), [[RALGPS1]] (+0.58, fdr 2e-05), [[USH1C]] (+0.57, fdr 2e-05); moves opposite to [[SLC30A9]] (-0.57, fdr 1e-05), [[PCNX4]] (-0.54, fdr 3e-05), [[RB1]] (-0.53, fdr 2e-05).
> It sits in the **-** arm of [[Module 148]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1096.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.32×** | +4.5 | 0.004 | 20/43 (H4, NCI-H2030, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.033 | 16/45 (NCI-H460, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.20×** | +3.7 | 0.045 | 16/46 (HepG2/C3A, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.082 | 13/43 (H4, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.20×** | +3.3 | 0.082 | 11/44 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.082 | 13/44 (hTERT-HPNE, SW48, …) | rises with dose | low cells (technical?) |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.10 | 10/45 (A-172, COLO 205, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.18× | +3.2 | 0.11 | 16/45 (HepG2/C3A, KATO III, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.11 | 15/45 (SW480, HepG2/C3A, …) | all doses, flat |  |
| [[Neratinib (drug)]] 5 µM |  | 1.17× | +3.0 | 0.14 | 9/45 (C-33 A, A549, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 21 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1096.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.356×** | -28.0 | 0e+00 | 42/44 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.373×** | -26.7 | 0e+00 | 40/45 (COLO 205, RKO, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.389×** | -18.1 | 0e+00 | 36/44 (COLO 205, LS 180, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.344×** | -17.3 | 0e+00 | 30/34 (HS-578T, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.448×** | -15.4 | 0e+00 | 40/45 (LS 180, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.457×** | -15.0 | 0e+00 | 37/45 (LS 180, COLO 205, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.481×** | -14.0 | 1e-42 | 34/44 (RKO, COLO 205, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.498×** | -13.3 | 9e-39 | 37/45 (LS 180, COLO 205, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.445×** | -13.1 | 1e-37 | 35/45 (COLO 205, MIA PaCa-2, …) | rises with dose | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.503×** | -11.2 | 3e-27 | 37/45 (HT-29, A-172, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.673×** | -10.7 | 5e-25 | 36/45 (SNU-423, SW1417, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.358×** | -10.3 | 4e-23 | 36/46 (LS 180, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.560×** | -10.3 | 4e-23 | 30/39 (SW480, RKO, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.547×** | -9.8 | 6e-21 | 34/44 (HS-578T, NCI-H23, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.619×** | -9.2 | 2e-18 | 32/45 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.691×** | -7.1 | 4e-11 | 28/45 (COLO 205, HT-29, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.525×** | -6.5 | 3e-09 | 22/43 (LS 180, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.601×** | -5.1 | 8e-06 | 20/44 (HT-29, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.769×** | -5.0 | 1e-05 | 22/46 (NCI-H2347, Panc 03.27, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.811×** | -4.0 | 0.001 | 19/44 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.686×** | -3.8 | 0.003 | 14/44 (SW 900, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.731×** | -3.1 | 0.029 | 13/43 (A498, SW 1088, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 5 µM |  | 0.900× | -2.8 | 0.073 | 7/45 (CHP-212, A-427, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.904× | -2.7 | 0.099 | 6/45 (HS-578T, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1096. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 146 | 0 | 16 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0772× (z -32.7) |
| [[COLO 205 (line)]] | alt | 255 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0922× (z -37.6) |
| [[LS 180 (line)]] | wt | 162 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -21.7) |
| [[MIA PaCa-2 (line)]] | alt | 29.9 | 0 | 13 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -15.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -11.5) |
| [[A-172 (line)]] | wt | 40.8 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -14.5) |
| [[HS-578T (line)]] | alt | 70.7 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -23.9) |
| [[NCI-H2347 (line)]] | alt | 53.9 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -18.5) |
| [[SW480 (line)]] | alt | 38.4 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0981× (z -23.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -14.9) |
| [[A498 (line)]] | wt | 65.1 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -16.9) |
| [[CFPAC-1 (line)]] | alt | 59.0 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -28.1) |
| [[NCI-H460 (line)]] | wt | 18.7 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -15.9) |
| [[RKO (line)]] | wt | 50.2 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0720× (z -23.5) |
| [[SW 900 (line)]] | alt | 36.1 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -14.9) |
| [[SW48 (line)]] | wt | 72.1 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -17.9) |
| [[LoVo (line)]] | wt | 29.5 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -20.0) |
| [[HEC-1-A (line)]] | alt | 56.7 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 35.4 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -14.9) |
| [[SW1417 (line)]] | alt | 51.6 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -18.9) |
| [[HOP62 (line)]] | alt | 29.5 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -11.3) |
| [[J82 (line)]] | alt | 39.1 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -19.7) |
| [[NCI-H1573 (line)]] | alt | 40.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -20.5) |
| [[Panc 03.27 (line)]] | alt | 28.2 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -14.8) |
| [[AN3 CA (line)]] | alt | 43.1 | 0 | 3 (2 ⚠) | — | [[Pimozide (drug)]] 0.05 µM 0.0914× (z -10.0) |
| [[C-33 A (line)]] | alt | 34.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -14.5) |
| [[HCT15 (line)]] | alt | 44.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -14.1) |
| [[hTERT-HPNE (line)]] | wt | 28.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 20.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0938× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 20.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -18.0) |
| [[SNU-1 (line)]] | wt | 48.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -13.9) |
| [[SNU-423 (line)]] | alt | 26.7 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -13.0) |
| [[A-427 (line)]] | wt | 21.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.278× (z -9.2) |
| [[C32 (line)]] | wt | 31.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -13.6) |
| [[RPMI-7951 (line)]] | alt | 31.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0956× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -11.6) |
| [[A549 (line)]] | wt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -12.3) |
| [[HepG2_C3A (line)]] | wt | 101 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -11.3) |
| [[KATO III (line)]] | alt | 25.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -11.2) |
| [[SHP-77 (line)]] | alt | 45.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.10 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.98 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.94 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1096), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEMA4D]] | +0.62 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[RALGPS1]] | +0.58 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[USH1C]] | +0.57 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[FAM102A]] | +0.56 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[FGD3]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 | same gene group; pathway: Cell death signalling via NRAGE, NRIF and NADE |
| [[HDHD3]] | +0.55 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[ST3GAL4]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[DNMT3B]] | +0.54 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[PRR5]] | +0.54 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[PIK3C2B]] | +0.53 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[TSPAN33]] | +0.53 | +0.39 / +0.43 | both halves | 6e-05 |  |
| [[USP2]] | +0.53 | +0.45 / +0.47 | both halves | 3e-05 | pathway: Death Receptor Signaling |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC30A9]] | -0.57 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[PCNX4]] | -0.54 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[RB1]] | -0.53 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[BZW1]] | -0.51 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[PRKAR1A]] | -0.50 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[C6orf120]] | -0.49 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[MCTS1]] | -0.48 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[EGFR]] | -0.48 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[CAV1]] | -0.48 | -0.52 / -0.37 | both halves | 8e-05 | pathway: RHOA GTPase cycle |
| [[ZBTB38]] | -0.47 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[SPRY2]] | -0.47 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[PRKG1-AS1]] | -0.47 | -0.46 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ARHGEF10L's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BLVRA]] | B | BLVRA activity lowers ARHGEF10L's level | lines that do not express BLVRA (5) vs lines expressing it (45) | 3.41× higher at baseline in the lines without BLVRA | 0.060 | ⚠ within organs, on part of the lines; also absent: GABBR1, SOAT1, DBN1; its own permutation p |
| [[PRKG1-AS1]] | B | PRKG1-AS1 activity lowers ARHGEF10L's level | lines that do not express PRKG1-AS1 (15) vs lines expressing it (35) | 2.07× higher at baseline in the lines without PRKG1-AS1 | 0.067 | ⚠ within organs, on part of the lines; also absent: HERC5, RAB31, GALC |
| [[PSMB5]] | B | PSMB5 activity lowers ARHGEF10L's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ADGRG1]] | B | ADGRG1 activity raises ARHGEF10L's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 1.58× lower at baseline in the lines without ADGRG1 | 0.071 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[ADCY4]] | B | ADCY4 activity raises ARHGEF10L's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 1.53× lower at baseline in the lines without ADCY4 | 0.082 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **-** arm (projection on the module's main direction -0.489). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (0.7, 4.8); signed map (-19.2, 32.8). **Vector** length 96.9, 26.3% of its response variance represented; |z| ≥ 3 in 1,304 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.4 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +5.4 | +3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~85% of this change | +4.8 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.7 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +0.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.4 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +1.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.7 | -10.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.4 | -8.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -14.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -3.6 | -8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -10.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.8 | -1.2 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -2.3 | -1.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -2.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 10 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:17,539,698-17,697,874 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10521, KIAA1626 |
| Gene groups (HGNC) | Dbl family Rho GEFs |
| Reactome | 13 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; RHOB GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCE6](https://www.uniprot.org/uniprotkb/Q9HCE6) (Rho guanine nucleotide exchange factor 10-like protein):

> Acts as a guanine nucleotide exchange factor (GEF) for RHOA, RHOB and RHOC.

**Summary**, from NCBI Gene [55160](https://www.ncbi.nlm.nih.gov/gene/55160):

> This gene belongs to the RhoGEF subfamily of RhoGTPases. Members of this subfamily are activated by specific guanine nucleotide exchange factors (GEFs) and are involved in signal transduction. The encoded protein shows cytosolic distribution. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:25540](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25540) · Entrez [55160](https://www.ncbi.nlm.nih.gov/gene/55160) · UniProt [Q9HCE6](https://www.uniprot.org/uniprotkb/Q9HCE6) · Ensembl [ENSG00000074964](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074964)

## Data

Gene col 1096: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1096); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1096, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1096]; `tensor/DDL_lfc|DDL_z.npy` [1096]; `embed/gene_vectors.npy` [1096]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1096 or target_col == 1096). Every well: [[ARHGEF10L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF10L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
