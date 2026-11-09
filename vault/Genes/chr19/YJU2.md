---
symbol: "YJU2"
type: "gene"
col: 2570
ensembl_id: "ENSG00000105248"
name: "YJU2 splicing factor homolog"
location: "19p13.3"
module: 51
arm: "+"
pooled_cpm: 11.51
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 14
n_dd_up_clean: 16
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# YJU2

*YJU2 splicing factor homolog* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.95× (z +27.4, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.340× (z -19.2, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM23]] (+0.80, fdr 7e-06), [[TRMO]] (+0.79, fdr 7e-06), [[FIZ1]] (+0.78, fdr 7e-06); moves opposite to [[SETD3]] (-0.68, fdr 7e-06), [[PCMT1]] (-0.66, fdr 1e-05), [[HDAC3]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SESTD1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2570.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.95×** | +27.4 | 0e+00 | 44/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.32×** | +14.5 | 6e-45 | 36/46 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.22×** | +13.5 | 4e-39 | 43/47 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +11.3 | 1e-27 | 35/45 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.42×** | +8.3 | 1e-14 | 30/44 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +7.2 | 4e-11 | 24/47 (LS 180, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +6.2 | 5e-08 | 20/46 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +6.0 | 1e-07 | 16/47 (NCI-H2030, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +4.9 | 5e-05 | 16/47 (NCI-H460, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +4.7 | 1e-04 | 12/47 (HT-29, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +4.3 | 0.001 | 7/46 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +4.1 | 0.002 | 16/46 (NCI-H460, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.15× | +3.6 | 0.015 | 4/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.021 | 5/47 (SW480, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.021 | 13/47 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.021 | 10/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2570.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.340×** | -19.2 | 0e+00 | 44/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.374×** | -17.6 | 0e+00 | 46/47 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.401×** | -16.3 | 0e+00 | 41/47 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.420×** | -15.5 | 0e+00 | 43/47 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.539×** | -11.0 | 5e-26 | 25/37 (LS 180, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.532×** | -10.8 | 3e-25 | 16/20 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.571×** | -9.6 | 6e-20 | 28/46 (HS-578T, A-427, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.584×** | -9.6 | 8e-20 | 31/44 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.406×** | -8.4 | 3e-15 | 29/48 (RPMI-7951, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.731×** | -7.9 | 2e-13 | 27/48 (NCI-H23, NCI-H2347, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -7.0 | 2e-10 | 24/47 (NCI-H23, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.750×** | -4.9 | 4e-05 | 15/41 (SNU-423, C32, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Radotinib (drug)]] 0.5 µM |  | **0.810×** | -3.7 | 0.009 | 12/44 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.830×** | -3.3 | 0.037 | 16/47 (SW 900, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 0.876× | -3.3 | 0.037 | 15/46 (NCI-H2030, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2570. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 12.3 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 35.4 | 0 | 5 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -15.3) |
| [[PANC-1 (line)]] | alt | 9.71 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 8.55× (z +23.0) | [[Belinostat (drug)]] 5 µM 0.239× (z -10.9) |
| [[A498 (line)]] | wt | 8.75 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +22.4) | [[Dinaciclib (drug)]] 5 µM 0.140× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 19.8 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.214× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 9.31 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.164× (z -11.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 12.9 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +10.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -9.7) |
| [[A-172 (line)]] | wt | 8.37 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.75× (z +15.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 13.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.226× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 12.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 13.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.73× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.0503× (z -15.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 13.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -9.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 13.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -9.0) |
| [[A549 (line)]] | wt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +12.4) | — |
| [[C32 (line)]] | wt | 11.6 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 9.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.95× (z +17.7) | — |
| [[COLO 205 (line)]] | alt | 10.3 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.103× (z -9.5) |
| [[H4 (line)]] | wt | 9.84 | 0 | 1 | — | [[NG25 (drug)]] 0.05 µM 0.0669× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 9.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +13.3) | — |
| [[HepG2_C3A (line)]] | wt | 9.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +13.2) | — |
| [[HOP62 (line)]] | alt | 5.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +11.8) | — |
| [[Hs 766T (line)]] | wt | 7.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.53× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 7.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +8.6) | — |
| [[J82 (line)]] | alt | 8.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +14.0) | — |
| [[LOX-IMVI (line)]] | wt | 9.81 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -10.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0610× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 14.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -8.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.61× (z +12.8) | — |
| [[SW 900 (line)]] | alt | 8.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 13.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.254× (z -8.5) |
| [[SW48 (line)]] | wt | 17.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.139× (z -8.5) |
| [[AN3 CA (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2570), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM23]] | +0.80 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[TRMO]] | +0.79 | +0.84 / +0.59 | both halves | 7e-06 |  |
| [[FIZ1]] | +0.78 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[ZNF830]] | +0.76 | +0.75 / +0.61 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[NAIF1]] | +0.75 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[KAT5]] | +0.75 | +0.77 / +0.80 | both halves | 7e-06 |  |
| [[WARS2]] | +0.74 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[EPC1]] | +0.73 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[METTL18]] | +0.73 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[INTS14]] | +0.73 | +0.73 / +0.44 | both halves | 3e-05 |  |
| [[ZNF764]] | +0.72 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[THG1L]] | +0.72 | +0.75 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD3]] | -0.68 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[PCMT1]] | -0.66 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[HDAC3]] | -0.63 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[STRN]] | -0.63 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[METAP1]] | -0.62 | -0.64 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SESTD1]] | C | SESTD1 activity lowers YJU2's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 1.53× higher at baseline in the lines without SESTD1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.781). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-35.9, 8.1); signed map (3.1, -21.0). **Vector** length 80.5, 15.7% of its response variance represented; |z| ≥ 3 in 1,150 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.8 | +27.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.5 | +11.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +14.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.0 | +3.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.8 | +13.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | -0.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.7 | -1.2 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -5.0 | -15.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.8 | -19.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.7 | -9.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -8.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.5 | -4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -7.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | +1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.6 | +0.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | YJU2 splicing factor homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,247,080-4,269,088 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10374; previously CCDC94 |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BW85](https://www.uniprot.org/uniprotkb/Q9BW85) (Splicing factor YJU2):

> Part of the spliceosome which catalyzes two sequential transesterification reactions, first the excision of the non-coding intron from pre-mRNA and then the ligation of the coding exons to form the mature mRNA. Plays a role in stabilizing the structure of the spliceosome catalytic core and docking of the branch helix into the active site, producing 5'-exon and lariat intron-3'-intermediates (By similarity). May protect cells from TP53-dependent apoptosis upon dsDNA break damage through …

**Summary**, from NCBI Gene [55702](https://www.ncbi.nlm.nih.gov/gene/55702):

> Predicted to enable metal ion binding activity. Predicted to contribute to first spliceosomal transesterification activity. Predicted to be involved in mRNA cis splicing, via spliceosome and negative regulation of DNA damage response, signal transduction by p53 class mediator. Part of U2-type catalytic step 1 spliceosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25518](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25518) · Entrez [55702](https://www.ncbi.nlm.nih.gov/gene/55702) · UniProt [Q9BW85](https://www.uniprot.org/uniprotkb/Q9BW85) · Ensembl [ENSG00000105248](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105248)

## Data

Gene col 2570: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2570); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2570, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2570]; `tensor/DDL_lfc|DDL_z.npy` [2570]; `embed/gene_vectors.npy` [2570]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2570 or target_col == 2570). Every well: [[YJU2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YJU2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
