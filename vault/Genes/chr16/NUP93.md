---
symbol: "NUP93"
type: "gene"
col: 2287
ensembl_id: "ENSG00000102900"
name: "nucleoporin 93"
location: "16q13"
module: 36
arm: "+"
pooled_cpm: 50.84
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 12
n_dd_up_clean: 13
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# NUP93

*nucleoporin 93* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.21× (z +19.1, q 0e+00, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.90× (z +17.4, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.665× (z -6.7, q 1e-08, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TREX2]] (+0.74, fdr 7e-06), [[NTAQ1]] (+0.74, fdr 7e-06), [[FAR1]] (+0.72, fdr 7e-06); moves opposite to [[RNF103-CHMP3]] (-0.70, fdr 8e-06), [[OFD1]] (-0.67, fdr 7e-06), [[HLA-V-1]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GNAZ]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2287.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.21×** | +19.1 | 0e+00 | 46/48 (LoVo, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.90×** | +17.4 | 0e+00 | 48/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.75×** | +16.6 | 0e+00 | 47/48 (LoVo, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.89×** | +10.4 | 2e-23 | 42/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.29×** | +10.2 | 2e-22 | 47/49 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.81×** | +9.7 | 2e-20 | 42/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +8.7 | 2e-16 | 41/47 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.68×** | +8.5 | 1e-15 | 36/47 (SW480, SW 900, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.71×** | +8.5 | 1e-15 | 38/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +8.1 | 5e-14 | 39/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +7.6 | 1e-12 | 36/48 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +6.6 | 3e-09 | 27/48 (HOP62, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +6.2 | 2e-08 | 34/48 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.38×** | +5.2 | 7e-06 | 31/48 (HOP62, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.37×** | +5.1 | 1e-05 | 26/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.79×** | +5.0 | 2e-05 | 31/48 (HT-29, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.002 | 24/48 (SW480, Hs 766T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.29×** | +4.0 | 0.002 | 24/48 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +3.6 | 0.006 | 18/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.008 | 20/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2287.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.665×** | -6.7 | 1e-08 | 34/48 (A-172, RKO, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.757×** | -6.5 | 3e-08 | 34/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | **0.735×** | -5.0 | 9e-05 | 28/48 (KATO III, SW 1088, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.742×** | -4.9 | 2e-04 | 28/48 (SW 1271, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.787×** | -3.9 | 0.010 | 19/48 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.798×** | -3.7 | 0.021 | 19/47 (LOX-IMVI, J82, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.801×** | -3.6 | 0.022 | 18/48 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.802×** | -3.6 | 0.022 | 14/48 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.736×** | -3.6 | 0.022 | 19/48 (A498, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.812×** | -3.4 | 0.037 | 17/48 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.750×** | -3.4 | 0.040 | 17/47 (SW48, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.816×** | -3.3 | 0.042 | 17/46 (HEC-1-A, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2287. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 65.9 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +15.1) | — |
| [[NCI-H460 (line)]] | wt | 71.8 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.96× (z +11.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.5) | — |
| [[LoVo (line)]] | wt | 32.5 | 4 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.66× (z +14.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.52× (z +11.9) | [[Auranofin (drug)]] 5 µM 0.404× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 19.7 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.53× (z +19.8) | — |
| [[HOP62 (line)]] | alt | 41.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +28.2) | — |
| [[hTERT-HPNE (line)]] | wt | 23.0 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +15.3) | — |
| [[SNU-423 (line)]] | alt | 26.3 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.72× (z +10.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.39× (z +10.2) | — |
| [[A549 (line)]] | wt | 54.7 | 3 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.00× (z +8.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.16× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 61.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -9.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 48.5 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.65× (z +10.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.93× (z +9.0) | — |
| [[KATO III (line)]] | alt | 27.3 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.93× (z +10.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.78× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 25.4 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.42× (z +10.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.44× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 38.1 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.42× (z +12.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.76× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 33.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.49× (z +18.6) | — |
| [[RPMI-7951 (line)]] | alt | 42.2 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.70× (z +9.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.37× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 43.8 | 3 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.36× (z +9.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.12× (z +8.6) | — |
| [[A498 (line)]] | wt | 76.9 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.507× (z -10.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.545× (z -9.7) |
| [[H4 (line)]] | wt | 27.2 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.29× (z +9.2) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HepG2_C3A (line)]] | wt | 44.7 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.59× (z +9.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.44× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 31.3 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.89× (z +10.3) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 68.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.62× (z +9.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[A-172 (line)]] | wt | 61.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.305× (z -12.1) |
| [[BT-474 (line)]] | alt | 41.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.36× (z +9.2) | — |
| [[C32 (line)]] | wt | 35.7 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +9.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[CHP-212 (line)]] | wt | 50.1 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.115× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 19.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.06× (z +8.9) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HCT15 (line)]] | alt | 28.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.72× (z +9.3) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[HS-578T (line)]] | alt | 46.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.96× (z +9.0) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[J82 (line)]] | alt | 72.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.4) | — |
| [[LOX-IMVI (line)]] | wt | 67.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +16.0) | — |
| [[NCI-H2030 (line)]] | alt | 128 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +20.6) | — |
| [[RKO (line)]] | wt | 74.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.309× (z -9.8) |
| [[A-427 (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2287), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TREX2]] | +0.74 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[NTAQ1]] | +0.74 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[FAR1]] | +0.72 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[NCAPD3]] | +0.71 | +0.64 / +0.70 | both halves | 7e-06 | pathway: Mitotic Prophase |
| [[WDR5]] | +0.70 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[COPG2]] | +0.70 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[RANBP1]] | +0.70 | +0.69 / +0.66 | both halves | 7e-06 | pathway: HIV Infection; STRING 706 |
| [[TCOF1]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[ATAD3A]] | +0.68 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[MFSD14B]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[FANCA]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[MMS22L]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF103-CHMP3]] | -0.70 | -0.66 / -0.58 | both halves | 8e-06 |  |
| [[OFD1]] | -0.67 | -0.73 / -0.60 | both halves | 7e-06 |  |
| [[HLA-V-1]] | -0.65 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[STX17-DT]] | -0.65 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[THAP2]] | -0.65 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[N4BP2L1]] | -0.63 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ARMCX3]] | -0.63 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[TCEAL3]] | -0.63 | -0.58 / -0.61 | both halves | 8e-06 |  |
| [[SDCBP]] | -0.62 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[ZNF585A]] | -0.61 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[FAM117A]] | -0.61 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[MED29]] | -0.61 | -0.65 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAZ]] | B | GNAZ activity raises NUP93's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.70× lower at baseline in the lines without GNAZ | 0.018 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[SATB1]] | B | SATB1 activity lowers NUP93's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.38× higher at baseline in the lines without SATB1 | 0.033 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |
| [[HLA-V-1]] | B | HLA-V-1 activity lowers NUP93's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 1.37× higher at baseline in the lines without HLA-V-1 | 0.056 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| [[USP31]] | C | USP31 activity raises NUP93's level | lines that do not express USP31 (3) vs lines expressing it (47) | 2.06× lower at baseline in the lines without USP31 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.698). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-6.5, -27.7); signed map (-43.1, -15.1). **Vector** length 97.8, 28.9% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +5.1 | +19.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.9 | +16.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +17.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | -1.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +2.9 | +5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +8.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +5.0 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | +2.0 | +1.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.7 | -6.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -8.0 | -6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.7 | +6.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -5.7 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | +1.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.9 | -5.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.4 | -3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -2.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | nucleoporin 93 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:56,730,118-56,850,286 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0095 |
| Gene groups (HGNC) | Nucleoporins |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Reactome | 73 pathways, smallest: Postmitotic nuclear pore complex (NPC) reformation; IP3 and IP4 transport between cytosol and nucleus; IP6 and IP7 transport between cytosol and nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N1F7](https://www.uniprot.org/uniprotkb/Q8N1F7) (Nuclear pore complex protein Nup93):

> Plays a role in the nuclear pore complex (NPC) assembly and/or maintenance. May anchor nucleoporins, but not NUP153 and TPR, to the NPC. During renal development, regulates podocyte migration and proliferation through SMAD4 signaling.

**Summary**, from NCBI Gene [9688](https://www.ncbi.nlm.nih.gov/gene/9688):

> The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. This gene encodes a nucleoporin protein that localizes both to the basket of the pore and to the nuclear entry of the central gated channel of the pore. The encoded protein is a target of caspase cysteine proteases that play …

**Accessions** — [HGNC:28958](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28958) · Entrez [9688](https://www.ncbi.nlm.nih.gov/gene/9688) · UniProt [Q8N1F7](https://www.uniprot.org/uniprotkb/Q8N1F7) · Ensembl [ENSG00000102900](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102900)

## Data

Gene col 2287: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2287); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2287, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2287]; `tensor/DDL_lfc|DDL_z.npy` [2287]; `embed/gene_vectors.npy` [2287]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2287 or target_col == 2287). Every well: [[NUP93 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUP93.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
