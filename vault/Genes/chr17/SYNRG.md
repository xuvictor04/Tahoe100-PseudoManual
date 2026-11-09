---
symbol: "SYNRG"
type: "gene"
col: 15839
ensembl_id: "ENSG00000275066"
name: "synergin gamma"
location: "17q12"
module: 118
arm: "+"
pooled_cpm: 121.72
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# SYNRG

*synergin gamma* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.00× (z +33.7, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.420× (z -29.8, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.768× (z -12.9, q 1e-35, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (CFPAC-1 0.164×, A-427 0.131×, NCI-H23 0.156×, A498 0.254×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (CFPAC-1 0.186×, NCI-H460 0.244×, NCI-H2030 0.264×, A-172 0.227×, …; ⚠ toxic; transcription drop); [[Tucidinostat (drug)]] 5 µM in 3 lines (CFPAC-1 0.694×, BT-474 0.644×, HOP62 0.698×); [[Auranofin (drug)]] 5 µM in 1 line (MIA PaCa-2 0.352×); [[Tucidinostat (drug)]] 0.5 µM in 1 line (CFPAC-1 0.646×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARID4B]] (+0.71, fdr 7e-06), [[GTF2IRD2B]] (+0.69, fdr 7e-06), [[MORN2]] (+0.69, fdr 7e-06); moves opposite to [[GALNT10]] (-0.63, fdr 1e-04), [[SSX2IP]] (-0.62, fdr 1e-05), [[MCOLN2]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15839.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +33.7 | 0e+00 | 47/49 (SW1417, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +20.2 | 0e+00 | 39/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +17.4 | 0e+00 | 44/48 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +14.0 | 3e-42 | 40/50 (SW1417, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +13.4 | 9e-39 | 34/48 (SW1417, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.66×** | +9.1 | 1e-17 | 34/49 (NCI-H460, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.27×** | +8.2 | 2e-14 | 30/48 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.25×** | +7.6 | 2e-12 | 25/48 (BT-474, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +7.4 | 6e-12 | 25/48 (NCI-H1573, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.22×** | +6.9 | 2e-10 | 25/48 (HEC-1-A, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.21×** | +6.7 | 1e-09 | 26/48 (BT-474, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.20×** | +6.3 | 2e-08 | 22/48 (HEC-1-A, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.18× | +5.4 | 2e-06 | 18/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.17× | +5.3 | 4e-06 | 14/48 (LoVo, HT-29, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +5.2 | 8e-06 | 13/48 (BT-474, NCI-H1792, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.27×** | +4.3 | 7e-04 | 16/49 (HEC-1-A, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.12× | +4.0 | 0.002 | 14/48 (HOP62, SK-MEL-2, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.12× | +3.9 | 0.002 | 4/48 (SW48, SNU-1, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.004 | 8/50 (HEC-1-A, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠; shown: the 15 strongest. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15839.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (CFPAC-1 0.164×, A-427 0.131×, NCI-H23 0.156×, A498 0.254×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (CFPAC-1 0.186×, NCI-H460 0.244×, NCI-H2030 0.264×, A-172 0.227×, …; ⚠ toxic; transcription drop); [[Tucidinostat (drug)]] 5 µM in 3 lines (CFPAC-1 0.694×, BT-474 0.644×, HOP62 0.698×); [[Auranofin (drug)]] 5 µM in 1 line (MIA PaCa-2 0.352×); [[Tucidinostat (drug)]] 0.5 µM in 1 line (CFPAC-1 0.646×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.420×** | -29.8 | 0e+00 | 45/49 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.475×** | -24.7 | 0e+00 | 39/44 (CFPAC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.477×** | -23.6 | 0e+00 | 41/45 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.768×** | -12.9 | 1e-35 | 34/48 (CFPAC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.724×** | -10.7 | 9e-25 | 39/47 (CFPAC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.781×** | -8.5 | 1e-15 | 31/49 (CFPAC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.855× | -5.4 | 4e-06 | 17/48 (CFPAC-1, HepG2/C3A, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.855× | -5.4 | 4e-06 | 21/48 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | 0.862× | -5.1 | 2e-05 | 14/48 (SW 1271, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.875× | -4.6 | 2e-04 | 16/48 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.874× | -4.5 | 4e-04 | 17/48 (NCI-H1792, NCI-H2030, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.887× | -4.2 | 0.002 | 14/48 (RKO, CFPAC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.897× | -3.8 | 0.007 | 3/48 (Panc 03.27, C32, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.912× | -3.2 | 0.057 | 7/48 (SNU-423, CFPAC-1, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.914× | -3.1 | 0.072 | 5/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15839. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 131 | 6 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +18.9) | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -19.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 299 | 6 (2 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +13.3) | [[Tucidinostat (drug)]] 5 µM 0.644× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 576 | 2 | 6 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +20.7) | [[Dinaciclib (drug)]] 5 µM 0.164× (z -37.0) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 0.5 µM 0.646× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 136 | 3 | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.55× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.266× (z -23.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 83.3 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -27.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 113 | 5 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -17.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 148 | 4 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +16.7) | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -17.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 101 | 3 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +19.9) | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.352× (z -14.5) |
| [[NCI-H460 (line)]] | wt | 111 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -25.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 78.3 | 4 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.475× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 74.3 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +18.4) | [[Dinaciclib (drug)]] 0.5 µM 0.440× (z -10.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 52.9 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +19.8) | [[Dinaciclib (drug)]] 5 µM 0.533× (z -9.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 118 | 3 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.65× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -22.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 132 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -23.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 96.5 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -15.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 93.4 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -16.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 125 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +16.3) | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -18.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 117 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -16.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 235 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +18.3) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -23.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 101 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.156× (z -25.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 129 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +19.3) | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -19.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 102 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -15.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 165 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -16.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 121 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -17.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 96.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +22.9) | — |
| [[A-172 (line)]] | wt | 121 | 1 | 2 (2 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.57× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -23.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 84.3 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.433× (z -8.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 101 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -17.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 113 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -12.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 116 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -17.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 73.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.144× (z -23.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 73.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.6) | — |
| [[C32 (line)]] | wt | 84.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +13.7) | — |
| [[HCT15 (line)]] | alt | 137 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.399× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[XRK3F2 (drug)]] 0.5 µM 0.314× (z -8.8) |
| [[LoVo (line)]] | wt | 78.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -18.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 78.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 91.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -12.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 66.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.146× (z -14.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 92.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -12.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -12.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 76.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 75.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +12.8) | — |
| [[SHP-77 (line)]] | alt | 88.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +11.0) | — |
| [[SNU-1 (line)]] | wt | 75.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.7) | — |
| [[SW 1271 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -12.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 119 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15839), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID4B]] | +0.71 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[GTF2IRD2B]] | +0.69 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[MORN2]] | +0.69 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.68 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[KBTBD4]] | +0.68 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[NDUFC1]] | +0.67 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[ZFYVE1]] | +0.67 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[YJU2B]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[MICU1]] | +0.65 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[DCP1A]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[APPBP2]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[ZMYM5]] | +0.64 | +0.58 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNT10]] | -0.63 | -0.36 / -0.69 | both halves | 1e-04 |  |
| [[SSX2IP]] | -0.62 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[MCOLN2]] | -0.62 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[PPP5C]] | -0.62 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[G3BP1]] | -0.62 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[TCOF1]] | -0.62 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[MAT2A]] | -0.62 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[SLC19A1]] | -0.61 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[AGPS]] | -0.61 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[MAPKAPK3]] | -0.60 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[NAA15]] | -0.60 | -0.55 / -0.66 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.60 | -0.62 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SYNRG's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.790). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-26.7, -8.8); signed map (-4.4, -3.7). **Vector** length 121, 36.1% of its response variance represented; |z| ≥ 3 in 1,272 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +33.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.9 | +17.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +14.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.3 | +13.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +4.3 | +4.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.8 | +0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.6 | +2.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.6 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -12.2 | -12.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -9.4 | -8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.6 | -23.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | -7.9 | -5.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.5 | -10.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.6 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -5.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.8 | -3.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | synergin gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:37,514,807-37,609,472 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SYNG, MGC104959; previously AP1GBP1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMZ2](https://www.uniprot.org/uniprotkb/Q9UMZ2) (Synergin gamma):

> Plays a role in endocytosis and/or membrane trafficking at the trans-Golgi network (TGN). May act by linking the adapter protein complex AP-1 to other proteins (Probable). Component of clathrin-coated vesicles. Component of the aftiphilin/p200/gamma-synergin complex, which plays roles in AP1G1/AP-1-mediated protein trafficking including the trafficking of transferrin from early to recycling endosomes, and the membrane trafficking of furin and the lysosomal enzyme cathepsin D between the …

**Summary**, from NCBI Gene [11276](https://www.ncbi.nlm.nih.gov/gene/11276):

> This gene encodes a protein that interacts with the gamma subunit of AP1 clathrin-adaptor complex. The AP1 complex is located at the trans-Golgi network and associates specific proteins with clathrin-coated vesicles. This encoded protein may act to connect the AP1 complex to other proteins. Alternatively spliced transcript variants that encode different isoforms have been described for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:557](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:557) · Entrez [11276](https://www.ncbi.nlm.nih.gov/gene/11276) · UniProt [Q9UMZ2](https://www.uniprot.org/uniprotkb/Q9UMZ2) · Ensembl [ENSG00000275066](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000275066)

## Data

Gene col 15839: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15839); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15839, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15839]; `tensor/DDL_lfc|DDL_z.npy` [15839]; `embed/gene_vectors.npy` [15839]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15839 or target_col == 15839). Every well: [[SYNRG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYNRG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
