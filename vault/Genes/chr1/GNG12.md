---
symbol: "GNG12"
type: "gene"
col: 10250
ensembl_id: "ENSG00000172380"
name: "G protein subunit gamma 12"
location: "1p31.3"
module: 111
arm: "+"
pooled_cpm: 115.31
n_lines_expressing: 48
n_dd_up: 14
n_dd_down: 15
n_dd_up_clean: 6
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# GNG12

*G protein subunit gamma 12* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.20× (z +14.2, q 8e-43, up in 38 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 1.70× (z +10.0, q 3e-21, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.491× (z -13.3, q 1e-37, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMGT1]] (+0.67, fdr 7e-06), [[CMTM6]] (+0.66, fdr 1e-05), [[ACTR3]] (+0.65, fdr 1e-05); moves opposite to [[NKAP]] (-0.66, fdr 7e-06), [[SMIM26]] (-0.66, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[SNHG7]] (-0.65, fdr 1e-05), [[SUGP1]] (-0.65, fdr 1e-05).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10250.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +14.2 | 8e-43 | 38/41 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.02×** | +13.2 | 3e-37 | 42/47 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +10.9 | 2e-25 | 36/43 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.70×** | +10.0 | 3e-21 | 42/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +9.6 | 1e-19 | 39/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +6.5 | 7e-09 | 34/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +6.3 | 3e-08 | 33/45 (C32, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +6.2 | 4e-08 | 33/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.54×** | +4.2 | 0.002 | 24/46 (C32, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +4.0 | 0.004 | 23/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.22×** | +3.8 | 0.008 | 24/46 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.014 | 22/47 (J82, SK-MEL-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | **1.21×** | +3.5 | 0.018 | 22/46 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.4 | 0.029 | 17/36 (SNU-423, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.20× | +3.4 | 0.029 | 16/45 (HOP62, SNU-423, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10250.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.491×** | -13.3 | 1e-37 | 42/46 (HOP62, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.510×** | -12.6 | 6e-34 | 41/46 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.679×** | -7.2 | 9e-11 | 37/46 (HOP62, A549, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.760×** | -7.1 | 2e-10 | 27/47 (SW1417, COLO 205, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.766×** | -6.9 | 7e-10 | 23/46 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.695×** | -6.6 | 5e-09 | 33/45 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.761×** | -5.1 | 2e-05 | 30/46 (AsPC-1, RKO, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.620×** | -4.7 | 2e-04 | 33/46 (RKO, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.638×** | -4.4 | 7e-04 | 29/46 (LOX-IMVI, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.652×** | -4.2 | 0.002 | 23/46 (MIA PaCa-2, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.659×** | -4.1 | 0.002 | 24/46 (SW48, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.810×** | -3.9 | 0.004 | 20/46 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.715×** | -3.8 | 0.005 | 26/46 (HEC-1-A, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.818×** | -3.5 | 0.021 | 20/45 (H4, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.704×** | -3.4 | 0.023 | 21/46 (SW1417, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.845× | -3.1 | 0.052 | 19/46 (NCI-H2347, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10250. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 154 | 6 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +15.7) | [[Panobinostat (drug)]] 0.5 µM 0.501× (z -8.6) |
| [[C32 (line)]] | wt | 152 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +9.3) | — |
| [[A549 (line)]] | wt | 104 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +14.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.314× (z -13.0) |
| [[HOP62 (line)]] | alt | 116 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +13.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.261× (z -14.1) |
| [[HS-578T (line)]] | alt | 222 | 5 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.38× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.433× (z -9.4) |
| [[PANC-1 (line)]] | alt | 114 | 4 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -11.2) |
| [[SW480 (line)]] | alt | 50.7 | 4 (1 ⚠) | 1 | [[Digitoxin (drug)]] 0.5 µM 2.57× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.463× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 134 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -11.1) |
| [[NCI-H1792 (line)]] | alt | 120 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -9.8) |
| [[RKO (line)]] | wt | 167 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -13.8) |
| [[SK-MEL-2 (line)]] | alt | 144 | 2 (2 ⚠) | 2 | [[Niclosamide (olamine) (drug)]] 5 µM 2.38× (z +9.3) ⚠ toxic | [[Panobinostat (drug)]] 5 µM 0.382× (z -10.8) |
| [[SNU-423 (line)]] | alt | 132 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.78× (z +14.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.458× (z -8.7) |
| [[HT-29 (line)]] | alt | 163 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -11.6) |
| [[J82 (line)]] | alt | 148 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.18× (z +9.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.428× (z -10.9) |
| [[LOX-IMVI (line)]] | wt | 202 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.318× (z -12.5) |
| [[LS 180 (line)]] | wt | 128 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.439× (z -9.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.462× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 70.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.15× (z +15.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 132 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.396× (z -10.4) |
| [[A-172 (line)]] | wt | 162 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.2) | — |
| [[A-427 (line)]] | wt | 75.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +11.4) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 127 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -11.3) |
| [[H4 (line)]] | wt | 247 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +9.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.280× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 128 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.459× (z -9.9) |
| [[LoVo (line)]] | wt | 74.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.31× (z +9.5) ⚠ toxic | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.489× (z -8.5) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 151 | 1 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 114 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.22× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 42.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +9.9) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 0.05 µM 0.196× (z -10.0) |
| [[SW1417 (line)]] | alt | 116 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.348× (z -12.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -12.6) |
| [[SW48 (line)]] | wt | 73.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -9.9) |
| [[C-33 A (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.362× (z -9.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 91.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.610× (z -8.9) |
| [[Hs 766T (line)]] | wt | 89.8 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.180× (z -8.7) ⚠ toxic |
| [[KATO III (line)]] | alt | 71.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.442× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 47.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 110 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.411× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.42× (z +9.5) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 151 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 110 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +9.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.61 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 185 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 89.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10250), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMGT1]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[CMTM6]] | +0.66 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[ACTR3]] | +0.65 | +0.50 / +0.74 | both halves | 1e-05 | pathway: Leishmania infection |
| [[CDC42]] | +0.65 | +0.38 / +0.79 | both halves | 6e-05 | pathway: G beta:gamma signalling through CDC42; STRING 593 |
| [[FKBP1A]] | +0.64 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[VMA21]] | +0.63 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[MOB1A]] | +0.63 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[SEPTIN11]] | +0.63 | +0.41 / +0.70 | both halves | 4e-05 |  |
| [[TGOLN2]] | +0.63 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[CDK6]] | +0.63 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[DR1]] | +0.62 | +0.42 / +0.69 | both halves | 4e-05 |  |
| [[ERLIN2]] | +0.61 | +0.30 / +0.63 | both halves | 2e-04 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 6 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKAP]] | -0.66 | -0.65 / -0.65 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | -0.66 | -0.52 / -0.69 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG7]] | -0.65 | -0.54 / -0.71 | both halves | 1e-05 |  |
| [[SUGP1]] | -0.65 | -0.72 / -0.57 | both halves | 1e-05 |  |
| [[ADPRM]] | -0.64 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[ADPRS]] | -0.64 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[ZNF766]] | -0.64 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[TMEM101]] | -0.63 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[PCGF1]] ⚠ | -0.63 | -0.37 / -0.67 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZRSR2]] | -0.62 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[TMEM258]] | -0.62 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[MPHOSPH10]] | -0.62 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[LEO1]] | -0.62 | -0.41 / -0.67 | both halves | 4e-05 | pathway: Signaling by WNT |
| [[FUT11]] | -0.62 | -0.26 / -0.67 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.7, -13.2); signed map (9.8, -9.5). **Vector** length 133, 43.7% of its response variance represented; |z| ≥ 3 in 1,209 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *FCGR3A-mediated phagocytosis* (reactome, mean cos +0.51 to 6); *Leishmania phagocytosis* (reactome, mean cos +0.51 to 6); *Parasite infection* (reactome, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +12.1 | +13.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.5 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.5 | +10.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.4 | +6.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +5.7 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.9 | +2.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.8 | +2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +0.8 |
| fall | [[venetoclax (drug)]] 5 µM |  | -5.1 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.6 | -6.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.3 | -4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.3 | -4.7 |
|  | [[EX229 (drug)]] 5 µM |  | -4.0 | -4.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.9 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit gamma 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:67,701,475-67,833,467 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | G protein subunits gamma |
| Hallmark sets | COAGULATION |
| Reactome | 66 pathways, smallest: G beta:gamma signalling through BTK; Prostacyclin signalling through prostacyclin receptor; G beta:gamma signalling through PLC beta |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBI6](https://www.uniprot.org/uniprotkb/Q9UBI6) (Guanine nucleotide-binding protein G(I)/G(S)/G(O) subunit gamma-12):

> Guanine nucleotide-binding proteins (G proteins) are involved as a modulator or transducer in various transmembrane signaling systems. The beta and gamma chains are required for the GTPase activity, for replacement of GDP by GTP, and for G protein-effector interaction.

**Summary**, from NCBI Gene [55970](https://www.ncbi.nlm.nih.gov/gene/55970):

> Enables PDZ domain binding activity. Predicted to be involved in G protein-coupled receptor signaling pathway. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19663](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19663) · Entrez [55970](https://www.ncbi.nlm.nih.gov/gene/55970) · UniProt [Q9UBI6](https://www.uniprot.org/uniprotkb/Q9UBI6) · Ensembl [ENSG00000172380](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172380)

## Data

Gene col 10250: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10250); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10250, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10250]; `tensor/DDL_lfc|DDL_z.npy` [10250]; `embed/gene_vectors.npy` [10250]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10250 or target_col == 10250). Every well: [[GNG12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNG12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
