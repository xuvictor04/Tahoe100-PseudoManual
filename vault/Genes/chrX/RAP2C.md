---
symbol: "RAP2C"
type: "gene"
col: 4456
ensembl_id: "ENSG00000123728"
name: "RAP2C, member of RAS oncogene family"
location: "Xq26.2"
module: 77
arm: "-"
pooled_cpm: 36.26
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 8
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# RAP2C

*RAP2C, member of RAS oncogene family* — Xq26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.06× (z +21.7, q 0e+00, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.567× (z -12.1, q 1e-30, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEPTIN8]] (+0.66, fdr 1e-05), [[CLN5]] (+0.66, fdr 2e-05), [[TAF9]] (+0.66, fdr 2e-05); moves opposite to [[RBAK-RBAKDN]] (-0.66, fdr 1e-05), [[ANKRD27]] (-0.66, fdr 3e-05), [[RNF216]] (-0.65, fdr 1e-05).
> It sits in the **-** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4456.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.06×** | +21.7 | 0e+00 | 36/47 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.21×** | +16.1 | 0e+00 | 45/48 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.96×** | +14.2 | 1e-43 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +13.0 | 3e-36 | 44/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +11.4 | 3e-28 | 26/36 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +10.0 | 9e-22 | 34/43 (HOP62, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +8.2 | 1e-14 | 27/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +7.6 | 2e-12 | 29/47 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +7.4 | 6e-12 | 27/47 (PANC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +7.3 | 2e-11 | 32/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +7.1 | 7e-11 | 27/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +6.6 | 2e-09 | 29/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.19× | +5.2 | 7e-06 | 23/48 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.28×** | +5.2 | 7e-06 | 22/46 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **1.32×** | +5.2 | 1e-05 | 19/40 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.009 | 17/48 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.064 | 7/45 (PANC-1, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.32×** | +3.0 | 0.064 | 2/48 (A498, NCI-H2030) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.10× | +2.9 | 0.084 | 11/48 (SNU-1, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4456.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.567×** | -12.1 | 1e-30 | 42/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.579×** | -11.6 | 1e-28 | 42/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.636×** | -9.6 | 1e-19 | 33/48 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.833×** | -5.5 | 5e-06 | 17/48 (SW480, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.788×** | -5.1 | 4e-05 | 22/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.789×** | -5.0 | 4e-05 | 21/48 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Lucanthone (drug)]] 5 µM |  | 0.834× | -3.7 | 0.017 | 8/48 (NCI-H661, LoVo, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.724×** | -3.6 | 0.023 | 11/48 (AsPC-1, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.844× | -3.5 | 0.034 | 12/48 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -3.3 | 0.047 | 16/47 (AsPC-1, HEC-1-A, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.856× | -3.3 | 0.047 | 16/48 (SNU-423, A-427, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.755×** | -3.1 | 0.087 | 14/48 (NCI-H2347, SW480, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4456. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 47.9 | 11 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +25.6) | — |
| [[NCI-H460 (line)]] | wt | 38.8 | 10 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.04× (z +16.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +15.9) | — |
| [[SW480 (line)]] | alt | 54.6 | 3 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.393× (z -13.3) |
| [[AsPC-1 (line)]] | alt | 73.8 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.288× (z -14.1) |
| [[HOP62 (line)]] | alt | 34.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.9) | — |
| [[LoVo (line)]] | wt | 21.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.33× (z +10.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 34.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.1) | — |
| [[A-427 (line)]] | wt | 24.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 3.17× (z +8.5) | — |
| [[A549 (line)]] | wt | 36.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +13.9) | — |
| [[HT-29 (line)]] | alt | 48.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.350× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 25.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.10× (z +18.0) | — |
| [[J82 (line)]] | alt | 31.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +15.2) | — |
| [[NCI-H1573 (line)]] | alt | 43.2 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.79× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +9.0) | — |
| [[NCI-H23 (line)]] | alt | 38.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.8) | — |
| [[NCI-H2347 (line)]] | alt | 40.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.371× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 37.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.376× (z -8.7) |
| [[SNU-423 (line)]] | alt | 58.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.23× (z +23.8) | — |
| [[A-172 (line)]] | wt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +9.4) | — |
| [[A498 (line)]] | wt | 40.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +13.4) | — |
| [[AN3 CA (line)]] | alt | 31.6 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0452× (z -12.7) |
| [[C-33 A (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -10.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 48.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.1) | — |
| [[H4 (line)]] | wt | 32.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -10.7) ⚠ cell-cycle shift, explains ~3% of this change |
| [[HEC-1-A (line)]] | alt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 39.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +12.6) | — |
| [[Hs 766T (line)]] | wt | 54.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +15.8) | — |
| [[LOX-IMVI (line)]] | wt | 35.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 34.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.0) | — |
| [[SNU-1 (line)]] | wt | 26.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 48.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.6) | — |
| [[BT-474 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4456), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN8]] | +0.66 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[CLN5]] | +0.66 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[TAF9]] | +0.66 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ARMT1]] | +0.65 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[PRKAR1A]] | +0.64 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[MED12]] | +0.64 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[TRAM2-AS1]] | +0.64 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[ZNF641]] | +0.63 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[SLC39A1]] | +0.63 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[CGGBP1]] | +0.63 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[TAF9B]] | +0.63 | +0.55 / +0.35 | both halves | 1e-04 |  |
| [[LEPROT]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBAK-RBAKDN]] | -0.66 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[ANKRD27]] | -0.66 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[RNF216]] | -0.65 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.63 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[PDPR2P]] | -0.62 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[ANKS3]] | -0.61 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[SNRPD2]] | -0.61 | -0.52 / -0.43 | both halves | 4e-05 |  |
| [[ZNF544]] | -0.61 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[ATG4B]] | -0.60 | -0.32 / -0.56 | both halves | 2e-04 |  |
| [[HERC2P2]] | -0.59 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[MMS19]] | -0.59 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[HERC2P9]] | -0.58 | -0.54 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises RAP2C's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises RAP2C's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC02985]] | B | LINC02985 activity lowers RAP2C's level | lines that do not express LINC02985 (15) vs lines expressing it (35) | 1.30× higher at baseline in the lines without LINC02985 | 0.073 | ⚠ within organs, on part of the lines; also absent: GXYLT2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **-** arm (projection on the module's main direction -0.676). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-9.4, 1.7); signed map (19.8, -18.7). **Vector** length 88.7, 20.3% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.5 | +7.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.9 | +16.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +21.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | +5.5 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | -0.8 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +1.5 | +1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.5 | +0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +0.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.1 | -11.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -12.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.4 | -9.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.1 | +0.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -1.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.4 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | RAP2C, member of RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.2 — chrX:132,203,024-132,219,480 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp313B211 |
| Gene groups (HGNC) | RAS type GTPase family |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3L5](https://www.uniprot.org/uniprotkb/Q9Y3L5) (Ras-related protein Rap-2c):

> Small GTP-binding protein which cycles between a GDP-bound inactive and a GTP-bound active form. May play a role in cytoskeletal rearrangements and regulate cell spreading through activation of the effector TNIK. May play a role in SRE-mediated gene transcription.

**Summary**, from NCBI Gene [57826](https://www.ncbi.nlm.nih.gov/gene/57826):

> The protein encoded by this gene is a member of the Ras-related protein subfamily of the Ras GTPase superfamily. Members of this family are small GTPases that act as molecular switches to regulate cellular proliferation, differentiation, and apoptosis. This protein has been reported to activate in vitro transcriptional activity of the serum response element. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Sep 2012]

**Accessions** — [HGNC:21165](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21165) · Entrez [57826](https://www.ncbi.nlm.nih.gov/gene/57826) · UniProt [Q9Y3L5](https://www.uniprot.org/uniprotkb/Q9Y3L5) · Ensembl [ENSG00000123728](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123728)

## Data

Gene col 4456: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4456); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4456, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4456]; `tensor/DDL_lfc|DDL_z.npy` [4456]; `embed/gene_vectors.npy` [4456]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4456 or target_col == 4456). Every well: [[RAP2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAP2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
