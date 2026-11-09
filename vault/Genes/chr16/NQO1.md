---
symbol: "NQO1"
type: "gene"
col: 11157
ensembl_id: "ENSG00000181019"
name: "NAD(P)H quinone dehydrogenase 1"
location: "16q22.1"
module: 17
arm: "-"
pooled_cpm: 111.46
n_lines_expressing: 45
n_dd_up: 22
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# NQO1

*NAD(P)H quinone dehydrogenase 1* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.22× (z +14.2, q 9e-43, up in 44 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.08× (z +10.2, q 4e-22, up in 37 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.511× (z -9.3, q 8e-18, down in 34 of 43 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKR1B10]] (+0.55, fdr 2e-05), [[G6PD]] (+0.55, fdr 7e-06), [[AKR1C3]] (+0.52, fdr 2e-05); moves opposite to [[GPSM1]] (-0.54, fdr 5e-05), [[PRPF39]] (-0.53, fdr 2e-04), [[PKN1]] (-0.52, fdr 7e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[CCDC180]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11157.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **4.22×** | +14.2 | 9e-43 | 44/44 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **3.79×** | +12.6 | 7e-34 | 40/41 (NCI-H1792, J82, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.08×** | +10.2 | 4e-22 | 37/44 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.34×** | +8.4 | 7e-15 | 37/43 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.48×** | +8.3 | 1e-14 | 37/41 (NCI-H1792, J82, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.0 | 1e-07 | 34/43 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Auranofin (drug)]] 0.5 µM |  | **1.75×** | +5.5 | 3e-06 | 32/43 (HCT15, BT-474, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.44×** | +5.1 | 3e-05 | 40/43 (HT-29, SW1417, …) | top dose only |  |
| [[AZD-7648 (drug)]] 5 µM |  | **2.38×** | +4.5 | 5e-04 | 33/42 (NCI-H1573, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +3.9 | 0.005 | 29/43 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **1.51×** | +3.9 | 0.005 | 26/42 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | **1.46×** | +3.7 | 0.009 | 29/43 (AsPC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.45×** | +3.5 | 0.019 | 29/45 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.41×** | +3.4 | 0.026 | 29/43 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.40×** | +3.3 | 0.035 | 24/43 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.047 | 28/43 (J82, A498, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.047 | 22/43 (NCI-H1792, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.047 | 19/43 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.056 | 21/43 (NCI-H460, H4, …) | top dose only |  |
| [[Gemcitabine (drug)]] 5 µM |  | **1.51×** | +3.0 | 0.076 | 22/43 (BT-474, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[DT-061 (drug)]] 5 µM |  | **1.77×** | +2.9 | 0.083 | 20/43 (SK-MEL-2, NCI-H2030, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11157.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.511×** | -9.3 | 8e-18 | 34/43 (HCT15, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.492×** | -7.0 | 1e-09 | 33/43 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.531×** | -6.2 | 1e-07 | 30/43 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.558×** | -5.7 | 1e-06 | 29/43 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.665×** | -3.8 | 0.018 | 27/43 (HCT15, AN3 CA, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.766×** | -3.7 | 0.021 | 26/44 (C32, SNU-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.701×** | -3.5 | 0.040 | 24/43 (SNU-1, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.791×** | -3.2 | 0.081 | 21/43 (SNU-1, A498, …) | rises with dose | low cells (technical?) |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.706×** | -3.2 | 0.081 | 29/44 (C32, NCI-H661, …) | inconsistent across doses | position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | **0.539×** | -3.2 | 0.085 | 24/44 (J82, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ciclopirox (drug)]] 5 µM |  | 0.803× | -3.0 | 0.13 | 22/43 (BT-474, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11157. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 51.9 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 20.0× (z +17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 154 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -18.0) |
| [[SW480 (line)]] | alt | 79.3 | 2 (1 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +14.4) | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -15.3) |
| [[HEC-1-A (line)]] | alt | 47.5 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +12.1) | — |
| [[HOP62 (line)]] | alt | 57.8 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.40× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +8.6) | — |
| [[KATO III (line)]] | alt | 164 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -18.4) |
| [[MIA PaCa-2 (line)]] | alt | 120 | 4 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -12.8) |
| [[A549 (line)]] | wt | 152 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.0× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 138 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -15.6) |
| [[HS-578T (line)]] | alt | 55.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.78× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 138 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.7× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 268 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -13.6) |
| [[SNU-1 (line)]] | wt | 243 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -18.5) |
| [[A498 (line)]] | wt | 171 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[AsPC-1 (line)]] | alt | 49.9 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +11.0) | — |
| [[BT-474 (line)]] | alt | 69.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -9.0) |
| [[C32 (line)]] | wt | 135 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.85× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.304× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 68.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.11× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -8.9) |
| [[Hs 766T (line)]] | wt | 51.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.81× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +9.7) | — |
| [[J82 (line)]] | alt | 177 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.50× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 103 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.26× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -15.1) |
| [[PANC-1 (line)]] | alt | 46.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.39× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.11× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 97.3 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -9.5) |
| [[AN3 CA (line)]] | alt | 107 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[CFPAC-1 (line)]] | alt | 81.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 41.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.25× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 485 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 87.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 130 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -18.6) |
| [[SK-MEL-2 (line)]] | alt | 52.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.36× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 32.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-427 (line)]] | wt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -11.2) |
| [[HCT15 (line)]] | alt | 336 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -20.5) |
| [[hTERT-HPNE (line)]] | wt | 34.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.71× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H23 (line)]] | alt | 137 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 56.9 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.57× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 181 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -10.7) |
| [[SW48 (line)]] | wt | 45.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -9.8) |
| [[C-33 A (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.6 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 75.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11157), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKR1B10]] | +0.55 | +0.47 / +0.53 | both halves | 2e-05 | STRING 630 |
| [[G6PD]] | +0.55 | +0.64 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_REACTIVE_OXYGEN_SPECIES_PATHWAY; STRING 568 |
| [[AKR1C3]] | +0.52 | +0.57 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM; STRING 567 |
| [[ARSB]] | +0.52 | +0.47 / +0.31 | both halves | 2e-04 |  |
| [[NXT2]] | +0.51 | +0.39 / +0.41 | both halves | 5e-05 |  |
| [[PGD]] | +0.51 | +0.48 / +0.54 | both halves | 2e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM; STRING 430 |
| [[DDX3X]] | +0.50 | +0.41 / +0.39 | both halves | 5e-05 |  |
| [[IL13RA1]] | +0.50 | +0.48 / +0.38 | both halves | 6e-05 |  |
| [[PKM]] | +0.50 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[RCC2]] | +0.49 | +0.44 / +0.30 | both halves | 2e-04 |  |
| [[PCDH7]] | +0.49 | +0.41 / +0.38 | both halves | 6e-05 |  |
| [[MBNL3]] | +0.49 | +0.56 / +0.27 | both halves | 3e-04 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPSM1]] | -0.54 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[PRPF39]] | -0.53 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[PKN1]] | -0.52 | -0.37 / -0.48 | both halves | 7e-05 |  |
| [[TAMM41]] | -0.52 | -0.26 / -0.51 | both halves | 4e-04 |  |
| [[CBY1]] | -0.52 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[ETNK2]] | -0.52 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[PIGH]] | -0.51 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[THOC1]] | -0.51 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[TTC38]] | -0.51 | -0.37 / -0.39 | both halves | 8e-05 |  |
| [[LCMT1]] | -0.50 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[ZMYM6]] | -0.50 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[SLC25A42]] | -0.50 | -0.46 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NQO1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises NQO1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC180]] | B | NQO1 activity lowers CCDC180's level | lines that do not express NQO1 (5) vs lines expressing it (45) | 2.46× higher at baseline in the lines without NQO1 | 0.078 | ⚠ within organs, on part of the lines |
| [[STRA6LP]] | B | NQO1 activity lowers STRA6LP's level | lines that do not express NQO1 (5) vs lines expressing it (45) | 1.67× higher at baseline in the lines without NQO1 | 0.098 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.418). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-17.4, 23.1); signed map (12.2, -1.6). **Vector** length 104, 33.4% of its response variance represented; |z| ≥ 3 in 1,200 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.7 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +8.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +3.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.1 | +3.5 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +2.5 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +0.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.3 | +3.4 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.7 | -3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.0 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.8 | -2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -9.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.7 | -6.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | -3.5 | +0.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -3.3 | -0.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | NAD(P)H quinone dehydrogenase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:69,706,996-69,726,668 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DHQU, QR1, DTD; previously NMOR1, DIA4 |
| Gene groups (HGNC) | Flavoproteins; Quinone dehydrogenase family |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY, MYOGENESIS, XENOBIOTIC_METABOLISM |
| Reactome | 13 pathways, smallest: NFE2L2 regulating anti-oxidant/detoxification enzymes; CHD6, CHD7, CHD8, CHD9 subfamily; Regulation of ornithine decarboxylase (ODC) |
| Matched by | ensembl_id |

**Function**, from UniProt [P15559](https://www.uniprot.org/uniprotkb/P15559) (NAD(P)H dehydrogenase):

> Flavin-containing quinone reductase that catalyzes two-electron reduction of quinones to hydroquinones using either NADH or NADPH as electron donors. In a ping-pong kinetic mechanism, the electrons are sequentially transferred from NAD(P)H to flavin cofactor and then from reduced flavin to the quinone, bypassing the formation of semiquinone and reactive oxygen species (By similarity). Regulates cellular redox state primarily through quinone detoxification. Reduces components of plasma membrane …

**Summary**, from NCBI Gene [1728](https://www.ncbi.nlm.nih.gov/gene/1728):

> This gene is a member of the NAD(P)H dehydrogenase (quinone) family and encodes a cytoplasmic 2-electron reductase. This FAD-binding protein forms homodimers and reduces quinones to hydroquinones. This protein's enzymatic activity prevents the one electron reduction of quinones that results in the production of radical species. Mutations in this gene have been associated with tardive dyskinesia (TD), an increased risk of hematotoxicity after exposure to benzene, and susceptibility to various …

**Accessions** — [HGNC:2874](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2874) · Entrez [1728](https://www.ncbi.nlm.nih.gov/gene/1728) · UniProt [P15559](https://www.uniprot.org/uniprotkb/P15559) · Ensembl [ENSG00000181019](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181019)

## Data

Gene col 11157: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11157); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11157, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11157]; `tensor/DDL_lfc|DDL_z.npy` [11157]; `embed/gene_vectors.npy` [11157]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11157 or target_col == 11157). Every well: [[NQO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NQO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
