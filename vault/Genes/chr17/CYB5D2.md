---
symbol: "CYB5D2"
type: "gene"
col: 9530
ensembl_id: "ENSG00000167740"
name: "cytochrome b5 domain containing 2"
location: "17p13.2"
module: 23
arm: "+"
pooled_cpm: 13.49
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# CYB5D2

*cytochrome b5 domain containing 2* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 22.0× (z +54.6, q 0e+00, up in 37 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.12× (z +18.8, q 0e+00, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.593× (z -9.2, q 2e-17, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC27-AS1]] (+0.82, fdr 7e-06), [[MSTO1]] (+0.75, fdr 7e-06), [[AHI1-DT]] (+0.74, fdr 5e-05); moves opposite to [[MRPL17]] (-0.68, fdr 2e-05), [[PUSL1]] (-0.67, fdr 1e-04), [[TRIM11]] (-0.65, fdr 3e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KATNAL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9530.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **22.0×** | +54.6 | 0e+00 | 37/37 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **23.9×** | +52.8 | 0e+00 | 29/29 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **13.0×** | +41.9 | 0e+00 | 32/32 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.12×** | +18.8 | 0e+00 | 36/47 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +15.8 | 0e+00 | 37/46 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.63×** | +8.6 | 9e-16 | 25/46 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.45×** | +8.3 | 1e-14 | 13/22 (NCI-H2030, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +7.7 | 7e-13 | 24/47 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +7.6 | 1e-12 | 24/48 (J82, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.48×** | +6.9 | 2e-10 | 23/47 (SW480, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +6.1 | 7e-08 | 19/46 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +5.3 | 5e-06 | 19/43 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +5.2 | 8e-06 | 16/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.8 | 6e-05 | 17/42 (NCI-H2030, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +4.4 | 3e-04 | 11/48 (KATO III, AN3 CA, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +4.2 | 1e-03 | 12/48 (SW480, HCT15, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.004 | 9/47 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.013 | 5/47 (COLO 205, A-172, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.14× | +3.3 | 0.024 | 7/48 (J82, NCI-H460, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.036 | 3/48 (SW480, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.048 | 7/47 (PANC-1, KATO III, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.048 | 6/48 (SW480, A-427, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9530.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.593×** | -9.2 | 2e-17 | 30/48 (NCI-H1573, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.609×** | -8.8 | 6e-16 | 28/47 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.707×** | -6.1 | 2e-07 | 19/47 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.709×** | -6.1 | 2e-07 | 22/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.703×** | -5.9 | 5e-07 | 19/48 (SK-MEL-2, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.631×** | -4.2 | 0.002 | 15/44 (A-427, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.792×** | -4.1 | 0.003 | 15/46 (Panc 03.27, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.798×** | -4.0 | 0.005 | 16/48 (SW480, SW 1088, …) | all doses, stronger at high dose |  |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | **0.808×** | -3.8 | 0.010 | 15/47 (NCI-H1792, HCT15, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.685×** | -3.5 | 0.028 | 10/48 (MIA PaCa-2, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.817×** | -3.4 | 0.038 | 11/47 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 0.5 µM |  | **0.831×** | -3.3 | 0.049 | 8/46 (SW48, SW 900, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.831×** | -3.3 | 0.049 | 7/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9530. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.1 | 13 (10 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 54.7× (z +31.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.53× (z +16.7) | — |
| [[J82 (line)]] | alt | 10.6 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 62.5× (z +21.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 8.54× (z +15.7) | — |
| [[NCI-H2030 (line)]] | alt | 16.2 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 29.2× (z +21.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.06× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 9.71 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 59.3× (z +16.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 6.11× (z +10.6) | — |
| [[C32 (line)]] | wt | 10.4 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 70.4× (z +19.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 13.6× (z +17.8) | — |
| [[HEC-1-A (line)]] | alt | 13.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 23.6× (z +20.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.64× (z +8.8) | — |
| [[LoVo (line)]] | wt | 17.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 76.5× (z +34.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.18× (z +12.8) | — |
| [[LOX-IMVI (line)]] | wt | 6.83 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 65.4× (z +19.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 7.43 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 13.0× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.78× (z +9.7) | — |
| [[SW 900 (line)]] | alt | 9.66 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 40.2× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 5.85× (z +10.1) | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0837× (z -9.3) |
| [[A-172 (line)]] | wt | 17.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.89× (z +15.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 12.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 27.4× (z +22.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 20.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 30.2× (z +22.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 9.52 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 26.6× (z +15.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 12.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 39.7× (z +22.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 15.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 20.5× (z +16.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 10.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 22.5× (z +15.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 6.68 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 22.8× (z +13.8) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 22.8× (z +12.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 18.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 34.4× (z +21.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 13.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 15.6× (z +13.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 15.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.93× (z +13.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 16.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 14.7× (z +15.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 14.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 22.1× (z +26.5) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 12.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 19.1× (z +12.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 9.74 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 27.8× (z +16.7) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 10.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 20.0× (z +15.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 20.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 17.9× (z +26.4) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 13.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.3× (z +12.0) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 18.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 28.3× (z +16.0) ⚠ toxic; transcription drop | [[Decitabine (drug)]] 0.05 µM 0.0965× (z -10.4) |
| [[LS 180 (line)]] | wt | 10.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 18.9× (z +16.3) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 18.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 19.8× (z +17.7) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 17.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 16.0× (z +8.6) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -8.5) |
| [[HCT15 (line)]] | alt | 18.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.6× (z +12.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 9.73 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 18.3× (z +14.6) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9530), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC27-AS1]] | +0.82 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[MSTO1]] | +0.75 | +0.78 / +0.59 | both halves | 7e-06 |  |
| [[AHI1-DT]] | +0.74 | +0.74 / +0.39 | both halves | 5e-05 |  |
| [[KMT2E-AS1]] | +0.74 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[OXA1L-DT]] | +0.74 | +0.79 / +0.34 | both halves | 1e-04 |  |
| [[TMEM202-AS1]] | +0.73 | +0.79 / +0.34 | both halves | 1e-04 |  |
| [[TAF9B]] | +0.72 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[SPTY2D1OS]] | +0.71 | +0.69 / +0.35 | both halves | 1e-04 |  |
| [[UGDH-AS1]] | +0.71 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | +0.71 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[TBCE-1]] | +0.71 | +0.68 / +0.49 | both halves | 1e-05 |  |
| [[HEXIM2-AS1]] | +0.71 | +0.71 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL17]] | -0.68 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[PUSL1]] | -0.67 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[TRIM11]] | -0.65 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[POP7]] | -0.64 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[MPG]] | -0.63 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[WRAP73]] | -0.63 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[MRPL55]] | -0.63 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[TSEN54]] | -0.63 | -0.50 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL2]] | B | KATNAL2 activity raises CYB5D2's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 1.35× lower at baseline in the lines without KATNAL2 | 0.030 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.727). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (5.0, 18.6); signed map (30.9, -15.5). **Vector** length 101, 22.7% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +12.5 | +41.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +11.3 | +54.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.9 | +52.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +18.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +15.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +4.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.4 | +4.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +6.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.3 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.8 | -8.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -9.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -4.7 | -6.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -4.3 | -4.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | -4.2 | -4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -2.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -3.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.1 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -4.2 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome b5 domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:4,143,168-4,187,310 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC32124 |
| Gene groups (HGNC) | Membrane associated progesterone receptor family; Cytochrome b5 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUJ1](https://www.uniprot.org/uniprotkb/Q8WUJ1) (Neuferricin):

> Heme-binding protein which promotes neuronal but not astrocyte differentiation.

**Summary**, from NCBI Gene [124936](https://www.ncbi.nlm.nih.gov/gene/124936):

> Predicted to enable heme binding activity and steroid binding activity. Predicted to be involved in nervous system development. Predicted to act upstream of or within positive regulation of neuron differentiation. Predicted to be located in extracellular region. Predicted to be active in endomembrane system and membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28471](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28471) · Entrez [124936](https://www.ncbi.nlm.nih.gov/gene/124936) · UniProt [Q8WUJ1](https://www.uniprot.org/uniprotkb/Q8WUJ1) · Ensembl [ENSG00000167740](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167740)

## Data

Gene col 9530: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9530); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9530, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9530]; `tensor/DDL_lfc|DDL_z.npy` [9530]; `embed/gene_vectors.npy` [9530]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9530 or target_col == 9530). Every well: [[CYB5D2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYB5D2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
