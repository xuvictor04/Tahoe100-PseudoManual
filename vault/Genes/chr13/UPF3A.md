---
symbol: "UPF3A"
type: "gene"
col: 9746
ensembl_id: "ENSG00000169062"
name: "UPF3A regulator of nonsense mediated mRNA decay"
location: "13q34"
module: 88
arm: "+"
pooled_cpm: 35.5
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# UPF3A

*UPF3A regulator of nonsense mediated mRNA decay* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.38× (z +17.1, q 0e+00, up in 41 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.49× (z +11.1, q 1e-26, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.691× (z -7.3, q 2e-10, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCAR1]] (+0.66, fdr 3e-05), [[QTRT1]] (+0.63, fdr 2e-05), [[ZSCAN21]] (+0.62, fdr 1e-05); moves opposite to [[PGK1]] (-0.65, fdr 7e-06), [[EGFL7]] (-0.62, fdr 5e-05), [[ALDOA]] (-0.57, fdr 3e-05).
> It sits in the **+** arm of [[Module 088]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9746.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +17.1 | 0e+00 | 41/46 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +15.6 | 0e+00 | 36/40 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +14.1 | 1e-42 | 36/44 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.98×** | +13.0 | 3e-36 | 44/46 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +11.1 | 1e-26 | 36/48 (J82, SW 900, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +7.8 | 5e-13 | 26/48 (J82, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +5.9 | 3e-07 | 28/48 (hTERT-HPNE, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +5.8 | 5e-07 | 30/48 (J82, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.9 | 6e-05 | 22/48 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +4.8 | 8e-05 | 22/48 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.27×** | +4.5 | 3e-04 | 21/46 (SW 900, J82, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.25×** | +4.5 | 4e-04 | 21/46 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.50×** | +4.2 | 0.001 | 16/48 (Hs 766T, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.002 | 17/48 (LS 180, SW480, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.003 | 13/48 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +3.9 | 0.003 | 17/48 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.005 | 7/47 (HT-29, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.005 | 20/48 (J82, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.005 | 10/48 (NCI-H1573, LOX-IMVI, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.013 | 10/47 (NCI-H1573, A-172, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.019 | 11/47 (SW480, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9746.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.691×** | -7.3 | 2e-10 | 36/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.537×** | -6.4 | 4e-08 | 30/49 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.586×** | -5.5 | 7e-06 | 21/47 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.759×** | -5.4 | 8e-06 | 28/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.770×** | -5.1 | 3e-05 | 23/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.782×** | -4.8 | 1e-04 | 17/48 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.800×** | -4.4 | 9e-04 | 20/46 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.816×** | -4.0 | 0.004 | 16/48 (SW480, HepG2/C3A, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.822×** | -3.9 | 0.007 | 12/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM |  | **0.786×** | -3.4 | 0.040 | 5/48 (NCI-H23, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.4 | 0.040 | 12/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.896× | -3.1 | 0.10 | 14/48 (SW480, J82, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9746. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 24.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.25× (z +12.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 49.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +20.5) | [[Digitoxin (drug)]] 5 µM 0.303× (z -11.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 33.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +9.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.394× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.403× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 18.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.76× (z +10.3) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 25.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 35.7 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.08× (z +8.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.12× (z +8.7) | — |
| [[LoVo (line)]] | wt | 26.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +11.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 50.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +12.6) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.390× (z -9.3) |
| [[SW480 (line)]] | alt | 97.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.31× (z +10.9) ⚠ toxic | [[Digitoxin (drug)]] 5 µM 0.476× (z -10.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 46.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 52.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +9.7) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 44.4 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0518× (z -13.0) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 44.8 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.270× (z -8.9) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 31.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.406× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 32.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +8.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 40.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 31.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +9.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9746), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCAR1]] | +0.66 | +0.75 / +0.46 | both halves | 3e-05 |  |
| [[QTRT1]] | +0.63 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[ZSCAN21]] | +0.62 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[RC3H2]] | +0.61 | +0.69 / +0.41 | both halves | 4e-05 |  |
| [[ZC3H7B]] | +0.61 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[TXNRD2]] | +0.60 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[TMEM192]] | +0.60 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[FAIM]] | +0.59 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[BRD1]] | +0.59 | +0.57 / +0.38 | both halves | 7e-05 |  |
| [[ZNF253]] | +0.59 | +0.66 / +0.38 | both halves | 7e-05 |  |
| [[ITPA]] | +0.58 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[RPAP2]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGK1]] | -0.65 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[EGFL7]] | -0.62 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[ALDOA]] | -0.57 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[PCSK1N]] | -0.57 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[TMEM92]] | -0.57 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[SIPA1]] | -0.56 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[CARHSP1]] | -0.55 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[PRDX1]] | -0.53 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[FAM162A]] | -0.53 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[CBR1]] | -0.52 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[NDRG1]] | -0.52 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[EIF4A3]] | -0.52 | -0.39 / -0.47 | both halves | 5e-05 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC); STRING 999 |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.577). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-5.7, 5.9); signed map (20.9, -31.0). **Vector** length 79.2, 16.2% of its response variance represented; |z| ≥ 3 in 893 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +7.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +13.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +4.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.3 | +1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.3 | +1.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +3.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -4.5 | -4.0 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | -0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -3.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.7 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | UPF3A regulator of nonsense mediated mRNA decay |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:114,281,601-114,305,817 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RENT3A, UPF3, HUPF3A |
| Reactome | 7 pathways, smallest: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC); Nonsense-Mediated Decay (NMD); Regulation of expression of SLITs and ROBOs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H1J1](https://www.uniprot.org/uniprotkb/Q9H1J1) (Regulator of nonsense transcripts 3A):

> Involved in nonsense-mediated decay (NMD) of mRNAs containing premature stop codons by associating with the nuclear exon junction complex (EJC) and serving as link between the EJC core and NMD machinery. Recruits UPF2 at the cytoplasmic side of the nuclear envelope and the subsequent formation of an UPF1-UPF2-UPF3 surveillance complex (including UPF1 bound to release factors at the stalled ribosome) is believed to activate NMD. However, UPF3A is shown to be only marginally active in NMD as …

**Summary**, from NCBI Gene [65110](https://www.ncbi.nlm.nih.gov/gene/65110):

> This gene encodes a protein that is part of a post-splicing multiprotein complex involved in both mRNA nuclear export and mRNA surveillance. The encoded protein is one of two functional homologs to yeast Upf3p. mRNA surveillance detects exported mRNAs with truncated open reading frames and initiates nonsense-mediated mRNA decay (NMD). When translation ends upstream from the last exon-exon junction, this triggers NMD to degrade mRNAs containing premature stop codons. This protein binds to the …

**Accessions** — [HGNC:20332](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20332) · Entrez [65110](https://www.ncbi.nlm.nih.gov/gene/65110) · UniProt [Q9H1J1](https://www.uniprot.org/uniprotkb/Q9H1J1) · Ensembl [ENSG00000169062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169062)

## Data

Gene col 9746: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9746); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9746, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9746]; `tensor/DDL_lfc|DDL_z.npy` [9746]; `embed/gene_vectors.npy` [9746]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9746 or target_col == 9746). Every well: [[UPF3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UPF3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
