---
symbol: "WDR3"
type: "gene"
col: 776
ensembl_id: "ENSG00000065183"
name: "WD repeat domain 3"
location: "1p12"
module: 33
arm: "+"
pooled_cpm: 48.75
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 11
n_dd_up_clean: 19
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# WDR3

*WD repeat domain 3* — 1p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (12 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.11× (z +15.4, q 0e+00, up in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 3.65× (z +14.0, q 2e-42, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.769× (z -7.7, q 5e-12, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR1B]] (+0.90, fdr 7e-06), [[GEMIN5]] (+0.83, fdr 7e-06), [[PDCD11]] (+0.80, fdr 7e-06).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ATXN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 776.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.11×** | +15.4 | 0e+00 | 44/48 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.09×** | +15.2 | 0e+00 | 47/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.03×** | +14.6 | 0e+00 | 45/48 (A498, Hs 766T, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.02×** | +14.6 | 1e-45 | 44/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.65×** | +14.0 | 2e-42 | 41/48 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.89×** | +11.5 | 2e-28 | 44/49 (NCI-H23, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +7.9 | 2e-13 | 23/35 (SK-MEL-2, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.07×** | +7.8 | 3e-13 | 38/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.05×** | +7.7 | 6e-13 | 33/48 (A498, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.47×** | +7.6 | 2e-12 | 30/47 (SHP-77, NCI-H1792, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +7.3 | 2e-11 | 31/48 (HT-29, C32, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.89×** | +6.9 | 3e-10 | 33/48 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.86×** | +6.7 | 9e-10 | 32/48 (AsPC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.36×** | +6.1 | 4e-08 | 25/46 (SW 900, C32, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +6.0 | 8e-08 | 23/48 (A498, SNU-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +5.2 | 6e-06 | 22/48 (NCI-H23, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.62×** | +5.2 | 6e-06 | 20/48 (PANC-1, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +5.1 | 7e-06 | 22/48 (NCI-H1792, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.28×** | +5.0 | 1e-05 | 23/48 (H4, A498, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.44×** | +4.8 | 4e-05 | 21/48 (A498, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.39×** | +4.3 | 5e-04 | 18/48 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.16× | +4.2 | 5e-04 | 8/49 (A549, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 776.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.769×** | -7.7 | 5e-12 | 27/48 (RKO, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.760×** | -5.7 | 3e-06 | 24/47 (NCI-H460, RPMI-7951, …) | two highest doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.793×** | -4.8 | 2e-04 | 20/48 (RKO, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.787×** | -4.8 | 2e-04 | 19/47 (NCI-H2030, J82, …) | two highest doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.795×** | -4.8 | 2e-04 | 16/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.806×** | -4.3 | 0.001 | 18/48 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.817×** | -4.1 | 0.004 | 21/47 (LoVo, A-427, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.825×** | -4.0 | 0.004 | 15/48 (PANC-1, KATO III, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.833×** | -3.9 | 0.006 | 16/48 (LoVo, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.703×** | -3.8 | 0.007 | 11/48 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.847× | -3.5 | 0.025 | 15/49 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.847× | -3.5 | 0.025 | 16/47 (RKO, KATO III, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.850× | -3.4 | 0.030 | 11/47 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.867× | -3.2 | 0.061 | 10/48 (LoVo, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.748×** | -3.2 | 0.061 | 5/48 (LoVo, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.857× | -3.1 | 0.069 | 12/47 (LOX-IMVI, LoVo, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.899× | -3.0 | 0.092 | 10/48 (A549, SW1417, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.902× | -3.0 | 0.094 | 11/48 (LoVo, H4, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 776. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 25.9 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 31.4 | 6 (5 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.09× (z +10.4) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.71× (z +10.3) | — |
| [[RKO (line)]] | wt | 96.9 | 1 | 5 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 8.29× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -18.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.336× (z -14.7) |
| [[A-172 (line)]] | wt | 21.5 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.36× (z +9.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 172 | 2 (1 ⚠) | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.68× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.326× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.570× (z -9.0) |
| [[Hs 766T (line)]] | wt | 38.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.96× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 49.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.29× (z +9.4) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[LoVo (line)]] | wt | 28.5 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.76× (z +11.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H23 (line)]] | alt | 170 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.36× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -14.0) |
| [[NCI-H2347 (line)]] | alt | 37.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.62× (z +11.0) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[PANC-1 (line)]] | alt | 57.2 | 1 | 2 | [[PH-797804 (drug)]] 5 µM 7.31× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -11.3) |
| [[SW48 (line)]] | wt | 88.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -9.8) |
| [[SW480 (line)]] | alt | 53.6 | 3 (2 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 5.64× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 75.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[CFPAC-1 (line)]] | alt | 32.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.81× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 64.6 | 2 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 7.88× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 18.9 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.57× (z +9.3) ⚠ toxic; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 39.6 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.44× (z +8.7) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -8.5) |
| [[SHP-77 (line)]] | alt | 123 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.85× (z +11.7) ⚠ toxic; cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 5 µM 0.367× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 64.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.356× (z -9.9) |
| [[A-427 (line)]] | wt | 43.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 64.1 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.74× (z +10.9) ⚠ unreliable plate only | — |
| [[AsPC-1 (line)]] | alt | 24.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.98× (z +8.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[C-33 A (line)]] | alt | 74.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -9.2) |
| [[CHP-212 (line)]] | wt | 77.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0827× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 20.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +9.0) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[J82 (line)]] | alt | 44.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.533× (z -9.0) |
| [[KATO III (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.233× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 61.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -11.7) |
| [[SNU-423 (line)]] | alt | 25.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.25× (z +8.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[SW1417 (line)]] | alt | 42.3 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.61× (z +8.9) ⚠ unreliable plate only | — |
| [[A549 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 71.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 776), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1B]] | +0.90 | +0.89 / +0.88 | both halves | 7e-06 | STRING 958 |
| [[GEMIN5]] | +0.83 | +0.78 / +0.81 | both halves | 7e-06 | same gene group |
| [[PDCD11]] | +0.80 | +0.75 / +0.81 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 997 |
| [[WDR36]] | +0.79 | +0.83 / +0.69 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[NLE1]] | +0.78 | +0.81 / +0.74 | both halves | 7e-06 | same gene group; STRING 671 |
| [[DKC1]] | +0.77 | +0.79 / +0.76 | both halves | 7e-06 | pathway: rRNA modification in the nucleus and cytosol; STRING 670 |
| [[URB1]] | +0.76 | +0.78 / +0.77 | both halves | 7e-06 | STRING 684 |
| [[LYAR]] | +0.76 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[DHX33]] | +0.76 | +0.75 / +0.84 | both halves | 7e-06 | STRING 520 |
| [[WDR43]] | +0.75 | +0.80 / +0.79 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[UTP18]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[NARS2]] | +0.75 | +0.69 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATXN1]] | B | ATXN1 activity lowers WDR3's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 1.80× higher at baseline in the lines without ATXN1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[MAP2K1]] | B | MAP2K1 activity raises WDR3's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.895). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.7, -39.2); signed map (-6.9, -51.1). **Vector** length 131, 42.2% of its response variance represented; |z| ≥ 3 in 1,255 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.66 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.1 | +14.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.3 | +14.0 |
|  | [[EX229 (drug)]] 5 µM |  | +6.2 | +7.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.6 | +7.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.1 | +6.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.6 | +6.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.3 | -7.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.8 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -7.0 | -4.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.9 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.2 | -4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.0 | -5.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.7 | -4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p12 — chr1:117,929,720-117,966,543 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12796, UTP12, DIP2 |
| Gene groups (HGNC) | WD repeat domain containing; UTPb subcomplex |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNX4](https://www.uniprot.org/uniprotkb/Q9UNX4) (WD repeat-containing protein 3):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome.

**Summary**, from NCBI Gene [10885](https://www.ncbi.nlm.nih.gov/gene/10885):

> This gene encodes a nuclear protein containing 10 WD repeats. WD repeats are approximately 30- to 40-amino acid domains containing several conserved residues, which usually include a trp-asp at the C-terminal end. Proteins belonging to the WD repeat family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12755](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12755) · Entrez [10885](https://www.ncbi.nlm.nih.gov/gene/10885) · UniProt [Q9UNX4](https://www.uniprot.org/uniprotkb/Q9UNX4) · Ensembl [ENSG00000065183](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065183)

## Data

Gene col 776: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 776); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 776, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 776]; `tensor/DDL_lfc|DDL_z.npy` [776]; `embed/gene_vectors.npy` [776]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 776 or target_col == 776). Every well: [[WDR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
