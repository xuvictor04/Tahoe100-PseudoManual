---
symbol: "SLC36A4"
type: "gene"
col: 11128
ensembl_id: "ENSG00000180773"
name: "solute carrier family 36 member 4"
location: "11q21"
module: 88
arm: "+"
pooled_cpm: 65.84
n_lines_expressing: 45
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 6
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# SLC36A4

*solute carrier family 36 member 4* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.55× (z +10.1, q 4e-21, up in 29 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.25× (z +5.3, q 1e-05, up in 21 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.375× (z -23.2, q 0e+00, down in 41 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS35L]] (+0.64, fdr 1e-05), [[ZNF655]] (+0.63, fdr 3e-05), [[FKRP]] (+0.59, fdr 4e-05); moves opposite to [[LRP5L]] (-0.62, fdr 2e-05), [[UBTD1]] (-0.61, fdr 6e-05), [[PHAF1]] (-0.58, fdr 1e-04).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → cells under [[Lonafarnib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11128.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +10.1 | 4e-21 | 29/39 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +9.2 | 8e-18 | 26/44 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.29×** | +5.7 | 3e-06 | 20/41 (C32, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.26×** | +5.5 | 4e-06 | 21/42 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +5.3 | 1e-05 | 21/43 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.47×** | +4.8 | 2e-04 | 16/44 (PANC-1, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +4.6 | 4e-04 | 17/43 (SW480, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.20×** | +4.4 | 7e-04 | 19/43 (BT-474, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.9 | 0.007 | 16/43 (NCI-H460, BT-474, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +3.7 | 0.010 | 15/43 (LoVo, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.18× | +3.6 | 0.013 | 13/43 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.16× | +3.6 | 0.013 | 8/43 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.023 | 17/42 (NCI-H2030, NCI-H23, …) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11128.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.375×** | -23.2 | 0e+00 | 41/43 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.512×** | -22.4 | 0e+00 | 40/44 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.390×** | -22.3 | 0e+00 | 41/43 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.406×** | -21.4 | 0e+00 | 41/43 (NCI-H1792, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.581×** | -12.9 | 8e-36 | 38/43 (H4, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.591×** | -12.4 | 1e-33 | 38/43 (J82, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.609×** | -11.3 | 9e-28 | 34/43 (hTERT-HPNE, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.580×** | -6.8 | 1e-09 | 25/44 (NCI-H1792, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.774×** | -5.8 | 3e-07 | 27/45 (C-33 A, PANC-1, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -5.6 | 2e-06 | 0/44 | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.881× | -4.2 | 0.001 | 15/43 (SNU-423, J82, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.842× | -4.1 | 0.002 | 19/43 (SHP-77, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~8% of this change | 0.850× | -3.9 | 0.005 | 19/43 (J82, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.857× | -3.6 | 0.011 | 14/43 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.868× | -3.3 | 0.032 | 12/43 (A-427, HepG2/C3A, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.908× | -3.2 | 0.047 | 5/43 (AsPC-1, NCI-H23, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.914× | -3.0 | 0.089 | 8/43 (NCI-H1573, H4, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.877× | -3.0 | 0.094 | 11/44 (A-427, C-33 A, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.883× | -2.9 | 0.097 | 10/43 (Hs 766T, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11128. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 74.7 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -15.3) |
| [[J82 (line)]] | alt | 113 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -17.1) |
| [[NCI-H1792 (line)]] | alt | 94.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -21.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.233× (z -18.6) |
| [[A-427 (line)]] | wt | 148 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.408× (z -12.2) |
| [[A549 (line)]] | wt | 61.4 | 1 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Belinostat (drug)]] 5 µM 0.262× (z -12.1) |
| [[HOP62 (line)]] | alt | 58.3 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -15.8) |
| [[NCI-H1573 (line)]] | alt | 59.7 | 3 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -9.7) |
| [[PANC-1 (line)]] | alt | 103 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -18.7) |
| [[C-33 A (line)]] | alt | 132 | 0 | 5 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -12.4) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.339× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 40.1 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.369× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 90.2 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -17.4) |
| [[RKO (line)]] | wt | 59.5 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.221× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.304× (z -10.6) |
| [[SHP-77 (line)]] | alt | 282 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -19.4) |
| [[SW480 (line)]] | alt | 63.0 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.28× (z +11.0) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.399× (z -12.6) |
| [[A-172 (line)]] | wt | 44.0 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.281× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 82.6 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.249× (z -14.5) |
| [[hTERT-HPNE (line)]] | wt | 67.6 | 0 | 4 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -13.7) |
| [[MIA PaCa-2 (line)]] | alt | 74.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.324× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 121 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -15.1) |
| [[NCI-H460 (line)]] | wt | 71.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.289× (z -16.8) |
| [[RPMI-7951 (line)]] | alt | 58.6 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -11.6) |
| [[SNU-423 (line)]] | alt | 60.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.301× (z -12.2) |
| [[SW 900 (line)]] | alt | 87.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.342× (z -11.1) |
| [[HS-578T (line)]] | alt | 61.3 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -14.7) |
| [[Hs 766T (line)]] | wt | 74.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -13.3) |
| [[LoVo (line)]] | wt | 36.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 58.4 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.353× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 59.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 68.1 | 0 | 2 | — | [[Filgotinib (drug)]] 0.05 µM 0.0612× (z -9.9) |
| [[SW1417 (line)]] | alt | 31.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.345× (z -9.6) |
| [[A498 (line)]] | wt | 46.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.440× (z -8.5) |
| [[AN3 CA (line)]] | alt | 31.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.126× (z -8.5) |
| [[BT-474 (line)]] | alt | 45.2 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.326× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 33.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 78.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -12.0) |
| [[HepG2_C3A (line)]] | wt | 23.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -8.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 33.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.344× (z -8.9) |
| [[C32 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 78.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.16 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 15.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.48 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.41 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11128), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*52 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS35L]] | +0.64 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ZNF655]] | +0.63 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[FKRP]] | +0.59 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[SMARCA1]] | +0.58 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[RCBTB2]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[RABL3]] | +0.58 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[SDCBP2-AS1]] | +0.57 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[DIO2]] | +0.57 | +0.50 / +0.42 | both halves | 4e-05 | pathway: Metabolism of amino acids and derivatives |
| [[CPLANE1]] | +0.57 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[CACNA2D1]] | +0.56 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[PSMC3]] | +0.55 | +0.44 / +0.56 | both halves | 3e-05 | pathway: Metabolism of amino acids and derivatives |
| [[C11orf58]] | +0.55 | +0.39 / +0.48 | both halves | 5e-05 |  |

## Genes that move opposite

*48 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRP5L]] | -0.62 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[UBTD1]] | -0.61 | -0.39 / -0.63 | both halves | 6e-05 |  |
| [[PHAF1]] | -0.58 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[FBXO31]] | -0.58 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[RNASET2]] | -0.58 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[EPB41L4B]] | -0.57 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[CNOT8]] | -0.57 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[MPG]] | -0.57 | -0.29 / -0.55 | both halves | 2e-04 |  |
| [[BAG4]] | -0.56 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[MED26]] | -0.56 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[TSEN54]] | -0.55 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[WDR45B]] | -0.55 | -0.41 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SLC36A4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises SLC36A4's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DNAJC18]] | C | DNAJC18 activity raises SLC36A4's level | lines that do not express DNAJC18 (4) vs lines expressing it (46) | 3.73× lower at baseline in the lines without DNAJC18 | 0.018 | ⚠ few lines (4 vs 46); across organs; also absent: TBKBP1, TTC23L, TMEFF1; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Lonafarnib (drug)]] 5 µM | C | SLC36A4 activity raises the cells' numbers under Lonafarnib 5 µM (protects the cells) | lines that do not express SLC36A4 (5) vs lines expressing it (43) | the lines without SLC36A4: 0.16× the cells of the other lines | 0.027 | ⚠ tissue-confounded; across organs; co-occurs with CTNNB1; also absent: KLHL5, FBXL2, SIX4 |
| cells under [[Furosemide (drug)]] 0.5 µM | C | SLC36A4 activity lowers the cells' numbers under Furosemide 0.5 µM (makes them more sensitive) | lines that do not express SLC36A4 (5) vs lines expressing it (43) | the lines without SLC36A4: 1.24× the cells of the other lines | 0.054 | ⚠ tissue-confounded; across organs; co-occurs with CTNNB1; also absent: KLHL5, FBXL2, SIX4 |
| cells under [[Pimozide (drug)]] 0.05 µM | C | SLC36A4 activity lowers the cells' numbers under Pimozide 0.05 µM (makes them more sensitive) | lines that do not express SLC36A4 (5) vs lines expressing it (43) | the lines without SLC36A4: 1.23× the cells of the other lines | 0.056 | ⚠ tissue-confounded; across organs; co-occurs with CTNNB1; also absent: KLHL5, FBXL2, SIX4 |
| cells under [[Erlotinib (drug)]] 0.05 µM | C | SLC36A4 activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express SLC36A4 (5) vs lines expressing it (43) | the lines without SLC36A4: 1.31× the cells of the other lines | 0.070 | ⚠ tissue-confounded; across organs; co-occurs with CTNNB1; also absent: KLHL5, FBXL2, SIX4 |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | SLC36A4 activity lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | lines that do not express SLC36A4 (5) vs lines expressing it (43) | the lines without SLC36A4: 1.29× the cells of the other lines | 0.074 | ⚠ tissue-confounded; across organs; co-occurs with CTNNB1; also absent: KLHL5, FBXL2, SIX4 |
| cells under [[Procainamide (hydrochloride) (drug)]] 0.5 µM | C | SLC36A4 activity lowers the cells' numbers under Procainamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express SLC36A4 (5) vs lines expressing it (43) | the lines without SLC36A4: 1.27× the cells of the other lines | 0.095 | ⚠ tissue-confounded; across organs; co-occurs with CTNNB1; also absent: KLHL5, FBXL2, SIX4 |

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.502). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (-7.8, -4.8); signed map (18.3, -27.1). **Vector** length 109, 28.7% of its response variance represented; |z| ≥ 3 in 1,060 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.4 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.1 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.1 | +5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.9 | -2.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.8 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | +3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +1.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.4 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | -4.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.2 | +2.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.7 | -12.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.6 | -23.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -22.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.4 | -1.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.0 | -2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 36 member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:93,144,174-93,197,991 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAT4, FLJ38932 |
| Gene groups (HGNC) | Solute carrier family 36 |
| Reactome | 6 pathways, smallest: Tryptophan catabolism; Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6YBV0](https://www.uniprot.org/uniprotkb/Q6YBV0) (Neutral amino acid uniporter 4):

> Uniporter that mediates the transport of neutral amino acids like L-tryptophan, proline and alanine. The transport activity is sodium ions-independent, electroneutral and therefore functions via facilitated diffusion.

**Summary**, from NCBI Gene [120103](https://www.ncbi.nlm.nih.gov/gene/120103):

> SLC36A4 belongs to the SLC36 family of amino acid transporters based on sequence similarity with other family members (e.g., SLC36A1; MIM 606561). SLC36 proteins contain about 500 amino acids and have 9 to 11 transmembrane domains. Unlike other SLC36 family members, which are proton-coupled amino acid transporters, SLC36A4 is a high-affinity/low-capacity non-proton-coupled amino acid transporter (Pillai and Meredith, 2011 [PubMed 21097500]).[supplied by OMIM, Feb 2011]

**Accessions** — [HGNC:19660](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19660) · Entrez [120103](https://www.ncbi.nlm.nih.gov/gene/120103) · UniProt [Q6YBV0](https://www.uniprot.org/uniprotkb/Q6YBV0) · Ensembl [ENSG00000180773](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180773)

## Data

Gene col 11128: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11128); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11128, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11128]; `tensor/DDL_lfc|DDL_z.npy` [11128]; `embed/gene_vectors.npy` [11128]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11128 or target_col == 11128). Every well: [[SLC36A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC36A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
