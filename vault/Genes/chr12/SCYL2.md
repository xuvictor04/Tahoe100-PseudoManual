---
symbol: "SCYL2"
type: "gene"
col: 5800
ensembl_id: "ENSG00000136021"
name: "SCY1 like pseudokinase 2"
location: "12q23.1"
module: 146
arm: "-"
pooled_cpm: 102.91
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# SCYL2

*SCY1 like pseudokinase 2* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.31× (z +27.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.818× (z -6.6, q 2e-08, down in 25 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 0.739× (z -5.0, q 1e-04, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KPNA4]] (+0.59, fdr 2e-05), [[ACTR2]] (+0.56, fdr 1e-05), [[AKIRIN1]] (+0.55, fdr 2e-05); moves opposite to [[PRPF39]] (-0.52, fdr 2e-05), [[NELFA]] (-0.51, fdr 2e-05), [[TRIT1]] (-0.51, fdr 3e-05).
> It sits in the **-** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[TAK-733 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5800.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.31×** | +27.3 | 0e+00 | 47/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.43×** | +20.5 | 0e+00 | 46/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.21×** | +17.6 | 0e+00 | 47/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +13.9 | 5e-42 | 43/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.13×** | +13.7 | 6e-41 | 45/49 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.73×** | +12.7 | 8e-35 | 46/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.71×** | +12.3 | 7e-33 | 41/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +11.7 | 9e-30 | 44/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.54×** | +9.9 | 2e-21 | 38/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.53×** | +9.8 | 6e-21 | 41/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +9.1 | 3e-18 | 34/48 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.94×** | +8.0 | 6e-14 | 40/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.41×** | +7.9 | 9e-14 | 37/48 (MIA PaCa-2, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.23×** | +6.6 | 1e-09 | 21/49 (MIA PaCa-2, AsPC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.30×** | +5.8 | 3e-07 | 32/47 (LoVo, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +5.2 | 9e-06 | 27/48 (HCT15, KATO III, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.21×** | +4.1 | 1e-03 | 22/48 (KATO III, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | 1.19× | +4.0 | 0.002 | 17/48 (SHP-77, SNU-1, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.6 | 0.006 | 19/48 (LoVo, CFPAC-1, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.006 | 21/48 (LOX-IMVI, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.2 | 0.031 | 17/48 (SHP-77, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5800.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.818×** | -6.6 | 2e-08 | 25/48 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -6.0 | 7e-07 | 2/50 (NCI-H23, HOP62) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.739×** | -5.0 | 1e-04 | 31/48 (HepG2/C3A, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.801×** | -4.8 | 3e-04 | 25/45 (A-427, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.819×** | -4.6 | 4e-04 | 26/49 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.820×** | -4.6 | 4e-04 | 24/48 (HOP62, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.822×** | -4.6 | 4e-04 | 25/48 (SNU-423, C32, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.833×** | -4.3 | 0.001 | 21/48 (HOP62, A549, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.837× | -4.1 | 0.002 | 24/48 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 0.839× | -4.1 | 0.003 | 19/48 (LS 180, HS-578T, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.842× | -4.0 | 0.003 | 18/48 (HT-29, HCT15, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.893× | -3.7 | 0.008 | 9/48 (MIA PaCa-2, SW 1271, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.851× | -3.7 | 0.008 | 16/49 (LoVo, NCI-H2347, …) | two highest doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.894× | -3.7 | 0.008 | 9/48 (A-427, AsPC-1, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.873× | -3.2 | 0.061 | 12/48 (SW 1271, AN3 CA, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.879× | -3.0 | 0.094 | 16/48 (NCI-H661, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5800. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 118 | 13 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +27.6) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 205 | 7 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +24.2) | [[Selinexor (drug)]] 5 µM 0.390× (z -17.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 117 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +16.1) | — |
| [[HEC-1-A (line)]] | alt | 91.6 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +21.9) | — |
| [[LoVo (line)]] | wt | 125 | 9 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +13.6) | — |
| [[BT-474 (line)]] | alt | 93.5 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +16.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 89.9 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +22.3) | — |
| [[NCI-H1573 (line)]] | alt | 144 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 107 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +19.7) | — |
| [[CFPAC-1 (line)]] | alt | 63.0 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +19.2) | — |
| [[LS 180 (line)]] | wt | 111 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +14.2) | — |
| [[C32 (line)]] | wt | 122 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +16.2) | [[Dinaciclib (drug)]] 0.05 µM 0.402× (z -9.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 79.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +13.7) | — |
| [[KATO III (line)]] | alt | 70.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +13.2) | — |
| [[SW 900 (line)]] | alt | 98.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +17.7) | — |
| [[SW1417 (line)]] | alt | 116 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +15.7) | — |
| [[A-427 (line)]] | wt | 117 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +15.6) | [[Dinaciclib (drug)]] 0.05 µM 0.0818× (z -30.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 106 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +17.6) | — |
| [[COLO 205 (line)]] | alt | 82.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +14.4) | — |
| [[Hs 766T (line)]] | wt | 60.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +13.3) | — |
| [[RKO (line)]] | wt | 147 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.458× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 103 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.70× (z +11.0) | — |
| [[A498 (line)]] | wt | 76.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +17.5) | — |
| [[H4 (line)]] | wt | 76.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +12.6) | — |
| [[HepG2_C3A (line)]] | wt | 136 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 143 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +12.7) | [[Dinaciclib (drug)]] 0.05 µM 0.463× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 98.6 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +11.0) | [[Selinexor (drug)]] 5 µM 0.565× (z -9.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 117 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +21.6) | — |
| [[HCT15 (line)]] | alt | 82.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.8) | — |
| [[HS-578T (line)]] | alt | 80.5 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 92.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +19.4) | — |
| [[RPMI-7951 (line)]] | alt | 67.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.1) | — |
| [[SW48 (line)]] | wt | 116 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.272× (z -10.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 86.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +14.2) | — |
| [[HT-29 (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.335× (z -13.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 77.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +10.1) | — |
| [[J82 (line)]] | alt | 78.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 91.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +14.2) | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.153× (z -11.9) |
| [[Panc 03.27 (line)]] | alt | 65.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.4) | — |
| [[SHP-77 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.180× (z -9.7) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 93.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 74.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.4) | — |
| [[SW 1271 (line)]] | alt | 87.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.152× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 128 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 105 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 91.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5800), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA4]] | +0.59 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[ACTR2]] | +0.56 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[AKIRIN1]] | +0.55 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[SETX]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[RB1]] | +0.53 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ARPC2]] | +0.52 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[HOMER1]] | +0.51 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[RO60]] | +0.49 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[OSBPL11]] | +0.49 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[TJP1]] | +0.49 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[OSTM1]] | +0.48 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[TSTD2]] | +0.48 | +0.41 / +0.65 | both halves | 4e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF39]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[NELFA]] | -0.51 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[TRIT1]] | -0.51 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[PISD]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[TADA1]] | -0.49 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[GGA2]] | -0.49 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[EIF3E]] | -0.49 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[METTL22]] | -0.48 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[SUPV3L1]] | -0.48 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[TFB2M]] | -0.48 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[NDUFAF7]] | -0.48 | -0.36 / -0.57 | both halves | 1e-04 |  |
| [[SNRPA1]] | -0.47 | -0.39 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[TAK-733 (drug)]] 5 µM | C | SCYL2's natural level raises the cells' numbers under TAK-733 5 µM (protects the cells) | SCYL2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.71 | 0.250 over the table, 0.020 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **-** arm (projection on the module's main direction -0.500). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-57.3, 3.1); signed map (-5.6, 38.3). **Vector** length 85.9, 25.7% of its response variance represented; |z| ≥ 3 in 1,365 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.0 | -1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.6 | -1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +3.7 | +6.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.6 | +17.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.4 | +9.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.4 | +4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +0.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.8 | -1.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -8.1 | -6.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -5.6 | -4.1 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.7 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -3.2 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -3.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.7 | -4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -4.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.3 | -4.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.1 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | SCY1 like pseudokinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:100,267,140-100,341,715 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1360, CVAK104 |
| Gene groups (HGNC) | SCY1 like pseudokinases; Armadillo like helical domain containing; Pseudokinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P3W7](https://www.uniprot.org/uniprotkb/Q6P3W7) (SCY1-like protein 2):

> Component of the AP2-containing clathrin coat that may regulate clathrin-dependent trafficking at plasma membrane, TGN and endosomal system (Probable). A possible serine/threonine-protein kinase toward the beta2-subunit of the plasma membrane adapter complex AP2 and other proteins in presence of poly-L-lysine has not been confirmed. By regulating the expression of excitatory receptors at synapses, plays an essential role in neuronal function and signaling and in brain development (By …

**Summary**, from NCBI Gene [55681](https://www.ncbi.nlm.nih.gov/gene/55681):

> The protein encoded by this gene associates with clathrin-coated complexes at the plasma membrane and with endocytic coated vesicles. The encoded protein phosphorylates the beta2 subunit of the plasma membrane adapter complex AP2 and interacts with clathrin, showing involvement in clathrin-dependent pathways between the trans-Golgi network and the endosomal system. In addition, this protein has a role in the Wnt signaling pathway by targeting frizzled 5 (Fzd5) for lysosomal degradation. Two …

**Accessions** — [HGNC:19286](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19286) · Entrez [55681](https://www.ncbi.nlm.nih.gov/gene/55681) · UniProt [Q6P3W7](https://www.uniprot.org/uniprotkb/Q6P3W7) · Ensembl [ENSG00000136021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136021)

## Data

Gene col 5800: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5800); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5800, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5800]; `tensor/DDL_lfc|DDL_z.npy` [5800]; `embed/gene_vectors.npy` [5800]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5800 or target_col == 5800). Every well: [[SCYL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCYL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
