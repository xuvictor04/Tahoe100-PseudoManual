---
symbol: "MMD"
type: "gene"
col: 3013
ensembl_id: "ENSG00000108960"
name: "monocyte to macrophage differentiation associated"
location: "17q22"
module: 217
arm: "+"
pooled_cpm: 17.46
n_lines_expressing: 48
n_dd_up: 22
n_dd_down: 9
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/217"]
generated_by: "tahoemap"
---

# MMD

*monocyte to macrophage differentiation associated* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.71× (z +25.3, q 0e+00, up in 35 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.661× (z -7.4, q 5e-11, down in 23 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HS3ST3B1]] (+0.60, fdr 1e-05), [[SYT12]] (+0.57, fdr 1e-05), [[BIRC3]] (+0.56, fdr 1e-05); moves opposite to [[FTL]] (-0.57, fdr 1e-05), [[ZFAND2A]] (-0.53, fdr 3e-05), [[ST13]] (-0.51, fdr 1e-04).
> It is in [[Module 217]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TGM2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3013.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.71×** | +25.3 | 0e+00 | 35/44 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.55×** | +16.2 | 0e+00 | 35/45 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +13.0 | 2e-36 | 32/44 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +12.8 | 4e-35 | 35/45 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **1.85×** | +11.0 | 3e-26 | 23/35 (CFPAC-1, PANC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.84×** | +10.2 | 3e-22 | 19/30 (LoVo, SW480, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +9.3 | 1e-18 | 28/44 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **1.71×** | +9.2 | 2e-18 | 10/22 (NCI-H2030, CFPAC-1, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +8.1 | 5e-14 | 24/43 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.53×** | +7.7 | 8e-13 | 24/45 (HOP62, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.52×** | +7.5 | 2e-12 | 25/46 (NCI-H460, KATO III, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.52×** | +7.5 | 3e-12 | 23/45 (KATO III, HOP62, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.44×** | +6.4 | 9e-09 | 20/43 (HOP62, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.40×** | +6.1 | 4e-08 | 19/42 (KATO III, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.37×** | +5.7 | 5e-07 | 19/46 (KATO III, HOP62, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +4.2 | 0.001 | 8/45 (A498, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.15× | +3.5 | 0.012 | 8/46 (SW480, SNU-423, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.026 | 8/41 (A549, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.030 | 5/45 (BT-474, HCT15, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.0 | 0.053 | 10/45 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Econazole (drug)]] 5 µM |  | 1.18× | +2.9 | 0.069 | 9/45 (A549, HOP62, …) | top dose only |  |
| [[Mifepristone (drug)]] 5 µM |  | 1.18× | +2.9 | 0.079 | 5/44 (A498, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3013.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.661×** | -7.4 | 5e-11 | 23/45 (HepG2/C3A, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.663×** | -7.4 | 5e-11 | 27/44 (SW 900, BT-474, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.643×** | -7.2 | 9e-11 | 23/44 (SW48, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.681×** | -6.9 | 8e-10 | 25/44 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.811×** | -5.3 | 1e-05 | 19/46 (BT-474, SW 900, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.758×** | -4.7 | 2e-04 | 13/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.623×** | -4.4 | 7e-04 | 13/40 (BT-474, A498, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.775×** | -4.4 | 8e-04 | 11/43 (HEC-1-A, CHP-212, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.820×** | -3.5 | 0.024 | 9/44 (BT-474, CFPAC-1, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.867× | -3.4 | 0.033 | 10/46 (COLO 205, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.861× | -3.4 | 0.035 | 8/45 (HEC-1-A, CHP-212, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.843× | -3.3 | 0.039 | 13/46 (A-427, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.951× | -3.3 | 0.044 | 1/46 (AsPC-1) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3013. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 28.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +20.4) | — |
| [[HepG2_C3A (line)]] | wt | 103 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.284× (z -11.1) |
| [[PANC-1 (line)]] | alt | 23.7 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +24.0) | [[Bortezomib (drug)]] 0.05 µM 0.363× (z -8.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.410× (z -8.5) |
| [[A-172 (line)]] | wt | 8.63 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.54× (z +15.2) | [[Proglumide (drug)]] 0.05 µM 0.103× (z -11.5) |
| [[A549 (line)]] | wt | 38.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +19.2) | — |
| [[NCI-H460 (line)]] | wt | 6.69 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +16.0) | — |
| [[BT-474 (line)]] | alt | 35.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +11.2) | [[Selinexor (drug)]] 5 µM 0.340× (z -8.9) ⚠ cell-cycle shift, explains ~85% of this change |
| [[H4 (line)]] | wt | 12.6 | 0 | 2 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0539× (z -10.6) |
| [[J82 (line)]] | alt | 7.54 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +10.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.132× (z -9.2) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 8.45 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +12.7) | — |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 2 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.113× (z -9.4) |
| [[SW 900 (line)]] | alt | 49.6 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.223× (z -9.7) |
| [[SW48 (line)]] | wt | 13.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.01× (z +11.0) | [[Bortezomib (drug)]] 0.05 µM 0.0463× (z -11.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 15.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +13.0) | — |
| [[HOP62 (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 11.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 14.2 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 5.25× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 12.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 21.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +10.6) | — |
| [[SK-MEL-2 (line)]] | alt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +10.1) | — |
| [[SNU-423 (line)]] | alt | 27.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.0) | — |
| [[A-427 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.94 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3013), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HS3ST3B1]] | +0.60 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[SYT12]] | +0.57 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[BIRC3]] | +0.56 | +0.52 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[SPRED1]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[IL4R]] | +0.55 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[FKBP5]] | +0.55 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ZNF217]] | +0.55 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[ADAMTS9]] | +0.54 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[ZC3H12C]] | +0.54 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[YAP1]] | +0.54 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[TGFBR2]] | +0.53 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[BCL9L]] | +0.52 | +0.51 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FTL]] | -0.57 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[ZFAND2A]] | -0.53 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[ST13]] | -0.51 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[TVP23C]] | -0.51 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[BTBD9]] | -0.49 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[HSPA9]] | -0.49 | -0.43 / -0.50 | both halves | 4e-05 |  |
| [[ANKRD23]] | -0.49 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[HIBCH]] | -0.49 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[TMPRSS5]] | -0.48 | -0.37 / -0.53 | both halves | 7e-05 |  |
| [[TXNL1]] | -0.48 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[RAB18]] | -0.48 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[VTI1A]] | -0.47 | -0.40 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGM2]] | B | TGM2 activity raises MMD's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 1.59× lower at baseline in the lines without TGM2 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[MET]] | B | MET activity raises MMD's level | lines that do not express MET (9) vs lines expressing it (41) | 1.52× lower at baseline in the lines without MET | 0.071 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[CCL20]] | B | CCL20 activity raises MMD's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 1.55× lower at baseline in the lines without CCL20 | 0.072 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[VDR]] | B | VDR activity raises MMD's level | lines that do not express VDR (8) vs lines expressing it (42) | 1.56× lower at baseline in the lines without VDR | 0.089 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 217]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (26.2, 8.9); signed map (12.6, 27.9). **Vector** length 95.3, 20.7% of its response variance represented; |z| ≥ 3 in 1,139 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +25.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +16.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +12.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | +3.8 | +9.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.6 | +2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.6 | +2.2 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.4 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.3 | +1.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.8 | -7.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.7 | -7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -6.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | -3.5 | -5.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.7 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | monocyte to macrophage differentiation associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:55,392,622-55,421,924 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MMA, PAQR11 |
| Gene groups (HGNC) | Progestin and adipoQ receptor family |
| Hallmark sets | KRAS_SIGNALING_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15546](https://www.uniprot.org/uniprotkb/Q15546) (Monocyte to macrophage differentiation factor):

> Involved in the dynamics of lysosomal membranes associated with microglial activation following brain lesion.

**Summary**, from NCBI Gene [23531](https://www.ncbi.nlm.nih.gov/gene/23531):

> This protein is expressed by in vitro differentiated macrophages but not freshly isolated monocytes. Although sequence analysis identifies seven potential transmembrane domains, this protein has little homology to G-protein receptors and it has not been positively identified as a receptor. A suggested alternative function is that of an ion channel protein in maturing macrophages. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7153](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7153) · Entrez [23531](https://www.ncbi.nlm.nih.gov/gene/23531) · UniProt [Q15546](https://www.uniprot.org/uniprotkb/Q15546) · Ensembl [ENSG00000108960](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108960)

## Data

Gene col 3013: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3013); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3013, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3013]; `tensor/DDL_lfc|DDL_z.npy` [3013]; `embed/gene_vectors.npy` [3013]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3013 or target_col == 3013). Every well: [[MMD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
