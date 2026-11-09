---
symbol: "C1QBP"
type: "gene"
col: 2967
ensembl_id: "ENSG00000108561"
name: "complement C1q binding protein"
location: "17p13.2"
module: 4
arm: "+"
pooled_cpm: 48.74
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# C1QBP

*complement C1q binding protein* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.46× (z +16.3, q 0e+00, up in 45 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.74× (z +4.9, q 1e-04, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.627× (z -3.7, q 0.073, down in 27 of 48 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.745× (z -3.7, q 0.073, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.337×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.281×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.368×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (COLO 205 0.0753×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATIC]] (+0.79, fdr 7e-06), [[PRKDC]] (+0.72, fdr 7e-06), [[POLR1A]] (+0.71, fdr 7e-06); moves opposite to [[ZFAND2B]] (-0.68, fdr 7e-06), [[SELENOK]] (-0.67, fdr 9e-06), [[WBP1]] (-0.65, fdr 8e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[ISCU]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2967.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **7.46×** | +16.3 | 0e+00 | 45/45 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **6.04×** | +15.1 | 0e+00 | 42/42 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.74×** | +12.6 | 4e-34 | 45/45 (J82, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +5.2 | 2e-05 | 41/46 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +4.9 | 1e-04 | 34/47 (MIA PaCa-2, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **1.73×** | +4.8 | 1e-04 | 38/46 (HOP62, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.81×** | +4.8 | 1e-04 | 37/48 (NCI-H1792, A549, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | **1.73×** | +4.6 | 3e-04 | 35/47 (NCI-H1792, C32, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **1.68×** | +4.6 | 3e-04 | 30/46 (SW480, COLO 205, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +4.1 | 0.002 | 29/48 (NCI-H1792, HT-29, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.43×** | +4.1 | 0.002 | 37/48 (NCI-H2030, HOP62, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.62×** | +4.1 | 0.002 | 31/48 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.022 | 33/47 (A498, SNU-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **2.11×** | +3.4 | 0.026 | 31/46 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **2.03×** | +3.2 | 0.046 | 25/48 (NCI-H1792, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.81×** | +3.2 | 0.055 | 28/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.96×** | +3.1 | 0.063 | 24/47 (AsPC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.77×** | +3.0 | 0.066 | 23/45 (SHP-77, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.93×** | +3.0 | 0.068 | 22/47 (NCI-H2030, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.93×** | +3.0 | 0.068 | 21/45 (C32, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2967.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.337×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.281×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.368×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (COLO 205 0.0753×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.627×** | -3.7 | 0.073 | 27/48 (LoVo, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.745×** | -3.7 | 0.073 | 25/48 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | 0.487× | -3.3 | 0.15 | 27/48 (LoVo, BT-474, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.769× | -3.3 | 0.15 | 32/48 (RKO, A-427, …) | all doses, flat | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 0.497× | -3.2 | 0.15 | 24/48 (A-427, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM |  | 0.700× | -3.0 | 0.25 | 24/48 (H4, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~21% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2967. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 74.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.40× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 30.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.25× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-427 (line)]] | wt | 93.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A498 (line)]] | wt | 42.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.26× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A549 (line)]] | wt | 53.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.9× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[C32 (line)]] | wt | 27.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.49× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HOP62 (line)]] | alt | 20.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.9× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HS-578T (line)]] | alt | 31.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.63× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HT-29 (line)]] | alt | 28.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.35× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[J82 (line)]] | alt | 39.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.09× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[KATO III (line)]] | alt | 69.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.10× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LoVo (line)]] | wt | 71.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.46× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LOX-IMVI (line)]] | wt | 33.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.68× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 72.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.45× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 24.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 19.9× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2030 (line)]] | alt | 54.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.58× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[Panc 03.27 (line)]] | alt | 22.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.60× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[PANC-1 (line)]] | alt | 51.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.23× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[RKO (line)]] | wt | 96.8 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.2) |
| [[SNU-423 (line)]] | alt | 18.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.8× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW480 (line)]] | alt | 104 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.02× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[CFPAC-1 (line)]] | alt | 14.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.45× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[H4 (line)]] | wt | 19.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.1× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HCT15 (line)]] | alt | 47.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.9× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HepG2_C3A (line)]] | wt | 36.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.13× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[Hs 766T (line)]] | wt | 35.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.21× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 24.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.72× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H23 (line)]] | alt | 92.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.86× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H460 (line)]] | wt | 75.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.50× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SW 900 (line)]] | alt | 18.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.65× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[C-33 A (line)]] | alt | 76.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.45× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[CHP-212 (line)]] | wt | 49.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.117× (z -8.6) ⚠ cell-cycle shift, explains ~76% of this change |
| [[COLO 205 (line)]] | alt | 17.1 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0753× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 46.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1573 (line)]] | alt | 15.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.83× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2347 (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[RPMI-7951 (line)]] | alt | 23.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.11× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SHP-77 (line)]] | alt | 97.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 24.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.81× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SNU-1 (line)]] | wt | 71.6 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.281× (z -10.4) |
| [[SW1417 (line)]] | alt | 34.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[AN3 CA (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 95.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2967), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATIC]] | +0.79 | +0.74 / +0.81 | both halves | 7e-06 |  |
| [[PRKDC]] | +0.72 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[NAA15]] | +0.71 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[RUVBL1]] | +0.71 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[FARSB]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[GOT2]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[PHB1]] | +0.71 | +0.75 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 847 |
| [[NME1]] | +0.70 | +0.79 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[MRPS27]] | +0.70 | +0.60 / +0.71 | both halves | 7e-06 | STRING 566 |
| [[VMA21]] | +0.69 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[MTHFD1]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFAND2B]] | -0.68 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[SELENOK]] | -0.67 | -0.57 / -0.63 | both halves | 9e-06 |  |
| [[WBP1]] | -0.65 | -0.58 / -0.66 | both halves | 8e-06 |  |
| [[BSDC1]] | -0.63 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[GABARAPL2]] | -0.62 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[IFT20]] | -0.62 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[SIRT2]] | -0.62 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.62 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[CCS]] | -0.62 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[PMM1]] | -0.61 | -0.69 / -0.64 | both halves | 7e-06 |  |
| [[PHF1]] | -0.61 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[FBXW5]] | -0.61 | -0.60 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ISCU]] | C | C1QBP's natural level strengthens ISCU's drug response | C1QBP's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67, reverse -0.22; direction not clear | 0.033 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.775). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-21.2, -34.6); signed map (-6.9, -46.5). **Vector** length 81.9, 26.9% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA processing in the nucleus* (reactome, mean cos +0.53 to 8); *Metabolism of non-coding RNA* (reactome, mean cos +0.51 to 7); *snRNP Assembly* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +3.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.5 | +4.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.1 | -0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.8 | +4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +4.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.1 | +3.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.6 | -0.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.7 | -0.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.5 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.7 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | -1.8 | -1.1 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.8 | +0.0 |
|  | [[NVP-BHG712 (drug)]] 0.5 µM |  | -1.7 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | complement C1q binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:5,432,777-5,448,830 (-) |
| Ensembl biotype | protein_coding |
| Also known as | gC1Q-R, gC1qR, p32, SF2p32; previously HABP1 |
| Gene groups (HGNC) | MIER complex subunits |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 14 pathways, smallest: Regulation of FXIIa and plasma kallikrein activity; FXIIa activates plasma kallikrein-kinin system; Apoptotic factor-mediated response |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07021](https://www.uniprot.org/uniprotkb/Q07021) (Complement component 1 Q subcomponent-binding protein, mitochondrial):

> Multifunctional and multicompartmental protein involved in inflammation and infection processes, ribosome biogenesis, protein synthesis in mitochondria, regulation of apoptosis, transcriptional regulation and pre-mRNA splicing. At the cell surface is thought to act as an endothelial receptor for plasma proteins of the complement and kallikrein-kinin cascades. Putative receptor for C1q; specifically binds to the globular 'heads' of C1q thus inhibiting C1; may perform the receptor function …

**Summary**, from NCBI Gene [708](https://www.ncbi.nlm.nih.gov/gene/708):

> The human complement subcomponent C1q associates with C1r and C1s in order to yield the first component of the serum complement system. The protein encoded by this gene is known to bind to the globular heads of C1q molecules and inhibit C1 activation. This protein has also been identified as the p32 subunit of pre-mRNA splicing factor SF2, as well as a hyaluronic acid-binding protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1243](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1243) · Entrez [708](https://www.ncbi.nlm.nih.gov/gene/708) · UniProt [Q07021](https://www.uniprot.org/uniprotkb/Q07021) · Ensembl [ENSG00000108561](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108561)

## Data

Gene col 2967: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2967); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2967, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2967]; `tensor/DDL_lfc|DDL_z.npy` [2967]; `embed/gene_vectors.npy` [2967]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2967 or target_col == 2967). Every well: [[C1QBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1QBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
