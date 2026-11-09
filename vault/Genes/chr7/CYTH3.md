---
symbol: "CYTH3"
type: "gene"
col: 162
ensembl_id: "ENSG00000008256"
name: "cytohesin 3"
location: "7p22.1"
module: 163
arm: "+"
pooled_cpm: 93.78
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/163"]
generated_by: "tahoemap"
---

# CYTH3

*cytohesin 3* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.85× (z +20.9, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.478× (z -14.1, q 2e-42, down in 35 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.714× (z -6.7, q 4e-09, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAP1A]] (+0.72, fdr 7e-06), [[TPST2]] (+0.70, fdr 1e-05), [[RNF38]] (+0.68, fdr 8e-06); moves opposite to [[OCIAD1]] (-0.64, fdr 1e-05), [[MAGOHB]] (-0.63, fdr 3e-05), [[PEF1]] (-0.62, fdr 5e-05).
> It is in [[Module 163]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[STARD9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 162.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.85×** | +20.9 | 0e+00 | 46/47 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.53×** | +18.5 | 0e+00 | 45/47 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.45×** | +17.9 | 0e+00 | 43/47 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +9.5 | 3e-19 | 39/47 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +8.0 | 1e-13 | 33/47 (HT-29, HepG2/C3A, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +8.0 | 2e-13 | 33/46 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.08×** | +7.6 | 2e-12 | 35/48 (PANC-1, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +7.3 | 2e-11 | 31/47 (SHP-77, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +6.3 | 1e-08 | 27/47 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +6.1 | 5e-08 | 32/47 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.79×** | +6.1 | 5e-08 | 29/44 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.30×** | +5.3 | 7e-06 | 27/47 (HepG2/C3A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.29×** | +5.1 | 1e-05 | 23/47 (KATO III, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +4.8 | 5e-05 | 24/47 (HepG2/C3A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +4.8 | 5e-05 | 21/48 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.007 | 16/48 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.016 | 6/47 (CFPAC-1, AN3 CA, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.32×** | +2.9 | 0.087 | 12/47 (NCI-H2347, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.16× | +2.9 | 0.088 | 17/47 (CFPAC-1, A-427, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 162.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.478×** | -14.1 | 2e-42 | 35/42 (A-427, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.537×** | -12.4 | 8e-33 | 39/48 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.714×** | -6.7 | 4e-09 | 32/47 (NCI-H1573, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.692×** | -6.3 | 4e-08 | 23/45 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.736×** | -6.1 | 1e-07 | 29/47 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -5.0 | 6e-05 | 20/47 (J82, SNU-1, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.772×** | -4.9 | 6e-05 | 26/47 (HOP62, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.786×** | -4.8 | 1e-04 | 26/47 (SW1417, HOP62, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 0.850× | -4.6 | 3e-04 | 27/47 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.856× | -4.4 | 7e-04 | 22/47 (SNU-1, HS-578T, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.668×** | -4.2 | 0.001 | 15/37 (Panc 03.27, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.702×** | -3.7 | 0.011 | 17/46 (SW1417, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.836× | -3.4 | 0.027 | 15/47 (NCI-H2347, Panc 03.27, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.783×** | -3.2 | 0.058 | 15/47 (SW1417, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.860× | -3.0 | 0.10 | 16/47 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 162. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 111 | 4 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.94× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.105× (z -24.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 94.3 | 4 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.90× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.333× (z -13.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 68.0 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.49× (z +13.2) | — |
| [[HepG2_C3A (line)]] | wt | 37.7 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.04× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 69.5 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.25× (z +9.1) | [[Harringtonine (drug)]] 5 µM 0.324× (z -12.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HT-29 (line)]] | alt | 35.7 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.57× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -8.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 94.4 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.69× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -16.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 199 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.21× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.393× (z -10.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 148 | 3 (3 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.79× (z +10.1) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.244× (z -10.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 82.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.75× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.267× (z -11.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 89.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -18.3) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 83.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.41× (z +11.5) | [[Selinexor (drug)]] 5 µM 0.503× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 88.2 | 1 | 3 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.66× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 54.8 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.22× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 117 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.71× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -10.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 55.7 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.11× (z +9.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.301× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 96.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.11× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.378× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 37.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.22× (z +11.0) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0664× (z -10.8) ⚠ toxic |
| [[A-427 (line)]] | wt | 94.7 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.18× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.0937× (z -25.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 64.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.92× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 80.1 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.94× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -11.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 46.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.10× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 39.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.45× (z +11.0) | — |
| [[H4 (line)]] | wt | 81.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.89× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 66.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.77× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -8.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 200 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.93× (z +10.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.21× (z +9.5) | [[Selinexor (drug)]] 5 µM 0.550× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 51.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.00× (z +13.3) | — |
| [[NCI-H1792 (line)]] | alt | 84.9 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.67× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -18.9) ⚠ cell-cycle shift, explains ~61% of this change |
| [[NCI-H23 (line)]] | alt | 51.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.22× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 87.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.12× (z +12.8) | — |
| [[SHP-77 (line)]] | alt | 75.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.85× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.103× (z -20.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 86.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.43× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -9.2) ⚠ cell-cycle shift, explains ~61% of this change |
| [[SW480 (line)]] | alt | 128 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.28× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.442× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 263 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -14.9) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -12.5) |
| [[AN3 CA (line)]] | alt | 116 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -9.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 165 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -11.3) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.208× (z -8.8) |
| [[CHP-212 (line)]] | wt | 40.4 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0714× (z -10.5) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -12.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 110 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.40× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 168 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.375× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 71.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.45× (z +9.1) | — |
| [[SW 1271 (line)]] | alt | 110 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.102× (z -10.5) |
| [[C-33 A (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 82.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 162), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAP1A]] | +0.72 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[TPST2]] | +0.70 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[RNF38]] | +0.68 | +0.72 / +0.58 | both halves | 8e-06 |  |
| [[UBE2G1]] | +0.67 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[SRPK2]] | +0.66 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[BICD2]] | +0.65 | +0.56 / +0.53 | both halves | 1e-05 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[GAS2L1]] | +0.65 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[INPP5F]] | +0.65 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[SPTLC2]] | +0.64 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[ANKRD27]] | +0.64 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[STRN]] | +0.63 | +0.71 / +0.35 | both halves | 1e-04 |  |
| [[GNB2]] | +0.63 | +0.65 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OCIAD1]] | -0.64 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[MAGOHB]] | -0.63 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[PEF1]] | -0.62 | -0.65 / -0.39 | both halves | 5e-05 |  |
| [[TRMT13]] | -0.62 | -0.63 / -0.40 | both halves | 5e-05 |  |
| [[KRR1]] | -0.61 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[WDR33]] | -0.61 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[MTHFSD]] | -0.60 | -0.59 / -0.37 | both halves | 7e-05 |  |
| [[LINC00174]] | -0.60 | -0.63 / -0.38 | both halves | 6e-05 |  |
| [[AIMP1]] | -0.60 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[C19orf54]] | -0.60 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[USP40]] | -0.60 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[ZNF764]] | -0.60 | -0.63 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD9]] | B | STARD9 activity raises CYTH3's level | lines that do not express STARD9 (8) vs lines expressing it (42) | 2.07× lower at baseline in the lines without STARD9 | 0.004 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent |
| [[LLGL2]] | B | LLGL2 activity strengthens CYTH3's drug response | lines that do not express LLGL2 (12) vs lines expressing it (36) | the lines without LLGL2 respond 0.76× as strongly (z diff +1.53); strongest at Belinostat 5 µM: 1.74x vs 2.56x (z diff +3.6) | 0.099 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR; target measured in part of the lines; artifact flags |
| [[GIPC1]] | C | GIPC1's natural level weakens CYTH3's drug response | GIPC1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.07; direction not clear | 0.064 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 163]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.728). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.8, 1.8); signed map (-42.8, -5.2). **Vector** length 121, 36.6% of its response variance represented; |z| ≥ 3 in 1,272 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.9 | +18.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.8 | +17.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.8 | +20.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.3 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +8.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.7 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.4 | +7.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.8 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.7 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.4 | -6.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -10.6 | -4.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -8.7 | -4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.9 | -6.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -4.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | +1.4 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -2.0 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | cytohesin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:6,161,779-6,272,644 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GRP1, ARNO3, cytohesin-3; previously PSCD3 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Cytohesins |
| Reactome | 4 pathways, smallest: Intra-Golgi traffic; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [O43739](https://www.uniprot.org/uniprotkb/O43739) (Cytohesin-3):

> Promotes guanine-nucleotide exchange on ARF1 and ARF6. Promotes the activation of ARF factors through replacement of GDP with GTP. Plays a role in the epithelial polarization (By similarity).

**Summary**, from NCBI Gene [9265](https://www.ncbi.nlm.nih.gov/gene/9265):

> This gene encodes a member of the PSCD (pleckstrin homology, Sec7 and coiled-coil domains) family. PSCD family members have identical structural organization that consists of an N-terminal coiled-coil motif, a central Sec7 domain, and a C-terminal pleckstrin homology (PH) domain. The coiled-coil motif is involved in homodimerization, the Sec7 domain contains guanine-nucleotide exchange protein (GEP) activity, and the PH domain interacts with phospholipids and is responsible for association of …

**Accessions** — [HGNC:9504](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9504) · Entrez [9265](https://www.ncbi.nlm.nih.gov/gene/9265) · UniProt [O43739](https://www.uniprot.org/uniprotkb/O43739) · Ensembl [ENSG00000008256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008256)

## Data

Gene col 162: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 162); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 162, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 162]; `tensor/DDL_lfc|DDL_z.npy` [162]; `embed/gene_vectors.npy` [162]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 162 or target_col == 162). Every well: [[CYTH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYTH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
