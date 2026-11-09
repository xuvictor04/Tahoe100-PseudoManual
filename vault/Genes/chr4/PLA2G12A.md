---
symbol: "PLA2G12A"
type: "gene"
col: 4458
ensembl_id: "ENSG00000123739"
name: "phospholipase A2 group XIIA"
location: "4q25"
module: 57
arm: "+"
pooled_cpm: 26.67
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 17
n_dd_up_clean: 12
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# PLA2G12A

*phospholipase A2 group XIIA* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.60× (z +19.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.522× (z -18.9, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDRG3]] (+0.76, fdr 7e-06), [[ATP5F1C]] (+0.71, fdr 7e-06), [[CNIH1]] (+0.71, fdr 7e-06); moves opposite to [[IL34]] (-0.69, fdr 5e-05), [[MZF1-AS1]] (-0.67, fdr 4e-05), [[ZBED5]] (-0.67, fdr 2e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4458.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.60×** | +19.6 | 0e+00 | 47/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.56×** | +19.4 | 0e+00 | 47/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.43×** | +18.3 | 0e+00 | 46/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +14.3 | 4e-44 | 33/44 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +13.7 | 2e-40 | 28/37 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +12.3 | 6e-33 | 43/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +9.9 | 4e-21 | 34/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.20×** | +8.5 | 2e-15 | 36/48 (A498, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +7.6 | 1e-12 | 25/48 (A498, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.24×** | +6.3 | 2e-08 | 22/48 (H4, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.34×** | +5.8 | 4e-07 | 21/45 (NCI-H2030, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +5.5 | 2e-06 | 19/42 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.29×** | +5.3 | 6e-06 | 17/48 (NCI-H2347, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.23×** | +4.2 | 1e-03 | 17/48 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.001 | 16/48 (C-33 A, RKO, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.20× | +3.7 | 0.007 | 5/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +3.5 | 0.016 | 15/48 (A-172, SW480, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.016 | 10/48 (SW480, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | 1.16× | +3.4 | 0.023 | 4/48 (HEC-1-A, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.17× | +3.2 | 0.039 | 7/48 (LS 180, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4458.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.522×** | -18.9 | 0e+00 | 43/47 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.550×** | -12.3 | 2e-32 | 31/47 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.561×** | -11.5 | 4e-28 | 33/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.604×** | -10.4 | 4e-23 | 30/48 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.635×** | -9.4 | 1e-18 | 32/46 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.655×** | -8.7 | 3e-16 | 31/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.678×** | -8.0 | 9e-14 | 31/48 (RKO, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.706×** | -7.2 | 5e-11 | 26/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.755×** | -5.8 | 5e-07 | 22/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.825×** | -5.6 | 1e-06 | 23/48 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.800×** | -4.6 | 2e-04 | 19/47 (NCI-H460, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.672×** | -4.3 | 9e-04 | 18/46 (NCI-H460, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.806×** | -4.2 | 0.001 | 18/47 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.824×** | -4.0 | 0.002 | 13/48 (H4, A-172, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.690×** | -4.0 | 0.002 | 12/48 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.837× | -3.7 | 0.008 | 17/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4458. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 25.4 | 3 | 6 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.55× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -20.4) |
| [[NCI-H460 (line)]] | wt | 17.3 | 3 | 5 | [[Panobinostat (drug)]] 0.5 µM 3.35× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -18.5) |
| [[A-172 (line)]] | wt | 20.6 | 2 | 5 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.58× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.177× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 37.5 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.73× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.31× (z +10.4) | — |
| [[A498 (line)]] | wt | 26.0 | 3 | 2 | [[Panobinostat (drug)]] 0.5 µM 3.13× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -12.2) |
| [[HOP62 (line)]] | alt | 22.9 | 2 | 2 | [[Panobinostat (drug)]] 0.5 µM 3.13× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -22.5) |
| [[MIA PaCa-2 (line)]] | alt | 18.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -14.3) |
| [[A-427 (line)]] | wt | 42.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -17.2) |
| [[C32 (line)]] | wt | 25.6 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.66× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -11.3) |
| [[H4 (line)]] | wt | 30.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.141× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 44.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.39× (z +13.8) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 15.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -12.3) |
| [[LOX-IMVI (line)]] | wt | 14.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0929× (z -16.0) |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -9.6) |
| [[SW 900 (line)]] | alt | 23.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -13.7) |
| [[A549 (line)]] | wt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 29.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.9) |
| [[CHP-212 (line)]] | wt | 38.7 | 0 | 1 | — | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.0802× (z -9.8) |
| [[HCT15 (line)]] | alt | 53.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -14.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -11.8) |
| [[HS-578T (line)]] | alt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -13.3) |
| [[hTERT-HPNE (line)]] | wt | 22.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.184× (z -9.4) |
| [[LoVo (line)]] | wt | 45.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 20.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 30.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -16.6) |
| [[NCI-H2347 (line)]] | alt | 32.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 25.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -8.6) |
| [[RKO (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 19.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -12.0) |
| [[SNU-1 (line)]] | wt | 24.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -8.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 31.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4458), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDRG3]] | +0.76 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[ATP5F1C]] | +0.71 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[CNIH1]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[RAB4A]] | +0.66 | +0.56 / +0.51 | both halves | 1e-05 | pathway: Phospholipid metabolism |
| [[CYB5R4]] | +0.66 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[ELP1]] | +0.65 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[MPP1]] | +0.65 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[SKIC3]] | +0.65 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[PAPSS1]] | +0.65 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[STX7]] | +0.64 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[SDHB]] | +0.64 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | +0.64 | +0.53 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL34]] | -0.69 | -0.69 / -0.40 | both halves | 5e-05 |  |
| [[MZF1-AS1]] | -0.67 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[ZBED5]] | -0.67 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[MEPCE]] | -0.65 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[PCNX4-DT]] | -0.65 | -0.53 / -0.24 | both halves | 4e-04 |  |
| [[NEK8]] | -0.65 | -0.57 / -0.29 | both halves | 2e-04 |  |
| [[ZNF689]] | -0.64 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[CDK6-AS1]] | -0.64 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ARMC5]] | -0.64 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[ACTR3-AS1]] | -0.63 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[BOLA1]] | -0.63 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[BAZ1A]] | -0.63 | -0.45 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.789). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-1.3, -7.2); signed map (-34.1, -13.7). **Vector** length 94.0, 22.4% of its response variance represented; |z| ≥ 3 in 1,132 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.4 | +18.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +12.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.3 | +19.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.3 | +9.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.1 | +8.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.5 | +1.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.9 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.8 | -5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -10.4 | -18.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.3 | -12.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.5 | -2.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.4 | -11.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -5.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.7 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase A2 group XIIA |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:109,709,989-109,730,070 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PLA2G12 |
| Gene groups (HGNC) | Phospholipases |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 9 pathways, smallest: Acyl chain remodelling of PI; Acyl chain remodelling of PG; Acyl chain remodelling of PS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZM1](https://www.uniprot.org/uniprotkb/Q9BZM1) (Group XIIA secretory phospholipase A2):

> PA2 catalyzes the calcium-dependent hydrolysis of the 2-acyl groups in 3-sn-phosphoglycerides. Does not exhibit detectable activity toward sn-2-arachidonoyl- or linoleoyl-phosphatidylcholine or -phosphatidylethanolamine.

**Summary**, from NCBI Gene [81579](https://www.ncbi.nlm.nih.gov/gene/81579):

> Secreted phospholipase A2 (sPLA2) enzymes liberate arachidonic acid from phospholipids for production of eicosanoids and exert a variety of physiologic and pathologic effects. Group XII sPLA2s, such as PLA2G12A, have relatively low specific activity and are structurally and functionally distinct from other sPLA2s (Gelb et al., 2000 [PubMed 11031251]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:18554](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18554) · Entrez [81579](https://www.ncbi.nlm.nih.gov/gene/81579) · UniProt [Q9BZM1](https://www.uniprot.org/uniprotkb/Q9BZM1) · Ensembl [ENSG00000123739](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123739)

## Data

Gene col 4458: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4458); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4458, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4458]; `tensor/DDL_lfc|DDL_z.npy` [4458]; `embed/gene_vectors.npy` [4458]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4458 or target_col == 4458). Every well: [[PLA2G12A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLA2G12A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
