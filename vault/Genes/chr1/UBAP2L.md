---
symbol: "UBAP2L"
type: "gene"
col: 6772
ensembl_id: "ENSG00000143569"
name: "ubiquitin associated protein 2 like"
location: "1q21.3"
module: 173
arm: "+"
pooled_cpm: 152.9
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# UBAP2L

*ubiquitin associated protein 2 like* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.91× (z +13.6, q 1e-39, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.542× (z -9.1, q 3e-17, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED12]] (+0.73, fdr 1e-05), [[BRPF3]] (+0.68, fdr 1e-05), [[ARFGAP2]] (+0.67, fdr 1e-05); moves opposite to [[TECPR1]] (-0.62, fdr 3e-05), [[ARID3B]] (-0.59, fdr 3e-05), [[PBX4]] (-0.59, fdr 6e-05).
> It is in [[Module 173]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6772.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +13.6 | 1e-39 | 45/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +8.1 | 2e-13 | 45/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.52×** | +6.2 | 8e-08 | 43/48 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +5.7 | 2e-06 | 3/50 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +4.9 | 1e-04 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.8 | 1e-04 | 34/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +4.1 | 0.003 | 29/48 (HOP62, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.61×** | +3.7 | 0.014 | 27/49 (NCI-H460, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.014 | 27/48 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.6 | 0.021 | 24/48 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.069 | 23/47 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.16× | +3.1 | 0.10 | 12/48 (SNU-1, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6772.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.542×** | -9.1 | 3e-17 | 48/48 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.568×** | -8.4 | 8e-15 | 48/48 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.582×** | -8.1 | 1e-13 | 46/48 (NCI-H23, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.660×** | -6.2 | 8e-08 | 43/48 (H4, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.659×** | -6.0 | 2e-07 | 28/44 (NCI-H23, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.700×** | -5.1 | 3e-05 | 40/47 (CFPAC-1, RKO, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.713×** | -4.7 | 2e-04 | 30/45 (NCI-H23, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.736×** | -4.6 | 3e-04 | 40/48 (A-172, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.749×** | -4.3 | 0.001 | 30/49 (SNU-1, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.832×** | -3.9 | 0.005 | 23/48 (HT-29, BT-474, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.797×** | -3.4 | 0.034 | 25/49 (CHP-212, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6772. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 235 | 13 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +38.2) | — |
| [[NCI-H1573 (line)]] | alt | 137 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +17.9) | — |
| [[NCI-H23 (line)]] | alt | 289 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.157× (z -22.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.481× (z -9.4) |
| [[PANC-1 (line)]] | alt | 123 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +13.8) | [[Panobinostat (drug)]] 5 µM 0.513× (z -8.7) |
| [[LoVo (line)]] | wt | 119 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[RKO (line)]] | wt | 152 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[A-172 (line)]] | wt | 179 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +21.0) | [[Dinaciclib (drug)]] 5 µM 0.420× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[A498 (line)]] | wt | 184 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.419× (z -10.0) |
| [[COLO 205 (line)]] | alt | 142 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +17.5) | — |
| [[Hs 766T (line)]] | wt | 161 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +18.8) | — |
| [[hTERT-HPNE (line)]] | wt | 145 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.386× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 125 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.410× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 131 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.396× (z -9.7) |
| [[AN3 CA (line)]] | alt | 189 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.9) | [[Canagliflozin (drug)]] 0.05 µM 0.283× (z -8.8) |
| [[H4 (line)]] | wt | 146 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.352× (z -8.8) |
| [[HOP62 (line)]] | alt | 112 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 98.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.447× (z -9.0) |
| [[HT-29 (line)]] | alt | 136 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.480× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 142 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.444× (z -8.8) |
| [[SNU-423 (line)]] | alt | 145 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +12.8) | — |
| [[A549 (line)]] | wt | 109 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +13.5) | — |
| [[AsPC-1 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.463× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.377× (z -11.1) ⚠ toxic |
| [[J82 (line)]] | alt | 140 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +11.4) | — |
| [[KATO III (line)]] | alt | 98.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 296 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.0) | — |
| [[SHP-77 (line)]] | alt | 160 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[SK-MEL-2 (line)]] | alt | 114 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +15.5) | — |
| [[SNU-1 (line)]] | wt | 154 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[SW 1088 (line)]] | alt | 132 | 0 | 1 | — | [[Thymopentin (drug)]] 0.05 µM 0.0837× (z -9.2) |
| [[SW48 (line)]] | wt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SW480 (line)]] | alt | 122 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +8.5) | — |
| [[A-427 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 130 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 227 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 107 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 85.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 122 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6772), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED12]] | +0.73 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[BRPF3]] | +0.68 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ARFGAP2]] | +0.67 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ATP13A1]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[CNOT3]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[EIF2B5]] | +0.63 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[CHD3]] | +0.63 | +0.52 / +0.49 | both halves | 1e-05 | same gene group |
| [[HLA-H]] | +0.63 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[HMGN2]] | +0.62 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[C5orf15]] | +0.62 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[C19orf54]] | +0.62 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[USP22]] | +0.61 | +0.47 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TECPR1]] | -0.62 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[ARID3B]] | -0.59 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[PBX4]] | -0.59 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[UBE2R2]] | -0.59 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[FLNB-AS1]] | -0.59 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ARPC1B]] | -0.58 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[NR2C1]] | -0.58 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[CHCHD2]] | -0.58 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[MYO9B]] | -0.57 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[MAP2K1]] | -0.57 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[COX6A1]] | -0.57 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[RPS21]] | -0.57 | -0.41 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises UBAP2L's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises UBAP2L's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.751). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-9.9, 4.8); signed map (16.2, -22.5). **Vector** length 97.7, 31.9% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +13.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +7.2 | +3.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +5.4 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +5.1 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | -0.8 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.3 | -0.5 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +2.2 | +0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.1 | -0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | -0.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.8 | -8.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.4 | -6.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.0 | -4.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.7 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +0.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | +0.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.3 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin associated protein 2 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:154,220,179-154,271,510 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NICE-4, KIAA0144 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14157](https://www.uniprot.org/uniprotkb/Q14157) (Ubiquitin-associated protein 2-like):

> Recruits the ubiquitination machinery to RNA polymerase II for polyubiquitination, removal and degradation, when the transcription-coupled nucleotide excision repair (TC-NER) machinery fails to resolve DNA damage. Plays an important role in the activity of long-term repopulating hematopoietic stem cells (LT-HSCs) (By similarity). Is a regulator of stress granule assembly, required for their efficient formation. Required for proper brain development and neocortex lamination (By similarity).

**Summary**, from NCBI Gene [9898](https://www.ncbi.nlm.nih.gov/gene/9898):

> Enables RNA binding activity. Involved in binding activity of sperm to zona pellucida; positive regulation of stress granule assembly; and stress granule assembly. Acts upstream of or within hematopoietic stem cell homeostasis. Part of PcG protein complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29877](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29877) · Entrez [9898](https://www.ncbi.nlm.nih.gov/gene/9898) · UniProt [Q14157](https://www.uniprot.org/uniprotkb/Q14157) · Ensembl [ENSG00000143569](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143569)

## Data

Gene col 6772: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6772); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6772, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6772]; `tensor/DDL_lfc|DDL_z.npy` [6772]; `embed/gene_vectors.npy` [6772]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6772 or target_col == 6772). Every well: [[UBAP2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBAP2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
