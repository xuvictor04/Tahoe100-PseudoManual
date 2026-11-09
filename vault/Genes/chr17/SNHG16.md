---
symbol: "SNHG16"
type: "gene"
col: 8724
ensembl_id: "ENSG00000163597"
name: "small nucleolar RNA host gene 16"
location: "17q25.1"
module: 33
arm: "+"
pooled_cpm: 60.04
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 3
n_dd_up_clean: 21
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# SNHG16

*small nucleolar RNA host gene 16* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (21 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.02× (z +11.5, q 6e-28, up in 38 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.59× (z +10.8, q 1e-24, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.720× (z -5.0, q 4e-04, down in 30 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.501×, CHP-212 0.368×; ⚠ cell-cycle shift, explains ~67% of this change); [[Bimiralisib (drug)]] 5 µM in 1 line (NCI-H596 0.164×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[URB1]] (+0.64, fdr 7e-06), [[DCAF13]] (+0.61, fdr 1e-05), [[RNPS1]] (+0.60, fdr 1e-05); moves opposite to [[GPKOW]] (-0.56, fdr 4e-05), [[DCTN3]] (-0.56, fdr 1e-05), [[UPF3B]] (-0.56, fdr 2e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MCOLN2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 22 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8724.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.02×** | +11.5 | 6e-28 | 38/46 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.07×** | +10.9 | 3e-25 | 39/43 (LoVo, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +10.8 | 1e-24 | 37/48 (A498, A549, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +10.5 | 1e-23 | 42/46 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +8.5 | 2e-15 | 43/48 (KATO III, SW480, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.69×** | +8.5 | 3e-15 | 39/49 (A498, NCI-H2347, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.63×** | +8.0 | 1e-13 | 36/48 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +7.9 | 2e-13 | 38/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.69×** | +7.8 | 3e-13 | 39/47 (SW480, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.61×** | +7.8 | 4e-13 | 33/48 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.67×** | +7.7 | 5e-13 | 35/45 (Panc 03.27, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +7.3 | 1e-11 | 35/48 (A-172, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.31×** | +7.1 | 4e-11 | 33/48 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **2.11×** | +6.4 | 8e-09 | 42/48 (KATO III, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.46×** | +6.2 | 2e-08 | 32/48 (A-172, SNU-423, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **2.04×** | +6.1 | 4e-08 | 36/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.89×** | +5.5 | 2e-06 | 35/48 (KATO III, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.31×** | +4.4 | 3e-04 | 21/48 (CFPAC-1, J82, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.68×** | +4.4 | 3e-04 | 26/48 (HEC-1-A, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.30×** | +4.3 | 4e-04 | 28/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +4.2 | 6e-04 | 21/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.001 | 25/48 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.41×** | +4.0 | 0.001 | 25/48 (KATO III, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.56×** | +3.8 | 0.002 | 21/48 (KATO III, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8724.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 0.501×, CHP-212 0.368×; ⚠ cell-cycle shift, explains ~67% of this change); [[Bimiralisib (drug)]] 5 µM in 1 line (NCI-H596 0.164×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.720×** | -5.0 | 4e-04 | 30/47 (LoVo, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.785×** | -3.9 | 0.026 | 21/49 (LoVo, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.807×** | -3.5 | 0.073 | 22/47 (LoVo, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.867× | -3.3 | 0.12 | 15/48 (LoVo, HOP62, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.806× | -3.3 | 0.12 | 17/47 (SW 1271, NCI-H2030, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.824× | -3.2 | 0.13 | 18/47 (SNU-423, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.858× | -3.0 | 0.19 | 18/48 (LoVo, C-33 A, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8724. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 54.5 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +9.1) | — |
| [[LoVo (line)]] | wt | 66.3 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +15.0) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[SW480 (line)]] | alt | 69.2 | 5 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.78× (z +12.9) | — |
| [[A-172 (line)]] | wt | 34.8 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +13.3) | — |
| [[KATO III (line)]] | alt | 64.9 | 4 (4 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.64× (z +12.3) ⚠ toxic | — |
| [[NCI-H460 (line)]] | wt | 67.9 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +11.2) | — |
| [[A498 (line)]] | wt | 82.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +15.3) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +15.1) | — |
| [[C32 (line)]] | wt | 55.5 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 60.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +20.5) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.21× (z +11.1) | — |
| [[A-427 (line)]] | wt | 67.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.22× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -10.4) ⚠ cell-cycle shift, explains ~67% of this change |
| [[HEC-1-A (line)]] | alt | 94.6 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.46× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 79.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[HT-29 (line)]] | alt | 37.8 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.30× (z +10.3) ⚠ toxic | — |
| [[NCI-H2347 (line)]] | alt | 54.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +13.4) | — |
| [[A549 (line)]] | wt | 73.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +14.9) | — |
| [[AsPC-1 (line)]] | alt | 23.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +11.0) | — |
| [[BT-474 (line)]] | alt | 34.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 33.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[CHP-212 (line)]] | wt | 152 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -9.6) ⚠ cell-cycle shift, explains ~67% of this change |
| [[HepG2_C3A (line)]] | wt | 74.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.6) | — |
| [[HS-578T (line)]] | alt | 38.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 45.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 52.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.62× (z +9.5) ⚠ toxic | — |
| [[NCI-H1573 (line)]] | alt | 36.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.95× (z +8.6) ⚠ toxic | — |
| [[NCI-H596 (line)]] | alt | 58.7 | 0 | 1 | — | [[Bimiralisib (drug)]] 5 µM 0.164× (z -9.1) |
| [[SW 900 (line)]] | alt | 36.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 70.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 112 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 77.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 71.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8724), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[URB1]] | +0.64 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[DCAF13]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[RNPS1]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[NSUN2]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[AHCY]] | +0.59 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[EIF2S3]] | +0.59 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[PTRH2]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[EARS2]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[EIF3B]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[SNHG29]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 | same gene group |
| [[TRAP1]] | +0.56 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[FAM53A]] | +0.56 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPKOW]] | -0.56 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[DCTN3]] | -0.56 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[UPF3B]] | -0.56 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[WBP4]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[SCAF11]] | -0.54 | -0.38 / -0.62 | both halves | 6e-05 |  |
| [[PPP1R12A]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[ZNF214]] | -0.53 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[XRN1]] | -0.51 | -0.31 / -0.60 | both halves | 2e-04 |  |
| [[HMGN2P5]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[TRMT1L]] | -0.51 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[PHIP]] | -0.51 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[RSF1]] | -0.50 | -0.31 / -0.58 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCOLN2]] | B | MCOLN2 activity raises SNHG16's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.17× lower at baseline in the lines without MCOLN2 | 0.032 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[MAP2K1]] | B | MAP2K1 activity raises SNHG16's level | compounds that target MAP2K1: 2 of 4 lower it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.6% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NBEAP2]] | B | NBEAP2 activity raises SNHG16's level | lines that do not express NBEAP2 (5) vs lines expressing it (45) | 1.87× lower at baseline in the lines without NBEAP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: C2orf27A, ROPN1L, ENSG00000287621 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.483). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-24.3, -38.6); signed map (-14.1, -57.7). **Vector** length 97.3, 28.4% of its response variance represented; |z| ≥ 3 in 1,232 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.3 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +7.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +3.1 |
|  | [[EX229 (drug)]] 5 µM |  | +5.0 | +6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.9 | +10.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.4 | +6.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.2 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +7.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.1 | -2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | +1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -3.0 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 16 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q25.1 — chr17:76,557,727-76,670,985 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ncRAN, Nbla12061, Nbla10727, ELNAT1 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100507246](https://www.ncbi.nlm.nih.gov/gene/100507246):

> Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:44352](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44352) · Entrez [100507246](https://www.ncbi.nlm.nih.gov/gene/100507246) · Ensembl [ENSG00000163597](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163597)

## Data

Gene col 8724: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8724); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8724, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8724]; `tensor/DDL_lfc|DDL_z.npy` [8724]; `embed/gene_vectors.npy` [8724]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8724 or target_col == 8724). Every well: [[SNHG16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
