---
symbol: "DRAM2"
type: "gene"
col: 7955
ensembl_id: "ENSG00000156171"
name: "DNA damage regulated autophagy modulator 2"
location: "1p13.3"
module: 190
arm: "+"
pooled_cpm: 26.59
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/190"]
generated_by: "tahoemap"
---

# DRAM2

*DNA damage regulated autophagy modulator 2* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.29× (z +5.3, q 6e-05, up in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.37×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.541× (z -17.7, q 0e+00, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FHIP2A]] (+0.73, fdr 7e-06), [[CIAO2A]] (+0.64, fdr 7e-06), [[NAPB]] (+0.63, fdr 8e-06); moves opposite to [[BACH1]] (-0.59, fdr 1e-05), [[IER2]] (-0.59, fdr 2e-05), [[PPP1R10]] (-0.58, fdr 1e-05).
> It is in [[Module 190]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7955.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.37×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +5.3 | 6e-05 | 22/48 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.007 | 15/47 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +4.1 | 0.007 | 13/48 (AsPC-1, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7955.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.541×** | -17.7 | 0e+00 | 35/47 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.440×** | -16.7 | 0e+00 | 39/47 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.442×** | -16.7 | 0e+00 | 46/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.489×** | -14.6 | 0e+00 | 43/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.533×** | -12.8 | 2e-35 | 38/47 (C32, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.570×** | -11.4 | 3e-28 | 40/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.597×** | -10.5 | 8e-24 | 41/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.589×** | -10.3 | 3e-23 | 34/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.623×** | -9.5 | 2e-19 | 39/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.644×** | -9.0 | 2e-17 | 32/46 (NCI-H460, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.653×** | -8.7 | 3e-16 | 30/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.669×** | -8.2 | 1e-14 | 31/48 (NCI-H460, SW480, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.701×** | -7.2 | 3e-11 | 31/47 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.759×** | -5.6 | 9e-07 | 22/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.744×** | -5.6 | 1e-06 | 23/40 (NCI-H23, SW 900, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.773×** | -4.9 | 3e-05 | 18/47 (PANC-1, C32, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.789×** | -4.8 | 6e-05 | 20/48 (A498, SNU-423, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.851× | -4.6 | 1e-04 | 17/48 (A-427, HS-578T, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.810×** | -4.3 | 6e-04 | 14/48 (A498, PANC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.871× | -3.9 | 0.003 | 14/48 (Hs 766T, SW480, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.694×** | -3.9 | 0.003 | 16/47 (MIA PaCa-2, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.877× | -3.7 | 0.005 | 10/48 (HS-578T, SW480, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.836× | -3.5 | 0.012 | 13/47 (SNU-423, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7955. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 31.6 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.312× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 51.4 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -25.5) |
| [[NCI-H460 (line)]] | wt | 22.5 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -13.4) |
| [[C32 (line)]] | wt | 21.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -13.3) |
| [[LoVo (line)]] | wt | 34.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -14.0) |
| [[NCI-H1573 (line)]] | alt | 21.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -19.6) |
| [[MIA PaCa-2 (line)]] | alt | 40.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -9.3) |
| [[A498 (line)]] | wt | 34.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -12.4) |
| [[HCT15 (line)]] | alt | 32.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.371× (z -8.5) |
| [[Hs 766T (line)]] | wt | 42.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.331× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 27.5 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.260× (z -9.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 23.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.380× (z -10.2) |
| [[RKO (line)]] | wt | 33.5 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.159× (z -13.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.331× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 23.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -16.9) |
| [[SK-MEL-2 (line)]] | alt | 37.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -15.7) |
| [[SNU-1 (line)]] | wt | 54.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -13.2) |
| [[SW1417 (line)]] | alt | 17.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -13.9) |
| [[COLO 205 (line)]] | alt | 20.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -11.9) |
| [[H4 (line)]] | wt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -8.8) |
| [[HS-578T (line)]] | alt | 28.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -11.4) |
| [[HT-29 (line)]] | alt | 37.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.319× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 32.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.296× (z -10.4) |
| [[SW 900 (line)]] | alt | 24.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -13.6) |
| [[A-172 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7955), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FHIP2A]] | +0.73 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[CIAO2A]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[NAPB]] | +0.63 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[RNPEP]] | +0.63 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[TMEM94]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[CHPT1]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[BMPR1A]] | +0.60 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[ABCB10]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[INTS8]] | +0.60 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[RAB12]] | +0.59 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[SLC35D1]] | +0.58 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[FBXO9]] | +0.57 | +0.53 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BACH1]] | -0.59 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[IER2]] | -0.59 | -0.65 / -0.48 | both halves | 2e-05 |  |
| [[PPP1R10]] | -0.58 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[CYTOR]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[MIR4435-2HG]] | -0.55 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[NABP1]] | -0.55 | -0.64 / -0.52 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[MIR222HG]] | -0.54 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[EGR1]] | -0.54 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[SGMS2]] | -0.54 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ZNF274]] | -0.53 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[RASAL2]] | -0.53 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ZSWIM6]] | -0.53 | -0.50 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 190]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.784). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.1, 15.5); signed map (-29.8, -18.7). **Vector** length 79.2, 15.9% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +3.4 | +0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.4 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +4.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.6 | -12.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -16.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -10.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -9.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.1 | -16.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.5 | -4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | DNA damage regulated autophagy modulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:111,117,163-111,140,203 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC54289, PRO180, WWFQ154, RP5-1180E21.1; previously TMEM77 |
| Gene groups (HGNC) | DRAM autophagy modulator family |
| Hallmark sets | ADIPOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UX65](https://www.uniprot.org/uniprotkb/Q6UX65) (DNA damage-regulated autophagy modulator protein 2):

> Plays a role in the initiation of autophagy. In the retina, might be involved in the process of photoreceptor cells renewal and recycling to preserve visual function. Induces apoptotic cell death when coexpressed with DRAM1.

**Summary**, from NCBI Gene [128338](https://www.ncbi.nlm.nih.gov/gene/128338):

> The protein encoded by this gene binds microtubule-associated protein 1 light chain 3 and is required for autophagy. Defects in this gene are a cause of retinal dystrophy. In addition, two microRNAs (microRNA 125b-1 and microRNA 144) can bind to the mRNA of this gene and produce the disease state. [provided by RefSeq, Mar 2017]

**Accessions** — [HGNC:28769](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28769) · Entrez [128338](https://www.ncbi.nlm.nih.gov/gene/128338) · UniProt [Q6UX65](https://www.uniprot.org/uniprotkb/Q6UX65) · Ensembl [ENSG00000156171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156171)

## Data

Gene col 7955: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7955); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7955, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7955]; `tensor/DDL_lfc|DDL_z.npy` [7955]; `embed/gene_vectors.npy` [7955]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7955 or target_col == 7955). Every well: [[DRAM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DRAM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
