---
symbol: "SEPTIN9"
type: "gene"
col: 11562
ensembl_id: "ENSG00000184640"
name: "septin 9"
location: "17q25.3"
module: 101
arm: "+"
pooled_cpm: 404.37
n_lines_expressing: 47
n_dd_up: 0
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 10
direction_downstream: 3
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# SEPTIN9

*septin 9* — 17q25.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1573 2.05×, RKO 2.08×, MIA PaCa-2 1.85×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 2.67×, NCI-H460 1.83×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 1.78×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 1.64×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 1.90×).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.609× (z -15.5, q 0e+00, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHB]] (+0.58, fdr 1e-05), [[MPRIP]] (+0.57, fdr 1e-05), [[ITGA3]] (+0.55, fdr 1e-05); moves opposite to [[RWDD3]] (-0.51, fdr 5e-05), [[RNPC3]] (-0.48, fdr 3e-05), [[LSM8]] (-0.48, fdr 3e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[MYEOV]] → it (grade B ⚠); 3 go from it, the strongest it → [[NIBAN2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11562.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H1573 2.05×, RKO 2.08×, MIA PaCa-2 1.85×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 2.67×, NCI-H460 1.83×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 1.78×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 1.64×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 1.90×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.12× | +3.7 | 0.14 | 7/45 (NCI-H2347, SW1417, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.19 | 19/44 (H4, SW48, …) | two highest doses | low cells (technical?) |
| [[PH-797804 (drug)]] 0.05 µM |  | 1.17× | +3.3 | 0.19 | 13/45 (A498, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11562.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.609×** | -15.5 | 0e+00 | 36/46 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.661×** | -13.0 | 6e-36 | 34/45 (SK-MEL-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.601×** | -10.8 | 4e-25 | 36/44 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.650×** | -9.5 | 2e-19 | 35/45 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.668×** | -8.9 | 4e-17 | 28/45 (A-172, PANC-1, …) | two highest doses | cell-cycle shift (explains ~16% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.678×** | -8.6 | 7e-16 | 32/45 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.680×** | -8.5 | 1e-15 | 33/45 (LoVo, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.704×** | -7.8 | 5e-13 | 31/45 (A-172, PANC-1, …) | two highest doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.725×** | -7.1 | 7e-11 | 32/45 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.743×** | -6.3 | 1e-08 | 24/45 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.826×** | -6.0 | 1e-07 | 22/45 (SK-MEL-2, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **0.757×** | -5.9 | 2e-07 | 24/44 (HOP62, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.776×** | -5.6 | 9e-07 | 26/45 (SK-MEL-2, A-172, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.626×** | -5.4 | 2e-06 | 32/44 (NCI-H460, SW48, …) | top dose only | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.811×** | -4.6 | 1e-04 | 23/45 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.837× | -3.9 | 0.002 | 20/45 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.840× | -3.8 | 0.003 | 21/45 (HOP62, A-172, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.723×** | -3.8 | 0.005 | 23/46 (Panc 03.27, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | 0.844× | -3.7 | 0.005 | 21/45 (NCI-H1792, A549, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.846× | -3.7 | 0.006 | 20/46 (LOX-IMVI, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11562. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 978 | 0 | 23 (13 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -16.0) |
| [[PANC-1 (line)]] | alt | 1,019 | 0 | 15 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -20.5) |
| [[A-172 (line)]] | wt | 791 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.247× (z -20.0) |
| [[LS 180 (line)]] | wt | 306 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -16.7) |
| [[SK-MEL-2 (line)]] | alt | 480 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -18.4) |
| [[HEC-1-A (line)]] | alt | 531 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -20.9) |
| [[hTERT-HPNE (line)]] | wt | 490 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.340× (z -11.4) |
| [[LoVo (line)]] | wt | 230 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -18.2) |
| [[NCI-H1792 (line)]] | alt | 516 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -19.3) |
| [[RPMI-7951 (line)]] | alt | 237 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.405× (z -10.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.434× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 430 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -13.9) |
| [[J82 (line)]] | alt | 327 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.402× (z -12.4) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.586× (z -10.7) |
| [[KATO III (line)]] | alt | 593 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -14.4) |
| [[Panc 03.27 (line)]] | alt | 540 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -13.0) |
| [[AsPC-1 (line)]] | alt | 327 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -9.9) |
| [[BT-474 (line)]] | alt | 363 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -13.9) |
| [[C32 (line)]] | wt | 436 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.559× (z -11.3) |
| [[HS-578T (line)]] | alt | 309 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.613× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 219 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.85× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -21.9) |
| [[NCI-H2030 (line)]] | alt | 195 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 179 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.587× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 224 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +11.1) | — |
| [[SW480 (line)]] | alt | 463 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -14.5) |
| [[COLO 205 (line)]] | alt | 354 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.422× (z -9.8) |
| [[HCT15 (line)]] | alt | 304 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -10.7) |
| [[HT-29 (line)]] | alt | 403 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 164 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.67× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 415 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -12.4) |
| [[A498 (line)]] | wt | 471 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.561× (z -8.8) ⚠ toxic |
| [[A549 (line)]] | wt | 405 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.540× (z -9.1) ⚠ toxic |
| [[H4 (line)]] | wt | 337 | 1 (1 ⚠) | 0 | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.26× (z +8.9) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[Hs 766T (line)]] | wt | 334 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.414× (z -9.7) ⚠ toxic |
| [[RKO (line)]] | wt | 121 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 194 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.65× (z +9.7) | — |
| [[SNU-1 (line)]] | wt | 237 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -14.2) |
| [[SNU-423 (line)]] | alt | 430 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -11.5) |
| [[SW1417 (line)]] | alt | 251 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -11.5) |
| [[SW48 (line)]] | wt | 514 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -9.6) |
| [[A-427 (line)]] | wt | 99.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 159 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 54.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 662 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 434 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 158 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 329 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 353 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 88.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 413 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 313 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11562), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHB]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[MPRIP]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 | STRING 511 |
| [[ITGA3]] | +0.55 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[KRT8]] | +0.55 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[ARHGAP23]] | +0.55 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[STK10]] | +0.54 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[KIAA0930]] | +0.54 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[CORO1C]] | +0.54 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ANO1]] | +0.54 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[IGSF9B]] | +0.53 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[MYH9]] | +0.53 | +0.49 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[TGFA]] | +0.52 | +0.59 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RWDD3]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[RNPC3]] | -0.48 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[LSM8]] | -0.48 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[RCHY1]] | -0.48 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[HOXA5]] | -0.47 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[PEX11A]] | -0.46 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[ZBED3]] | -0.45 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[TRA2A]] | -0.45 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[SLC19A2]] | -0.45 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[ZCCHC8]] | -0.44 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[PNISR]] | -0.44 | -0.46 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYEOV]] | B | MYEOV activity raises SEPTIN9's level | lines that do not express MYEOV (19) vs lines expressing it (31) | 1.67× lower at baseline in the lines without MYEOV | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000260877, MALL, LAMC2 |
| [[TINAGL1]] | B | TINAGL1 activity raises SEPTIN9's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.60× lower at baseline in the lines without TINAGL1 | 0.013 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[ADAM19]] | B | ADAM19 activity raises SEPTIN9's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 1.60× lower at baseline in the lines without ADAM19 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[COL7A1]] | B | COL7A1 activity raises SEPTIN9's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 1.86× lower at baseline in the lines without COL7A1 | 0.021 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[ITGA3]] | B | ITGA3 activity raises SEPTIN9's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 2.16× lower at baseline in the lines without ITGA3 | 0.032 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[PITPNM3]] | B | PITPNM3 activity lowers SEPTIN9's level | lines that do not express PITPNM3 (5) vs lines expressing it (45) | 1.82× higher at baseline in the lines without PITPNM3 | 0.040 | ⚠ within organs, on part of the lines; also absent: DOK4; maybe low, not absent |
| [[SH3BP2]] | B | SH3BP2 activity raises SEPTIN9's level | lines that do not express SH3BP2 (8) vs lines expressing it (42) | 1.91× lower at baseline in the lines without SH3BP2 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CD44]] | B | CD44 activity raises SEPTIN9's level | lines that do not express CD44 (15) vs lines expressing it (35) | 1.62× lower at baseline in the lines without CD44 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[SMAD3]] | C | SMAD3 activity raises SEPTIN9's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 3.10× lower at baseline in the lines without SMAD3 | 0.011 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent; co-absent with the target |
| [[NIBAN2]] | C | NIBAN2 activity raises SEPTIN9's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 3.01× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NIBAN2]] | C | SEPTIN9 activity raises NIBAN2's level | lines that do not express SEPTIN9 (3) vs lines expressing it (47) | 6.36× lower at baseline in the lines without SEPTIN9 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent; co-absent with the target; its own permutation p |
| [[SHB]] | C | SEPTIN9 activity raises SHB's level | lines that do not express SEPTIN9 (3) vs lines expressing it (47) | 4.15× lower at baseline in the lines without SEPTIN9 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent; co-absent with the target; its own permutation p |
| [[HRH1]] | C | SEPTIN9 activity raises HRH1's level | lines that do not express SEPTIN9 (3) vs lines expressing it (47) | 5.17× lower at baseline in the lines without SEPTIN9 | 0.096 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with WNK2; also absent: SLC2A1, CEMIP2, S100A13; maybe low, not absent |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.435). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.9, 51.5); signed map (-10.6, 37.8). **Vector** length 123, 40.8% of its response variance represented; |z| ≥ 3 in 1,465 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +0.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +3.3 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +2.4 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +0.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.2 | -10.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.9 | -6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.1 | -7.1 |
|  | [[NG25 (drug)]] 5 µM |  | -4.8 | -5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -15.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.5 | -1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.3 | -3.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -3.1 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | septin 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:77,280,569-77,500,596 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MSF1, KIAA0991, PNUTL4, AF17q25, SeptD1; previously MSF, SEPT9 |
| Gene groups (HGNC) | Septins |
| Hallmark sets | MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHD8](https://www.uniprot.org/uniprotkb/Q9UHD8) (Septin-9):

> Filament-forming cytoskeletal GTPase (By similarity). May play a role in cytokinesis (Potential). May play a role in the internalization of 2 intracellular microbial pathogens, Listeria monocytogenes and Shigella flexneri.

**Summary**, from NCBI Gene [10801](https://www.ncbi.nlm.nih.gov/gene/10801):

> This gene is a member of the septin family involved in cytokinesis and cell cycle control. This gene is a candidate for the ovarian tumor suppressor gene. Mutations in this gene cause hereditary neuralgic amyotrophy, also known as neuritis with brachial predilection. A chromosomal translocation involving this gene on chromosome 17 and the MLL gene on chromosome 11 results in acute myelomonocytic leukemia. Multiple alternatively spliced transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:7323](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7323) · Entrez [10801](https://www.ncbi.nlm.nih.gov/gene/10801) · UniProt [Q9UHD8](https://www.uniprot.org/uniprotkb/Q9UHD8) · Ensembl [ENSG00000184640](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184640)

## Data

Gene col 11562: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11562); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11562, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11562]; `tensor/DDL_lfc|DDL_z.npy` [11562]; `embed/gene_vectors.npy` [11562]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11562 or target_col == 11562). Every well: [[SEPTIN9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEPTIN9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
