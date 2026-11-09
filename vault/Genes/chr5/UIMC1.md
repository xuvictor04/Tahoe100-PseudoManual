---
symbol: "UIMC1"
type: "gene"
col: 1490
ensembl_id: "ENSG00000087206"
name: "ubiquitin interaction motif containing 1"
location: "5q35.2"
module: 18
arm: "+"
pooled_cpm: 121.51
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# UIMC1

*ubiquitin interaction motif containing 1* — 5q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.55× (z +13.3, q 2e-37, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.654× (z -8.5, q 9e-15, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RYK]] (+0.57, fdr 1e-05), [[RILPL1]] (+0.56, fdr 9e-05), [[ZNF786]] (+0.55, fdr 3e-05); moves opposite to [[TOX4]] (-0.50, fdr 1e-04), [[FAM117A]] (-0.47, fdr 2e-05), [[STK17B]] (-0.47, fdr 6e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1490.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.55×** | +13.3 | 2e-37 | 48/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.03×** | +11.6 | 9e-29 | 45/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +8.7 | 4e-16 | 36/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +7.1 | 2e-10 | 34/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +6.5 | 8e-09 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +6.5 | 8e-09 | 39/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +5.2 | 2e-05 | 29/48 (NCI-H460, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +4.6 | 3e-04 | 26/48 (SNU-423, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.23×** | +4.2 | 0.002 | 22/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +4.1 | 0.002 | 25/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.23×** | +4.1 | 0.002 | 25/48 (CFPAC-1, PANC-1, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.0 | 0.002 | 27/48 (CFPAC-1, HCT15, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.0 | 0.002 | 20/38 (AsPC-1, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.21×** | +3.7 | 0.008 | 19/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.6 | 0.013 | 10/49 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.036 | 17/48 (MIA PaCa-2, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1490.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.654×** | -8.5 | 9e-15 | 40/48 (SK-MEL-2, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.721×** | -6.6 | 1e-08 | 33/48 (A549, PANC-1, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.750×** | -5.6 | 5e-06 | 26/44 (SK-MEL-2, A-427, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.777×** | -5.1 | 5e-05 | 27/48 (A549, LOX-IMVI, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.762×** | -5.0 | 5e-05 | 24/45 (NCI-H2030, HEC-1-A, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.845× | -4.8 | 2e-04 | 24/48 (HOP62, SW1417, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.800×** | -4.5 | 6e-04 | 26/48 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.814×** | -4.2 | 0.002 | 25/49 (A-427, C-33 A, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.882× | -3.6 | 0.020 | 22/49 (HS-578T, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.888× | -3.4 | 0.039 | 12/48 (SW1417, A-427, …) | top dose only | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.800×** | -3.1 | 0.086 | 25/48 (HCT15, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.858× | -3.1 | 0.093 | 17/48 (HS-578T, A-172, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.860× | -3.0 | 0.100 | 16/48 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1490. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 124 | 7 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.24× (z +15.5) | — |
| [[PANC-1 (line)]] | alt | 131 | 5 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.436× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.531× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 131 | 5 (2 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 4.77× (z +11.8) | [[Panobinostat (drug)]] 0.5 µM 0.537× (z -9.0) |
| [[COLO 205 (line)]] | alt | 74.2 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 21.8× (z +12.9) | — |
| [[HEC-1-A (line)]] | alt | 146 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.82× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[KATO III (line)]] | alt | 79.4 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.43× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.443× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 154 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.27× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[LS 180 (line)]] | wt | 76.0 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 9.30× (z +13.5) | — |
| [[NCI-H1573 (line)]] | alt | 111 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 187 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW480 (line)]] | alt | 121 | 3 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 5.04× (z +15.6) | [[Auranofin (drug)]] 5 µM 0.591× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 125 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.67× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 145 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.14× (z +10.4) | [[Lonafarnib (drug)]] 5 µM 0.121× (z -13.5) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 149 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.91× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.383× (z -12.1) |
| [[A549 (line)]] | wt | 148 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.428× (z -9.5) |
| [[H4 (line)]] | wt | 120 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.68× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[LOX-IMVI (line)]] | wt | 150 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.18× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.437× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[MIA PaCa-2 (line)]] | alt | 157 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.68× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 108 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 107 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.73× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.333× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[RKO (line)]] | wt | 143 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 7.59× (z +13.0) | — |
| [[SW48 (line)]] | wt | 118 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.26× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[C-33 A (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[C32 (line)]] | wt | 96.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.327× (z -11.4) |
| [[HOP62 (line)]] | alt | 124 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.618× (z -8.6) |
| [[HS-578T (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -8.5) ⚠ cell-cycle shift, explains ~24% of this change |
| [[HT-29 (line)]] | alt | 77.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.81× (z +10.2) | — |
| [[J82 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.574× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 94.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.49× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SNU-1 (line)]] | wt | 148 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.41× (z +11.3) | — |
| [[SW 1271 (line)]] | alt | 148 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0863× (z -9.2) |
| [[SW1417 (line)]] | alt | 159 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.40× (z +8.9) | — |
| [[A-172 (line)]] | wt | 90.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 184 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 126 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 95.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 189 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1490), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RYK]] | +0.57 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[RILPL1]] | +0.56 | +0.64 / +0.36 | both halves | 9e-05 |  |
| [[ZNF786]] | +0.55 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[PEX7]] | +0.55 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[PEMT]] | +0.55 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[RPIA]] | +0.54 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[DDX54]] | +0.54 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[FOXK2]] | +0.54 | +0.67 / +0.50 | both halves | 1e-05 | pathway: Deubiquitination |
| [[PCCB]] | +0.54 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[PAXBP1]] | +0.54 | +0.36 / +0.65 | both halves | 1e-04 |  |
| [[TXNRD3]] | +0.54 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[PACS2]] | +0.53 | +0.53 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOX4]] | -0.50 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[FAM117A]] | -0.47 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[STK17B]] | -0.47 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[ATP7A]] | -0.47 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[TOB1]] | -0.46 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[RP2]] | -0.44 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[RAB8A]] | -0.44 | -0.37 / -0.43 | both halves | 7e-05 |  |
| [[PRKCA]] | -0.44 | -0.51 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises UIMC1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.534). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.9, -28.6); signed map (-42.7, -16.9). **Vector** length 86.0, 24.9% of its response variance represented; |z| ≥ 3 in 1,101 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +3.3 | -5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +2.9 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +2.9 | -5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | -0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | -0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.2 | +2.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.5 | -8.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | +3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.1 | +8.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | +6.5 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -2.0 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -4.8 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.9 | -1.2 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin interaction motif containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:176,905,005-177,022,633 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAP80 |
| Gene groups (HGNC) | BRCA1 A complex; Zinc fingers UBZ4 CCHC-type |
| Reactome | 14 pathways, smallest: Metalloprotease DUBs; Nonhomologous End-Joining (NHEJ); Recruitment and ATM-mediated phosphorylation of repair and signaling proteins at DNA double strand breaks |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RL1](https://www.uniprot.org/uniprotkb/Q96RL1) (BRCA1-A complex subunit RAP80):

> Ubiquitin-binding protein. Specifically recognizes and binds 'Lys-63'-linked ubiquitin. Plays a central role in the BRCA1-A complex by specifically binding 'Lys-63'-linked ubiquitinated histones H2A and H2AX at DNA lesions sites, leading to target the BRCA1-BARD1 heterodimer to sites of DNA damage at double-strand breaks (DSBs). The BRCA1-A complex also possesses deubiquitinase activity that specifically removes 'Lys-63'-linked ubiquitin on histones H2A and H2AX. Also weakly binds monoubiquitin …

**Summary**, from NCBI Gene [51720](https://www.ncbi.nlm.nih.gov/gene/51720):

> This gene encodes a nuclear protein that interacts with Brca1 (breast cancer 1) in a complex to recognize and repair DNA lesions. This protein binds ubiquitinated lysine 63 of histone H2A and H2AX. This protein may also function as a repressor of transcription. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:30298](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30298) · Entrez [51720](https://www.ncbi.nlm.nih.gov/gene/51720) · UniProt [Q96RL1](https://www.uniprot.org/uniprotkb/Q96RL1) · Ensembl [ENSG00000087206](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087206)

## Data

Gene col 1490: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1490); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1490, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1490]; `tensor/DDL_lfc|DDL_z.npy` [1490]; `embed/gene_vectors.npy` [1490]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1490 or target_col == 1490). Every well: [[UIMC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UIMC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
