---
symbol: "ZNF37BP"
type: "gene"
col: 13956
ensembl_id: "ENSG00000234420"
name: "zinc finger protein 37B, pseudogene"
location: "10q11.21"
module: 4
arm: "+"
pooled_cpm: 37.04
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 22
n_dd_up_clean: 14
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# ZNF37BP

*zinc finger protein 37B, pseudogene* — 10q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.71× (z +7.6, q 2e-11, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.418× (z -12.5, q 3e-33, down in 43 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.419× (z -12.5, q 3e-33, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRE11]] (+0.57, fdr 1e-04), [[TMTC4]] (+0.56, fdr 5e-05), [[NAE1]] (+0.55, fdr 3e-05); moves opposite to [[FKBP15]] (-0.55, fdr 3e-05), [[HMGCL]] (-0.55, fdr 3e-05), [[COX7B]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13956.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +7.6 | 2e-11 | 40/48 (HT-29, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +7.3 | 1e-10 | 28/42 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.61×** | +6.8 | 1e-09 | 29/48 (AsPC-1, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +6.4 | 2e-08 | 32/48 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +6.4 | 2e-08 | 33/47 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +6.1 | 8e-08 | 31/48 (AsPC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +6.1 | 8e-08 | 32/47 (SW480, H4, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.7 | 7e-07 | 27/48 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +5.6 | 1e-06 | 34/47 (LoVo, HOP62, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +5.4 | 4e-06 | 33/47 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.39×** | +4.7 | 2e-04 | 29/47 (LOX-IMVI, A549, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.82×** | +4.5 | 3e-04 | 27/48 (PANC-1, BT-474, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.23×** | +4.2 | 0.001 | 24/48 (SNU-423, LoVo, …) | top dose only | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.70×** | +4.0 | 0.002 | 20/48 (HT-29, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.64×** | +3.7 | 0.008 | 21/48 (PANC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +3.2 | 0.048 | 11/48 (AN3 CA, RPMI-7951, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.062 | 11/48 (A549, NCI-H460, …) | all doses, flat |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.085 | 11/48 (SW480, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13956.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.418×** | -12.5 | 3e-33 | 43/47 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.419×** | -12.5 | 3e-33 | 44/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.653×** | -8.6 | 1e-15 | 34/48 (NCI-H23, RKO, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.558×** | -8.3 | 1e-14 | 34/47 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.568×** | -8.1 | 6e-14 | 36/48 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.593×** | -7.5 | 7e-12 | 38/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.623×** | -6.5 | 6e-09 | 32/48 (SNU-1, RKO, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.614×** | -5.0 | 4e-05 | 25/48 (NCI-H460, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.702×** | -5.0 | 4e-05 | 23/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.522×** | -4.9 | 6e-05 | 29/48 (HEC-1-A, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.736×** | -4.4 | 6e-04 | 25/48 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.745×** | -4.2 | 0.001 | 20/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.584×** | -4.0 | 0.002 | 19/47 (HEC-1-A, SW 1271, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.589×** | -4.0 | 0.003 | 22/47 (SW 1271, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.760×** | -3.9 | 0.003 | 25/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.599×** | -3.8 | 0.004 | 23/47 (NCI-H1792, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.614×** | -3.7 | 0.008 | 20/47 (HEC-1-A, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.764×** | -3.6 | 0.009 | 18/48 (MIA PaCa-2, LoVo, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.704×** | -3.6 | 0.010 | 20/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.713×** | -3.4 | 0.015 | 18/48 (PANC-1, HEC-1-A, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13956. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 36.6 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -11.6) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.274× (z -11.4) |
| [[SNU-1 (line)]] | wt | 84.7 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.236× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.266× (z -10.4) |
| [[RKO (line)]] | wt | 109 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.228× (z -13.2) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.380× (z -8.7) |
| [[PANC-1 (line)]] | alt | 43.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -11.8) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.318× (z -11.3) |
| [[SW480 (line)]] | alt | 62.7 | 1 | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.270× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -11.8) |
| [[LoVo (line)]] | wt | 30.9 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.227× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 49.7 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.228× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.368× (z -8.5) |
| [[SNU-423 (line)]] | alt | 49.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -9.6) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.271× (z -9.2) |
| [[A-427 (line)]] | wt | 47.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -14.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 31.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -10.2) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 46.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.30× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -10.2) ⚠ cell-cycle shift, explains ~60% of this change |
| [[Hs 766T (line)]] | wt | 28.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.209× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 23.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.159× (z -13.7) |
| [[MIA PaCa-2 (line)]] | alt | 58.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -11.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[NCI-H1792 (line)]] | alt | 30.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.234× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -9.9) |
| [[A-172 (line)]] | wt | 52.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.61× (z +8.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 52.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.151× (z -8.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[BT-474 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.130× (z -11.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 70.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.9) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[HepG2_C3A (line)]] | wt | 32.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.161× (z -10.2) |
| [[HT-29 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.249× (z -9.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 48.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.369× (z -9.5) |
| [[LS 180 (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -8.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -8.6) ⚠ cell-cycle shift, explains ~60% of this change |
| [[SW 900 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -9.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13956), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRE11]] | +0.57 | +0.35 / +0.61 | both halves | 1e-04 |  |
| [[TMTC4]] | +0.56 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[NAE1]] | +0.55 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[PEX26]] | +0.55 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[CLNS1A]] | +0.55 | +0.34 / +0.63 | both halves | 1e-04 |  |
| [[HACD3]] | +0.54 | +0.49 / +0.51 | both halves | 2e-05 |  |
| [[CDC123]] | +0.53 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[NUDT3]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[PCMTD2]] | +0.53 | +0.33 / +0.59 | both halves | 1e-04 |  |
| [[SETD6]] | +0.53 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[IGF1R]] | +0.52 | +0.37 / +0.47 | both halves | 7e-05 |  |
| [[NAA50]] | +0.52 | +0.52 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP15]] | -0.55 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[HMGCL]] | -0.55 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[COX7B]] | -0.50 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[FUT11]] | -0.50 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[TMEM106A]] | -0.50 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[KRT10]] ⚠ | -0.49 | -0.45 / -0.37 | both halves | 9e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COPE]] | -0.49 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[NBPF19]] | -0.48 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[CA9]] | -0.48 | -0.37 / -0.60 | both halves | 8e-05 |  |
| [[SEC22A]] | -0.48 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[INAFM1]] | -0.48 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[SEC23B]] | -0.47 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[TRIM5]] | -0.47 | -0.37 / -0.50 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.486). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-25.6, -29.6); signed map (-22.0, -48.6). **Vector** length 77.9, 18.1% of its response variance represented; |z| ≥ 3 in 1,113 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +3.9 | -0.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.9 | -3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.5 | +5.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.4 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | -1.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.1 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -6.8 | -8.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.8 | -3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.6 | -4.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.2 | -3.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.2 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 37B, pseudogene |
| Locus type | pseudogene |
| Location | 10q11.21 — chr10:42,519,695-42,521,046 (-) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Also known as | KOX21, FLJ23327; previously ZNF37B |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:13103](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13103) · Entrez [100129482](https://www.ncbi.nlm.nih.gov/gene/100129482) · Ensembl [ENSG00000234420](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234420)

## Data

Gene col 13956: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13956); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13956, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13956]; `tensor/DDL_lfc|DDL_z.npy` [13956]; `embed/gene_vectors.npy` [13956]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13956 or target_col == 13956). Every well: [[ZNF37BP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF37BP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
