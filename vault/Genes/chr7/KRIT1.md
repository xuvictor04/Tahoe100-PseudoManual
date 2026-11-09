---
symbol: "KRIT1"
type: "gene"
col: 16
ensembl_id: "ENSG00000001631"
name: "KRIT1 ankyrin repeat containing"
location: "7q21.2"
module: 114
arm: "+"
pooled_cpm: 109.62
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 25
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# KRIT1

*KRIT1 ankyrin repeat containing* — 7q21.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 1.63×, A-427 1.61×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 1.64×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (17 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.492× (z -15.7, q 0e+00, down in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.637× (z -10.0, q 2e-21, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FCF1]] (+0.72, fdr 7e-06), [[GOSR1]] (+0.68, fdr 7e-06), [[ZNF764]] (+0.68, fdr 3e-05); moves opposite to [[METAP1]] (-0.65, fdr 1e-05), [[LPCAT4]] (-0.60, fdr 3e-05), [[ABHD6]] (-0.58, fdr 2e-05).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LYPD5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 1.63×, A-427 1.61×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 1.64×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.18× | +3.3 | 0.62 | 17/50 (C32, LoVo, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.492×** | -15.7 | 0e+00 | 46/48 (SNU-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.547×** | -11.6 | 1e-28 | 43/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.594×** | -11.5 | 2e-28 | 45/48 (SW480, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.600×** | -11.3 | 2e-27 | 45/48 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.609×** | -11.0 | 5e-26 | 40/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.637×** | -10.0 | 2e-21 | 39/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.639×** | -9.1 | 5e-18 | 32/45 (AsPC-1, PANC-1, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.669×** | -8.9 | 5e-17 | 37/48 (SW480, AsPC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.672×** | -8.8 | 1e-16 | 35/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.774×** | -8.0 | 7e-14 | 40/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.666×** | -7.8 | 3e-13 | 37/47 (RKO, SW 900, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.718×** | -7.3 | 1e-11 | 30/49 (COLO 205, H4, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.558×** | -6.7 | 7e-10 | 34/49 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **0.737×** | -5.9 | 2e-07 | 26/44 (NCI-H23, C-33 A, …) | all doses, flat | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -5.8 | 3e-07 | 0/50 | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.615×** | -5.6 | 6e-07 | 31/48 (C32, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.792×** | -5.1 | 8e-06 | 34/49 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.801×** | -4.9 | 3e-05 | 25/48 (RPMI-7951, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.813×** | -4.6 | 1e-04 | 25/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.851× | -3.6 | 0.008 | 19/48 (HCT15, J82, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.739×** | -3.5 | 0.010 | 19/48 (NCI-H460, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.849× | -3.1 | 0.035 | 18/48 (J82, NCI-H460, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.914× | -2.8 | 0.099 | 7/49 (AsPC-1, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 155 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.442× (z -13.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.471× (z -12.4) |
| [[LoVo (line)]] | wt | 119 | 0 | 8 (7 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.335× (z -14.4) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.556× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 104 | 0 | 8 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.328× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.519× (z -9.1) |
| [[PANC-1 (line)]] | alt | 118 | 0 | 8 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.376× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.502× (z -11.8) |
| [[A-427 (line)]] | wt | 91.9 | 1 (1 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.345× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.306× (z -8.8) |
| [[SNU-423 (line)]] | alt | 105 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.305× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.503× (z -8.5) |
| [[HOP62 (line)]] | alt | 85.9 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.371× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.443× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 142 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.389× (z -13.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LS 180 (line)]] | wt | 73.6 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.358× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.469× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 118 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -17.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 175 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.172× (z -21.6) ⚠ toxic |
| [[H4 (line)]] | wt | 151 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[Hs 766T (line)]] | wt | 130 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.463× (z -9.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[KATO III (line)]] | alt | 133 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.490× (z -10.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[MIA PaCa-2 (line)]] | alt | 127 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.399× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.477× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 109 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.406× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 137 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +10.5) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.107× (z -29.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[AN3 CA (line)]] | alt | 120 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.224× (z -9.3) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 92.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.457× (z -10.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[Panc 03.27 (line)]] | alt | 96.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.454× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[RPMI-7951 (line)]] | alt | 126 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.359× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SK-MEL-2 (line)]] | alt | 136 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -12.6) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SW 1088 (line)]] | alt | 189 | 0 | 2 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0840× (z -11.1) |
| [[SW 900 (line)]] | alt | 114 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.322× (z -13.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.469× (z -9.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A549 (line)]] | wt | 99.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.421× (z -9.6) ⚠ cell-cycle shift, explains ~21% of this change |
| [[BT-474 (line)]] | alt | 78.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.414× (z -8.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 95.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[C32 (line)]] | wt | 122 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.382× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 97.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.446× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[COLO 205 (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0628× (z -29.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[HCT15 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[HEC-1-A (line)]] | alt | 99.2 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.508× (z -10.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HS-578T (line)]] | alt | 94.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0498× (z -16.9) ⚠ toxic |
| [[HT-29 (line)]] | alt | 92.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.424× (z -9.9) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 80.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.380× (z -8.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 98.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.482× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -18.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 99.2 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.487× (z -8.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 96.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 67.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 72.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 81.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCF1]] | +0.72 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[GOSR1]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[ZNF764]] | +0.68 | +0.72 / +0.44 | both halves | 3e-05 |  |
| [[NAIF1]] | +0.66 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[TRIP11]] | +0.66 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[ZNF830]] | +0.65 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[ZNF506]] | +0.64 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[NKAPD1]] | +0.64 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[UBXN4]] | +0.64 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[RPAP1]] | +0.64 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[SLC4A1AP]] | +0.63 | +0.64 / +0.57 | both halves | 8e-06 |  |
| [[ZNF189]] | +0.63 | +0.59 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METAP1]] | -0.65 | -0.65 / -0.52 | both halves | 1e-05 | same gene group |
| [[LPCAT4]] | -0.60 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[ABHD6]] | -0.58 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[HPSE]] | -0.57 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[MGAT4A]] | -0.57 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[ANOS1]] | -0.56 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[RALGPS1]] | -0.56 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[PODXL2]] | -0.56 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[LRP5L]] | -0.55 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[TRABD]] | -0.55 | -0.57 / -0.27 | both halves | 3e-04 |  |
| [[SMARCD3]] | -0.55 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[PDXP]] | -0.55 | -0.52 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LYPD5]] | B | LYPD5 activity raises KRIT1's level | lines that do not express LYPD5 (16) vs lines expressing it (34) | 1.14× lower at baseline in the lines without LYPD5 | 0.024 | ⚠ within organs, on part of the lines; also absent: AGMAT, ZNF320, LIPG; maybe low, not absent |
| [[NNT-AS1]] | B | NNT-AS1 activity lowers KRIT1's level | lines that do not express NNT-AS1 (6) vs lines expressing it (44) | 1.33× higher at baseline in the lines without NNT-AS1 | 0.040 | ⚠ within organs, on part of the lines; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.561). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.5, 5.7); signed map (8.1, -20.6). **Vector** length 88.5, 25.3% of its response variance represented; |z| ≥ 3 in 1,161 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.5 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.1 | +1.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | -1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +2.5 | -5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.2 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +1.3 | -0.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.1 | +1.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.1 | +1.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.5 | -8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.2 | -5.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.4 | -11.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.3 | -11.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.1 | -11.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -0.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | KRIT1 ankyrin repeat containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.2 — chr7:92,197,498-92,246,166 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CAM; previously CCM1 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; FERM domain containing; MicroRNA protein coding host genes; CCM adhesion complex |
| Matched by | ensembl_id |

**Function**, from UniProt [O00522](https://www.uniprot.org/uniprotkb/O00522) (Krev interaction trapped protein 1):

> Component of the CCM signaling pathway which is a crucial regulator of heart and vessel formation and integrity (By similarity). Negative regulator of angiogenesis. Inhibits endothelial proliferation, apoptosis, migration, lumen formation and sprouting angiogenesis in primary endothelial cells. Promotes AKT phosphorylation in a NOTCH-dependent and independent manner, and inhibits ERK1/2 phosphorylation indirectly through activation of the DELTA-NOTCH cascade. Acts in concert with CDH5 to …

**Summary**, from NCBI Gene [889](https://www.ncbi.nlm.nih.gov/gene/889):

> This gene encodes a protein containing four ankyrin repeats, a band 4.1/ezrin/radixin/moesin (FERM) domain, and multiple NPXY sequences. The encoded protein is localized in the nucleus and cytoplasm. It binds to integrin cytoplasmic domain-associated protein-1 alpha (ICAP1alpha), and plays a critical role in beta1-integrin-mediated cell proliferation. It associates with junction proteins and RAS-related protein 1A (Rap1A), which requires the encoded protein for maintaining the integrity of …

**Accessions** — [HGNC:1573](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1573) · Entrez [889](https://www.ncbi.nlm.nih.gov/gene/889) · UniProt [O00522](https://www.uniprot.org/uniprotkb/O00522) · Ensembl [ENSG00000001631](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000001631)

## Data

Gene col 16: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16]; `tensor/DDL_lfc|DDL_z.npy` [16]; `embed/gene_vectors.npy` [16]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16 or target_col == 16). Every well: [[KRIT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRIT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
