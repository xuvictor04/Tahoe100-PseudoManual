---
symbol: "PAIP2"
type: "gene"
col: 4215
ensembl_id: "ENSG00000120727"
name: "poly(A) binding protein interacting protein 2"
location: "5q31.2"
module: 69
arm: "+"
pooled_cpm: 157.43
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# PAIP2

*poly(A) binding protein interacting protein 2* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.59× (z +9.4, q 3e-18, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.497× (z -14.2, q 3e-43, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[venetoclax (drug)]] 5 µM: 0.479× (z -7.8, q 1e-12, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLU7]] (+0.71, fdr 5e-05), [[BNIP3L]] (+0.70, fdr 7e-06), [[OTUD5]] (+0.69, fdr 7e-06); moves opposite to [[PROSER1]] (-0.55, fdr 1e-05), [[CAD]] (-0.51, fdr 1e-05), [[HEATR3]] (-0.51, fdr 2e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4215.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.59×** | +9.4 | 3e-18 | 38/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +8.4 | 2e-14 | 38/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.87×** | +6.7 | 5e-09 | 44/48 (SHP-77, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +6.0 | 4e-07 | 35/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.32×** | +5.6 | 2e-06 | 32/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.28×** | +5.1 | 4e-05 | 29/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.24×** | +4.4 | 8e-04 | 25/49 (SW480, A498, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.49×** | +4.3 | 0.001 | 34/49 (LoVo, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.019 | 21/48 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.024 | 27/48 (LoVo, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.3 | 0.058 | 18/48 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.17× | +3.2 | 0.065 | 20/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4215.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.497×** | -14.2 | 3e-43 | 48/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.479×** | -7.8 | 1e-12 | 43/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.501×** | -7.4 | 3e-11 | 43/48 (MIA PaCa-2, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.530×** | -6.7 | 2e-09 | 44/48 (MIA PaCa-2, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.543×** | -6.5 | 9e-09 | 40/48 (MIA PaCa-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.603×** | -5.4 | 7e-06 | 35/48 (MIA PaCa-2, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.798×** | -4.6 | 4e-04 | 25/48 (C32, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.800×** | -4.3 | 0.001 | 27/50 (NCI-H1573, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.859× | -4.3 | 0.001 | 14/48 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **0.821×** | -4.0 | 0.004 | 23/48 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.827×** | -3.7 | 0.010 | 22/47 (SNU-423, AN3 CA, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | 0.836× | -3.6 | 0.012 | 21/48 (SW480, AN3 CA, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.825×** | -3.6 | 0.013 | 25/48 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.783×** | -3.6 | 0.015 | 26/49 (MIA PaCa-2, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | **0.801×** | -3.2 | 0.047 | 22/48 (LoVo, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.854× | -3.2 | 0.047 | 19/47 (A549, NCI-H1573, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.849× | -3.2 | 0.047 | 19/47 (NCI-H1573, C32, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.860× | -3.1 | 0.067 | 8/49 (AsPC-1, NCI-H1573, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4215. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 220 | 0 | 6 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.278× (z -19.1) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.170× (z -13.8) |
| [[SW480 (line)]] | alt | 159 | 5 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +11.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.531× (z -10.1) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 161 | 2 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +11.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.495× (z -11.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.327× (z -9.2) |
| [[PANC-1 (line)]] | alt | 155 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +12.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.522× (z -9.4) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 149 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +12.1) | — |
| [[NCI-H460 (line)]] | wt | 181 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +10.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.320× (z -14.6) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 168 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +9.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.411× (z -13.2) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.321× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 182 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +9.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.352× (z -13.0) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 231 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.620× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 165 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.496× (z -11.0) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.329× (z -9.1) |
| [[LS 180 (line)]] | wt | 116 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.24× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 151 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SHP-77 (line)]] | alt | 195 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.83× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.532× (z -9.2) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 109 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +8.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.351× (z -9.4) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 170 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 1.91× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A498 (line)]] | wt | 130 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.387× (z -13.3) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 160 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.450× (z -10.3) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.417× (z -9.4) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 152 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 161 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 152 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.486× (z -9.1) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.478× (z -10.1) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.420× (z -10.3) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 170 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.483× (z -9.1) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.507× (z -8.8) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.433× (z -13.0) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 159 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.449× (z -10.5) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 130 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.417× (z -9.2) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 175 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.523× (z -9.1) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 192 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 161 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 163 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 139 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 153 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 146 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 141 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 158 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4215), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLU7]] | +0.71 | +0.40 / +0.80 | both halves | 5e-05 |  |
| [[BNIP3L]] | +0.70 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[OTUD5]] | +0.69 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[TBC1D15]] | +0.68 | +0.38 / +0.79 | both halves | 7e-05 |  |
| [[UBXN7]] | +0.67 | +0.49 / +0.73 | both halves | 1e-05 |  |
| [[RB1CC1]] | +0.67 | +0.41 / +0.75 | both halves | 4e-05 |  |
| [[SERINC1]] | +0.65 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[WDR26]] | +0.65 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CRIPT]] | +0.63 | +0.49 / +0.73 | both halves | 1e-05 |  |
| [[GCC2]] | +0.61 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[TCP11L2]] | +0.61 | +0.40 / +0.69 | both halves | 5e-05 |  |
| [[RAB5A]] | +0.60 | +0.58 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PROSER1]] | -0.55 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[CAD]] | -0.51 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[HEATR3]] | -0.51 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[CLN6]] | -0.51 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[VARS1]] | -0.51 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[MRPL3]] | -0.50 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[ABCC4]] | -0.50 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[TADA2A]] | -0.49 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[LARP1]] | -0.49 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ZNRF3]] | -0.49 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[NAA15]] | -0.49 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[RIOX2]] | -0.49 | -0.49 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.565). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.3, -44.8); signed map (-15.4, 10.0). **Vector** length 124, 40.4% of its response variance represented; |z| ≥ 3 in 1,121 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PF-06260933 (drug)]] 5 µM |  | +4.7 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | -0.3 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | -1.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -15.4 | -14.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -9.9 | -7.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -9.8 | -7.4 |
|  | [[EX229 (drug)]] 5 µM |  | -9.1 | -6.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -8.7 | -6.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.7 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | poly(A) binding protein interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:139,341,587-139,369,720 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PAIP2A |
| Reactome | 2 pathways, smallest: M-decay: degradation of maternal mRNAs by maternally stored factors; Maternal to zygotic transition (MZT) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BPZ3](https://www.uniprot.org/uniprotkb/Q9BPZ3) (Polyadenylate-binding protein-interacting protein 2):

> Acts as a repressor in the regulation of translation initiation of poly(A)-containing mRNAs. Its inhibitory activity on translation is mediated via its action on PABPC1. Displaces the interaction of PABPC1 with poly(A) RNA and competes with PAIP1 for binding to PABPC1. Its association with PABPC1 results in disruption of the cytoplasmic poly(A) RNP structure organization.

**Summary**, from NCBI Gene [51247](https://www.ncbi.nlm.nih.gov/gene/51247):

> Enables translation repressor activity. Involved in negative regulation of translational initiation. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17970](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17970) · Entrez [51247](https://www.ncbi.nlm.nih.gov/gene/51247) · UniProt [Q9BPZ3](https://www.uniprot.org/uniprotkb/Q9BPZ3) · Ensembl [ENSG00000120727](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120727)

## Data

Gene col 4215: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4215); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4215, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4215]; `tensor/DDL_lfc|DDL_z.npy` [4215]; `embed/gene_vectors.npy` [4215]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4215 or target_col == 4215). Every well: [[PAIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
