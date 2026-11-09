---
symbol: "FBXW7"
type: "gene"
col: 3069
ensembl_id: "ENSG00000109670"
name: "F-box and WD repeat domain containing 7"
location: "4q31.3"
module: 17
arm: "-"
pooled_cpm: 245.83
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# FBXW7

*F-box and WD repeat domain containing 7* — 4q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.65× (z +12.3, q 5e-32, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.431× (z -19.9, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (LS 180 0.128×, SK-MEL-2 0.270×, LoVo 0.272×, A-172 0.254×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-427 0.285×, hTERT-HPNE 0.217×, HT-29 0.298×, SW480 0.371×, …; ⚠ toxic; transcription drop); [[AZD-7648 (drug)]] 5 µM in 1 line (CHP-212 0.0541×); [[Radotinib (drug)]] 5 µM in 1 line (AsPC-1 0.593×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COP1]] (+0.64, fdr 7e-06), [[LMBR1]] (+0.64, fdr 7e-06), [[SENP5]] (+0.63, fdr 1e-05); moves opposite to [[KPNA5]] (-0.65, fdr 7e-06), [[ZSCAN12]] (-0.62, fdr 1e-05), [[ZSCAN26]] (-0.59, fdr 1e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ENSG00000268833]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3069.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +12.3 | 5e-32 | 45/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.61×** | +11.7 | 6e-29 | 45/48 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.37×** | +11.0 | 4e-26 | 35/49 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +11.0 | 9e-26 | 40/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.53×** | +10.1 | 9e-22 | 35/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +8.7 | 3e-16 | 32/47 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +8.4 | 4e-15 | 36/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.96×** | +7.8 | 6e-13 | 38/49 (NCI-H460, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +7.7 | 1e-12 | 41/48 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +7.6 | 1e-12 | 37/48 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.36×** | +7.6 | 2e-12 | 32/48 (A-172, SNU-423, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +7.1 | 7e-11 | 25/48 (HOP62, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +6.9 | 3e-10 | 31/48 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +6.8 | 5e-10 | 32/48 (Hs 766T, NCI-H460, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.32×** | +6.5 | 3e-09 | 32/50 (NCI-H460, H4, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +5.4 | 2e-06 | 32/48 (C32, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.20× | +4.4 | 3e-04 | 24/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.18× | +4.1 | 0.001 | 16/48 (NCI-H460, C32, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.029 | 22/48 (SW480, COLO 205, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3069.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 10 lines (LS 180 0.128×, SK-MEL-2 0.270×, LoVo 0.272×, A-172 0.254×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A-427 0.285×, hTERT-HPNE 0.217×, HT-29 0.298×, SW480 0.371×, …; ⚠ toxic; transcription drop); [[AZD-7648 (drug)]] 5 µM in 1 line (CHP-212 0.0541×); [[Radotinib (drug)]] 5 µM in 1 line (AsPC-1 0.593×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.431×** | -19.9 | 0e+00 | 43/44 (LS 180, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.500×** | -17.1 | 0e+00 | 47/49 (A-427, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.635×** | -10.4 | 7e-23 | 35/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.712×** | -8.4 | 8e-15 | 40/48 (KATO III, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.853× | -5.6 | 3e-06 | 17/48 (AsPC-1, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.871× | -4.8 | 1e-04 | 14/48 (NCI-H1573, SHP-77, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.826×** | -4.7 | 2e-04 | 25/49 (NCI-H1573, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.854× | -3.9 | 0.006 | 20/48 (KATO III, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.848× | -3.9 | 0.006 | 20/47 (NCI-H2030, SW1417, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.856× | -3.9 | 0.006 | 18/48 (LoVo, HS-578T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.872× | -3.4 | 0.034 | 16/48 (A-427, LoVo, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | 0.898× | -3.3 | 0.040 | 8/49 (Hs 766T, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.881× | -3.2 | 0.070 | 10/48 (KATO III, SW 1088, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.882× | -3.0 | 0.11 | 12/48 (SK-MEL-2, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3069. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 204 | 12 (7 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +16.7) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.391× (z -16.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 278 | 6 (4 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +11.9) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.305× (z -14.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 206 | 6 (4 ⚠) | 3 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.27× (z +12.5) ⚠ toxic · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.62× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.513× (z -10.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 156 | 7 (3 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +20.4) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.06× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.469× (z -10.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 207 | 7 (5 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.93× (z +13.5) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +13.2) | [[Docetaxel (drug)]] 0.05 µM 0.423× (z -10.8) ⚠ transcription drop |
| [[SNU-1 (line)]] | wt | 233 | 7 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -13.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 218 | 5 (3 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +14.4) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.00× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -14.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 334 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.54× (z +13.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +12.0) | — |
| [[A-172 (line)]] | wt | 207 | 3 (2 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +12.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.27× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -18.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 167 | 3 (1 ⚠) | 3 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.87× (z +9.4) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 1.80× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.384× (z -14.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 404 | 1 | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -19.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 317 | 3 (1 ⚠) | 3 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.82× (z +9.6) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 3.38× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -16.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 246 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 5.91× (z +10.2) | — |
| [[KATO III (line)]] | alt | 280 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 293 | 1 | 4 (4 ⚠) | [[Belinostat (drug)]] 5 µM 1.78× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.287× (z -17.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 176 | 3 (2 ⚠) | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 1.70× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.528× (z -11.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 237 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.27× (z +11.1) | — |
| [[A-427 (line)]] | wt | 237 | 2 | 2 (2 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.52× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -21.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 234 | 1 | 3 (3 ⚠) | [[Belinostat (drug)]] 5 µM 1.62× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.434× (z -14.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 338 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -16.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 258 | 1 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +8.7) ⚠ cell-cycle shift, explains ~23% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -19.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 239 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -16.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 536 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -23.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 298 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.50× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -19.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 125 | 3 (2 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.41× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.508× (z -8.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 408 | 0 | 3 (2 ⚠) | — | [[Radotinib (drug)]] 5 µM 0.593× (z -9.9) |
| [[C-33 A (line)]] | alt | 277 | 1 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 1.85× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.413× (z -12.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 308 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -14.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 177 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.448× (z -10.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 160 | 1 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +11.3) ⚠ cell-cycle shift, explains ~23% of this change | [[Dinaciclib (drug)]] 5 µM 0.262× (z -17.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 274 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[AZD-7648 (drug)]] 5 µM 0.0541× (z -12.7) |
| [[HCT15 (line)]] | alt | 245 | 1 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 1.98× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -12.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 231 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +11.2) ⚠ cell-cycle shift, explains ~23% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 134 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +8.8) ⚠ cell-cycle shift, explains ~23% of this change | [[Dinaciclib (drug)]] 5 µM 0.295× (z -16.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 211 | 1 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 1.95× (z +8.9) | [[Docetaxel (drug)]] 0.05 µM 0.510× (z -9.0) ⚠ transcription drop |
| [[SW1417 (line)]] | alt | 293 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.432× (z -12.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 270 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.397× (z -11.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 214 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -17.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 305 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.97× (z +8.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1573 (line)]] | alt | 325 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.585× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 155 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.325× (z -14.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 193 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.500× (z -8.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 219 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 189 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3069), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COP1]] | +0.64 | +0.64 / +0.65 | both halves | 7e-06 | same gene group; pathway: Neddylation |
| [[LMBR1]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[SENP5]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SNTB2]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ANKS1A]] | +0.60 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CSNK1G2]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[PITPNA]] | +0.59 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ARPC5L]] | +0.58 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[TBC1D2]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 | same gene group |
| [[HDAC4]] | +0.55 | +0.49 / +0.58 | both halves | 1e-05 | same gene group; pathway: Constitutive Signaling by NOTCH1 HD+PEST Domain Mutants; STRING 441 |
| [[RAB5IF]] | +0.55 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[PDCD6]] | +0.55 | +0.43 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA5]] | -0.65 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[ZSCAN12]] | -0.62 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[ZSCAN26]] | -0.59 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[ZDHHC17]] | -0.58 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[SUGT1P3]] | -0.58 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[CFL2]] | -0.58 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[NBN]] | -0.57 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[TAB2]] | -0.56 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[MKS1]] | -0.56 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[NDUFA5]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CLK4]] | -0.55 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[TCEANC]] | -0.55 | -0.51 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FBXW7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CCDC102A]] | B | CCDC102A activity lowers FBXW7's level | lines that do not express CCDC102A (5) vs lines expressing it (45) | 1.49× higher at baseline in the lines without CCDC102A | 0.057 | ⚠ within organs, on part of the lines; also absent: CYP46A1, TMOD2, DPF1; maybe low, not absent |
| [[CFL2]] | C | CFL2 activity lowers FBXW7's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.73× higher at baseline in the lines without CFL2 | 0.089 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENSG00000268833]] | C | FBXW7 activity lowers ENSG00000268833's level | recorded loss-of-function mutation of FBXW7 in 5 lines vs 45 not recorded | 3.43× higher at baseline in the FBXW7-altered lines | 0.336 over the table, 0.073 within its group | ⚠ within its group only (a lead); within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.532). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-21.8, 2.3); signed map (-46.9, 0.3). **Vector** length 122, 45.1% of its response variance represented; |z| ≥ 3 in 1,467 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +8.4 | +10.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +8.2 | +6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +6.4 | +11.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.7 | +8.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.6 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +7.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.4 | +1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +3.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -10.6 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -10.2 | -1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.5 | -1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.8 | -3.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -6.8 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.7 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -4.8 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -3.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | F-box and WD repeat domain containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.3 — chr4:152,320,544-152,536,092 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AGO, FLJ11071, SEL-10, SEL10, FBW7, FBX30, CDC4, FBXW6 |
| Gene groups (HGNC) | WD repeat domain containing; F-box and WD repeat domain containing; E3 ubiquitin ligases; MicroRNA protein coding host genes |
| Hallmark sets | P53_PATHWAY |
| Reactome | 20 pathways, smallest: FBXW7 Mutants and NOTCH1 in Cancer; Loss of Function of FBXW7 in Cancer and NOTCH1 Signaling; Association of TriC/CCT with target proteins during biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969H0](https://www.uniprot.org/uniprotkb/Q969H0) (F-box/WD repeat-containing protein 7):

> Substrate recognition component of a SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Recognizes and binds phosphorylated sites/phosphodegrons within target proteins and thereafter brings them to the SCF complex for ubiquitination. Identified substrates include cyclin-E (CCNE1 or CCNE2), DISC1, JUN, MYC, NOTCH1 released notch intracellular domain (NICD), NFE2L1, NOTCH2, MCL1, MLST8, …

**Summary**, from NCBI Gene [55294](https://www.ncbi.nlm.nih.gov/gene/55294):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:16712](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16712) · Entrez [55294](https://www.ncbi.nlm.nih.gov/gene/55294) · UniProt [Q969H0](https://www.uniprot.org/uniprotkb/Q969H0) · Ensembl [ENSG00000109670](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109670)

## Data

Gene col 3069: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3069); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3069, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3069]; `tensor/DDL_lfc|DDL_z.npy` [3069]; `embed/gene_vectors.npy` [3069]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3069 or target_col == 3069). Every well: [[FBXW7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXW7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
