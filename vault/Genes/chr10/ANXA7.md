---
symbol: "ANXA7"
type: "gene"
col: 6147
ensembl_id: "ENSG00000138279"
name: "annexin A7"
location: "10q22.2"
module: 64
arm: "+"
pooled_cpm: 62.37
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# ANXA7

*annexin A7* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.63× (z +18.7, q 0e+00, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.782× (z -9.4, q 2e-18, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW480 0.601×, RKO 0.460×, LoVo 0.639×); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.309×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.323×); [[Canagliflozin (drug)]] 5 µM in 1 line (SW 1271 0.0689×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPS10]] (+0.69, fdr 7e-06), [[PSMD6]] (+0.67, fdr 7e-06), [[PSMD4]] (+0.65, fdr 1e-05); moves opposite to [[INTS6L]] (-0.55, fdr 1e-05), [[NOG]] (-0.54, fdr 1e-04), [[TMEM41A]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6147.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +18.7 | 0e+00 | 41/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.91×** | +17.4 | 0e+00 | 43/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.84×** | +16.5 | 0e+00 | 47/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.79×** | +14.8 | 0e+00 | 45/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.64×** | +13.4 | 6e-39 | 39/49 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +12.4 | 4e-33 | 28/40 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +12.3 | 6e-33 | 35/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +10.1 | 2e-22 | 35/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +9.7 | 2e-20 | 33/48 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.97×** | +9.6 | 7e-20 | 35/49 (NCI-H1573, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.42×** | +8.8 | 6e-17 | 25/45 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.25×** | +5.9 | 1e-07 | 24/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +5.8 | 3e-07 | 26/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.28×** | +4.8 | 6e-05 | 19/49 (LOX-IMVI, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~9% of this change | **1.20×** | +4.8 | 8e-05 | 19/47 (HepG2/C3A, HEC-1-A, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.15× | +3.8 | 0.005 | 12/47 (H4, A-172, …) | rises with dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.021 | 17/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.13× | +3.3 | 0.029 | 8/48 (HEC-1-A, NCI-H2030, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.12× | +3.1 | 0.052 | 6/48 (NCI-H1573, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6147.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW480 0.601×, RKO 0.460×, LoVo 0.639×); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.309×; ⚠ toxic; transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.323×); [[Canagliflozin (drug)]] 5 µM in 1 line (SW 1271 0.0689×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.782×** | -9.4 | 2e-18 | 27/48 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.767×** | -6.9 | 1e-09 | 26/48 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.900× | -4.0 | 0.008 | 19/48 (A498, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.862× | -4.0 | 0.008 | 11/48 (AsPC-1, LS 180, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.891× | -3.1 | 0.19 | 17/48 (HT-29, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.890× | -3.0 | 0.20 | 15/50 (SW480, LoVo, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.891× | -3.0 | 0.20 | 10/47 (SW48, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6147. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 78.3 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +21.3) | — |
| [[HOP62 (line)]] | alt | 53.7 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.88× (z +12.4) | — |
| [[NCI-H1573 (line)]] | alt | 79.3 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.70× (z +12.1) | — |
| [[NCI-H460 (line)]] | wt | 57.0 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.4) | — |
| [[A498 (line)]] | wt | 92.6 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +13.4) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.664× (z -8.5) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A549 (line)]] | wt | 74.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +15.7) | — |
| [[LoVo (line)]] | wt | 54.9 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.639× (z -8.8) |
| [[SW480 (line)]] | alt | 70.6 | 3 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.14× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.601× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 66.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.1) | — |
| [[LOX-IMVI (line)]] | wt | 38.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.57× (z +12.3) | — |
| [[A-172 (line)]] | wt | 77.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +16.3) | — |
| [[COLO 205 (line)]] | alt | 41.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.22× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 63.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.11× (z +9.0) | — |
| [[KATO III (line)]] | alt | 48.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.67× (z +10.1) | — |
| [[LS 180 (line)]] | wt | 65.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.81× (z +11.4) | — |
| [[NCI-H1792 (line)]] | alt | 46.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.9) | — |
| [[RKO (line)]] | wt | 58.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +11.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -10.6) |
| [[SNU-423 (line)]] | alt | 69.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +14.7) | — |
| [[A-427 (line)]] | wt | 62.0 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.13× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 70.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +14.3) | — |
| [[C32 (line)]] | wt | 40.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.68× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 54.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 63.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +9.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 39.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.21× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 54.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 54.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +10.7) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 36.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.325× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~9% of this change |
| [[SNU-1 (line)]] | wt | 52.9 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.323× (z -11.5) |
| [[SW 1271 (line)]] | alt | 58.9 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0689× (z -9.8) |
| [[SW48 (line)]] | wt | 92.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.1) | — |
| [[AN3 CA (line)]] | alt | 91.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 53.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 93.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 67.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6147), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS10]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[PSMD6]] | +0.67 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[PSMD4]] | +0.65 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[PSMD11]] | +0.64 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[USP14]] | +0.63 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[PSMC5]] | +0.63 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[DCTN2]] | +0.63 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[FECH]] | +0.61 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[EXOC5]] | +0.60 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[DLD]] | +0.59 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[IDE]] | +0.59 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[SMARCE1]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS6L]] | -0.55 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[NOG]] | -0.54 | -0.35 / -0.65 | both halves | 1e-04 |  |
| [[TMEM41A]] | -0.54 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[FASTKD1]] | -0.53 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[SMIM4]] | -0.53 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[POM121]] | -0.53 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[TOB2]] | -0.53 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[MIA]] | -0.52 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[SEPTIN1]] | -0.52 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[NARF]] | -0.52 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[POLG2]] | -0.52 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[IKBIP]] | -0.50 | -0.49 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ANXA7's level | compounds that target TOP2A: 2 of 5 lower it (Doxorubicin, Idarubicin) | 40% of the class's compounds vs 0.6% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-22.8, -9.7); signed map (-6.3, -35.7). **Vector** length 113, 29.9% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.7 | +16.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.7 | +14.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.1 | +17.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.2 | +18.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.2 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +5.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.9 | +2.4 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.1 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -3.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -9.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | +0.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -0.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.1 | -0.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | annexin A7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:73,375,101-73,414,076 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ANX7 |
| Gene groups (HGNC) | Annexins |
| Matched by | ensembl_id |

**Function**, from UniProt [P20073](https://www.uniprot.org/uniprotkb/P20073) (Annexin A7):

> Calcium/phospholipid-binding protein which promotes membrane fusion and is involved in exocytosis.

**Summary**, from NCBI Gene [310](https://www.ncbi.nlm.nih.gov/gene/310):

> Annexin VII is a member of the annexin family of calcium-dependent phospholipid binding proteins.The Annexin VII gene contains 14 exons and spans approximately 34 kb of DNA. An alternatively spliced cassette exon results in two mRNA transcripts of 2.0 and 2.4 kb which are predicted to generate two protein isoforms differing in their N-terminal domain. The alternative splicing event is tissue specific and the mRNA containing the cassette exon is prevalent in brain, heart and skeletal muscle. The …

**Accessions** — [HGNC:545](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:545) · Entrez [310](https://www.ncbi.nlm.nih.gov/gene/310) · UniProt [P20073](https://www.uniprot.org/uniprotkb/P20073) · Ensembl [ENSG00000138279](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138279)

## Data

Gene col 6147: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6147); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6147, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6147]; `tensor/DDL_lfc|DDL_z.npy` [6147]; `embed/gene_vectors.npy` [6147]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6147 or target_col == 6147). Every well: [[ANXA7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANXA7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
