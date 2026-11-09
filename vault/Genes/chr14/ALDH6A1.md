---
symbol: "ALDH6A1"
type: "gene"
col: 4107
ensembl_id: "ENSG00000119711"
name: "aldehyde dehydrogenase 6 family member A1"
location: "14q24.3"
module: 41
arm: "+"
pooled_cpm: 16.99
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 39
n_dd_up_clean: 23
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# ALDH6A1

*aldehyde dehydrogenase 6 family member A1* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.73× (z +15.0, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.509× (z -14.2, q 3e-43, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMUT]] (+0.75, fdr 7e-06), [[DCAF11]] (+0.73, fdr 7e-06), [[OS9]] (+0.67, fdr 7e-06); moves opposite to [[NOP56]] (-0.64, fdr 9e-06), [[GPATCH4]] (-0.63, fdr 1e-05), [[SNHG26]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NYAP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4107.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.73×** | +15.0 | 0e+00 | 44/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.48×** | +13.6 | 1e-39 | 44/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.37×** | +12.9 | 5e-36 | 45/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +11.0 | 8e-26 | 20/25 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +10.9 | 8e-26 | 40/47 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +9.4 | 4e-19 | 27/39 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.63×** | +6.8 | 8e-10 | 22/34 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +6.0 | 1e-07 | 26/45 (SW1417, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.26×** | +5.0 | 4e-05 | 22/48 (H4, NCI-H1573, …) | rises with dose | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.57×** | +4.5 | 3e-04 | 19/45 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +4.4 | 7e-04 | 14/48 (NCI-H2347, KATO III, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.71×** | +4.2 | 0.001 | 16/48 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.70×** | +4.2 | 0.001 | 10/46 (BT-474, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Alpelisib (drug)]] 5 µM |  | **1.64×** | +3.9 | 0.004 | 10/44 (HCT15, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.19× | +3.7 | 0.007 | 11/48 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.011 | 13/48 (SW480, KATO III, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.012 | 9/48 (SW480, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.021 | 6/47 (SW480, LS 180, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4107.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.509×** | -14.2 | 3e-43 | 46/48 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.390×** | -14.0 | 3e-42 | 38/47 (NCI-H2347, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.403×** | -13.5 | 2e-39 | 44/48 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.434×** | -12.4 | 2e-33 | 42/47 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.440×** | -12.2 | 3e-32 | 37/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.471×** | -11.2 | 3e-27 | 37/48 (COLO 205, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.482×** | -10.9 | 2e-25 | 41/48 (COLO 205, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.498×** | -10.4 | 2e-23 | 40/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.510×** | -10.0 | 7e-22 | 36/46 (Panc 03.27, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.527×** | -9.5 | 9e-20 | 37/48 (NCI-H2347, RPMI-7951, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.535×** | -9.3 | 7e-19 | 36/48 (SW480, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.552×** | -8.8 | 5e-17 | 33/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.577×** | -7.9 | 2e-13 | 35/47 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.411×** | -6.9 | 2e-10 | 32/47 (Panc 03.27, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.586×** | -6.1 | 5e-08 | 27/47 (KATO III, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.478×** | -5.8 | 3e-07 | 23/45 (MIA PaCa-2, A498, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.681×** | -5.7 | 4e-07 | 26/47 (NCI-H1573, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4107. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 24.4 | 2 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +8.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.52× (z +8.6) | [[Ixazomib citrate (drug)]] 5 µM 0.240× (z -13.2) |
| [[KATO III (line)]] | alt | 26.7 | 1 | 4 | [[Panobinostat (drug)]] 5 µM 3.48× (z +9.3) | [[Ixazomib citrate (drug)]] 5 µM 0.107× (z -16.5) |
| [[NCI-H2347 (line)]] | alt | 27.3 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.212× (z -14.4) |
| [[Hs 766T (line)]] | wt | 16.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0787× (z -13.0) |
| [[HT-29 (line)]] | alt | 15.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.126× (z -12.1) |
| [[PANC-1 (line)]] | alt | 7.46 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 5.27× (z +10.8) | [[Harringtonine (drug)]] 0.5 µM 0.192× (z -10.7) |
| [[COLO 205 (line)]] | alt | 16.0 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0932× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 18.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +10.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 22.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.317× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.330× (z -8.6) |
| [[J82 (line)]] | alt | 13.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.61× (z +9.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.175× (z -10.1) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 23.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -13.8) |
| [[A549 (line)]] | wt | 11.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.16× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 21.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -11.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 18.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.01× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -12.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[RPMI-7951 (line)]] | alt | 20.7 | 0 | 2 | — | [[Tucidinostat (drug)]] 5 µM 0.320× (z -8.8) |
| [[SW 900 (line)]] | alt | 23.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.234× (z -8.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -8.6) |
| [[A498 (line)]] | wt | 14.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.32× (z +8.8) | — |
| [[AsPC-1 (line)]] | alt | 8.91 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.143× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -11.6) |
| [[HS-578T (line)]] | alt | 18.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -8.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[hTERT-HPNE (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -8.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[LoVo (line)]] | wt | 11.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.244× (z -8.8) |
| [[LS 180 (line)]] | wt | 25.4 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.314× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 17.1 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.330× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 10.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.39× (z +8.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -12.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 21.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -9.0) |
| [[SW1417 (line)]] | alt | 16.2 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.363× (z -9.0) |
| [[A-172 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4107), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMUT]] | +0.75 | +0.73 / +0.75 | both halves | 7e-06 | STRING 442 |
| [[DCAF11]] | +0.73 | +0.65 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM |
| [[OS9]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.66 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[PLAG1]] | +0.65 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[ATF6B]] | +0.64 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[DHTKD1]] | +0.63 | +0.58 / +0.55 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives; STRING 552 |
| [[RAB40B]] | +0.63 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[RBL2]] | +0.62 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[YIPF2]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[FAM174A]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[BBOF1]] | +0.61 | +0.49 / +0.71 | both halves | 2e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[HDAC6]] | +0.61 | +0.58 / +0.69 | both halves | 8e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOP56]] | -0.64 | -0.57 / -0.62 | both halves | 9e-06 |  |
| [[GPATCH4]] | -0.63 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[SNHG26]] | -0.62 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[ZNF562]] | -0.60 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[BICD1]] | -0.58 | -0.66 / -0.46 | both halves | 2e-05 |  |
| [[ZNF195]] | -0.58 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[GALNT14]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[MLH3]] | -0.56 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[PVR]] | -0.55 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[GCFC2]] | -0.55 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[DNAJC6]] | -0.54 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[PPIF]] | -0.54 | -0.49 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NYAP2]] | B | NYAP2 activity weakens ALDH6A1's drug response | lines that do not express NYAP2 (16) vs lines expressing it (32) | the lines without NYAP2 respond 1.05× as strongly (z diff -0.20); strongest at Dinaciclib 5 µM: 2.66x vs 1.73x (z diff -3.0) | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CHSY3, AIM2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[NYAP2]] | B | NYAP2 activity raises ALDH6A1's level | lines that do not express NYAP2 (16) vs lines expressing it (34) | 1.19× lower at baseline in the lines without NYAP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CHSY3, AIM2; maybe low, not absent |
| [[IFT122]] | C | IFT122's natural level strengthens ALDH6A1's drug response | IFT122's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.27; direction not clear | 0.069 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[RPA3]] | C | RPA3's natural level strengthens ALDH6A1's drug response | RPA3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.19; direction not clear | 0.078 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.512). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-13.9, -19.2); signed map (-20.3, 6.9). **Vector** length 106, 29.0% of its response variance represented; |z| ≥ 3 in 1,357 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.3 | +13.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.2 | +15.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.9 | +12.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | -1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +9.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.4 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | -4.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.2 | +3.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.1 | +4.5 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.6 | -0.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -12.1 | -14.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -9.8 | -8.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.5 | -12.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.3 | -13.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.6 | -9.5 |
|  | [[EX229 (drug)]] 5 µM |  | -4.4 | -6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -5.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.1 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | aldehyde dehydrogenase 6 family member A1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:74,056,847-74,084,492 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MMSDH |
| Gene groups (HGNC) | Aldehyde dehydrogenases |
| Hallmark sets | HEME_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 2 pathways, smallest: Branched-chain amino acid catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02252](https://www.uniprot.org/uniprotkb/Q02252) (Methylmalonate-semialdehyde/malonate-semialdehyde dehydrogenase):

> Malonate and methylmalonate semialdehyde dehydrogenase involved in the catabolism of valine, thymine, and compounds catabolized by way of beta-alanine, including uracil and cytidine.

**Summary**, from NCBI Gene [4329](https://www.ncbi.nlm.nih.gov/gene/4329):

> This gene encodes a member of the aldehyde dehydrogenase protein family. The encoded protein is a mitochondrial methylmalonate semialdehyde dehydrogenase that plays a role in the valine and pyrimidine catabolic pathways. This protein catalyzes the irreversible oxidative decarboxylation of malonate and methylmalonate semialdehydes to acetyl- and propionyl-CoA. Methylmalonate semialdehyde dehydrogenase deficiency is characterized by elevated beta-alanine, 3-hydroxypropionic acid, and both isomers …

**Accessions** — [HGNC:7179](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7179) · Entrez [4329](https://www.ncbi.nlm.nih.gov/gene/4329) · UniProt [Q02252](https://www.uniprot.org/uniprotkb/Q02252) · Ensembl [ENSG00000119711](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119711)

## Data

Gene col 4107: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4107); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4107, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4107]; `tensor/DDL_lfc|DDL_z.npy` [4107]; `embed/gene_vectors.npy` [4107]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4107 or target_col == 4107). Every well: [[ALDH6A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALDH6A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
