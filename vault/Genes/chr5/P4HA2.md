---
symbol: "P4HA2"
type: "gene"
col: 1026
ensembl_id: "ENSG00000072682"
name: "prolyl 4-hydroxylase subunit alpha 2"
location: "5q31.1"
module: 99
arm: "+"
pooled_cpm: 143.99
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 27
n_dd_up_clean: 8
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# P4HA2

*prolyl 4-hydroxylase subunit alpha 2* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.18× (z +9.4, q 4e-18, up in 12 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.57× (z +7.6, q 9e-12, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.308× (z -28.0, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCB6]] (+0.72, fdr 7e-06), [[FAM219A]] (+0.71, fdr 7e-06), [[GAPDH]] (+0.66, fdr 7e-06); moves opposite to [[ZC3H7B]] (-0.59, fdr 1e-05), [[TFAM]] (-0.55, fdr 2e-05), [[HNRNPD]] (-0.55, fdr 1e-04).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CASZ1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1026.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +9.4 | 4e-18 | 12/49 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +7.6 | 9e-12 | 32/47 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.61×** | +7.5 | 9e-12 | 31/47 (HEC-1-A, KATO III, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +6.9 | 8e-10 | 35/47 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +5.9 | 3e-07 | 26/47 (HEC-1-A, RKO, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.43×** | +4.3 | 0.001 | 23/48 (MIA PaCa-2, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Fumaric acid (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.041 | 25/48 (A-172, A549, …) | top dose only | plate-row cell shift; position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.4 | 0.049 | 22/44 (A-427, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.049 | 21/48 (A-172, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Infigratinib (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.049 | 22/47 (AsPC-1, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1026.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.308×** | -28.0 | 0e+00 | 45/47 (MIA PaCa-2, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.273×** | -21.8 | 0e+00 | 45/47 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.422×** | -13.9 | 6e-42 | 40/47 (C32, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.484×** | -11.7 | 2e-29 | 38/46 (LOX-IMVI, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.501×** | -11.2 | 7e-27 | 43/46 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.613×** | -7.6 | 3e-12 | 34/44 (LOX-IMVI, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.643×** | -7.4 | 8e-12 | 36/47 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.658×** | -7.0 | 1e-10 | 37/47 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.753×** | -6.7 | 1e-09 | 32/47 (HT-29, C32, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.681×** | -6.1 | 6e-08 | 35/46 (HEC-1-A, SW1417, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.719×** | -5.5 | 2e-06 | 26/47 (LoVo, C-33 A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.713×** | -5.5 | 2e-06 | 28/43 (RPMI-7951, J82, …) | all doses, flat | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.546×** | -5.3 | 5e-06 | 33/48 (LoVo, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.731×** | -5.3 | 5e-06 | 29/47 (NCI-H460, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.750×** | -4.8 | 5e-05 | 30/47 (HOP62, SW 900, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.753×** | -4.8 | 6e-05 | 26/47 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.590×** | -4.6 | 1e-04 | 29/48 (HS-578T, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.770×** | -4.4 | 3e-04 | 34/47 (NCI-H460, HS-578T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.775×** | -4.3 | 5e-04 | 26/47 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.787×** | -4.0 | 0.001 | 24/47 (HOP62, A549, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.634×** | -4.0 | 0.001 | 23/47 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.787×** | -3.9 | 0.002 | 30/48 (HS-578T, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1026. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 323 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -25.6) |
| [[C32 (line)]] | wt | 207 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0992× (z -26.6) |
| [[LoVo (line)]] | wt | 152 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -17.7) |
| [[HEC-1-A (line)]] | alt | 109 | 4 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.65× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -21.0) |
| [[HT-29 (line)]] | alt | 97.9 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -28.8) |
| [[NCI-H460 (line)]] | wt | 101 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -31.0) |
| [[RPMI-7951 (line)]] | alt | 343 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -25.1) |
| [[A-427 (line)]] | wt | 105 | 3 | 4 | [[Ixazomib citrate (drug)]] 5 µM 2.55× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.0892× (z -36.1) |
| [[MIA PaCa-2 (line)]] | alt | 109 | 3 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.67× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.0742× (z -41.3) |
| [[A549 (line)]] | wt | 173 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -23.3) |
| [[C-33 A (line)]] | alt | 133 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -24.4) |
| [[J82 (line)]] | alt | 137 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.504× (z -10.5) |
| [[KATO III (line)]] | alt | 68.2 | 2 | 4 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.11× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -21.7) |
| [[LOX-IMVI (line)]] | wt | 133 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -26.7) |
| [[NCI-H1792 (line)]] | alt | 213 | 1 | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.404× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.461× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 66.8 | 1 | 5 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.41× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.0770× (z -36.4) |
| [[PANC-1 (line)]] | alt | 64.5 | 4 | 2 | [[Ixazomib citrate (drug)]] 0.5 µM 2.24× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -19.0) |
| [[RKO (line)]] | wt | 84.4 | 2 | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.73× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -24.4) |
| [[SW480 (line)]] | alt | 62.9 | 3 | 3 | [[Ixazomib citrate (drug)]] 0.5 µM 2.61× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -16.0) |
| [[HOP62 (line)]] | alt | 437 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -30.9) |
| [[NCI-H1573 (line)]] | alt | 45.1 | 1 | 4 | [[Bortezomib (drug)]] 0.05 µM 2.98× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -15.8) |
| [[SK-MEL-2 (line)]] | alt | 151 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -29.1) |
| [[AsPC-1 (line)]] | alt | 60.9 | 2 | 2 | [[Bortezomib (drug)]] 0.05 µM 2.88× (z +9.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.257× (z -13.0) |
| [[CFPAC-1 (line)]] | alt | 163 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.284× (z -15.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.493× (z -12.7) |
| [[H4 (line)]] | wt | 285 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0835× (z -37.2) |
| [[Hs 766T (line)]] | wt | 114 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -11.8) |
| [[LS 180 (line)]] | wt | 95.5 | 1 | 3 | [[Ixazomib citrate (drug)]] 0.5 µM 2.21× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -25.6) |
| [[NCI-H2030 (line)]] | alt | 130 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -36.3) |
| [[SW1417 (line)]] | alt | 47.8 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.09× (z +11.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.304× (z -11.1) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.374× (z -9.0) |
| [[COLO 205 (line)]] | alt | 48.0 | 1 | 2 | [[Ixazomib citrate (drug)]] 5 µM 3.48× (z +8.7) | [[Harringtonine (drug)]] 5 µM 0.111× (z -14.6) |
| [[HCT15 (line)]] | alt | 123 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -15.9) |
| [[HS-578T (line)]] | alt | 411 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -18.5) |
| [[hTERT-HPNE (line)]] | wt | 263 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -17.4) |
| [[NCI-H2347 (line)]] | alt | 127 | 1 | 2 | [[Bortezomib (drug)]] 0.05 µM 2.30× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -15.9) |
| [[Panc 03.27 (line)]] | alt | 80.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.61× (z +10.6) | — |
| [[SW 900 (line)]] | alt | 189 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -28.8) |
| [[SNU-423 (line)]] | alt | 331 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -15.1) |
| [[SW48 (line)]] | wt | 89.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -13.3) |
| [[AN3 CA (line)]] | alt | 190 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -10.8) |
| [[BT-474 (line)]] | alt | 44.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.327× (z -8.9) |
| [[CHP-212 (line)]] | wt | 140 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -8.9) |
| [[SHP-77 (line)]] | alt | 53.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -13.5) |
| [[SW 1088 (line)]] | alt | 561 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -11.5) |
| [[A498 (line)]] | wt | 200 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 102 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 125 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1026), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCB6]] | +0.72 | +0.63 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[FAM219A]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[GAPDH]] | +0.66 | +0.68 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 506 |
| [[PFKFB4]] | +0.63 | +0.66 / +0.58 | both halves | 7e-06 | same gene group |
| [[NQO2]] | +0.63 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[LRP1]] | +0.62 | +0.65 / +0.57 | both halves | 9e-06 | same gene group |
| [[INSIG2]] | +0.61 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[TPI1]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[MACO1]] | +0.61 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[UBE2O]] | +0.61 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[LNPK]] | +0.61 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[GYS1]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H7B]] | -0.59 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[TFAM]] | -0.55 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[HNRNPD]] | -0.55 | -0.35 / -0.55 | both halves | 1e-04 | pathway: Dengue Virus Genome Translation and Replication |
| [[MRRF]] | -0.54 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[GNL3L]] | -0.53 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[SCAF8]] | -0.53 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[SENP6]] | -0.53 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[SLC25A13]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 | same gene group; pathway: HALLMARK_GLYCOLYSIS |
| [[POGLUT1]] | -0.51 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[C22orf46]] | -0.51 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[CHTOP]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[TRMT13]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASZ1]] | B | CASZ1 activity lowers P4HA2's level | lines that do not express CASZ1 (10) vs lines expressing it (40) | 2.16× higher at baseline in the lines without CASZ1 | 0.031 | ⚠ within organs, on part of the lines; also absent: SBK1, CPLX1, LLGL2; maybe low, not absent |
| [[PLOD2]] | B | PLOD2 activity raises P4HA2's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 2.21× lower at baseline in the lines without PLOD2 | 0.047 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[TTLL7]] | B | TTLL7 activity raises P4HA2's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 2.35× lower at baseline in the lines without TTLL7 | 0.048 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725 |
| [[PSMB5]] | B | PSMB5 activity lowers P4HA2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.6, -15.7); signed map (-40.1, 30.1). **Vector** length 138, 46.4% of its response variance represented; |z| ≥ 3 in 1,417 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Gluconeogenesis* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.5 | +7.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.3 | +7.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.0 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +5.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.1 | +3.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.7 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.9 | +2.5 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -8.6 | -11.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.3 | -13.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -6.4 | -5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.4 | -7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -5.9 | -4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.3 | -4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.2 | -3.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.8 | -4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.6 | -6.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.6 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | prolyl 4-hydroxylase subunit alpha 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:132,190,147-132,295,315 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C-P4Halpha(II), lncRNA-PE |
| Gene groups (HGNC) | Iron (II) and 2-oxoglutarate dependent oxygenases; MicroRNA protein coding host genes; Prolyl 4-hydroxylase subunits |
| Hallmark sets | HEME_METABOLISM, GLYCOLYSIS, HYPOXIA |
| Reactome | 7 pathways, smallest: Maturation of DENV proteins; Collagen biosynthesis and modifying enzymes; Collagen formation |
| Matched by | ensembl_id |

**Function**, from UniProt [O15460](https://www.uniprot.org/uniprotkb/O15460) (Prolyl 4-hydroxylase subunit alpha-2):

> Catalyzes the post-translational formation of 4-hydroxyproline in -Xaa-Pro-Gly- sequences in collagens and other proteins.

**Summary**, from NCBI Gene [8974](https://www.ncbi.nlm.nih.gov/gene/8974):

> This gene encodes a component of prolyl 4-hydroxylase, a key enzyme in collagen synthesis composed of two identical alpha subunits and two beta subunits. The encoded protein is one of several different types of alpha subunits and provides the major part of the catalytic site of the active enzyme. In collagen and related proteins, prolyl 4-hydroxylase catalyzes the formation of 4-hydroxyproline that is essential to the proper three-dimensional folding of newly synthesized procollagen chains. …

**Accessions** — [HGNC:8547](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8547) · Entrez [8974](https://www.ncbi.nlm.nih.gov/gene/8974) · UniProt [O15460](https://www.uniprot.org/uniprotkb/O15460) · Ensembl [ENSG00000072682](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072682)

## Data

Gene col 1026: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1026); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1026, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1026]; `tensor/DDL_lfc|DDL_z.npy` [1026]; `embed/gene_vectors.npy` [1026]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1026 or target_col == 1026). Every well: [[P4HA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/P4HA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
