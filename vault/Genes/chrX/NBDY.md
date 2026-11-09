---
symbol: "NBDY"
type: "gene"
col: 12843
ensembl_id: "ENSG00000204272"
name: "negative regulator of P-body association"
location: "Xp11.21"
module: 17
arm: "+"
pooled_cpm: 55.52
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# NBDY

*negative regulator of P-body association* — Xp11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.08× (z +35.4, q 0e+00, up in 42 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Osimertinib (mesylate) (drug)]] 5 µM: 1.30× (z +6.0, q 2e-07, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.444× (z -25.9, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KPNA5]] (+0.64, fdr 4e-05), [[TEN1]] (+0.56, fdr 4e-05), [[NEPRO]] (+0.55, fdr 1e-05); moves opposite to [[ZBTB11]] (-0.56, fdr 2e-04), [[ENDOG]] (-0.54, fdr 4e-05), [[CKS2]] (-0.52, fdr 1e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12843.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.08×** | +35.4 | 0e+00 | 42/42 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.64×** | +34.8 | 0e+00 | 48/48 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.62×** | +26.9 | 0e+00 | 38/44 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.31×** | +8.7 | 3e-16 | 30/47 (LoVo, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.41×** | +7.8 | 1e-12 | 34/47 (H4, PANC-1, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.30×** | +6.0 | 2e-07 | 27/47 (C-33 A, BT-474, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.26×** | +5.3 | 9e-06 | 30/48 (C-33 A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.27×** | +5.1 | 2e-05 | 26/47 (C32, HT-29, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +4.9 | 6e-05 | 25/47 (HT-29, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.6 | 2e-04 | 22/47 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.20×** | +4.2 | 0.001 | 20/47 (LS 180, LoVo, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.013 | 15/47 (NCI-H460, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.075 | 10/47 (RPMI-7951, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.15× | +3.1 | 0.091 | 16/46 (CFPAC-1, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12843.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.444×** | -25.9 | 0e+00 | 45/47 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.433×** | -18.2 | 0e+00 | 40/47 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.534×** | -14.2 | 3e-43 | 42/47 (NCI-H23, H4, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.547×** | -13.1 | 6e-37 | 43/49 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.588×** | -12.0 | 4e-31 | 37/47 (C-33 A, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.619×** | -10.8 | 2e-25 | 38/47 (HS-578T, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.641×** | -10.0 | 8e-22 | 30/47 (SW480, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.737×** | -9.7 | 2e-20 | 34/47 (SNU-423, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.738×** | -9.7 | 2e-20 | 29/47 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.691×** | -8.3 | 4e-15 | 34/47 (NCI-H23, H4, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.712×** | -7.4 | 1e-11 | 29/46 (A-427, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.794×** | -5.2 | 1e-05 | 20/47 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.818×** | -4.5 | 3e-04 | 20/47 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.688×** | -4.4 | 4e-04 | 23/48 (A498, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.703×** | -4.2 | 0.001 | 23/47 (RKO, COLO 205, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.907× | -3.1 | 0.066 | 2/47 (HCT15, SW48) | top dose only |  |
| [[Lucanthone (drug)]] 5 µM |  | 0.868× | -3.0 | 0.069 | 11/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12843. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 92.2 | 3 (3 ⚠) | 6 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 12.0× (z +22.3) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -15.9) |
| [[SK-MEL-2 (line)]] | alt | 57.4 | 3 (3 ⚠) | 5 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 10.3× (z +22.8) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -14.0) |
| [[HS-578T (line)]] | alt | 48.6 | 3 (3 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 9.15× (z +20.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 42.0 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.27× (z +18.1) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -18.7) |
| [[NCI-H23 (line)]] | alt | 96.1 | 1 (1 ⚠) | 6 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +13.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -22.2) |
| [[NCI-H460 (line)]] | wt | 91.1 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +22.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -28.1) |
| [[PANC-1 (line)]] | alt | 61.2 | 3 (3 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.51× (z +22.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -16.0) |
| [[C-33 A (line)]] | alt | 100 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +14.7) ⚠ toxic; transcription drop | [[Auranofin (drug)]] 5 µM 0.263× (z -15.0) |
| [[HOP62 (line)]] | alt | 61.1 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 19.0× (z +32.1) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 107 | 3 (3 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.76× (z +17.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -21.4) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -14.4) |
| [[RPMI-7951 (line)]] | alt | 87.2 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 12.2× (z +25.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -12.9) |
| [[SNU-423 (line)]] | alt | 54.2 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.57× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -13.8) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -13.3) |
| [[SW1417 (line)]] | alt | 66.1 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 8.29× (z +23.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -16.5) |
| [[SW480 (line)]] | alt | 41.2 | 2 (2 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.45× (z +14.0) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -13.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -12.0) |
| [[A-172 (line)]] | wt | 44.7 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 11.1× (z +24.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 62.6 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.33× (z +17.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -9.3) |
| [[KATO III (line)]] | alt | 38.9 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.18× (z +15.3) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.322× (z -10.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 58.8 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 67.3 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.65× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -15.5) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 50.0 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.28× (z +18.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -12.2) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 74.1 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.65× (z +17.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -16.2) |
| [[Panc 03.27 (line)]] | alt | 66.7 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 10.5× (z +24.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -16.2) |
| [[RKO (line)]] | wt | 77.8 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +12.4) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -13.9) |
| [[SHP-77 (line)]] | alt | 93.4 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 9.45× (z +23.1) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.324× (z -11.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -11.9) |
| [[SW 900 (line)]] | alt | 40.4 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 12.9× (z +21.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -9.5) |
| [[A-427 (line)]] | wt | 70.7 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +12.4) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -14.1) |
| [[A498 (line)]] | wt | 21.9 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +14.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -14.3) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A549 (line)]] | wt | 74.0 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 14.3× (z +28.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -16.6) |
| [[C32 (line)]] | wt | 41.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 9.09× (z +18.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -14.3) |
| [[HEC-1-A (line)]] | alt | 56.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +12.7) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 56.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.30× (z +13.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -9.7) |
| [[LoVo (line)]] | wt | 26.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.21× (z +13.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -8.8) |
| [[SW48 (line)]] | wt | 51.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +9.6) ⚠ toxic; transcription drop | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 29.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.30× (z +13.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 32.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.82× (z +12.8) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 32.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 17.9× (z +21.0) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 71.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.57× (z +9.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -10.5) |
| [[COLO 205 (line)]] | alt | 38.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +12.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -9.1) |
| [[Hs 766T (line)]] | wt | 30.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.94× (z +13.5) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 40.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 12.6× (z +16.2) ⚠ toxic; transcription drop | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -9.2) |
| [[SW 1271 (line)]] | alt | 55.8 | 0 | 2 | — | [[Resveratrol (drug)]] 0.05 µM 0.0748× (z -9.4) |
| [[AN3 CA (line)]] | alt | 103 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -10.4) |
| [[LS 180 (line)]] | wt | 28.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -8.9) |
| [[BT-474 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12843), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA5]] | +0.64 | +0.42 / +0.70 | both halves | 4e-05 |  |
| [[TEN1]] | +0.56 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[NEPRO]] | +0.55 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[DYNC2LI1]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ZDHHC17]] | +0.54 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[RPAP3]] | +0.54 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[BBS5]] | +0.53 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[TOM1L1]] | +0.52 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[APOOL]] | +0.51 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[CTC1]] | +0.51 | +0.28 / +0.55 | both halves | 3e-04 |  |
| [[IRAK1BP1]] | +0.51 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[GNPDA2]] | +0.50 | +0.51 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB11]] | -0.56 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[ENDOG]] | -0.54 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[CKS2]] | -0.52 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[TMEM187]] | -0.51 | -0.26 / -0.51 | both halves | 4e-04 |  |
| [[SNTB2]] | -0.49 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[LEMD3]] | -0.48 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[ANKMY1]] | -0.48 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[RMI2]] | -0.48 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[SLC10A3]] | -0.48 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[CFL1]] | -0.48 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[FEN1]] | -0.47 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[FANCM]] | -0.46 | -0.29 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NBDY's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.470). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-22.9, 1.1); signed map (-21.6, -18.3). **Vector** length 116, 32.6% of its response variance represented; |z| ≥ 3 in 1,136 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +9.4 | +8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.1 | +4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | +7.9 | +5.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +7.7 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.7 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.4 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.0 | +2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.6 | +6.0 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -9.6 | -18.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.4 | -25.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -8.7 | -13.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.2 | -12.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.8 | -9.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | -1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Thymol (drug)]] 5 µM |  | -2.1 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | negative regulator of P-body association |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.21 — chrX:56,729,241-56,819,179 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NoBody; previously LINC01420 |
| Matched by | ensembl_id |

**Function**, from UniProt [A0A0U1RRE5](https://www.uniprot.org/uniprotkb/A0A0U1RRE5) (Negative regulator of P-body association):

> Promotes dispersal of P-body components and is likely to play a role in the mRNA decapping process.

**Summary**, from NCBI Gene [550643](https://www.ncbi.nlm.nih.gov/gene/550643):

> Involved in negative regulation of cytoplasmic mRNA processing body assembly and nuclear-transcribed mRNA catabolic process. Located in P-body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:50713](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50713) · Entrez [550643](https://www.ncbi.nlm.nih.gov/gene/550643) · UniProt [A0A0U1RRE5](https://www.uniprot.org/uniprotkb/A0A0U1RRE5) · Ensembl [ENSG00000204272](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204272)

## Data

Gene col 12843: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12843); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12843, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12843]; `tensor/DDL_lfc|DDL_z.npy` [12843]; `embed/gene_vectors.npy` [12843]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12843 or target_col == 12843). Every well: [[NBDY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBDY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
