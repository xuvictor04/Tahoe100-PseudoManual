---
symbol: "LPP"
type: "gene"
col: 6949
ensembl_id: "ENSG00000145012"
name: "LIM domain containing preferred translocation partner in lipoma"
location: "3q27.3-q28"
module: 40
arm: "-"
pooled_cpm: 642.7
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 24
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# LPP

*LIM domain containing preferred translocation partner in lipoma* — 3q27.3-q28

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 1.62×; ⚠ cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 2.24×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.397× (z -22.5, q 0e+00, down in 49 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNG12]] (+0.57, fdr 3e-05), [[COMMD10]] (+0.57, fdr 9e-05), [[IL6ST]] (+0.57, fdr 1e-04); moves opposite to [[TBC1D20]] (-0.60, fdr 4e-05), [[ESCO1]] (-0.59, fdr 1e-05), [[PPIL3]] (-0.58, fdr 4e-05).
> It sits in the **-** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6949.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 1.62×; ⚠ cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 2.24×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Demeclocycline (drug)]] 5 µM |  | 1.15× | +3.5 | 0.29 | 10/48 (RKO, NCI-H2347, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | 1.40× | +3.0 | 0.76 | 30/50 (A-427, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6949.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.397×** | -22.5 | 0e+00 | 49/49 (NCI-H1792, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.320×** | -19.6 | 0e+00 | 48/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.341×** | -18.5 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.351×** | -17.3 | 0e+00 | 47/47 (RKO, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.415×** | -15.1 | 0e+00 | 48/48 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.506×** | -11.1 | 1e-26 | 48/48 (C32, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.567×** | -9.4 | 5e-19 | 46/48 (SW480, C32, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.613×** | -8.1 | 3e-14 | 46/50 (SW480, KATO III, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.660×** | -7.2 | 5e-11 | 42/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.668×** | -6.9 | 2e-10 | 44/48 (KATO III, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.679×** | -6.7 | 1e-09 | 42/48 (BT-474, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.713×** | -5.8 | 3e-07 | 34/48 (SW 900, H4, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.715×** | -5.8 | 3e-07 | 41/48 (A-172, RKO, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.791×** | -5.7 | 5e-07 | 27/48 (COLO 205, CFPAC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.724×** | -5.6 | 1e-06 | 32/48 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.735×** | -5.3 | 4e-06 | 37/49 (HOP62, RKO, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.568×** | -5.1 | 1e-05 | 45/48 (MIA PaCa-2, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | **0.818×** | -4.9 | 3e-05 | 29/49 (SW480, RPMI-7951, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.748×** | -4.6 | 1e-04 | 39/47 (hTERT-HPNE, RKO, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.837× | -4.3 | 4e-04 | 24/48 (BT-474, HOP62, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.841× | -4.2 | 7e-04 | 22/48 (NCI-H2030, J82, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.789×** | -3.9 | 0.003 | 33/48 (H4, RKO, …) | inconsistent across doses |  |
| [[Irinotecan (drug)]] 5 µM |  | **0.690×** | -3.3 | 0.020 | 39/50 (CFPAC-1, NCI-H2030, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.48 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6949. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 881 | 0 | 13 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -24.9) |
| [[KATO III (line)]] | alt | 874 | 1 (1 ⚠) | 11 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +9.8) ⚠ cell-cycle shift, explains ~32% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -22.9) |
| [[Panc 03.27 (line)]] | alt | 859 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -24.6) |
| [[RKO (line)]] | wt | 916 | 0 | 12 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.136× (z -26.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.242× (z -19.6) |
| [[HOP62 (line)]] | alt | 610 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -23.1) |
| [[MIA PaCa-2 (line)]] | alt | 563 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -22.8) |
| [[PANC-1 (line)]] | alt | 568 | 0 | 11 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -21.8) |
| [[A-172 (line)]] | wt | 462 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.247× (z -21.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.263× (z -20.5) |
| [[BT-474 (line)]] | alt | 982 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -19.9) |
| [[C32 (line)]] | wt | 604 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -24.2) |
| [[H4 (line)]] | wt | 712 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -18.4) |
| [[J82 (line)]] | alt | 607 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -22.3) |
| [[RPMI-7951 (line)]] | alt | 671 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -19.3) |
| [[SK-MEL-2 (line)]] | alt | 496 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -16.9) |
| [[SW 900 (line)]] | alt | 466 | 0 | 9 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.315× (z -17.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -17.3) |
| [[SW480 (line)]] | alt | 490 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -27.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.214× (z -25.0) |
| [[CFPAC-1 (line)]] | alt | 797 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -22.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.334× (z -14.4) |
| [[COLO 205 (line)]] | alt | 874 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -33.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.262× (z -17.5) |
| [[HCT15 (line)]] | alt | 615 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -17.5) |
| [[HEC-1-A (line)]] | alt | 1,094 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -23.8) |
| [[LoVo (line)]] | wt | 777 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -23.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.262× (z -20.1) |
| [[LOX-IMVI (line)]] | wt | 705 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -18.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.269× (z -16.4) |
| [[NCI-H1792 (line)]] | alt | 604 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -25.2) |
| [[NCI-H460 (line)]] | wt | 369 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.326× (z -16.7) |
| [[SNU-423 (line)]] | alt | 717 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.321× (z -17.6) |
| [[NCI-H1573 (line)]] | alt | 635 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.230× (z -19.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -18.7) |
| [[NCI-H23 (line)]] | alt | 361 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -17.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.289× (z -16.0) |
| [[NCI-H2347 (line)]] | alt | 1,114 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -14.8) |
| [[A549 (line)]] | wt | 550 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -20.1) |
| [[HepG2_C3A (line)]] | wt | 677 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.323× (z -14.4) |
| [[Hs 766T (line)]] | wt | 361 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -16.5) |
| [[HS-578T (line)]] | alt | 866 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -23.1) |
| [[SNU-1 (line)]] | wt | 932 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -20.2) |
| [[SW1417 (line)]] | alt | 520 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -18.1) |
| [[A-427 (line)]] | wt | 544 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.329× (z -16.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.361× (z -14.8) |
| [[A498 (line)]] | wt | 618 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -22.7) |
| [[AN3 CA (line)]] | alt | 600 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -16.2) |
| [[AsPC-1 (line)]] | alt | 514 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -18.8) |
| [[HT-29 (line)]] | alt | 530 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.215× (z -17.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.238× (z -16.8) |
| [[LS 180 (line)]] | wt | 719 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.274× (z -19.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.277× (z -19.2) |
| [[SW48 (line)]] | wt | 604 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -17.6) |
| [[CHP-212 (line)]] | wt | 533 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -15.1) |
| [[C-33 A (line)]] | alt | 205 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.24× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.434× (z -9.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.450× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 521 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -12.2) |
| [[SHP-77 (line)]] | alt | 280 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.322× (z -13.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -12.6) |
| [[SW 1088 (line)]] | alt | 575 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -13.2) |
| [[SW 1271 (line)]] | alt | 517 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -11.2) |
| [[NCI-H2122 (line)]] | alt | 608 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 571 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 244 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6949), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNG12]] | +0.57 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[COMMD10]] | +0.57 | +0.36 / +0.58 | both halves | 9e-05 |  |
| [[IL6ST]] | +0.57 | +0.34 / +0.63 | both halves | 1e-04 |  |
| [[MBNL1]] | +0.56 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[ACTR3]] | +0.56 | +0.37 / +0.65 | both halves | 8e-05 |  |
| [[LINC00342]] | +0.55 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[TRIP12]] | +0.55 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[ADGRG6]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[YWHAE]] | +0.54 | +0.30 / +0.57 | both halves | 2e-04 |  |
| [[MED13L]] | +0.54 | +0.54 / +0.48 | both halves | 2e-05 | same gene group |
| [[PARVA]] | +0.54 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[ENAH]] | +0.53 | +0.37 / +0.46 | both halves | 7e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D20]] | -0.60 | -0.40 / -0.61 | both halves | 4e-05 |  |
| [[ESCO1]] | -0.59 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[PPIL3]] | -0.58 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[DNAJC25]] | -0.58 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[EEF1AKMT4]] | -0.57 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[QPCTL]] | -0.56 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[BET1L]] | -0.56 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[SPICE1]] | -0.55 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[ANKRD37]] | -0.55 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[NUDT22]] | -0.54 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[ZNF684]] | -0.54 | -0.36 / -0.60 | both halves | 1e-04 |  |
| [[SSR2]] | -0.54 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP1]] | B | TOP1 activity raises LPP's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 4.5% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ALCAM]] | B | ALCAM activity raises LPP's level | lines that do not express ALCAM (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without ALCAM | 0.078 | ⚠ within organs, on part of the lines; also absent: GEM, IL7, RND3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **-** arm (projection on the module's main direction -0.548). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (6.7, -32.7); signed map (20.4, -38.1). **Vector** length 108, 43.4% of its response variance represented; |z| ≥ 3 in 1,683 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +8.3 | -3.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +7.9 | -2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.3 | -2.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | -0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +5.2 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.2 | +2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.2 | +1.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.7 | +1.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +3.5 | +2.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.4 | +1.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.4 | -17.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.8 | -11.1 |
|  | [[Vilanterol (drug)]] 5 µM |  | -4.2 | -4.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.9 | -6.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.1 | -9.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.1 | -3.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.9 | -5.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.8 | -1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | LIM domain containing preferred translocation partner in lipoma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.3-q28 — chr3:188,153,284-188,890,671 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Zyxin family; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93052](https://www.uniprot.org/uniprotkb/Q93052) (Lipoma-preferred partner):

> May play a structural role at sites of cell adhesion in maintaining cell shape and motility. In addition to these structural functions, it may also be implicated in signaling events and activation of gene transcription. May be involved in signal transduction from cell adhesion sites to the nucleus allowing successful integration of signals arising from soluble factors and cell-cell adhesion sites. Also suggested to serve as a scaffold protein upon which distinct protein complexes are assembled …

**Summary**, from NCBI Gene [4026](https://www.ncbi.nlm.nih.gov/gene/4026):

> This gene encodes a member of a subfamily of LIM domain proteins that are characterized by an N-terminal proline-rich region and three C-terminal LIM domains. The encoded protein localizes to the cell periphery in focal adhesions and may be involved in cell-cell adhesion and cell motility. This protein also shuttles through the nucleus and may function as a transcriptional co-activator. This gene is located at the junction of certain disease-related chromosomal translocations, which result in …

**Accessions** — [HGNC:6679](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6679) · Entrez [4026](https://www.ncbi.nlm.nih.gov/gene/4026) · UniProt [Q93052](https://www.uniprot.org/uniprotkb/Q93052) · Ensembl [ENSG00000145012](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145012)

## Data

Gene col 6949: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6949); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6949, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6949]; `tensor/DDL_lfc|DDL_z.npy` [6949]; `embed/gene_vectors.npy` [6949]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6949 or target_col == 6949). Every well: [[LPP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LPP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
