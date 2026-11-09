---
symbol: "BTN2A1"
type: "gene"
col: 3403
ensembl_id: "ENSG00000112763"
name: "butyrophilin subfamily 2 member A1"
location: "6p22.2"
module: 94
arm: "+"
pooled_cpm: 41.9
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 11
n_dd_up_clean: 13
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# BTN2A1

*butyrophilin subfamily 2 member A1* — 6p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.74× (z +11.7, q 7e-29, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.477× (z -15.5, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C3orf38]] (+0.80, fdr 7e-06), [[ZNF563]] (+0.77, fdr 7e-06), [[ZNF226]] (+0.73, fdr 7e-06); moves opposite to [[RSU1]] (-0.70, fdr 1e-05), [[GNB1L]] (-0.65, fdr 1e-05), [[CORO1C]] (-0.65, fdr 1e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PCAT7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3403.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +11.7 | 7e-29 | 42/47 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +10.8 | 1e-24 | 31/47 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.64×** | +10.0 | 4e-21 | 38/47 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +9.8 | 1e-20 | 38/47 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +9.8 | 1e-20 | 29/47 (J82, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +7.8 | 9e-13 | 34/47 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +7.2 | 5e-11 | 32/47 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +7.0 | 2e-10 | 30/46 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.82×** | +6.6 | 3e-09 | 28/48 (HS-578T, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.36×** | +6.5 | 4e-09 | 30/47 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.37×** | +6.2 | 3e-08 | 27/46 (HS-578T, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +6.1 | 6e-08 | 23/47 (A498, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +4.9 | 4e-05 | 23/47 (NCI-H2030, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.47×** | +4.2 | 9e-04 | 19/47 (AsPC-1, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.21×** | +4.1 | 0.002 | 18/47 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3403.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.477×** | -15.5 | 0e+00 | 46/47 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.479×** | -15.5 | 0e+00 | 44/47 (CFPAC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.507×** | -14.3 | 8e-44 | 46/47 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.575×** | -11.6 | 6e-29 | 35/46 (A-427, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.654×** | -8.6 | 1e-15 | 27/35 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.669×** | -8.4 | 3e-15 | 39/47 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.702×** | -6.9 | 5e-10 | 22/42 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.755×** | -5.9 | 3e-07 | 28/47 (AsPC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.626×** | -5.1 | 2e-05 | 28/47 (SNU-423, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.819×** | -4.2 | 0.002 | 18/47 (NCI-H2347, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.876× | -3.9 | 0.006 | 10/47 (LOX-IMVI, A-172, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.834× | -3.8 | 0.007 | 16/47 (NCI-H23, CFPAC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.839× | -3.7 | 0.011 | 16/47 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.719×** | -3.6 | 0.012 | 17/47 (A498, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 0.885× | -3.6 | 0.014 | 12/47 (A498, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3403. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 41.9 | 4 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.42× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.340× (z -13.0) |
| [[A-172 (line)]] | wt | 50.5 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.59× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.0600× (z -29.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.369× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 77.0 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.358× (z -10.6) |
| [[SNU-423 (line)]] | alt | 83.9 | 0 | 6 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.390× (z -10.7) |
| [[A498 (line)]] | wt | 37.4 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +12.1) | — |
| [[A549 (line)]] | wt | 54.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.349× (z -9.7) |
| [[J82 (line)]] | alt | 70.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +16.4) | — |
| [[A-427 (line)]] | wt | 26.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -14.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 58.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -9.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 49.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.324× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 48.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -12.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 56.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -11.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 40.8 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.456× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.480× (z -8.9) |
| [[SW480 (line)]] | alt | 33.3 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.59× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.451× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 38.9 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.318× (z -10.4) |
| [[CHP-212 (line)]] | wt | 43.0 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.110× (z -10.2) ⚠ transcription drop; cell-cycle shift, explains ~22% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.128× (z -9.5) |
| [[COLO 205 (line)]] | alt | 56.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.304× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 27.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.3) | — |
| [[HOP62 (line)]] | alt | 46.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +11.6) | — |
| [[HT-29 (line)]] | alt | 28.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.278× (z -10.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 33.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -10.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 46.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -12.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 37.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -9.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -9.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 39.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.227× (z -9.7) |
| [[Hs 766T (line)]] | wt | 46.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.355× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 39.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 29.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.434× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 70.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.369× (z -8.5) |
| [[AN3 CA (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.43 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3403), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C3orf38]] | +0.80 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[ZNF563]] | +0.77 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[ZNF226]] | +0.73 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[WHAMM]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[MR1]] | +0.71 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[MED18]] | +0.70 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[PPCS]] | +0.70 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ZNF442]] | +0.70 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[N4BP2L1]] | +0.69 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ZNF44]] | +0.69 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[ZNF585A]] | +0.69 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[STAP2]] | +0.69 | +0.54 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSU1]] | -0.70 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[GNB1L]] | -0.65 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[CORO1C]] | -0.65 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[SMYD3]] | -0.65 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[TCF3]] | -0.63 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[TBCD]] | -0.62 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[ST6GALNAC4]] | -0.61 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[APMAP]] | -0.61 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[IPO7]] | -0.61 | -0.55 / -0.68 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCAT7]] | B | PCAT7 activity lowers BTN2A1's level | lines that do not express PCAT7 (12) vs lines expressing it (38) | 1.32× higher at baseline in the lines without PCAT7 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000286850, CRACD, NFIA; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises BTN2A1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.709). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.0, 23.4); signed map (16.6, -16.3). **Vector** length 115, 30.8% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.8 | +9.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +8.1 | +6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.1 | +7.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.9 | +11.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.8 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.7 | +6.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.0 | +2.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.8 | -14.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.4 | -15.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.8 | -8.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.7 | -15.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.7 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -5.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.8 | -4.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.6 | -3.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.3 | -3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | butyrophilin subfamily 2 member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.2 — chr6:26,457,904-26,476,621 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BT2.1, BTF1, BTN2.1 |
| Gene groups (HGNC) | Butyrophilins; V-set domain containing; C2-set domain containing |
| Reactome | 2 pathways, smallest: Butyrophilin (BTN) family interactions; Adaptive Immune System |
| Matched by | ensembl_id |

UniProt [Q7KYR7](https://www.uniprot.org/uniprotkb/Q7KYR7) carries no function annotation.

**Summary**, from NCBI Gene [11120](https://www.ncbi.nlm.nih.gov/gene/11120):

> This gene encodes a member of the immunoglobulin superfamily. The gene is located in a cluster of butyrophilin-like genes in the juxta-telomeric region of the major histocompatibility complex on chromosome 6. A pseudogene of this gene has been identified in this cluster. The encoded protein is an integral plasma membrane protein involved in lipid, fatty-acid, and sterol metabolism. Alterations in this gene may be associated with several disease states including metabolic syndrome. Multiple …

**Accessions** — [HGNC:1136](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1136) · Entrez [11120](https://www.ncbi.nlm.nih.gov/gene/11120) · UniProt [Q7KYR7](https://www.uniprot.org/uniprotkb/Q7KYR7) · Ensembl [ENSG00000112763](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112763)

## Data

Gene col 3403: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3403); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3403, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3403]; `tensor/DDL_lfc|DDL_z.npy` [3403]; `embed/gene_vectors.npy` [3403]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3403 or target_col == 3403). Every well: [[BTN2A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTN2A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
