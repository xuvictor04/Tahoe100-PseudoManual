---
symbol: "UBE4A"
type: "gene"
col: 3131
ensembl_id: "ENSG00000110344"
name: "ubiquitination factor E4A"
location: "11q23.3"
module: 210
arm: "+"
pooled_cpm: 113.91
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/210"]
generated_by: "tahoemap"
---

# UBE4A

*ubiquitination factor E4A* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.87× (z +17.6, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.854× (z -6.3, q 1e-07, down in 21 of 49 measured lines) ⚠ cell-cycle shift, explains ~0% of this change. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.815× (z -5.6, q 5e-06, down in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (AsPC-1 0.515×, HOP62 0.576×, Hs 766T 0.583×, A498 0.604×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (Panc 03.27 0.478×, RKO 0.434×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.319×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RTF2]] (+0.72, fdr 7e-06), [[ASCC2]] (+0.67, fdr 7e-06), [[SEC22B]] (+0.67, fdr 7e-06); moves opposite to [[MEMO1]] (-0.62, fdr 1e-05), [[JADE3]] (-0.54, fdr 4e-05), [[RNF138]] (-0.54, fdr 2e-05).
> It is in [[Module 210]], a single-armed module (tRNA processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3131.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.87×** | +17.6 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +17.3 | 0e+00 | 46/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.59×** | +14.0 | 2e-42 | 45/49 (NCI-H1573, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +13.0 | 2e-36 | 44/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +10.5 | 7e-24 | 37/48 (SHP-77, NCI-H2030, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +6.1 | 9e-08 | 26/48 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +6.0 | 2e-07 | 31/48 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +5.9 | 2e-07 | 26/48 (A-427, NCI-H2347, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.21×** | +5.4 | 5e-06 | 21/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.13× | +4.8 | 8e-05 | 9/48 (CFPAC-1, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.17× | +4.5 | 3e-04 | 17/48 (SW48, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.15× | +4.0 | 0.003 | 20/48 (NCI-H2347, RKO, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.008 | 16/47 (NCI-H1792, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | 1.15× | +3.7 | 0.008 | 19/47 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.09× | +3.3 | 0.033 | 17/48 (MIA PaCa-2, NCI-H23, …) | top dose only | composition shift |
| [[EX229 (drug)]] 0.05 µM |  | 1.13× | +3.3 | 0.033 | 10/48 (LoVo, J82, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.13× | +3.2 | 0.050 | 3/48 (NCI-H460, RPMI-7951, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.064 | 15/49 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.23×** | +3.0 | 0.064 | 15/49 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.16× | +2.9 | 0.086 | 8/48 (Hs 766T, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3131.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (AsPC-1 0.515×, HOP62 0.576×, Hs 766T 0.583×, A498 0.604×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (Panc 03.27 0.478×, RKO 0.434×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.319×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.854× | -6.3 | 1e-07 | 21/49 (AsPC-1, HOP62, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.809×** | -5.8 | 2e-06 | 27/47 (H4, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.815×** | -5.6 | 5e-06 | 24/48 (RKO, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.950× | -4.8 | 2e-04 | 0/50 | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | 0.854× | -4.5 | 9e-04 | 19/48 (CFPAC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.847× | -4.3 | 0.001 | 19/47 (HepG2/C3A, H4, …) | inconsistent across doses | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.870× | -3.9 | 0.007 | 12/48 (SW 1088, AsPC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.853× | -3.2 | 0.096 | 11/48 (NCI-H661, Panc 03.27, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | 0.891× | -3.2 | 0.097 | 12/47 (SW 900, Panc 03.27, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.856× | -3.1 | 0.097 | 16/47 (SHP-77, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 0.893× | -3.1 | 0.10 | 10/49 (J82, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3131. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 87.5 | 7 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.18× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 92.0 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.16× (z +15.2) | — |
| [[NCI-H460 (line)]] | wt | 87.3 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.35× (z +13.8) | — |
| [[SW480 (line)]] | alt | 175 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.40× (z +14.9) | — |
| [[AsPC-1 (line)]] | alt | 140 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.12× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 90.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.04× (z +11.2) | — |
| [[Hs 766T (line)]] | wt | 126 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.30× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 118 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.12× (z +10.3) | — |
| [[PANC-1 (line)]] | alt | 144 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.01× (z +12.4) | — |
| [[SHP-77 (line)]] | alt | 101 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.35× (z +10.8) | — |
| [[A549 (line)]] | wt | 74.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.43× (z +11.5) | — |
| [[BT-474 (line)]] | alt | 72.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.53× (z +10.3) | — |
| [[C-33 A (line)]] | alt | 77.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.84× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 71.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.38× (z +10.1) | — |
| [[NCI-H2030 (line)]] | alt | 91.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.08× (z +10.0) | — |
| [[RKO (line)]] | wt | 128 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.65× (z +8.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -14.1) |
| [[SW48 (line)]] | wt | 120 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.71× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 135 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.79× (z +9.4) | [[Docetaxel (drug)]] 0.05 µM 0.586× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~15% of this change |
| [[COLO 205 (line)]] | alt | 155 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.08× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[HOP62 (line)]] | alt | 67.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.87× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 217 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.13× (z +11.4) | — |
| [[SNU-1 (line)]] | wt | 110 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.04× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 98.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.590× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 64.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.18× (z +8.8) | — |
| [[A498 (line)]] | wt | 90.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 136 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.07× (z +9.5) | — |
| [[H4 (line)]] | wt | 139 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.351× (z -9.6) ⚠ toxic |
| [[HS-578T (line)]] | alt | 93.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.84× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 106 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 134 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 1.89× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 109 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.74× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 127 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.478× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 105 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 81.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 268 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 146 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3131), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTF2]] | +0.72 | +0.74 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[ASCC2]] | +0.67 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[SEC22B]] | +0.67 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[LTN1]] | +0.65 | +0.62 / +0.57 | both halves | 9e-06 | same gene group; pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[SEC13]] | +0.65 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[NUP214]] | +0.65 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[COPE]] | +0.64 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[COPB1]] | +0.62 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[POFUT2]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[TTC1]] | +0.60 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[POLR2C]] | +0.59 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[SCFD1]] | +0.59 | +0.58 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEMO1]] | -0.62 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[JADE3]] | -0.54 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[RNF138]] | -0.54 | -0.48 / -0.50 | both halves | 2e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[HIVEP1]] | -0.51 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[QKI]] | -0.51 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[PSPC1]] | -0.50 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[PHLPP2]] | -0.50 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[NACC2]] | -0.50 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[POU2F1]] | -0.49 | -0.23 / -0.61 | both halves | 5e-04 |  |
| [[CPNE8]] | -0.49 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[ARID1B]] | -0.49 | -0.36 / -0.46 | both halves | 9e-05 | same gene group |
| [[SINHCAF]] | -0.49 | -0.40 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 210]] — tRNA processing; 13 genes; every member is in the + arm (projection on the module's main direction 0.760). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.0, -35.1); signed map (-53.1, 16.8). **Vector** length 123, 35.6% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.0 | +14.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +10.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.4 | +17.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +17.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +6.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | +2.8 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.4 | +2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -9.2 | -6.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -5.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.7 | -5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | +1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -1.9 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -2.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitination factor E4A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:118,359,600-118,399,211 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UBOX2, UFD2, KIAA0126, E4 |
| Gene groups (HGNC) | U-box domain containing; Armadillo like helical domain containing |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14139](https://www.uniprot.org/uniprotkb/Q14139) (Ubiquitin conjugation factor E4 A):

> Ubiquitin-protein ligase that probably functions as an E3 ligase in conjunction with specific E1 and E2 ligases. May also function as an E4 ligase mediating the assembly of polyubiquitin chains on substrates ubiquitinated by another E3 ubiquitin ligase. Mediates 'Lys-48'-linked polyubiquitination of substrates.

**Summary**, from NCBI Gene [9354](https://www.ncbi.nlm.nih.gov/gene/9354):

> This gene encodes a member of the U-box ubiquitin ligase family. The encoded protein is involved in multiubiquitin chain assembly and plays a critical role in chromosome condensation and separation through the polyubiquitination of securin. Autoantibodies against the encoded protein may be markers for scleroderma and Crohn's disease. A pseudogene of this gene is located on the long arm of chromosome 3. Alternatively spliced transcript variants encoding multiple isoforms have been observed for …

**Accessions** — [HGNC:12499](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12499) · Entrez [9354](https://www.ncbi.nlm.nih.gov/gene/9354) · UniProt [Q14139](https://www.uniprot.org/uniprotkb/Q14139) · Ensembl [ENSG00000110344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110344)

## Data

Gene col 3131: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3131); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3131, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3131]; `tensor/DDL_lfc|DDL_z.npy` [3131]; `embed/gene_vectors.npy` [3131]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3131 or target_col == 3131). Every well: [[UBE4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
