---
symbol: "ANKRD13A"
type: "gene"
col: 1153
ensembl_id: "ENSG00000076513"
name: "ankyrin repeat domain 13A"
location: "12q24.11"
module: 17
arm: "+"
pooled_cpm: 43.05
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 17
n_dd_up_clean: 26
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ANKRD13A

*ankyrin repeat domain 13A* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.20× (z +20.8, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.621× (z -8.9, q 5e-16, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIMA1]] (+0.54, fdr 1e-05), [[LCOR]] (+0.49, fdr 3e-05), [[ACBD5]] (+0.49, fdr 3e-05); moves opposite to [[APTX]] (-0.47, fdr 7e-05), [[ANKMY1]] (-0.45, fdr 5e-05), [[VTI1A]] (-0.45, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[VEGFD]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 2 with an alert ⚠; shown: the 15 strongest. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1153.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.20×** | +20.8 | 0e+00 | 45/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.83×** | +19.3 | 0e+00 | 47/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.43×** | +16.5 | 0e+00 | 46/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.33×** | +15.7 | 0e+00 | 45/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +11.4 | 5e-28 | 35/48 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.84×** | +10.9 | 1e-25 | 37/48 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +9.8 | 7e-21 | 31/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +9.3 | 9e-19 | 38/48 (HOP62, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +7.3 | 2e-11 | 27/48 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Trametinib (drug)]] 5 µM |  | **1.43×** | +7.2 | 5e-11 | 33/49 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.40×** | +6.2 | 2e-08 | 30/48 (LS 180, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +6.2 | 4e-08 | 33/48 (A498, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +6.0 | 7e-08 | 29/47 (AsPC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.9 | 1e-07 | 27/49 (LS 180, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +5.5 | 1e-06 | 25/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1153.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.621×** | -8.9 | 5e-16 | 33/48 (HT-29, SW1417, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.690×** | -6.9 | 1e-09 | 29/48 (HT-29, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.690×** | -6.6 | 6e-09 | 30/47 (NCI-H460, SW1417, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.708×** | -6.4 | 2e-08 | 32/48 (HT-29, NCI-H2030, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.555×** | -5.7 | 1e-06 | 26/48 (HT-29, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.727×** | -5.4 | 7e-06 | 25/48 (HT-29, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.604×** | -4.9 | 7e-05 | 23/43 (Hs 766T, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.758×** | -4.8 | 1e-04 | 20/40 (SW480, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.778×** | -4.7 | 2e-04 | 23/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.788×** | -4.4 | 5e-04 | 21/48 (C32, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.793×** | -4.3 | 8e-04 | 20/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change | **0.803×** | -4.1 | 0.002 | 22/48 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.658×** | -4.1 | 0.002 | 22/48 (SK-MEL-2, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.661×** | -4.0 | 0.002 | 19/48 (PANC-1, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.683×** | -3.7 | 0.008 | 19/47 (HS-578T, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.717×** | -3.2 | 0.040 | 15/48 (AsPC-1, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Erythromycin (drug)]] 5 µM |  | 0.850× | -3.0 | 0.070 | 8/48 (AN3 CA, H4, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 0.855× | -2.9 | 0.094 | 14/48 (LoVo, SK-MEL-2, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1153. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 41.6 | 3 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +14.8) | [[Ixazomib citrate (drug)]] 5 µM 0.244× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 26.6 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +12.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.252× (z -13.1) ⚠ toxic |
| [[SW480 (line)]] | alt | 37.2 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +19.3) | [[Dinaciclib (drug)]] 0.05 µM 0.290× (z -13.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 41.7 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 4.87× (z +12.5) | — |
| [[PANC-1 (line)]] | alt | 31.3 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.67× (z +12.8) | — |
| [[A-427 (line)]] | wt | 19.9 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.87× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 52.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +13.2) | — |
| [[LS 180 (line)]] | wt | 26.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +17.2) | — |
| [[A498 (line)]] | wt | 51.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +11.1) | — |
| [[A549 (line)]] | wt | 28.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.05× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 67.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.324× (z -9.1) |
| [[KATO III (line)]] | alt | 33.5 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 29.7 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.82× (z +13.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 25.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +15.0) | — |
| [[SNU-423 (line)]] | alt | 44.8 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.64× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.99× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 47.5 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +17.1) | [[Auranofin (drug)]] 5 µM 0.339× (z -9.4) |
| [[HS-578T (line)]] | alt | 33.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +12.1) | — |
| [[hTERT-HPNE (line)]] | wt | 34.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +13.7) | — |
| [[AN3 CA (line)]] | alt | 45.0 | 0 | 2 (1 ⚠) | — | [[Silodosin (drug)]] 5 µM 0.0627× (z -11.3) |
| [[HepG2_C3A (line)]] | wt | 50.1 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.265× (z -9.4) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 62.1 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.91× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 32.6 | 2 | 0 | [[Belinostat (drug)]] 5 µM 3.52× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 47.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +14.7) | — |
| [[RKO (line)]] | wt | 98.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 40.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +14.9) | — |
| [[C-33 A (line)]] | alt | 22.6 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.19× (z +9.0) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[CFPAC-1 (line)]] | alt | 38.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 32.9 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0879× (z -9.3) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 21.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.85× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 41.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -11.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 53.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -9.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 18.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +8.5) | — |
| [[A-172 (line)]] | wt | 84.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1153), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIMA1]] | +0.54 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[LCOR]] | +0.49 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[ACBD5]] | +0.49 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[CGN]] | +0.48 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[SCOC]] | +0.48 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[NMT2]] | +0.47 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[ILK]] | +0.47 | +0.34 / +0.44 | both halves | 1e-04 | same gene group |
| [[SLC50A1]] | +0.46 | +0.52 / +0.39 | both halves | 6e-05 |  |
| [[TLCD4]] | +0.46 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[BPNT1]] | +0.46 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[ACTR1B]] | +0.46 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[MITF]] | +0.45 | +0.43 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APTX]] | -0.47 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[ANKMY1]] | -0.45 | -0.43 / -0.40 | both halves | 5e-05 | same gene group |
| [[VTI1A]] | -0.45 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[SLC38A6]] | -0.45 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[HSPE1]] | -0.45 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[GPR135]] | -0.44 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[LRP8]] | -0.44 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[MTHFD2L]] | -0.44 | -0.36 / -0.37 | both halves | 9e-05 |  |
| [[LRRC69]] | -0.43 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[ZKSCAN2-DT]] | -0.42 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[LMBR1]] | -0.42 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[PHF14]] | -0.41 | -0.30 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VEGFD]] | B | VEGFD activity lowers ANKRD13A's level | lines that do not express VEGFD (13) vs lines expressing it (37) | 1.19× higher at baseline in the lines without VEGFD | 0.045 | ⚠ within organs, on part of the lines; also absent: PIR, ELMO1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers ANKRD13A's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.233). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (5.1, -27.6); signed map (11.7, -13.9). **Vector** length 108, 30.5% of its response variance represented; |z| ≥ 3 in 1,487 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.9 | +10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +20.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.7 | +2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.5 | +4.2 |
|  | [[Trametinib (drug)]] 5 µM |  | +4.1 | +7.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.8 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.6 | +2.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.5 | +0.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +4.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.8 | -8.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.8 | -6.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.8 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.7 | -4.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -6.4 |
|  | [[EX229 (drug)]] 5 µM |  | -3.5 | -4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.4 | -4.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.3 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 13A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:109,999,186-110,039,763 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NY-REN-25; previously ANKRD13 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZ07](https://www.uniprot.org/uniprotkb/Q8IZ07) (Ankyrin repeat domain-containing protein 13A):

> Ubiquitin-binding protein that specifically recognizes and binds 'Lys-63'-linked ubiquitin. Does not bind 'Lys-48'-linked ubiquitin. Positively regulates the internalization of ligand-activated EGFR by binding to the Ub moiety of ubiquitinated EGFR at the cell membrane.

**Summary**, from NCBI Gene [88455](https://www.ncbi.nlm.nih.gov/gene/88455):

> Enables ubiquitin-modified protein reader activity. Involved in negative regulation of protein localization to endosome and negative regulation of receptor internalization. Located in late endosome; perinuclear region of cytoplasm; and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21268](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21268) · Entrez [88455](https://www.ncbi.nlm.nih.gov/gene/88455) · UniProt [Q8IZ07](https://www.uniprot.org/uniprotkb/Q8IZ07) · Ensembl [ENSG00000076513](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076513)

## Data

Gene col 1153: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1153); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1153, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1153]; `tensor/DDL_lfc|DDL_z.npy` [1153]; `embed/gene_vectors.npy` [1153]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1153 or target_col == 1153). Every well: [[ANKRD13A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD13A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
