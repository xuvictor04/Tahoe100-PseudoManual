---
symbol: "RASEF"
type: "gene"
col: 9068
ensembl_id: "ENSG00000165105"
name: "RAS and EF-hand domain containing"
location: "9q21.32"
module: 66
arm: "+"
pooled_cpm: 47.06
n_lines_expressing: 30
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 26
direction_downstream: 46
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# RASEF

*RAS and EF-hand domain containing* — 9q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.02× (z +28.2, q 0e+00, up in 25 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.656× (z -7.4, q 6e-11, down in 18 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABLIM1]] (+0.63, fdr 7e-06), [[PTPRK]] (+0.63, fdr 9e-06), [[SEMA3E]] (+0.60, fdr 1e-05); moves opposite to [[SLC38A9]] (-0.60, fdr 1e-05), [[PMS2P3]] (-0.59, fdr 3e-05), [[STARD3]] (-0.59, fdr 1e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[ELF3-AS1]] → it (grade B ⚠); 46 go from it, the strongest it → [[ARAP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9068.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.02×** | +28.2 | 0e+00 | 25/28 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.23×** | +14.4 | 8e-45 | 26/28 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +12.2 | 3e-32 | 24/28 (SW1417, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.96×** | +11.7 | 3e-29 | 24/28 (A498, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +9.6 | 8e-20 | 21/28 (LS 180, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +8.9 | 6e-17 | 19/29 (SW1417, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.58×** | +8.3 | 9e-15 | 23/28 (A498, SK-MEL-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +6.7 | 1e-09 | 14/27 (LS 180, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +6.4 | 8e-09 | 16/27 (NCI-H1573, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +6.1 | 5e-08 | 6/28 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.9 | 2e-07 | 17/28 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.65×** | +4.7 | 1e-04 | 13/27 (SK-MEL-2, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +4.6 | 2e-04 | 7/25 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +4.5 | 3e-04 | 13/28 (LS 180, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.002 | 15/28 (LS 180, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.005 | 7/28 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.016 | 9/28 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.040 | 3/29 (J82, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.18× | +2.9 | 0.086 | 5/28 (C32, SW1417, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9068.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.656×** | -7.4 | 6e-11 | 18/28 (KATO III, BT-474, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.698×** | -6.5 | 2e-08 | 17/28 (KATO III, SW48, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.713×** | -6.1 | 2e-07 | 17/28 (KATO III, LS 180, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.794×** | -4.1 | 0.007 | 17/27 (BT-474, SW48, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.797×** | -4.0 | 0.008 | 6/28 (SNU-423, RPMI-7951, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.815×** | -3.6 | 0.030 | 11/28 (SNU-423, RPMI-7951, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.877× | -3.3 | 0.060 | 9/28 (SNU-423, Panc 03.27, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.831×** | -3.3 | 0.060 | 9/28 (SNU-423, A-172, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.839× | -3.2 | 0.099 | 8/28 (NCI-H1573, A-427, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | 0.844× | -3.1 | 0.12 | 3/28 (RPMI-7951, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9068. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 144 | 3 | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +14.8) | [[Panobinostat (drug)]] 5 µM 0.296× (z -10.8) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.288× (z -10.7) |
| [[LS 180 (line)]] | wt | 98.9 | 5 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +23.0) | [[Panobinostat (drug)]] 5 µM 0.291× (z -12.9) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.323× (z -11.5) |
| [[A498 (line)]] | wt | 71.7 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +27.3) | — |
| [[COLO 205 (line)]] | alt | 120 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.221× (z -10.5) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.287× (z -8.5) |
| [[HT-29 (line)]] | alt | 277 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -12.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.255× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 83.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +21.0) | — |
| [[A-172 (line)]] | wt | 15.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +21.7) | — |
| [[A549 (line)]] | wt | 74.3 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -9.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.308× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 38.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +27.0) | — |
| [[C32 (line)]] | wt | 13.1 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.85× (z +14.0) | [[Pyridoxine (drug)]] 0.5 µM 0.132× (z -9.2) |
| [[KATO III (line)]] | alt | 196 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -15.0) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.182× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 49.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +16.9) | — |
| [[NCI-H2347 (line)]] | alt | 84.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +15.7) | — |
| [[PANC-1 (line)]] | alt | 12.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +18.0) | — |
| [[SW 900 (line)]] | alt | 93.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -9.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[BT-474 (line)]] | alt | 161 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -12.6) |
| [[J82 (line)]] | alt | 13.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.25× (z +17.1) | — |
| [[SW1417 (line)]] | alt | 42.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.0) | — |
| [[A-427 (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -10.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 79.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -9.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 39.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.357× (z -8.6) ⚠ cell-cycle shift, explains ~24% of this change |
| [[NCI-H1792 (line)]] | alt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.20× (z +14.1) | — |
| [[Panc 03.27 (line)]] | alt | 67.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +13.6) | — |
| [[SW48 (line)]] | wt | 51.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.209× (z -10.0) |
| [[AN3 CA (line)]] | alt | 7.90 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.06 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.29 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.76 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.13 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.95 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.62 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.93 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.84 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.81 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.38 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.65 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.49 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.70 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9068), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABLIM1]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[PTPRK]] | +0.63 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[SEMA3E]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ARHGEF38]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ARAP2]] | +0.58 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[ARHGAP42]] | +0.57 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[GATA6]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[LYPD1]] | +0.57 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[LINC00857]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[JUN]] | +0.56 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[RASSF6]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[EXPH5]] | +0.55 | +0.60 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC38A9]] | -0.60 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[PMS2P3]] | -0.59 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[STARD3]] | -0.59 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | -0.56 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[RNF4]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ASB16-AS1]] | -0.55 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[UBOX5]] | -0.55 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[PGS1]] | -0.54 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[ZNF500]] | -0.54 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[ANKRD13D]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[HYKK]] | -0.53 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[WIPI2]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 14, C 12. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises RASEF's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 3.97× lower at baseline in the lines without ELF3-AS1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[LGALS3]] | B | LGALS3 activity raises RASEF's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 4.29× lower at baseline in the lines without LGALS3 | 0.011 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[SYTL2]] | B | SYTL2 activity raises RASEF's level | lines that do not express SYTL2 (7) vs lines expressing it (43) | 4.50× lower at baseline in the lines without SYTL2 | 0.016 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent |
| [[MAP7]] | B | MAP7 activity raises RASEF's level | lines that do not express MAP7 (21) vs lines expressing it (29) | 3.16× lower at baseline in the lines without MAP7 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: MST1R, ENTPD2, TC2N |
| [[SERTAD4]] | B | SERTAD4 activity raises RASEF's level | lines that do not express SERTAD4 (14) vs lines expressing it (36) | 2.22× lower at baseline in the lines without SERTAD4 | 0.034 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC |
| [[ATP1B1]] | B | ATP1B1 activity raises RASEF's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 4.47× lower at baseline in the lines without ATP1B1 | 0.034 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[LRATD2]] | B | LRATD2 activity raises RASEF's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 3.63× lower at baseline in the lines without LRATD2 | 0.045 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[ARAP2]] | B | ARAP2 activity raises RASEF's level | lines that do not express ARAP2 (10) vs lines expressing it (40) | 4.14× lower at baseline in the lines without ARAP2 | 0.050 | ⚠ within organs, on part of the lines; also absent: RAPGEF5 |
| [[GATA6]] | B | GATA6 activity raises RASEF's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 2.83× lower at baseline in the lines without GATA6 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[PTPRK]] | B | PTPRK activity raises RASEF's level | lines that do not express PTPRK (6) vs lines expressing it (44) | 4.85× lower at baseline in the lines without PTPRK | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000246225, EPS8, ASPH |
| [[HDAC6]] | B | HDAC6 activity raises RASEF's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[KLF4]] | B | KLF4 activity raises RASEF's level | lines that do not express KLF4 (6) vs lines expressing it (44) | 3.76× lower at baseline in the lines without KLF4 | 0.071 | ⚠ within organs, on part of the lines; also absent: APOL6, LGALS3BP, TNS3; maybe low, not absent |

### Downstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 36, C 10. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARAP2]] | B | RASEF activity raises ARAP2's level | lines that do not express RASEF (20) vs lines expressing it (30) | 3.25× lower at baseline in the lines without RASEF | 0.002 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[SERTAD4]] | B | RASEF activity raises SERTAD4's level | lines that do not express RASEF (20) vs lines expressing it (30) | 1.79× lower at baseline in the lines without RASEF | 0.003 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[EXPH5]] | B | RASEF activity raises EXPH5's level | lines that do not express RASEF (20) vs lines expressing it (30) | 2.74× lower at baseline in the lines without RASEF | 0.005 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[LGALS3]] | B | RASEF activity raises LGALS3's level | lines that do not express RASEF (20) vs lines expressing it (30) | 2.50× lower at baseline in the lines without RASEF | 0.006 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[RBM47]] | B | RASEF activity raises RBM47's level | lines that do not express RASEF (20) vs lines expressing it (30) | 3.56× lower at baseline in the lines without RASEF | 0.007 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[RNF103-CHMP3]] | B | RASEF activity raises RNF103-CHMP3's level | lines that do not express RASEF (20) vs lines expressing it (30) | 2.19× lower at baseline in the lines without RASEF | 0.007 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[LITAF]] | B | RASEF activity raises LITAF's level | lines that do not express RASEF (20) vs lines expressing it (30) | 2.09× lower at baseline in the lines without RASEF | 0.007 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[ATP1B1]] | B | RASEF activity raises ATP1B1's level | lines that do not express RASEF (20) vs lines expressing it (30) | 2.70× lower at baseline in the lines without RASEF | 0.008 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[ARHGAP42]] | B | RASEF activity raises ARHGAP42's level | lines that do not express RASEF (20) vs lines expressing it (30) | 2.60× lower at baseline in the lines without RASEF | 0.009 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[ELF3-AS1]] | B | RASEF activity raises ELF3-AS1's level | lines that do not express RASEF (20) vs lines expressing it (30) | 2.35× lower at baseline in the lines without RASEF | 0.011 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[PTPRK]] | B | RASEF activity raises PTPRK's level | lines that do not express RASEF (20) vs lines expressing it (30) | 2.23× lower at baseline in the lines without RASEF | 0.011 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[ZNF165]] | B | RASEF activity raises ZNF165's level | lines that do not express RASEF (20) vs lines expressing it (30) | 2.40× lower at baseline in the lines without RASEF | 0.013 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.351). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.4, 13.9); signed map (46.9, 14.8). **Vector** length 100, 29.8% of its response variance represented; |z| ≥ 3 in 775 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +12.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.3 | +11.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +28.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +14.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +1.5 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | -7.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.7 | -6.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -2.6 | -6.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -4.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.0 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | RAS and EF-hand domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.32 — chr9:82,979,590-83,063,177 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31614, TSG; previously RAB45 |
| Gene groups (HGNC) | RAB, member RAS oncogene GTPases; EF-hand domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZ41](https://www.uniprot.org/uniprotkb/Q8IZ41) (Ras and EF-hand domain-containing protein):

> [Isoform 1]: Rab GTPase that acts as a dynein adapter protein, thereby activating dynein-mediated transport and dynein-dynactin motility on microtubules. RASEF-mediated dynein motility is Ca(2+)-independent. Also regulates the formation and sorting of zymogen granules and secretion of digestive enzymes by pancreatic acinar cells (By similarity).

**Summary**, from NCBI Gene [158158](https://www.ncbi.nlm.nih.gov/gene/158158):

> This gene is a member of the Rab family of GTPases that are involved in regulation of membrane traffic. The encoded protein contains an N-terminal EF-hand domain, a coiled-coil motif and a C-terminal Rab domain. A potential role as tumor suppressor has been indicated for this gene. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:26464](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26464) · Entrez [158158](https://www.ncbi.nlm.nih.gov/gene/158158) · UniProt [Q8IZ41](https://www.uniprot.org/uniprotkb/Q8IZ41) · Ensembl [ENSG00000165105](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165105)

## Data

Gene col 9068: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9068); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9068, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9068]; `tensor/DDL_lfc|DDL_z.npy` [9068]; `embed/gene_vectors.npy` [9068]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9068 or target_col == 9068). Every well: [[RASEF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASEF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
