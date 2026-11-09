---
symbol: "CPNE1"
type: "gene"
col: 13170
ensembl_id: "ENSG00000214078"
name: "copine 1"
location: "20q11.22"
module: 3
arm: "-"
pooled_cpm: 126.96
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CPNE1

*copine 1* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.77× (z +17.2, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.723× (z -7.0, q 1e-09, down in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 2 lines (RPMI-7951 0.399×, SW1417 0.469×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.425×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.433×; ⚠ toxic; transcription drop); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1088 0.0990×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YWHAE]] (+0.70, fdr 7e-06), [[NEK9]] (+0.69, fdr 7e-06), [[HNRNPK]] (+0.69, fdr 1e-05); moves opposite to [[SLC25A29]] (-0.66, fdr 8e-06), [[BAHD1]] (-0.66, fdr 1e-05), [[TRIM62]] (-0.62, fdr 2e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13170.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +17.2 | 0e+00 | 42/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +8.2 | 9e-14 | 38/48 (LoVo, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +7.9 | 5e-13 | 43/49 (RKO, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +7.8 | 1e-12 | 33/48 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +7.4 | 2e-11 | 38/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.44×** | +7.2 | 8e-11 | 40/48 (HT-29, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.84×** | +6.8 | 7e-10 | 39/48 (RKO, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +5.2 | 2e-05 | 30/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.27×** | +5.1 | 2e-05 | 24/49 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | **1.27×** | +5.0 | 3e-05 | 31/48 (HT-29, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.0 | 4e-05 | 19/48 (NCI-H2347, AsPC-1, …) | top dose only | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +4.0 | 0.003 | 24/47 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +3.9 | 0.004 | 22/44 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.20×** | +3.9 | 0.004 | 23/48 (Hs 766T, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.006 | 19/48 (PANC-1, HT-29, …) | inconsistent across doses | position effect removed |
| [[Fumaric acid (drug)]] 0.05 µM |  | **1.21×** | +3.8 | 0.006 | 25/48 (Hs 766T, J82, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.020 | 21/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.058 | 19/48 (J82, PANC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13170.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 2 lines (RPMI-7951 0.399×, SW1417 0.469×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.425×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 0.433×; ⚠ toxic; transcription drop); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1088 0.0990×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.723×** | -7.0 | 1e-09 | 40/48 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.780×** | -5.4 | 2e-05 | 25/48 (PANC-1, H4, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.800×** | -4.8 | 2e-04 | 27/48 (HOP62, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.675×** | -4.4 | 0.001 | 30/45 (KATO III, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.874× | -4.1 | 0.004 | 8/48 (A-427, SHP-77, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 0.863× | -3.2 | 0.13 | 17/48 (C-33 A, SW 900, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.870× | -3.0 | 0.19 | 18/48 (KATO III, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.871× | -3.0 | 0.19 | 8/48 (HT-29, PANC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13170. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 186 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.425× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 94.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +17.7) | — |
| [[PANC-1 (line)]] | alt | 128 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +20.8) | — |
| [[RPMI-7951 (line)]] | alt | 169 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +15.7) | [[Docetaxel (drug)]] 0.05 µM 0.399× (z -12.4) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 110 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.8) | — |
| [[A498 (line)]] | wt | 80.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.8) | — |
| [[C32 (line)]] | wt | 61.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +15.8) | — |
| [[COLO 205 (line)]] | alt | 107 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.1) | — |
| [[HOP62 (line)]] | alt | 127 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +12.3) | — |
| [[HS-578T (line)]] | alt | 121 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +15.4) | — |
| [[LOX-IMVI (line)]] | wt | 150 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +14.2) | — |
| [[LS 180 (line)]] | wt | 103 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.6) | — |
| [[NCI-H1792 (line)]] | alt | 202 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +19.2) | — |
| [[NCI-H460 (line)]] | wt | 91.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +19.1) | — |
| [[SK-MEL-2 (line)]] | alt | 133 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 131 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.9) | — |
| [[A549 (line)]] | wt | 108 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.36× (z +10.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 96.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 115 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 85.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.3) | — |
| [[Hs 766T (line)]] | wt | 257 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.2) | — |
| [[J82 (line)]] | alt | 168 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.9) | — |
| [[KATO III (line)]] | alt | 169 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.541× (z -8.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[MIA PaCa-2 (line)]] | alt | 88.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 92.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 148 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +15.6) | — |
| [[NCI-H23 (line)]] | alt | 230 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 77.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +9.6) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[SNU-423 (line)]] | alt | 145 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +8.6) | — |
| [[SW 1088 (line)]] | alt | 143 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0990× (z -10.0) |
| [[SW1417 (line)]] | alt | 189 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.469× (z -9.8) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 81.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.3) | — |
| [[SW480 (line)]] | alt | 141 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +13.6) | — |
| [[A-427 (line)]] | wt | 206 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 114 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 172 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 101 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 296 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 97.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13170), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAE]] | +0.70 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[NEK9]] | +0.69 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[HNRNPK]] | +0.69 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[ZC3H11A]] | +0.66 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[SF3B3]] | +0.66 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[SLC35A5]] | +0.64 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ANAPC13]] | +0.63 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[CNOT3]] | +0.63 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[HNRNPL]] | +0.63 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[NCOA4]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[BMI1]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[EIF4G2]] | +0.61 | +0.61 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A29]] | -0.66 | -0.63 / -0.58 | both halves | 8e-06 |  |
| [[BAHD1]] | -0.66 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[TRIM62]] | -0.62 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[RAD9A]] | -0.62 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[ATOX1]] | -0.60 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[TPST2]] | -0.60 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[MED31]] | -0.59 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[MYO9B]] | -0.59 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[PBX4]] | -0.59 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[SDHAP2]] | -0.58 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[MAP3K9]] | -0.58 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[UBTD1]] | -0.58 | -0.52 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CPNE1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ICE2]] | C | ICE2's natural level strengthens CPNE1's drug response | ICE2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.65, reverse -0.09; direction not clear | 0.045 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.632). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-9.9, -0.2); signed map (16.1, -33.3). **Vector** length 115, 30.5% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +17.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.5 | +7.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.4 | +5.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.0 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.0 | +2.1 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -7.4 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -6.1 | -3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -4.6 | -5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.5 | -1.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.4 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -3.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.4 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | -1.7 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | copine 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22 — chr20:35,626,031-35,664,956 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CPN1 |
| Gene groups (HGNC) | Copines |
| Reactome | 5 pathways, smallest: Glycerophospholipid biosynthesis; Phospholipid metabolism; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99829](https://www.uniprot.org/uniprotkb/Q99829) (Copine-1):

> Calcium-dependent phospholipid-binding protein that plays a role in calcium-mediated intracellular processes. Involved in the TNF receptor signaling pathway in a calcium-dependent manner. Exhibits calcium-dependent phospholipid binding properties. Plays a role in neuronal progenitor cell differentiation; induces neurite outgrowth via a AKT-dependent signaling cascade and calcium-independent manner. May recruit target proteins to the cell membrane in a calcium-dependent manner. May function in …

**Summary**, from NCBI Gene [8904](https://www.ncbi.nlm.nih.gov/gene/8904):

> Calcium-dependent membrane-binding proteins may regulate molecular events at the interface of the cell membrane and cytoplasm. This gene encodes a calcium-dependent protein that also contains two N-terminal type II C2 domains and an integrin A domain-like sequence in the C-terminus. However, the encoded protein does not contain a predicted signal sequence or transmembrane domains. This protein has a broad tissue distribution and it may function in membrane trafficking. This gene and the gene …

**Accessions** — [HGNC:2314](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2314) · Entrez [8904](https://www.ncbi.nlm.nih.gov/gene/8904) · UniProt [Q99829](https://www.uniprot.org/uniprotkb/Q99829) · Ensembl [ENSG00000214078](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214078)

## Data

Gene col 13170: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13170); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13170, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13170]; `tensor/DDL_lfc|DDL_z.npy` [13170]; `embed/gene_vectors.npy` [13170]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13170 or target_col == 13170). Every well: [[CPNE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPNE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
