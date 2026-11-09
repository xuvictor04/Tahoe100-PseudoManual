---
symbol: "SCN9A"
type: "gene"
col: 9806
ensembl_id: "ENSG00000169432"
name: "sodium voltage-gated channel alpha subunit 9"
location: "2q24.3"
module: 9
arm: "+"
pooled_cpm: 18.26
n_lines_expressing: 29
n_dd_up: 42
n_dd_down: 13
n_dd_up_clean: 38
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 3
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SCN9A

*sodium voltage-gated channel alpha subunit 9* — 2q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.24× (z +26.5, q 0e+00, up in 26 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.567× (z -10.4, q 1e-22, down in 19 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNCA]] (+0.61, fdr 1e-05), [[COL4A4]] (+0.57, fdr 1e-05), [[RTN3]] (+0.56, fdr 4e-05); moves opposite to [[NMNAT1]] (-0.51, fdr 1e-04), [[KIAA0753]] (-0.51, fdr 9e-05), [[COL27A1]] (-0.49, fdr 2e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 3 go from it, the strongest it → [[MPP7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9806.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.24×** | +26.5 | 0e+00 | 26/26 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.54×** | +16.4 | 0e+00 | 23/25 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.32×** | +15.5 | 0e+00 | 19/26 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.19×** | +15.0 | 0e+00 | 20/26 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.10×** | +14.6 | 0e+00 | 10/23 (hTERT-HPNE, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.68×** | +12.8 | 2e-35 | 21/26 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.66×** | +12.7 | 5e-35 | 19/26 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.27×** | +10.6 | 2e-24 | 21/26 (NCI-H1573, SW 900, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +10.3 | 5e-23 | 10/17 (hTERT-HPNE, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +8.0 | 8e-14 | 10/22 (hTERT-HPNE, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **3.24×** | +8.0 | 8e-14 | 20/27 (NCI-H23, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.67×** | +6.6 | 2e-09 | 20/26 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +6.0 | 1e-07 | 13/25 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.38×** | +5.8 | 2e-07 | 16/27 (A-172, J82, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.55×** | +5.5 | 2e-06 | 16/25 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.31×** | +5.0 | 2e-05 | 12/26 (SW 900, CFPAC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.49×** | +5.0 | 2e-05 | 9/25 (A-172, A498, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.39×** | +4.2 | 7e-04 | 10/25 (A-172, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9806.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.567×** | -10.4 | 1e-22 | 19/26 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.460×** | -9.7 | 1e-19 | 19/26 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.514×** | -8.6 | 1e-15 | 18/26 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.541×** | -8.0 | 2e-13 | 18/25 (NCI-H23, HT-29, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.588×** | -6.9 | 6e-10 | 13/25 (SW 900, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.618×** | -6.2 | 4e-08 | 16/26 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.621×** | -6.2 | 5e-08 | 17/26 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.666×** | -5.3 | 1e-05 | 17/25 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.680×** | -5.0 | 4e-05 | 17/25 (J82, Panc 03.27, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.691×** | -4.8 | 9e-05 | 14/25 (HEC-1-A, HepG2/C3A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.719×** | -4.3 | 1e-03 | 15/25 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.749×** | -3.8 | 0.008 | 9/26 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.790×** | -3.1 | 0.097 | 12/26 (HepG2/C3A, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9806. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 46.5 | 1 | 13 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.36× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -20.4) |
| [[HepG2_C3A (line)]] | wt | 231 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -17.5) |
| [[NCI-H460 (line)]] | wt | 49.1 | 3 | 6 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.92× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.176× (z -11.1) |
| [[A498 (line)]] | wt | 4.69 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 11.1× (z +15.1) | — |
| [[NCI-H23 (line)]] | alt | 40.3 | 1 | 5 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.71× (z +10.1) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0680× (z -14.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.141× (z -10.7) |
| [[A-172 (line)]] | wt | 26.1 | 1 | 4 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.79× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.149× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 17.4 | 2 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.11× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 14.6 | 1 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.27× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -16.9) |
| [[NCI-H2030 (line)]] | alt | 27.8 | 1 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.37× (z +9.1) | [[Auranofin (drug)]] 5 µM 0.148× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 14.5 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0771× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0804× (z -11.9) |
| [[CHP-212 (line)]] | wt | 491 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0681× (z -23.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 7.33 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 12.0× (z +12.9) | [[Digitoxin (drug)]] 0.5 µM 0.0843× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 28.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.76× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.04× (z +8.5) | — |
| [[SW480 (line)]] | alt | 5.25 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 12.3× (z +16.8) | — |
| [[H4 (line)]] | wt | 8.35 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 8.10× (z +8.8) | [[Verteporfin (drug)]] 0.5 µM 0.0503× (z -9.0) |
| [[J82 (line)]] | alt | 13.6 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.57× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.0541× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW 900 (line)]] | alt | 9.91 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 6.72× (z +9.5) | [[Digitoxin (drug)]] 0.05 µM 0.0567× (z -10.2) |
| [[A-427 (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0788× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[A549 (line)]] | wt | 61.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 10.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.98× (z +11.0) | — |
| [[SHP-77 (line)]] | alt | 30.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.9) |
| [[SNU-423 (line)]] | alt | 12.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.10× (z +9.3) | — |
| [[SW48 (line)]] | wt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0761× (z -13.0) |
| [[AN3 CA (line)]] | alt | 3.94 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.29 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.60 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9806), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNCA]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[COL4A4]] | +0.57 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[RTN3]] | +0.56 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[ASXL3]] | +0.56 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[SYT1]] | +0.55 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[PRKAR2B]] | +0.55 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[GLRB]] | +0.55 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[TRIM58]] | +0.54 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[NCAM2]] | +0.54 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ADGRV1]] | +0.53 | +0.34 / +0.66 | both halves | 1e-04 | STRING 651 |
| [[TMOD2]] | +0.53 | +0.43 / +0.53 | both halves | 3e-05 | pathway: Muscle contraction |
| [[MARCHF1]] | +0.53 | +0.48 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMNAT1]] | -0.51 | -0.32 / -0.43 | both halves | 1e-04 |  |
| [[KIAA0753]] | -0.51 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[COL27A1]] | -0.49 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[ZNF785]] | -0.46 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[FAM120B]] | -0.46 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[IPPK]] | -0.46 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[TRIM39]] | -0.45 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[RECQL5]] | -0.44 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[ZNF597]] | -0.43 | -0.26 / -0.33 | both halves | 4e-04 |  |
| [[LINC01134]] | -0.43 | -0.26 / -0.33 | both halves | 4e-04 |  |
| [[ACAD9]] | -0.43 | -0.25 / -0.38 | both halves | 4e-04 |  |
| [[ARHGAP31]] | -0.43 | -0.34 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPP7]] | B | SCN9A activity raises MPP7's level | lines that do not express SCN9A (21) vs lines expressing it (29) | 1.75× lower at baseline in the lines without SCN9A | 0.053 | ⚠ within organs, on part of the lines; also absent: PTPRM, RPS6KA6, UCHL1 |
| [[MCAM]] | B | SCN9A activity raises MCAM's level | lines that do not express SCN9A (21) vs lines expressing it (29) | 2.05× lower at baseline in the lines without SCN9A | 0.060 | ⚠ within organs, on part of the lines; also absent: PTPRM, RPS6KA6, UCHL1 |
| [[KRT81]] | C | SCN9A activity raises KRT81's level | lines that do not express SCN9A (21) vs lines expressing it (29) | 3.78× lower at baseline in the lines without SCN9A | 0.079 | ⚠ within organs, on part of the lines; also absent: PTPRM, RPS6KA6, UCHL1; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.433). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.7, 36.3); signed map (41.1, 37.5). **Vector** length 89.0, 24.7% of its response variance represented; |z| ≥ 3 in 837 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.9 | +26.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.4 | +16.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.2 | +14.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +8.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +10.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.9 | +2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +8.0 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -3.3 | -6.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -2.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.1 | -9.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -6.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.0 | -1.7 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.5 | -2.3 |
|  | [[Ivermectin (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -0.4 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -1.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | sodium voltage-gated channel alpha subunit 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.3 — chr2:166,195,185-166,376,001 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Nav1.7, PN1, NE-NA, NENA, ETHA |
| Gene groups (HGNC) | Sodium voltage-gated channel alpha subunits |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 10 pathways, smallest: Sensory perception of sweet, bitter, and umami (glutamate) taste; Sensory perception of taste; Interaction between L1 and Ankyrins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15858](https://www.uniprot.org/uniprotkb/Q15858) (Sodium channel protein type 9 subunit alpha):

> Pore-forming subunit of Nav1.7, a voltage-gated sodium (Nav) channel that directly mediates the depolarizing phase of action potentials in excitable membranes. Navs, also called VGSCs (voltage-gated sodium channels) or VDSCs (voltage-dependent sodium channels), operate by switching between closed and open conformations depending on the voltage difference across the membrane. In the open conformation they allow Na(+) ions to selectively pass through the pore, along their electrochemical …

**Summary**, from NCBI Gene [6335](https://www.ncbi.nlm.nih.gov/gene/6335):

> This gene encodes a voltage-gated sodium channel which plays a significant role in nociception signaling. Mutations in this gene have been associated with primary erythermalgia, channelopathy-associated insensitivity to pain, and paroxysmal extreme pain disorder. [provided by RefSeq, Aug 2009]

**Accessions** — [HGNC:10597](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10597) · Entrez [6335](https://www.ncbi.nlm.nih.gov/gene/6335) · UniProt [Q15858](https://www.uniprot.org/uniprotkb/Q15858) · Ensembl [ENSG00000169432](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169432)

## Data

Gene col 9806: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9806); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9806, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9806]; `tensor/DDL_lfc|DDL_z.npy` [9806]; `embed/gene_vectors.npy` [9806]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9806 or target_col == 9806). Every well: [[SCN9A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCN9A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
