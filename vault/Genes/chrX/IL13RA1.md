---
symbol: "IL13RA1"
type: "gene"
col: 5235
ensembl_id: "ENSG00000131724"
name: "interleukin 13 receptor subunit alpha 1"
location: "Xq24"
module: 29
arm: "+"
pooled_cpm: 74.54
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 28
n_dd_up_clean: 3
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# IL13RA1

*interleukin 13 receptor subunit alpha 1* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.29× (z +13.8, q 2e-40, up in 42 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.37× (z +7.5, q 1e-11, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.567× (z -13.4, q 6e-38, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM123]] (+0.63, fdr 7e-06), [[MOB1A]] (+0.63, fdr 1e-05), [[CMPK1]] (+0.62, fdr 2e-05); moves opposite to [[CCDC127]] (-0.64, fdr 1e-05), [[NOL7]] (-0.61, fdr 3e-05, ⚠ NOL7 in the vector space only through flagged drug-doses), [[NSUN5P1-1]] (-0.61, fdr 1e-05), [[MED10]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5235.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.29×** | +13.8 | 2e-40 | 42/48 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +12.9 | 9e-36 | 33/41 (HOP62, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +8.2 | 3e-14 | 35/44 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.5 | 1e-11 | 31/47 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.0 | 6e-05 | 28/49 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.6 | 3e-04 | 28/47 (SNU-423, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.21× | +3.2 | 0.12 | 15/47 (PANC-1, A-172, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.12 | 18/47 (NCI-H23, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.21× | +3.0 | 0.16 | 15/47 (HOP62, A549, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5235.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.567×** | -13.4 | 6e-38 | 37/47 (C32, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.478×** | -12.3 | 2e-32 | 39/47 (C32, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.524×** | -10.8 | 1e-24 | 42/47 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.608×** | -8.3 | 2e-14 | 37/47 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.615×** | -8.1 | 6e-14 | 38/47 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.732×** | -7.3 | 2e-11 | 33/47 (C32, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.683×** | -6.3 | 2e-08 | 39/47 (C32, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.776×** | -6.0 | 2e-07 | 30/48 (C32, BT-474, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.708×** | -5.8 | 6e-07 | 28/47 (C32, Hs 766T, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.721×** | -5.4 | 3e-06 | 29/47 (KATO III, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.716×** | -5.3 | 5e-06 | 29/47 (AN3 CA, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.720×** | -5.3 | 7e-06 | 34/48 (HepG2/C3A, RKO, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.723×** | -5.1 | 1e-05 | 31/47 (HepG2/C3A, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.740×** | -5.0 | 2e-05 | 27/47 (HepG2/C3A, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.743×** | -5.0 | 3e-05 | 28/47 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.811×** | -4.9 | 3e-05 | 24/48 (C32, BT-474, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5235. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 166 | 0 | 14 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -20.5) |
| [[HepG2_C3A (line)]] | wt | 164 | 0 | 11 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.232× (z -13.2) |
| [[SW480 (line)]] | alt | 63.5 | 1 (1 ⚠) | 7 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -11.6) |
| [[KATO III (line)]] | alt | 115 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.222× (z -15.4) |
| [[A498 (line)]] | wt | 77.4 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -10.2) |
| [[HT-29 (line)]] | alt | 143 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -16.0) |
| [[LS 180 (line)]] | wt | 45.2 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 2.87× (z +9.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.377× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 27.8 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.32× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.5) | — |
| [[J82 (line)]] | alt | 87.5 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.52× (z +9.8) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.357× (z -10.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.418× (z -9.6) |
| [[LoVo (line)]] | wt | 36.6 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.81× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 103 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.54× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 67.9 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.17× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -12.5) |
| [[A-427 (line)]] | wt | 58.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 2.52× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -14.6) |
| [[COLO 205 (line)]] | alt | 43.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 39.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +12.4) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 50.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +13.8) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 51.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.341× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 58.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -14.9) |
| [[NCI-H1792 (line)]] | alt | 33.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.14× (z +12.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 49.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 46.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 241 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.363× (z -11.4) |
| [[SW1417 (line)]] | alt | 94.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -10.5) |
| [[A-172 (line)]] | wt | 42.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +10.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 72.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.415× (z -8.8) |
| [[Hs 766T (line)]] | wt | 96.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -10.4) |
| [[RKO (line)]] | wt | 58.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.302× (z -10.3) |
| [[SHP-77 (line)]] | alt | 35.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.40× (z +12.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 67.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +8.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 97.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.213× (z -9.7) |
| [[BT-474 (line)]] | alt | 58.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -9.0) |
| [[C-33 A (line)]] | alt | 53.6 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0898× (z -9.1) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 78.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.342× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 53.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +9.6) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 32.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 93.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +10.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 83.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 75.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.53 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5235), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM123]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[MOB1A]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[CMPK1]] | +0.62 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[SCARB2]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[GOLM1]] | +0.61 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[ITM2B]] | +0.61 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[TRIP12]] | +0.60 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[IRAK4]] | +0.60 | +0.37 / +0.64 | both halves | 8e-05 |  |
| [[PPIC]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[FKBP9]] | +0.59 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[LIPA]] | +0.58 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[ERAP1]] | +0.57 | +0.45 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC127]] | -0.64 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[NOL7]] ⚠ | -0.61 | -0.45 / -0.57 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NSUN5P1-1]] | -0.61 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[MED10]] | -0.61 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[PCGF1]] ⚠ | -0.60 | -0.49 / -0.56 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NSUN5P2-1]] ⚠ | -0.60 | -0.40 / -0.61 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[VPS37C]] | -0.59 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[MPHOSPH10]] | -0.57 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[RPP21]] | -0.57 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[C1orf35]] | -0.57 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[SMIM26]] ⚠ | -0.56 | -0.46 / -0.54 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[GTF2H2]] | -0.56 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[RBMX2]] | -0.56 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[SNHG7]] | -0.56 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[ZNF765]] | -0.55 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[POLR2I]] | -0.55 | -0.47 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IL13RA1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.628). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.4, -20.9); signed map (-22.6, -38.1). **Vector** length 114, 33.0% of its response variance represented; |z| ≥ 3 in 1,333 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.6 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +12.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.4 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.0 | +3.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.9 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.5 | -7.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.1 | -4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.8 | -1.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.6 | -5.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.6 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 13 receptor subunit alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:118,727,133-118,794,535 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IL-13Ra, NR4, CD213a1 |
| Gene groups (HGNC) | CD molecules; Interleukin receptors |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, GLYCOLYSIS |
| Reactome | 3 pathways, smallest: Interleukin-4 and Interleukin-13 signaling; Signaling by Interleukins; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [P78552](https://www.uniprot.org/uniprotkb/P78552) (Interleukin-13 receptor subunit alpha-1):

> Binds with low affinity to interleukin-13 (IL13). Together with IL4RA can form a functional receptor for IL13. Also serves as an alternate accessory protein to the common cytokine receptor gamma chain for interleukin-4 (IL4) signaling, but cannot replace the function of IL2RG in allowing enhanced interleukin-2 (IL2) binding activity.

**Summary**, from NCBI Gene [3597](https://www.ncbi.nlm.nih.gov/gene/3597):

> The protein encoded by this gene is a subunit of the interleukin 13 receptor. This subunit forms a receptor complex with IL4 receptor alpha, a subunit shared by IL13 and IL4 receptors. This subunit serves as a primary IL13-binding subunit of the IL13 receptor, and may also be a component of IL4 receptors. This protein has been shown to bind tyrosine kinase TYK2, and thus may mediate the signaling processes that lead to the activation of JAK1, STAT3 and STAT6 induced by IL13 and IL4. [provided …

**Accessions** — [HGNC:5974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5974) · Entrez [3597](https://www.ncbi.nlm.nih.gov/gene/3597) · UniProt [P78552](https://www.uniprot.org/uniprotkb/P78552) · Ensembl [ENSG00000131724](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131724)

## Data

Gene col 5235: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5235); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5235, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5235]; `tensor/DDL_lfc|DDL_z.npy` [5235]; `embed/gene_vectors.npy` [5235]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5235 or target_col == 5235). Every well: [[IL13RA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL13RA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
