---
symbol: "CFAP69"
type: "gene"
col: 2666
ensembl_id: "ENSG00000105792"
name: "cilia and flagella associated protein 69"
location: "7q21.13"
module: 205
arm: "+"
pooled_cpm: 22.61
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 18
n_dd_up_clean: 22
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/205"]
generated_by: "tahoemap"
---

# CFAP69

*cilia and flagella associated protein 69* — 7q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.04× (z +13.2, q 3e-37, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.516× (z -8.7, q 2e-15, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOK]] (+0.70, fdr 7e-06), [[ANKRD42]] (+0.66, fdr 7e-06), [[TMEM67]] (+0.63, fdr 7e-06); moves opposite to [[FAM131A]] (-0.46, fdr 4e-05), [[MDFI]] (-0.45, fdr 6e-05), [[CDYL2]] (-0.45, fdr 4e-05).
> It is in [[Module 205]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2666.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +13.2 | 3e-37 | 35/48 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.11×** | +9.8 | 4e-20 | 41/48 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.09×** | +9.6 | 1e-19 | 41/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +8.3 | 2e-14 | 33/45 (SW1417, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.71×** | +7.0 | 3e-10 | 30/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +6.2 | 6e-08 | 27/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +5.1 | 2e-05 | 22/45 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +5.1 | 3e-05 | 26/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.44×** | +4.8 | 1e-04 | 24/47 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +4.6 | 2e-04 | 24/48 (SW480, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +4.2 | 0.001 | 25/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +4.2 | 0.001 | 21/47 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.004 | 22/48 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.22×** | +3.7 | 0.009 | 14/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +3.5 | 0.017 | 19/46 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.029 | 17/48 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **1.46×** | +3.2 | 0.038 | 7/48 (J82, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.040 | 13/47 (AsPC-1, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2666.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.516×** | -8.7 | 2e-15 | 37/48 (LoVo, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.636×** | -8.4 | 1e-14 | 37/48 (SW480, SW48, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.631×** | -6.1 | 3e-07 | 29/48 (SW48, NCI-H460, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.662×** | -5.4 | 9e-06 | 29/44 (hTERT-HPNE, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.668×** | -5.3 | 1e-05 | 27/45 (SK-MEL-2, LoVo, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **0.439×** | -5.1 | 3e-05 | 26/46 (LS 180, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.668×** | -5.1 | 3e-05 | 26/47 (NCI-H1573, HT-29, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.702×** | -4.6 | 2e-04 | 23/47 (NCI-H23, NCI-H460, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.587×** | -4.6 | 3e-04 | 23/47 (HT-29, NCI-H2030, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.787×** | -4.5 | 5e-04 | 26/48 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.723×** | -4.3 | 0.001 | 19/48 (SW48, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.734×** | -4.1 | 0.002 | 22/47 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.737×** | -4.0 | 0.003 | 22/47 (HT-29, H4, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.745×** | -3.7 | 0.008 | 16/48 (CFPAC-1, SW48, …) | top dose only |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.718×** | -3.5 | 0.016 | 15/48 (Hs 766T, SW 1271, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | 0.840× | -3.2 | 0.037 | 18/48 (A549, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2666. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.97 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.55× (z +11.1) | — |
| [[SW480 (line)]] | alt | 41.5 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.444× (z -12.0) |
| [[COLO 205 (line)]] | alt | 40.9 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.167× (z -10.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.220× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 13.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +10.9) | — |
| [[A498 (line)]] | wt | 34.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.5) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 10.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.44× (z +9.3) | — |
| [[LoVo (line)]] | wt | 25.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.287× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 27.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0753× (z -16.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 37.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -14.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 33.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.111× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[H4 (line)]] | wt | 28.6 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0885× (z -12.3) |
| [[HCT15 (line)]] | alt | 31.2 | 0 | 1 | — | [[PH-797804 (drug)]] 0.5 µM 0.0774× (z -8.7) |
| [[HOP62 (line)]] | alt | 15.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[HT-29 (line)]] | alt | 23.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 15.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.152× (z -8.6) ⚠ transcription drop |
| [[KATO III (line)]] | alt | 22.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.238× (z -8.5) |
| [[LS 180 (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 32.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 18.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +13.1) | — |
| [[NCI-H23 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -9.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 26.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +10.9) | — |
| [[RPMI-7951 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -10.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 59.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.101× (z -14.8) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2666), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOK]] | +0.70 | +0.68 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[ANKRD42]] | +0.66 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[TMEM67]] | +0.63 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[DRC3]] | +0.62 | +0.45 / +0.67 | both halves | 3e-05 | same gene group; STRING 461 |
| [[CCDC157]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[DNAH7]] | +0.58 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[MORN2]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[FAM174A]] | +0.57 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[WDR19]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[ZNF487]] | +0.55 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[INTU]] | +0.55 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[IFT57]] | +0.54 | +0.58 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM131A]] | -0.46 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[MDFI]] | -0.45 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[CDYL2]] | -0.45 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[MICALL1]] | -0.44 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[SPSB1]] | -0.43 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[NPL]] | -0.43 | -0.03 / -0.47 | ⚠ not reproduced | 0.006 |  |
| [[ADCY7]] | -0.43 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[RTN4]] | -0.43 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[EXTL3]] | -0.42 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[LINC02236]] | -0.42 | -0.41 / -0.37 | both halves | 9e-05 |  |
| [[PSME4]] | -0.41 | -0.46 / -0.33 | both halves | 1e-04 | same gene group |
| [[SCEL]] | -0.41 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[MELTF]] | -0.41 | -0.30 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 205]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.795). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-42.1, 21.3); signed map (-19.1, 4.6). **Vector** length 102, 25.4% of its response variance represented; |z| ≥ 3 in 1,197 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.9 | +6.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.4 | +4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.1 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +8.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[IQ 1 (drug)]] 5 µM |  | +2.0 | +1.8 |
|  | [[AZD-8055 (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +2.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.6 | -8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.4 | -8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.7 | -4.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.7 | -6.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.0 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.9 | -4.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.5 | -5.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.3 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 69 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.13 — chr7:90,245,174-90,311,063 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21062, FAP69; previously C7orf63 |
| Gene groups (HGNC) | Cilia and flagella associated; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [A5D8W1](https://www.uniprot.org/uniprotkb/A5D8W1) (Cilia- and flagella-associated protein 69):

> Cilium- and flagellum-associated protein. In the olfactory epithelium, regulates the speed of activation and termination of the odor response and thus contributes to the robustness of olfactory transduction pathways (By similarity). Required for sperm flagellum assembly and stability.

**Summary**, from NCBI Gene [79846](https://www.ncbi.nlm.nih.gov/gene/79846):

> Acts upstream of or within sperm axoneme assembly. Located in cytoplasm and sperm midpiece. Implicated in spermatogenic failure 24. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26107](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26107) · Entrez [79846](https://www.ncbi.nlm.nih.gov/gene/79846) · UniProt [A5D8W1](https://www.uniprot.org/uniprotkb/A5D8W1) · Ensembl [ENSG00000105792](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105792)

## Data

Gene col 2666: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2666); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2666, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2666]; `tensor/DDL_lfc|DDL_z.npy` [2666]; `embed/gene_vectors.npy` [2666]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2666 or target_col == 2666). Every well: [[CFAP69 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP69.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
