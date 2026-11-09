---
symbol: "ERO1B"
type: "gene"
col: 1466
ensembl_id: "ENSG00000086619"
name: "endoplasmic reticulum oxidoreductase 1 beta"
location: "1q42.3"
module: 4
arm: "-"
pooled_cpm: 55.4
n_lines_expressing: 47
n_dd_up: 27
n_dd_down: 11
n_dd_up_clean: 24
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 4
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# ERO1B

*endoplasmic reticulum oxidoreductase 1 beta* — 1q42.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.43× (z +28.4, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.681× (z -4.7, q 0.002, down in 26 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Busulfan (drug)]] 0.05 µM: 0.712× (z -4.1, q 0.011, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC3-DT]] (+0.69, fdr 7e-06), [[RSRP1]] (+0.65, fdr 7e-06), [[BET1]] (+0.63, fdr 1e-05); moves opposite to [[DIS3L2]] (-0.66, fdr 7e-06), [[LCLAT1]] (-0.65, fdr 7e-06), [[AGK]] (-0.65, fdr 8e-06).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[TSPYL2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1466.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.43×** | +28.4 | 0e+00 | 43/45 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.45×** | +25.9 | 0e+00 | 45/46 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.16×** | +14.0 | 5e-42 | 41/45 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **3.22×** | +13.7 | 3e-40 | 39/45 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.65×** | +11.9 | 2e-30 | 37/45 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.65×** | +11.4 | 5e-28 | 39/45 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.57×** | +11.0 | 2e-26 | 40/47 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.20×** | +9.6 | 9e-20 | 41/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +8.5 | 9e-16 | 35/44 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.88×** | +7.7 | 1e-12 | 36/45 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.83×** | +7.3 | 1e-11 | 34/45 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.3 | 2e-11 | 28/45 (A-172, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.81×** | +7.2 | 2e-11 | 36/45 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +6.5 | 4e-09 | 31/44 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.63×** | +5.9 | 1e-07 | 29/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +5.2 | 8e-06 | 32/46 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +5.2 | 8e-06 | 31/45 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1466.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.681×** | -4.7 | 0.002 | 26/45 (C32, A-427, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.712×** | -4.1 | 0.011 | 24/46 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.540×** | -3.9 | 0.018 | 26/45 (C32, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.745×** | -3.6 | 0.049 | 22/45 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.746×** | -3.4 | 0.063 | 22/45 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.588×** | -3.4 | 0.063 | 21/45 (SHP-77, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.761×** | -3.3 | 0.063 | 20/45 (HT-29, NCI-H2347, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.763×** | -3.3 | 0.063 | 22/46 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.597×** | -3.3 | 0.063 | 18/44 (CFPAC-1, C32, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.756×** | -3.3 | 0.063 | 16/36 (SW 900, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.771×** | -3.2 | 0.083 | 16/45 (NCI-H1573, HCT15, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.779× | -3.0 | 0.11 | 23/46 (CFPAC-1, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1466. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 130 | 16 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +29.6) | — |
| [[SW480 (line)]] | alt | 56.6 | 14 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +27.7) | — |
| [[PANC-1 (line)]] | alt | 40.5 | 13 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +22.8) | — |
| [[A-172 (line)]] | wt | 49.6 | 8 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +21.6) | — |
| [[BT-474 (line)]] | alt | 37.5 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.35× (z +14.7) | — |
| [[LOX-IMVI (line)]] | wt | 27.0 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.95× (z +21.1) | — |
| [[C32 (line)]] | wt | 92.2 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +23.2) | — |
| [[HOP62 (line)]] | alt | 40.0 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.04× (z +20.0) | — |
| [[Panc 03.27 (line)]] | alt | 57.3 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.53× (z +20.9) | — |
| [[NCI-H2347 (line)]] | alt | 42.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +19.3) | — |
| [[SW 900 (line)]] | alt | 155 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.79× (z +17.9) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -9.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 93.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +24.9) | — |
| [[A498 (line)]] | wt | 40.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +28.4) | — |
| [[hTERT-HPNE (line)]] | wt | 35.6 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.07× (z +14.0) | — |
| [[RKO (line)]] | wt | 64.7 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.51× (z +16.4) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -11.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 41.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +19.5) | — |
| [[SK-MEL-2 (line)]] | alt | 36.3 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +13.2) | — |
| [[HEC-1-A (line)]] | alt | 43.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +16.3) | — |
| [[A549 (line)]] | wt | 52.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.25× (z +18.9) | — |
| [[C-33 A (line)]] | alt | 33.3 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +12.9) | — |
| [[H4 (line)]] | wt | 67.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +13.3) | — |
| [[Hs 766T (line)]] | wt | 23.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +16.7) | — |
| [[HT-29 (line)]] | alt | 27.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.14× (z +13.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 51.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +20.2) | — |
| [[NCI-H1792 (line)]] | alt | 48.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.05× (z +18.3) | — |
| [[NCI-H2030 (line)]] | alt | 41.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +23.6) | — |
| [[SNU-1 (line)]] | wt | 60.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.98× (z +13.6) | — |
| [[SNU-423 (line)]] | alt | 62.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +14.5) | — |
| [[SW48 (line)]] | wt | 41.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +16.5) | — |
| [[A-427 (line)]] | wt | 160 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.8) | — |
| [[AN3 CA (line)]] | alt | 62.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +11.9) | — |
| [[CFPAC-1 (line)]] | alt | 63.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +18.9) | — |
| [[COLO 205 (line)]] | alt | 82.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +16.2) | — |
| [[HCT15 (line)]] | alt | 105 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +12.6) | — |
| [[HepG2_C3A (line)]] | wt | 51.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.86× (z +13.7) | — |
| [[J82 (line)]] | alt | 47.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.57× (z +14.7) | — |
| [[LoVo (line)]] | wt | 49.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +14.4) | — |
| [[LS 180 (line)]] | wt | 29.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 75.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.30× (z +21.9) | — |
| [[CHP-212 (line)]] | wt | 35.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.68× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 24.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 100 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.65× (z +13.9) | — |
| [[AsPC-1 (line)]] | alt | 9.68 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.71 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.80 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1466), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC3-DT]] | +0.69 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[RSRP1]] | +0.65 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[BET1]] | +0.63 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SMIM14]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[C12orf57]] | +0.62 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[DNAJB9]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 | STRING 616 |
| [[FAM117A]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[TESK2]] | +0.60 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[GTF2B]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[STX5-DT]] | +0.59 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[PLPP5]] | +0.59 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[STX5]] | +0.59 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIS3L2]] | -0.66 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[LCLAT1]] | -0.65 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[AGK]] | -0.65 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[MRPS27]] | -0.64 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[COA1]] | -0.62 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[LTV1]] | -0.60 | -0.49 / -0.70 | both halves | 1e-05 |  |
| [[POLR1A]] | -0.60 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[FARSB]] | -0.59 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[NOL10]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[GFM1]] | -0.58 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[DDX10]] | -0.58 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[ELAC2]] | -0.58 | -0.47 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ERO1B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GPR137B]] | C | GPR137B activity raises ERO1B's level | lines that do not express GPR137B (3) vs lines expressing it (47) | 4.41× lower at baseline in the lines without GPR137B | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: CRYBG3, ERO1B, TEX14; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPYL2]] | C | ERO1B activity raises TSPYL2's level | lines that do not express ERO1B (3) vs lines expressing it (47) | 2.70× lower at baseline in the lines without ERO1B | 0.052 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF26, ZNF483, RUNDC3A-AS1 |
| [[GPR137B]] | C | ERO1B activity raises GPR137B's level | lines that do not express ERO1B (3) vs lines expressing it (47) | 3.22× lower at baseline in the lines without ERO1B | 0.067 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF26, ZNF483, RUNDC3A-AS1; co-absent with the target |
| [[MSH3]] | C | ERO1B activity raises MSH3's level | lines that do not express ERO1B (3) vs lines expressing it (47) | 1.64× lower at baseline in the lines without ERO1B | 0.080 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF26, ZNF483, RUNDC3A-AS1 |
| [[YLPM1]] | C | ERO1B activity raises YLPM1's level | lines that do not express ERO1B (3) vs lines expressing it (47) | 1.72× lower at baseline in the lines without ERO1B | 0.097 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF26, ZNF483, RUNDC3A-AS1 |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.628). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-17.8, -42.5); signed map (-11.0, 9.4). **Vector** length 105, 32.4% of its response variance represented; |z| ≥ 3 in 1,225 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.3 | +14.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +25.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +11.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +11.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +5.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.9 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +7.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.9 | -4.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | -1.0 |
|  | [[EX229 (drug)]] 5 µM |  | -5.8 | -3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.3 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.1 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.3 | -1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | endoplasmic reticulum oxidoreductase 1 beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.3 — chr1:236,214,681-236,282,019 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ERO1-L(beta), Ero1beta; previously ERO1LB |
| Gene groups (HGNC) | Flavoproteins |
| Reactome | 2 pathways, smallest: Insulin processing; Peptide hormone metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YB8](https://www.uniprot.org/uniprotkb/Q86YB8) (ERO1-like protein beta):

> Oxidoreductase involved in disulfide bond formation in the endoplasmic reticulum. Efficiently reoxidizes P4HB/PDI, the enzyme catalyzing protein disulfide formation, in order to allow P4HB to sustain additional rounds of disulfide formation. Other protein disulfide isomerase family members can also be reoxidized, but at lower rates compared to P4HB, including PDIA2 (50% of P4HB reoxidation rate), as well as PDIA3, PDIA4, PDIA6 and NXNDC12 (<10%). Following P4HB reoxidation, passes its electrons …

**Summary**, from NCBI Gene [56605](https://www.ncbi.nlm.nih.gov/gene/56605):

> Enables protein-disulfide reductase activity and thiol oxidase activity. Involved in protein folding in endoplasmic reticulum. Predicted to be located in endoplasmic reticulum lumen. Predicted to be active in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14355](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14355) · Entrez [56605](https://www.ncbi.nlm.nih.gov/gene/56605) · UniProt [Q86YB8](https://www.uniprot.org/uniprotkb/Q86YB8) · Ensembl [ENSG00000086619](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086619)

## Data

Gene col 1466: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1466); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1466, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1466]; `tensor/DDL_lfc|DDL_z.npy` [1466]; `embed/gene_vectors.npy` [1466]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1466 or target_col == 1466). Every well: [[ERO1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERO1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
