---
symbol: "TRIM36"
type: "gene"
col: 7637
ensembl_id: "ENSG00000152503"
name: "tripartite motif containing 36"
location: "5q22.3"
module: 233
arm: "+"
pooled_cpm: 27.87
n_lines_expressing: 48
n_dd_up: 39
n_dd_down: 11
n_dd_up_clean: 31
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/233"]
generated_by: "tahoemap"
---

# TRIM36

*tripartite motif containing 36* — 5q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.23× (z +28.3, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.561× (z -6.8, q 7e-09, down in 21 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.534× (z -4.0, q 0.009, down in 16 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELOVL7]] (+0.66, fdr 7e-06), [[TGFBR1]] (+0.57, fdr 4e-05), [[ZC2HC1A]] (+0.56, fdr 2e-05); moves opposite to [[ERGIC2]] (-0.60, fdr 2e-05), [[CDKAL1]] (-0.56, fdr 2e-05), [[DCAF1]] (-0.55, fdr 2e-05).
> It is in [[Module 233]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ULBP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7637.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.23×** | +28.3 | 0e+00 | 43/46 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +16.6 | 0e+00 | 45/45 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.76×** | +16.1 | 0e+00 | 43/46 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.68×** | +15.8 | 0e+00 | 44/46 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.35×** | +14.1 | 2e-43 | 42/46 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.16×** | +14.0 | 2e-42 | 44/46 (SW1417, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.07×** | +13.6 | 2e-40 | 42/46 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.85×** | +12.7 | 2e-35 | 44/46 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.72×** | +12.2 | 2e-32 | 41/45 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.23×** | +9.7 | 1e-20 | 37/46 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +9.3 | 8e-19 | 35/46 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +9.1 | 5e-18 | 33/44 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.10×** | +9.0 | 1e-17 | 36/45 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.82×** | +7.0 | 1e-10 | 35/45 (RKO, C32, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +6.9 | 2e-10 | 33/46 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.75×** | +6.8 | 4e-10 | 29/46 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +6.3 | 1e-08 | 29/46 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.57×** | +6.0 | 6e-08 | 30/46 (C32, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7637.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.561×** | -6.8 | 7e-09 | 21/37 (SHP-77, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.589×** | -6.4 | 3e-08 | 28/42 (RKO, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.625×** | -5.3 | 2e-05 | 22/39 (A549, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.534×** | -4.0 | 0.009 | 16/44 (MIA PaCa-2, Hs 766T, …) | top dose only | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.736×** | -3.7 | 0.021 | 16/46 (CHP-212, SW1417, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM |  | **0.813×** | -3.5 | 0.032 | 18/46 (A549, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.748×** | -3.5 | 0.032 | 20/46 (A-172, AsPC-1, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.754×** | -3.4 | 0.042 | 16/46 (AsPC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Demeclocycline (drug)]] 5 µM |  | **0.828×** | -3.2 | 0.068 | 17/46 (SW1417, NCI-H460, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.767×** | -3.2 | 0.068 | 16/46 (SK-MEL-2, CHP-212, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.770×** | -3.2 | 0.073 | 13/46 (HEC-1-A, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7637. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.3 | 13 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.05× (z +18.6) | — |
| [[SW480 (line)]] | alt | 32.2 | 12 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +17.9) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 43.6 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +18.8) | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -9.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 25.4 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.40× (z +17.8) | — |
| [[LoVo (line)]] | wt | 38.7 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.34× (z +14.4) | — |
| [[HOP62 (line)]] | alt | 23.0 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +22.4) | — |
| [[NCI-H1573 (line)]] | alt | 28.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.03× (z +19.1) | — |
| [[SNU-423 (line)]] | alt | 25.3 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.58× (z +17.5) | [[Dinaciclib (drug)]] 0.05 µM 0.127× (z -11.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 34.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +15.4) | — |
| [[A549 (line)]] | wt | 19.0 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.59× (z +16.4) | [[Dinaciclib (drug)]] 0.05 µM 0.0938× (z -12.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 57.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.30× (z +19.7) | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -9.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 28.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +15.1) | — |
| [[NCI-H2030 (line)]] | alt | 12.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.86× (z +14.5) | — |
| [[A-172 (line)]] | wt | 56.5 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -12.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 41.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.63× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.126× (z -11.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 47.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -12.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 57.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +12.5) | — |
| [[SW 900 (line)]] | alt | 18.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +14.6) | — |
| [[A-427 (line)]] | wt | 25.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.78× (z +10.9) | — |
| [[A498 (line)]] | wt | 39.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.13× (z +16.6) | — |
| [[CFPAC-1 (line)]] | alt | 21.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +24.7) | — |
| [[HepG2_C3A (line)]] | wt | 24.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.33× (z +12.8) | — |
| [[HT-29 (line)]] | alt | 13.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +13.0) | — |
| [[LOX-IMVI (line)]] | wt | 28.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +12.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +15.4) | — |
| [[RPMI-7951 (line)]] | alt | 16.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.93× (z +13.2) | — |
| [[SHP-77 (line)]] | alt | 59.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.126× (z -16.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 26.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +12.1) | — |
| [[hTERT-HPNE (line)]] | wt | 12.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +14.9) | — |
| [[LS 180 (line)]] | wt | 24.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.93× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 13.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.39× (z +13.6) | — |
| [[Panc 03.27 (line)]] | alt | 28.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.09× (z +16.9) | — |
| [[AN3 CA (line)]] | alt | 78.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0974× (z -11.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 30.4 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.133× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 25.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 10.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 38.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.84× (z +11.2) | — |
| [[KATO III (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.214× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 10.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.00× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 22.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +10.2) | — |
| [[SW48 (line)]] | wt | 95.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -9.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.57 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.86 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 56.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7637), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*37 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELOVL7]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[TGFBR1]] | +0.57 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[ZC2HC1A]] | +0.56 | +0.48 / +0.62 | both halves | 2e-05 | STRING 426 |
| [[ATP11B]] | +0.56 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[PLPP1]] | +0.55 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[DLK2]] | +0.54 | +0.36 / +0.45 | both halves | 9e-05 |  |
| [[LNX2]] | +0.54 | +0.45 / +0.61 | both halves | 3e-05 | same gene group |
| [[KATNA1]] | +0.54 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[LONRF1]] | +0.53 | +0.38 / +0.43 | both halves | 6e-05 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[RAB8B]] | +0.53 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[CNNM4]] | +0.53 | +0.37 / +0.66 | both halves | 8e-05 |  |
| [[FAM241A]] | +0.52 | +0.53 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*63 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERGIC2]] | -0.60 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[CDKAL1]] | -0.56 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[DCAF1]] | -0.55 | -0.47 / -0.53 | both halves | 2e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[SMIM7]] | -0.55 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[LSG1]] | -0.55 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[PRPF31]] | -0.55 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[NUP214]] | -0.54 | -0.43 / -0.67 | both halves | 3e-05 |  |
| [[NUDC]] | -0.54 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[CDK11B]] | -0.54 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[RPTOR]] | -0.53 | -0.46 / -0.66 | both halves | 3e-05 |  |
| [[NAA20]] | -0.53 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[NOL10]] | -0.53 | -0.43 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ULBP1]] | B | ULBP1 activity lowers TRIM36's level | lines that do not express ULBP1 (15) vs lines expressing it (35) | 1.30× higher at baseline in the lines without ULBP1 | 0.037 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 233]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.862). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.2, -24.7); signed map (-22.9, 16.6). **Vector** length 76.2, 20.1% of its response variance represented; |z| ≥ 3 in 1,323 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +16.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.2 | +7.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +6.9 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.9 | +2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.6 | +2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | +2.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.6 | +6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.8 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -0.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.0 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | +2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | +0.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.4 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 36 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.3 — chr5:115,124,762-115,180,546 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RBCC728, RNF98, HAPRIN |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; Fibronectin type III domain containing; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ86](https://www.uniprot.org/uniprotkb/Q9NQ86) (E3 ubiquitin-protein ligase TRIM36):

> E3 ubiquitin-protein ligase which mediates ubiquitination and subsequent proteasomal degradation of target proteins including CTNNB1, FOXA2 and AKT1. Involved in chromosome segregation and cell cycle regulation. May play a role in the acrosome reaction and fertilization. Inhibits lung fibroblast proliferation, migration, and differentiation. Mechanistically, mediates 'Lys-48'-linked polyubiquitination of phospho-AKT1, leading to its proteasomal degradation and consequent inhibition of AKT …

**Summary**, from NCBI Gene [55521](https://www.ncbi.nlm.nih.gov/gene/55521):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. Multiple alternatively spliced transcript variants that encode different protein isoforms have been described for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16280](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16280) · Entrez [55521](https://www.ncbi.nlm.nih.gov/gene/55521) · UniProt [Q9NQ86](https://www.uniprot.org/uniprotkb/Q9NQ86) · Ensembl [ENSG00000152503](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152503)

## Data

Gene col 7637: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7637); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7637, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7637]; `tensor/DDL_lfc|DDL_z.npy` [7637]; `embed/gene_vectors.npy` [7637]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7637 or target_col == 7637). Every well: [[TRIM36 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM36.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
