---
symbol: "BRD1"
type: "gene"
col: 1959
ensembl_id: "ENSG00000100425"
name: "bromodomain containing 1"
location: "22q13.33"
module: 46
arm: "+"
pooled_cpm: 47.75
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# BRD1

*bromodomain containing 1* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.83× (z +13.4, q 2e-38, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.206× (z -24.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SETD1B]] (+0.76, fdr 7e-06), [[PHF2]] (+0.76, fdr 7e-06), [[UBTF]] (+0.70, fdr 1e-05); moves opposite to [[UBA6]] (-0.65, fdr 4e-05), [[RADX]] (-0.63, fdr 4e-05), [[YIF1B]] (-0.61, fdr 3e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1959.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +13.4 | 2e-38 | 40/48 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +7.6 | 1e-11 | 37/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +6.8 | 2e-09 | 35/48 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.21×** | +6.5 | 1e-08 | 36/48 (NCI-H1573, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +5.9 | 5e-07 | 33/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.00×** | +5.7 | 1e-06 | 32/49 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +5.2 | 2e-05 | 30/48 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +4.5 | 5e-04 | 23/48 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1959.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.206×** | -24.9 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.227×** | -23.3 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.302×** | -18.9 | 0e+00 | 47/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.496×** | -11.0 | 4e-26 | 45/48 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.693×** | -8.2 | 3e-14 | 44/48 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **0.697×** | -5.7 | 1e-06 | 32/47 (NCI-H23, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.709×** | -5.4 | 4e-06 | 32/47 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.689×** | -5.4 | 4e-06 | 29/44 (C32, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.712×** | -5.3 | 6e-06 | 33/48 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **0.703×** | -5.3 | 6e-06 | 24/40 (AsPC-1, C32, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.848× | -3.7 | 0.013 | 21/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.801×** | -3.5 | 0.023 | 21/48 (HepG2/C3A, NCI-H2347, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.813×** | -3.3 | 0.049 | 19/48 (AsPC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.680×** | -3.2 | 0.061 | 18/49 (HT-29, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1959. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 44.9 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -21.9) |
| [[AsPC-1 (line)]] | alt | 39.6 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.0650× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.147× (z -15.5) |
| [[C32 (line)]] | wt | 75.3 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.220× (z -12.7) |
| [[KATO III (line)]] | alt | 54.4 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -20.1) |
| [[NCI-H2347 (line)]] | alt | 54.7 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -19.0) |
| [[NCI-H460 (line)]] | wt | 43.3 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.2) | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -17.0) |
| [[SHP-77 (line)]] | alt | 59.7 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -17.0) |
| [[A549 (line)]] | wt | 34.3 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -14.5) |
| [[HCT15 (line)]] | alt | 58.7 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.232× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 39.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.152× (z -12.9) |
| [[Hs 766T (line)]] | wt | 36.8 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.254× (z -10.8) |
| [[HT-29 (line)]] | alt | 45.9 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.170× (z -15.2) |
| [[LoVo (line)]] | wt | 51.0 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.171× (z -18.0) |
| [[MIA PaCa-2 (line)]] | alt | 52.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -20.0) |
| [[NCI-H1573 (line)]] | alt | 52.5 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +18.2) | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -12.5) |
| [[NCI-H2030 (line)]] | alt | 62.7 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -11.9) |
| [[PANC-1 (line)]] | alt | 28.4 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.256× (z -14.3) |
| [[RKO (line)]] | wt | 52.0 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.123× (z -16.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.177× (z -14.2) |
| [[SK-MEL-2 (line)]] | alt | 26.4 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.134× (z -13.9) |
| [[SW 900 (line)]] | alt | 197 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.254× (z -13.1) |
| [[A-172 (line)]] | wt | 32.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.181× (z -15.0) |
| [[A498 (line)]] | wt | 36.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.244× (z -13.8) |
| [[AN3 CA (line)]] | alt | 65.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.170× (z -9.1) |
| [[BT-474 (line)]] | alt | 58.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.146× (z -17.1) |
| [[C-33 A (line)]] | alt | 77.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -14.5) |
| [[CFPAC-1 (line)]] | alt | 46.0 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.268× (z -11.7) |
| [[CHP-212 (line)]] | wt | 55.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.107× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.154× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 53.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -20.4) |
| [[HOP62 (line)]] | alt | 57.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.139× (z -18.6) |
| [[HS-578T (line)]] | alt | 47.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -13.4) |
| [[hTERT-HPNE (line)]] | wt | 44.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -14.2) |
| [[J82 (line)]] | alt | 30.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.259× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 35.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -17.3) |
| [[LS 180 (line)]] | wt | 53.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.225× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 44.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 35.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.255× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 37.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -15.5) |
| [[SNU-423 (line)]] | alt | 42.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.212× (z -13.5) |
| [[SW1417 (line)]] | alt | 37.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -12.5) |
| [[SW48 (line)]] | wt | 63.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0906× (z -16.2) |
| [[A-427 (line)]] | wt | 30.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.242× (z -11.1) |
| [[COLO 205 (line)]] | alt | 55.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -11.9) |
| [[H4 (line)]] | wt | 30.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.148× (z -10.6) |
| [[NCI-H661 (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0918× (z -8.9) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 28.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.221× (z -8.9) |
| [[NCI-H2122 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1959), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETD1B]] | +0.76 | +0.65 / +0.66 | both halves | 7e-06 | pathway: Chromatin modifying enzymes |
| [[PHF2]] | +0.76 | +0.60 / +0.69 | both halves | 7e-06 | same gene group; pathway: Chromatin modifying enzymes |
| [[UBTF]] | +0.70 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[KDM3B]] | +0.70 | +0.60 / +0.51 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[FIZ1]] | +0.69 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[AFG3L1P]] | +0.69 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[ZMYND11]] | +0.68 | +0.50 / +0.59 | both halves | 1e-05 | same gene group |
| [[DNMT3A]] | +0.68 | +0.59 / +0.53 | both halves | 1e-05 | same gene group; pathway: Chromatin modifying enzymes |
| [[PPP1R3F]] | +0.67 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[ZBTB8A]] | +0.67 | +0.64 / +0.39 | both halves | 5e-05 |  |
| [[ZNF689]] | +0.67 | +0.62 / +0.35 | both halves | 1e-04 |  |
| [[MEPCE]] | +0.67 | +0.56 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBA6]] | -0.65 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[RADX]] | -0.63 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[YIF1B]] | -0.61 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[TMEM92]] | -0.61 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[FCHO1]] | -0.61 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[AP2S1]] | -0.59 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[NHP2]] | -0.58 | -0.42 / -0.25 | both halves | 4e-04 |  |
| [[PDCD10]] | -0.58 | -0.50 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises BRD1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises BRD1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF721]] | C | ZNF721's natural level weakens BRD1's drug response | ZNF721's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.26; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-5.8, 12.1); signed map (26.0, -25.0). **Vector** length 95.3, 26.1% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +13.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.8 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.4 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +6.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +1.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -8.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.5 | -18.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.1 | -11.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -24.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.0 | -23.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -1.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.8 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | bromodomain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:49,773,283-49,827,873 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BRL, BRPF2 |
| Gene groups (HGNC) | PHD finger proteins; PWWP domain containing; Bromodomain containing |
| Reactome | 6 pathways, smallest: Regulation of TP53 Activity through Acetylation; HATs acetylate histones; Regulation of TP53 Activity |
| Matched by | ensembl_id |

**Function**, from UniProt [O95696](https://www.uniprot.org/uniprotkb/O95696) (Bromodomain-containing protein 1):

> Scaffold subunit of various histone acetyltransferase (HAT) complexes, such as the MOZ/MORF and HBO1 complexes, that acts as a regulator of hematopoiesis. Plays a key role in HBO1 complex by directing KAT7/HBO1 specificity towards histone H3 'Lys-14' acetylation (H3K14ac), thereby promoting erythroid differentiation.

**Summary**, from NCBI Gene [23774](https://www.ncbi.nlm.nih.gov/gene/23774):

> This gene encodes a bromodomain-containing protein that localizes to the nucleus and can interact with DNA and histone tails. The encoded protein is a component of the MOZ/MORF acetyltransferase complex and can stimulate acetylation of histones H3 and H4, thereby potentially playing a role in gene activation. Variation in this gene is associated with schizophrenia and bipolar disorder in some study populations. Alternative splicing results in multiple transcript variants. [provided by RefSeq, …

**Accessions** — [HGNC:1102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1102) · Entrez [23774](https://www.ncbi.nlm.nih.gov/gene/23774) · UniProt [O95696](https://www.uniprot.org/uniprotkb/O95696) · Ensembl [ENSG00000100425](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100425)

## Data

Gene col 1959: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1959); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1959, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1959]; `tensor/DDL_lfc|DDL_z.npy` [1959]; `embed/gene_vectors.npy` [1959]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1959 or target_col == 1959). Every well: [[BRD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
