---
symbol: "SHCBP1"
type: "gene"
col: 10080
ensembl_id: "ENSG00000171241"
name: "SHC binding and spindle associated 1"
location: "16q11.2"
module: 22
arm: "+"
pooled_cpm: 43.9
n_lines_expressing: 49
n_dd_up: 31
n_dd_down: 21
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# SHCBP1

*SHC binding and spindle associated 1* — 16q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (24 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.63× (z +7.3, q 2e-10, up in 30 of 47 measured lines) ⚠ cell-cycle shift, explains ~95% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.72× (z +4.2, q 0.001, up in 20 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.705× (z -7.4, q 6e-11, down in 26 of 47 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Rapamycin (drug)]] 5 µM: 0.795× (z -4.8, q 1e-04, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PBK]] (+0.89, fdr 7e-06), [[NCAPG]] (+0.87, fdr 7e-06), [[PLK4]] (+0.87, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 24 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10080.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.63×** | +7.3 | 2e-10 | 30/47 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.38×** | +6.8 | 2e-09 | 31/47 (SNU-423, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | **1.56×** | +6.6 | 6e-09 | 31/47 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.34×** | +6.5 | 8e-09 | 30/47 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.52×** | +6.2 | 5e-08 | 23/45 (NCI-H23, PANC-1, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.40×** | +5.1 | 4e-05 | 19/46 (SW 900, NCI-H2030, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +4.7 | 2e-04 | 25/47 (PANC-1, RKO, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.36×** | +4.6 | 2e-04 | 20/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | **1.36×** | +4.5 | 5e-04 | 22/46 (LoVo, SW48, …) | top dose only |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.23×** | +4.4 | 7e-04 | 22/47 (Panc 03.27, NCI-H2030, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.23×** | +4.4 | 7e-04 | 22/47 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.35×** | +4.3 | 8e-04 | 25/47 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.72×** | +4.2 | 0.001 | 20/47 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.33×** | +4.1 | 0.002 | 18/38 (PANC-1, A-172, …) | all doses, flat | composition shift |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.21×** | +4.0 | 0.003 | 15/47 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.004 | 20/47 (hTERT-HPNE, A549, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.015 | 15/47 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.024 | 18/47 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.041 | 11/47 (SW480, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.056 | 13/47 (NCI-H2030, NCI-H1573, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.056 | 15/47 (NCI-H460, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10080.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.705×** | -7.4 | 6e-11 | 26/47 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.610×** | -7.3 | 6e-11 | 34/47 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.685×** | -5.6 | 3e-06 | 30/47 (Hs 766T, A498, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.671×** | -5.6 | 3e-06 | 29/47 (A-172, KATO III, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **0.493×** | -5.4 | 6e-06 | 21/43 (LS 180, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.627×** | -5.0 | 7e-05 | 25/47 (SW480, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **0.795×** | -4.8 | 1e-04 | 27/47 (MIA PaCa-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.733×** | -4.4 | 6e-04 | 24/47 (J82, SW 1088, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.813×** | -4.4 | 8e-04 | 23/47 (A-172, HCT15, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.736×** | -4.3 | 9e-04 | 26/47 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 5 µM |  | **0.596×** | -4.0 | 0.003 | 19/46 (Hs 766T, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.765×** | -4.0 | 0.003 | 22/47 (SNU-1, Hs 766T, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.772×** | -3.8 | 0.005 | 20/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.836× | -3.8 | 0.007 | 22/47 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.838× | -3.7 | 0.008 | 17/47 (NCI-H1792, HT-29, …) | top dose only |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.848× | -3.5 | 0.017 | 19/47 (SW480, COLO 205, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.800×** | -3.3 | 0.026 | 10/47 (RKO, NCI-H2030, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.804×** | -3.2 | 0.034 | 17/46 (NCI-H2030, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Futibatinib (drug)]] 5 µM |  | **0.662×** | -3.2 | 0.040 | 14/45 (hTERT-HPNE, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.808×** | -3.2 | 0.040 | 17/47 (HEC-1-A, HCT15, …) | all doses, flat |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.674×** | -3.0 | 0.059 | 9/47 (Panc 03.27, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.05 µM |  | **0.816×** | -3.0 | 0.060 | 16/47 (SW 1271, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10080. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 95.2 | 0 | 9 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.236× (z -21.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.325× (z -16.6) |
| [[A-172 (line)]] | wt | 65.6 | 0 | 6 (5 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.123× (z -15.4) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.341× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 25.6 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.281× (z -10.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.219× (z -9.1) |
| [[PANC-1 (line)]] | alt | 27.8 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +15.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 58.8 | 0 | 3 (2 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.114× (z -16.4) |
| [[LS 180 (line)]] | wt | 23.5 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.255× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 42.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 43.9 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.156× (z -13.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.145× (z -10.0) |
| [[A-427 (line)]] | wt | 50.1 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.274× (z -14.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 39.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +11.6) ⚠ cell-cycle shift, would explain all of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.270× (z -9.3) ⚠ cell-cycle shift, explains ~93% of this change |
| [[KATO III (line)]] | alt | 54.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +8.6) ⚠ cell-cycle shift, explains ~95% of this change | [[Bortezomib (drug)]] 0.05 µM 0.281× (z -9.5) ⚠ cell-cycle shift, explains ~78% of this change |
| [[C-33 A (line)]] | alt | 38.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 71.5 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0808× (z -14.4) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 45.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.363× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 43.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 21.1 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.38× (z +9.6) ⚠ cell-cycle shift, explains ~95% of this change | — |
| [[NCI-H2030 (line)]] | alt | 75.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 41.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 68.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.327× (z -9.1) ⚠ cell-cycle shift, explains ~78% of this change |
| [[SNU-423 (line)]] | alt | 30.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +9.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[SW480 (line)]] | alt | 44.8 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +9.5) ⚠ cell-cycle shift, explains ~95% of this change | — |
| [[AN3 CA (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.1 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10080), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBK]] | +0.89 | +0.89 / +0.90 | both halves | 7e-06 | STRING 834 |
| [[NCAPG]] | +0.87 | +0.86 / +0.85 | both halves | 7e-06 | STRING 830 |
| [[PLK4]] | +0.87 | +0.86 / +0.87 | both halves | 7e-06 | STRING 513 |
| [[KIF15]] | +0.86 | +0.86 / +0.85 | both halves | 7e-06 | STRING 646 |
| [[KIF22]] | +0.86 | +0.84 / +0.85 | both halves | 7e-06 | STRING 434 |
| [[KIF11]] | +0.86 | +0.85 / +0.85 | both halves | 7e-06 | STRING 863 |
| [[SPC25]] | +0.85 | +0.82 / +0.87 | both halves | 7e-06 | STRING 687 |
| [[RACGAP1]] | +0.85 | +0.85 / +0.83 | both halves | 7e-06 | STRING 965 |
| [[AURKB]] | +0.85 | +0.85 / +0.82 | both halves | 7e-06 | STRING 555 |
| [[CDCA5]] | +0.85 | +0.87 / +0.83 | both halves | 7e-06 | STRING 583 |
| [[CDK1]] | +0.84 | +0.83 / +0.84 | both halves | 7e-06 | STRING 698 |
| [[MAD2L1]] | +0.84 | +0.86 / +0.80 | both halves | 7e-06 | STRING 712 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises SHCBP1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.46× lower at baseline in the lines without PIMREG | 0.008 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises SHCBP1's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.02× lower at baseline in the lines without NEURL1B | 0.069 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[AURKB]] | C | AURKB activity raises SHCBP1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.57× lower at baseline in the lines without AURKB | 0.033 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises SHCBP1's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.15× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[C21orf58]], [[SKA3]] | C | C21orf58, SKA3 activity raises SHCBP1's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 2.75× lower at baseline in the lines without C21orf58, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[PBK]] | C | PBK activity raises SHCBP1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.43× lower at baseline in the lines without PBK | 0.080 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.827). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.7, -52.5); signed map (-46.0, -43.4). **Vector** length 139, 46.0% of its response variance represented; |z| ≥ 3 in 1,294 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.67 to 60); *DREAM G2/M down* (control, mean cos +0.71 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.64 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.4 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.9 | +6.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +3.7 | +5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.6 |
|  | [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +3.2 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +1.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.5 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.4 | +2.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.4 | +2.4 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +2.2 | +3.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | -6.7 | -5.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | -6.1 | -7.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.1 | -7.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -1.5 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -3.8 | -5.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.7 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -1.3 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -3.1 | -3.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -3.1 | -3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.1 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | SHC binding and spindle associated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q11.2 — chr16:46,578,591-46,621,379 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22009, PAL |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEM2](https://www.uniprot.org/uniprotkb/Q8NEM2) (SHC SH2 domain-binding protein 1):

> May play a role in signaling pathways governing cellular proliferation, cell growth and differentiation. May be a component of a novel signaling pathway downstream of Shc. Acts as a positive regulator of FGF signaling in neural progenitor cells.

**Summary**, from NCBI Gene [79801](https://www.ncbi.nlm.nih.gov/gene/79801):

> Predicted to enable SH2 domain binding activity. Predicted to be involved in fibroblast growth factor receptor signaling pathway and regulation of neural precursor cell proliferation. Located in midbody and mitotic spindle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29547](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29547) · Entrez [79801](https://www.ncbi.nlm.nih.gov/gene/79801) · UniProt [Q8NEM2](https://www.uniprot.org/uniprotkb/Q8NEM2) · Ensembl [ENSG00000171241](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171241)

## Data

Gene col 10080: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10080); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10080, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10080]; `tensor/DDL_lfc|DDL_z.npy` [10080]; `embed/gene_vectors.npy` [10080]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10080 or target_col == 10080). Every well: [[SHCBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SHCBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
