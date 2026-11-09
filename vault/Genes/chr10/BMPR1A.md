---
symbol: "BMPR1A"
type: "gene"
col: 2878
ensembl_id: "ENSG00000107779"
name: "bone morphogenetic protein receptor type 1A"
location: "10q23.2"
module: 186
arm: "+"
pooled_cpm: 125.14
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/186"]
generated_by: "tahoemap"
---

# BMPR1A

*bone morphogenetic protein receptor type 1A* — 10q23.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 2.45×, CFPAC-1 2.25×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW480 1.93×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 1.50×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.383× (z -21.5, q 0e+00, down in 39 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.568× (z -12.7, q 1e-34, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP2R5E]] (+0.66, fdr 7e-06), [[FHIP2A]] (+0.66, fdr 1e-05), [[CIAO2A]] (+0.63, fdr 1e-05); moves opposite to [[IER2]] (-0.61, fdr 1e-05), [[CSRNP1]] (-0.60, fdr 1e-05), [[EGR1]] (-0.58, fdr 2e-05).
> It is in [[Module 186]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2878.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 2.45×, CFPAC-1 2.25×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW480 1.93×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 1.50×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.17× | +3.2 | 0.39 | 15/49 (RKO, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.0 | 0.39 | 15/48 (NCI-H460, LoVo, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.39 | 11/47 (SW480, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2878.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.383×** | -21.5 | 0e+00 | 39/48 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.424×** | -18.5 | 0e+00 | 36/43 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.437×** | -17.1 | 0e+00 | 38/44 (NCI-H2030, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.625×** | -14.3 | 3e-44 | 37/47 (A-172, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.568×** | -12.7 | 1e-34 | 44/47 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.570×** | -12.6 | 2e-34 | 43/47 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.596×** | -11.6 | 3e-29 | 43/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.636×** | -10.1 | 3e-22 | 39/47 (HT-29, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.689×** | -8.3 | 5e-15 | 36/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.709×** | -7.7 | 9e-13 | 35/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.717×** | -7.5 | 5e-12 | 40/47 (hTERT-HPNE, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.784×** | -5.4 | 3e-06 | 23/47 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.817×** | -4.3 | 7e-04 | 24/47 (SNU-423, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.703×** | -3.9 | 0.004 | 22/48 (NCI-H2347, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.892× | -3.4 | 0.030 | 6/47 (MIA PaCa-2, SHP-77, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.758×** | -3.1 | 0.076 | 19/46 (CFPAC-1, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.863× | -3.0 | 0.079 | 14/46 (PANC-1, C32, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2878. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 132 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -29.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.241× (z -19.2) |
| [[NCI-H460 (line)]] | wt | 162 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.468× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 166 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.294× (z -17.6) |
| [[SW480 (line)]] | alt | 177 | 1 (1 ⚠) | 7 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.459× (z -13.0) |
| [[HOP62 (line)]] | alt | 115 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.268× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.433× (z -10.6) |
| [[LoVo (line)]] | wt | 141 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.45× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -13.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.401× (z -13.3) |
| [[Panc 03.27 (line)]] | alt | 133 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -13.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.447× (z -10.7) |
| [[PANC-1 (line)]] | alt | 167 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.501× (z -11.4) |
| [[SNU-423 (line)]] | alt | 132 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.380× (z -13.7) |
| [[SW1417 (line)]] | alt | 152 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.459× (z -10.6) |
| [[A-427 (line)]] | wt | 160 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0537× (z -37.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.439× (z -10.9) |
| [[A549 (line)]] | wt | 139 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.428× (z -11.9) |
| [[AN3 CA (line)]] | alt | 359 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 160 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.375× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 98.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.372× (z -12.8) |
| [[LS 180 (line)]] | wt | 137 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.395× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 110 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.256× (z -17.7) |
| [[NCI-H2030 (line)]] | alt | 131 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -27.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.477× (z -10.0) |
| [[C32 (line)]] | wt | 165 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.411× (z -10.7) |
| [[HT-29 (line)]] | alt | 98.2 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.286× (z -15.1) |
| [[NCI-H2347 (line)]] | alt | 90.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -11.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.493× (z -9.3) |
| [[A498 (line)]] | wt | 85.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -14.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 313 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -16.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 147 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.538× (z -8.5) |
| [[Hs 766T (line)]] | wt | 105 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 106 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0726× (z -31.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.476× (z -9.0) |
| [[NCI-H661 (line)]] | alt | 344 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -12.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 93.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.410× (z -9.7) |
| [[SNU-1 (line)]] | wt | 222 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.385× (z -10.6) |
| [[SW48 (line)]] | wt | 178 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -18.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 81.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -11.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.418× (z -9.8) |
| [[HS-578T (line)]] | alt | 64.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -10.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.433× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 99.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -24.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 75.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.25× (z +10.0) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 174 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -10.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 75.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -9.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[hTERT-HPNE (line)]] | wt | 68.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.165× (z -15.7) ⚠ transcription drop; cell-cycle shift, explains ~35% of this change |
| [[J82 (line)]] | alt | 64.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.444× (z -8.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.387× (z -10.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 73.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.411× (z -8.5) |
| [[SHP-77 (line)]] | alt | 82.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.358× (z -10.4) |
| [[BT-474 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.05 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 53.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2878), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP2R5E]] | +0.66 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[FHIP2A]] | +0.66 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[CIAO2A]] | +0.63 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[SEC24B]] | +0.62 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[STIM1]] | +0.62 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[PDE7A]] | +0.61 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[NFATC3]] | +0.61 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[DRAM2]] | +0.60 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[SOS1]] | +0.60 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[HOXB6]] | +0.59 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[GNAQ]] | +0.59 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[ZMYM2]] | +0.59 | +0.66 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER2]] | -0.61 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[CSRNP1]] | -0.60 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[EGR1]] | -0.58 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[TUT7]] | -0.57 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[BCL10]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[BACH1]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[CD163L1]] | -0.53 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[ZKSCAN2]] | -0.53 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[BCAN-AS1]] | -0.52 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[JUNB]] | -0.52 | -0.45 / -0.45 | both halves | 3e-05 | pathway: HALLMARK_TGF_BETA_SIGNALING |
| [[VGF]] | -0.52 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[SOCS3]] | -0.52 | -0.52 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 186]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.829). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-9.4, -8.4); signed map (-30.3, -18.2). **Vector** length 110, 33.9% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.0 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.2 | -0.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.3 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.2 | +3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.2 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.7 | -12.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -5.5 | -14.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -10.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.4 | -12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.3 | -17.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -3.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | bone morphogenetic protein receptor type 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.2 — chr10:86,755,786-86,932,825 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ALK3, CD292; previously ACVRLK3 |
| Gene groups (HGNC) | Type 1 receptor serine/threonine kinases; CD molecules; BMP receptors |
| Hallmark sets | TGF_BETA_SIGNALING, UV_RESPONSE_DN |
| Reactome | 2 pathways, smallest: Signaling by BMP; Signaling by TGFB family members |
| Matched by | ensembl_id |

**Function**, from UniProt [P36894](https://www.uniprot.org/uniprotkb/P36894) (Bone morphogenetic protein receptor type-1A):

> On ligand binding, forms a receptor complex consisting of two type II and two type I transmembrane serine/threonine kinases. Type II receptors phosphorylate and activate type I receptors which autophosphorylate, then bind and activate SMAD transcriptional regulators. Receptor for BMP2, BMP4, GDF5 and GDF6. Positively regulates chondrocyte differentiation through GDF5 interaction. Mediates induction of adipogenesis by GDF6. May promote the expression of HAMP, potentially via its interaction with …

**Summary**, from NCBI Gene [657](https://www.ncbi.nlm.nih.gov/gene/657):

> The bone morphogenetic protein (BMP) receptors are a family of transmembrane serine/threonine kinases that include the type I receptors BMPR1A and BMPR1B and the type II receptor BMPR2. These receptors are also closely related to the activin receptors, ACVR1 and ACVR2. The ligands of these receptors are members of the TGF-beta superfamily. TGF-betas and activins transduce their signals through the formation of heteromeric complexes with 2 different types of serine (threonine) kinase receptors: …

**Accessions** — [HGNC:1076](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1076) · Entrez [657](https://www.ncbi.nlm.nih.gov/gene/657) · UniProt [P36894](https://www.uniprot.org/uniprotkb/P36894) · Ensembl [ENSG00000107779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107779)

## Data

Gene col 2878: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2878); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2878, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2878]; `tensor/DDL_lfc|DDL_z.npy` [2878]; `embed/gene_vectors.npy` [2878]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2878 or target_col == 2878). Every well: [[BMPR1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMPR1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
