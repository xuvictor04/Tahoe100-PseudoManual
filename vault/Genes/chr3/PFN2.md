---
symbol: "PFN2"
type: "gene"
col: 939
ensembl_id: "ENSG00000070087"
name: "profilin 2"
location: "3q25.1"
module: 25
arm: "+"
pooled_cpm: 41.94
n_lines_expressing: 46
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 6
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# PFN2

*profilin 2* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.48× (z +15.9, q 0e+00, up in 39 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.80× (z +7.5, q 1e-11, up in 35 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.442× (z -14.7, q 0e+00, down in 40 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOT2]] (+0.67, fdr 1e-05), [[AZIN1]] (+0.64, fdr 7e-06), [[UBQLN1]] (+0.62, fdr 9e-06); moves opposite to [[TERF2IP]] (-0.62, fdr 1e-05), [[TMEM258]] (-0.61, fdr 1e-05), [[SELENOH]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NXPE3]] → it (grade C ⚠); 2 go from it, the strongest it → [[TMEM109]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 939.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.48×** | +15.9 | 0e+00 | 39/40 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.94×** | +13.2 | 2e-37 | 35/35 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.37×** | +8.2 | 7e-14 | 34/40 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +7.5 | 1e-11 | 35/44 (HT-29, HOP62, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.18× | +6.9 | 5e-10 | 17/44 (J82, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +5.8 | 5e-07 | 30/44 (HT-29, Panc 03.27, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.51×** | +3.7 | 0.015 | 19/43 (SHP-77, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.015 | 20/43 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.030 | 19/44 (HS-578T, NCI-H1573, …) | inconsistent across doses |  |
| [[DT-061 (drug)]] 5 µM |  | **1.61×** | +3.2 | 0.092 | 16/42 (SK-MEL-2, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.28×** | +3.1 | 0.100 | 15/44 (NCI-H460, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 939.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.442×** | -14.7 | 0e+00 | 40/43 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.540×** | -7.8 | 1e-12 | 38/44 (J82, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.566×** | -7.2 | 8e-11 | 39/44 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.564×** | -6.8 | 1e-09 | 35/43 (SW48, Panc 03.27, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.613×** | -6.2 | 5e-08 | 32/44 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.627×** | -5.9 | 3e-07 | 32/44 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.643×** | -5.6 | 1e-06 | 33/43 (J82, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.656×** | -5.4 | 5e-06 | 30/44 (SNU-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.754×** | -5.1 | 2e-05 | 27/44 (SHP-77, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.487×** | -4.8 | 9e-05 | 31/44 (Panc 03.27, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.612×** | -4.6 | 2e-04 | 24/43 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.707×** | -4.4 | 5e-04 | 24/44 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.713×** | -4.3 | 7e-04 | 25/43 (A-172, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.550×** | -4.0 | 0.003 | 24/44 (Hs 766T, A-427, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **0.608×** | -3.3 | 0.035 | 17/44 (SW48, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.774×** | -3.3 | 0.039 | 22/43 (HOP62, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 939. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 31.4 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.21× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.19× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 46.3 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.286× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 42.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.29× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -18.7) |
| [[SW480 (line)]] | alt | 23.2 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 6.31× (z +15.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -8.9) |
| [[HOP62 (line)]] | alt | 38.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -11.6) |
| [[HS-578T (line)]] | alt | 68.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -14.0) |
| [[J82 (line)]] | alt | 130 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -21.4) |
| [[MIA PaCa-2 (line)]] | alt | 27.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.90× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -13.3) |
| [[PANC-1 (line)]] | alt | 61.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -10.5) |
| [[A498 (line)]] | wt | 37.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.39× (z +13.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 45.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +12.4) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 64.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 59.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +10.5) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 50.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 36.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.96× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -14.4) |
| [[NCI-H1792 (line)]] | alt | 28.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.16× (z +14.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 33.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 57.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -17.5) |
| [[SK-MEL-2 (line)]] | alt | 38.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -9.5) |
| [[SNU-1 (line)]] | wt | 54.1 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -8.8) |
| [[SNU-423 (line)]] | alt | 27.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.34× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -9.6) |
| [[A-172 (line)]] | wt | 56.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +11.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 117 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -11.4) |
| [[AN3 CA (line)]] | alt | 38.1 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0961× (z -9.3) |
| [[BT-474 (line)]] | alt | 24.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -8.6) |
| [[C32 (line)]] | wt | 31.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +9.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 66.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 24.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 56.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -16.6) |
| [[NCI-H2030 (line)]] | alt | 64.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -21.1) |
| [[NCI-H661 (line)]] | alt | 47.1 | 0 | 1 | — | [[4EGI-1 (drug)]] 0.05 µM 0.0627× (z -9.3) |
| [[SHP-77 (line)]] | alt | 57.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -10.1) |
| [[SW 900 (line)]] | alt | 35.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 54.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.61 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 939), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOT2]] | +0.67 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[AZIN1]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[UBQLN1]] | +0.62 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[PTGES3]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[COPS6]] | +0.61 | +0.67 / +0.40 | both halves | 4e-05 |  |
| [[FAM199X]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[DYNC1H1]] | +0.58 | +0.53 / +0.62 | both halves | 1e-05 | pathway: RHO GTPase Effectors |
| [[TALDO1]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[RAD23B]] | +0.58 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[CCT7]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[G6PD]] | +0.57 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[PFKM]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TERF2IP]] | -0.62 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[TMEM258]] | -0.61 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[SELENOH]] | -0.60 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[NR1H3]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | -0.58 | -0.65 / -0.58 | both halves | 7e-06 | pathway: Signaling by ROBO receptors; ⚠ in the vector space only through flagged drug-doses |
| [[COX17]] | -0.56 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[HIC2]] | -0.55 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[ZBTB7A]] | -0.55 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[UPF2]] | -0.54 | -0.52 / -0.39 | both halves | 6e-05 | pathway: Signaling by ROBO receptors |
| [[TPRN]] | -0.54 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[MRPL51]] ⚠ | -0.54 | -0.56 / -0.50 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PDCD7]] | -0.54 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[TNRC6C]] | -0.53 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[RBX1]] | -0.53 | -0.44 / -0.49 | both halves | 3e-05 | pathway: Signaling by ROBO receptors |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NXPE3]] | C | NXPE3 activity raises PFN2's level | lines that do not express NXPE3 (5) vs lines expressing it (45) | 3.65× lower at baseline in the lines without NXPE3 | 0.089 | ⚠ within organs, on part of the lines; also absent: FAM171B, TTC23L, LCA5; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM109]] | C | PFN2 activity raises TMEM109's level | lines that do not express PFN2 (4) vs lines expressing it (46) | 1.74× lower at baseline in the lines without PFN2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: ASAP3, CCDC102A, TPST1; its own permutation p |
| [[TMX3]] | C | PFN2 activity raises TMX3's level | lines that do not express PFN2 (4) vs lines expressing it (46) | 1.74× lower at baseline in the lines without PFN2 | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: ASAP3, CCDC102A, TPST1 |

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.597). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-25.0, -14.0); signed map (-25.6, -31.6). **Vector** length 96.8, 27.0% of its response variance represented; |z| ≥ 3 in 820 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.8 | +7.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +5.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.9 | +3.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.1 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.8 |
|  | [[Lopinavir (drug)]] 5 µM |  | +2.8 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | -0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +2.2 | +0.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.3 | -2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -5.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.1 | -5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | -14.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.1 | -7.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.7 | -2.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.2 | -1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.9 | +0.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.6 | -1.4 |
|  | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | -2.4 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | profilin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.1 — chr3:149,964,904-150,050,788 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Profilins |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 7 pathways, smallest: RHO GTPases Activate Formins; Signaling by ROBO receptors; RHO GTPase Effectors |
| Matched by | ensembl_id |

**Function**, from UniProt [P35080](https://www.uniprot.org/uniprotkb/P35080) (Profilin-2):

> Binds to actin and affects the structure of the cytoskeleton. At high concentrations, profilin prevents the polymerization of actin, whereas it enhances it at low concentrations. By binding to PIP2, it inhibits the formation of IP3 and DG.

**Summary**, from NCBI Gene [5217](https://www.ncbi.nlm.nih.gov/gene/5217):

> The protein encoded by this gene is a ubiquitous actin monomer-binding protein belonging to the profilin family. It is thought to regulate actin polymerization in response to extracellular signals. There are two alternatively spliced transcript variants encoding different isoforms described for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8882](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8882) · Entrez [5217](https://www.ncbi.nlm.nih.gov/gene/5217) · UniProt [P35080](https://www.uniprot.org/uniprotkb/P35080) · Ensembl [ENSG00000070087](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070087)

## Data

Gene col 939: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 939); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 939, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 939]; `tensor/DDL_lfc|DDL_z.npy` [939]; `embed/gene_vectors.npy` [939]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 939 or target_col == 939). Every well: [[PFN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PFN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
