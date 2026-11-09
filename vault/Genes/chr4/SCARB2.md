---
symbol: "SCARB2"
type: "gene"
col: 6229
ensembl_id: "ENSG00000138760"
name: "scavenger receptor class B member 2"
location: "4q21.1"
module: 29
arm: "+"
pooled_cpm: 149.78
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# SCARB2

*scavenger receptor class B member 2* — 4q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.87× (z +12.5, q 6e-33, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM: 1.21× (z +3.8, q 0.018, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.401× (z -25.8, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITM2B]] (+0.76, fdr 7e-06), [[TMEM123]] (+0.74, fdr 7e-06), [[LAMP2]] (+0.74, fdr 7e-06); moves opposite to [[ZNF593]] (-0.66, fdr 7e-06), [[PPP1R35]] (-0.66, fdr 7e-06, ⚠ PPP1R35 in the vector space only through flagged drug-doses), [[CROCCP2-1]] (-0.62, fdr 7e-06), [[EIF5B]] (-0.60, fdr 8e-06).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PLSCR4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6229.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +12.5 | 6e-33 | 47/49 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +10.8 | 9e-25 | 38/44 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +6.7 | 4e-09 | 32/45 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.21×** | +3.8 | 0.018 | 23/48 (Panc 03.27, A498, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.018 | 26/48 (AsPC-1, SW480, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.018 | 27/49 (AsPC-1, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.19× | +3.7 | 0.018 | 21/48 (AsPC-1, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.17× | +3.5 | 0.030 | 15/48 (AsPC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.040 | 3/48 (MIA PaCa-2, LOX-IMVI, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +3.4 | 0.040 | 20/47 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.083 | 21/48 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.088 | 16/49 (AsPC-1, LoVo, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.096 | 23/50 (SK-MEL-2, HEC-1-A, …) | top dose only | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.18× | +3.0 | 0.10 | 15/48 (AsPC-1, LoVo, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6229.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.401×** | -25.8 | 0e+00 | 47/48 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.504×** | -13.1 | 7e-37 | 46/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.543×** | -10.7 | 3e-24 | 43/48 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.708×** | -6.9 | 8e-10 | 38/48 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.733×** | -6.2 | 7e-08 | 38/48 (LoVo, SW1417, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.754×** | -5.6 | 1e-06 | 30/48 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.754×** | -5.6 | 1e-06 | 32/48 (SNU-1, A-427, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **0.753×** | -5.4 | 4e-06 | 30/47 (SHP-77, SNU-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.768×** | -5.3 | 8e-06 | 33/48 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.786×** | -4.6 | 2e-04 | 26/49 (HepG2/C3A, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.801×** | -4.4 | 5e-04 | 24/48 (A-427, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.803×** | -4.4 | 5e-04 | 27/48 (MIA PaCa-2, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~3% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.857× | -4.4 | 5e-04 | 20/49 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.730×** | -4.1 | 0.002 | 34/48 (SW 900, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.816×** | -4.1 | 0.002 | 25/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.834× | -3.6 | 0.009 | 24/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6229. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 122 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +15.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -21.2) |
| [[PANC-1 (line)]] | alt | 99.2 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -25.3) |
| [[A498 (line)]] | wt | 242 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -23.3) |
| [[J82 (line)]] | alt | 120 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -22.8) |
| [[A549 (line)]] | wt | 120 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -20.9) |
| [[C32 (line)]] | wt | 246 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 142 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +15.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -13.7) |
| [[HOP62 (line)]] | alt | 130 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -17.6) |
| [[HS-578T (line)]] | alt | 208 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -23.9) |
| [[NCI-H1792 (line)]] | alt | 145 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -18.0) |
| [[NCI-H460 (line)]] | wt | 123 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -15.9) |
| [[SHP-77 (line)]] | alt | 175 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.04× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -16.0) |
| [[SK-MEL-2 (line)]] | alt | 200 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -9.0) |
| [[SNU-1 (line)]] | wt | 167 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -17.0) |
| [[SW 900 (line)]] | alt | 162 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -25.0) |
| [[A-172 (line)]] | wt | 193 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -18.3) |
| [[H4 (line)]] | wt | 150 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -16.7) |
| [[KATO III (line)]] | alt | 150 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 81.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -16.5) |
| [[MIA PaCa-2 (line)]] | alt | 110 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -13.4) |
| [[RPMI-7951 (line)]] | alt | 225 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -21.2) |
| [[SW480 (line)]] | alt | 69.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.32× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.624× (z -9.0) |
| [[A-427 (line)]] | wt | 109 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -16.0) |
| [[AN3 CA (line)]] | alt | 192 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.272× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 94.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -15.6) |
| [[C-33 A (line)]] | alt | 162 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -16.0) |
| [[COLO 205 (line)]] | alt | 183 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -16.9) |
| [[HepG2_C3A (line)]] | wt | 164 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -20.5) |
| [[NCI-H2030 (line)]] | alt | 122 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 198 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -24.0) |
| [[Panc 03.27 (line)]] | alt | 122 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -15.5) |
| [[RKO (line)]] | wt | 136 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -26.0) |
| [[SNU-423 (line)]] | alt | 109 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -19.7) |
| [[BT-474 (line)]] | alt | 270 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -15.1) |
| [[CFPAC-1 (line)]] | alt | 179 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -15.3) |
| [[HCT15 (line)]] | alt | 175 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.24× (z +8.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 113 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -14.1) |
| [[HT-29 (line)]] | alt | 218 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -13.9) |
| [[hTERT-HPNE (line)]] | wt | 201 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -12.6) |
| [[LoVo (line)]] | wt | 152 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.526× (z -9.1) ⚠ cell-cycle shift, explains ~24% of this change |
| [[LS 180 (line)]] | wt | 224 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.655× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 116 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -18.1) |
| [[SW 1088 (line)]] | alt | 328 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -10.3) |
| [[CHP-212 (line)]] | wt | 188 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 209 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6229), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITM2B]] | +0.76 | +0.72 / +0.79 | both halves | 7e-06 |  |
| [[TMEM123]] | +0.74 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[LAMP2]] | +0.74 | +0.65 / +0.79 | both halves | 7e-06 | STRING 654 |
| [[GNS]] | +0.73 | +0.63 / +0.77 | both halves | 7e-06 | STRING 503 |
| [[TMEM30A]] | +0.72 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[LIPA]] | +0.71 | +0.59 / +0.73 | both halves | 7e-06 | STRING 522 |
| [[SH3BGRL]] | +0.71 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[DDOST]] | +0.69 | +0.65 / +0.67 | both halves | 7e-06 | STRING 664 |
| [[ERMP1]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[TSPAN6]] | +0.68 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[ATRAID]] | +0.68 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[PGAM1]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF593]] | -0.66 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[PPP1R35]] ⚠ | -0.66 | -0.60 / -0.64 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CROCCP2-1]] | -0.62 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[EIF5B]] | -0.60 | -0.58 / -0.59 | both halves | 8e-06 |  |
| [[UBE2J2]] | -0.58 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[NT5C]] | -0.58 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[FBXL6]] | -0.58 | -0.44 / -0.64 | both halves | 3e-05 |  |
| [[ZNF316]] | -0.57 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[UBE2CP5]] | -0.57 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[RGP1]] | -0.57 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[MTRES1]] | -0.56 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[NSUN5P2-1]] ⚠ | -0.56 | -0.47 / -0.57 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SURF6]] | -0.56 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[LIME1]] | -0.56 | -0.48 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLSCR4]] | B | PLSCR4 activity raises SCARB2's level | lines that do not express PLSCR4 (11) vs lines expressing it (39) | 1.20× lower at baseline in the lines without PLSCR4 | 0.063 | ⚠ within organs, on part of the lines; also absent: IRF7, KLF12, GSDMD |
| [[MAP2K2]] | B | MAP2K2 activity lowers SCARB2's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.838). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.0, -20.5); signed map (-22.2, -39.2). **Vector** length 136, 45.3% of its response variance represented; |z| ≥ 3 in 1,089 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | +2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +6.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.6 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +10.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.2 | +3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +5.1 | +3.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.9 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.6 | +3.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.5 | -13.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.7 | -4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -25.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | -5.1 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -10.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.3 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -3.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.9 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.8 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | scavenger receptor class B member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.1 — chr4:76,158,737-76,234,536 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HLGP85, LIMPII, SR-BII, LIMP-2; previously CD36L2 |
| Gene groups (HGNC) | Scavenger receptors |
| Reactome | 4 pathways, smallest: Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14108](https://www.uniprot.org/uniprotkb/Q14108) (Lysosome membrane protein 2):

> Acts as a lysosomal receptor for glucosylceramidase (GBA1) targeting.; (Microbial infection) Acts as a receptor for enterovirus 71.

**Summary**, from NCBI Gene [950](https://www.ncbi.nlm.nih.gov/gene/950):

> The protein encoded by this gene is a type III glycoprotein that is located primarily in limiting membranes of lysosomes and endosomes. Earlier studies in mice and rat suggested that this protein may participate in membrane transportation and the reorganization of endosomal/lysosomal compartment. The protein deficiency in mice was reported to impair cell membrane transport processes and cause pelvic junction obstruction, deafness, and peripheral neuropathy. Further studies in human showed that …

**Accessions** — [HGNC:1665](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1665) · Entrez [950](https://www.ncbi.nlm.nih.gov/gene/950) · UniProt [Q14108](https://www.uniprot.org/uniprotkb/Q14108) · Ensembl [ENSG00000138760](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138760)

## Data

Gene col 6229: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6229); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6229, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6229]; `tensor/DDL_lfc|DDL_z.npy` [6229]; `embed/gene_vectors.npy` [6229]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6229 or target_col == 6229). Every well: [[SCARB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCARB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
