---
symbol: "SOX13"
type: "gene"
col: 6812
ensembl_id: "ENSG00000143842"
name: "SRY-box transcription factor 13"
location: "1q32.1"
module: 162
arm: "+"
pooled_cpm: 37.09
n_lines_expressing: 46
n_dd_up: 10
n_dd_down: 31
n_dd_up_clean: 10
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 18
direction_downstream: 3
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# SOX13

*SRY-box transcription factor 13* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.45× (z +8.6, q 4e-15, up in 30 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.455× (z -12.8, q 7e-35, down in 27 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.620× (z -7.8, q 9e-13, down in 30 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRE5]] (+0.68, fdr 7e-06), [[EPHB3]] (+0.64, fdr 1e-04), [[SEMA3F]] (+0.63, fdr 1e-05); moves opposite to [[HTATIP2]] (-0.54, fdr 3e-05), [[ZRANB2-DT]] (-0.54, fdr 2e-05), [[SPAG16]] (-0.52, fdr 5e-05).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[TINAGL1]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Daptomycin (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6812.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +8.6 | 4e-15 | 30/44 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +7.0 | 1e-09 | 31/43 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +6.7 | 3e-09 | 24/43 (A498, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +6.0 | 4e-07 | 22/43 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +5.4 | 6e-06 | 3/45 (COLO 205, NCI-H1573, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +5.3 | 1e-05 | 24/43 (RKO, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +5.2 | 1e-05 | 24/44 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.66×** | +4.3 | 0.001 | 14/41 (HOP62, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.006 | 14/43 (HS-578T, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.007 | 16/44 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.023 | 11/44 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~3% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6812.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.455×** | -12.8 | 7e-35 | 27/35 (C32, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.546×** | -9.1 | 2e-17 | 27/35 (Panc 03.27, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.561×** | -9.1 | 2e-17 | 24/31 (C32, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.620×** | -7.8 | 9e-13 | 30/44 (SW 900, NCI-H23, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.657×** | -6.8 | 9e-10 | 27/43 (C32, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.669×** | -6.5 | 5e-09 | 27/44 (A-172, LoVo, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.686×** | -6.1 | 6e-08 | 24/43 (HT-29, NCI-H23, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.767×** | -6.1 | 6e-08 | 22/42 (C32, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.707×** | -5.4 | 3e-06 | 21/43 (LoVo, NCI-H2347, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.724×** | -4.9 | 6e-05 | 20/44 (LoVo, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.745×** | -4.8 | 8e-05 | 20/45 (LoVo, AsPC-1, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.751×** | -4.7 | 1e-04 | 18/43 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.584×** | -4.6 | 2e-04 | 18/41 (LoVo, NCI-H460, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.768×** | -4.1 | 0.001 | 17/42 (C32, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.835× | -4.1 | 0.001 | 19/44 (LoVo, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.800×** | -4.1 | 0.002 | 19/44 (LoVo, CHP-212, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.773×** | -4.0 | 0.002 | 16/43 (AsPC-1, LoVo, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.789×** | -3.9 | 0.004 | 13/44 (SK-MEL-2, HEC-1-A, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.651×** | -3.7 | 0.008 | 14/41 (HCT15, KATO III, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6812. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 257 | 1 | 8 (4 ⚠) | [[Belumosudil (drug)]] 5 µM 2.36× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0907× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -16.3) |
| [[Hs 766T (line)]] | wt | 197 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.208× (z -13.1) |
| [[SW480 (line)]] | alt | 67.9 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 61.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0474× (z -23.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 45.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0997× (z -18.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 24.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -12.1) |
| [[A-172 (line)]] | wt | 26.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.0955× (z -17.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 21.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -9.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 38.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -10.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 33.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +11.7) | — |
| [[KATO III (line)]] | alt | 45.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -9.4) |
| [[LoVo (line)]] | wt | 42.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -10.6) ⚠ cell-cycle shift, explains ~61% of this change |
| [[MIA PaCa-2 (line)]] | alt | 37.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -8.8) |
| [[PANC-1 (line)]] | alt | 18.4 | 1 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.60× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -11.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -9.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -11.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.231× (z -9.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 31.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.243× (z -9.9) |
| [[LS 180 (line)]] | wt | 46.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.302× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0877× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.107× (z -12.5) ⚠ toxic; cell-cycle shift, explains ~19% of this change |
| [[NCI-H23 (line)]] | alt | 20.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.212× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 31.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -11.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 20.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +11.1) | — |
| [[SW 900 (line)]] | alt | 35.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.259× (z -8.9) |
| [[SW1417 (line)]] | alt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -12.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.89 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.56 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.05 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6812), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRE5]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[EPHB3]] | +0.64 | +0.34 / +0.67 | both halves | 1e-04 |  |
| [[SEMA3F]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[HIVEP3]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[TLE3]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 | pathway: Deactivation of the beta-catenin transactivating complex |
| [[NECTIN1]] | +0.61 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[PLK3]] | +0.61 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[EPHA2]] | +0.60 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[DUSP6]] | +0.60 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[TINAGL1]] | +0.60 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[MYEOV]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[ETV4]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HTATIP2]] | -0.54 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[ZRANB2-DT]] | -0.54 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[SPAG16]] | -0.52 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[CSDE1]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[ZFR]] | -0.49 | -0.44 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 17, C 1. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TINAGL1]] | B | TINAGL1 activity raises SOX13's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.90× lower at baseline in the lines without TINAGL1 | 0.002 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[CEACAM1]] | B | CEACAM1 activity raises SOX13's level | lines that do not express CEACAM1 (27) vs lines expressing it (23) | 2.23× lower at baseline in the lines without CEACAM1 | 0.009 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[SH3TC2-DT]] | B | SH3TC2-DT activity raises SOX13's level | lines that do not express SH3TC2-DT (24) vs lines expressing it (26) | 1.85× lower at baseline in the lines without SH3TC2-DT | 0.010 | ⚠ within organs, on part of the lines; also absent: SH3TC2, LHX1-DT, MT1G |
| [[PCDH1]] | B | PCDH1 activity raises SOX13's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.20× lower at baseline in the lines without PCDH1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[MAP2K1]] | B | MAP2K1 activity raises SOX13's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.2% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds |
| [[SHH]] | B | SHH activity raises SOX13's level | lines that do not express SHH (29) vs lines expressing it (21) | 1.75× lower at baseline in the lines without SHH | 0.038 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[LYPD3]] | B | LYPD3 activity raises SOX13's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 1.84× lower at baseline in the lines without LYPD3 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[WNT7A]] | B | WNT7A activity raises SOX13's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 1.80× lower at baseline in the lines without WNT7A | 0.044 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[PRAG1]] | B | PRAG1 activity raises SOX13's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 1.56× lower at baseline in the lines without PRAG1 | 0.064 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[PRSS3]] | B | PRSS3 activity raises SOX13's level | lines that do not express PRSS3 (30) vs lines expressing it (20) | 1.71× lower at baseline in the lines without PRSS3 | 0.074 | ⚠ within organs, on part of the lines; also absent: IL20RA, ABO, EDAR |
| [[EPHB3]] | B | EPHB3 activity raises SOX13's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.54× lower at baseline in the lines without EPHB3 | 0.076 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SOX13's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Daptomycin (drug)]] 5 µM | C | SOX13 activity raises the cells' numbers under Daptomycin 5 µM (protects the cells) | lines that do not express SOX13 (4) vs lines expressing it (44) | the lines without SOX13: 0.70× the cells of the other lines | 0.033 | ⚠ few lines (4 vs 46); across organs; also absent: KIAA1671, TRIM47, FZD5; maybe low, not absent; cell counts less trustworthy |
| [[CD58]] | C | SOX13 activity raises CD58's level | lines that do not express SOX13 (4) vs lines expressing it (46) | 1.99× lower at baseline in the lines without SOX13 | 0.057 | ⚠ few lines (4 vs 46); across organs; also absent: KIAA1671, TRIM47, FZD5; maybe low, not absent |
| [[BAIAP2L1]] | C | SOX13 activity raises BAIAP2L1's level | lines that do not express SOX13 (4) vs lines expressing it (46) | 3.28× lower at baseline in the lines without SOX13 | 0.080 | ⚠ few lines (4 vs 46); across organs; also absent: KIAA1671, TRIM47, FZD5; maybe low, not absent |

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.741). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.8, 48.9); signed map (0.0, 40.9). **Vector** length 114, 29.5% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +8.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.3 | +5.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.0 | +7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.9 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +1.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +4.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +2.2 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.0 | -9.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.0 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.8 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.8 | -4.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.8 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.8 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.8 | -7.8 |

## What is on record

|  |  |
|---|---|
| Name | SRY-box transcription factor 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:204,073,115-204,127,743 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Sox-13, ICA12, MGC117216 |
| Gene groups (HGNC) | SRY-box transcription factors |
| Reactome | 3 pathways, smallest: Deactivation of the beta-catenin transactivating complex; TCF dependent signaling in response to WNT; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UN79](https://www.uniprot.org/uniprotkb/Q9UN79) (Transcription factor SOX-13):

> Transcription factor that binds to DNA at the consensus sequence 5'-AACAAT-3'. Binds to the proximal promoter region of the myelin protein MPZ gene, and may thereby be involved in the differentiation of oligodendroglia in the developing spinal tube (By similarity). Binds to the gene promoter of MBP and acts as a transcriptional repressor (By similarity). Binds to and modifies the activity of TCF7/TCF1, thereby inhibiting transcription and modulates normal gamma-delta T-cell development and …

**Summary**, from NCBI Gene [9580](https://www.ncbi.nlm.nih.gov/gene/9580):

> This gene encodes a member of the SOX (SRY-related HMG-box) family of transcription factors involved in the regulation of embryonic development and in the determination of cell fate. The encoded protein may act as a transcriptional regulator after forming a protein complex with other proteins. It has also been determined to be a type-1 diabetes autoantigen, also known as islet cell antibody 12. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11192](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11192) · Entrez [9580](https://www.ncbi.nlm.nih.gov/gene/9580) · UniProt [Q9UN79](https://www.uniprot.org/uniprotkb/Q9UN79) · Ensembl [ENSG00000143842](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143842)

## Data

Gene col 6812: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6812); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6812, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6812]; `tensor/DDL_lfc|DDL_z.npy` [6812]; `embed/gene_vectors.npy` [6812]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6812 or target_col == 6812). Every well: [[SOX13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOX13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
