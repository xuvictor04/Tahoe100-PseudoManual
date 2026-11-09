---
symbol: "RIT1"
type: "gene"
col: 6781
ensembl_id: "ENSG00000143622"
name: "Ras like without CAAX 1"
location: "1q22"
module: 135
arm: "+"
pooled_cpm: 40.44
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# RIT1

*Ras like without CAAX 1* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.03× (z +17.4, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.671× (z -6.7, q 9e-09, down in 21 of 39 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SHP-77 0.142×, NCI-H1573 0.189×, NCI-H2347 0.292×, CFPAC-1 0.250×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 6 lines (NCI-H23 0.168×, NCI-H2347 0.343×, A549 0.213×, NCI-H2030 0.278×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (COLO 205 0.157×, NCI-H2347 0.300×, C32 0.242×; ⚠ toxic; transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (SNU-1 0.121×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLIC2]] (+0.60, fdr 1e-04), [[RSRC2]] (+0.59, fdr 2e-05), [[GNGT1]] (+0.55, fdr 3e-05); moves opposite to [[VKORC1L1]] (-0.55, fdr 1e-05), [[NUP93]] (-0.54, fdr 1e-04), [[TREX2]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF711]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6781.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.03×** | +17.4 | 0e+00 | 42/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.26×** | +14.2 | 2e-43 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **4.27×** | +13.2 | 9e-38 | 45/49 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +11.7 | 1e-29 | 41/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +10.1 | 5e-22 | 32/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.80×** | +9.8 | 1e-20 | 34/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.71×** | +9.4 | 7e-19 | 35/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.67×** | +8.9 | 4e-17 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +8.9 | 5e-17 | 40/48 (NCI-H460, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.57×** | +8.6 | 5e-16 | 36/47 (NCI-H2030, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +8.1 | 2e-14 | 32/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.63×** | +8.0 | 7e-14 | 39/48 (A-172, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +7.9 | 9e-14 | 35/48 (A-172, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +7.7 | 6e-13 | 37/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.7 | 5e-07 | 2/49 (H4, SNU-1) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | **1.20×** | +4.5 | 2e-04 | 21/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.42×** | +4.3 | 4e-04 | 19/48 (A-172, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6781.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SHP-77 0.142×, NCI-H1573 0.189×, NCI-H2347 0.292×, CFPAC-1 0.250×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 6 lines (NCI-H23 0.168×, NCI-H2347 0.343×, A549 0.213×, NCI-H2030 0.278×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (COLO 205 0.157×, NCI-H2347 0.300×, C32 0.242×; ⚠ toxic; transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (SNU-1 0.121×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.671×** | -6.7 | 9e-09 | 21/39 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.716×** | -5.9 | 1e-06 | 27/46 (COLO 205, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.826× | -3.4 | 0.13 | 17/48 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.831× | -3.3 | 0.15 | 15/47 (NCI-H2347, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6781. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 46.9 | 15 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -8.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 29.2 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +15.1) | — |
| [[NCI-H23 (line)]] | alt | 40.8 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 75.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +17.9) | — |
| [[A549 (line)]] | wt | 28.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 73.6 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -14.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 26.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.5) | — |
| [[A498 (line)]] | wt | 65.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 26.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +12.4) | — |
| [[Hs 766T (line)]] | wt | 41.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 37.6 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.85× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.189× (z -13.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 36.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +12.7) | — |
| [[A-427 (line)]] | wt | 31.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 73.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -13.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 39.4 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.90× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -11.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 32.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +13.9) | — |
| [[NCI-H2030 (line)]] | alt | 96.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.278× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 25.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 58.3 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 34.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 34.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -9.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 47.0 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.113× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 54.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -14.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 33.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.5) | — |
| [[KATO III (line)]] | alt | 21.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.67× (z +10.7) | — |
| [[LoVo (line)]] | wt | 37.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 28.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 27.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 38.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 26.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 37.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -9.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 58.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -14.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 15.8 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.121× (z -8.6) |
| [[SNU-423 (line)]] | alt | 27.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6781), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLIC2]] | +0.60 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[RSRC2]] | +0.59 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[GNGT1]] | +0.55 | +0.46 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_PI3K_AKT_MTOR_SIGNALING |
| [[KCP]] | +0.55 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[DNAJB4]] | +0.54 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[POLR2M]] | +0.54 | +0.43 / +0.41 | both halves | 4e-05 |  |
| [[TCEAL1]] | +0.53 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[ZNF585A]] | +0.53 | +0.35 / +0.44 | both halves | 1e-04 |  |
| [[SLC3A2]] | +0.53 | +0.39 / +0.43 | both halves | 6e-05 |  |
| [[ARMCX5-GPRASP2]] | +0.52 | +0.40 / +0.41 | both halves | 5e-05 |  |
| [[PPP1R15A]] | +0.52 | +0.50 / +0.41 | both halves | 4e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[PLCD4]] | +0.51 | +0.45 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VKORC1L1]] | -0.55 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[NUP93]] | -0.54 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[TREX2]] | -0.54 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[ADARB1]] | -0.53 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[ODF2]] | -0.52 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[TCF3]] | -0.52 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[GRK6]] | -0.52 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[SRGAP2D]] | -0.52 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[CMC2]] | -0.51 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[PACS2]] | -0.50 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[TEX2]] | -0.50 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[MAPK8]] | -0.50 | -0.40 / -0.37 | both halves | 8e-05 | pathway: HALLMARK_PI3K_AKT_MTOR_SIGNALING |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF711]] | B | ZNF711 activity lowers RIT1's level | lines that do not express ZNF711 (15) vs lines expressing it (35) | 1.12× higher at baseline in the lines without ZNF711 | 0.051 | ⚠ within organs, on part of the lines; also absent: FRMPD3, RPS6KA6, MIR9-3HG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **+** arm (projection on the module's main direction 0.499). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (25.5, -30.1); signed map (6.9, -9.5). **Vector** length 65.4, 13.0% of its response variance represented; |z| ≥ 3 in 1,087 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.2 | +7.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.6 | +3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.6 | +9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | +2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | -2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | +8.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | -2.8 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | +8.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | +2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[vincristine (drug)]] 5 µM |  | -1.6 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.5 | +2.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | Ras like without CAAX 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,897,808-155,911,404 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RIBB, ROC1, MGC125864, MGC125865; previously RIT |
| Gene groups (HGNC) | RAS type GTPase family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, MYOGENESIS, MTORC1_SIGNALING |
| Reactome | 5 pathways, smallest: Signalling to p38 via RIT and RIN; Signalling to ERKs; Signaling by NTRK1 (TRKA) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92963](https://www.uniprot.org/uniprotkb/Q92963) (GTP-binding protein Rit1):

> Plays a crucial role in coupling nerve growth factor (NGF) stimulation to the activation of both EPHB2 and MAPK14 signaling pathways and in NGF-dependent neuronal differentiation. Involved in ELK1 transactivation through the Ras-MAPK signaling cascade that mediates a wide variety of cellular functions, including cell proliferation, survival, and differentiation. Recognized by LZTR1, which mediates its ubiquitination by a BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complex.

**Summary**, from NCBI Gene [6016](https://www.ncbi.nlm.nih.gov/gene/6016):

> This gene encodes a member of a subfamily of Ras-related GTPases. The encoded protein is involved in regulating p38 MAPK-dependent signaling cascades related to cellular stress. This protein also cooperates with nerve growth factor to promote neuronal development and regeneration. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Feb 2012]

**Accessions** — [HGNC:10023](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10023) · Entrez [6016](https://www.ncbi.nlm.nih.gov/gene/6016) · UniProt [Q92963](https://www.uniprot.org/uniprotkb/Q92963) · Ensembl [ENSG00000143622](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143622)

## Data

Gene col 6781: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6781); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6781, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6781]; `tensor/DDL_lfc|DDL_z.npy` [6781]; `embed/gene_vectors.npy` [6781]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6781 or target_col == 6781). Every well: [[RIT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
