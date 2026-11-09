---
symbol: "SLC45A4"
type: "gene"
col: 335
ensembl_id: "ENSG00000022567"
name: "solute carrier family 45 member 4"
location: "8q24.3"
module: 159
arm: "+"
pooled_cpm: 59.65
n_lines_expressing: 45
n_dd_up: 14
n_dd_down: 21
n_dd_up_clean: 13
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# SLC45A4

*solute carrier family 45 member 4* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.91× (z +22.9, q 0e+00, up in 42 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.505× (z -11.0, q 2e-25, down in 21 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.657× (z -7.0, q 3e-10, down in 27 of 43 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPAN9]] (+0.67, fdr 1e-05), [[BCR]] (+0.61, fdr 2e-05), [[DNAJB1]] (+0.61, fdr 2e-05); moves opposite to [[DNAI4]] (-0.62, fdr 3e-05), [[AHI1-DT]] (-0.59, fdr 4e-05), [[BMI1]] (-0.59, fdr 3e-05).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[EEPD1]] → it (grade B ⚠); 3 go from it, the strongest it → [[CHKA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 335.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.91×** | +22.9 | 0e+00 | 42/43 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.09×** | +18.9 | 0e+00 | 41/43 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.42×** | +14.9 | 0e+00 | 38/42 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.15×** | +12.8 | 1e-35 | 36/42 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.09×** | +11.7 | 2e-29 | 34/43 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.80×** | +9.9 | 6e-21 | 34/42 (HOP62, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +7.3 | 3e-11 | 28/43 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +5.5 | 2e-06 | 19/43 (HOP62, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.9 | 6e-05 | 15/43 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.53×** | +4.6 | 2e-04 | 14/44 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +4.6 | 3e-04 | 20/42 (HOP62, SHP-77, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +4.3 | 7e-04 | 16/44 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.60×** | +4.1 | 0.002 | 16/41 (RKO, LOX-IMVI, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.48×** | +3.5 | 0.022 | 12/37 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 335.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.505×** | -11.0 | 2e-25 | 21/32 (Panc 03.27, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.596×** | -8.7 | 1e-15 | 29/42 (Panc 03.27, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.596×** | -8.0 | 3e-13 | 25/37 (Panc 03.27, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.657×** | -7.0 | 3e-10 | 27/43 (LoVo, A498, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.688×** | -6.2 | 5e-08 | 29/44 (NCI-H1573, PANC-1, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.781×** | -5.8 | 5e-07 | 22/43 (Hs 766T, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.738×** | -5.7 | 9e-07 | 26/43 (HOP62, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.530×** | -5.6 | 2e-06 | 26/40 (Hs 766T, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.535×** | -5.5 | 3e-06 | 16/28 (SW480, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.724×** | -5.2 | 1e-05 | 23/42 (PANC-1, HOP62, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.732×** | -5.0 | 3e-05 | 24/44 (Hs 766T, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.786×** | -4.9 | 5e-05 | 20/44 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.814×** | -4.8 | 6e-05 | 22/43 (Hs 766T, SW1417, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.733×** | -4.8 | 6e-05 | 21/42 (NCI-H1573, NCI-H23, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.748×** | -4.7 | 1e-04 | 21/42 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.763×** | -4.5 | 2e-04 | 21/43 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.817×** | -4.0 | 0.002 | 19/44 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.794×** | -3.7 | 0.007 | 19/42 (KATO III, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.797×** | -3.6 | 0.008 | 14/43 (NCI-H2347, HS-578T, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.862× | -3.5 | 0.012 | 11/43 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 335. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 41.7 | 18 | 1 (1 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 6.77× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -9.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 254 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -16.9) |
| [[HOP62 (line)]] | alt | 19.4 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +14.3) | — |
| [[NCI-H2347 (line)]] | alt | 43.2 | 3 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.53× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -10.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 29.6 | 4 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.56× (z +15.7) | [[Lonafarnib (drug)]] 5 µM 0.0946× (z -12.8) ⚠ toxic |
| [[HT-29 (line)]] | alt | 619 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 34.1 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.07× (z +14.8) | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -8.6) |
| [[PANC-1 (line)]] | alt | 29.3 | 5 | 1 | [[Panobinostat (drug)]] 5 µM 4.43× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -10.5) |
| [[SW1417 (line)]] | alt | 89.1 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.08× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -10.3) |
| [[KATO III (line)]] | alt | 121 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.69× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.141× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -13.3) |
| [[SHP-77 (line)]] | alt | 46.6 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.84× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -12.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 121 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -12.3) |
| [[J82 (line)]] | alt | 31.0 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 4.09× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -10.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 76.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.284× (z -12.0) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.376× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 25.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.57× (z +14.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 38.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.80× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 28.0 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.66× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 66.6 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.91× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.0801× (z -19.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 19.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.00× (z +10.9) | — |
| [[BT-474 (line)]] | alt | 27.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 94.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 15.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +13.2) | — |
| [[A-427 (line)]] | wt | 34.3 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.296× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 28.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.67× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 90.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -12.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 82.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.37× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -16.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 38.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.94× (z +10.9) | — |
| [[COLO 205 (line)]] | alt | 92.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -9.0) |
| [[HCT15 (line)]] | alt | 53.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.10× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 36.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 43.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 22.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.19× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 33.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -8.7) |
| [[SNU-1 (line)]] | wt | 34.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -11.8) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SW48 (line)]] | wt | 41.7 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.48× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.5 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.64 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 335), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPAN9]] | +0.67 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[BCR]] | +0.61 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[DNAJB1]] | +0.61 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[CORO2A]] | +0.60 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[ARHGAP8]] | +0.59 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[HDAC11]] | +0.58 | +0.48 / +0.38 | both halves | 7e-05 |  |
| [[SEMA4D]] | +0.58 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[MAST3]] | +0.57 | +0.38 / +0.44 | both halves | 6e-05 |  |
| [[HPCAL1]] | +0.57 | +0.43 / +0.46 | both halves | 4e-05 |  |
| [[ARHGEF16]] | +0.57 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[GRAMD4]] | +0.56 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[SLC8B1]] | +0.56 | +0.45 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAI4]] | -0.62 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[AHI1-DT]] | -0.59 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[BMI1]] | -0.59 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[RNF146]] | -0.58 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[MAD2L1-DT]] | -0.58 | -0.49 / -0.25 | both halves | 4e-04 |  |
| [[WAC-AS1]] | -0.58 | -0.46 / -0.33 | both halves | 1e-04 |  |
| [[MIR181A2HG]] | -0.57 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[PCMTD1-DT]] | -0.57 | -0.55 / -0.31 | both halves | 2e-04 |  |
| [[CFAP418-AS1]] | -0.57 | -0.46 / -0.31 | both halves | 2e-04 |  |
| [[RC3H2]] | -0.56 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[DPH6-DT]] | -0.56 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[MFF-DT]] | -0.56 | -0.41 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EEPD1]] | B | EEPD1 activity raises SLC45A4's level | lines that do not express EEPD1 (14) vs lines expressing it (36) | 2.07× lower at baseline in the lines without EEPD1 | 0.018 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises SLC45A4's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KCNK5]] | B | KCNK5 activity raises SLC45A4's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 2.82× lower at baseline in the lines without KCNK5 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2 |
| [[MAP2K1]] | B | MAP2K1 activity raises SLC45A4's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[DNM1]] | B | DNM1 activity raises SLC45A4's level | lines that do not express DNM1 (5) vs lines expressing it (45) | 1.98× lower at baseline in the lines without DNM1 | 0.093 | ⚠ within organs, on part of the lines; also absent: PKN3, STARD10; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHKA]] | B | SLC45A4 activity raises CHKA's level | lines that do not express SLC45A4 (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without SLC45A4 | 0.060 | ⚠ within organs, on part of the lines; also absent: ARHGEF3; maybe low, not absent; its own permutation p |
| [[HDAC11]] | B | SLC45A4 activity raises HDAC11's level | lines that do not express SLC45A4 (5) vs lines expressing it (45) | 1.15× lower at baseline in the lines without SLC45A4 | 0.084 | ⚠ within organs, on part of the lines; also absent: ARHGEF3; maybe low, not absent |
| [[EEPD1]] | B | SLC45A4 activity raises EEPD1's level | lines that do not express SLC45A4 (5) vs lines expressing it (45) | 1.67× lower at baseline in the lines without SLC45A4 | 0.089 | ⚠ within organs, on part of the lines; also absent: ARHGEF3; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.501). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.1, 14.5); signed map (-20.6, 35.4). **Vector** length 114, 30.8% of its response variance represented; |z| ≥ 3 in 1,298 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.9 | +12.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.8 | +11.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.8 | +22.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.5 | +18.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +9.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.9 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +1.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -3.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -4.9 | -3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.6 | -7.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.3 | -4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.8 | -6.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.6 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 45 member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:141,207,166-141,308,305 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1126 |
| Gene groups (HGNC) | Solute carrier family 45 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5BKX6](https://www.uniprot.org/uniprotkb/Q5BKX6) (Polyamine-transporter SLC45A4):

> Neuronal polyamine-transporter involved in pain perception. Transports polyamines such as putrescine, cadaverine, spermine and spermidine. Expressed in sensory neuron subtypes within the dorsal root ganglion, where it regulates the excitability of C-polymodal nociceptors by mediating polyamine transport (By similarity).

**Summary**, from NCBI Gene [57210](https://www.ncbi.nlm.nih.gov/gene/57210):

> Enables putrescine transmembrane transporter activity; spermidine transmembrane transporter activity; and spermine transmembrane transporter activity. Involved in sensory perception of pain. Is active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29196](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29196) · Entrez [57210](https://www.ncbi.nlm.nih.gov/gene/57210) · UniProt [Q5BKX6](https://www.uniprot.org/uniprotkb/Q5BKX6) · Ensembl [ENSG00000022567](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000022567)

## Data

Gene col 335: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 335); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 335, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 335]; `tensor/DDL_lfc|DDL_z.npy` [335]; `embed/gene_vectors.npy` [335]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 335 or target_col == 335). Every well: [[SLC45A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC45A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
