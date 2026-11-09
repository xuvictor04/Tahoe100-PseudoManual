---
symbol: "WWC2"
type: "gene"
col: 7557
ensembl_id: "ENSG00000151718"
name: "WW and C2 domain containing 2"
location: "4q35.1"
module: 143
arm: "+"
pooled_cpm: 180.88
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 5
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# WWC2

*WW and C2 domain containing 2* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.81× (z +16.0, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.631× (z -11.9, q 1e-29, down in 41 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.833× (z -4.9, q 1e-04, down in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 6 lines (HepG2/C3A 0.258×, LOX-IMVI 0.417×, CFPAC-1 0.451×, HCT15 0.295×, …; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A549 0.535×, J82 0.589×, NCI-H1792 0.517×, PANC-1 0.667×; ⚠ cell-cycle shift, explains ~4% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.255×, BT-474 0.355×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.594×, HCT15 0.531×); [[Proglumide (drug)]] 0.05 µM in 1 line (SW 1088 0.0846×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEAD1]] (+0.60, fdr 1e-05), [[PICALM]] (+0.59, fdr 1e-05), [[WWC3]] (+0.56, fdr 3e-05); moves opposite to [[PARL]] (-0.57, fdr 1e-05), [[MED6]] (-0.55, fdr 2e-05), [[CWF19L1]] (-0.54, fdr 1e-05).
> It is in [[Module 143]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7557.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.81×** | +16.0 | 0e+00 | 44/47 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +14.6 | 1e-45 | 33/47 (NCI-H2347, LS 180, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +10.8 | 7e-25 | 40/47 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +10.7 | 2e-24 | 42/47 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +10.0 | 1e-21 | 34/47 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +7.9 | 2e-13 | 34/47 (LS 180, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +6.5 | 6e-09 | 31/46 (SNU-423, A498, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.23×** | +5.5 | 2e-06 | 27/46 (BT-474, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.23×** | +5.4 | 3e-06 | 23/47 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.20×** | +4.9 | 5e-05 | 22/46 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.19× | +4.8 | 1e-04 | 22/47 (SHP-77, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.19× | +4.6 | 2e-04 | 22/47 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.19× | +4.5 | 3e-04 | 20/46 (SHP-77, LS 180, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.40×** | +4.4 | 4e-04 | 25/48 (LS 180, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.16× | +4.0 | 0.003 | 19/47 (BT-474, LoVo, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.9 | 0.003 | 10/48 (SHP-77, A-172, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.13× | +3.4 | 0.021 | 14/47 (HS-578T, NCI-H460, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.12× | +3.0 | 0.064 | 13/46 (HEC-1-A, hTERT-HPNE, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.12× | +2.9 | 0.088 | 7/47 (HEC-1-A, A-172, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7557.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 6 lines (HepG2/C3A 0.258×, LOX-IMVI 0.417×, CFPAC-1 0.451×, HCT15 0.295×, …; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A549 0.535×, J82 0.589×, NCI-H1792 0.517×, PANC-1 0.667×; ⚠ cell-cycle shift, explains ~4% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (RKO 0.255×, BT-474 0.355×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 0.594×, HCT15 0.531×); [[Proglumide (drug)]] 0.05 µM in 1 line (SW 1088 0.0846×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.631×** | -11.9 | 1e-29 | 41/46 (HepG2/C3A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.750×** | -7.1 | 3e-10 | 29/44 (RKO, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.850× | -6.2 | 1e-07 | 17/47 (J82, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 0.833× | -4.9 | 1e-04 | 23/47 (J82, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.845× | -4.5 | 7e-04 | 23/47 (PANC-1, SW 1271, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.795×** | -4.4 | 0.001 | 28/47 (RKO, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.851× | -4.3 | 0.001 | 23/48 (A-427, SW 900, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.857× | -4.1 | 0.003 | 22/47 (CFPAC-1, J82, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.810×** | -4.0 | 0.004 | 20/47 (HEC-1-A, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.857× | -4.0 | 0.004 | 20/43 (NCI-H23, HepG2/C3A, …) | all doses, flat | composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.871× | -3.7 | 0.011 | 13/47 (SK-MEL-2, H4, …) | all doses, stronger at high dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.771×** | -3.4 | 0.028 | 18/44 (Hs 766T, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.914× | -3.4 | 0.029 | 7/47 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.886× | -3.2 | 0.046 | 13/47 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.918× | -3.2 | 0.046 | 6/47 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.895× | -3.0 | 0.097 | 10/47 (BT-474, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7557. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 139 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +20.2) | — |
| [[BT-474 (line)]] | alt | 141 | 7 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.92× (z +20.8) | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 79.3 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +21.1) | — |
| [[SW1417 (line)]] | alt | 103 | 6 (2 ⚠) | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.80× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.499× (z -8.7) ⚠ toxic |
| [[SW480 (line)]] | alt | 226 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +16.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.573× (z -10.0) ⚠ toxic |
| [[LoVo (line)]] | wt | 202 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +18.8) | [[Dinaciclib (drug)]] 0.05 µM 0.563× (z -9.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 438 | 0 | 5 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.258× (z -16.8) ⚠ toxic |
| [[KATO III (line)]] | alt | 117 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +15.9) | — |
| [[PANC-1 (line)]] | alt | 270 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +18.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.557× (z -10.9) ⚠ toxic |
| [[C-33 A (line)]] | alt | 312 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.427× (z -10.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 190 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.482× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 156 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -14.5) ⚠ cell-cycle shift, explains ~4% of this change |
| [[CFPAC-1 (line)]] | alt | 229 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.451× (z -12.1) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 92.8 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +11.8) | — |
| [[H4 (line)]] | wt | 169 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.7) | — |
| [[HCT15 (line)]] | alt | 458 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.295× (z -12.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.531× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 167 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +16.0) | [[Selinexor (drug)]] 5 µM 0.657× (z -9.8) ⚠ cell-cycle shift, explains ~19% of this change |
| [[HT-29 (line)]] | alt | 72.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +14.3) | — |
| [[J82 (line)]] | alt | 293 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.551× (z -13.8) ⚠ cell-cycle shift, explains ~19% of this change |
| [[NCI-H1792 (line)]] | alt | 252 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -11.8) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.594× (z -9.3) |
| [[SNU-1 (line)]] | wt | 123 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.3) | [[Selinexor (drug)]] 5 µM 0.560× (z -8.7) ⚠ cell-cycle shift, explains ~19% of this change |
| [[LOX-IMVI (line)]] | wt | 264 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.417× (z -12.4) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 161 | 1 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.92× (z +9.3) ⚠ cell-cycle shift, explains ~20% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.382× (z -11.1) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 113 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.366× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 263 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -17.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 78.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +15.6) | — |
| [[SW 900 (line)]] | alt | 162 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.441× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 176 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +18.1) | — |
| [[AsPC-1 (line)]] | alt | 160 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +13.5) | — |
| [[HOP62 (line)]] | alt | 200 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.506× (z -9.0) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 92.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.476× (z -8.7) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 156 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.425× (z -10.6) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 236 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.483× (z -11.0) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 167 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.493× (z -10.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 243 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.491× (z -9.0) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 104 | 0 | 1 | — | [[Proglumide (drug)]] 0.05 µM 0.0846× (z -9.8) |
| [[A-172 (line)]] | wt | 188 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 315 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 78.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 179 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 375 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7557), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEAD1]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[PICALM]] | +0.59 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[WWC3]] | +0.56 | +0.43 / +0.60 | both halves | 3e-05 | same gene group |
| [[SCHIP1]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[FRYL]] | +0.56 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[SLC4A7]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[PKP4]] | +0.54 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[CRIM1]] | +0.54 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[ROCK2]] | +0.53 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[VPS13A]] | +0.52 | +0.38 / +0.57 | both halves | 7e-05 |  |
| [[RBFOX2]] | +0.52 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[CTNNAL1]] | +0.51 | +0.43 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARL]] | -0.57 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[MED6]] | -0.55 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[CWF19L1]] | -0.54 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[METTL22]] | -0.53 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[SCNM1]] | -0.52 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[NGDN]] | -0.52 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[UBOX5]] | -0.51 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[SNIP1]] | -0.51 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[BRAP]] | -0.50 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ZNF230]] | -0.50 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[SMPDL3A]] | -0.50 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[TFIP11]] | -0.49 | -0.53 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.472). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.2, 15.0); signed map (-14.7, 30.8). **Vector** length 111, 31.9% of its response variance represented; |z| ≥ 3 in 1,426 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.6 | +10.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.5 | +16.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.4 | +4.5 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +4.3 | +4.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +4.0 | +10.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.9 | +3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +4.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.8 | -11.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -7.1 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.3 | -4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -4.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -3.3 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | +1.9 |

## What is on record

|  |  |
|---|---|
| Name | WW and C2 domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:183,099,257-183,320,777 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BOMB, FLJ22029 |
| Gene groups (HGNC) | WWC family; C2 and WW domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6AWC2](https://www.uniprot.org/uniprotkb/Q6AWC2) (Protein WWC2):

> Regulator of the Hippo signaling pathway, also known as the Salvador-Warts-Hippo (SWH) pathway. Enhances phosphorylation of LATS1 and YAP1 and negatively regulates cell proliferation and organ growth due to a suppression of the transcriptional activity of YAP1, the major effector of the Hippo pathway.

**Summary**, from NCBI Gene [80014](https://www.ncbi.nlm.nih.gov/gene/80014):

> This gene encodes a member of the WW-and-C2-domain-containing family of proteins. Members of this family have two N-terminal WW domains that mediate binding to target proteins harboring L/PPxY motifs, an internal C2 domain for membrane association, and C-terminal alpha protein kinase C binding sites and class III PDZ domain-interaction motifs. Proteins of this family are able to form homo- and heterodimers and to modulate hippo pathway signaling. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:24148](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24148) · Entrez [80014](https://www.ncbi.nlm.nih.gov/gene/80014) · UniProt [Q6AWC2](https://www.uniprot.org/uniprotkb/Q6AWC2) · Ensembl [ENSG00000151718](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151718)

## Data

Gene col 7557: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7557); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7557, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7557]; `tensor/DDL_lfc|DDL_z.npy` [7557]; `embed/gene_vectors.npy` [7557]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7557 or target_col == 7557). Every well: [[WWC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WWC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
