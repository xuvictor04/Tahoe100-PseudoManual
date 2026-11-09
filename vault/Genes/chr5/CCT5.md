---
symbol: "CCT5"
type: "gene"
col: 7456
ensembl_id: "ENSG00000150753"
name: "chaperonin containing TCP1 subunit 5"
location: "5p15.2"
module: 4
arm: "+"
pooled_cpm: 124.56
n_lines_expressing: 50
n_dd_up: 46
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# CCT5

*chaperonin containing TCP1 subunit 5* — 5p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 46 drug-doses (22 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.55× (z +19.6, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 2.71× (z +12.9, q 8e-36, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW48 0.446×, RKO 0.511×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.421×; ⚠ cell-cycle shift, explains ~0% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (CHP-212 0.0776×); [[Atazanavir (sulfate) (drug)]] 0.05 µM in 1 line (NCI-H596 0.341×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCT3]] (+0.90, fdr 7e-06), [[CCT2]] (+0.85, fdr 7e-06), [[CCT6A]] (+0.84, fdr 7e-06); moves opposite to [[SIRT2]] (-0.75, fdr 7e-06), [[PHPT1]] (-0.73, fdr 7e-06), [[TERF2IP]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DHRS3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 22 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 46 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7456.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **4.55×** | +19.6 | 0e+00 | 48/49 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **4.24×** | +18.0 | 0e+00 | 44/44 (A498, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **3.32×** | +14.3 | 3e-44 | 45/45 (A498, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.71×** | +12.9 | 8e-36 | 48/48 (HT-29, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.69×** | +12.8 | 3e-35 | 48/48 (HT-29, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.65×** | +12.6 | 2e-34 | 47/48 (HT-29, C32, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **2.21×** | +9.8 | 7e-21 | 44/47 (COLO 205, C32, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.97×** | +8.3 | 9e-15 | 42/48 (HT-29, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.78×** | +7.5 | 6e-12 | 40/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.67×** | +6.6 | 2e-09 | 41/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.58×** | +5.9 | 2e-07 | 33/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.27×** | +5.5 | 2e-06 | 38/45 (AsPC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +5.4 | 3e-06 | 35/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.54×** | +5.4 | 3e-06 | 28/48 (NCI-H1792, C32, …) | all doses, stronger at high dose | composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.52×** | +5.4 | 3e-06 | 37/47 (HOP62, NCI-H460, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.11×** | +5.0 | 2e-05 | 42/48 (HT-29, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +4.7 | 7e-05 | 33/48 (LOX-IMVI, A549, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.94×** | +4.5 | 2e-04 | 34/48 (CFPAC-1, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.001 | 26/48 (NCI-H1792, C32, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.001 | 28/49 (HT-29, SW 900, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.001 | 30/48 (A549, HS-578T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.37×** | +4.0 | 0.001 | 26/48 (AN3 CA, SW 900, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.001 | 33/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.36×** | +4.0 | 0.001 | 32/47 (HOP62, H4, …) | all doses, stronger at high dose |  |
| [[Thymol (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.002 | 28/48 (HT-29, A-427, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.004 | 24/48 (A-172, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7456.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW48 0.446×, RKO 0.511×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.421×; ⚠ cell-cycle shift, explains ~0% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (CHP-212 0.0776×); [[Atazanavir (sulfate) (drug)]] 0.05 µM in 1 line (NCI-H596 0.341×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.739× | -3.6 | 0.12 | 26/50 (NCI-H596, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | 0.751× | -3.5 | 0.12 | 30/49 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.762× | -3.4 | 0.12 | 25/48 (A-427, H4, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.766× | -3.3 | 0.12 | 23/47 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.631× | -3.1 | 0.20 | 23/50 (BT-474, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7456. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 66.9 | 10 (9 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.9× (z +17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 3.71× (z +9.3) | — |
| [[A-172 (line)]] | wt | 112 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +16.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.82× (z +9.0) | — |
| [[C32 (line)]] | wt | 43.6 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.34× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.19× (z +10.9) | — |
| [[HT-29 (line)]] | alt | 95.1 | 8 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.12× (z +16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.75× (z +11.7) | — |
| [[NCI-H1573 (line)]] | alt | 41.7 | 8 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.46× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.73× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 64.1 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.51× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.76× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 61.6 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.57× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 121 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.72× (z +15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.90× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 117 | 5 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.29× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.33× (z +10.1) | [[Adagrasib (drug)]] 0.05 µM 0.661× (z -11.8) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 96.7 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.55× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.41× (z +10.6) | — |
| [[SW 900 (line)]] | alt | 94.7 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.35× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.15× (z +10.1) | — |
| [[SW480 (line)]] | alt | 173 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.84× (z +10.3) | — |
| [[A498 (line)]] | wt | 206 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.81× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 116 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.41× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.37× (z +8.8) | — |
| [[J82 (line)]] | alt | 203 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.47× (z +9.4) | — |
| [[KATO III (line)]] | alt | 78.9 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.26× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.33× (z +9.7) | — |
| [[LoVo (line)]] | wt | 122 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.86× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 141 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.37× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.70× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 151 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.27× (z +8.8) | — |
| [[RKO (line)]] | wt | 127 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.20× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 59.3 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.37× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.79× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 121 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.68× (z +10.5) | — |
| [[A-427 (line)]] | wt | 290 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 92.9 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.86× (z +9.3) | — |
| [[A549 (line)]] | wt | 95.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.42× (z +17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[AN3 CA (line)]] | alt | 165 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.16× (z +8.6) | — |
| [[AsPC-1 (line)]] | alt | 74.3 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.06× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 91.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 84.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.94× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 91.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 273 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H460 (line)]] | wt | 101 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.12× (z +19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[RPMI-7951 (line)]] | alt | 79.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.34× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 93.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.97× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 115 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[CHP-212 (line)]] | wt | 93.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0776× (z -12.1) |
| [[COLO 205 (line)]] | alt | 51.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.12× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[H4 (line)]] | wt | 98.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.93× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HCT15 (line)]] | alt | 95.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.09× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H23 (line)]] | alt | 167 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2347 (line)]] | alt | 149 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.05× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 222 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 58.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.18× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW48 (line)]] | wt | 127 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.90× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 175 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.66× (z +9.1) | — |
| [[NCI-H596 (line)]] | alt | 98.2 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.341× (z -9.4) |
| [[NCI-H2122 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 104 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7456), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT3]] | +0.90 | +0.92 / +0.88 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[CCT2]] | +0.85 | +0.85 / +0.86 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[CCT6A]] | +0.84 | +0.86 / +0.80 | both halves | 7e-06 | same gene group; pathway: Association of TriC/CCT with target proteins during biosynthesis; STRING 999 |
| [[CCT7]] | +0.83 | +0.83 / +0.81 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[STIP1]] | +0.76 | +0.75 / +0.76 | both halves | 7e-06 | STRING 978 |
| [[CCT4]] | +0.76 | +0.84 / +0.68 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[NUDC]] | +0.75 | +0.76 / +0.74 | both halves | 7e-06 | STRING 715 |
| [[PTPN11]] | +0.74 | +0.77 / +0.76 | both halves | 7e-06 |  |
| [[ATIC]] | +0.73 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[HSPD1]] | +0.72 | +0.78 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 588 |
| [[ABCF2]] | +0.72 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[TMEM33]] | +0.72 | +0.69 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT2]] | -0.75 | -0.74 / -0.74 | both halves | 7e-06 |  |
| [[PHPT1]] | -0.73 | -0.70 / -0.72 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.71 | -0.66 / -0.73 | both halves | 7e-06 |  |
| [[AAMDC]] | -0.70 | -0.70 / -0.66 | both halves | 7e-06 |  |
| [[MINDY2]] | -0.70 | -0.66 / -0.71 | both halves | 7e-06 |  |
| [[TNRC6C]] | -0.69 | -0.68 / -0.63 | both halves | 7e-06 | pathway: Cilium Assembly |
| [[GABARAP]] ⚠ | -0.69 | -0.72 / -0.58 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[INAFM1]] | -0.69 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[TMEM258]] | -0.69 | -0.68 / -0.65 | both halves | 7e-06 |  |
| [[SERF2]] | -0.68 | -0.66 / -0.63 | both halves | 7e-06 |  |
| [[ZFYVE1]] | -0.68 | -0.69 / -0.65 | both halves | 7e-06 |  |
| [[FKBP2]] ⚠ | -0.68 | -0.63 / -0.63 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RSRP1]] | -0.68 | -0.61 / -0.75 | both halves | 7e-06 |  |
| [[DCTN6-DT]] | -0.67 | -0.66 / -0.69 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DHRS3]] | B | DHRS3 activity lowers CCT5's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 1.34× higher at baseline in the lines without DHRS3 | 0.069 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |
| [[SACS]] | B | SACS activity raises CCT5's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.42× lower at baseline in the lines without SACS | 0.095 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.819). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-21.8, -31.8); signed map (-11.9, -44.6). **Vector** length 104, 44.7% of its response variance represented; |z| ≥ 3 in 1,420 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA Aminoacylation* (reactome, mean cos +0.50 to 7); *tRNA processing in the nucleus* (reactome, mean cos +0.55 to 8); *tRNA processing* (reactome, mean cos +0.53 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +7.3 | +12.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.1 | +12.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.9 | +8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.8 | +12.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.9 | +6.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +2.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.3 | +4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.3 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.8 | -1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | +2.5 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -2.3 | -0.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.1 | -0.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.1 | +0.8 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.1 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | chaperonin containing TCP1 subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.2 — chr5:10,249,929-10,266,389 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0098, CCTE |
| Gene groups (HGNC) | Chaperonin containing TCP1 |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 13 pathways, smallest: Folding of actin by CCT/TriC; Formation of tubulin folding intermediates by CCT/TriC; BBSome-mediated cargo-targeting to cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [P48643](https://www.uniprot.org/uniprotkb/P48643) (T-complex protein 1 subunit epsilon):

> Component of the chaperonin-containing T-complex (TRiC), a molecular chaperone complex that assists the folding of actin, tubulin and other proteins upon ATP hydrolysis. The TRiC complex mediates the folding of WRAP53/TCAB1, thereby regulating telomere maintenance. As part of the TRiC complex may play a role in the assembly of BBSome, a complex involved in ciliogenesis regulating transports vesicles to the cilia.

**Summary**, from NCBI Gene [22948](https://www.ncbi.nlm.nih.gov/gene/22948):

> The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including actin and tubulin. Mutations in this gene cause hereditary sensory and autonomic …

**Accessions** — [HGNC:1618](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1618) · Entrez [22948](https://www.ncbi.nlm.nih.gov/gene/22948) · UniProt [P48643](https://www.uniprot.org/uniprotkb/P48643) · Ensembl [ENSG00000150753](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150753)

## Data

Gene col 7456: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7456); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7456, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7456]; `tensor/DDL_lfc|DDL_z.npy` [7456]; `embed/gene_vectors.npy` [7456]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7456 or target_col == 7456). Every well: [[CCT5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCT5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
