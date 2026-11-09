---
symbol: "CABIN1"
type: "gene"
col: 1838
ensembl_id: "ENSG00000099991"
name: "calcineurin binding protein 1"
location: "22q11.23"
module: 134
arm: "+"
pooled_cpm: 145.2
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# CABIN1

*calcineurin binding protein 1* — 22q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.47× (z +7.0, q 1e-09, up in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 5 lines (SW480 2.18×, MIA PaCa-2 2.12×, Panc 03.27 1.90×, A498 2.14×, …); [[Panobinostat (drug)]] 0.5 µM in 2 lines (A498 2.25×, SW480 1.79×; ⚠ cell-cycle shift, explains ~25% of this change); [[Belinostat (drug)]] 5 µM in 1 line (SW480 1.84×; ⚠ cell-cycle shift, explains ~26% of this change).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.403× (z -16.5, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.528× (z -16.4, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDK3]] (+0.77, fdr 7e-06), [[PDXP]] (+0.76, fdr 7e-06), [[PFKFB4]] (+0.74, fdr 7e-06); moves opposite to [[PPP3CB-AS1]] (-0.65, fdr 3e-04), [[C11orf58]] (-0.62, fdr 3e-05), [[ARAP2]] (-0.60, fdr 8e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GPR155]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1838.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 5 lines (SW480 2.18×, MIA PaCa-2 2.12×, Panc 03.27 1.90×, A498 2.14×, …); [[Panobinostat (drug)]] 0.5 µM in 2 lines (A498 2.25×, SW480 1.79×; ⚠ cell-cycle shift, explains ~25% of this change); [[Belinostat (drug)]] 5 µM in 1 line (SW480 1.84×; ⚠ cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +7.0 | 1e-09 | 37/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.39×** | +6.0 | 6e-07 | 33/48 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.36×** | +5.6 | 4e-06 | 33/48 (SW480, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1838.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.403×** | -16.5 | 0e+00 | 46/49 (C32, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.528×** | -16.4 | 0e+00 | 40/48 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.414×** | -15.4 | 0e+00 | 41/44 (A-427, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.421×** | -14.5 | 1e-45 | 43/45 (C32, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.483×** | -12.7 | 5e-35 | 45/47 (C32, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.499×** | -12.6 | 1e-34 | 42/48 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.516×** | -11.6 | 5e-29 | 44/47 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.522×** | -11.4 | 5e-28 | 38/48 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -10.8 | 3e-25 | 33/49 (C32, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.558×** | -10.6 | 2e-24 | 47/48 (AN3 CA, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.763×** | -7.0 | 2e-10 | 35/48 (C32, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.746×** | -5.3 | 5e-06 | 36/48 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.783×** | -4.3 | 9e-04 | 26/50 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.790×** | -4.1 | 0.002 | 29/48 (C32, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.863× | -3.8 | 0.006 | 21/48 (C32, J82, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.822×** | -3.4 | 0.021 | 22/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.829×** | -3.4 | 0.021 | 23/48 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 0.881× | -3.3 | 0.034 | 10/48 (SW 900, RKO, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.844× | -3.1 | 0.055 | 15/48 (SW48, PANC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.845× | -3.1 | 0.058 | 21/48 (NCI-H460, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1838. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 607 | 0 | 19 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0916× (z -41.1) |
| [[C-33 A (line)]] | alt | 394 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -14.3) |
| [[HS-578T (line)]] | alt | 279 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.467× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 189 | 1 | 10 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.12× (z +9.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -19.9) |
| [[NCI-H1573 (line)]] | alt | 124 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -18.0) |
| [[SK-MEL-2 (line)]] | alt | 286 | 0 | 11 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.340× (z -17.2) |
| [[J82 (line)]] | alt | 110 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -20.7) |
| [[LOX-IMVI (line)]] | wt | 134 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -20.2) |
| [[NCI-H1792 (line)]] | alt | 222 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -27.0) |
| [[NCI-H460 (line)]] | wt | 135 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.493× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 232 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -17.1) |
| [[SNU-423 (line)]] | alt | 146 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -24.4) |
| [[PANC-1 (line)]] | alt | 128 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -12.7) |
| [[HOP62 (line)]] | alt | 125 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -13.0) |
| [[AN3 CA (line)]] | alt | 217 | 0 | 6 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.127× (z -15.6) |
| [[NCI-H23 (line)]] | alt | 140 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.517× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 113 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.486× (z -13.9) |
| [[SW 900 (line)]] | alt | 120 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.486× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 120 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.362× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.436× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 202 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.90× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.539× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -15.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 128 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -16.1) |
| [[SW480 (line)]] | alt | 118 | 3 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.18× (z +12.1) | [[Auranofin (drug)]] 5 µM 0.581× (z -8.5) |
| [[A-172 (line)]] | wt | 76.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.313× (z -14.7) |
| [[A-427 (line)]] | wt | 119 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0646× (z -30.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.474× (z -8.7) |
| [[A498 (line)]] | wt | 44.7 | 2 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.25× (z +9.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.14× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.559× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 143 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -14.6) |
| [[RKO (line)]] | wt | 145 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.400× (z -9.7) |
| [[SNU-1 (line)]] | wt | 165 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -11.7) |
| [[A549 (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -11.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 53.9 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.38× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -9.4) |
| [[H4 (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -10.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 128 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -10.0) |
| [[Hs 766T (line)]] | wt | 146 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -13.7) |
| [[LoVo (line)]] | wt | 104 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -11.3) |
| [[SW1417 (line)]] | alt | 152 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.385× (z -13.1) ⚠ toxic |
| [[SW48 (line)]] | wt | 150 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -12.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.359× (z -9.9) |
| [[CHP-212 (line)]] | wt | 190 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.206× (z -10.7) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 76.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -8.5) |
| [[HT-29 (line)]] | alt | 84.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.498× (z -8.6) |
| [[KATO III (line)]] | alt | 111 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.391× (z -11.2) |
| [[NCI-H661 (line)]] | alt | 166 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.160× (z -9.2) ⚠ toxic |
| [[HCT15 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 155 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1838), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDK3]] | +0.77 | +0.82 / +0.64 | both halves | 7e-06 |  |
| [[PDXP]] | +0.76 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[PFKFB4]] | +0.74 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[PEX3]] | +0.74 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[FAM234B]] | +0.72 | +0.81 / +0.52 | both halves | 1e-05 |  |
| [[EFNA3]] | +0.72 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[ARL6]] | +0.72 | +0.75 / +0.49 | both halves | 1e-05 |  |
| [[YEATS2]] | +0.72 | +0.82 / +0.62 | both halves | 7e-06 |  |
| [[ATRN]] | +0.72 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[NCKIPSD]] | +0.72 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[SNAPC3]] | +0.72 | +0.76 / +0.53 | both halves | 1e-05 |  |
| [[USP37]] | +0.72 | +0.74 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP3CB-AS1]] | -0.65 | -0.66 / -0.28 | both halves | 3e-04 |  |
| [[C11orf58]] | -0.62 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[ARAP2]] | -0.60 | -0.64 / -0.37 | both halves | 8e-05 |  |
| [[ZNF655]] | -0.59 | -0.54 / -0.43 | both halves | 4e-05 |  |
| [[LINC00571]] | -0.59 | -0.58 / -0.29 | both halves | 3e-04 |  |
| [[KCNMB3]] | -0.58 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[ARMCX4]] | -0.58 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[WNT3]] | -0.58 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[FKRP]] | -0.58 | -0.57 / -0.36 | both halves | 9e-05 |  |
| [[MMADHC-DT]] | -0.58 | -0.61 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR155]] | B | GPR155 activity raises CABIN1's level | lines that do not express GPR155 (6) vs lines expressing it (44) | 1.64× lower at baseline in the lines without GPR155 | 0.004 | ⚠ within organs, on part of the lines; also absent: CYP46A1, PKIG, TBC1D19; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers CABIN1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MPP2]] | B | MPP2 activity raises CABIN1's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without MPP2 | 0.069 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[ZFPM2]] | B | ZFPM2 activity raises CABIN1's level | lines that do not express ZFPM2 (15) vs lines expressing it (35) | 1.41× lower at baseline in the lines without ZFPM2 | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF883, EVC, TRIM9; maybe low, not absent |
| [[HACE1]] | C | HACE1 activity raises CABIN1's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 2.08× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.789). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.3, -16.0); signed map (-37.1, 23.1). **Vector** length 150, 54.7% of its response variance represented; |z| ≥ 3 in 1,182 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +10.3 | +7.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +10.0 | +5.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +9.5 | +6.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.4 | +1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.0 | +2.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +4.0 | +2.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.5 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +2.3 |
|  | [[Allopurinol (drug)]] 0.05 µM |  | +3.3 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.0 | -12.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.2 | -16.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.1 | -10.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.1 | -7.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.5 | -12.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -5.8 | -3.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -5.2 | -0.8 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -4.1 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | calcineurin binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.23 — chr22:24,011,192-24,178,628 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0330, PPP3IN |
| Gene groups (HGNC) | HIRA histone chaperone complex subunits |
| Reactome | 5 pathways, smallest: Formation of Senescence-Associated Heterochromatin Foci (SAHF); DNA Damage/Telomere Stress Induced Senescence; Cellular Senescence |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6J0](https://www.uniprot.org/uniprotkb/Q9Y6J0) (Calcineurin-binding protein cabin-1):

> May be required for replication-independent chromatin assembly. May serve as a negative regulator of T-cell receptor (TCR) signaling via inhibition of calcineurin. Inhibition of activated calcineurin is dependent on both PKC and calcium signals. Acts as a negative regulator of p53/TP53 by keeping p53 in an inactive state on chromatin at promoters of a subset of its target genes.

**Summary**, from NCBI Gene [23523](https://www.ncbi.nlm.nih.gov/gene/23523):

> Calcineurin plays an important role in the T-cell receptor-mediated signal transduction pathway. The protein encoded by this gene binds specifically to the activated form of calcineurin and inhibits calcineurin-mediated signal transduction. The encoded protein is found in the nucleus and contains a leucine zipper domain as well as several PEST motifs, sequences which confer targeted degradation to those proteins which contain them. Alternative splicing results in multiple transcript variants …

**Accessions** — [HGNC:24187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24187) · Entrez [23523](https://www.ncbi.nlm.nih.gov/gene/23523) · UniProt [Q9Y6J0](https://www.uniprot.org/uniprotkb/Q9Y6J0) · Ensembl [ENSG00000099991](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099991)

## Data

Gene col 1838: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1838); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1838, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1838]; `tensor/DDL_lfc|DDL_z.npy` [1838]; `embed/gene_vectors.npy` [1838]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1838 or target_col == 1838). Every well: [[CABIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CABIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
