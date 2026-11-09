---
symbol: "IDH3A"
type: "gene"
col: 9300
ensembl_id: "ENSG00000166411"
name: "isocitrate dehydrogenase (NAD(+)) 3 catalytic subunit alpha"
location: "15q25.1"
module: 20
arm: "+"
pooled_cpm: 25.12
n_lines_expressing: 50
n_dd_up: 43
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# IDH3A

*isocitrate dehydrogenase (NAD(+)) 3 catalytic subunit alpha* — 15q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (23 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.05× (z +30.7, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 4.56× (z +28.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM: 0.800× (z -4.1, q 0.013, down in 12 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.398×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VMA21]] (+0.65, fdr 7e-06), [[SIGMAR1]] (+0.62, fdr 1e-05), [[EFR3A]] (+0.61, fdr 8e-06); moves opposite to [[IGBP1]] (-0.66, fdr 7e-06), [[KLC4]] (-0.63, fdr 1e-05), [[AKAP17A]] (-0.63, fdr 2e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 25 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9300.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **5.05×** | +30.7 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.56×** | +28.8 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **4.17×** | +27.1 | 0e+00 | 47/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.63×** | +17.6 | 0e+00 | 35/37 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +17.6 | 0e+00 | 38/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.40×** | +16.6 | 0e+00 | 40/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.29×** | +15.7 | 0e+00 | 40/47 (HT-29, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.68×** | +13.9 | 5e-42 | 40/47 (A498, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.95×** | +11.7 | 6e-30 | 34/39 (A-172, C32, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.89×** | +11.6 | 2e-29 | 39/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.81×** | +11.2 | 1e-27 | 37/48 (SW480, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +11.2 | 3e-27 | 40/48 (HT-29, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.76×** | +10.7 | 5e-25 | 39/47 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.73×** | +10.4 | 1e-23 | 39/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.74×** | +10.1 | 2e-22 | 33/47 (LoVo, Hs 766T, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +9.7 | 7e-21 | 37/47 (A-172, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +8.1 | 2e-14 | 31/48 (HEC-1-A, C32, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.06×** | +7.2 | 2e-11 | 32/48 (PANC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.8 | 3e-05 | 17/47 (C32, NCI-H23, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.61×** | +4.7 | 5e-05 | 16/48 (NCI-H460, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.57×** | +4.5 | 2e-04 | 11/47 (NCI-H460, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.4 | 2e-04 | 16/48 (SW 900, SW480, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.25×** | +4.2 | 4e-04 | 18/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +4.1 | 6e-04 | 14/47 (SK-MEL-2, HOP62, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9300.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.398×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **0.800×** | -4.1 | 0.013 | 12/47 (AsPC-1, NCI-H2347, …) | top dose only | plate-row cell shift |
| [[Meloxicam (drug)]] 0.5 µM |  | **0.808×** | -4.1 | 0.013 | 16/47 (hTERT-HPNE, C-33 A, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.886× | -3.3 | 0.18 | 5/48 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.848× | -3.2 | 0.22 | 9/47 (SW48, SK-MEL-2, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | 0.895× | -3.0 | 0.24 | 14/48 (KATO III, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9300. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 35.3 | 12 (8 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.44× (z +17.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.07× (z +16.3) | — |
| [[A-172 (line)]] | wt | 18.2 | 6 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.75× (z +12.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.02× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 18.6 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.09× (z +13.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.47× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 16.8 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +12.7) | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 6 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.66× (z +11.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 6.89× (z +10.4) | — |
| [[A498 (line)]] | wt | 25.0 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.30× (z +13.8) | — |
| [[A549 (line)]] | wt | 31.2 | 5 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 6.16× (z +14.3) | — |
| [[CFPAC-1 (line)]] | alt | 17.9 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.63× (z +12.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.20× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 21.5 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.23× (z +13.5) | — |
| [[HT-29 (line)]] | alt | 28.2 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.96× (z +14.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.43× (z +14.1) | — |
| [[NCI-H460 (line)]] | wt | 25.2 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.54× (z +15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.57× (z +11.9) | — |
| [[AsPC-1 (line)]] | alt | 12.1 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.33× (z +10.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 6.85× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 26.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 18.4 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.90× (z +11.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 6.58× (z +11.1) | — |
| [[KATO III (line)]] | alt | 35.4 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.46× (z +14.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.17× (z +13.9) | — |
| [[LoVo (line)]] | wt | 36.1 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.99× (z +14.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.96× (z +12.8) | — |
| [[LOX-IMVI (line)]] | wt | 19.5 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 6.42× (z +12.8) | — |
| [[NCI-H2030 (line)]] | alt | 29.5 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.64× (z +12.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.62× (z +12.0) | — |
| [[NCI-H23 (line)]] | alt | 20.9 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.38× (z +11.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.68× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 25.7 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.56× (z +12.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.48× (z +12.0) | — |
| [[PANC-1 (line)]] | alt | 25.6 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.38× (z +15.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.26× (z +15.2) | — |
| [[SNU-423 (line)]] | alt | 13.1 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.87× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 38.3 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.28× (z +13.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.91× (z +12.4) | — |
| [[HS-578T (line)]] | alt | 15.9 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.39× (z +10.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.54× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 14.3 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.58× (z +10.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 7.25× (z +9.2) | — |
| [[J82 (line)]] | alt | 26.3 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.81× (z +9.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.45× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 21.1 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.88× (z +11.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.45× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 18.4 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +10.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.59× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 26.0 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.82× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 20.0 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.32× (z +10.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 6.61× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 22.2 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.42× (z +10.9) | — |
| [[SW 900 (line)]] | alt | 14.7 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.74× (z +9.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 5.57× (z +8.9) | — |
| [[A-427 (line)]] | wt | 21.2 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.39× (z +8.8) ⚠ cell-cycle shift, explains ~25% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.398× (z -9.5) |
| [[C32 (line)]] | wt | 22.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.66× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 22.7 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.75× (z +10.1) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[HepG2_C3A (line)]] | wt | 18.4 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.49× (z +8.6) | — |
| [[RKO (line)]] | wt | 41.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.01× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9300), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[SIGMAR1]] | +0.62 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[EFR3A]] | +0.61 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[MMGT1]] | +0.60 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[ICMT]] | +0.60 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[BTBD1]] | +0.59 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[WDR77]] | +0.59 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[OCRL]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[NAE1]] | +0.57 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[TTLL12]] | +0.56 | +0.33 / +0.61 | both halves | 1e-04 |  |
| [[TEX2]] | +0.56 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[AKAP11]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IGBP1]] | -0.66 | -0.67 / -0.64 | both halves | 7e-06 |  |
| [[KLC4]] | -0.63 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[AKAP17A]] | -0.63 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[CWC25]] | -0.61 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[NOXRED1]] | -0.60 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[NGDN]] | -0.59 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[SPACDR]] | -0.59 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[APPBP2]] | -0.58 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[RAB5A]] | -0.58 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[IST1]] | -0.58 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[ISY1-RAB43]] | -0.58 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[COQ10B]] | -0.58 | -0.64 / -0.54 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.378). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.2, -29.3); signed map (-12.0, -39.4). **Vector** length 62.2, 12.8% of its response variance represented; |z| ≥ 3 in 1,260 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | +5.0 | +16.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +4.8 | +17.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +3.1 | +11.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.3 | +10.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +8.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.7 | +4.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.6 | +1.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.3 | +3.2 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | +4.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.9 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.7 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | +4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -0.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | isocitrate dehydrogenase (NAD(+)) 3 catalytic subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.1 — chr15:78,131,498-78,171,945 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Isocitrate dehydrogenases |
| Hallmark sets | ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Citric acid cycle (TCA cycle); Mitochondrial protein degradation; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P50213](https://www.uniprot.org/uniprotkb/P50213) (Isocitrate dehydrogenase):

> Catalytic subunit of the enzyme which catalyzes the decarboxylation of isocitrate (ICT) into alpha-ketoglutarate. The heterodimer composed of the alpha (IDH3A) and beta (IDH3B) subunits and the heterodimer composed of the alpha (IDH3A) and gamma (IDH3G) subunits, have considerable basal activity but the full activity of the heterotetramer (containing two subunits of IDH3A, one of IDH3B and one of IDH3G) requires the assembly and cooperative function of both heterodimers.

**Summary**, from NCBI Gene [3419](https://www.ncbi.nlm.nih.gov/gene/3419):

> Isocitrate dehydrogenases catalyze the oxidative decarboxylation of isocitrate to 2-oxoglutarate. These enzymes belong to two distinct subclasses, one of which utilizes NAD(+) as the electron acceptor and the other NADP(+). Five isocitrate dehydrogenases have been reported: three NAD(+)-dependent isocitrate dehydrogenases, which localize to the mitochondrial matrix, and two NADP(+)-dependent isocitrate dehydrogenases, one of which is mitochondrial and the other predominantly cytosolic. …

**Accessions** — [HGNC:5384](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5384) · Entrez [3419](https://www.ncbi.nlm.nih.gov/gene/3419) · UniProt [P50213](https://www.uniprot.org/uniprotkb/P50213) · Ensembl [ENSG00000166411](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166411)

## Data

Gene col 9300: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9300); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9300, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9300]; `tensor/DDL_lfc|DDL_z.npy` [9300]; `embed/gene_vectors.npy` [9300]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9300 or target_col == 9300). Every well: [[IDH3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IDH3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
