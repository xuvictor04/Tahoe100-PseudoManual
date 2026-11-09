---
symbol: "AVL9"
type: "gene"
col: 2664
ensembl_id: "ENSG00000105778"
name: "AVL9 cell migration associated"
location: "7p14.3"
module: 36
arm: "+"
pooled_cpm: 230.85
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 18
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# AVL9

*AVL9 cell migration associated* — 7p14.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (Hs 766T 2.03×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 1.66×; ⚠ cell-cycle shift, explains ~98% of this change).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.384× (z -18.1, q 0e+00, down in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.668× (z -10.3, q 1e-22, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARMC10]] (+0.58, fdr 7e-06), [[VPS26C]] (+0.57, fdr 3e-05), [[NAGLU]] (+0.54, fdr 1e-05); moves opposite to [[DDX5]] (-0.55, fdr 1e-05), [[SRSF3]] (-0.48, fdr 3e-05), [[CHD4]] (-0.47, fdr 6e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2664.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (Hs 766T 2.03×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 1.66×; ⚠ cell-cycle shift, explains ~98% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.16× | +3.8 | 0.094 | 5/48 (LoVo, SW 900, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 1.39× | +3.1 | 0.56 | 24/48 (NCI-H460, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 17 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2664.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.384×** | -18.1 | 0e+00 | 48/49 (SK-MEL-2, H4, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.420×** | -15.8 | 0e+00 | 42/44 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.430×** | -14.8 | 0e+00 | 43/45 (HS-578T, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.668×** | -10.3 | 1e-22 | 43/49 (A549, A-172, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.664×** | -7.8 | 9e-13 | 44/48 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.699×** | -6.8 | 1e-09 | 41/48 (CFPAC-1, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.683×** | -6.5 | 5e-09 | 47/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.719×** | -6.0 | 1e-07 | 32/47 (HepG2/C3A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.731×** | -5.7 | 7e-07 | 31/48 (NCI-H1792, HEC-1-A, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.768×** | -4.8 | 9e-05 | 28/50 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **0.827×** | -4.8 | 9e-05 | 24/48 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.778×** | -4.8 | 9e-05 | 29/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.761×** | -4.7 | 1e-04 | 32/48 (SK-MEL-2, LOX-IMVI, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **0.786×** | -4.6 | 2e-04 | 31/48 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.859× | -3.8 | 0.005 | 14/48 (A-172, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.804×** | -3.7 | 0.007 | 25/48 (CFPAC-1, SW1417, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2664. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 302 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -16.2) |
| [[CFPAC-1 (line)]] | alt | 160 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -12.1) ⚠ cell-cycle shift, explains ~98% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 274 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.488× (z -10.7) |
| [[SNU-423 (line)]] | alt | 225 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -12.8) |
| [[SW 900 (line)]] | alt | 225 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.503× (z -8.7) |
| [[A498 (line)]] | wt | 343 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 179 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.371× (z -13.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 240 | 2 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HS-578T (line)]] | alt | 213 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -23.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 189 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -17.8) ⚠ cell-cycle shift, explains ~98% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 358 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -12.0) |
| [[A549 (line)]] | wt | 202 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -16.5) |
| [[AsPC-1 (line)]] | alt | 297 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -13.3) |
| [[C32 (line)]] | wt | 176 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.327× (z -14.0) |
| [[LoVo (line)]] | wt | 263 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[PANC-1 (line)]] | alt | 300 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -9.7) |
| [[SHP-77 (line)]] | alt | 208 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SK-MEL-2 (line)]] | alt | 202 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -29.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.446× (z -10.9) |
| [[SW1417 (line)]] | alt | 249 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[BT-474 (line)]] | alt | 180 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.570× (z -10.4) ⚠ cell-cycle shift, explains ~98% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -9.8) |
| [[H4 (line)]] | wt | 401 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HOP62 (line)]] | alt | 150 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.395× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.487× (z -8.9) |
| [[HT-29 (line)]] | alt | 283 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -12.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 144 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[KATO III (line)]] | alt | 361 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[LOX-IMVI (line)]] | wt | 157 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.429× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[LS 180 (line)]] | wt | 212 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 202 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RPMI-7951 (line)]] | alt | 256 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW480 (line)]] | alt | 278 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HCT15 (line)]] | alt | 226 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H2030 (line)]] | alt | 190 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H23 (line)]] | alt | 205 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H2347 (line)]] | alt | 164 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -8.7) |
| [[RKO (line)]] | wt | 168 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SNU-1 (line)]] | wt | 133 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -12.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.385× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[C-33 A (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[CHP-212 (line)]] | wt | 147 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -9.4) |
| [[COLO 205 (line)]] | alt | 211 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HepG2_C3A (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.378× (z -10.9) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 436 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW48 (line)]] | wt | 222 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[AN3 CA (line)]] | alt | 194 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 168 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 220 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2664), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC10]] | +0.58 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[VPS26C]] | +0.57 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[NAGLU]] | +0.54 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[RMND1]] | +0.54 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[VPS8]] | +0.52 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[MRPS21]] | +0.51 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[CHURC1-FNTB]] | +0.50 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[FNIP1]] | +0.50 | +0.48 / +0.41 | both halves | 4e-05 | same gene group |
| [[FBXO28]] | +0.50 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[MED9]] | +0.49 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[MRPS36]] ⚠ | +0.49 | +0.40 / +0.43 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BRI3]] | +0.49 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[PSMD5]] | +0.49 | +0.30 / +0.54 | both halves | 2e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX5]] | -0.55 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[SRSF3]] | -0.48 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[CHD4]] | -0.47 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[MAPRE1]] | -0.47 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[USP12]] | -0.46 | -0.39 / -0.40 | both halves | 5e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[TAPT1-AS1]] | -0.45 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[YWHAZ]] | -0.44 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[ITPR2-AS1]] | -0.44 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[MYOSLID]] | -0.44 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[SFPQ]] | -0.42 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[HNRNPA2B1]] | -0.42 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[CCDC200]] | -0.42 | -0.52 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises AVL9's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | AVL9's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | AVL9's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.59 | 0.472 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.145). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-28.9, -8.3); signed map (-14.2, -19.3). **Vector** length 92.1, 32.2% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +2.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.4 | -0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.3 | +0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.3 | +0.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.8 | +2.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +0.5 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.0 | -3.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.7 | -2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -1.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.1 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -2.1 | -1.8 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -2.0 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | AVL9 cell migration associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:32,495,426-32,588,726 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0241 |
| Gene groups (HGNC) | DENN domain containing |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBF6](https://www.uniprot.org/uniprotkb/Q8NBF6) (Late secretory pathway protein AVL9 homolog):

> Functions in cell migration.

**Summary**, from NCBI Gene [23080](https://www.ncbi.nlm.nih.gov/gene/23080):

> Involved in cell migration. Located in recycling endosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28994](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28994) · Entrez [23080](https://www.ncbi.nlm.nih.gov/gene/23080) · UniProt [Q8NBF6](https://www.uniprot.org/uniprotkb/Q8NBF6) · Ensembl [ENSG00000105778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105778)

## Data

Gene col 2664: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2664); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2664, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2664]; `tensor/DDL_lfc|DDL_z.npy` [2664]; `embed/gene_vectors.npy` [2664]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2664 or target_col == 2664). Every well: [[AVL9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AVL9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
