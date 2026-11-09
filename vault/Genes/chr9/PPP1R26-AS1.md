---
symbol: "PPP1R26-AS1"
type: "gene"
col: 13452
ensembl_id: "ENSG00000225361"
name: "PPP1R26 antisense RNA 1"
location: "9q34.3"
module: 15
arm: "+"
pooled_cpm: 14.33
n_lines_expressing: 47
n_dd_up: 11
n_dd_down: 24
n_dd_up_clean: 10
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# PPP1R26-AS1

*PPP1R26 antisense RNA 1* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.23× (z +13.9, q 3e-41, up in 35 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.236× (z -17.7, q 0e+00, down in 43 of 44 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPN9]] (+0.68, fdr 7e-06), [[GLUD1P3]] (+0.67, fdr 1e-05), [[TIRAP]] (+0.67, fdr 5e-05); moves opposite to [[AMOT]] (-0.58, fdr 3e-05), [[LMCD1]] (-0.58, fdr 3e-05), [[POLR2E]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13452.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +13.9 | 3e-41 | 35/41 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +6.8 | 2e-09 | 27/43 (SW1417, HEC-1-A, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 0.002 | 14/43 (LoVo, KATO III, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.021 | 11/44 (LoVo, KATO III, …) | two highest doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.021 | 6/43 (HepG2/C3A, NCI-H2347, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.042 | 10/43 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.3 | 0.065 | 8/43 (LoVo, SNU-423, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.065 | 6/43 (C32, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.086 | 6/43 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.092 | 13/42 (A498, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sodium Salicylate (drug)]] 5 µM |  | 1.20× | +3.1 | 0.092 | 9/45 (Hs 766T, HEC-1-A, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.100 | 7/41 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13452.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.236×** | -17.7 | 0e+00 | 43/44 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.369×** | -17.3 | 0e+00 | 35/42 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.286×** | -15.4 | 0e+00 | 41/43 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.309×** | -13.9 | 1e-41 | 38/43 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.344×** | -13.1 | 3e-37 | 40/44 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.346×** | -13.0 | 7e-37 | 40/44 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.459×** | -9.6 | 1e-19 | 28/40 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.462×** | -9.5 | 2e-19 | 32/42 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.525×** | -7.9 | 2e-13 | 26/43 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.304×** | -7.6 | 1e-12 | 30/44 (MIA PaCa-2, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.591×** | -6.2 | 3e-08 | 24/38 (SNU-423, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.610×** | -6.1 | 6e-08 | 29/44 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.626×** | -5.7 | 4e-07 | 26/44 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.627×** | -5.7 | 4e-07 | 27/44 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.434×** | -5.4 | 3e-06 | 21/40 (HEC-1-A, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.758×** | -4.8 | 5e-05 | 25/44 (HEC-1-A, Panc 03.27, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.691×** | -4.3 | 6e-04 | 16/44 (A-172, SK-MEL-2, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.532×** | -4.1 | 0.002 | 15/44 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.735×** | -3.8 | 0.005 | 19/43 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13452. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 23.3 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0871× (z -21.5) |
| [[HEC-1-A (line)]] | alt | 42.1 | 1 | 10 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.96× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -17.5) |
| [[A-172 (line)]] | wt | 28.8 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0819× (z -18.3) |
| [[HOP62 (line)]] | alt | 20.7 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0820× (z -14.0) |
| [[SW480 (line)]] | alt | 16.9 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0806× (z -19.1) |
| [[A498 (line)]] | wt | 11.5 | 2 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.56× (z +16.7) | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -15.4) |
| [[MIA PaCa-2 (line)]] | alt | 59.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0323× (z -30.8) |
| [[NCI-H23 (line)]] | alt | 9.84 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -15.2) |
| [[Panc 03.27 (line)]] | alt | 21.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -11.9) |
| [[A549 (line)]] | wt | 7.13 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.88× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -12.4) |
| [[BT-474 (line)]] | alt | 20.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.0886× (z -13.5) |
| [[CFPAC-1 (line)]] | alt | 8.22 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -9.8) |
| [[COLO 205 (line)]] | alt | 7.44 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0354× (z -11.3) |
| [[J82 (line)]] | alt | 22.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.195× (z -10.4) |
| [[LS 180 (line)]] | wt | 23.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -10.8) |
| [[SHP-77 (line)]] | alt | 13.2 | 0 | 2 | — | [[Pemigatinib (drug)]] 0.05 µM 0.0708× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 11.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -11.3) |
| [[SW1417 (line)]] | alt | 19.8 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.86× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -11.4) |
| [[C-33 A (line)]] | alt | 11.4 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0610× (z -9.4) |
| [[C32 (line)]] | wt | 7.83 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0399× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 7.64 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0360× (z -10.9) |
| [[KATO III (line)]] | alt | 10.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -9.9) |
| [[LoVo (line)]] | wt | 9.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 8.80 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0505× (z -12.2) |
| [[NCI-H2347 (line)]] | alt | 6.14 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -12.1) |
| [[PANC-1 (line)]] | alt | 5.13 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -10.4) |
| [[SNU-423 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.120× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~35% of this change |
| [[SW48 (line)]] | wt | 12.9 | 0 | 1 | — | [[Thymopentin (drug)]] 0.05 µM 0.0654× (z -8.9) |
| [[A-427 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13452), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPN9]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[GLUD1P3]] | +0.67 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[TIRAP]] | +0.67 | +0.40 / +0.67 | both halves | 5e-05 |  |
| [[EIF4ENIF1]] | +0.65 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[ZNF529-AS1]] | +0.64 | +0.48 / +0.61 | both halves | 2e-05 | same gene group |
| [[TMEM11-DT]] | +0.64 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[PEX6]] | +0.64 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CTC-338M12.4]] | +0.64 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[MIR762HG]] | +0.63 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[GATD1-DT]] | +0.63 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[NUDT16-DT]] | +0.63 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[ZNF778]] | +0.61 | +0.37 / +0.67 | both halves | 7e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AMOT]] | -0.58 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[LMCD1]] | -0.58 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[POLR2E]] | -0.58 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[GDE1]] | -0.55 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[C4orf33]] | -0.53 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[PPP1CC]] | -0.53 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[PRDX2]] | -0.53 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[LIMA1]] | -0.52 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[TIPARP]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[SEMA3C]] | -0.52 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[EFR3A]] | -0.52 | -0.32 / -0.60 | both halves | 2e-04 |  |
| [[DMXL2]] | -0.51 | -0.36 / -0.61 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.696). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.3, 21.6); signed map (3.8, -1.1). **Vector** length 97.5, 23.8% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.4 | +13.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.9 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +2.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.2 | +2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +1.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +0.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.6 | +3.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | +2.4 | +3.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -13.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.1 | -15.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.1 | -17.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -1.6 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | PPP1R26 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9q34.3 — chr9:135,462,727-135,480,777 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48717) · Entrez [100506599](https://www.ncbi.nlm.nih.gov/gene/100506599) · Ensembl [ENSG00000225361](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225361)

## Data

Gene col 13452: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13452); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13452, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13452]; `tensor/DDL_lfc|DDL_z.npy` [13452]; `embed/gene_vectors.npy` [13452]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13452 or target_col == 13452). Every well: [[PPP1R26-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R26-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
