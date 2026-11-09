---
symbol: "USP3"
type: "gene"
col: 6411
ensembl_id: "ENSG00000140455"
name: "ubiquitin specific peptidase 3"
location: "15q22.31"
module: 204
arm: "+"
pooled_cpm: 221.7
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 24
n_dd_up_clean: 11
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/204"]
generated_by: "tahoemap"
---

# USP3

*ubiquitin specific peptidase 3* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.83× (z +6.8, q 5e-09, up in 40 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.71× (z +6.1, q 3e-07, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.352× (z -11.4, q 2e-27, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.465× (z -8.7, q 5e-16, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPOPL]] (+0.67, fdr 8e-06), [[SEC61A2]] (+0.67, fdr 7e-06), [[RYK]] (+0.67, fdr 7e-06); moves opposite to [[TAF2]] (-0.73, fdr 7e-06), [[REXO1]] (-0.68, fdr 9e-06), [[ZNF776]] (-0.66, fdr 1e-05).
> It is in [[Module 204]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6411.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +6.8 | 5e-09 | 40/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.71×** | +6.1 | 3e-07 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.33×** | +5.0 | 1e-04 | 39/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.54×** | +4.9 | 1e-04 | 33/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.50×** | +4.4 | 0.001 | 37/49 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.2 | 0.002 | 31/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.019 | 29/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.85×** | +3.6 | 0.019 | 37/48 (AsPC-1, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.027 | 27/48 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.029 | 28/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fumaric acid (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.031 | 26/49 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift |
| [[Diphenhydramine (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.045 | 26/48 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.055 | 26/49 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.30× | +3.0 | 0.11 | 27/48 (HEC-1-A, LS 180, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6411.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.352×** | -11.4 | 2e-27 | 42/44 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.408×** | -10.2 | 6e-22 | 48/49 (NCI-H2347, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.465×** | -8.7 | 5e-16 | 45/48 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.495×** | -8.0 | 2e-13 | 46/48 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.515×** | -7.3 | 4e-11 | 45/47 (RKO, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.625×** | -5.4 | 8e-06 | 44/48 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.669×** | -4.6 | 4e-04 | 40/48 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.654×** | -4.5 | 6e-04 | 30/45 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.692×** | -4.2 | 0.002 | 29/48 (SW480, HepG2/C3A, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.719×** | -3.8 | 0.009 | 36/48 (KATO III, NCI-H460, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.720×** | -3.8 | 0.009 | 35/48 (A-172, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.803×** | -3.5 | 0.019 | 24/48 (CHP-212, NCI-H2347, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.736×** | -3.5 | 0.021 | 31/48 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.739×** | -3.4 | 0.022 | 35/49 (NCI-H2347, CHP-212, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.740×** | -3.4 | 0.022 | 28/48 (HT-29, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.743×** | -3.4 | 0.024 | 30/48 (RPMI-7951, HEC-1-A, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.744×** | -3.4 | 0.024 | 29/48 (RPMI-7951, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.812×** | -3.4 | 0.024 | 28/48 (HCT15, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Busulfan (drug)]] 0.05 µM |  | **0.756×** | -3.2 | 0.043 | 28/49 (C32, A-172, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.760×** | -3.1 | 0.050 | 30/47 (J82, NCI-H1792, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.763×** | -3.1 | 0.054 | 29/48 (NCI-H460, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6411. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 186 | 6 (2 ⚠) | 5 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 3.34× (z +16.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +15.6) | [[Panobinostat (drug)]] 5 µM 0.350× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 208 | 6 (2 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 3.47× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.374× (z -9.5) |
| [[HT-29 (line)]] | alt | 335 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.375× (z -10.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.399× (z -10.0) |
| [[KATO III (line)]] | alt | 164 | 3 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.20× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.466× (z -8.5) |
| [[PANC-1 (line)]] | alt | 191 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.98× (z +14.4) | — |
| [[HOP62 (line)]] | alt | 288 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.242× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 224 | 3 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.34× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 275 | 1 (1 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.34× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 334 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -14.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 438 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 245 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -11.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 222 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.332× (z -9.5) |
| [[LoVo (line)]] | wt | 338 | 1 (1 ⚠) | 2 | [[Niclosamide (olamine) (drug)]] 5 µM 2.94× (z +11.6) ⚠ toxic | [[Panobinostat (drug)]] 0.5 µM 0.360× (z -11.4) |
| [[LS 180 (line)]] | wt | 246 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -9.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 335 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.217× (z -14.2) ⚠ toxic |
| [[SW1417 (line)]] | alt | 318 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -10.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 205 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.367× (z -8.5) |
| [[COLO 205 (line)]] | alt | 219 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.03× (z +9.6) ⚠ toxic | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -11.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 213 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -9.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 222 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.268× (z -9.2) |
| [[SHP-77 (line)]] | alt | 173 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -14.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 269 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -11.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -8.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 178 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -10.2) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 217 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 333 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 79.0 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.67× (z +9.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 183 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -13.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 191 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 225 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -9.4) |
| [[A-172 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 80.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 198 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 288 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 234 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 154 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 149 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 232 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 215 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 316 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 296 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 182 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 291 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6411), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPOPL]] | +0.67 | +0.74 / +0.58 | both halves | 8e-06 |  |
| [[SEC61A2]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[RYK]] | +0.67 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[PDK1]] | +0.66 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[LRP5L]] | +0.66 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[KDM1A]] | +0.65 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[TRIM33]] | +0.65 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[PPP1R2]] | +0.65 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[SRP54-AS1]] | +0.65 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[SNRPA1]] | +0.65 | +0.76 / +0.52 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.65 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[FOXJ3]] | +0.65 | +0.76 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF2]] | -0.73 | -0.79 / -0.59 | both halves | 7e-06 |  |
| [[REXO1]] | -0.68 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[ZNF776]] | -0.66 | -0.72 / -0.49 | both halves | 1e-05 |  |
| [[ZNF140]] | -0.66 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[ANKLE2]] | -0.65 | -0.68 / -0.52 | both halves | 1e-05 |  |
| [[ZNF268]] | -0.65 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[SRCAP]] | -0.64 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[EPC2]] | -0.63 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[CDK11A]] | -0.63 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[SP2]] | -0.62 | -0.73 / -0.47 | both halves | 2e-05 |  |
| [[MIS12]] | -0.62 | -0.70 / -0.47 | both halves | 2e-05 |  |
| [[ZNF274]] | -0.62 | -0.58 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 204]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.842). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.54; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.2, -8.7); signed map (-34.6, -10.6). **Vector** length 104, 45.7% of its response variance represented; |z| ≥ 3 in 1,337 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +6.7 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.3 | +1.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.4 | +4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.1 | -2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +4.0 | +2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | -0.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | -1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.6 | +4.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | +2.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | +5.0 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.5 | -1.5 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -2.3 | -3.1 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -2.3 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:63,504,511-63,594,640 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Reactome | 2 pathways, smallest: Ub-specific processing proteases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6I4](https://www.uniprot.org/uniprotkb/Q9Y6I4) (Ubiquitin carboxyl-terminal hydrolase 3):

> Deubiquitinase that plays a role in several cellular processes including transcriptional regulation, cell cycle progression or innate immunity. In response to DNA damage, deubiquitinates monoubiquitinated target proteins such as histone H2A and H2AX and thereby counteracts RNF168- and RNF8-mediated ubiquitination. In turn, participates in the recruitment of DNA damage repair factors to DNA break sites. Required for proper progression through S phase and subsequent mitotic entry. Acts as a …

**Summary**, from NCBI Gene [9960](https://www.ncbi.nlm.nih.gov/gene/9960):

> Enables deubiquitinase activity and histone binding activity. Involved in DNA repair and DNA repair-dependent chromatin remodeling. Located in chromatin and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:12626](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12626) · Entrez [9960](https://www.ncbi.nlm.nih.gov/gene/9960) · UniProt [Q9Y6I4](https://www.uniprot.org/uniprotkb/Q9Y6I4) · Ensembl [ENSG00000140455](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140455)

## Data

Gene col 6411: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6411); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6411, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6411]; `tensor/DDL_lfc|DDL_z.npy` [6411]; `embed/gene_vectors.npy` [6411]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6411 or target_col == 6411). Every well: [[USP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
