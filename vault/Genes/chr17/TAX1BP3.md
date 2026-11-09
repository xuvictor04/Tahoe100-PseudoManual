---
symbol: "TAX1BP3"
type: "gene"
col: 13155
ensembl_id: "ENSG00000213977"
name: "Tax1 binding protein 3"
location: "17p13.2"
module: 3
arm: "-"
pooled_cpm: 13.3
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 16
n_dd_up_clean: 15
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# TAX1BP3

*Tax1 binding protein 3* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.46× (z +17.0, q 0e+00, up in 27 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.08× (z +13.7, q 1e-40, up in 37 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.597× (z -7.2, q 4e-10, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYB561A3]] (+0.66, fdr 1e-05), [[NCOA4]] (+0.62, fdr 1e-05), [[EIF4G2]] (+0.62, fdr 3e-05); moves opposite to [[SLC27A1]] (-0.60, fdr 7e-05), [[MRPS34]] (-0.60, fdr 4e-05), [[CAMKK1]] (-0.59, fdr 2e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13155.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.46×** | +17.0 | 0e+00 | 27/32 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.50×** | +16.5 | 0e+00 | 22/25 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +13.7 | 1e-40 | 37/43 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +9.2 | 3e-18 | 20/30 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +9.1 | 7e-18 | 24/38 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +8.2 | 2e-14 | 29/44 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.80×** | +8.0 | 8e-14 | 33/47 (A549, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +7.9 | 3e-13 | 28/42 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +6.9 | 4e-10 | 6/48 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +6.3 | 2e-08 | 23/46 (KATO III, LS 180, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +6.3 | 2e-08 | 27/45 (LS 180, RKO, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +5.7 | 7e-07 | 20/43 (AsPC-1, RKO, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.3 | 4e-06 | 24/48 (A-172, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.44×** | +5.0 | 3e-05 | 19/43 (BT-474, HT-29, …) | rises with dose | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.00×** | +4.9 | 3e-05 | 14/43 (J82, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +4.8 | 5e-05 | 21/47 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.003 | 16/47 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.67×** | +3.7 | 0.007 | 11/37 (PANC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.021 | 10/46 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +2.9 | 0.073 | 12/44 (LS 180, MIA PaCa-2, …) | two highest doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.24×** | +2.9 | 0.084 | 4/48 (HS-578T, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13155.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.597×** | -7.2 | 4e-10 | 26/47 (KATO III, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.602×** | -7.1 | 5e-10 | 31/44 (SNU-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.610×** | -6.9 | 1e-09 | 28/47 (KATO III, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.644×** | -5.8 | 1e-06 | 27/44 (A-172, J82, …) | all doses, flat | cell-cycle shift (explains ~21% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.680×** | -5.4 | 8e-06 | 25/47 (HS-578T, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.498×** | -5.1 | 4e-05 | 19/43 (RKO, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.767×** | -3.5 | 0.033 | 17/47 (LS 180, LOX-IMVI, …) | inconsistent across doses |  |
| [[Penfluridol (drug)]] 5 µM |  | **0.772×** | -3.5 | 0.033 | 13/45 (SNU-423, HOP62, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.783×** | -3.4 | 0.033 | 14/44 (SK-MEL-2, A-427, …) | two highest doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.775×** | -3.4 | 0.033 | 11/45 (A498, J82, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.634×** | -3.3 | 0.047 | 9/43 (LOX-IMVI, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.649×** | -3.1 | 0.078 | 6/46 (NCI-H1792, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.654×** | -3.1 | 0.085 | 16/46 (J82, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **0.804×** | -3.1 | 0.086 | 7/47 (J82, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.806×** | -3.0 | 0.086 | 17/46 (NCI-H460, hTERT-HPNE, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.807×** | -3.0 | 0.086 | 15/46 (SW48, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13155. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 15.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 13.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.67× (z +9.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 20.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +12.4) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.64× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 8.48 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +8.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 9.80 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +10.9) | — |
| [[A-172 (line)]] | wt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 25.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +9.2) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 16.2 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.120× (z -10.6) |
| [[Hs 766T (line)]] | wt | 16.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +8.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 19.2 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.256× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 7.56 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.38× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 10.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.17× (z +10.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 12.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 13.6 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0763× (z -9.7) |
| [[SW1417 (line)]] | alt | 17.4 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.266× (z -9.0) |
| [[SW48 (line)]] | wt | 9.53 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0686× (z -9.3) |
| [[A-427 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13155), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB561A3]] | +0.66 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[NCOA4]] | +0.62 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[EIF4G2]] | +0.62 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[LRRC57]] | +0.61 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[LEPROT]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[CGGBP1]] | +0.60 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[TUG1]] | +0.60 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[TAF9]] | +0.59 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[UBE2A]] | +0.58 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[THAP9]] | +0.58 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[ERAP1]] | +0.57 | +0.51 / +0.36 | both halves | 9e-05 |  |
| [[TAPBP]] | +0.57 | +0.48 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A1]] | -0.60 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[MRPS34]] | -0.60 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[CAMKK1]] | -0.59 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[TOMM20]] | -0.58 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[PHKA2]] | -0.57 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[RBAK-RBAKDN]] | -0.55 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[CAMK2G]] | -0.55 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[DHX57]] | -0.55 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[ANKRD27]] | -0.55 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[CARMIL2]] | -0.54 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[MPHOSPH10]] | -0.54 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[SETD5]] | -0.54 | -0.55 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TAX1BP3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.400). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-9.4, 1.0); signed map (21.5, -20.8). **Vector** length 99.9, 22.5% of its response variance represented; |z| ≥ 3 in 1,068 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +6.4 | +8.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +7.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +17.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +13.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +6.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | +2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.0 | +2.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.8 | -7.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.1 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.0 | -5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.7 | -5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -5.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -3.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | Tax1 binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:3,662,895-3,668,679 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIP-1 |
| Gene groups (HGNC) | PDZ domain containing |
| Hallmark sets | P53_PATHWAY |
| Reactome | 4 pathways, smallest: RHO GTPases Activate Rhotekin and Rhophilins; RHO GTPase Effectors; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [O14907](https://www.uniprot.org/uniprotkb/O14907) (Tax1-binding protein 3):

> May regulate a number of protein-protein interactions by competing for PDZ domain binding sites. Binds CTNNB1 and may thereby act as an inhibitor of the Wnt signaling pathway. Competes with LIN7A for KCNJ4 binding, and thereby promotes KCNJ4 internalization. May play a role in the Rho signaling pathway. May play a role in activation of CDC42 by the viral protein HPV16 E6.

**Summary**, from NCBI Gene [30851](https://www.ncbi.nlm.nih.gov/gene/30851):

> This gene encodes a small, highly conserved protein with a single PDZ domain. PDZ (PSD-95/Discs large/ZO-1 homologous) domains promote protein-protein interactions that affect cell signaling, adhesion, protein scaffolding, and receptor and ion transporter functions. The encoded protein interacts with a large number of target proteins that play roles in signaling pathways; for example, it interacts with Rho A and glutaminase L and also acts as a negative regulator of the Wnt/beta-catenin …

**Accessions** — [HGNC:30684](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30684) · Entrez [30851](https://www.ncbi.nlm.nih.gov/gene/30851) · UniProt [O14907](https://www.uniprot.org/uniprotkb/O14907) · Ensembl [ENSG00000213977](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213977)

## Data

Gene col 13155: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13155); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13155, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13155]; `tensor/DDL_lfc|DDL_z.npy` [13155]; `embed/gene_vectors.npy` [13155]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13155 or target_col == 13155). Every well: [[TAX1BP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAX1BP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
