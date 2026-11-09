---
symbol: "RFX2"
type: "gene"
col: 1515
ensembl_id: "ENSG00000087903"
name: "regulatory factor X2"
location: "19p13.3"
module: 79
arm: "+"
pooled_cpm: 69.87
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 17
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# RFX2

*regulatory factor X2* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.53× (z +12.4, q 1e-32, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.428× (z -11.4, q 2e-27, down in 36 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.534× (z -8.4, q 5e-15, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFHC1]] (+0.75, fdr 7e-06), [[HILPDA]] (+0.73, fdr 7e-06), [[PDK3]] (+0.73, fdr 7e-06); moves opposite to [[MAPKAPK5]] (-0.66, fdr 1e-05), [[DNAJC11]] (-0.65, fdr 1e-05), [[ZSCAN29]] (-0.64, fdr 3e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1515.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.53×** | +12.4 | 1e-32 | 44/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.40×** | +11.7 | 5e-29 | 41/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.05×** | +9.6 | 2e-19 | 41/47 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.01×** | +9.3 | 1e-18 | 39/47 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.70×** | +7.1 | 2e-10 | 38/47 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +6.3 | 3e-08 | 32/47 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +5.4 | 4e-06 | 30/47 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +5.2 | 1e-05 | 27/47 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.41×** | +4.6 | 3e-04 | 27/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.93×** | +4.6 | 3e-04 | 31/48 (PANC-1, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +3.9 | 0.005 | 25/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[palbociclib (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.068 | 15/47 (Hs 766T, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1515.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.428×** | -11.4 | 2e-27 | 36/48 (A-427, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.415×** | -11.3 | 2e-27 | 34/41 (AN3 CA, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.434×** | -10.4 | 7e-23 | 33/43 (CFPAC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.534×** | -8.4 | 5e-15 | 35/47 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.683×** | -4.8 | 2e-04 | 29/47 (CFPAC-1, Hs 766T, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.786×** | -4.6 | 4e-04 | 24/47 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.720×** | -4.3 | 0.002 | 26/47 (C-33 A, NCI-H2030, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.809×** | -4.0 | 0.004 | 21/47 (SNU-423, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.729×** | -3.9 | 0.005 | 24/47 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.627×** | -3.9 | 0.005 | 22/47 (Hs 766T, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.816×** | -3.9 | 0.005 | 21/47 (CFPAC-1, LOX-IMVI, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.746×** | -3.8 | 0.007 | 21/46 (SNU-423, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.763×** | -3.4 | 0.029 | 21/47 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.838× | -3.4 | 0.030 | 19/47 (Hs 766T, KATO III, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.786×** | -3.2 | 0.044 | 18/47 (NCI-H2347, SNU-423, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.781×** | -3.1 | 0.060 | 22/48 (HT-29, Hs 766T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1515. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 52.5 | 9 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.26× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -9.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 135 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -18.7) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -18.3) |
| [[LOX-IMVI (line)]] | wt | 56.2 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.92× (z +9.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.349× (z -9.7) |
| [[SNU-423 (line)]] | alt | 103 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -13.9) |
| [[MIA PaCa-2 (line)]] | alt | 105 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.240× (z -13.1) |
| [[A-427 (line)]] | wt | 61.4 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.94× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0835× (z -25.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 31.4 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 5.71× (z +15.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.328× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 62.0 | 2 | 3 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.44× (z +8.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -17.7) |
| [[Hs 766T (line)]] | wt | 166 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -12.2) |
| [[HS-578T (line)]] | alt | 120 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.94× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -9.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 94.8 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -12.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 24.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 9.06× (z +13.0) | — |
| [[NCI-H1792 (line)]] | alt | 120 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0362× (z -24.6) |
| [[NCI-H2030 (line)]] | alt | 48.2 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.44× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 36.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.83× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -10.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 27.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.76× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.170× (z -11.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 29.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.60× (z +11.8) | — |
| [[SW480 (line)]] | alt | 53.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.39× (z +13.0) | — |
| [[A-172 (line)]] | wt | 156 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -11.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 50.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.76× (z +9.9) | — |
| [[C-33 A (line)]] | alt | 149 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -16.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 29.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.52× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 63.1 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.56× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -16.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 38.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.81× (z +10.8) | — |
| [[RKO (line)]] | wt | 50.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.31× (z +11.7) | — |
| [[SHP-77 (line)]] | alt | 93.5 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.74× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -13.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 41.7 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.11× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -8.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 199 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0505× (z -19.2) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 142 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0613× (z -14.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 86.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -9.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 77.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -10.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 37.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.20× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -9.5) |
| [[A549 (line)]] | wt | 64.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -9.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 85.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -11.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 24.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.39× (z +9.0) | — |
| [[KATO III (line)]] | alt | 85.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -8.9) ⚠ cell-cycle shift, explains ~21% of this change |
| [[RPMI-7951 (line)]] | alt | 77.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -11.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 33.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.73× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -10.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 40.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.10× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 79.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1515), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFHC1]] | +0.75 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[HILPDA]] | +0.73 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[PDK3]] | +0.73 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[MLF1]] | +0.71 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[RNF24]] | +0.68 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[CDON]] | +0.66 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ABCB9]] | +0.66 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[PFKFB4]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.65 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[ANKRD37]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[NXPH4]] | +0.64 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.64 | +0.57 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK5]] | -0.66 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[DNAJC11]] | -0.65 | -0.67 / -0.49 | both halves | 1e-05 | pathway: Organelle biogenesis and maintenance |
| [[ZSCAN29]] | -0.64 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[PPP3CB-AS1]] | -0.64 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[FAIM]] | -0.63 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[ANKRD40]] | -0.62 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[FIZ1]] | -0.61 | -0.68 / -0.29 | both halves | 2e-04 |  |
| [[MTHFSD]] | -0.61 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[SNX19]] | -0.61 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[ZMYND11]] | -0.61 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[PYM1]] | -0.61 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[CENPBD1P]] | -0.61 | -0.68 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers RFX2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.701). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.3, -10.3); signed map (-33.5, 21.5). **Vector** length 138, 43.9% of its response variance represented; |z| ≥ 3 in 1,310 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.54 to 5); *glycolysis* (hallmark, mean cos +0.50 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +8.1 | +11.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +6.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.5 | +12.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +7.0 | +9.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.9 | +7.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +2.7 |
|  | [[Arbutin (drug)]] 5 µM |  | +3.1 | +0.8 |
|  | [[Ritonavir (drug)]] 0.5 µM |  | +2.8 | +2.3 |
|  | [[Silodosin (drug)]] 5 µM |  | +2.8 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.9 | -8.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.0 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.9 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -4.9 | -4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.2 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.7 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | regulatory factor X2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:5,993,164-6,199,572 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14226 |
| Gene groups (HGNC) | Regulatory factor X family |
| Reactome | 4 pathways, smallest: Assembly of the 9+2 motile cilia; Transcriptional regulation of multiciliogenesis; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P48378](https://www.uniprot.org/uniprotkb/P48378) (DNA-binding protein RFX2):

> Transcription factor that acts as a key regulator of spermatogenesis. Acts by regulating expression of genes required for the haploid phase during spermiogenesis, such as genes required for cilium assembly and function (By similarity). Recognizes and binds the X-box, a regulatory motif with DNA sequence 5'-GTNRCC(0-3N)RGYAAC-3' present on promoters. Probably activates transcription of the testis-specific histone gene H1-6 (By similarity).

**Summary**, from NCBI Gene [5990](https://www.ncbi.nlm.nih.gov/gene/5990):

> This gene is a member of the regulatory factor X gene family, which encodes transcription factors that contain a highly-conserved winged helix DNA binding domain. The protein encoded by this gene is structurally related to regulatory factors X1, X3, X4, and X5. It is a transcriptional activator that can bind DNA as a monomer or as a heterodimer with other RFX family members. This protein can bind to cis elements in the promoter of the IL-5 receptor alpha gene. Two transcript variants encoding …

**Accessions** — [HGNC:9983](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9983) · Entrez [5990](https://www.ncbi.nlm.nih.gov/gene/5990) · UniProt [P48378](https://www.uniprot.org/uniprotkb/P48378) · Ensembl [ENSG00000087903](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087903)

## Data

Gene col 1515: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1515); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1515, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1515]; `tensor/DDL_lfc|DDL_z.npy` [1515]; `embed/gene_vectors.npy` [1515]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1515 or target_col == 1515). Every well: [[RFX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
