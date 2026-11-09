---
symbol: "LRRC8B"
type: "gene"
col: 12354
ensembl_id: "ENSG00000197147"
name: "leucine rich repeat containing 8 VRAC subunit B"
location: "1p22.2"
module: 118
arm: "-"
pooled_cpm: 38.71
n_lines_expressing: 44
n_dd_up: 28
n_dd_down: 6
n_dd_up_clean: 21
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# LRRC8B

*leucine rich repeat containing 8 VRAC subunit B* — 1p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.73× (z +27.9, q 0e+00, up in 37 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.556× (z -8.8, q 4e-16, down in 27 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.811× (z -4.5, q 0.001, down in 22 of 42 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIOS]] (+0.54, fdr 5e-05), [[C12orf29]] (+0.52, fdr 4e-05), [[IKZF3]] (+0.50, fdr 4e-05); moves opposite to [[WBP1L]] (-0.56, fdr 1e-05), [[PRPF18]] (-0.56, fdr 4e-05), [[BMT2]] (-0.54, fdr 1e-05).
> It sits in the **-** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[MARK4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12354.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.73×** | +27.9 | 0e+00 | 37/42 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.37×** | +17.5 | 0e+00 | 37/41 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.36×** | +12.9 | 1e-35 | 32/41 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.85×** | +9.2 | 4e-18 | 30/41 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.80×** | +8.8 | 2e-16 | 31/41 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +8.8 | 2e-16 | 28/40 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +8.8 | 2e-16 | 30/42 (C32, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.75×** | +8.4 | 3e-15 | 34/41 (HT-29, MIA PaCa-2, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +8.4 | 4e-15 | 32/41 (NCI-H23, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +7.9 | 2e-13 | 30/41 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.68×** | +7.8 | 4e-13 | 26/41 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +7.8 | 4e-13 | 30/41 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +7.2 | 2e-11 | 28/41 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.61×** | +7.2 | 3e-11 | 26/41 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +6.5 | 2e-09 | 28/41 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.99×** | +5.4 | 2e-06 | 25/42 (PANC-1, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 3e-04 | 22/41 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.007 | 15/41 (LS 180, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +3.2 | 0.036 | 19/41 (BT-474, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.038 | 13/40 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12354.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.556×** | -8.8 | 4e-16 | 27/39 (NCI-H23, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.545×** | -8.8 | 4e-16 | 23/34 (NCI-H1573, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.811×** | -4.5 | 0.001 | 22/42 (HepG2/C3A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.760×** | -4.1 | 0.005 | 20/41 (SW480, RKO, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.788×** | -3.6 | 0.037 | 18/41 (LoVo, SW 1271, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.688×** | -3.5 | 0.047 | 18/41 (HCT15, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.862× | -3.2 | 0.12 | 17/42 (SW1417, SNU-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.682× | -3.0 | 0.16 | 17/39 (SNU-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.814× | -3.0 | 0.16 | 6/41 (SW48, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12354. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.1 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +14.7) | — |
| [[C32 (line)]] | wt | 17.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +18.3) | — |
| [[NCI-H1573 (line)]] | alt | 61.1 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +17.9) | [[Dinaciclib (drug)]] 5 µM 0.0998× (z -20.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 37.9 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -9.5) |
| [[BT-474 (line)]] | alt | 74.4 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.64× (z +12.7) | — |
| [[KATO III (line)]] | alt | 37.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +13.7) | — |
| [[LS 180 (line)]] | wt | 63.8 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.36× (z +12.5) | — |
| [[SW1417 (line)]] | alt | 74.9 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -9.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 41.2 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.278× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.327× (z -10.7) |
| [[A549 (line)]] | wt | 28.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -11.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 32.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +22.1) | — |
| [[HS-578T (line)]] | alt | 19.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +14.2) | — |
| [[NCI-H2347 (line)]] | alt | 39.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +17.5) | — |
| [[PANC-1 (line)]] | alt | 61.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +24.8) | — |
| [[SNU-1 (line)]] | wt | 47.7 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.95× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -10.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 29.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +17.0) | — |
| [[HEC-1-A (line)]] | alt | 85.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +14.1) | — |
| [[LoVo (line)]] | wt | 42.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 28.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +15.6) | — |
| [[NCI-H1792 (line)]] | alt | 36.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +12.1) | — |
| [[Panc 03.27 (line)]] | alt | 28.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.157× (z -11.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 55.7 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.290× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 23.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +14.8) | — |
| [[SW 900 (line)]] | alt | 21.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +14.8) | — |
| [[SW48 (line)]] | wt | 77.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 70.7 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0863× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 12.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +15.6) | — |
| [[COLO 205 (line)]] | alt | 21.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +12.6) | — |
| [[HCT15 (line)]] | alt | 30.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.191× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 88.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -15.5) |
| [[Hs 766T (line)]] | wt | 46.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 54.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +16.3) | — |
| [[J82 (line)]] | alt | 24.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +14.4) | — |
| [[LOX-IMVI (line)]] | wt | 24.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +13.1) | — |
| [[NCI-H2030 (line)]] | alt | 31.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +15.4) | — |
| [[A-172 (line)]] | wt | 5.43 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.94 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.98 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.11 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12354), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIOS]] | +0.54 | +0.40 / +0.65 | both halves | 5e-05 |  |
| [[C12orf29]] | +0.52 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[IKZF3]] | +0.50 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[ISOC1]] | +0.50 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[NEK3]] | +0.50 | +0.29 / +0.53 | both halves | 2e-04 |  |
| [[EFR3A]] | +0.49 | +0.35 / +0.63 | both halves | 1e-04 |  |
| [[CAMK1]] | +0.49 | +0.33 / +0.47 | both halves | 1e-04 |  |
| [[SSX2IP]] | +0.49 | +0.38 / +0.60 | both halves | 7e-05 |  |
| [[N6AMT1]] | +0.49 | +0.36 / +0.54 | both halves | 9e-05 |  |
| [[CLN6]] | +0.49 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[MFSD13A]] | +0.48 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[GRB14]] | +0.48 | +0.41 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WBP1L]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[PRPF18]] | -0.56 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[BMT2]] | -0.54 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[FANK1]] | -0.53 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[EMC3]] | -0.52 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[KIAA0753]] | -0.50 | -0.37 / -0.57 | both halves | 7e-05 |  |
| [[ASB3]] | -0.50 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[ISY1-RAB43]] | -0.50 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[PRRG2]] | -0.50 | -0.30 / -0.58 | both halves | 2e-04 |  |
| [[VPS4B]] | -0.49 | -0.25 / -0.64 | both halves | 4e-04 |  |
| [[LRRC41]] | -0.49 | -0.33 / -0.63 | both halves | 1e-04 |  |
| [[ZNF75D]] | -0.49 | -0.37 / -0.56 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MARK4]] | B | LRRC8B activity lowers MARK4's level | lines that do not express LRRC8B (6) vs lines expressing it (44) | 1.07× higher at baseline in the lines without LRRC8B | 0.059 | ⚠ within organs, on part of the lines; also absent: GCLC, RHOF, RHPN1 |
| [[PPA1]] | B | LRRC8B activity raises PPA1's level | lines that do not express LRRC8B (6) vs lines expressing it (44) | 1.68× lower at baseline in the lines without LRRC8B | 0.059 | ⚠ within organs, on part of the lines; also absent: GCLC, RHOF, RHPN1 |
| [[MXD4]] | B | LRRC8B activity lowers MXD4's level | lines that do not express LRRC8B (6) vs lines expressing it (44) | 1.43× higher at baseline in the lines without LRRC8B | 0.069 | ⚠ within organs, on part of the lines; also absent: GCLC, RHOF, RHPN1 |
| [[MFSD13A]] | B | LRRC8B activity raises MFSD13A's level | lines that do not express LRRC8B (6) vs lines expressing it (44) | 1.68× lower at baseline in the lines without LRRC8B | 0.096 | ⚠ within organs, on part of the lines; also absent: GCLC, RHOF, RHPN1 |

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **-** arm (projection on the module's main direction -0.520). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-20.4, 30.9); signed map (1.6, -38.5). **Vector** length 89.5, 23.0% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +4.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +17.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.5 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +0.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.6 | -4.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.8 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -4.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -0.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.9 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 8 VRAC subunit B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.2 — chr1:89,524,829-89,597,861 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TA-LRRP, KIAA0231 |
| Gene groups (HGNC) | Volume regulated anion channel subunits |
| Reactome | 2 pathways, smallest: Miscellaneous transport and binding events; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P9F7](https://www.uniprot.org/uniprotkb/Q6P9F7) (Volume-regulated anion channel subunit LRRC8B):

> Non-essential component of the volume-regulated anion channel (VRAC, also named VSOAC channel), an anion channel required to maintain a constant cell volume in response to extracellular or intracellular osmotic changes. The VRAC channel conducts iodide better than chloride and can also conduct organic osmolytes like taurine. Channel activity requires LRRC8A plus at least one other family member (LRRC8B, LRRC8C, LRRC8D or LRRC8E); channel characteristics depend on the precise subunit composition.

**Summary**, from NCBI Gene [23507](https://www.ncbi.nlm.nih.gov/gene/23507):

> Contributes to volume-sensitive anion channel activity. Involved in monoatomic anion transmembrane transport. Located in cytoplasm and plasma membrane. Part of monoatomic ion channel complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30692](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30692) · Entrez [23507](https://www.ncbi.nlm.nih.gov/gene/23507) · UniProt [Q6P9F7](https://www.uniprot.org/uniprotkb/Q6P9F7) · Ensembl [ENSG00000197147](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197147)

## Data

Gene col 12354: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12354); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12354, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12354]; `tensor/DDL_lfc|DDL_z.npy` [12354]; `embed/gene_vectors.npy` [12354]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12354 or target_col == 12354). Every well: [[LRRC8B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC8B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
