---
symbol: "LRRC49"
type: "gene"
col: 6077
ensembl_id: "ENSG00000137821"
name: "leucine rich repeat containing 49"
location: "15q23"
module: 14
arm: "+"
pooled_cpm: 70.1
n_lines_expressing: 39
n_dd_up: 26
n_dd_down: 28
n_dd_up_clean: 21
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 6
direction_downstream: 13
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# LRRC49

*leucine rich repeat containing 49* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.98× (z +31.1, q 0e+00, up in 34 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.556× (z -11.4, q 2e-27, down in 21 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.683× (z -7.7, q 3e-12, down in 26 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAF1]] (+0.66, fdr 7e-06), [[AFF3]] (+0.62, fdr 1e-05), [[TNFRSF9]] (+0.61, fdr 1e-05); moves opposite to [[CCND3]] (-0.49, fdr 4e-05), [[TAF8]] (-0.48, fdr 3e-05), [[COPS8]] (-0.48, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[KCNMA1]] → it (grade B ⚠); 13 go from it, the strongest it → [[TRAF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6077.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.98×** | +31.1 | 0e+00 | 34/37 (HOP62, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.89×** | +12.4 | 1e-32 | 33/37 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +12.1 | 1e-31 | 28/37 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +11.1 | 2e-26 | 30/37 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.47×** | +11.0 | 6e-26 | 26/37 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +9.4 | 4e-19 | 25/37 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **1.44×** | +7.4 | 2e-11 | 23/37 (HS-578T, SNU-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +7.1 | 8e-11 | 17/37 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.40×** | +6.8 | 6e-10 | 25/36 (Hs 766T, HS-578T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.36×** | +6.2 | 3e-08 | 22/37 (J82, A498, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.36×** | +6.1 | 5e-08 | 20/37 (SNU-1, Hs 766T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +6.1 | 5e-08 | 15/37 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.74×** | +5.8 | 3e-07 | 26/38 (HOP62, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.6 | 8e-07 | 15/37 (SW1417, LoVo, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +5.2 | 7e-06 | 20/36 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +4.2 | 7e-04 | 19/37 (LoVo, Panc 03.27, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.21×** | +3.9 | 0.003 | 11/37 (RKO, SW1417, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6077.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.556×** | -11.4 | 2e-27 | 21/29 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.658×** | -8.4 | 9e-15 | 23/36 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.683×** | -7.7 | 3e-12 | 26/37 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.668×** | -7.5 | 7e-12 | 23/36 (A549, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.710×** | -6.9 | 5e-10 | 20/37 (NCI-H1792, HS-578T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.718×** | -6.7 | 2e-09 | 22/37 (NCI-H1792, HS-578T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.733×** | -6.3 | 3e-08 | 21/37 (H4, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.739×** | -6.1 | 7e-08 | 22/37 (NCI-H1792, A498, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.813×** | -5.9 | 2e-07 | 17/37 (H4, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.751×** | -5.8 | 4e-07 | 19/37 (H4, NCI-H1792, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.743×** | -5.8 | 4e-07 | 22/35 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.752×** | -5.8 | 4e-07 | 20/37 (NCI-H1792, A549, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **0.755×** | -5.7 | 6e-07 | 21/37 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **0.762×** | -5.5 | 2e-06 | 20/37 (PANC-1, H4, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.770×** | -5.3 | 5e-06 | 21/37 (NCI-H1792, H4, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.772×** | -5.2 | 6e-06 | 19/37 (PANC-1, H4, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.769×** | -4.9 | 3e-05 | 19/36 (NCI-H1792, H4, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.786×** | -4.9 | 3e-05 | 18/37 (NCI-H1792, HS-578T, …) | all doses, flat |  |
| [[Ritonavir (drug)]] 5 µM |  | 0.855× | -4.5 | 2e-04 | 10/37 (LoVo, PANC-1, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -4.5 | 2e-04 | 18/37 (A498, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6077. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 181 | 3 | 12 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +24.0) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.263× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 284 | 3 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +13.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0963× (z -19.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.249× (z -12.1) |
| [[H4 (line)]] | wt | 247 | 2 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.233× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 280 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 0.358× (z -9.7) |
| [[A498 (line)]] | wt | 115 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -14.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 135 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -15.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 178 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.96× (z +19.3) | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -12.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 45.8 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 24.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +25.3) | — |
| [[Panc 03.27 (line)]] | alt | 88.9 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.25× (z +28.5) | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -8.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 87.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.3× (z +34.5) | — |
| [[Hs 766T (line)]] | wt | 43.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +13.4) | — |
| [[HS-578T (line)]] | alt | 157 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -12.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 81.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -9.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 98.9 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +15.0) | [[Harringtonine (drug)]] 0.5 µM 0.320× (z -9.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 47.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.58× (z +22.2) | — |
| [[SW1417 (line)]] | alt | 18.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.60× (z +11.0) | — |
| [[SW480 (line)]] | alt | 38.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +21.5) | — |
| [[A549 (line)]] | wt | 52.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +16.0) | [[Harringtonine (drug)]] 0.05 µM 0.262× (z -9.9) |
| [[J82 (line)]] | alt | 45.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +25.8) | — |
| [[NCI-H460 (line)]] | wt | 19.0 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.22× (z +10.1) | [[Homoharringtonine (drug)]] 0.05 µM 0.355× (z -8.9) |
| [[SNU-1 (line)]] | wt | 43.2 | 2 | 0 | [[Artesunate (drug)]] 5 µM 4.49× (z +10.0) | — |
| [[SW 1271 (line)]] | alt | 218 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0657× (z -11.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 94.5 | 0 | 1 | — | [[EX229 (drug)]] 5 µM 0.0475× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 92.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +23.4) | — |
| [[CHP-212 (line)]] | wt | 55.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +13.9) | — |
| [[HepG2_C3A (line)]] | wt | 58.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.25× (z +13.9) | — |
| [[LOX-IMVI (line)]] | wt | 46.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +18.2) | — |
| [[NCI-H2030 (line)]] | alt | 57.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.7) | — |
| [[A-427 (line)]] | wt | 13.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.25 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.94 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 96.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6077), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAF1]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[AFF3]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[TNFRSF9]] | +0.61 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[SLC41A2]] | +0.60 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[NEURL3]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[IL1A]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[HMGN2P46]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SLAMF7]] | +0.58 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[NINJ1]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[LINC01828]] | +0.56 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[RIPK2]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[RPLP0P2]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCND3]] | -0.49 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[TAF8]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[COPS8]] | -0.48 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[ABHD2]] | -0.45 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[TMEM164]] | -0.45 | -0.51 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNMA1]] | B | KCNMA1 activity raises LRRC49's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 3.28× lower at baseline in the lines without KCNMA1 | 0.008 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[C15orf48]] | B | C15orf48 activity raises LRRC49's level | lines that do not express C15orf48 (25) vs lines expressing it (25) | 2.23× lower at baseline in the lines without C15orf48 | 0.009 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG |
| [[GSDME]] | B | GSDME activity raises LRRC49's level | lines that do not express GSDME (15) vs lines expressing it (35) | 3.11× lower at baseline in the lines without GSDME | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000285804, FBXO17, PYGO1 |
| [[NR3C1]] | B | NR3C1 activity lowers LRRC49's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.0% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds |
| [[GBP5]] | B | GBP5 activity raises LRRC49's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 2.84× lower at baseline in the lines without GBP5 | 0.070 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |
| [[PPP4R4]] | C | PPP4R4 activity raises LRRC49's level | lines that do not express PPP4R4 (10) vs lines expressing it (40) | 3.54× lower at baseline in the lines without PPP4R4 | 0.020 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, ENSG00000285804, LINC01088; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 11, C 2. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRAF1]] | B | LRRC49 activity raises TRAF1's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 2.99× lower at baseline in the lines without LRRC49 | 0.019 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent |
| [[GSDME]] | B | LRRC49 activity raises GSDME's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 4.10× lower at baseline in the lines without LRRC49 | 0.019 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent |
| [[DYRK3]] | B | LRRC49 activity raises DYRK3's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 2.83× lower at baseline in the lines without LRRC49 | 0.025 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent |
| [[KCNMA1]] | B | LRRC49 activity raises KCNMA1's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 5.84× lower at baseline in the lines without LRRC49 | 0.027 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent |
| [[LINC00944]] | B | LRRC49 activity raises LINC00944's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 3.09× lower at baseline in the lines without LRRC49 | 0.047 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent |
| [[PIK3CD]] | B | LRRC49 activity raises PIK3CD's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 2.39× lower at baseline in the lines without LRRC49 | 0.051 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent |
| [[GPR158]] | B | LRRC49 activity raises GPR158's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 2.25× lower at baseline in the lines without LRRC49 | 0.060 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent |
| [[PTHLH]] | B | LRRC49 activity raises PTHLH's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 2.69× lower at baseline in the lines without LRRC49 | 0.069 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent |
| [[CXCL8]] | B | LRRC49 activity raises CXCL8's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 3.29× lower at baseline in the lines without LRRC49 | 0.081 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent |
| [[LACTB]] | B | LRRC49 activity raises LACTB's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 1.60× lower at baseline in the lines without LRRC49 | 0.091 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent |
| [[LINC01828]] | B | LRRC49 activity raises LINC01828's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 2.14× lower at baseline in the lines without LRRC49 | 0.096 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent |
| [[PPP4R4]] | C | LRRC49 activity raises PPP4R4's level | lines that do not express LRRC49 (11) vs lines expressing it (39) | 3.67× lower at baseline in the lines without LRRC49 | 0.009 | ⚠ within organs, on part of the lines; also absent: LARP6, HEG1, FJX1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.517). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.6, 1.0); signed map (42.6, 12.3). **Vector** length 117, 31.4% of its response variance represented; |z| ≥ 3 in 1,366 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.7 | +31.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.8 | +12.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +12.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +5.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.0 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.7 | +1.6 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +2.5 | +2.5 |
| fall | [[Triamcinolone (drug)]] 0.5 µM |  | -4.6 | -6.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.5 | -6.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.4 | -4.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.4 | -6.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -4.1 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 49 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:70,853,239-71,053,658 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20156, CSTPP2, PGs4 |
| Gene groups (HGNC) | Tubulin polyglutamylase complex subunits; Centriolar satellite proteins |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUZ0](https://www.uniprot.org/uniprotkb/Q8IUZ0) (Leucine-rich repeat-containing protein 49):

> Subunit of the tubulin polyglutamylase complex (TPGC). The complex mediates cilia and flagella polyglutamylation which is essential for their biogenesis and motility.

**Summary**, from NCBI Gene [54839](https://www.ncbi.nlm.nih.gov/gene/54839):

> Located in centriolar satellite. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25965](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25965) · Entrez [54839](https://www.ncbi.nlm.nih.gov/gene/54839) · UniProt [Q8IUZ0](https://www.uniprot.org/uniprotkb/Q8IUZ0) · Ensembl [ENSG00000137821](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137821)

## Data

Gene col 6077: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6077); `tables/drug_effects.parquet` (78 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6077, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6077]; `tensor/DDL_lfc|DDL_z.npy` [6077]; `embed/gene_vectors.npy` [6077]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6077 or target_col == 6077). Every well: [[LRRC49 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC49.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
