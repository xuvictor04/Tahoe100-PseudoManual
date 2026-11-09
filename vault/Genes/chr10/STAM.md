---
symbol: "STAM"
type: "gene"
col: 5898
ensembl_id: "ENSG00000136738"
name: "signal transducing adaptor molecule"
location: "10p12.33"
module: 30
arm: "+"
pooled_cpm: 78.33
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 7
n_dd_up_clean: 21
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# STAM

*signal transducing adaptor molecule* — 10p12.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.07× (z +11.9, q 7e-30, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.565× (z -7.7, q 7e-12, down in 34 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 0.05 µM: 0.774× (z -3.6, q 0.050, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB18]] (+0.68, fdr 7e-06), [[NTAN1]] (+0.66, fdr 1e-05), [[STX7]] (+0.65, fdr 1e-05); moves opposite to [[ERCC6L2]] (-0.70, fdr 1e-05), [[SP2]] (-0.64, fdr 1e-05), [[SKIL]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 030]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5898.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.07×** | +11.9 | 7e-30 | 48/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.32×** | +11.8 | 1e-29 | 48/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.05×** | +10.1 | 2e-21 | 44/48 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.56×** | +9.3 | 2e-18 | 42/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +8.9 | 7e-17 | 45/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.80×** | +7.8 | 9e-13 | 41/48 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +7.7 | 9e-13 | 41/48 (SW480, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.64×** | +6.9 | 3e-10 | 39/48 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.62×** | +6.8 | 8e-10 | 39/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.61×** | +6.7 | 1e-09 | 41/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +6.6 | 2e-09 | 38/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +5.8 | 3e-07 | 32/47 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +5.2 | 1e-05 | 28/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +4.9 | 5e-05 | 30/48 (KATO III, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.41×** | +4.8 | 7e-05 | 29/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +4.7 | 8e-05 | 30/49 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.59×** | +4.7 | 1e-04 | 34/49 (PANC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5898.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.565×** | -7.7 | 7e-12 | 34/44 (NCI-H1573, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.634×** | -6.4 | 4e-08 | 34/49 (Panc 03.27, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.774×** | -3.6 | 0.050 | 27/48 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -3.6 | 0.050 | 21/49 (AsPC-1, HepG2/C3A, …) | top dose only |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.782×** | -3.5 | 0.061 | 23/48 (RPMI-7951, A498, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.785×** | -3.4 | 0.061 | 24/48 (NCI-H2347, RPMI-7951, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.850× | -3.2 | 0.096 | 20/48 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.799×** | -3.2 | 0.096 | 20/48 (AsPC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.799×** | -3.2 | 0.096 | 19/47 (C32, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5898. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 46.7 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +11.3) | — |
| [[LoVo (line)]] | wt | 73.8 | 6 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.2× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.365× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 58.2 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 43.4 | 5 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.94× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.138× (z -16.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 53.9 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.72× (z +16.4) | — |
| [[J82 (line)]] | alt | 108 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +13.6) | — |
| [[LS 180 (line)]] | wt | 135 | 3 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -11.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 87.7 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.12× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.410× (z -8.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 167 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.65× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 48.1 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.36× (z +10.9) | — |
| [[NCI-H2347 (line)]] | alt | 105 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.98× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -11.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 52.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.98× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 122 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +10.9) | — |
| [[RKO (line)]] | wt | 114 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.68× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -13.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 99.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.89× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -8.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 148 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.13× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 96.6 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.16× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 67.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +11.9) | — |
| [[SNU-423 (line)]] | alt | 69.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +8.7) | — |
| [[A498 (line)]] | wt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +13.4) | — |
| [[AN3 CA (line)]] | alt | 74.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.191× (z -8.8) |
| [[C-33 A (line)]] | alt | 50.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -9.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -9.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 46.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.2× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 164 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 68.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +10.3) | — |
| [[NCI-H596 (line)]] | alt | 85.2 | 0 | 1 | — | [[Oxaprozin (drug)]] 5 µM 0.139× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 47.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -14.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 72.7 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.117× (z -8.7) |
| [[A-172 (line)]] | wt | 87.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 71.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 70.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5898), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB18]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[NTAN1]] | +0.66 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[STX7]] | +0.65 | +0.68 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[SEC11A]] | +0.64 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[OTULIN]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[RTCA]] | +0.64 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CYB5R4]] | +0.64 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[IGSF8]] | +0.62 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[MBOAT2]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[NFRKB]] | +0.62 | +0.57 / +0.45 | both halves | 3e-05 | pathway: Deubiquitination |
| [[HBS1L]] | +0.62 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[SERAC1]] | +0.61 | +0.59 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.70 | -0.73 / -0.55 | both halves | 1e-05 |  |
| [[SP2]] | -0.64 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[SKIL]] | -0.63 | -0.66 / -0.44 | both halves | 3e-05 |  |
| [[ATXN7]] | -0.62 | -0.59 / -0.44 | both halves | 3e-05 | pathway: Deubiquitination |
| [[MEPCE]] | -0.61 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[KDSR]] | -0.61 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[ZC3H7B]] | -0.61 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[IBA57]] | -0.61 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[FKRP]] | -0.60 | -0.66 / -0.30 | both halves | 2e-04 |  |
| [[ZNF764]] | -0.58 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[DCAF8]] | -0.58 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[ZCCHC3]] | -0.58 | -0.63 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.670). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-5.6, -12.0); signed map (-34.2, -15.6). **Vector** length 87.9, 28.5% of its response variance represented; |z| ≥ 3 in 1,268 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +7.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.1 | +6.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.9 | +6.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.6 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.5 | +10.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +4.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +1.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.7 | -0.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.5 | -1.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.5 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | +1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.5 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | +0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -1.2 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -1.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | signal transducing adaptor molecule |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.33 — chr10:17,644,151-17,716,824 (+) |
| Ensembl biotype | protein_coding |
| Also known as | STAM1 |
| Gene groups (HGNC) | ESCRT-0; SH3 domain containing |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 19 pathways, smallest: InlB-mediated entry of Listeria monocytogenes into host cell; Listeria monocytogenes entry into host cells; Negative regulation of MET activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92783](https://www.uniprot.org/uniprotkb/Q92783) (Signal transducing adapter molecule 1):

> Involved in intracellular signal transduction mediated by cytokines and growth factors. Upon IL-2 and GM-CSL stimulation, it plays a role in signaling leading to DNA synthesis and MYC induction. May also play a role in T-cell development. Involved in down-regulation of receptor tyrosine kinase via multivesicular body (MVBs) when complexed with HGS (ESCRT-0 complex). The ESCRT-0 complex binds ubiquitin and acts as a sorting machinery that recognizes ubiquitinated receptors and transfers them to …

**Summary**, from NCBI Gene [8027](https://www.ncbi.nlm.nih.gov/gene/8027):

> This gene encodes a member of the signal-transducing adaptor molecule family. These proteins mediate downstream signaling of cytokine receptors and also play a role in ER to Golgi trafficking by interacting with the coat protein II complex. The encoded protein also associates with hepatocyte growth factor-regulated substrate to form the endosomal sorting complex required for transport-0 (ESCRT-0), which sorts ubiquitinated membrane proteins to the ESCRT-1 complex for lysosomal degradation. …

**Accessions** — [HGNC:11357](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11357) · Entrez [8027](https://www.ncbi.nlm.nih.gov/gene/8027) · UniProt [Q92783](https://www.uniprot.org/uniprotkb/Q92783) · Ensembl [ENSG00000136738](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136738)

## Data

Gene col 5898: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5898); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5898, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5898]; `tensor/DDL_lfc|DDL_z.npy` [5898]; `embed/gene_vectors.npy` [5898]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5898 or target_col == 5898). Every well: [[STAM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
