---
symbol: "MAP1B"
type: "gene"
col: 5234
ensembl_id: "ENSG00000131711"
name: "microtubule associated protein 1B"
location: "5q13.2"
module: 136
arm: "+"
pooled_cpm: 362.1
n_lines_expressing: 34
n_dd_up: 34
n_dd_down: 32
n_dd_up_clean: 25
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 4
direction_downstream: 11
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# MAP1B

*microtubule associated protein 1B* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (9 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.40× (z +17.0, q 0e+00, up in 32 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.490× (z -19.6, q 0e+00, down in 28 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SH3KBP1]] (+0.66, fdr 7e-06), [[CTNNA1]] (+0.66, fdr 7e-06), [[MAP4]] (+0.65, fdr 7e-06); moves opposite to [[SELENOH]] (-0.51, fdr 5e-05), [[POLR1H]] (-0.50, fdr 9e-05), [[PPM1D]] (-0.50, fdr 5e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[SACS]] → it (grade B ⚠); 11 go from it, the strongest it → [[DST]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 61 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5234.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.40×** | +17.0 | 0e+00 | 32/32 (NCI-H460, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.35×** | +16.6 | 0e+00 | 30/33 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +14.7 | 0e+00 | 29/30 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.05×** | +14.0 | 4e-42 | 32/32 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.03×** | +13.0 | 8e-37 | 31/32 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.86×** | +12.1 | 8e-32 | 32/32 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.95×** | +12.0 | 2e-31 | 26/30 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.57×** | +8.8 | 7e-17 | 30/31 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +8.6 | 5e-16 | 27/32 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.55×** | +8.3 | 8e-15 | 30/31 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.53×** | +7.9 | 1e-13 | 24/31 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.50×** | +7.9 | 1e-13 | 28/32 (NCI-H460, C-33 A, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.47×** | +7.5 | 2e-12 | 27/32 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.31×** | +7.5 | 4e-12 | 20/33 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.42×** | +6.9 | 2e-10 | 23/31 (SW 900, NCI-H2030, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Artesunate (drug)]] 5 µM |  | **1.25×** | +6.1 | 3e-08 | 19/32 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.37×** | +6.1 | 3e-08 | 23/32 (NCI-H460, C-33 A, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.37×** | +6.1 | 3e-08 | 24/31 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.32×** | +5.4 | 2e-06 | 21/32 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.31×** | +5.2 | 5e-06 | 19/32 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.28×** | +4.8 | 3e-05 | 19/32 (NCI-H1792, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5234.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.490×** | -19.6 | 0e+00 | 28/32 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.565×** | -15.7 | 0e+00 | 26/33 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.556×** | -11.0 | 1e-25 | 27/31 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.579×** | -10.6 | 3e-24 | 26/32 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.582×** | -10.5 | 8e-24 | 29/32 (PANC-1, SW 1088, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.595×** | -9.7 | 3e-20 | 26/32 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.620×** | -9.3 | 1e-18 | 22/32 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.651×** | -8.3 | 6e-15 | 26/32 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.654×** | -8.2 | 1e-14 | 23/32 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.472×** | -7.6 | 1e-12 | 30/33 (A-427, H4, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.679×** | -7.5 | 3e-12 | 24/32 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.697×** | -7.0 | 1e-10 | 23/32 (CHP-212, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.707×** | -6.7 | 7e-10 | 18/32 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.717×** | -6.5 | 4e-09 | 25/32 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -6.0 | 8e-08 | 20/32 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.809×** | -5.8 | 2e-07 | 20/32 (A-427, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.749×** | -5.6 | 6e-07 | 22/32 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5234. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 355 | 22 (7 ⚠) | 8 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.42× (z +19.0) | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -21.6) |
| [[PANC-1 (line)]] | alt | 560 | 7 (2 ⚠) | 17 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.13× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -28.7) |
| [[SW 900 (line)]] | alt | 585 | 10 (3 ⚠) | 10 | [[Auranofin (drug)]] 5 µM 3.24× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -14.8) |
| [[A-427 (line)]] | wt | 472 | 6 (2 ⚠) | 11 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.14× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -24.4) |
| [[A-172 (line)]] | wt | 1,361 | 1 | 14 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.02× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.249× (z -17.8) |
| [[BT-474 (line)]] | alt | 132 | 9 (2 ⚠) | 5 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 5.77× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -10.7) |
| [[SW480 (line)]] | alt | 183 | 12 (6 ⚠) | 2 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.63× (z +18.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.393× (z -11.4) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.422× (z -10.6) |
| [[HS-578T (line)]] | alt | 839 | 4 (3 ⚠) | 9 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.98× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -16.3) |
| [[HepG2_C3A (line)]] | wt | 259 | 11 (5 ⚠) | 1 | [[Daptomycin (drug)]] 5 µM 3.45× (z +13.1) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.31× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -11.0) |
| [[A549 (line)]] | wt | 478 | 8 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 6.01× (z +24.8) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.30× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -14.5) |
| [[LOX-IMVI (line)]] | wt | 378 | 6 (2 ⚠) | 4 | [[Ixazomib citrate (drug)]] 0.5 µM 2.76× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -19.3) |
| [[SNU-423 (line)]] | alt | 312 | 10 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.71× (z +15.2) | — |
| [[C32 (line)]] | wt | 282 | 3 | 6 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.80× (z +14.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -15.4) |
| [[J82 (line)]] | alt | 669 | 4 (3 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.05× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.422× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.439× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 602 | 7 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +16.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.46× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -23.4) |
| [[NCI-H23 (line)]] | alt | 135 | 7 (2 ⚠) | 2 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.40× (z +14.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.358× (z -9.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.543× (z -8.6) |
| [[SHP-77 (line)]] | alt | 884 | 6 (3 ⚠) | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.40× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -16.3) |
| [[A498 (line)]] | wt | 870 | 4 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +17.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.54× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -14.2) |
| [[NCI-H2347 (line)]] | alt | 540 | 6 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.24× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -14.3) |
| [[C-33 A (line)]] | alt | 239 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 2.39× (z +9.5) | — |
| [[H4 (line)]] | wt | 774 | 1 | 6 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.73× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -21.2) |
| [[RPMI-7951 (line)]] | alt | 348 | 2 | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.60× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -11.5) |
| [[HOP62 (line)]] | alt | 752 | 2 (1 ⚠) | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.61× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 625 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.19× (z +12.5) | — |
| [[NCI-H2030 (line)]] | alt | 339 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.23× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -22.9) |
| [[CFPAC-1 (line)]] | alt | 602 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.84× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -10.1) |
| [[SW 1088 (line)]] | alt | 1,100 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0931× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.283× (z -11.4) |
| [[CHP-212 (line)]] | wt | 966 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.280× (z -12.5) |
| [[AN3 CA (line)]] | alt | 440 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -11.6) |
| [[NCI-H661 (line)]] | alt | 209 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 106 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.389× (z -9.9) |
| [[SW 1271 (line)]] | alt | 546 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.63× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 28.0 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 25.2 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 28.4 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 26.1 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 80.9 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 29.5 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 23.5 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 24.0 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 24.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.8 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 59.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.3 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 27.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 28.3 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 49.4 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 35.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5234), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SH3KBP1]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[CTNNA1]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[MAP4]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 | STRING 570 |
| [[AAK1]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[MYO5A]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[MSN]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[GTPBP2]] | +0.61 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[POPDC3]] | +0.60 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[DYNC1H1]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[RTN4]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[PSMD2]] | +0.58 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[ARPC5]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SELENOH]] | -0.51 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[POLR1H]] | -0.50 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[PPM1D]] | -0.50 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[FBXL5]] | -0.49 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[PER1]] | -0.49 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[PPP4R3A]] | -0.48 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[YY1AP1]] | -0.48 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[MAP3K1]] | -0.48 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[YAP1]] | -0.48 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[FMC1]] | -0.47 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[MAML1]] | -0.47 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[RCHY1]] | -0.46 | -0.36 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SACS]] | B | SACS activity raises MAP1B's level | lines that do not express SACS (5) vs lines expressing it (45) | 5.12× lower at baseline in the lines without SACS | 0.080 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[MLLT11]] | C | MLLT11 activity raises MAP1B's level | lines that do not express MLLT11 (21) vs lines expressing it (29) | 7.10× lower at baseline in the lines without MLLT11 | 0.029 | ⚠ within organs, on part of the lines; also absent: DZIP1, ADAMTS18, KCNJ6; maybe low, not absent; co-absent with the target |
| [[POPDC3]] | C | POPDC3 activity raises MAP1B's level | lines that do not express POPDC3 (18) vs lines expressing it (32) | 5.52× lower at baseline in the lines without POPDC3 | 0.032 | ⚠ within organs, on part of the lines; also absent: WIPF1, WDR17, BVES-AS1; co-absent with the target |
| [[TTLL7]] | C | TTLL7 activity raises MAP1B's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 6.12× lower at baseline in the lines without TTLL7 | 0.069 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 5, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DST]] | B | MAP1B activity raises DST's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 2.26× lower at baseline in the lines without MAP1B | 0.007 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL |
| [[NRSN2]] | B | MAP1B activity raises NRSN2's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 2.78× lower at baseline in the lines without MAP1B | 0.012 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL |
| [[NXPE3]] | B | MAP1B activity raises NXPE3's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 2.35× lower at baseline in the lines without MAP1B | 0.021 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL |
| [[TXNRD1]] | B | MAP1B activity lowers TXNRD1's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 1.51× higher at baseline in the lines without MAP1B | 0.055 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL |
| [[LARP6]] | B | MAP1B activity raises LARP6's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 2.78× lower at baseline in the lines without MAP1B | 0.088 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL |
| [[TTLL7]] | C | MAP1B activity raises TTLL7's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 5.12× lower at baseline in the lines without MAP1B | 0.003 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL; co-absent with the target |
| [[POPDC3]] | C | MAP1B activity raises POPDC3's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 4.65× lower at baseline in the lines without MAP1B | 0.012 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL; co-absent with the target |
| [[UCHL1]] | C | MAP1B activity raises UCHL1's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 6.26× lower at baseline in the lines without MAP1B | 0.013 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL; co-absent with the target |
| [[TUBA1A]] | C | MAP1B activity raises TUBA1A's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 5.04× lower at baseline in the lines without MAP1B | 0.018 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL; co-absent with the target |
| [[MLLT11]] | C | MAP1B activity raises MLLT11's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 3.58× lower at baseline in the lines without MAP1B | 0.019 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL; co-absent with the target |
| [[B4GALNT1]] | C | MAP1B activity raises B4GALNT1's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 3.14× lower at baseline in the lines without MAP1B | 0.036 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL; co-absent with the target |

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.393). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.7, 42.4); signed map (-9.2, 24.1). **Vector** length 141, 46.3% of its response variance represented; |z| ≥ 3 in 1,860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.9 | +17.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +10.9 | +12.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.6 | +14.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.7 | +13.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +7.0 | +7.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.2 | +8.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.1 | -11.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.5 | -10.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -5.1 | -4.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.2 | -4.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.0 | -7.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.6 | -3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.4 | -3.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -3.2 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated protein 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:72,107,234-72,209,565 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAP5, PPP1R102 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 3 pathways, smallest: RSV-host interactions; Respiratory Syncytial Virus Infection Pathway; Viral Infection Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [P46821](https://www.uniprot.org/uniprotkb/P46821) (Microtubule-associated protein 1B):

> Facilitates tyrosination of alpha-tubulin in neuronal microtubules (By similarity). Phosphorylated MAP1B is required for proper microtubule dynamics and plays a role in the cytoskeletal changes that accompany neuronal differentiation and neurite extension. Possibly MAP1B binds to at least two tubulin subunits in the polymer, and this bridging of subunits might be involved in nucleating microtubule polymerization and in stabilizing microtubules. Acts as a positive cofactor in DAPK1-mediated …

**Summary**, from NCBI Gene [4131](https://www.ncbi.nlm.nih.gov/gene/4131):

> This gene encodes a protein that belongs to the microtubule-associated protein family. The proteins of this family are thought to be involved in microtubule assembly, which is an essential step in neurogenesis. The product of this gene is a precursor polypeptide that presumably undergoes proteolytic processing to generate the final MAP1B heavy chain and LC1 light chain. Gene knockout studies of the mouse microtubule-associated protein 1B gene suggested an important role in development and …

**Accessions** — [HGNC:6836](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6836) · Entrez [4131](https://www.ncbi.nlm.nih.gov/gene/4131) · UniProt [P46821](https://www.uniprot.org/uniprotkb/P46821) · Ensembl [ENSG00000131711](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131711)

## Data

Gene col 5234: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5234); `tables/drug_effects.parquet` (108 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5234, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5234]; `tensor/DDL_lfc|DDL_z.npy` [5234]; `embed/gene_vectors.npy` [5234]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5234 or target_col == 5234). Every well: [[MAP1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
