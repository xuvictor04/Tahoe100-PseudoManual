---
symbol: "FKBP1A"
type: "gene"
col: 1546
ensembl_id: "ENSG00000088832"
name: "FKBP prolyl isomerase 1A"
location: "20p13"
module: 29
arm: "+"
pooled_cpm: 74.88
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# FKBP1A

*FKBP prolyl isomerase 1A* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.49× (z +22.9, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.72× (z +9.9, q 6e-21, up in 43 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (NCI-H460 4.85×, LoVo 5.51×, PANC-1 4.76×, NCI-H23 5.19×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 5.23×, NCI-H460 4.02×, SW480 3.26×, LS 180 4.06×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Auranofin (drug)]] 5 µM in 4 lines (SW480 2.68×, C32 3.69×, SK-MEL-2 2.73×, MIA PaCa-2 2.54×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.656× (z -11.0, q 3e-25, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM30A]] (+0.69, fdr 7e-06), [[ARF3]] (+0.67, fdr 7e-06), [[VMA21]] (+0.67, fdr 7e-06); moves opposite to [[SNHG32]] (-0.69, fdr 7e-06), [[CCDC174]] (-0.69, fdr 7e-06), [[NKAP]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LDOC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 18 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1546.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 10 lines (NCI-H460 4.85×, LoVo 5.51×, PANC-1 4.76×, NCI-H23 5.19×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (LoVo 5.23×, NCI-H460 4.02×, SW480 3.26×, LS 180 4.06×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Auranofin (drug)]] 5 µM in 4 lines (SW480 2.68×, C32 3.69×, SK-MEL-2 2.73×, MIA PaCa-2 2.54×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.49×** | +22.9 | 0e+00 | 49/49 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.17×** | +20.3 | 0e+00 | 43/43 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.97×** | +18.4 | 0e+00 | 43/45 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +9.9 | 6e-21 | 43/48 (SW480, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.41×** | +6.3 | 4e-08 | 35/48 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.37×** | +5.7 | 9e-07 | 31/48 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.37×** | +5.7 | 9e-07 | 33/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.36×** | +5.3 | 6e-06 | 28/48 (LOX-IMVI, SNU-423, …) | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.95×** | +5.3 | 8e-06 | 21/36 (NCI-H2347, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.33×** | +5.0 | 3e-05 | 28/50 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.31×** | +4.9 | 5e-05 | 29/48 (HepG2/C3A, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.30×** | +4.7 | 1e-04 | 27/48 (BT-474, SW480, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.18× | +4.3 | 8e-04 | 22/49 (A-427, NCI-H2347, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.26×** | +4.2 | 0.001 | 24/48 (CFPAC-1, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change | **1.25×** | +4.1 | 0.001 | 25/48 (BT-474, PANC-1, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.028 | 14/48 (A-427, BT-474, …) | top dose only |  |
| [[Ritonavir (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.030 | 17/48 (SHP-77, NCI-H460, …) | inconsistent across doses |  |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.040 | 14/48 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1546.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.656×** | -11.0 | 3e-25 | 36/47 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.680×** | -6.7 | 6e-09 | 36/48 (H4, hTERT-HPNE, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.547×** | -4.8 | 3e-04 | 32/49 (SW480, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.786×** | -4.4 | 0.001 | 27/48 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.752×** | -4.4 | 0.001 | 31/50 (NCI-H596, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.785×** | -4.3 | 0.002 | 22/47 (CHP-212, RPMI-7951, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.815×** | -4.2 | 0.002 | 21/48 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.610×** | -3.9 | 0.006 | 23/45 (H4, HOP62, …) | all doses, flat | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.812×** | -3.8 | 0.007 | 24/48 (HOP62, A-172, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.864× | -3.8 | 0.007 | 15/48 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **0.806×** | -3.8 | 0.009 | 21/49 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.834× | -3.3 | 0.039 | 18/48 (H4, NCI-H2030, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.831×** | -3.2 | 0.054 | 17/48 (SK-MEL-2, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -3.1 | 0.071 | 22/47 (NCI-H460, H4, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.891× | -3.0 | 0.093 | 10/49 (NCI-H460, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1546. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 89.9 | 5 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.68× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 57.4 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.54× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 72.6 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -13.3) |
| [[A-427 (line)]] | wt | 56.2 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +11.1) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[A498 (line)]] | wt | 57.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A549 (line)]] | wt | 64.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[C32 (line)]] | wt | 62.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.69× (z +10.4) | — |
| [[KATO III (line)]] | alt | 80.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -10.4) |
| [[LoVo (line)]] | wt | 43.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.527× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 60.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.20× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 66.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.19× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 82.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[RPMI-7951 (line)]] | alt | 261 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -9.9) |
| [[SW 900 (line)]] | alt | 90.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -9.9) |
| [[C-33 A (line)]] | alt | 52.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.96× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[CFPAC-1 (line)]] | alt | 89.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[H4 (line)]] | wt | 109 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.29× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.300× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.478× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 57.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HOP62 (line)]] | alt | 86.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HS-578T (line)]] | alt | 98.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HT-29 (line)]] | alt | 58.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[J82 (line)]] | alt | 97.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -10.6) |
| [[LS 180 (line)]] | wt | 57.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1573 (line)]] | alt | 31.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 40.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.10× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[Panc 03.27 (line)]] | alt | 52.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[PANC-1 (line)]] | alt | 84.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 96.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.73× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 90.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW1417 (line)]] | alt | 44.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.20× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 94.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[AsPC-1 (line)]] | alt | 73.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[RKO (line)]] | wt | 92.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -18.0) |
| [[SHP-77 (line)]] | alt | 85.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW48 (line)]] | wt | 54.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.61× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[BT-474 (line)]] | alt | 50.9 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.05× (z +11.9) ⚠ cell-cycle shift, explains ~82% of this change | — |
| [[COLO 205 (line)]] | alt | 67.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HCT15 (line)]] | alt | 51.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.81× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[Hs 766T (line)]] | wt | 133 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 99.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2030 (line)]] | alt | 42.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H596 (line)]] | alt | 68.9 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.137× (z -12.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW 1088 (line)]] | alt | 132 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0773× (z -10.3) |
| [[AN3 CA (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 166 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 89.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1546), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM30A]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[ARF3]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[VMA21]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[COLGALT1]] | +0.65 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[TMED7]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[F2R]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[TGOLN2]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[GNG12]] | +0.64 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[ITM2C]] | +0.64 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[AGPAT1]] | +0.64 | +0.63 / +0.52 | both halves | 1e-05 | same gene group |
| [[MDH2]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[MMGT1]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG32]] | -0.69 | -0.70 / -0.64 | both halves | 7e-06 |  |
| [[CCDC174]] | -0.69 | -0.65 / -0.64 | both halves | 7e-06 |  |
| [[NKAP]] | -0.69 | -0.66 / -0.68 | both halves | 7e-06 |  |
| [[ATF4]] | -0.69 | -0.65 / -0.66 | both halves | 7e-06 |  |
| [[UPF3B]] | -0.69 | -0.68 / -0.68 | both halves | 7e-06 |  |
| [[RBMX2]] | -0.68 | -0.68 / -0.71 | both halves | 7e-06 |  |
| [[PPIG]] | -0.67 | -0.66 / -0.58 | both halves | 8e-06 | pathway: SARS-CoV-1 Infection |
| [[SMIM26]] ⚠ | -0.67 | -0.66 / -0.71 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[WASHC1]] | -0.67 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[ANKRD49]] | -0.66 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[AK6]] | -0.66 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[FNBP4]] | -0.66 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[EPB41L4A-AS1]] | -0.65 | -0.66 / -0.66 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LDOC1]] | B | LDOC1 activity raises FKBP1A's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 1.16× lower at baseline in the lines without LDOC1 | 0.087 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91 |
| [[ARHGDIB]] | B | ARHGDIB activity raises FKBP1A's level | lines that do not express ARHGDIB (23) vs lines expressing it (27) | 1.22× lower at baseline in the lines without ARHGDIB | 0.090 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[TRAPPC2B]] | B | TRAPPC2B activity raises FKBP1A's level | lines that do not express TRAPPC2B (7) vs lines expressing it (43) | 1.51× lower at baseline in the lines without TRAPPC2B | 0.097 | ⚠ within organs, on part of the lines; also absent: ZNF547, ZNF548, ZNF530 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-37.0, -13.0); signed map (-26.0, -39.8). **Vector** length 116, 35.3% of its response variance represented; |z| ≥ 3 in 1,054 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +18.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +5.0 | +22.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +4.9 | +20.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +9.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.8 | +3.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.8 | -11.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | -7.3 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.8 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.7 | -3.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.5 | -4.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.5 | -2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | FKBP prolyl isomerase 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:1,368,977-1,393,164 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FKBP-12, FKBP12, PKC12, PPIASE, FKBP12C; previously FKBP1 |
| Gene groups (HGNC) | FKBP prolyl isomerase family; MicroRNA protein coding host genes |
| Hallmark sets | TGF_BETA_SIGNALING |
| Reactome | 20 pathways, smallest: TGFBR1 LBD Mutants in Cancer; Loss of Function of TGFBR1 in Cancer; Signaling by TGF-beta Receptor Complex in Cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [P62942](https://www.uniprot.org/uniprotkb/P62942) (Peptidyl-prolyl cis-trans isomerase FKBP1A):

> Keeps in an inactive conformation TGFBR1, the TGF-beta type I serine/threonine kinase receptor, preventing TGF-beta receptor activation in absence of ligand. Recruits SMAD7 to ACVR1B which prevents the association of SMAD2 and SMAD3 with the activin receptor complex, thereby blocking the activin signal. May modulate the RYR1 calcium channel activity. PPIases accelerate the folding of proteins. It catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides.

**Summary**, from NCBI Gene [2280](https://www.ncbi.nlm.nih.gov/gene/2280):

> The protein encoded by this gene is a member of the immunophilin protein family, which play a role in immunoregulation and basic cellular processes involving protein folding and trafficking. The protein is a cis-trans prolyl isomerase that binds the immunosuppressants FK506 and rapamycin. It interacts with several intracellular signal transduction proteins including type I TGF-beta receptor. It also interacts with multiple intracellular calcium release channels, and coordinates multi-protein …

**Accessions** — [HGNC:3711](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3711) · Entrez [2280](https://www.ncbi.nlm.nih.gov/gene/2280) · UniProt [P62942](https://www.uniprot.org/uniprotkb/P62942) · Ensembl [ENSG00000088832](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088832)

## Data

Gene col 1546: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1546); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1546, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1546]; `tensor/DDL_lfc|DDL_z.npy` [1546]; `embed/gene_vectors.npy` [1546]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1546 or target_col == 1546). Every well: [[FKBP1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FKBP1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
