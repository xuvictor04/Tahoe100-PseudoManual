---
symbol: "NNT"
type: "gene"
col: 3424
ensembl_id: "ENSG00000112992"
name: "nicotinamide nucleotide transhydrogenase"
location: "5p12"
module: 192
arm: "+"
pooled_cpm: 47.75
n_lines_expressing: 44
n_dd_up: 9
n_dd_down: 24
n_dd_up_clean: 3
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 6
direction_downstream: 7
tags: ["gene", "module/192"]
generated_by: "tahoemap"
---

# NNT

*nicotinamide nucleotide transhydrogenase* — 5p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.46× (z +6.8, q 5e-09, up in 30 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 5 µM: 1.68× (z +4.9, q 2e-04, up in 25 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.288× (z -22.3, q 0e+00, down in 42 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF2D]] (+0.67, fdr 3e-05), [[MCCC2]] (+0.66, fdr 5e-05), [[DECR1]] (+0.65, fdr 2e-05); moves opposite to [[PLIN3]] (-0.69, fdr 1e-05), [[MIDN]] (-0.67, fdr 1e-05), [[ARID3A]] (-0.64, fdr 3e-05).
> It is in [[Module 192]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ANGPTL4]] → it (grade B ⚠); 7 go from it, the strongest it → [[N4BP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3424.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +6.8 | 5e-09 | 30/43 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +5.7 | 3e-06 | 20/36 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.24×** | +5.6 | 5e-06 | 21/42 (AsPC-1, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[NG25 (drug)]] 5 µM |  | **1.68×** | +4.9 | 2e-04 | 25/41 (SW 900, C32, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.3 | 0.002 | 21/42 (SW 900, J82, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +3.8 | 0.014 | 17/42 (NCI-H2347, C32, …) | two highest doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.021 | 18/41 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.21×** | +3.5 | 0.036 | 13/42 (AsPC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.3 | 0.056 | 10/42 (LoVo, C32, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.3 | 0.056 | 0/43 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.21×** | +3.2 | 0.065 | 15/38 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.20×** | +3.2 | 0.069 | 13/43 (NCI-H2347, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.086 | 13/41 (Hs 766T, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3424.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.288×** | -22.3 | 0e+00 | 42/42 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.290×** | -22.2 | 0e+00 | 42/42 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.292×** | -22.1 | 0e+00 | 42/42 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.530×** | -16.1 | 0e+00 | 33/42 (NCI-H1792, H4, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.534×** | -11.3 | 2e-27 | 38/42 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.600×** | -9.2 | 5e-18 | 35/42 (LoVo, SHP-77, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.717×** | -8.4 | 3e-15 | 34/42 (SW480, SHP-77, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.625×** | -8.4 | 3e-15 | 33/42 (C32, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.635×** | -8.1 | 3e-14 | 33/42 (SW48, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.638×** | -7.7 | 6e-13 | 29/42 (AN3 CA, COLO 205, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.656×** | -7.5 | 2e-12 | 30/42 (SHP-77, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.669×** | -7.2 | 3e-11 | 28/42 (SNU-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.685×** | -6.8 | 5e-10 | 32/42 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.579×** | -5.1 | 1e-05 | 25/42 (SW480, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.580×** | -5.1 | 1e-05 | 26/43 (H4, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~25% here); composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.615×** | -4.6 | 2e-04 | 23/42 (CFPAC-1, C32, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.785×** | -4.3 | 5e-04 | 21/42 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.788×** | -4.3 | 6e-04 | 23/42 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.693×** | -3.4 | 0.015 | 16/42 (SNU-1, Panc 03.27, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3424. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.2 | 1 (1 ⚠) | 8 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -15.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.256× (z -13.4) |
| [[SW480 (line)]] | alt | 96.8 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.124× (z -28.1) |
| [[LoVo (line)]] | wt | 66.7 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.45× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -15.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.313× (z -14.0) |
| [[NCI-H1792 (line)]] | alt | 67.2 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -21.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.308× (z -12.3) |
| [[Panc 03.27 (line)]] | alt | 60.2 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.202× (z -15.8) |
| [[SHP-77 (line)]] | alt | 193 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -20.7) |
| [[AN3 CA (line)]] | alt | 177 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -13.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.225× (z -10.2) |
| [[C32 (line)]] | wt | 67.5 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -11.2) |
| [[PANC-1 (line)]] | alt | 51.5 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -12.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.377× (z -12.2) |
| [[SNU-423 (line)]] | alt | 56.8 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.187× (z -16.8) |
| [[AsPC-1 (line)]] | alt | 25.9 | 1 (1 ⚠) | 4 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.18× (z +8.5) ⚠ cell-cycle shift, explains ~69% of this change | [[Digitoxin (drug)]] 5 µM 0.250× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.318× (z -8.9) |
| [[COLO 205 (line)]] | alt | 64.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -11.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.251× (z -10.9) |
| [[H4 (line)]] | wt | 70.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -19.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0668× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 31.0 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.263× (z -10.9) |
| [[SW1417 (line)]] | alt | 75.0 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.188× (z -20.1) |
| [[A-172 (line)]] | wt | 44.3 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +11.9) ⚠ cell-cycle shift, explains ~33% of this change | [[Belinostat (drug)]] 5 µM 0.204× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 32.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -12.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.334× (z -10.0) |
| [[J82 (line)]] | alt | 84.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -17.4) |
| [[KATO III (line)]] | alt | 55.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -20.8) |
| [[SNU-1 (line)]] | wt | 63.9 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.233× (z -10.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.250× (z -9.8) |
| [[SW48 (line)]] | wt | 64.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -12.7) |
| [[CFPAC-1 (line)]] | alt | 36.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.82× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -13.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.307× (z -10.8) |
| [[HCT15 (line)]] | alt | 69.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -12.7) |
| [[HOP62 (line)]] | alt | 20.3 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.186× (z -12.0) |
| [[Hs 766T (line)]] | wt | 82.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -17.4) |
| [[HT-29 (line)]] | alt | 34.3 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.211× (z -13.1) |
| [[LS 180 (line)]] | wt | 59.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -17.4) |
| [[NCI-H2347 (line)]] | alt | 91.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.400× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 40.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.185× (z -11.9) |
| [[SW 900 (line)]] | alt | 73.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.312× (z -10.6) |
| [[A-427 (line)]] | wt | 19.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -10.7) |
| [[CHP-212 (line)]] | wt | 63.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0877× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0993× (z -11.6) |
| [[HS-578T (line)]] | alt | 32.2 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.208× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 26.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -11.6) |
| [[A549 (line)]] | wt | 16.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.170× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 35.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.268× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.279× (z -8.7) ⚠ cell-cycle shift, explains ~62% of this change |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0657× (z -12.7) |
| [[A498 (line)]] | wt | 3.34 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.95 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.43 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.92 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.71 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3424), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2D]] | +0.67 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[MCCC2]] | +0.66 | +0.39 / +0.66 | both halves | 5e-05 |  |
| [[DECR1]] | +0.65 | +0.48 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[HFE]] | +0.64 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[VPS52]] | +0.64 | +0.30 / +0.59 | both halves | 2e-04 |  |
| [[EXOSC10]] | +0.63 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[ADI1]] | +0.63 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[SH3BGRL]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[CIAO2A]] | +0.62 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[VBP1]] | +0.62 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[SNX5]] | +0.61 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[RAB11FIP2]] | +0.61 | +0.35 / +0.54 | both halves | 1e-04 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLIN3]] | -0.69 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[MIDN]] | -0.67 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[ARID3A]] | -0.64 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[CSNK1E]] | -0.64 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[FAM89B]] | -0.64 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[ZFYVE28]] | -0.64 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[SPATA2L]] | -0.63 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[SYP]] | -0.63 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[POLD4]] | -0.62 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[DUSP5]] | -0.61 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[CDKN2D]] | -0.61 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[SH3BGRL3]] | -0.61 | -0.40 / -0.49 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANGPTL4]] | B | ANGPTL4 activity lowers NNT's level | lines that do not express ANGPTL4 (13) vs lines expressing it (37) | 2.16× higher at baseline in the lines without ANGPTL4 | 0.021 | ⚠ within organs, on part of the lines; also absent: CLDN14-AS1, LGALS1, EBI3 |
| [[GPNMB]] | B | GPNMB activity raises NNT's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 1.71× lower at baseline in the lines without GPNMB | 0.039 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6 |
| [[PGAP4]] | B | PGAP4 activity raises NNT's level | lines that do not express PGAP4 (17) vs lines expressing it (33) | 1.65× lower at baseline in the lines without PGAP4 | 0.079 | ⚠ within organs, on part of the lines; also absent: CRACR2A, TMEM98, ARMCX4 |
| [[LRRC34]] | B | LRRC34 activity strengthens NNT's drug response | lines that do not express LRRC34 (17) vs lines expressing it (25) | the lines without LRRC34 respond 0.85× as strongly (z diff +1.15); strongest at Belinostat 5 µM: 0.34x vs 0.26x (z diff +2.1) | 0.081 | ⚠ within organs, on part of the lines; also absent: PLTP, SLC45A1, GNA15; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ZNF93]] | B | ZNF93 activity raises NNT's level | lines that do not express ZNF93 (21) vs lines expressing it (29) | 1.88× lower at baseline in the lines without ZNF93 | 0.088 | ⚠ within organs, on part of the lines; also absent: ZNF665, ZNF682, ZNF347 |
| [[FUCA2]] | C | FUCA2 activity raises NNT's level | lines that do not express FUCA2 (3) vs lines expressing it (47) | 5.07× lower at baseline in the lines without FUCA2 | 0.088 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPX1, AIFM2, SP100; maybe low, not absent; its own permutation p |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[N4BP3]] | B | NNT activity lowers N4BP3's level | lines that do not express NNT (6) vs lines expressing it (44) | 1.60× higher at baseline in the lines without NNT | 0.051 | ⚠ within organs, on part of the lines; co-absent genes |
| [[SRSF9]] | B | NNT activity lowers SRSF9's level | lines that do not express NNT (6) vs lines expressing it (44) | 1.17× higher at baseline in the lines without NNT | 0.058 | ⚠ within organs, on part of the lines; co-absent genes |
| cells under [[Topotecan (hydrochloride) (drug)]] 5 µM | B | NNT, [[NNT-AS1]] activity raises the cells' numbers under Topotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express NNT, NNT-AS1 (6) vs lines expressing them (42) | the lines without NNT, NNT-AS1: 0.65× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; co-absent genes |
| cells under [[Docetaxel (drug)]] 5 µM | B | NNT, [[NNT-AS1]] activity raises the cells' numbers under Docetaxel 5 µM (protects the cells) | lines that do not express NNT, NNT-AS1 (6) vs lines expressing them (42) | the lines without NNT, NNT-AS1: 0.85× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; co-absent genes |
| [[MRPL30]] | B | NNT activity lowers MRPL30's level | lines that do not express NNT (6) vs lines expressing it (44) | 1.27× higher at baseline in the lines without NNT | 0.081 | ⚠ within organs, on part of the lines; co-absent genes |
| [[KCTD20]] | B | NNT activity lowers KCTD20's level | lines that do not express NNT (6) vs lines expressing it (44) | 1.25× higher at baseline in the lines without NNT | 0.086 | ⚠ within organs, on part of the lines; co-absent genes |
| [[SH3BGRL]] | B | NNT activity raises SH3BGRL's level | lines that do not express NNT (6) vs lines expressing it (44) | 2.05× lower at baseline in the lines without NNT | 0.093 | ⚠ within organs, on part of the lines; co-absent genes |

## Where it sits

- **Module**: [[Module 192]]; 17 genes; every member is in the + arm (projection on the module's main direction -0.750). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.50; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.0, 1.7); signed map (21.4, -30.4). **Vector** length 98.4, 25.4% of its response variance represented; |z| ≥ 3 in 1,077 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.7 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.6 | +6.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +8.1 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.6 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.8 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +0.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +2.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.1 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -8.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.2 | -22.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.9 | -22.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.7 | -22.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.5 | -11.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.1 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -9.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -4.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | nicotinamide nucleotide transhydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p12 — chr5:43,602,692-43,707,405 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | HEME_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 2 pathways, smallest: Citric acid cycle (TCA cycle); Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13423](https://www.uniprot.org/uniprotkb/Q13423) (NAD(P) transhydrogenase, mitochondrial):

> The transhydrogenation between NADH and NADP is coupled to respiration and ATP hydrolysis and functions as a proton pump across the membrane (By similarity). May play a role in reactive oxygen species (ROS) detoxification in the adrenal gland.

**Summary**, from NCBI Gene [23530](https://www.ncbi.nlm.nih.gov/gene/23530):

> This gene encodes an integral protein of the inner mitochondrial membrane. The enzyme couples hydride transfer between NAD(H) and NADP(+) to proton translocation across the inner mitochondrial membrane. Under most physiological conditions, the enzyme uses energy from the mitochondrial proton gradient to produce high concentrations of NADPH. The resulting NADPH is used for biosynthesis and in free radical detoxification. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:7863](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7863) · Entrez [23530](https://www.ncbi.nlm.nih.gov/gene/23530) · UniProt [Q13423](https://www.uniprot.org/uniprotkb/Q13423) · Ensembl [ENSG00000112992](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112992)

## Data

Gene col 3424: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3424); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3424, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3424]; `tensor/DDL_lfc|DDL_z.npy` [3424]; `embed/gene_vectors.npy` [3424]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3424 or target_col == 3424). Every well: [[NNT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NNT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
