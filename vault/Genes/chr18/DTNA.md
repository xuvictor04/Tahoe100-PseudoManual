---
symbol: "DTNA"
type: "gene"
col: 5602
ensembl_id: "ENSG00000134769"
name: "dystrobrevin alpha"
location: "18q12.1"
module: 154
arm: "+"
pooled_cpm: 222.93
n_lines_expressing: 28
n_dd_up: 24
n_dd_down: 56
n_dd_up_clean: 20
n_dd_down_clean: 40
in_vector_space: true
direction_upstream: 4
direction_downstream: 10
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# DTNA

*dystrobrevin alpha* — 18q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (4 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.95× (z +13.2, q 8e-37, up in 24 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 56 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.302× (z -23.5, q 0e+00, down in 26 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP2R5B]] (+0.66, fdr 1e-05), [[MPP2]] (+0.66, fdr 1e-05), [[FGFR1]] (+0.65, fdr 1e-05); moves opposite to [[SOCS6]] (-0.51, fdr 8e-05), [[TNRC18]] (-0.50, fdr 5e-05), [[RPRD1B]] (-0.49, fdr 4e-04).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAST4]] → it (grade B ⚠); 10 go from it, the strongest it → [[CRYBG3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5602.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.95×** | +13.2 | 8e-37 | 24/27 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **2.24×** | +11.2 | 1e-26 | 24/26 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.98×** | +9.2 | 1e-17 | 21/25 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +8.6 | 8e-16 | 18/26 (NCI-H23, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.80×** | +8.2 | 3e-14 | 20/26 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.71×** | +7.5 | 7e-12 | 19/26 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only; position correction uncertain | **1.70×** | +7.3 | 2e-11 | 21/25 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.95×** | +7.3 | 3e-11 | 19/27 (NCI-H460, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **2.76×** | +6.8 | 7e-10 | 23/26 (SHP-77, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +6.3 | 1e-08 | 17/27 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.45×** | +5.1 | 1e-05 | 16/25 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.59×** | +4.5 | 3e-04 | 14/26 (NCI-H1573, C32, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.39×** | +4.4 | 4e-04 | 15/26 (BT-474, NCI-H23, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **1.86×** | +4.2 | 0.001 | 16/24 (NCI-H1573, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.50×** | +3.9 | 0.003 | 16/26 (NCI-H460, NCI-H1573, …) | two highest doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.4 | 0.024 | 13/25 (NCI-H460, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.035 | 10/27 (NCI-H1573, NCI-H1792, …) | top dose only | plate-row cell shift |
| [[vincristine (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.040 | 13/26 (BT-474, SK-MEL-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 56 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5602.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.302×** | -23.5 | 0e+00 | 26/27 (J82, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.311×** | -16.2 | 0e+00 | 23/27 (SHP-77, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **0.467×** | -14.9 | 0e+00 | 18/26 (LOX-IMVI, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.347×** | -14.1 | 4e-43 | 20/24 (A-427, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.369×** | -13.3 | 2e-38 | 23/25 (J82, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.376×** | -13.1 | 5e-37 | 25/25 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.529×** | -12.5 | 7e-34 | 23/26 (J82, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ position correction uncertain | **0.440×** | -11.4 | 4e-28 | 21/26 (LOX-IMVI, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM | ⚠ position correction uncertain | **0.532×** | -8.7 | 1e-16 | 24/26 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.545×** | -8.4 | 2e-15 | 24/26 (CFPAC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.581×** | -7.2 | 2e-11 | 21/26 (NCI-H23, HS-578T, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[NG25 (drug)]] 5 µM |  | **0.388×** | -6.3 | 1e-08 | 16/25 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.634×** | -6.1 | 6e-08 | 14/26 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 5 µM | ⚠ position correction uncertain | **0.660×** | -5.8 | 3e-07 | 19/26 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -5.7 | 4e-07 | 21/28 (LOX-IMVI, A-427, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.670×** | -5.6 | 9e-07 | 16/26 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.688×** | -5.2 | 6e-06 | 18/26 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.711×** | -4.7 | 6e-05 | 15/26 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.692×** | -4.7 | 6e-05 | 16/25 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.782×** | -4.7 | 6e-05 | 18/27 (C32, HOP62, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.736×** | -4.3 | 5e-04 | 14/26 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.743×** | -4.1 | 8e-04 | 15/26 (HS-578T, BT-474, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.813×** | -4.1 | 0.001 | 11/26 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5602. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 1,883 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0583× (z -27.7) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -22.0) |
| [[NCI-H1573 (line)]] | alt | 321 | 5 (2 ⚠) | 8 (7 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 6.24× (z +19.1) | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -18.5) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 1,020 | 2 | 10 (7 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.24× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0595× (z -24.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -21.3) |
| [[HOP62 (line)]] | alt | 563 | 0 | 12 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -16.5) |
| [[NCI-H2347 (line)]] | alt | 592 | 2 (2 ⚠) | 9 (5 ⚠) | [[Daptomycin (drug)]] 5 µM 2.80× (z +9.6) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.5 µM 0.0913× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -19.3) |
| [[SHP-77 (line)]] | alt | 803 | 2 | 7 (6 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.77× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -25.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -19.8) |
| [[C32 (line)]] | wt | 125 | 3 | 5 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.70× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -16.9) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -14.5) |
| [[J82 (line)]] | alt | 444 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -22.3) |
| [[Panc 03.27 (line)]] | alt | 120 | 5 (2 ⚠) | 3 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 3.05× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 467 | 2 (1 ⚠) | 5 (3 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.50× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.100× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 241 | 1 (1 ⚠) | 6 (5 ⚠) | [[Daptomycin (drug)]] 5 µM 2.66× (z +8.5) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -22.0) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -21.2) |
| [[NCI-H23 (line)]] | alt | 76.2 | 4 (1 ⚠) | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.44× (z +14.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -15.0) |
| [[SNU-423 (line)]] | alt | 193 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -20.0) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -18.6) |
| [[A-427 (line)]] | wt | 470 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +13.8) ⚠ position correction uncertain | [[Dinaciclib (drug)]] 5 µM 0.0631× (z -28.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 179 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.39× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -17.0) |
| [[CHP-212 (line)]] | wt | 447 | 1 | 4 (3 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.67× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -14.7) |
| [[HS-578T (line)]] | alt | 141 | 1 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.30× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -17.5) |
| [[SK-MEL-2 (line)]] | alt | 93.2 | 2 | 3 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.11× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -11.7) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -8.9) |
| [[A-172 (line)]] | wt | 192 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +11.8) ⚠ position correction uncertain | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -12.0) |
| [[BT-474 (line)]] | alt | 656 | 2 | 2 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.83× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -17.6) |
| [[RPMI-7951 (line)]] | alt | 83.7 | 1 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.30× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -16.4) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -13.4) |
| [[hTERT-HPNE (line)]] | wt | 118 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -17.5) |
| [[SW 1271 (line)]] | alt | 368 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -12.4) |
| [[SW 900 (line)]] | alt | 122 | 1 | 2 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.30× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -10.9) |
| [[H4 (line)]] | wt | 378 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.200× (z -9.9) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 141 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.5 µM 0.0475× (z -10.5) |
| [[A498 (line)]] | wt | 17.2 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 49.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 41.4 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 19.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 22.2 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 25.9 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 43.3 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 24.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 23.1 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 15.9 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 15.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 16.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 27.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 335 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 317 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.9 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 17.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 19.2 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 18.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 21.7 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 18.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5602), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP2R5B]] | +0.66 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[MPP2]] | +0.66 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[FGFR1]] | +0.65 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[NGLY1]] | +0.63 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[SH3GL3]] | +0.62 | +0.66 / +0.43 | both halves | 3e-05 |  |
| [[PKIA]] | +0.60 | +0.51 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_MYOGENESIS |
| [[SMS]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[UBA6]] | +0.59 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[KHDRBS3]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[TMCC3]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[UPRT]] | +0.57 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[JAKMIP1]] | +0.57 | +0.39 / +0.47 | both halves | 5e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOCS6]] | -0.51 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[TNRC18]] | -0.50 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[RPRD1B]] | -0.49 | -0.26 / -0.36 | both halves | 4e-04 |  |
| [[SPART-AS1]] | -0.47 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[ADI1]] | -0.47 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[HECTD1]] | -0.47 | -0.46 / -0.37 | both halves | 7e-05 |  |
| [[FOXG1]] | -0.46 | -0.49 / -0.21 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAST4]] | B | MAST4 activity raises DTNA's level | lines that do not express MAST4 (11) vs lines expressing it (39) | 2.63× lower at baseline in the lines without MAST4 | 0.039 | ⚠ within organs, on part of the lines; also absent: TSPAN12, AHR, TLE4; maybe low, not absent |
| [[NOL4]] | C | NOL4 activity raises DTNA's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 6.06× lower at baseline in the lines without NOL4 | 0.025 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent; co-absent with the target |
| [[PKIA]] | C | PKIA activity raises DTNA's level | lines that do not express PKIA (22) vs lines expressing it (28) | 4.55× lower at baseline in the lines without PKIA | 0.056 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4; co-absent with the target |
| [[CRYBG3]] | C | CRYBG3 activity raises DTNA's level | lines that do not express CRYBG3 (3) vs lines expressing it (47) | 4.36× lower at baseline in the lines without CRYBG3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPR137B, PAM, DTX3L; its own permutation p |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRYBG3]] | B | DTNA activity raises CRYBG3's level | lines that do not express DTNA (22) vs lines expressing it (28) | 1.75× lower at baseline in the lines without DTNA | 0.007 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, MMP16, ENSG00000253553 |
| [[PAM]] | B | DTNA activity raises PAM's level | lines that do not express DTNA (22) vs lines expressing it (28) | 1.48× lower at baseline in the lines without DTNA | 0.007 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, MMP16, ENSG00000253553 |
| [[PPP2R3A]] | B | DTNA activity raises PPP2R3A's level | lines that do not express DTNA (22) vs lines expressing it (28) | 1.96× lower at baseline in the lines without DTNA | 0.041 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, MMP16, ENSG00000253553 |
| [[CFAP20DC]] | B | DTNA activity raises CFAP20DC's level | lines that do not express DTNA (22) vs lines expressing it (28) | 3.73× lower at baseline in the lines without DTNA | 0.053 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, MMP16, ENSG00000253553 |
| [[FAM162A]] | B | DTNA activity raises FAM162A's level | lines that do not express DTNA (22) vs lines expressing it (28) | 1.47× lower at baseline in the lines without DTNA | 0.060 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, MMP16, ENSG00000253553 |
| [[ARID5A]] | B | DTNA activity raises ARID5A's level | lines that do not express DTNA (22) vs lines expressing it (28) | 1.52× lower at baseline in the lines without DTNA | 0.072 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, MMP16, ENSG00000253553 |
| [[GLUL]] | B | DTNA activity raises GLUL's level | lines that do not express DTNA (22) vs lines expressing it (28) | 1.89× lower at baseline in the lines without DTNA | 0.088 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, MMP16, ENSG00000253553 |
| [[CAMK4]] | C | DTNA activity raises CAMK4's level | lines that do not express DTNA (22) vs lines expressing it (28) | 5.64× lower at baseline in the lines without DTNA | 0.026 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, MMP16, ENSG00000253553; co-absent with the target |
| [[PKIA]] | C | DTNA activity raises PKIA's level | lines that do not express DTNA (22) vs lines expressing it (28) | 3.86× lower at baseline in the lines without DTNA | 0.067 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, MMP16, ENSG00000253553; co-absent with the target |
| [[MME]] | C | DTNA activity raises MME's level | lines that do not express DTNA (22) vs lines expressing it (28) | 6.06× lower at baseline in the lines without DTNA | 0.093 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, MMP16, ENSG00000253553; co-absent with the target |

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.692). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.1, -2.7); signed map (-5.9, 48.3). **Vector** length 124, 39.2% of its response variance represented; |z| ≥ 3 in 1,207 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.4 | +8.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.9 | +6.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | -16.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | -5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | -14.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.5 | +13.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.2 | +9.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.5 | +8.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +4.1 | +4.5 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.4 | -12.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.3 | -1.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM | ⚠ position correction uncertain | -4.0 | -5.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | +1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.4 | -3.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM | ⚠ position correction uncertain | -3.3 | -8.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.9 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | dystrobrevin alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.1 — chr18:34,493,291-34,891,844 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D18S892E, DTN, DTN-1, DTN-2, DTN-3, DRP3 |
| Gene groups (HGNC) | Zinc fingers ZZ-type |
| Hallmark sets | MYOGENESIS, HYPOXIA |
| Reactome | 3 pathways, smallest: Formation of the dystrophin-glycoprotein complex (DGC); Non-integrin membrane-ECM interactions; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4J8](https://www.uniprot.org/uniprotkb/Q9Y4J8) (Dystrobrevin alpha):

> May be involved in the formation and stability of synapses as well as being involved in the clustering of nicotinic acetylcholine receptors.

**Summary**, from NCBI Gene [1837](https://www.ncbi.nlm.nih.gov/gene/1837):

> The protein encoded by this gene belongs to the dystrobrevin subfamily of the dystrophin family. This protein is a component of the dystrophin-associated protein complex (DPC), which consists of dystrophin and several integral and peripheral membrane proteins, including dystroglycans, sarcoglycans, syntrophins and alpha- and beta-dystrobrevin. The DPC localizes to the sarcolemma and its disruption is associated with various forms of muscular dystrophy. Mutations in this gene are associated with …

**Accessions** — [HGNC:3057](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3057) · Entrez [1837](https://www.ncbi.nlm.nih.gov/gene/1837) · UniProt [Q9Y4J8](https://www.uniprot.org/uniprotkb/Q9Y4J8) · Ensembl [ENSG00000134769](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134769)

## Data

Gene col 5602: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5602); `tables/drug_effects.parquet` (85 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5602, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5602]; `tensor/DDL_lfc|DDL_z.npy` [5602]; `embed/gene_vectors.npy` [5602]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5602 or target_col == 5602). Every well: [[DTNA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DTNA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
