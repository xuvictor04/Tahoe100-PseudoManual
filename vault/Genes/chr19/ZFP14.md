---
symbol: "ZFP14"
type: "gene"
col: 6593
ensembl_id: "ENSG00000142065"
name: "ZFP14 zinc finger protein"
location: "19q13.12"
module: 30
arm: "+"
pooled_cpm: 16.7
n_lines_expressing: 46
n_dd_up: 17
n_dd_down: 32
n_dd_up_clean: 17
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 8
direction_downstream: 2
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# ZFP14

*ZFP14 zinc finger protein* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.42× (z +5.9, q 3e-06, up in 18 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.341× (z -25.3, q 0e+00, down in 36 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRYZL1]] (+0.81, fdr 7e-06), [[RHOT1]] (+0.73, fdr 7e-06), [[PRUNE1]] (+0.72, fdr 7e-06); moves opposite to [[AP3B2]] (-0.63, fdr 3e-05), [[TTPAL]] (-0.63, fdr 1e-05), [[MSRA]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 2 go from it, the strongest it → [[ZNF567-DT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 1 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6593.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +5.9 | 3e-06 | 18/44 (HOP62, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +5.7 | 4e-06 | 20/43 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.25×** | +5.4 | 1e-05 | 17/44 (RKO, AsPC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +5.2 | 4e-05 | 20/43 (LS 180, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +5.1 | 4e-05 | 17/44 (PANC-1, RKO, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +4.4 | 1e-03 | 14/43 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.29×** | +4.3 | 0.001 | 16/44 (A-172, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.002 | 18/43 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +3.6 | 0.024 | 10/44 (MIA PaCa-2, RKO, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.025 | 13/43 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.026 | 9/43 (PANC-1, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.028 | 10/44 (SW480, RKO, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.031 | 9/44 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.031 | 8/44 (HOP62, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Regorafenib (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.052 | 6/43 (A549, RKO, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6593.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.341×** | -25.3 | 0e+00 | 36/43 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.325×** | -18.6 | 0e+00 | 35/43 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.343×** | -17.1 | 0e+00 | 41/44 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.487×** | -11.9 | 1e-30 | 30/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.527×** | -10.6 | 3e-24 | 32/43 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.544×** | -10.1 | 6e-22 | 30/42 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.555×** | -9.8 | 1e-20 | 32/44 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.570×** | -9.3 | 9e-19 | 31/43 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.596×** | -8.2 | 1e-14 | 25/42 (SHP-77, HS-578T, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.621×** | -7.9 | 2e-13 | 23/38 (C-33 A, C32, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.636×** | -7.5 | 3e-12 | 23/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.752×** | -6.6 | 1e-09 | 24/44 (SW480, BT-474, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.713×** | -5.6 | 1e-06 | 20/43 (MIA PaCa-2, SW480, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.748×** | -4.6 | 2e-04 | 18/44 (AN3 CA, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **0.751×** | -4.5 | 2e-04 | 16/26 (PANC-1, Panc 03.27, …) | all doses, flat | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.591×** | -4.4 | 4e-04 | 14/44 (MIA PaCa-2, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.598×** | -4.3 | 6e-04 | 17/44 (MIA PaCa-2, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.832×** | -4.3 | 6e-04 | 15/44 (MIA PaCa-2, CHP-212, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.779×** | -4.1 | 0.001 | 16/43 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.787×** | -4.0 | 0.002 | 13/43 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.626×** | -3.9 | 0.002 | 14/43 (NCI-H460, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.807×** | -3.5 | 0.009 | 11/43 (SNU-423, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6593. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.2 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -18.3) |
| [[PANC-1 (line)]] | alt | 30.6 | 0 | 10 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.143× (z -19.3) |
| [[A549 (line)]] | wt | 32.3 | 0 | 8 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.117× (z -17.3) |
| [[NCI-H1573 (line)]] | alt | 14.7 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0544× (z -19.4) |
| [[SW480 (line)]] | alt | 22.4 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.270× (z -11.7) |
| [[HOP62 (line)]] | alt | 11.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 23.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -13.5) |
| [[A-172 (line)]] | wt | 10.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -11.5) |
| [[A498 (line)]] | wt | 12.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0374× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -11.0) |
| [[C32 (line)]] | wt | 19.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -17.6) |
| [[NCI-H1792 (line)]] | alt | 16.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 9.13 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -13.5) |
| [[Panc 03.27 (line)]] | alt | 21.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -11.9) |
| [[C-33 A (line)]] | alt | 44.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[HEC-1-A (line)]] | alt | 29.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -18.4) |
| [[Hs 766T (line)]] | wt | 14.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -15.0) |
| [[NCI-H2030 (line)]] | alt | 22.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -17.3) |
| [[RPMI-7951 (line)]] | alt | 17.8 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0709× (z -13.1) |
| [[A-427 (line)]] | wt | 44.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.6) | — |
| [[AN3 CA (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0814× (z -9.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[BT-474 (line)]] | alt | 19.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -9.9) |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0586× (z -17.8) |
| [[HepG2_C3A (line)]] | wt | 8.62 | 0 | 1 | — | [[Almonertinib (mesylate) (drug)]] 0.05 µM 0.0792× (z -8.6) |
| [[HS-578T (line)]] | alt | 7.03 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.106× (z -9.0) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 20.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +12.3) | — |
| [[SHP-77 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.160× (z -11.1) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 32.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -8.7) ⚠ cell-cycle shift, explains ~20% of this change |
| [[SNU-423 (line)]] | alt | 8.20 | 0 | 1 | — | [[Peretinoin (drug)]] 0.5 µM 0.0442× (z -13.8) |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.167× (z -9.0) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.85 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6593), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYZL1]] | +0.81 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[RHOT1]] | +0.73 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[PRUNE1]] | +0.72 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[USP30]] | +0.71 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[KLHDC10]] | +0.70 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[TMEM185A]] | +0.69 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[SLC9A6]] | +0.67 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[TNRC6A]] | +0.67 | +0.71 / +0.57 | both halves | 9e-06 |  |
| [[MYPOP]] | +0.67 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ASB7]] | +0.66 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[MALSU1]] | +0.66 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[SUFU]] | +0.66 | +0.54 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP3B2]] | -0.63 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[TTPAL]] | -0.63 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[MSRA]] | -0.61 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[SERPINB8]] | -0.60 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[DGKH]] | -0.60 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.59 | -0.52 / -0.52 | both halves | 1e-05 | same gene group |
| [[WDR1]] | -0.59 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[DESI1]] | -0.59 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[PIEZO1]] | -0.58 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[TRIP12]] | -0.58 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[KRT8P12]] | -0.57 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[RAPH1]] | -0.57 | -0.53 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers ZFP14's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[MGLL]] | B | MGLL activity lowers ZFP14's level | lines that do not express MGLL (14) vs lines expressing it (36) | 2.07× higher at baseline in the lines without MGLL | 0.071 | ⚠ within organs, on part of the lines; also absent: CXCL3, MET, PSORS1C1; maybe low, not absent |
| [[ZNF567-DT]] | C | ZNF567-DT activity raises ZFP14's level | lines that do not express ZNF567-DT (6) vs lines expressing it (44) | 5.03× lower at baseline in the lines without ZNF567-DT | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF420, ZNF850, ZNF540; co-absent with the target |
| [[ZNF540]] | C | ZNF540 activity raises ZFP14's level | lines that do not express ZNF540 (5) vs lines expressing it (45) | 5.52× lower at baseline in the lines without ZNF540 | 0.015 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZFP14, ZNF573; maybe low, not absent; co-absent with the target |
| [[ZNF420]] | C | ZNF420 activity raises ZFP14's level | lines that do not express ZNF420 (7) vs lines expressing it (43) | 3.89× lower at baseline in the lines without ZNF420 | 0.021 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF850, ZNF540; co-absent with the target |
| [[ZNF461]] | C | ZNF461 activity raises ZFP14's level | lines that do not express ZNF461 (7) vs lines expressing it (43) | 3.55× lower at baseline in the lines without ZNF461 | 0.053 | ⚠ within organs, on part of the lines; also absent: ZNF567, ZNF529-AS1, ZNF571; co-absent with the target |
| [[FAM182B]] | C | FAM182B activity raises ZFP14's level | lines that do not express FAM182B (4) vs lines expressing it (46) | 2.05× lower at baseline in the lines without FAM182B | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CATSPER2P1, FGF12, SLFNL1-AS1; maybe low, not absent; its own permutation p |
| [[GDPD1]] | C | GDPD1 activity raises ZFP14's level | lines that do not express GDPD1 (4) vs lines expressing it (46) | 1.81× lower at baseline in the lines without GDPD1 | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CHD7, NRTN, ENSG00000256673; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF567-DT]] | C | ZFP14 activity raises ZNF567-DT's level | lines that do not express ZFP14 (4) vs lines expressing it (46) | 2.98× lower at baseline in the lines without ZFP14 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ZNF540, ZNF566, ZNF567; co-absent with the target; its own permutation p |
| [[ZNF540]] | C | ZFP14 activity raises ZNF540's level | lines that do not express ZFP14 (4) vs lines expressing it (46) | 2.64× lower at baseline in the lines without ZFP14 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ZNF540, ZNF566, ZNF567; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.730). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-1.2, -10.2); signed map (-30.5, -9.0). **Vector** length 85.1, 18.1% of its response variance represented; |z| ≥ 3 in 1,017 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +3.7 | +5.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.0 | +5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +5.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +4.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -18.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.5 | -17.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.7 | -25.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ZFP14 zinc finger protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:36,334,453-36,379,201 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1559, ZNF531 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCL3](https://www.uniprot.org/uniprotkb/Q9HCL3) (Zinc finger protein 14 homolog):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [57677](https://www.ncbi.nlm.nih.gov/gene/57677):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to act upstream of or within blastocyst hatching. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29312](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29312) · Entrez [57677](https://www.ncbi.nlm.nih.gov/gene/57677) · UniProt [Q9HCL3](https://www.uniprot.org/uniprotkb/Q9HCL3) · Ensembl [ENSG00000142065](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142065)

## Data

Gene col 6593: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6593); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6593, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6593]; `tensor/DDL_lfc|DDL_z.npy` [6593]; `embed/gene_vectors.npy` [6593]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6593 or target_col == 6593). Every well: [[ZFP14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFP14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
