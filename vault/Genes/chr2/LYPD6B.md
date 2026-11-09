---
symbol: "LYPD6B"
type: "gene"
col: 7444
ensembl_id: "ENSG00000150556"
name: "LY6/PLAUR domain containing 6B"
location: "2q23.2"
module: 55
arm: "+"
pooled_cpm: 20.21
n_lines_expressing: 27
n_dd_up: 9
n_dd_down: 30
n_dd_up_clean: 7
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 7
direction_downstream: 16
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# LYPD6B

*LY6/PLAUR domain containing 6B* — 2q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.08× (z +16.0, q 0e+00, up in 17 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.401× (z -13.6, q 2e-39, down in 17 of 23 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.475× (z -11.5, q 1e-28, down in 15 of 23 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALDH1L1]] (+0.64, fdr 1e-05), [[UNC5B]] (+0.62, fdr 2e-05), [[SLC5A1]] (+0.60, fdr 1e-05); moves opposite to [[PUS10]] (-0.41, fdr 3e-04), [[ZNF253]] (-0.39, fdr 1e-04), [[ZNF431]] (-0.39, fdr 4e-04).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TMPRSS3]] → it (grade B ⚠); 16 go from it, the strongest it → [[MROH7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7444.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.08×** | +16.0 | 0e+00 | 17/25 (SW1417, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.30×** | +12.9 | 2e-35 | 18/24 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.46×** | +5.8 | 1e-06 | 10/25 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +4.6 | 5e-04 | 1/12 (BT-474) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.1 | 0.004 | 5/22 (COLO 205, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.020 | 6/25 (NCI-H1792, J82, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **1.26×** | +3.6 | 0.024 | 5/24 (NCI-H1792, BT-474, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.024 | 9/24 (HCT15, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.068 | 0/23 | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | 1.47× | +3.1 | 0.10 | 1/17 (BT-474) | inconsistent across doses | noisy plate (z scaled) |
| [[Sildenafil (drug)]] 0.5 µM |  | 1.22× | +3.1 | 0.11 | 2/24 (SW1417, HT-29) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7444.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.401×** | -13.6 | 2e-39 | 17/23 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.544×** | -13.3 | 4e-38 | 20/24 (LoVo, H4, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.456×** | -12.2 | 1e-31 | 19/24 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.475×** | -11.5 | 1e-28 | 15/23 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.488×** | -11.1 | 2e-26 | 22/24 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.513×** | -10.3 | 5e-23 | 17/21 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.545×** | -9.4 | 5e-19 | 19/24 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.558×** | -9.0 | 1e-17 | 17/24 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.653×** | -6.6 | 3e-09 | 16/24 (J82, SW480, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.688×** | -5.8 | 4e-07 | 13/24 (J82, LoVo, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.496×** | -5.7 | 7e-07 | 12/25 (LoVo, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.720×** | -5.1 | 2e-05 | 12/24 (H4, SW480, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | **0.793×** | -5.1 | 2e-05 | 6/25 (NCI-H1792, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.728×** | -4.7 | 9e-05 | 13/21 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.734×** | -4.6 | 2e-04 | 11/24 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.750×** | -4.3 | 6e-04 | 8/25 (NCI-H661, A-427, …) | top dose only |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **0.765×** | -4.1 | 1e-03 | 8/25 (J82, SW480, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.787×** | -3.7 | 0.006 | 14/24 (SW48, H4, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.788×** | -3.7 | 0.006 | 10/24 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.638×** | -3.6 | 0.007 | 8/22 (SW 900, J82, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.643×** | -3.6 | 0.008 | 5/20 (LS 180, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.787×** | -3.6 | 0.008 | 6/24 (SW 900, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.646×** | -3.5 | 0.009 | 10/21 (LS 180, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7444. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.1 | 0 | 17 (10 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0911× (z -15.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -14.3) |
| [[LoVo (line)]] | wt | 75.6 | 1 (1 ⚠) | 14 (10 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.95× (z +9.7) ⚠ cell-cycle shift, explains ~87% of this change | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -28.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -18.5) |
| [[J82 (line)]] | alt | 204 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -19.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.177× (z -13.4) |
| [[HT-29 (line)]] | alt | 33.2 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -13.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.232× (z -8.5) |
| [[LS 180 (line)]] | wt | 32.2 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -15.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.112× (z -12.4) |
| [[H4 (line)]] | wt | 215 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0444× (z -23.6) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 90.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -19.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -12.1) |
| [[COLO 205 (line)]] | alt | 13.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0465× (z -16.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0858× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0917× (z -10.1) |
| [[SW1417 (line)]] | alt | 33.4 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.68× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 23.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0317× (z -20.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.107× (z -9.5) |
| [[A-427 (line)]] | wt | 10.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -10.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.213× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HOP62 (line)]] | alt | 32.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -10.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[KATO III (line)]] | alt | 15.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0726× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 6.72 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0411× (z -13.3) |
| [[A-172 (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.75 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 21.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7444), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH1L1]] | +0.64 | +0.52 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[UNC5B]] | +0.62 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[SLC5A1]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[FAM83F]] | +0.54 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[MCTP2]] | +0.53 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[HKDC1]] | +0.50 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[PREX1]] | +0.50 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[IGSF9]] | +0.49 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[KIF21B]] | +0.47 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[ESRP1]] | +0.46 | +0.49 / +0.38 | both halves | 6e-05 |  |
| [[CYP4F11]] | +0.45 | +0.40 / +0.36 | both halves | 1e-04 |  |
| [[ATP2C2]] | +0.45 | +0.31 / +0.44 | both halves | 2e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUS10]] | -0.41 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[ZNF253]] | -0.39 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[ZNF431]] | -0.39 | -0.40 / -0.25 | both halves | 4e-04 |  |
| [[RBKS]] | -0.39 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[HIPK3]] | -0.38 | -0.24 / -0.35 | both halves | 5e-04 |  |
| [[MCPH1-AS1]] | -0.37 | -0.35 / -0.27 | both halves | 3e-04 |  |
| [[ZNF714]] | -0.37 | -0.33 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMPRSS3]] | B | TMPRSS3 activity raises LYPD6B's level | lines that do not express TMPRSS3 (29) vs lines expressing it (21) | 2.21× lower at baseline in the lines without TMPRSS3 | 0.067 | ⚠ within organs, on part of the lines; also absent: S100P, TFF2, HSD17B2 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers LYPD6B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[JAK1]], [[JAK3]] | B | JAK1, JAK3 activity lowers LYPD6B's level | compounds that target JAK1, JAK3: 2 of 2 raise it (Filgotinib, Tofacitinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[PTPRE]] | B | PTPRE activity raises LYPD6B's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 2.88× lower at baseline in the lines without PTPRE | 0.098 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[MCTP2]] | C | MCTP2 activity raises LYPD6B's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 2.55× lower at baseline in the lines without MCTP2 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3; co-absent with the target |
| [[SKAP1]] | C | SKAP1 activity raises LYPD6B's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 2.81× lower at baseline in the lines without SKAP1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1; co-absent with the target |
| [[ARHGAP8]] | C | ARHGAP8 activity raises LYPD6B's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 2.29× lower at baseline in the lines without ARHGAP8 | 0.050 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 7, C 9. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MROH7]] | B | LYPD6B activity raises MROH7's level | lines that do not express LYPD6B (23) vs lines expressing it (27) | 2.45× lower at baseline in the lines without LYPD6B | 0.017 | ⚠ within organs, on part of the lines; also absent: GPR35, ATP2C2, EPHB6 |
| [[PTPRE]] | B | LYPD6B activity raises PTPRE's level | lines that do not express LYPD6B (23) vs lines expressing it (27) | 2.65× lower at baseline in the lines without LYPD6B | 0.019 | ⚠ within organs, on part of the lines; also absent: GPR35, ATP2C2, EPHB6 |
| [[TMPRSS3]] | B | LYPD6B activity raises TMPRSS3's level | lines that do not express LYPD6B (23) vs lines expressing it (27) | 1.86× lower at baseline in the lines without LYPD6B | 0.034 | ⚠ within organs, on part of the lines; also absent: GPR35, ATP2C2, EPHB6 |
| [[COLEC12]] | B | LYPD6B activity raises COLEC12's level | lines that do not express LYPD6B (23) vs lines expressing it (27) | 1.62× lower at baseline in the lines without LYPD6B | 0.067 | ⚠ within organs, on part of the lines; also absent: GPR35, ATP2C2, EPHB6 |
| [[PTPRE]] | B | LYPD6B activity strengthens PTPRE's drug response | lines that do not express LYPD6B (13) vs lines expressing it (24) | the lines without LYPD6B respond 0.73× as strongly (z diff +1.97); strongest at Homoharringtonine 0.5 µM: 0.73x vs 0.39x (z diff +4.4) | 0.076 | ⚠ within organs, on part of the lines; also absent: GPR35, ATP2C2, EPHB6; target measured in part of the lines; artifact flags |
| [[SYTL1]] | B | LYPD6B activity raises SYTL1's level | lines that do not express LYPD6B (23) vs lines expressing it (27) | 1.87× lower at baseline in the lines without LYPD6B | 0.089 | ⚠ within organs, on part of the lines; also absent: GPR35, ATP2C2, EPHB6 |
| [[PLEKHG1]] | B | LYPD6B activity raises PLEKHG1's level | lines that do not express LYPD6B (23) vs lines expressing it (27) | 2.39× lower at baseline in the lines without LYPD6B | 0.089 | ⚠ within organs, on part of the lines; also absent: GPR35, ATP2C2, EPHB6 |
| [[MCTP2]] | C | LYPD6B activity raises MCTP2's level | lines that do not express LYPD6B (23) vs lines expressing it (27) | 3.94× lower at baseline in the lines without LYPD6B | 0.024 | ⚠ within organs, on part of the lines; also absent: GPR35, ATP2C2, EPHB6; co-absent with the target |
| [[ARHGAP8]] | C | LYPD6B activity raises ARHGAP8's level | lines that do not express LYPD6B (23) vs lines expressing it (27) | 3.08× lower at baseline in the lines without LYPD6B | 0.024 | ⚠ within organs, on part of the lines; also absent: GPR35, ATP2C2, EPHB6; co-absent with the target |
| [[ESRP1]] | C | LYPD6B activity raises ESRP1's level | lines that do not express LYPD6B (23) vs lines expressing it (27) | 5.25× lower at baseline in the lines without LYPD6B | 0.034 | ⚠ within organs, on part of the lines; also absent: GPR35, ATP2C2, EPHB6; co-absent with the target |
| [[SLC5A1]] | C | LYPD6B activity raises SLC5A1's level | lines that do not express LYPD6B (23) vs lines expressing it (27) | 2.15× lower at baseline in the lines without LYPD6B | 0.049 | ⚠ within organs, on part of the lines; also absent: GPR35, ATP2C2, EPHB6; co-absent with the target |
| [[SLC12A8]] | C | LYPD6B activity raises SLC12A8's level | lines that do not express LYPD6B (23) vs lines expressing it (27) | 2.76× lower at baseline in the lines without LYPD6B | 0.051 | ⚠ within organs, on part of the lines; also absent: GPR35, ATP2C2, EPHB6; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.372). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.5, 48.6); signed map (55.5, -5.7). **Vector** length 72.7, 17.9% of its response variance represented; |z| ≥ 3 in 803 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +16.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | +1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +4.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.3 | +4.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +5.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.1 | +0.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -11.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -10.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.0 | -9.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.7 | -12.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.0 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | LY6/PLAUR domain containing 6B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q23.2 — chr2:149,038,107-149,215,262 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CT116, LYPD7 |
| Gene groups (HGNC) | LY6/PLAUR domain containing |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NI32](https://www.uniprot.org/uniprotkb/Q8NI32) (Ly6/PLAUR domain-containing protein 6B):

> Likely acts as a modulator of nicotinic acetylcholine receptors (nAChRs) activity. In vitro acts on nAChRs in a subtype- and stoichiometry-dependent manner. Modulates specifically alpha-3(3):beta-4(2) nAChRs by enhancing the sensitivity to ACh, decreasing ACh-induced maximal current response and increasing the rate of desensitization to ACh; has no effect on alpha-7 homomeric nAChRs; modulates alpha-3(2):alpha-5:beta-4(2) nAChRs in the context of CHRNA5/alpha-5 variant Asn-398 but not its …

**Summary**, from NCBI Gene [130576](https://www.ncbi.nlm.nih.gov/gene/130576):

> Enables acetylcholine receptor regulator activity. Predicted to be located in extracellular region and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27018](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27018) · Entrez [130576](https://www.ncbi.nlm.nih.gov/gene/130576) · UniProt [Q8NI32](https://www.uniprot.org/uniprotkb/Q8NI32) · Ensembl [ENSG00000150556](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150556)

## Data

Gene col 7444: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7444); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7444, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7444]; `tensor/DDL_lfc|DDL_z.npy` [7444]; `embed/gene_vectors.npy` [7444]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7444 or target_col == 7444). Every well: [[LYPD6B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LYPD6B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
