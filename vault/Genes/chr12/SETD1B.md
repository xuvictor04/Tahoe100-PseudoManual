---
symbol: "SETD1B"
type: "gene"
col: 6337
ensembl_id: "ENSG00000139718"
name: "SET domain containing 1B, histone lysine methyltransferase"
location: "12q24.31"
module: 46
arm: "+"
pooled_cpm: 27.47
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 13
n_dd_up_clean: 12
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# SETD1B

*SET domain containing 1B, histone lysine methyltransferase* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.87× (z +24.9, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.204× (z -26.5, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRD1]] (+0.76, fdr 7e-06), [[PHF2]] (+0.73, fdr 2e-05), [[ARID1A]] (+0.68, fdr 1e-05); moves opposite to [[SMYD3]] (-0.61, fdr 1e-04), [[RADX]] (-0.60, fdr 1e-04), [[SKIC3]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 1 goes from it, the strongest it → [[COL21A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6337.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.87×** | +24.9 | 0e+00 | 47/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +7.9 | 9e-13 | 29/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +7.1 | 2e-10 | 29/46 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +6.3 | 5e-08 | 32/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +6.2 | 9e-08 | 30/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +5.9 | 3e-07 | 24/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.95×** | +5.9 | 3e-07 | 30/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +5.9 | 3e-07 | 25/46 (A-427, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +5.7 | 6e-07 | 25/45 (J82, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.8 | 7e-05 | 21/45 (RKO, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +4.6 | 2e-04 | 20/48 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.32×** | +4.1 | 0.002 | 14/48 (SW1417, NCI-H2347, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.011 | 17/48 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.6 | 0.011 | 12/42 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.012 | 21/47 (C-33 A, PANC-1, …) | top dose only |  |
| [[crizotinib (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.026 | 10/48 (CFPAC-1, HEC-1-A, …) | top dose only | position effect removed |
| [[Pentoxifylline (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.046 | 7/47 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6337.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.204×** | -26.5 | 0e+00 | 48/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.218×** | -25.4 | 0e+00 | 47/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.342×** | -17.9 | 0e+00 | 46/47 (HT-29, AsPC-1, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.615×** | -11.5 | 2e-28 | 45/48 (LOX-IMVI, SHP-77, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.622×** | -7.9 | 3e-13 | 36/48 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.640×** | -6.2 | 6e-08 | 31/47 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.687×** | -5.9 | 3e-07 | 22/37 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.517×** | -5.8 | 6e-07 | 25/48 (SHP-77, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.810×** | -5.0 | 4e-05 | 20/48 (Hs 766T, SW 900, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.732×** | -4.8 | 8e-05 | 18/41 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change | **0.770×** | -4.4 | 7e-04 | 21/43 (AsPC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.803×** | -3.7 | 0.012 | 13/47 (NCI-H460, A-172, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.775×** | -3.5 | 0.018 | 14/48 (KATO III, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.863× | -3.5 | 0.022 | 12/48 (HEC-1-A, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6337. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 29.0 | 1 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.263× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 40.7 | 1 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.0547× (z -24.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.175× (z -15.7) |
| [[SW480 (line)]] | alt | 24.6 | 4 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +16.7) | [[Panobinostat (drug)]] 5 µM 0.159× (z -18.0) |
| [[HT-29 (line)]] | alt | 36.1 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.0878× (z -20.7) |
| [[KATO III (line)]] | alt | 24.9 | 2 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.146× (z -15.2) |
| [[PANC-1 (line)]] | alt | 22.9 | 3 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +17.5) | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 41.7 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.0696× (z -21.8) |
| [[LoVo (line)]] | wt | 39.0 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 24.0 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.106× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.226× (z -10.7) |
| [[A498 (line)]] | wt | 20.1 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +12.4) | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -15.1) |
| [[HepG2_C3A (line)]] | wt | 30.7 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +11.6) | [[Belinostat (drug)]] 5 µM 0.154× (z -11.5) |
| [[HOP62 (line)]] | alt | 19.4 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -13.0) |
| [[Hs 766T (line)]] | wt | 21.7 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.141× (z -11.9) |
| [[HS-578T (line)]] | alt | 23.0 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.133× (z -13.9) |
| [[LS 180 (line)]] | wt | 27.3 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -13.7) |
| [[NCI-H1573 (line)]] | alt | 36.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.197× (z -13.6) |
| [[NCI-H460 (line)]] | wt | 23.7 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +17.3) | [[Panobinostat (drug)]] 5 µM 0.172× (z -15.8) |
| [[SHP-77 (line)]] | alt | 31.5 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -12.6) |
| [[SNU-423 (line)]] | alt | 23.3 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.159× (z -11.8) |
| [[SW 900 (line)]] | alt | 22.5 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -10.4) |
| [[SW1417 (line)]] | alt | 53.9 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.157× (z -16.3) |
| [[SW48 (line)]] | wt | 34.3 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -10.1) |
| [[A549 (line)]] | wt | 22.1 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +15.0) | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -11.1) |
| [[C-33 A (line)]] | alt | 36.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -14.6) |
| [[COLO 205 (line)]] | alt | 27.8 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.178× (z -10.2) |
| [[J82 (line)]] | alt | 33.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.294× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 19.2 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.184× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 44.2 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.242× (z -11.5) |
| [[AN3 CA (line)]] | alt | 47.8 | 0 | 2 | — | [[Verteporfin (drug)]] 5 µM 0.0785× (z -10.9) |
| [[BT-474 (line)]] | alt | 38.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.0831× (z -17.1) |
| [[CFPAC-1 (line)]] | alt | 19.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.288× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 19.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.28× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.132× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 30.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 18.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.110× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 24.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.247× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 28.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -14.4) |
| [[A-427 (line)]] | wt | 18.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -9.4) |
| [[C32 (line)]] | wt | 23.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +13.5) | — |
| [[H4 (line)]] | wt | 16.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.39× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 42.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.272× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 21.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +13.9) | — |
| [[NCI-H661 (line)]] | alt | 37.9 | 0 | 1 | — | [[CP21R7 (drug)]] 0.05 µM 0.0655× (z -8.5) |
| [[RKO (line)]] | wt | 29.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +11.9) | — |
| [[SNU-1 (line)]] | wt | 36.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -8.9) |
| [[CHP-212 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6337), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRD1]] | +0.76 | +0.65 / +0.66 | both halves | 7e-06 | pathway: Chromatin modifying enzymes |
| [[PHF2]] | +0.73 | +0.47 / +0.67 | both halves | 2e-05 | pathway: Chromatin modifying enzymes; STRING 460 |
| [[ARID1A]] | +0.68 | +0.54 / +0.55 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[UBTF]] | +0.67 | +0.49 / +0.56 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |
| [[KMT2D]] | +0.66 | +0.54 / +0.59 | both halves | 1e-05 | same gene group; pathway: Chromatin modifying enzymes; STRING 896 |
| [[ANXA2R-OT1]] | +0.65 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[TLCD3A]] | +0.64 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[ZNF689]] | +0.64 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[HOXC9]] | +0.63 | +0.39 / +0.42 | both halves | 5e-05 |  |
| [[RNF217-AS1]] | +0.63 | +0.30 / +0.49 | both halves | 2e-04 |  |
| [[ATXN1L]] | +0.63 | +0.35 / +0.44 | both halves | 1e-04 |  |
| [[CCNJ]] | +0.62 | +0.49 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMYD3]] | -0.61 | -0.37 / -0.34 | both halves | 1e-04 | same gene group; pathway: Chromatin modifying enzymes; STRING 747 |
| [[RADX]] | -0.60 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[SKIC3]] | -0.60 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[MOCS2]] | -0.60 | -0.30 / -0.64 | both halves | 2e-04 |  |
| [[KCTD17]] | -0.58 | -0.26 / -0.38 | both halves | 4e-04 |  |
| [[POT1]] | -0.58 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[NDUFA12]] | -0.57 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[FCHO1]] | -0.57 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[SGSM1]] | -0.57 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[INTS13]] | -0.56 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[PAFAH1B3]] | -0.56 | -0.26 / -0.25 | both halves | 4e-04 |  |
| [[HLTF]] | -0.56 | -0.28 / -0.44 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises SETD1B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises SETD1B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL21A1]] | B | the direction of SETD1B's effect on COL21A1's drug response is not inferred (the mechanism is not recorded) | recorded alteration (mechanism not recorded) of SETD1B in 8 lines vs 32 not recorded | the SETD1B-altered lines respond 0.41× as strongly (z diff +1.73); strongest at Dinaciclib 0.5 µM: 0.25x vs 2.06x (z diff +8.8) | 0.048 | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3, ACVR2A, ARID1A; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.725). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-5.5, 12.2); signed map (25.9, -24.5). **Vector** length 121, 32.8% of its response variance represented; |z| ≥ 3 in 1,049 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +16.7 | +24.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.6 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +5.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.2 | -11.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.8 | -25.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.7 | -26.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.8 | -17.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.9 | -6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -5.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.1 | -2.9 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | SET domain containing 1B, histone lysine methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:121,804,009-121,832,656 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1076, Set1B, KMT2G |
| Gene groups (HGNC) | Histone lysine methyltransferases; RNA binding motif containing; SET domain containing |
| Reactome | 8 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; PKMTs methylate histone lysines; RUNX1 regulates genes involved in megakaryocyte differentiation and platelet function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPS6](https://www.uniprot.org/uniprotkb/Q9UPS6) (Histone-lysine N-methyltransferase SETD1B):

> Histone methyltransferase that catalyzes methyl group transfer from S-adenosyl-L-methionine to the epsilon-amino group of 'Lys-4' of histone H3 (H3K4) via a non-processive mechanism. Part of chromatin remodeling machinery, forms H3K4me1, H3K4me2 and H3K4me3 methylation marks at active chromatin sites where transcription and DNA repair take place. Plays an essential role in regulating the transcriptional programming of multipotent hematopoietic progenitor cells and lymphoid lineage specification …

**Summary**, from NCBI Gene [23067](https://www.ncbi.nlm.nih.gov/gene/23067):

> SET1B is a component of a histone methyltransferase complex that produces trimethylated histone H3 at Lys4 (Lee et al., 2007 [PubMed 17355966]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:29187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29187) · Entrez [23067](https://www.ncbi.nlm.nih.gov/gene/23067) · UniProt [Q9UPS6](https://www.uniprot.org/uniprotkb/Q9UPS6) · Ensembl [ENSG00000139718](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139718)

## Data

Gene col 6337: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6337); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6337, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6337]; `tensor/DDL_lfc|DDL_z.npy` [6337]; `embed/gene_vectors.npy` [6337]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6337 or target_col == 6337). Every well: [[SETD1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SETD1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
