---
symbol: "ADSS2"
type: "gene"
col: 432
ensembl_id: "ENSG00000035687"
name: "adenylosuccinate synthase 2"
location: "1q44"
module: 48
arm: "-"
pooled_cpm: 65.56
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# ADSS2

*adenylosuccinate synthase 2* — 1q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.49× (z +13.0, q 9e-36, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.740× (z -7.0, q 2e-09, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC39A10]] (+0.62, fdr 1e-05), [[UBQLN4]] (+0.61, fdr 1e-05), [[OXCT1]] (+0.61, fdr 1e-05); moves opposite to [[MIR210HG]] (-0.68, fdr 7e-06), [[NDUFA3]] (-0.64, fdr 1e-05), [[RNF114]] (-0.62, fdr 2e-05).
> It sits in the **-** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 432.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +13.0 | 9e-36 | 32/48 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +11.2 | 2e-26 | 26/42 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +10.2 | 5e-22 | 34/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +9.8 | 2e-20 | 30/48 (CFPAC-1, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +9.3 | 1e-18 | 33/48 (HT-29, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.46×** | +8.5 | 3e-15 | 35/48 (NCI-H1573, COLO 205, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.48×** | +8.3 | 8e-15 | 33/44 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +7.1 | 1e-10 | 28/48 (C32, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.26×** | +5.1 | 3e-05 | 22/48 (SNU-423, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +5.0 | 4e-05 | 20/48 (CFPAC-1, J82, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.4 | 5e-04 | 21/48 (CFPAC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +4.4 | 5e-04 | 19/48 (C32, NCI-H460, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.004 | 19/48 (A-172, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.029 | 21/50 (A-172, HOP62, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.15× | +3.3 | 0.038 | 14/47 (H4, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 432.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.740×** | -7.0 | 2e-09 | 28/48 (BT-474, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.771×** | -6.0 | 6e-07 | 26/48 (Hs 766T, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **0.776×** | -5.9 | 9e-07 | 27/48 (J82, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.594×** | -5.8 | 9e-07 | 28/49 (RKO, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **0.793×** | -5.3 | 1e-05 | 27/48 (LS 180, SW 1088, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.815×** | -4.7 | 2e-04 | 23/48 (SW480, A498, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~19% of this change | **0.820×** | -4.6 | 4e-04 | 22/47 (NCI-H661, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.751×** | -4.1 | 0.003 | 22/47 (RKO, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.839× | -4.1 | 0.003 | 17/48 (SW48, HepG2/C3A, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -3.9 | 0.005 | 21/48 (SNU-423, KATO III, …) | two highest doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.857× | -3.6 | 0.020 | 17/48 (HepG2/C3A, H4, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.785×** | -3.4 | 0.028 | 8/48 (PANC-1, hTERT-HPNE, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 432. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 59.4 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 47.6 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +13.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 78.0 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 66.6 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.24× (z +9.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.64× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 75.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.3) | — |
| [[A-427 (line)]] | wt | 53.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -20.8) |
| [[A549 (line)]] | wt | 47.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +9.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 64.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +17.0) | — |
| [[J82 (line)]] | alt | 67.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.2) | [[Digitoxin (drug)]] 5 µM 0.483× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[A498 (line)]] | wt | 101 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.1) | — |
| [[BT-474 (line)]] | alt | 81.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.4) | — |
| [[H4 (line)]] | wt | 42.4 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0610× (z -10.2) |
| [[HCT15 (line)]] | alt | 46.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 57.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +17.2) | — |
| [[HS-578T (line)]] | alt | 51.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.7) | — |
| [[hTERT-HPNE (line)]] | wt | 61.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +10.7) | — |
| [[LoVo (line)]] | wt | 37.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 70.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 39.6 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.48× (z +10.6) ⚠ toxic | — |
| [[NCI-H23 (line)]] | alt | 38.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.106× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~19% of this change |
| [[SW 900 (line)]] | alt | 81.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.4) | — |
| [[A-172 (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 81.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 147 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 65.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 78.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 72.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 432), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*37 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC39A10]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[UBQLN4]] | +0.61 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[OXCT1]] | +0.61 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[DARS2]] | +0.59 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[STK26]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[SNX5]] | +0.57 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[PAK2]] | +0.57 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[MCCC2]] | +0.57 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[ATP11C]] | +0.57 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[RCC2]] | +0.57 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[SLC5A6]] | +0.56 | +0.55 / +0.39 | both halves | 5e-05 |  |
| [[GSPT1]] | +0.56 | +0.55 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*63 of its nearest partners move opposite, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR210HG]] | -0.68 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[NDUFA3]] | -0.64 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[RNF114]] | -0.62 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[COX6A1]] | -0.62 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ANAPC11]] | -0.61 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[NSFP1]] | -0.61 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[SEC61G]] | -0.60 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[SDHAF1]] | -0.60 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[CHMP2A]] | -0.59 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[PCSK1N]] | -0.58 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[WIPF2]] | -0.58 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[KRT10]] ⚠ | -0.58 | -0.43 / -0.61 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MIF]] | -0.58 | -0.50 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **-** arm (projection on the module's main direction -0.603). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-48.4, -19.2); signed map (21.7, -35.1). **Vector** length 115, 28.6% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.7 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +11.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.5 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +7.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.2 | +8.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +4.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.3 | +2.5 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.6 | -5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.4 | -7.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | -5.0 | -5.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -4.3 | -6.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.8 | -4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -4.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.5 | -5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -2.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.0 | -3.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -1.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | adenylosuccinate synthase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q44 — chr1:244,408,494-244,451,909 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ADSS |
| Gene groups (HGNC) | Adenylosuccinate synthase family |
| Reactome | 3 pathways, smallest: Purine ribonucleoside monophosphate biosynthesis; Nucleotide biosynthesis; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [P30520](https://www.uniprot.org/uniprotkb/P30520) (Adenylosuccinate synthetase isozyme 2):

> Plays an important role in the de novo pathway and in the salvage pathway of purine nucleotide biosynthesis. Catalyzes the first committed step in the biosynthesis of AMP from IMP.

**Summary**, from NCBI Gene [159](https://www.ncbi.nlm.nih.gov/gene/159):

> This gene encodes the enzyme adenylosuccinate synthetase which catalyzes the first committed step in the conversion of inosine monophosphate to adenosine monophosphate. A pseudogene of this gene is found on chromosome 17.[provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:292](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:292) · Entrez [159](https://www.ncbi.nlm.nih.gov/gene/159) · UniProt [P30520](https://www.uniprot.org/uniprotkb/P30520) · Ensembl [ENSG00000035687](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000035687)

## Data

Gene col 432: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 432); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 432, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 432]; `tensor/DDL_lfc|DDL_z.npy` [432]; `embed/gene_vectors.npy` [432]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 432 or target_col == 432). Every well: [[ADSS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADSS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
