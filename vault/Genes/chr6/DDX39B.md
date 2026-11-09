---
symbol: "DDX39B"
type: "gene"
col: 12619
ensembl_id: "ENSG00000198563"
name: "DExD-box helicase 39B"
location: "6p21.33"
module: 58
arm: "+"
pooled_cpm: 137.07
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 8
n_dd_up_clean: 18
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# DDX39B

*DExD-box helicase 39B* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.13× (z +22.8, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.758× (z -5.9, q 2e-06, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[U2AF2]] (+0.70, fdr 2e-05), [[HNRNPL]] (+0.68, fdr 1e-05), [[VPS52]] (+0.68, fdr 3e-05); moves opposite to [[MRPL41]] (-0.69, fdr 1e-05, ⚠ MRPL41 in the vector space only through flagged drug-doses), [[POLR2J]] (-0.67, fdr 4e-05, ⚠ POLR2J in the vector space only through flagged drug-doses), [[ELOB]] (-0.67, fdr 1e-05), [[ATP5MJ]] (-0.66, fdr 3e-05), [[LIN7B]] (-0.65, fdr 7e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12619.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +22.8 | 0e+00 | 46/48 (A549, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.80×** | +12.4 | 5e-33 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.98×** | +12.1 | 2e-31 | 47/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.80×** | +12.1 | 3e-31 | 43/48 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +11.4 | 4e-28 | 45/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.66×** | +10.9 | 1e-25 | 45/48 (LoVo, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.52×** | +8.6 | 9e-16 | 38/44 (A549, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.47×** | +8.1 | 3e-14 | 35/49 (NCI-H460, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +8.0 | 8e-14 | 29/49 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +7.8 | 4e-13 | 40/48 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +7.6 | 1e-12 | 35/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +7.6 | 1e-12 | 38/47 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +7.6 | 2e-12 | 37/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.86×** | +6.9 | 3e-10 | 44/49 (Panc 03.27, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.39×** | +6.5 | 4e-09 | 32/45 (A-427, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +6.3 | 1e-08 | 40/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +5.4 | 2e-06 | 24/48 (A-172, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +5.3 | 3e-06 | 34/48 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +5.3 | 3e-06 | 28/47 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.001 | 27/48 (LOX-IMVI, RPMI-7951, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12619.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.758×** | -5.9 | 2e-06 | 32/48 (SK-MEL-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.765×** | -5.7 | 3e-06 | 34/48 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.786×** | -5.2 | 4e-05 | 26/48 (SK-MEL-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.786×** | -5.2 | 4e-05 | 31/48 (CFPAC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.798×** | -4.8 | 1e-04 | 30/48 (CFPAC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.827×** | -3.9 | 0.009 | 25/47 (A-427, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.862× | -3.8 | 0.010 | 15/48 (SW480, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.727×** | -3.6 | 0.025 | 22/49 (SK-MEL-2, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 5 µM |  | 0.844× | -3.5 | 0.029 | 17/48 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.853× | -3.4 | 0.036 | 21/48 (MIA PaCa-2, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.855× | -3.4 | 0.038 | 14/49 (LoVo, RKO, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.811×** | -3.2 | 0.065 | 22/48 (COLO 205, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.866× | -3.1 | 0.079 | 12/48 (J82, NCI-H23, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.861× | -3.1 | 0.079 | 16/48 (SW48, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.870× | -3.0 | 0.10 | 14/48 (SW 1271, HCT15, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12619. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 99.1 | 14 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +18.9) | — |
| [[HS-578T (line)]] | alt | 95.9 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +17.1) | — |
| [[SW480 (line)]] | alt | 173 | 9 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +14.8) | — |
| [[HOP62 (line)]] | alt | 145 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +16.8) | — |
| [[LoVo (line)]] | wt | 145 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +14.2) | — |
| [[NCI-H2347 (line)]] | alt | 108 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +18.4) | — |
| [[PANC-1 (line)]] | alt | 181 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +19.3) | — |
| [[A549 (line)]] | wt | 96.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +23.0) | — |
| [[BT-474 (line)]] | alt | 153 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +15.8) | — |
| [[LOX-IMVI (line)]] | wt | 170 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +17.1) | — |
| [[A-172 (line)]] | wt | 80.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +15.1) | — |
| [[A498 (line)]] | wt | 67.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +15.5) | — |
| [[J82 (line)]] | alt | 216 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +19.5) | — |
| [[AsPC-1 (line)]] | alt | 79.1 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +20.9) | — |
| [[KATO III (line)]] | alt | 146 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 187 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +15.7) | — |
| [[RKO (line)]] | wt | 188 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.4) | — |
| [[RPMI-7951 (line)]] | alt | 140 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.3) | — |
| [[COLO 205 (line)]] | alt | 111 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +15.7) | — |
| [[HEC-1-A (line)]] | alt | 147 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +17.0) | — |
| [[hTERT-HPNE (line)]] | wt | 123 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +14.5) | — |
| [[NCI-H1573 (line)]] | alt | 103 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +11.6) | — |
| [[NCI-H1792 (line)]] | alt | 104 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +15.3) | — |
| [[NCI-H23 (line)]] | alt | 231 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +11.6) | — |
| [[SW1417 (line)]] | alt | 114 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +9.8) | — |
| [[A-427 (line)]] | wt | 130 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.4) | — |
| [[C32 (line)]] | wt | 101 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +15.4) | — |
| [[H4 (line)]] | wt | 132 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.1) | — |
| [[HepG2_C3A (line)]] | wt | 130 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +10.1) | — |
| [[HT-29 (line)]] | alt | 104 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +13.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 164 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.5) | — |
| [[Panc 03.27 (line)]] | alt | 136 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +14.6) | — |
| [[SK-MEL-2 (line)]] | alt | 112 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +13.0) | — |
| [[CFPAC-1 (line)]] | alt | 136 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +13.6) | — |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.205× (z -8.9) |
| [[SHP-77 (line)]] | alt | 144 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 127 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 128 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +18.3) | — |
| [[SW 1271 (line)]] | alt | 139 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.197× (z -8.9) |
| [[SW 900 (line)]] | alt | 125 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.8) | — |
| [[SW48 (line)]] | wt | 178 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.39× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 207 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 202 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 179 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 71.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 166 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 162 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12619), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*29 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[U2AF2]] | +0.70 | +0.48 / +0.60 | both halves | 2e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 996 |
| [[HNRNPL]] | +0.68 | +0.57 / +0.60 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 807 |
| [[VPS52]] | +0.68 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[SRSF1]] | +0.65 | +0.46 / +0.63 | both halves | 2e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 914 |
| [[QTRT1]] | +0.65 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[PCBP1-AS1]] | +0.64 | +0.55 / +0.32 | both halves | 2e-04 |  |
| [[SNX5]] | +0.64 | +0.44 / +0.55 | both halves | 3e-05 | same gene group |
| [[ACADM]] | +0.63 | +0.43 / +0.52 | both halves | 3e-05 | STRING 435 |
| [[BCLAF1]] | +0.62 | +0.52 / +0.54 | both halves | 1e-05 | STRING 754 |
| [[EIF4G2]] | +0.62 | +0.55 / +0.39 | both halves | 5e-05 | same gene group |
| [[PRKAR1A]] | +0.62 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[SRRM2]] | +0.61 | +0.53 / +0.54 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 872 |

## Genes that move opposite

*71 of its nearest partners move opposite, 6 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL41]] ⚠ | -0.69 | -0.52 / -0.55 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[POLR2J]] ⚠ | -0.67 | -0.41 / -0.60 | both halves | 4e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; ⚠ in the vector space only through flagged drug-doses |
| [[ELOB]] | -0.67 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[ATP5MJ]] | -0.66 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[LIN7B]] | -0.65 | -0.38 / -0.63 | both halves | 7e-05 |  |
| [[MPST]] | -0.65 | -0.40 / -0.59 | both halves | 4e-05 |  |
| [[TMEM256]] | -0.64 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[C4orf48]] | -0.64 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[PUSL1]] | -0.64 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[YIF1B]] | -0.63 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[SSNA1]] | -0.63 | -0.24 / -0.57 | both halves | 5e-04 |  |
| [[BLVRA]] | -0.63 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[SERAC1]] | -0.63 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[LAMTOR5]] | -0.62 | -0.43 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises DDX39B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF577]] | B | ZNF577 activity weakens DDX39B's drug response | lines that do not express ZNF577 (10) vs lines expressing it (39) | the lines without ZNF577 respond 1.25× as strongly (z diff -1.07); strongest at Dinaciclib 0.5 µM: 1.70x vs 1.39x (z diff -2.6) | 0.081 | ⚠ within organs, on part of the lines; also absent: ZNF649, ZNF724, ENSG00000283201; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction -0.622). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-45.9, -18.6); signed map (16.2, -37.5). **Vector** length 113, 37.1% of its response variance represented; |z| ≥ 3 in 1,407 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +10.0 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +9.4 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +8.7 | +6.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +6.7 | +4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +6.3 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +10.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.1 | +6.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -7.7 | -5.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.2 | -4.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.1 | -5.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.7 | -5.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.9 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | -0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.2 | -3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -0.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | DExD-box helicase 39B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,530,219-31,542,448 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D6S81E, Uap56; previously BAT1 |
| Gene groups (HGNC) | DEAD-box helicases; Transcription and export complex 1 subunits; Spliceosomal E complex; Small nucleolar RNA protein coding host genes |
| Reactome | 12 pathways, smallest: RHOBTB2 GTPase cycle; RHOBTB GTPase Cycle; Transport of Mature mRNA derived from an Intron-Containing Transcript |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13838](https://www.uniprot.org/uniprotkb/Q13838) (Spliceosome RNA helicase DDX39B):

> Involved in nuclear export of spliced and unspliced mRNA. Component of the TREX complex which is thought to couple mRNA transcription, processing and nuclear export, and specifically associates with spliced mRNA and not with unspliced pre-mRNA. The TREX complex is recruited to spliced mRNAs by a transcription-independent mechanism, binds to mRNA upstream of the exon-junction complex (EJC) and is recruited in a splicing- and cap-dependent manner to a region near the 5' end of the mRNA where it …

**Summary**, from NCBI Gene [7919](https://www.ncbi.nlm.nih.gov/gene/7919):

> This gene encodes a member of the DEAD box family of RNA-dependent ATPases that mediate ATP hydrolysis during pre-mRNA splicing. The encoded protein is an essential splicing factor required for association of U2 small nuclear ribonucleoprotein with pre-mRNA, and it also plays an important role in mRNA export from the nucleus to the cytoplasm. This gene belongs to a cluster of genes localized in the vicinity of the genes encoding tumor necrosis factor alpha and tumor necrosis factor beta. These …

**Accessions** — [HGNC:13917](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13917) · Entrez [7919](https://www.ncbi.nlm.nih.gov/gene/7919) · UniProt [Q13838](https://www.uniprot.org/uniprotkb/Q13838) · Ensembl [ENSG00000198563](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198563)

## Data

Gene col 12619: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12619); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12619, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12619]; `tensor/DDL_lfc|DDL_z.npy` [12619]; `embed/gene_vectors.npy` [12619]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12619 or target_col == 12619). Every well: [[DDX39B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX39B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
