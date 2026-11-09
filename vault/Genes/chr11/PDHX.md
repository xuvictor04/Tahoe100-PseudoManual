---
symbol: "PDHX"
type: "gene"
col: 3139
ensembl_id: "ENSG00000110435"
name: "pyruvate dehydrogenase complex component X"
location: "11p13"
module: 82
arm: "+"
pooled_cpm: 90.33
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# PDHX

*pyruvate dehydrogenase complex component X* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +14.2, q 8e-43, up in 35 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.717× (z -8.7, q 2e-15, down in 27 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.732× (z -8.5, q 8e-15, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIAL1]] (+0.62, fdr 5e-05), [[PMS2P4-1]] (+0.60, fdr 1e-05), [[MRPL11]] (+0.59, fdr 3e-05); moves opposite to [[GPRIN1]] (-0.62, fdr 3e-05), [[R3HDM4]] (-0.61, fdr 4e-05), [[ADAMTSL5]] (-0.59, fdr 3e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3139.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +14.2 | 8e-43 | 35/49 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +12.8 | 3e-35 | 42/48 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +11.6 | 6e-29 | 42/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +11.2 | 6e-27 | 40/50 (Panc 03.27, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.11×** | +10.6 | 6e-24 | 42/49 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +7.3 | 3e-11 | 32/48 (PANC-1, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.20×** | +7.0 | 3e-10 | 21/48 (MIA PaCa-2, J82, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +6.8 | 1e-09 | 22/48 (HOP62, SW1417, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +6.4 | 1e-08 | 31/48 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +5.9 | 2e-07 | 26/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +5.8 | 3e-07 | 22/48 (SK-MEL-2, NCI-H1573, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +5.7 | 4e-07 | 29/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.22×** | +5.3 | 4e-06 | 23/48 (MIA PaCa-2, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +5.3 | 4e-06 | 24/48 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +4.3 | 6e-04 | 11/48 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +3.5 | 0.013 | 13/48 (A-427, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.028 | 8/49 (PANC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.029 | 7/48 (J82, A-172, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.056 | 11/48 (PANC-1, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.12× | +3.0 | 0.069 | 5/48 (H4, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3139.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.717×** | -8.7 | 2e-15 | 27/44 (NCI-H23, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.732×** | -8.5 | 8e-15 | 34/48 (SW480, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.757×** | -7.5 | 9e-12 | 30/48 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.761×** | -6.8 | 1e-09 | 28/45 (NCI-H2030, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.799×** | -6.1 | 1e-07 | 25/48 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.807×** | -5.8 | 5e-07 | 22/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.879× | -4.9 | 6e-05 | 15/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -4.9 | 7e-05 | 21/48 (HOP62, SW 1271, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.848× | -4.5 | 5e-04 | 23/49 (C-33 A, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.828×** | -3.6 | 0.014 | 16/48 (NCI-H460, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.870× | -3.6 | 0.014 | 20/47 (NCI-H2030, SW480, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.883× | -3.4 | 0.032 | 11/47 (A-427, NCI-H661, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.887× | -3.3 | 0.049 | 13/48 (SW480, HCT15, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | 0.852× | -3.1 | 0.077 | 12/48 (MIA PaCa-2, LS 180, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.893× | -3.1 | 0.080 | 10/49 (SW480, AN3 CA, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3139. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 69.3 | 3 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.470× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.531× (z -9.0) |
| [[SW480 (line)]] | alt | 129 | 2 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.38× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.491× (z -12.2) |
| [[HOP62 (line)]] | alt | 79.8 | 4 | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +12.9) | [[Auranofin (drug)]] 5 µM 0.544× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 50.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 69.9 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.34× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +8.7) | — |
| [[HT-29 (line)]] | alt | 73.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +13.2) | — |
| [[NCI-H2030 (line)]] | alt | 76.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.321× (z -12.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 80.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +12.9) | — |
| [[PANC-1 (line)]] | alt | 107 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +12.1) | — |
| [[A-427 (line)]] | wt | 73.6 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 74.0 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 159 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.74× (z +10.1) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.39× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 95.5 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.156× (z -23.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 68.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 84.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +11.1) | — |
| [[AN3 CA (line)]] | alt | 75.2 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.230× (z -8.5) |
| [[C-33 A (line)]] | alt | 78.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -15.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.343× (z -10.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 33.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +13.7) | — |
| [[COLO 205 (line)]] | alt | 70.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.5) | — |
| [[H4 (line)]] | wt | 157 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.390× (z -9.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.367× (z -9.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 131 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +8.5) | — |
| [[J82 (line)]] | alt | 112 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.53× (z +8.6) ⚠ cell-cycle shift, explains ~8% of this change | — |
| [[LoVo (line)]] | wt | 86.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.204× (z -9.0) ⚠ toxic |
| [[LS 180 (line)]] | wt | 103 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 77.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.439× (z -8.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.353× (z -11.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 91.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.344× (z -11.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 77.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +11.0) | — |
| [[SW 1271 (line)]] | alt | 110 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.122× (z -10.6) ⚠ transcription drop; cell-cycle shift, explains ~18% of this change |
| [[SW48 (line)]] | wt | 53.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +9.1) | — |
| [[A-172 (line)]] | wt | 67.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 130 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 76.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 113 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 72.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 93.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3139), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIAL1]] | +0.62 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[PMS2P4-1]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[MRPL11]] | +0.59 | +0.43 / +0.51 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[SYNRG]] | +0.59 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[C5orf15]] | +0.58 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[PBLD]] | +0.58 | +0.36 / +0.32 | both halves | 2e-04 |  |
| [[LEMD3]] | +0.57 | +0.44 / +0.38 | both halves | 7e-05 |  |
| [[MTREX]] | +0.57 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[CNPY2]] | +0.57 | +0.52 / +0.36 | both halves | 1e-04 |  |
| [[APPBP2]] | +0.57 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[PDSS2]] | +0.57 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[PNISR-AS1]] | +0.56 | +0.38 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRIN1]] | -0.62 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[R3HDM4]] | -0.61 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[ADAMTSL5]] | -0.59 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[GIPC1]] | -0.59 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[ATP1A3]] | -0.59 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[CCDC112]] | -0.58 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[TMOD2]] | -0.57 | -0.37 / -0.46 | both halves | 7e-05 |  |
| [[C15orf39]] | -0.55 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[AFDN]] | -0.55 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[RMC1]] | -0.54 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[MOCS1]] | -0.54 | -0.27 / -0.38 | both halves | 3e-04 |  |
| [[DUSP2]] | -0.53 | -0.47 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PDHX's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises PDHX's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction -0.471). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.1, 24.5); signed map (5.7, 3.1). **Vector** length 104, 26.4% of its response variance represented; |z| ≥ 3 in 1,084 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +12.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +14.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +11.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.2 | +6.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | +6.7 | +7.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.7 | +3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.4 | +2.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.5 | -8.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.5 | -6.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.4 | -7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -5.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -2.1 |
|  | [[Neratinib (drug)]] 5 µM |  | -2.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | pyruvate dehydrogenase complex component X |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:34,915,829-35,020,591 (+) |
| Ensembl biotype | protein_coding |
| Also known as | E3BP, proX, PDX1, OPDX, DLDBP |
| Gene groups (HGNC) | Pyruvate dehydrogenase complex subunits; MicroRNA protein coding host genes |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 7 pathways, smallest: PDH complex synthesizes acetyl-CoA from PYR; Regulation of pyruvate dehydrogenase (PDH) complex; Regulation of pyruvate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O00330](https://www.uniprot.org/uniprotkb/O00330) (Pyruvate dehydrogenase protein X component, mitochondrial):

> Required for anchoring dihydrolipoamide dehydrogenase (E3) to the dihydrolipoamide transacetylase (E2) core of the pyruvate dehydrogenase complexes of eukaryotes. This specific binding is essential for a functional PDH complex.

**Summary**, from NCBI Gene [8050](https://www.ncbi.nlm.nih.gov/gene/8050):

> The pyruvate dehydrogenase (PDH) complex is located in the mitochondrial matrix and catalyzes the conversion of pyruvate to acetyl coenzyme A. The PDH complex thereby links glycolysis to Krebs cycle. The PDH complex contains three catalytic subunits, E1, E2, and E3, two regulatory subunits, E1 kinase and E1 phosphatase, and a non-catalytic subunit, E3 binding protein (E3BP). This gene encodes the E3 binding protein subunit; also known as component X of the pyruvate dehydrogenase complex. This …

**Accessions** — [HGNC:21350](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21350) · Entrez [8050](https://www.ncbi.nlm.nih.gov/gene/8050) · UniProt [O00330](https://www.uniprot.org/uniprotkb/O00330) · Ensembl [ENSG00000110435](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110435)

## Data

Gene col 3139: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3139); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3139, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3139]; `tensor/DDL_lfc|DDL_z.npy` [3139]; `embed/gene_vectors.npy` [3139]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3139 or target_col == 3139). Every well: [[PDHX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDHX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
