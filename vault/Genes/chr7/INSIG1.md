---
symbol: "INSIG1"
type: "gene"
col: 11820
ensembl_id: "ENSG00000186480"
name: "insulin induced gene 1"
location: "7q36.3"
module: 86
arm: "+"
pooled_cpm: 99.59
n_lines_expressing: 49
n_dd_up: 43
n_dd_down: 39
n_dd_up_clean: 35
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# INSIG1

*insulin induced gene 1* — 7q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.93× (z +15.0, q 0e+00, up in 32 of 47 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Berbamine (drug)]] 5 µM: 2.73× (z +14.0, q 3e-42, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (10 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.631× (z -6.5, q 6e-08, down in 33 of 47 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.645× (z -6.2, q 2e-07, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SREBF2]] (+0.76, fdr 7e-06), [[SQLE]] (+0.75, fdr 7e-06), [[FDFT1]] (+0.75, fdr 7e-06); moves opposite to [[ANGEL2]] (-0.49, fdr 1e-04), [[MAPKAPK5]] (-0.48, fdr 5e-05), [[C8orf33]] (-0.48, fdr 1e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11820.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.93×** | +15.0 | 0e+00 | 32/47 (PANC-1, NCI-H2347, …) | rises with dose | composition shift |
| [[Berbamine (drug)]] 5 µM |  | **2.73×** | +14.0 | 3e-42 | 46/48 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | **2.69×** | +13.8 | 5e-41 | 46/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.37×** | +11.5 | 1e-28 | 26/47 (PANC-1, HS-578T, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.14×** | +11.3 | 1e-27 | 45/47 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.05×** | +11.0 | 3e-26 | 47/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.05×** | +11.0 | 3e-26 | 42/47 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.96×** | +10.7 | 5e-25 | 43/47 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.33×** | +8.4 | 4e-15 | 38/47 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.17×** | +7.6 | 1e-12 | 39/47 (NCI-H460, SW 900, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.16×** | +7.6 | 1e-12 | 42/47 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.06×** | +7.1 | 4e-11 | 29/47 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.91×** | +6.1 | 4e-08 | 39/48 (C32, LS 180, …) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +5.9 | 2e-07 | 33/46 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.78×** | +5.7 | 5e-07 | 40/47 (A549, NCI-H2030, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | **1.47×** | +5.4 | 2e-06 | 41/47 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.69×** | +5.0 | 2e-05 | 34/47 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.68×** | +4.9 | 2e-05 | 30/47 (LS 180, LoVo, …) | top dose only | plate-row cell shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.70×** | +4.9 | 2e-05 | 30/47 (HEC-1-A, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +4.8 | 3e-05 | 27/47 (Panc 03.27, AN3 CA, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11820.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.631×** | -6.5 | 6e-08 | 33/47 (SW48, HS-578T, …) | top dose only | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.645×** | -6.2 | 2e-07 | 39/47 (hTERT-HPNE, A-172, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.553×** | -5.9 | 8e-07 | 32/47 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.571×** | -5.4 | 1e-05 | 27/47 (KATO III, HCT15, …) | top dose only |  |
| [[Quinestrol (drug)]] 5 µM |  | **0.698×** | -5.1 | 5e-05 | 34/48 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.584×** | -4.8 | 2e-04 | 28/47 (C32, hTERT-HPNE, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.623×** | -4.7 | 2e-04 | 35/48 (PANC-1, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.627×** | -4.6 | 2e-04 | 27/47 (HOP62, A498, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -4.5 | 5e-04 | 24/41 (Hs 766T, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | **0.734×** | -4.3 | 8e-04 | 32/47 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.639×** | -4.3 | 9e-04 | 27/46 (hTERT-HPNE, LS 180, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.662×** | -4.1 | 0.002 | 31/47 (KATO III, CFPAC-1, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.667×** | -4.0 | 0.002 | 24/47 (HOP62, SNU-423, …) | all doses, flat | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.667×** | -4.0 | 0.002 | 29/47 (HOP62, A498, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.682×** | -3.8 | 0.005 | 25/47 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.686×** | -3.8 | 0.006 | 28/47 (LS 180, HCT15, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.686×** | -3.7 | 0.006 | 22/47 (A-427, BT-474, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.693×** | -3.6 | 0.008 | 26/47 (HOP62, A498, …) | all doses, flat | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.679×** | -3.6 | 0.008 | 29/46 (RPMI-7951, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11820. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 58.4 | 15 (8 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 17.8× (z +16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 15.9× (z +15.8) | — |
| [[PANC-1 (line)]] | alt | 87.6 | 13 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +30.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.96× (z +14.4) | — |
| [[HS-578T (line)]] | alt | 143 | 11 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 12.4× (z +17.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Cepharanthine (drug)]] 5 µM 4.02× (z +14.0) | [[Selinexor (drug)]] 5 µM 0.392× (z -9.4) ⚠ cell-cycle shift, explains ~53% of this change |
| [[hTERT-HPNE (line)]] | wt | 262 | 6 (4 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.39× (z +17.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.79× (z +10.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.250× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~37% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.277× (z -8.8) |
| [[SW 900 (line)]] | alt | 117 | 11 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.61× (z +17.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 16.4× (z +17.0) | — |
| [[HOP62 (line)]] | alt | 98.3 | 5 (2 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 6.86× (z +17.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Cepharanthine (drug)]] 5 µM 4.76× (z +13.8) | [[Clobetasol propionate (drug)]] 0.05 µM 0.220× (z -9.5) |
| [[HCT15 (line)]] | alt | 152 | 4 | 4 (3 ⚠) | [[Berbamine (drug)]] 5 µM 3.15× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -15.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.274× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 41.4 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 23.1× (z +24.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 7.64× (z +11.2) | — |
| [[A549 (line)]] | wt | 33.4 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +22.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Cepharanthine (drug)]] 5 µM 7.80× (z +16.2) | — |
| [[AsPC-1 (line)]] | alt | 67.4 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.8× (z +25.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 6.41× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 67.8 | 7 (3 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 4.89× (z +14.1) | — |
| [[KATO III (line)]] | alt | 291 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -12.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Quinestrol (drug)]] 5 µM 0.315× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 35.2 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +18.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 12.6× (z +13.9) | — |
| [[A498 (line)]] | wt | 179 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +21.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Cepharanthine (drug)]] 5 µM 2.94× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 134 | 6 (1 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 4.70× (z +14.6) | — |
| [[NCI-H1792 (line)]] | alt | 141 | 6 (4 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 12.6× (z +15.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 8.74× (z +13.9) | — |
| [[NCI-H2347 (line)]] | alt | 48.1 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +28.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.61× (z +10.1) | — |
| [[A-427 (line)]] | wt | 52.5 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.78× (z +9.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.0715× (z -19.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.270× (z -9.8) |
| [[J82 (line)]] | alt | 111 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +23.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 6.85× (z +11.8) | — |
| [[SNU-423 (line)]] | alt | 156 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.01× (z +18.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Cepharanthine (drug)]] 5 µM 3.28× (z +10.5) | — |
| [[SW48 (line)]] | wt | 112 | 3 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 6.41× (z +8.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 6.38× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.0718× (z -11.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 40.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 5.55× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 83.0 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.77× (z +12.5) | — |
| [[LS 180 (line)]] | wt | 170 | 3 | 1 (1 ⚠) | [[Berbamine (drug)]] 5 µM 5.59× (z +14.3) | [[Selinexor (drug)]] 5 µM 0.356× (z -8.5) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SNU-1 (line)]] | wt | 92.4 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.51× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 6.22× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 93.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.51× (z +13.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Berbamine (drug)]] 5 µM 2.71× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 37.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +13.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Cepharanthine (drug)]] 5 µM 3.71× (z +12.1) | — |
| [[NCI-H23 (line)]] | alt | 30.2 | 3 (1 ⚠) | 0 | [[Cepharanthine (drug)]] 5 µM 9.70× (z +17.5) | — |
| [[SHP-77 (line)]] | alt | 46.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.60× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 59.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 6.42× (z +10.2) ⚠ cell-cycle shift, explains ~26% of this change | [[Dinaciclib (drug)]] 5 µM 0.151× (z -10.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 175 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 9.68× (z +12.5) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[BT-474 (line)]] | alt | 141 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.252× (z -9.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.281× (z -8.7) |
| [[C-33 A (line)]] | alt | 75.8 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.38× (z +13.2) | — |
| [[C32 (line)]] | wt | 254 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.17× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 184 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +26.8) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[CHP-212 (line)]] | wt | 38.8 | 1 | 1 | [[Cepharanthine (drug)]] 5 µM 7.35× (z +9.4) | [[Temuterkib (drug)]] 0.05 µM 0.0379× (z -10.2) |
| [[LoVo (line)]] | wt | 90.2 | 2 | 0 | [[Berbamine (drug)]] 5 µM 7.05× (z +18.4) | — |
| [[SW 1088 (line)]] | alt | 141 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.58× (z +10.5) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[Hs 766T (line)]] | wt | 48.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0658× (z -13.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 129 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 11.6× (z +16.4) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[AN3 CA (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 97.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.70 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 85.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 99.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11820), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SREBF2]] | +0.76 | +0.73 / +0.67 | both halves | 7e-06 | pathway: Metabolism of steroids; STRING 997 |
| [[SQLE]] | +0.75 | +0.77 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 773 |
| [[FDFT1]] | +0.75 | +0.72 / +0.70 | both halves | 7e-06 | pathway: Metabolism of steroids; STRING 774 |
| [[IDI1]] | +0.74 | +0.73 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 860 |
| [[STARD4]] | +0.74 | +0.74 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 576 |
| [[HMGCS1]] | +0.74 | +0.74 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 885 |
| [[MVD]] | +0.73 | +0.75 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION; STRING 492 |
| [[DHCR7]] | +0.71 | +0.74 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 709 |
| [[HMGCR]] | +0.71 | +0.70 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 999 |
| [[SCD]] | +0.71 | +0.74 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 690 |
| [[ACSS2]] | +0.68 | +0.72 / +0.55 | both halves | 1e-05 | STRING 535 |
| [[EBP]] | +0.66 | +0.69 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 427 |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANGEL2]] | -0.49 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[MAPKAPK5]] | -0.48 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[C8orf33]] | -0.48 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[FAIM]] | -0.47 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[ARMC8]] | -0.46 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[EXOSC10]] | -0.45 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[NOL9]] | -0.45 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[PCBD2]] | -0.45 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[ALG8]] | -0.44 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[METAP1D]] | -0.44 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[QTRT1]] | -0.44 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[QTRT2]] | -0.43 | -0.43 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.791). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.3, -48.8); signed map (-53.1, 32.4). **Vector** length 153, 59.7% of its response variance represented; |z| ≥ 3 in 2,153 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cholesterol biosynthesis* (reactome, mean cos +0.64 to 20); *cholesterol homeostasis* (hallmark, mean cos +0.63 to 24); *Activation of gene expression by SREBF (SREBP)* (reactome, mean cos +0.67 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +11.7 | +13.8 |
|  | [[Berbamine (drug)]] 5 µM |  | +10.1 | +14.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +9.1 | +11.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +9.1 | +11.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +8.0 | +5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +7.5 | +3.0 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +6.2 | +6.1 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -6.2 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -6.0 | -4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.8 | -5.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -5.7 | -4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -5.6 | -6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -6.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.4 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | insulin induced gene 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.3 — chr7:155,297,776-155,310,235 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CL-6, MGC1405 |
| Hallmark sets | ANDROGEN_RESPONSE, UV_RESPONSE_DN, APICAL_JUNCTION, MTORC1_SIGNALING |
| Reactome | 3 pathways, smallest: Regulation of cholesterol biosynthesis by SREBP (SREBF); Metabolism of steroids; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [O15503](https://www.uniprot.org/uniprotkb/O15503) (Insulin-induced gene 1 protein):

> Oxysterol-binding protein that mediates feedback control of cholesterol synthesis by controlling both endoplasmic reticulum to Golgi transport of SCAP and degradation of HMGCR. Acts as a negative regulator of cholesterol biosynthesis by mediating the retention of the SCAP-SREBP complex in the endoplasmic reticulum, thereby blocking the processing of sterol regulatory element-binding proteins (SREBPs) SREBF1/SREBP1 and SREBF2/SREBP2. Binds oxysterol, including 25-hydroxycholesterol, regulating …

**Summary**, from NCBI Gene [3638](https://www.ncbi.nlm.nih.gov/gene/3638):

> This gene encodes an endoplasmic reticulum membrane protein that regulates cholesterol metabolism, lipogenesis, and glucose homeostasis. The encoded protein has six transmembrane helices which contain an effector protein binding site. It binds the sterol-sensing domains of sterol regulatory element-binding protein (SREBP) cleavage-activating protein (SCAP) and 3-hydroxy-3-methylglutaryl-coenzyme A reductase (HMG-CoA reductase), and is essential for the sterol-mediated trafficking of these two …

**Accessions** — [HGNC:6083](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6083) · Entrez [3638](https://www.ncbi.nlm.nih.gov/gene/3638) · UniProt [O15503](https://www.uniprot.org/uniprotkb/O15503) · Ensembl [ENSG00000186480](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186480)

## Data

Gene col 11820: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11820); `tables/drug_effects.parquet` (82 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11820, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11820]; `tensor/DDL_lfc|DDL_z.npy` [11820]; `embed/gene_vectors.npy` [11820]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11820 or target_col == 11820). Every well: [[INSIG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INSIG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
