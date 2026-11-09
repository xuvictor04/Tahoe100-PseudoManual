---
symbol: "BCL2L1"
type: "gene"
col: 10129
ensembl_id: "ENSG00000171552"
name: "BCL2 like 1"
location: "20q11.21"
module: 147
arm: "+"
pooled_cpm: 228.41
n_lines_expressing: 44
n_dd_up: 18
n_dd_down: 31
n_dd_up_clean: 18
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 19
direction_downstream: 16
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# BCL2L1

*BCL2 like 1* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.34× (z +6.5, q 6e-08, up in 32 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.322× (z -16.4, q 0e+00, down in 42 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCL2L1-AS1]] (+0.70, fdr 7e-06, ⚠ same locus), [[BCAR3]] (+0.67, fdr 7e-06), [[MYEOV]] (+0.63, fdr 7e-06), [[CASC19]] (+0.63, fdr 7e-06); moves opposite to [[MAP3K2]] (-0.52, fdr 5e-05), [[NMB]] (-0.51, fdr 3e-05), [[TMEM167B]] (-0.51, fdr 2e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[ITGB4]] → it (grade B ⚠); 16 go from it, the strongest it → [[SLC16A5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, none with an alert; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10129.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.34×** | +6.5 | 6e-08 | 32/43 (A498, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.55×** | +6.3 | 6e-08 | 26/42 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.51×** | +6.0 | 5e-07 | 27/42 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.39×** | +4.8 | 2e-04 | 24/42 (HS-578T, SNU-423, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.39×** | +4.8 | 2e-04 | 21/42 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.38×** | +4.7 | 3e-04 | 21/42 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.37×** | +4.5 | 5e-04 | 21/42 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.36×** | +4.4 | 7e-04 | 23/42 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.35×** | +4.4 | 7e-04 | 22/42 (HOP62, SNU-423, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.76×** | +4.3 | 0.001 | 26/42 (A-172, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.004 | 21/42 (HS-578T, HOP62, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.009 | 24/41 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.012 | 18/43 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.020 | 21/42 (HS-578T, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.26×** | +3.4 | 0.026 | 19/42 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10129.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.322×** | -16.4 | 0e+00 | 42/42 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.485×** | -14.8 | 0e+00 | 38/43 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.373×** | -14.2 | 1e-43 | 40/42 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.507×** | -13.9 | 2e-41 | 32/42 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.485×** | -10.5 | 2e-23 | 38/42 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.529×** | -8.9 | 8e-17 | 33/42 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.550×** | -8.3 | 9e-15 | 34/44 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.585×** | -7.8 | 6e-13 | 37/43 (MIA PaCa-2, HEC-1-A, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.623×** | -6.6 | 3e-09 | 31/41 (J82, A-172, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.678×** | -6.4 | 8e-09 | 34/43 (MIA PaCa-2, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.699×** | -6.4 | 8e-09 | 32/42 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.689×** | -6.4 | 8e-09 | 34/44 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.646×** | -6.3 | 1e-08 | 29/42 (J82, KATO III, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.661×** | -6.0 | 9e-08 | 32/42 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.662×** | -5.9 | 1e-07 | 28/42 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.653×** | -5.9 | 1e-07 | 33/42 (J82, A-172, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10129. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 326 | 0 | 20 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -32.4) |
| [[SW48 (line)]] | wt | 450 | 0 | 19 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0655× (z -22.5) |
| [[MIA PaCa-2 (line)]] | alt | 168 | 1 | 15 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 11.0× (z +13.3) | [[Adagrasib (drug)]] 0.05 µM 0.492× (z -26.9) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -18.8) |
| [[KATO III (line)]] | alt | 626 | 0 | 15 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -28.9) |
| [[SW480 (line)]] | alt | 454 | 1 | 13 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.92× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -24.8) |
| [[HS-578T (line)]] | alt | 66.9 | 13 | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 3.47× (z +10.3) | — |
| [[RKO (line)]] | wt | 217 | 5 (2 ⚠) | 8 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 2.79× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.97× (z +10.3) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -15.1) |
| [[A-172 (line)]] | wt | 265 | 2 | 10 | [[TAK-901 (drug)]] 5 µM 7.77× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.170× (z -21.4) |
| [[HOP62 (line)]] | alt | 70.9 | 12 | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 3.79× (z +11.0) | — |
| [[LS 180 (line)]] | wt | 230 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -22.2) |
| [[J82 (line)]] | alt | 269 | 0 | 11 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -14.0) |
| [[A549 (line)]] | wt | 364 | 1 | 8 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.62× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -26.8) |
| [[AsPC-1 (line)]] | alt | 373 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -21.6) |
| [[HEC-1-A (line)]] | alt | 260 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -22.0) |
| [[SW1417 (line)]] | alt | 908 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -25.2) |
| [[CFPAC-1 (line)]] | alt | 477 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -25.9) |
| [[COLO 205 (line)]] | alt | 275 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0663× (z -23.9) |
| [[SNU-423 (line)]] | alt | 75.9 | 8 | 0 | [[Dexamethasone (drug)]] 0.5 µM 3.42× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 425 | 0 | 7 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -19.8) |
| [[NCI-H2347 (line)]] | alt | 200 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -15.3) |
| [[NCI-H460 (line)]] | wt | 65.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 177 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 272 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -13.4) |
| [[A498 (line)]] | wt | 109 | 3 | 2 | [[TAK-901 (drug)]] 5 µM 19.0× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.310× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 434 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -14.7) |
| [[A-427 (line)]] | wt | 92.5 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 8.98× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.318× (z -13.3) |
| [[HCT15 (line)]] | alt | 162 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -11.5) |
| [[Hs 766T (line)]] | wt | 534 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -16.3) |
| [[PANC-1 (line)]] | alt | 192 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 10.3× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.329× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 96.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -18.7) |
| [[BT-474 (line)]] | alt | 129 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 89.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 58.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -18.5) |
| [[RPMI-7951 (line)]] | alt | 65.6 | 1 | 0 | [[Dexamethasone (drug)]] 0.5 µM 2.83× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 64.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.311× (z -9.7) |
| [[SNU-1 (line)]] | wt | 99.4 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -10.2) |
| [[AN3 CA (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 49.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 42.2 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 47.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.1 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 45.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 66.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10129), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL2L1-AS1]] | +0.70 | +0.70 / +0.71 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[BCAR3]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[MYEOV]] | +0.63 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[CASC19]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[EFNB2]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[ASAP2]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[GJB3]] | +0.61 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[ELK3]] | +0.61 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[TNS4]] | +0.60 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[LINC02320]] | +0.60 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[PANX1]] | +0.60 | +0.62 / +0.57 | both halves | 8e-06 | pathway: Inflammasomes |
| [[ITGB4]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[THSD4]] | +0.59 | +0.59 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K2]] | -0.52 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[NMB]] | -0.51 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[TMEM167B]] | -0.51 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[SLC41A2]] | -0.50 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[ANKMY2]] | -0.50 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[SIRLNT]] | -0.49 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[ZSCAN31]] | -0.49 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[MPC2]] | -0.48 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[MAF]] | -0.48 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[TENT5A]] | -0.48 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[MEF2C-AS1]] | -0.48 | -0.50 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 18, C 1. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB4]] | B | ITGB4 activity raises BCL2L1's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 3.29× lower at baseline in the lines without ITGB4 | 0.001 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[TNS4]] | B | TNS4 activity raises BCL2L1's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 3.12× lower at baseline in the lines without TNS4 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[B3GNT3]] | B | B3GNT3 activity raises BCL2L1's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.89× lower at baseline in the lines without B3GNT3 | 0.004 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[PKP2]] | B | PKP2 activity raises BCL2L1's level | lines that do not express PKP2 (16) vs lines expressing it (34) | 2.98× lower at baseline in the lines without PKP2 | 0.005 | ⚠ within organs, on part of the lines; also absent: EPHA2-AS1, EPS8L2, OCLN |
| [[CASC19]] | B | CASC19 activity raises BCL2L1's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 3.12× lower at baseline in the lines without CASC19 | 0.007 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4 |
| [[GJB3]] | B | GJB3 activity raises BCL2L1's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 3.16× lower at baseline in the lines without GJB3 | 0.014 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[SH2D3A]] | B | SH2D3A activity raises BCL2L1's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 2.39× lower at baseline in the lines without SH2D3A | 0.015 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[NR3C1]] | B | NR3C1 activity raises BCL2L1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.8% of all compounds | 0.028 | ⚠ off-target possible; 3 compounds |
| [[SLC16A5]] | B | SLC16A5 activity raises BCL2L1's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 2.33× lower at baseline in the lines without SLC16A5 | 0.028 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |
| [[MST1R]] | B | MST1R activity raises BCL2L1's level | lines that do not express MST1R (24) vs lines expressing it (26) | 2.55× lower at baseline in the lines without MST1R | 0.041 | ⚠ within organs, on part of the lines; also absent: SLC52A3, SPINT1, MAP7 |
| [[ZBED2]] | B | ZBED2 activity raises BCL2L1's level | lines that do not express ZBED2 (39) vs lines expressing it (11) | 2.85× lower at baseline in the lines without ZBED2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPON1, ENSG00000289850, KLK11 |
| [[ZNF860]] | B | ZNF860 activity raises BCL2L1's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 2.19× lower at baseline in the lines without ZNF860 | 0.046 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 15, C 1. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC16A5]] | B | BCL2L1 activity raises SLC16A5's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 3.10× lower at baseline in the lines without BCL2L1 | 0.028 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |
| [[MYL12B]] | B | BCL2L1 activity raises MYL12B's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 2.26× lower at baseline in the lines without BCL2L1 | 0.039 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |
| [[ITGB4]] | B | BCL2L1 activity raises ITGB4's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 4.17× lower at baseline in the lines without BCL2L1 | 0.043 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |
| [[MEF2C-AS1]] | B | BCL2L1 activity lowers MEF2C-AS1's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 3.83× higher at baseline in the lines without BCL2L1 | 0.043 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |
| [[SPRED1]] | B | BCL2L1 activity lowers SPRED1's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 1.46× higher at baseline in the lines without BCL2L1 | 0.052 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |
| [[ASAP2]] | B | BCL2L1 activity raises ASAP2's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 2.38× lower at baseline in the lines without BCL2L1 | 0.057 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |
| [[KPNA2P3]] | B | BCL2L1 activity raises KPNA2P3's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 1.63× lower at baseline in the lines without BCL2L1 | 0.062 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |
| [[NTSR1]] | B | BCL2L1 activity raises NTSR1's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 2.97× lower at baseline in the lines without BCL2L1 | 0.069 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |
| [[RAP1GAP2]] | B | BCL2L1 activity strengthens RAP1GAP2's drug response | lines that do not express BCL2L1 (5) vs lines expressing it (40) | the lines without BCL2L1 respond 0.56× as strongly (z diff +1.25); strongest at Homoharringtonine 5 µM: 1.20x vs 0.51x (z diff +7.2) | 0.070 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[BCAR3]] | B | BCL2L1 activity raises BCAR3's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 2.04× lower at baseline in the lines without BCL2L1 | 0.071 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |
| [[VASP]] | B | BCL2L1 activity raises VASP's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 1.85× lower at baseline in the lines without BCL2L1 | 0.073 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |
| [[PDE9A]] | B | BCL2L1 activity raises PDE9A's level | lines that do not express BCL2L1 (6) vs lines expressing it (44) | 2.06× lower at baseline in the lines without BCL2L1 | 0.085 | ⚠ within organs, on part of the lines; also absent: AMOTL2, RASSF7, CTSH; maybe low, not absent |

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.550). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.6, 7.5); signed map (8.1, 36.1). **Vector** length 142, 52.9% of its response variance represented; |z| ≥ 3 in 1,914 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.5 | +6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.1 | +4.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +6.3 | +6.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +6.3 | +6.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.5 | +4.5 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | +5.3 | +4.8 |
| fall | [[Cobimetinib (drug)]] 5 µM |  | -8.3 | -6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.5 | -7.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.2 | -6.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -7.0 | -6.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -6.8 | -6.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.7 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21 — chr20:31,664,452-31,723,989 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BCLX, BCL2L, Bcl-X, bcl-xL, bcl-xS, PPP1R52 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; BCL2 family |
| Hallmark sets | APOPTOSIS, IL2_STAT5_SIGNALING |
| Reactome | 29 pathways, smallest: The NLRP1 inflammasome; STAT5 activation downstream of FLT3 ITD mutants; BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07817](https://www.uniprot.org/uniprotkb/Q07817) (Bcl-2-like protein 1):

> Potent inhibitor of cell death. Inhibits activation of caspases. Appears to regulate cell death by blocking the voltage-dependent anion channel (VDAC) by binding to it and preventing the release of the caspase activator, CYC1, from the mitochondrial membrane. Also acts as a regulator of G2 checkpoint and progression to cytokinesis during mitosis.; Isoform Bcl-X(L) also regulates presynaptic plasticity, including neurotransmitter release and recovery, number of axonal mitochondria as well as …

**Summary**, from NCBI Gene [598](https://www.ncbi.nlm.nih.gov/gene/598):

> The protein encoded by this gene belongs to the BCL-2 protein family. BCL-2 family members form hetero- or homodimers and act as anti- or pro-apoptotic regulators that are involved in a wide variety of cellular activities. The proteins encoded by this gene are located at the outer mitochondrial membrane, and have been shown to regulate outer mitochondrial membrane channel (VDAC) opening. VDAC regulates mitochondrial membrane potential, and thus controls the production of reactive oxygen species …

**Accessions** — [HGNC:992](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:992) · Entrez [598](https://www.ncbi.nlm.nih.gov/gene/598) · UniProt [Q07817](https://www.uniprot.org/uniprotkb/Q07817) · Ensembl [ENSG00000171552](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171552)

## Data

Gene col 10129: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10129); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10129, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10129]; `tensor/DDL_lfc|DDL_z.npy` [10129]; `embed/gene_vectors.npy` [10129]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10129 or target_col == 10129). Every well: [[BCL2L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL2L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
