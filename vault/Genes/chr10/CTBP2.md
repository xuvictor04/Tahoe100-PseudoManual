---
symbol: "CTBP2"
type: "gene"
col: 10552
ensembl_id: "ENSG00000175029"
name: "C-terminal binding protein 2"
location: "10q26.13"
module: 64
arm: "-"
pooled_cpm: 334.3
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 24
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# CTBP2

*C-terminal binding protein 2* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.21× (z +3.9, q 0.031, up in 23 of 46 measured lines) ⚠ toxic.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 0.05 µM in 2 lines (SW48 2.58×, BT-474 2.01×); [[Digitoxin (drug)]] 0.05 µM in 1 line (SW480 1.61×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.286× (z -27.1, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VAV2]] (+0.58, fdr 1e-05), [[SNX25]] (+0.56, fdr 1e-05), [[TENT4A]] (+0.53, fdr 5e-05); moves opposite to [[C12orf4]] (-0.61, fdr 1e-05), [[CHURC1]] (-0.58, fdr 1e-05), [[PGGT1B]] (-0.57, fdr 2e-05).
> It sits in the **-** arm of [[Module 064]] (proteasome).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10552.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 0.05 µM in 2 lines (SW48 2.58×, BT-474 2.01×); [[Digitoxin (drug)]] 0.05 µM in 1 line (SW480 1.61×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.21×** | +3.9 | 0.031 | 23/46 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.8 | 0.031 | 20/47 (H4, PANC-1, …) | rises with dose | composition shift |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.031 | 16/47 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.15 | 15/46 (SNU-423, SHP-77, …) | two highest doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.15 | 17/47 (SW480, H4, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 1.32× | +3.2 | 0.15 | 23/47 (SW48, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10552.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.286×** | -27.1 | 0e+00 | 47/47 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.302×** | -26.0 | 0e+00 | 47/47 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.451×** | -17.3 | 0e+00 | 47/47 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.642×** | -13.6 | 7e-40 | 35/47 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.543×** | -12.6 | 3e-34 | 44/46 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.544×** | -12.5 | 5e-34 | 40/43 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.615×** | -9.7 | 2e-20 | 39/44 (A549, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.643×** | -9.6 | 6e-20 | 40/48 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.650×** | -9.3 | 6e-19 | 33/47 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.664×** | -8.4 | 2e-15 | 33/47 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.583×** | -6.1 | 5e-08 | 28/48 (NCI-H1573, RKO, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.763×** | -5.9 | 2e-07 | 33/47 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.832×** | -5.6 | 7e-07 | 24/47 (RKO, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.773×** | -5.6 | 9e-07 | 32/47 (NCI-H2347, C32, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.834× | -5.6 | 1e-06 | 23/48 (NCI-H2347, KATO III, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.860× | -4.7 | 1e-04 | 21/47 (A549, HEC-1-A, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.686×** | -4.3 | 6e-04 | 29/47 (LoVo, A498, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.873× | -4.2 | 7e-04 | 17/47 (A549, HEC-1-A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.849× | -3.6 | 0.009 | 20/47 (NCI-H23, J82, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.734×** | -3.5 | 0.010 | 22/46 (NCI-H23, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.738×** | -3.4 | 0.013 | 23/48 (SK-MEL-2, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.857× | -3.4 | 0.016 | 18/48 (SW480, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10552. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 396 | 0 | 14 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -19.8) |
| [[NCI-H1573 (line)]] | alt | 398 | 0 | 12 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.245× (z -23.6) |
| [[SW480 (line)]] | alt | 275 | 1 (1 ⚠) | 8 (2 ⚠) | [[Digitoxin (drug)]] 0.05 µM 1.61× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.164× (z -33.4) |
| [[A498 (line)]] | wt | 389 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.299× (z -19.6) |
| [[LoVo (line)]] | wt | 580 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -21.5) |
| [[LS 180 (line)]] | wt | 421 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -20.6) |
| [[PANC-1 (line)]] | alt | 436 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.266× (z -22.2) |
| [[A-172 (line)]] | wt | 250 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.172× (z -18.0) |
| [[AsPC-1 (line)]] | alt | 426 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.129× (z -28.8) |
| [[C32 (line)]] | wt | 356 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -18.1) |
| [[HCT15 (line)]] | alt | 657 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 427 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.213× (z -27.7) |
| [[KATO III (line)]] | alt | 440 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.170× (z -21.0) |
| [[LOX-IMVI (line)]] | wt | 250 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.308× (z -18.3) |
| [[NCI-H460 (line)]] | wt | 431 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -16.5) |
| [[RKO (line)]] | wt | 225 | 0 | 7 | — | [[Harringtonine (drug)]] 5 µM 0.310× (z -15.7) |
| [[SK-MEL-2 (line)]] | alt | 338 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.185× (z -22.1) |
| [[A549 (line)]] | wt | 385 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -23.3) |
| [[HT-29 (line)]] | alt | 602 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.172× (z -17.1) |
| [[SW 900 (line)]] | alt | 458 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -20.3) |
| [[A-427 (line)]] | wt | 194 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.287× (z -19.3) |
| [[BT-474 (line)]] | alt | 214 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.01× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -17.0) |
| [[HOP62 (line)]] | alt | 188 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.216× (z -22.7) |
| [[MIA PaCa-2 (line)]] | alt | 247 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.222× (z -20.1) |
| [[NCI-H23 (line)]] | alt | 189 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.172× (z -25.3) |
| [[SHP-77 (line)]] | alt | 242 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.367× (z -13.3) |
| [[SW1417 (line)]] | alt | 432 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -19.3) |
| [[AN3 CA (line)]] | alt | 440 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.364× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 327 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.283× (z -19.3) |
| [[hTERT-HPNE (line)]] | wt | 269 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -19.4) |
| [[NCI-H2030 (line)]] | alt | 291 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -21.5) |
| [[SW48 (line)]] | wt | 290 | 1 | 3 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.58× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.357× (z -10.5) |
| [[C-33 A (line)]] | alt | 251 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.348× (z -13.8) |
| [[COLO 205 (line)]] | alt | 307 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -15.7) |
| [[Hs 766T (line)]] | wt | 198 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -11.9) |
| [[HS-578T (line)]] | alt | 240 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.234× (z -16.8) |
| [[J82 (line)]] | alt | 199 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.289× (z -19.8) |
| [[Panc 03.27 (line)]] | alt | 358 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.253× (z -19.1) |
| [[RPMI-7951 (line)]] | alt | 176 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.332× (z -13.0) |
| [[SNU-1 (line)]] | wt | 310 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.346× (z -14.0) |
| [[SNU-423 (line)]] | alt | 215 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.388× (z -12.2) |
| [[CHP-212 (line)]] | wt | 230 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.351× (z -8.6) |
| [[H4 (line)]] | wt | 204 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.367× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 245 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.444× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 26.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 315 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 349 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 258 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 192 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10552), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*31 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAV2]] | +0.58 | +0.71 / +0.52 | both halves | 1e-05 | pathway: Adherens junctions interactions |
| [[SNX25]] | +0.56 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[TENT4A]] | +0.53 | +0.71 / +0.40 | both halves | 5e-05 |  |
| [[TBC1D4]] | +0.53 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[KLF13]] | +0.53 | +0.57 / +0.61 | both halves | 1e-05 | STRING 490 |
| [[DOCK9]] | +0.52 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[ATP11A]] | +0.52 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[B4GALNT3]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[TSPAN14]] | +0.51 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[RALGPS1]] | +0.51 | +0.59 / +0.35 | both halves | 1e-04 |  |
| [[MCF2L]] | +0.51 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[HDAC4]] | +0.50 | +0.40 / +0.52 | both halves | 4e-05 | same gene group |

## Genes that move opposite

*69 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C12orf4]] | -0.61 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[CHURC1]] | -0.58 | -0.70 / -0.49 | both halves | 1e-05 |  |
| [[PGGT1B]] | -0.57 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[THAP6]] | -0.56 | -0.70 / -0.49 | both halves | 1e-05 |  |
| [[ZNF136]] | -0.56 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[TMEM128]] | -0.55 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[RBSN]] | -0.55 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[BBS1]] | -0.54 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[NDUFA5]] | -0.54 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[ZNF140]] | -0.54 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[ZNF197]] | -0.54 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[TMEM254]] | -0.53 | -0.52 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **-** arm (projection on the module's main direction -0.471). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-28.9, 5.7); signed map (-35.1, 29.0). **Vector** length 95.9, 32.6% of its response variance represented; |z| ≥ 3 in 1,391 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +5.8 | -5.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.4 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | -1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +4.1 | -4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +3.9 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | -1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | -0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | -0.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.8 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.2 | -9.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -8.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.3 | -12.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -13.6 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.9 | -1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -4.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.8 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -3.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | C-terminal binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:124,984,317-125,161,170 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ribeye |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 18 pathways, smallest: Signaling by TCF7L2 mutants; Repression of WNT target genes; Signaling by WNT in cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [P56545](https://www.uniprot.org/uniprotkb/P56545) (C-terminal-binding protein 2):

> Corepressor targeting diverse transcription regulators. Functions in brown adipose tissue (BAT) differentiation (By similarity).; Isoform 2 probably acts as a scaffold for specialized synapses.

**Summary**, from NCBI Gene [1488](https://www.ncbi.nlm.nih.gov/gene/1488):

> This gene produces alternative transcripts encoding two distinct proteins. One protein is a transcriptional repressor, while the other isoform is a major component of specialized synapses known as synaptic ribbons. Both proteins contain a NAD+ binding domain similar to NAD+-dependent 2-hydroxyacid dehydrogenases. A portion of the 3' untranslated region was used to map this gene to chromosome 21q21.3; however, it was noted that similar loci elsewhere in the genome are likely. Blast analysis …

**Accessions** — [HGNC:2495](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2495) · Entrez [1488](https://www.ncbi.nlm.nih.gov/gene/1488) · UniProt [P56545](https://www.uniprot.org/uniprotkb/P56545) · Ensembl [ENSG00000175029](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175029)

## Data

Gene col 10552: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10552); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10552, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10552]; `tensor/DDL_lfc|DDL_z.npy` [10552]; `embed/gene_vectors.npy` [10552]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10552 or target_col == 10552). Every well: [[CTBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
