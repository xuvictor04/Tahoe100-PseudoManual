---
symbol: "TMBIM1"
type: "gene"
col: 5780
ensembl_id: "ENSG00000135926"
name: "transmembrane BAX inhibitor motif containing 1"
location: "2q35"
module: 31
arm: "+"
pooled_cpm: 82.14
n_lines_expressing: 48
n_dd_up: 18
n_dd_down: 11
n_dd_up_clean: 13
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# TMBIM1

*transmembrane BAX inhibitor motif containing 1* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.71× (z +7.9, q 1e-12, up in 37 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 1.38× (z +4.5, q 8e-04, up in 23 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.321× (z -16.7, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SFN]] (+0.56, fdr 1e-05), [[LINC00520]] (+0.54, fdr 3e-05), [[ZBTB43]] (+0.54, fdr 3e-05); moves opposite to [[DNMT1]] (-0.54, fdr 3e-05), [[HNRNPR]] (-0.53, fdr 4e-05), [[COA1]] (-0.52, fdr 4e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HLTF]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5780.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +7.9 | 1e-12 | 37/47 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +6.6 | 9e-09 | 30/40 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +5.8 | 1e-06 | 34/46 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +4.5 | 8e-04 | 23/46 (H4, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +4.4 | 0.001 | 30/46 (Panc 03.27, NCI-H2030, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +4.3 | 0.001 | 29/46 (C32, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +4.1 | 0.004 | 24/46 (C32, H4, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.008 | 22/45 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.015 | 21/46 (A498, C32, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.020 | 24/46 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +3.5 | 0.020 | 24/46 (SK-MEL-2, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.5 | 0.024 | 23/46 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.031 | 22/46 (COLO 205, HT-29, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.065 | 15/47 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.069 | 20/45 (Panc 03.27, HT-29, …) | rises with dose | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.073 | 17/45 (PANC-1, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.075 | 21/47 (A-427, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.077 | 16/46 (Panc 03.27, HT-29, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.15× | +3.0 | 0.090 | 13/46 (SK-MEL-2, SNU-1, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5780.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.321×** | -16.7 | 0e+00 | 45/46 (AsPC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.378×** | -14.3 | 3e-44 | 45/46 (AsPC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.433×** | -12.3 | 1e-32 | 45/46 (AsPC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.623×** | -9.8 | 1e-20 | 35/45 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.697×** | -5.3 | 1e-05 | 32/46 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.502×** | -5.3 | 1e-05 | 32/47 (HOP62, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.790×** | -4.9 | 7e-05 | 29/46 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.725×** | -4.6 | 4e-04 | 30/47 (HepG2/C3A, SNU-423, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.557×** | -4.5 | 4e-04 | 31/47 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.763×** | -3.7 | 0.011 | 27/46 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.807×** | -3.2 | 0.083 | 17/46 (LS 180, A498, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5780. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 461 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.0908× (z -30.8) |
| [[LoVo (line)]] | wt | 134 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0994× (z -21.8) |
| [[KATO III (line)]] | alt | 226 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0918× (z -21.8) |
| [[NCI-H1573 (line)]] | alt | 106 | 1 (1 ⚠) | 4 | [[Digitoxin (drug)]] 5 µM 3.26× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.164× (z -15.1) |
| [[NCI-H2347 (line)]] | alt | 116 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -21.7) |
| [[CFPAC-1 (line)]] | alt | 168 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -17.6) |
| [[HOP62 (line)]] | alt | 75.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.241× (z -15.1) |
| [[Hs 766T (line)]] | wt | 207 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -21.7) |
| [[HT-29 (line)]] | alt | 124 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 65.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -13.8) |
| [[A-172 (line)]] | wt | 93.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.277× (z -13.0) |
| [[A549 (line)]] | wt | 69.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.265× (z -12.6) |
| [[BT-474 (line)]] | alt | 46.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.256× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 121 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -10.4) |
| [[HS-578T (line)]] | alt | 52.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 90.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.325× (z -10.8) |
| [[PANC-1 (line)]] | alt | 48.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +9.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.391× (z -9.9) |
| [[SNU-423 (line)]] | alt | 72.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.231× (z -12.9) |
| [[SW48 (line)]] | wt | 89.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -10.9) |
| [[A498 (line)]] | wt | 60.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +8.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.453× (z -8.5) |
| [[COLO 205 (line)]] | alt | 81.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -14.2) |
| [[LOX-IMVI (line)]] | wt | 51.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -10.8) |
| [[LS 180 (line)]] | wt | 77.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 52.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -10.4) |
| [[SNU-1 (line)]] | wt | 92.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -11.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.241× (z -10.8) |
| [[A-427 (line)]] | wt | 61.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -8.9) |
| [[C32 (line)]] | wt | 64.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +11.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 74.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.304× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 42.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.325× (z -9.1) |
| [[RKO (line)]] | wt | 48.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 52.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.318× (z -9.4) |
| [[SW 1088 (line)]] | alt | 59.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0578× (z -8.6) |
| [[SW 900 (line)]] | alt | 40.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.312× (z -8.6) |
| [[AN3 CA (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.77 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5780), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFN]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[LINC00520]] | +0.54 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[ZBTB43]] | +0.54 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[ALS2CL]] | +0.53 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[PPP2CB]] | +0.53 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[ARL8A]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[SWT1]] | +0.53 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[SDCBP2]] | +0.52 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[KLC1]] | +0.52 | +0.55 / +0.49 | both halves | 2e-05 |  |
| [[MFGE8]] | +0.52 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[DUSP22]] | +0.51 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[AKAP13-AS1]] | +0.51 | +0.36 / +0.50 | both halves | 9e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNMT1]] | -0.54 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[HNRNPR]] | -0.53 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[COA1]] | -0.52 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[FIGNL1]] | -0.52 | -0.37 / -0.56 | both halves | 9e-05 |  |
| [[C2CD5]] | -0.50 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[LMNB1]] | -0.50 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[E2F8]] | -0.49 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[UBE2T]] | -0.49 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[MAD2L1]] | -0.49 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[NCAPH]] | -0.49 | -0.40 / -0.49 | both halves | 4e-05 |  |
| [[SSRP1]] | -0.49 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[WDPCP]] | -0.49 | -0.51 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLTF]] | B | HLTF activity lowers TMBIM1's level | lines that do not express HLTF (8) vs lines expressing it (42) | 2.15× higher at baseline in the lines without HLTF | 0.010 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[PKP3]] | B | PKP3 activity raises TMBIM1's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 1.72× lower at baseline in the lines without PKP3 | 0.037 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent |
| [[GJB3]] | B | GJB3 activity raises TMBIM1's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 1.83× lower at baseline in the lines without GJB3 | 0.050 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[ALS2CL]] | B | ALS2CL activity raises TMBIM1's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 1.61× lower at baseline in the lines without ALS2CL | 0.059 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[PLEKHN1]] | C | PLEKHN1 activity raises TMBIM1's level | lines that do not express PLEKHN1 (3) vs lines expressing it (47) | 3.08× lower at baseline in the lines without PLEKHN1 | 0.087 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.401). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-29.4, -38.4); signed map (7.3, 18.2). **Vector** length 102, 31.8% of its response variance represented; |z| ≥ 3 in 1,121 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.1 | +4.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +6.0 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.9 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.7 | +4.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +5.5 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.2 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.3 | +2.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -4.8 | -5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -0.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.5 | -0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.5 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane BAX inhibitor motif containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:218,274,197-218,292,586 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PP1201, RECS1, LFG3 |
| Gene groups (HGNC) | Transmembrane BAX inhibitor motif containing |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969X1](https://www.uniprot.org/uniprotkb/Q969X1) (Protein lifeguard 3):

> Negatively regulates aortic matrix metalloproteinase-9 (MMP9) production and may play a protective role in vascular remodeling.

**Summary**, from NCBI Gene [64114](https://www.ncbi.nlm.nih.gov/gene/64114):

> Enables death receptor binding activity. Involved in negative regulation of Fas signaling pathway; negative regulation of extrinsic apoptotic signaling pathway via death domain receptors; and negative regulation of protein localization to plasma membrane. Located in Golgi membrane; endosome membrane; and lysosomal membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23410](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23410) · Entrez [64114](https://www.ncbi.nlm.nih.gov/gene/64114) · UniProt [Q969X1](https://www.uniprot.org/uniprotkb/Q969X1) · Ensembl [ENSG00000135926](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135926)

## Data

Gene col 5780: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5780); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5780, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5780]; `tensor/DDL_lfc|DDL_z.npy` [5780]; `embed/gene_vectors.npy` [5780]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5780 or target_col == 5780). Every well: [[TMBIM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMBIM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
