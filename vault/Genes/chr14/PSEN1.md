---
symbol: "PSEN1"
type: "gene"
col: 1290
ensembl_id: "ENSG00000080815"
name: "presenilin 1"
location: "14q24.2"
module: 145
arm: "+"
pooled_cpm: 146.62
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 17
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# PSEN1

*presenilin 1* — 14q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.30× (z +6.4, q 1e-07, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.508× (z -16.4, q 0e+00, down in 42 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.746× (z -7.1, q 1e-10, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYTH1]] (+0.59, fdr 1e-05), [[OTUD5]] (+0.57, fdr 1e-05), [[FBXO11]] (+0.57, fdr 1e-05); moves opposite to [[MAP4K5]] (-0.58, fdr 1e-05), [[UBA5]] (-0.57, fdr 1e-05), [[TRUB1]] (-0.52, fdr 2e-05).
> It is in [[Module 145]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PI3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1290.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +6.4 | 1e-07 | 30/48 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +5.1 | 1e-04 | 26/48 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +4.8 | 2e-04 | 23/48 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +4.5 | 8e-04 | 23/48 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.005 | 23/49 (BT-474, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.18× | +4.0 | 0.006 | 18/47 (A-172, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.8 | 0.013 | 0/50 | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.17× | +3.6 | 0.027 | 21/47 (hTERT-HPNE, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.041 | 20/48 (BT-474, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.3 | 0.053 | 18/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.32× | +3.1 | 0.10 | 16/48 (LS 180, RKO, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.14× | +3.1 | 0.10 | 9/48 (A-172, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1290.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.508×** | -16.4 | 0e+00 | 42/49 (RKO, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -13.7 | 3e-40 | 39/44 (AsPC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.630×** | -10.3 | 9e-23 | 36/45 (SW48, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.662×** | -10.0 | 2e-21 | 41/48 (NCI-H1792, SW1417, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~23% of this change | **0.736×** | -7.4 | 1e-11 | 37/48 (SW1417, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.746×** | -7.1 | 1e-10 | 35/48 (SNU-423, Panc 03.27, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.767×** | -6.4 | 1e-08 | 31/48 (HT-29, COLO 205, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.853× | -5.5 | 3e-06 | 21/48 (LoVo, COLO 205, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.812×** | -5.1 | 3e-05 | 28/48 (NCI-H1792, HepG2/C3A, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.638×** | -5.0 | 4e-05 | 34/48 (MIA PaCa-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.684×** | -4.2 | 0.001 | 23/48 (A498, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.684×** | -4.2 | 0.001 | 26/48 (CFPAC-1, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.862× | -3.6 | 0.014 | 21/48 (NCI-H1573, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.864× | -3.5 | 0.016 | 19/49 (LoVo, LS 180, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.865× | -3.5 | 0.016 | 15/48 (LoVo, A549, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.744×** | -3.3 | 0.034 | 18/48 (SHP-77, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.824×** | -3.0 | 0.066 | 12/49 (KATO III, NCI-H1792, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.763×** | -3.0 | 0.068 | 16/48 (A549, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.826×** | -3.0 | 0.068 | 18/48 (SW 900, COLO 205, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.827×** | -3.0 | 0.069 | 12/48 (NCI-H1792, A498, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.856× | -2.9 | 0.086 | 9/48 (LoVo, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | 0.900× | -2.9 | 0.086 | 5/49 (LoVo, NCI-H1573, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1290. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 205 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -13.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 234 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.344× (z -15.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 205 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.397× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 247 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.303× (z -15.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 121 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +11.0) | — |
| [[SW480 (line)]] | alt | 118 | 2 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.95× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.549× (z -9.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 132 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -12.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 120 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 219 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -13.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 220 | 0 | 3 (3 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0672× (z -17.6) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 97.2 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 130 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.453× (z -8.8) |
| [[SW48 (line)]] | wt | 183 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -17.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 158 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.489× (z -10.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 83.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 233 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -19.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 122 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -11.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 150 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.398× (z -10.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 140 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 123 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -11.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 146 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -17.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 131 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.466× (z -9.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 110 | 0 | 2 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.05 µM 0.0867× (z -10.4) |
| [[SW 900 (line)]] | alt | 141 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -15.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -13.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 203 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.439× (z -10.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 195 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.374× (z -8.8) ⚠ cell-cycle shift, explains ~18% of this change |
| [[HEC-1-A (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.540× (z -9.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.507× (z -9.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 80.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0567× (z -16.1) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -9.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 192 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -14.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.491× (z -9.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.375× (z -9.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 97.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.460× (z -9.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.476× (z -10.6) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 122 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 115 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 117 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 185 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 180 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1290), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYTH1]] | +0.59 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[OTUD5]] | +0.57 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[FBXO11]] | +0.57 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ARIH1]] | +0.56 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[MOB2]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[MYO1E]] | +0.55 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[MAPKAPK2]] | +0.54 | +0.61 / +0.49 | both halves | 1e-05 | pathway: Death Receptor Signaling |
| [[FAAP20]] | +0.52 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[INPP5K]] | +0.52 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[FBXW7]] | +0.52 | +0.54 / +0.44 | both halves | 3e-05 | pathway: Constitutive Signaling by NOTCH1 HD+PEST Domain Mutants; STRING 453 |
| [[CATSPERG]] | +0.52 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[CYTH2]] | +0.51 | +0.50 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP4K5]] | -0.58 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[UBA5]] | -0.57 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[TRUB1]] | -0.52 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[RAD23B]] | -0.52 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[LRRC58]] | -0.52 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[TTC8]] | -0.51 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[TRIT1]] | -0.50 | -0.33 / -0.63 | both halves | 1e-04 |  |
| [[AADAT]] | -0.49 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[DDX1]] | -0.49 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[TSEN15]] | -0.48 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[FIP1L1]] | -0.48 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[RFXAP]] | -0.47 | -0.39 / -0.55 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PI3]] | B | PI3 activity raises PSEN1's level | lines that do not express PI3 (27) vs lines expressing it (23) | 1.24× lower at baseline in the lines without PI3 | 0.068 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.493). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.2, -6.0); signed map (4.5, 18.9). **Vector** length 119, 37.3% of its response variance represented; |z| ≥ 3 in 1,066 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.9 | +2.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.6 | +3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +4.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.3 | +0.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -7.2 | -6.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.6 | -5.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.9 | -10.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.8 | -5.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.4 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -7.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -4.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | presenilin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.2 — chr14:73,136,418-73,223,691 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FAD, S182, PS1, PS-1, PSNL1; previously AD3 |
| Gene groups (HGNC) | Presenilin family; Gamma-secretase complex subunits |
| Hallmark sets | INFLAMMATORY_RESPONSE, APOPTOSIS, COMPLEMENT |
| Reactome | 36 pathways, smallest: Noncanonical activation of NOTCH3; NOTCH4 Activation and Transmission of Signal to the Nucleus; Regulated proteolysis of p75NTR |
| Matched by | ensembl_id |

**Function**, from UniProt [P49768](https://www.uniprot.org/uniprotkb/P49768) (Presenilin-1):

> Catalytic subunit of the gamma-secretase complex, an endoprotease complex that catalyzes the intramembrane cleavage of integral membrane proteins such as Notch receptors and APP (amyloid-beta precursor protein). Requires the presence of the other members of the gamma-secretase complex for protease activity. Plays a role in Notch and Wnt signaling cascades and regulation of downstream processes via its role in processing key regulatory proteins, and by regulating cytosolic CTNNB1 levels. …

**Summary**, from NCBI Gene [5663](https://www.ncbi.nlm.nih.gov/gene/5663):

> Alzheimer's disease (AD) patients with an inherited form of the disease carry mutations in the presenilin proteins (PSEN1; PSEN2) or in the amyloid precursor protein (APP). These disease-linked mutations result in increased production of the longer form of amyloid-beta (main component of amyloid deposits found in AD brains). Presenilins are postulated to regulate APP processing through their effects on gamma-secretase, an enzyme that cleaves APP. Also, it is thought that the presenilins are …

**Accessions** — [HGNC:9508](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9508) · Entrez [5663](https://www.ncbi.nlm.nih.gov/gene/5663) · UniProt [P49768](https://www.uniprot.org/uniprotkb/P49768) · Ensembl [ENSG00000080815](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080815)

## Data

Gene col 1290: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1290); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1290, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1290]; `tensor/DDL_lfc|DDL_z.npy` [1290]; `embed/gene_vectors.npy` [1290]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1290 or target_col == 1290). Every well: [[PSEN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSEN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
