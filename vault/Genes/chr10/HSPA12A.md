---
symbol: "HSPA12A"
type: "gene"
col: 9198
ensembl_id: "ENSG00000165868"
name: "heat shock protein family A (Hsp70) member 12A"
location: "10q25.3"
module: 159
arm: "+"
pooled_cpm: 40.71
n_lines_expressing: 46
n_dd_up: 13
n_dd_down: 19
n_dd_up_clean: 10
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# HSPA12A

*heat shock protein family A (Hsp70) member 12A* — 10q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.60× (z +20.6, q 0e+00, up in 39 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.462× (z -16.0, q 0e+00, down in 25 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.357× (z -11.6, q 7e-29, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPAN9]] (+0.55, fdr 3e-05), [[RGS10]] (+0.52, fdr 2e-04), [[PRR5]] (+0.52, fdr 2e-04); moves opposite to [[HIPK3]] (-0.50, fdr 6e-05), [[ZSCAN30]] (-0.49, fdr 2e-04), [[GANC]] (-0.48, fdr 3e-04).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CAPN14]] → it (grade B ⚠); 3 go from it, the strongest it → [[UBE2Q2P2-1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9198.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.60×** | +20.6 | 0e+00 | 39/44 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.58×** | +20.5 | 0e+00 | 41/44 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.89×** | +13.7 | 3e-40 | 37/44 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +13.4 | 1e-38 | 36/44 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +11.1 | 1e-26 | 36/44 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +10.2 | 2e-22 | 25/44 (hTERT-HPNE, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +8.0 | 8e-14 | 25/44 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.40×** | +7.2 | 3e-11 | 21/43 (NCI-H460, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +6.9 | 4e-10 | 23/44 (HEC-1-A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +6.2 | 4e-08 | 23/44 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.66×** | +5.7 | 6e-07 | 19/39 (NCI-H1792, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.23×** | +4.4 | 6e-04 | 18/43 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.004 | 9/43 (AsPC-1, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +3.8 | 0.006 | 18/44 (NCI-H460, SW48, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.18× | +3.5 | 0.016 | 8/43 (NCI-H1792, PANC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +3.5 | 0.016 | 11/44 (CFPAC-1, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9198.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.462×** | -16.0 | 0e+00 | 25/35 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.495×** | -15.2 | 0e+00 | 28/42 (HCT15, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.357×** | -11.6 | 7e-29 | 34/45 (SW480, HT-29, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.603×** | -10.1 | 8e-22 | 28/41 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.439×** | -9.3 | 2e-18 | 35/44 (C-33 A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.659×** | -9.0 | 2e-17 | 28/43 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.688×** | -8.1 | 6e-14 | 28/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.722×** | -7.0 | 1e-10 | 22/44 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.740×** | -6.5 | 5e-09 | 24/43 (LS 180, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.805×** | -4.5 | 4e-04 | 15/44 (HOP62, A549, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **0.817×** | -4.4 | 6e-04 | 18/41 (HepG2/C3A, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.830×** | -4.0 | 0.003 | 17/44 (A549, A498, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~10% of this change | **0.828×** | -3.9 | 0.004 | 19/43 (HepG2/C3A, A498, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.836× | -3.9 | 0.004 | 13/43 (SW480, hTERT-HPNE, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.830×** | -3.9 | 0.004 | 18/44 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.882× | -3.8 | 0.004 | 14/44 (SW480, HOP62, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.832×** | -3.8 | 0.005 | 13/44 (COLO 205, A498, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.788×** | -3.7 | 0.007 | 11/43 (LoVo, SW 1271, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.736×** | -3.5 | 0.015 | 15/42 (LS 180, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | 0.859× | -3.3 | 0.027 | 2/44 (HepG2/C3A, COLO 205) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.899× | -3.3 | 0.027 | 10/44 (SW480, COLO 205, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9198. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 105 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.439× (z -10.5) |
| [[LS 180 (line)]] | wt | 62.1 | 2 | 6 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.66× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.330× (z -10.4) |
| [[PANC-1 (line)]] | alt | 23.0 | 6 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.23× (z +16.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.326× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 39.5 | 3 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.18× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.0590× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.348× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 35.7 | 3 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.15× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 24.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +13.2) | — |
| [[AsPC-1 (line)]] | alt | 13.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +15.5) | — |
| [[HT-29 (line)]] | alt | 20.2 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 4.71× (z +10.2) | [[TAK-901 (drug)]] 5 µM 0.0765× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 82.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.376× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 46.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +11.9) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.42× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -11.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 25.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.40× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.256× (z -9.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 39.6 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -13.7) |
| [[A498 (line)]] | wt | 86.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -13.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 66.3 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.4) ⚠ cell-cycle shift, explains ~66% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -12.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 26.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +15.0) | — |
| [[HepG2_C3A (line)]] | wt | 146 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -16.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 40.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0879× (z -22.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 29.3 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -13.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 33.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.37× (z +10.3) | — |
| [[HCT15 (line)]] | alt | 75.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0570× (z -19.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 43.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +15.6) | — |
| [[NCI-H2030 (line)]] | alt | 36.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -12.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 17.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 76.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0911× (z -13.4) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 55.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -11.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 22.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.78× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 36.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 17.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.54× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 23.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.25× (z +8.8) | — |
| [[J82 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -11.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 46.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -12.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -9.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 26.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.84× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 64.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -16.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +11.1) | — |
| [[SW 900 (line)]] | alt | 43.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0814× (z -18.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.75 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.93 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.70 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 88.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9198), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPAN9]] | +0.55 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[RGS10]] | +0.52 | +0.30 / +0.50 | both halves | 2e-04 |  |
| [[PRR5]] | +0.52 | +0.31 / +0.55 | both halves | 2e-04 |  |
| [[SH3BP1]] | +0.51 | +0.39 / +0.47 | both halves | 6e-05 |  |
| [[WFS1]] | +0.51 | +0.37 / +0.50 | both halves | 8e-05 |  |
| [[PBX4]] | +0.51 | +0.22 / +0.55 | both halves | 6e-04 |  |
| [[SGSM1]] | +0.51 | +0.34 / +0.51 | both halves | 1e-04 |  |
| [[ULBP3]] | +0.51 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[CAMK2G]] | +0.51 | +0.28 / +0.50 | both halves | 3e-04 | pathway: Cellular response to heat stress |
| [[SLC45A4]] | +0.51 | +0.31 / +0.45 | both halves | 2e-04 |  |
| [[IQSEC1]] | +0.50 | +0.32 / +0.48 | both halves | 2e-04 |  |
| [[PDE9A]] | +0.50 | +0.37 / +0.51 | both halves | 8e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIPK3]] | -0.50 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[ZSCAN30]] | -0.49 | -0.29 / -0.37 | both halves | 2e-04 |  |
| [[GANC]] | -0.48 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[C6orf120]] | -0.47 | -0.33 / -0.31 | both halves | 2e-04 |  |
| [[WAC-AS1]] | -0.46 | -0.18 / -0.33 | ⚠ not reproduced | 9e-04 |  |
| [[WASHC3]] | -0.45 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[BDNF-AS]] | -0.45 | -0.18 / -0.31 | ⚠ not reproduced | 1e-03 |  |
| [[ZNF532]] | -0.44 | -0.22 / -0.48 | both halves | 6e-04 |  |
| [[RBM48]] | -0.44 | -0.18 / -0.40 | ⚠ not reproduced | 0.001 |  |
| [[NTN4]] | -0.44 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[ZMPSTE24]] | -0.44 | -0.26 / -0.32 | both halves | 4e-04 |  |
| [[DECR1]] | -0.44 | -0.23 / -0.38 | both halves | 5e-04 |  |
| [[LEPROT]] | -0.43 | -0.24 / -0.42 | both halves | 4e-04 |  |
| [[ANXA2R-AS1]] | -0.43 | -0.21 / -0.28 | both halves | 6e-04 |  |
| [[PRPF18]] | -0.43 | -0.28 / -0.33 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAPN14]] | B | CAPN14 activity raises HSPA12A's level | lines that do not express CAPN14 (16) vs lines expressing it (34) | 1.78× lower at baseline in the lines without CAPN14 | 0.055 | ⚠ within organs, on part of the lines; also absent: CFAP46, EBF2, GAS7; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBE2Q2P2-1]] | C | HSPA12A activity raises UBE2Q2P2-1's level | lines that do not express HSPA12A (4) vs lines expressing it (46) | 1.30× lower at baseline in the lines without HSPA12A | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR3659HG, ENSG00000287400; maybe low, not absent; its own permutation p |
| [[UBE2Q2P2]] | C | HSPA12A activity raises UBE2Q2P2's level | lines that do not express HSPA12A (4) vs lines expressing it (46) | 1.23× lower at baseline in the lines without HSPA12A | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR3659HG, ENSG00000287400; maybe low, not absent |
| [[NRIP3]] | C | HSPA12A activity lowers NRIP3's level | lines that do not express HSPA12A (4) vs lines expressing it (46) | 1.53× higher at baseline in the lines without HSPA12A | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR3659HG, ENSG00000287400; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.432). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.2, 4.6); signed map (-20.8, 36.5). **Vector** length 92.4, 21.7% of its response variance represented; |z| ≥ 3 in 1,229 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +13.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.9 | +8.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +4.7 | +5.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.3 | +7.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +6.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.1 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +0.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.8 | +1.0 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.3 | -11.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.2 | -9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -7.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein family A (Hsp70) member 12A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.3 — chr10:116,671,192-116,850,251 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13874, KIAA0417 |
| Gene groups (HGNC) | Heat shock 70kDa proteins |
| Reactome | 4 pathways, smallest: Regulation of HSF1-mediated heat shock response; Cellular response to heat stress; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [O43301](https://www.uniprot.org/uniprotkb/O43301) (Heat shock 70 kDa protein 12A):

> Adapter protein for SORL1, but not SORT1. Delays SORL1 internalization and affects SORL1 subcellular localization.

**Summary**, from NCBI Gene [259217](https://www.ncbi.nlm.nih.gov/gene/259217):

> Predicted to enable ATP binding activity. Predicted to act upstream of or within several processes, including import into nucleus; liver development; and macrophage activation. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19022](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19022) · Entrez [259217](https://www.ncbi.nlm.nih.gov/gene/259217) · UniProt [O43301](https://www.uniprot.org/uniprotkb/O43301) · Ensembl [ENSG00000165868](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165868)

## Data

Gene col 9198: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9198); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9198, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9198]; `tensor/DDL_lfc|DDL_z.npy` [9198]; `embed/gene_vectors.npy` [9198]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9198 or target_col == 9198). Every well: [[HSPA12A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPA12A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
