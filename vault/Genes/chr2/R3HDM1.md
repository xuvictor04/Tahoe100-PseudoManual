---
symbol: "R3HDM1"
type: "gene"
col: 542
ensembl_id: "ENSG00000048991"
name: "R3H domain containing 1"
location: "2q21.3"
module: 18
arm: "+"
pooled_cpm: 144.14
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# R3HDM1

*R3H domain containing 1* — 2q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.05× (z +21.2, q 0e+00, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.77× (z +16.7, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.606× (z -7.7, q 7e-12, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PMS1]] (+0.63, fdr 7e-06), [[MPHOSPH9]] (+0.62, fdr 1e-05), [[SUGP2]] (+0.61, fdr 1e-05); moves opposite to [[SAP18]] (-0.59, fdr 3e-05), [[ZNF490]] (-0.58, fdr 5e-05), [[IST1]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[VAMP5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 21 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 542.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.05×** | +21.2 | 0e+00 | 43/48 (A-172, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.00×** | +20.3 | 0e+00 | 44/48 (A-172, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.95×** | +19.6 | 0e+00 | 40/48 (A-172, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +16.7 | 0e+00 | 42/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.05×** | +11.1 | 2e-26 | 41/49 (AsPC-1, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +10.1 | 7e-22 | 36/48 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.37×** | +9.0 | 2e-17 | 26/44 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | **1.33×** | +8.5 | 2e-15 | 33/49 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +7.6 | 1e-12 | 24/48 (SW 900, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +7.2 | 3e-11 | 28/48 (HepG2/C3A, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.55×** | +6.7 | 1e-09 | 31/48 (MIA PaCa-2, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +6.2 | 3e-08 | 27/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 1.15× | +5.7 | 6e-07 | 20/49 (NCI-H2347, SNU-423, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.20×** | +5.4 | 2e-06 | 23/47 (H4, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.21×** | +5.3 | 4e-06 | 21/48 (SW480, Hs 766T, …) | top dose only | composition shift; position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +4.6 | 1e-04 | 18/49 (C32, HS-578T, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.014 | 9/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.11× | +3.0 | 0.061 | 16/48 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[Irinotecan (drug)]] 0.5 µM |  | 1.15× | +2.9 | 0.081 | 3/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.07× | +2.8 | 0.089 | 2/48 (HCT15, SW 900) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 542.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.606×** | -7.7 | 7e-12 | 37/49 (NCI-H460, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.773×** | -7.6 | 9e-12 | 29/48 (SW480, A-427, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.845× | -7.0 | 3e-10 | 26/48 (J82, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.761×** | -5.8 | 1e-06 | 27/48 (NCI-H661, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.825×** | -5.7 | 1e-06 | 25/48 (LS 180, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.849× | -4.8 | 1e-04 | 17/49 (AsPC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.744×** | -4.6 | 4e-04 | 24/48 (RPMI-7951, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.864× | -4.3 | 0.001 | 14/48 (HEC-1-A, H4, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.911× | -3.9 | 0.006 | 11/49 (LoVo, PANC-1, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.893× | -3.4 | 0.041 | 13/47 (RKO, LS 180, …) | two highest doses | low cells (technical?) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 0.889× | -3.4 | 0.041 | 9/49 (HOP62, SNU-423, …) | top dose only | plate-row cell shift |
| [[Temsirolimus (drug)]] 5 µM |  | 0.925× | -3.3 | 0.048 | 1/49 (RKO) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.892× | -3.2 | 0.061 | 12/48 (HT-29, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 542. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 189 | 7 (7 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.24× (z +11.4) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H1792 (line)]] | alt | 95.7 | 6 (5 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.76× (z +12.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.33× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -12.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 70.3 | 7 (6 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.82× (z +14.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.90× (z +11.1) | — |
| [[NCI-H460 (line)]] | wt | 191 | 3 (3 ⚠) | 3 (2 ⚠) | [[Belinostat (drug)]] 5 µM 1.76× (z +10.5) ⚠ cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.610× (z -13.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.370× (z -9.7) |
| [[A-172 (line)]] | wt | 116 | 5 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.44× (z +16.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.58× (z +12.3) | — |
| [[AsPC-1 (line)]] | alt | 85.5 | 5 (4 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.63× (z +14.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.66× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 222 | 5 (4 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.04× (z +10.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 1.86× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 125 | 4 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.29× (z +11.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 1.85× (z +8.7) | [[Auranofin (drug)]] 5 µM 0.495× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 76.9 | 3 (3 ⚠) | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.71× (z +11.5) ⚠ cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -13.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 59.8 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 160 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.23× (z +10.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.02× (z +9.3) | — |
| [[A498 (line)]] | wt | 156 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.10× (z +10.8) ⚠ cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.648× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 52.9 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.52× (z +13.6) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[COLO 205 (line)]] | alt | 61.4 | 4 (4 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.67× (z +12.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HOP62 (line)]] | alt | 124 | 4 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.54× (z +12.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.24× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 111 | 3 (2 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.10× (z +9.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 1.94× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.612× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 89.7 | 4 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.08× (z +11.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.46× (z +8.9) | — |
| [[J82 (line)]] | alt | 144 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.80× (z +9.6) ⚠ cell-cycle shift, explains ~37% of this change | [[Docetaxel (drug)]] 0.05 µM 0.592× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 107 | 4 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.45× (z +12.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 1.89× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 114 | 4 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.71× (z +11.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.25× (z +9.7) | — |
| [[Panc 03.27 (line)]] | alt | 97.4 | 4 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.66× (z +10.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.18× (z +8.6) | — |
| [[SW480 (line)]] | alt | 219 | 2 (1 ⚠) | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 1.58× (z +9.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 1.54× (z +8.6) | [[Auranofin (drug)]] 5 µM 0.491× (z -14.3) |
| [[C32 (line)]] | wt | 102 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.62× (z +10.3) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[Hs 766T (line)]] | wt | 69.8 | 3 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.03× (z +11.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[KATO III (line)]] | alt | 60.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.49× (z +9.1) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[RPMI-7951 (line)]] | alt | 109 | 3 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.55× (z +9.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 246 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.511× (z -10.6) |
| [[C-33 A (line)]] | alt | 283 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.537× (z -9.7) |
| [[PANC-1 (line)]] | alt | 264 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.640× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change |
| [[BT-474 (line)]] | alt | 87.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HepG2_C3A (line)]] | wt | 126 | 1 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.49× (z +10.0) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[LOX-IMVI (line)]] | wt | 169 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.549× (z -13.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H596 (line)]] | alt | 128 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.104× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 81.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.10× (z +8.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW 1271 (line)]] | alt | 216 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0726× (z -8.6) ⚠ toxic |
| [[SW1417 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.493× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 187 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.373× (z -10.8) |
| [[A549 (line)]] | wt | 158 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 193 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 151 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 542), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS1]] | +0.63 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[MPHOSPH9]] | +0.62 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[SUGP2]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[TTC13]] | +0.61 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[TBC1D31]] | +0.61 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[HERC2]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[MACROH2A1]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[CKAP5]] | +0.59 | +0.50 / +0.61 | both halves | 1e-05 | same gene group |
| [[NIN]] | +0.59 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[PKP4]] | +0.59 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[CLASP2]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[VWA8]] | +0.58 | +0.53 / +0.62 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAP18]] | -0.59 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[ZNF490]] | -0.58 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[IST1]] | -0.57 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[EIF3J-DT]] | -0.56 | -0.38 / -0.58 | both halves | 7e-05 |  |
| [[RNF103]] | -0.56 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[VAMP5]] | -0.55 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ZFYVE1]] | -0.55 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.55 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[FAM177B]] | -0.54 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[OSER1]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[FMO4]] | -0.53 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[TCEAL3]] | -0.53 | -0.37 / -0.50 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[VAMP5]] | B | VAMP5 activity lowers R3HDM1's level | lines that do not express VAMP5 (13) vs lines expressing it (37) | 1.50× higher at baseline in the lines without VAMP5 | 0.039 | ⚠ within organs, on part of the lines; also absent: GRAMD2B, LGALS3, LINC00511 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.528). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-30.3, -53.4); signed map (-19.1, -51.6). **Vector** length 130, 43.3% of its response variance represented; |z| ≥ 3 in 1,326 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.3 | +6.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | +6.0 | +5.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.6 | +16.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +4.5 | +3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | +4.5 | +3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.4 | +11.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.4 | +2.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.3 | +2.3 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.6 | +2.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -12.0 | -7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -10.3 | -7.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -8.6 | +0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -8.3 | +5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -7.2 | -0.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -5.3 | -5.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -4.8 | -4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | R3H domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.3 — chr2:135,531,455-135,725,270 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0029; previously R3HDM |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q15032](https://www.uniprot.org/uniprotkb/Q15032) carries no function annotation.

**Summary**, from NCBI Gene [23518](https://www.ncbi.nlm.nih.gov/gene/23518):

> Enables RNA binding activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9757](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9757) · Entrez [23518](https://www.ncbi.nlm.nih.gov/gene/23518) · UniProt [Q15032](https://www.uniprot.org/uniprotkb/Q15032) · Ensembl [ENSG00000048991](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000048991)

## Data

Gene col 542: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 542); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 542, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 542]; `tensor/DDL_lfc|DDL_z.npy` [542]; `embed/gene_vectors.npy` [542]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 542 or target_col == 542). Every well: [[R3HDM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/R3HDM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
