---
symbol: "TASP1"
type: "gene"
col: 1570
ensembl_id: "ENSG00000089123"
name: "taspase 1"
location: "20p12.1"
module: 185
arm: "+"
pooled_cpm: 102.04
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/185"]
generated_by: "tahoemap"
---

# TASP1

*taspase 1* — 20p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.79× (z +19.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.486× (z -14.0, q 8e-42, down in 46 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 12 lines (SW480 0.305×, HOP62 0.279×, MIA PaCa-2 0.260×, LoVo 0.317×, …); [[Dinaciclib (drug)]] 5 µM in 5 lines (SHP-77 0.123×, HCT15 0.140×, LOX-IMVI 0.280×, SW480 0.354×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (KATO III 0.335×, SW480 0.344×, A-427 0.278×, SK-MEL-2 0.287×; ⚠ toxic; transcription drop); [[Naproxen (drug)]] 0.05 µM in 1 line (AN3 CA 0.177×); [[Saquinavir (drug)]] 0.5 µM in 1 line (SW 1088 0.0789×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUBPL]] (+0.69, fdr 7e-06), [[DIS3L2]] (+0.68, fdr 7e-06), [[NOL10]] (+0.65, fdr 1e-05); moves opposite to [[SIX4]] (-0.47, fdr 5e-04), [[ERO1B]] (-0.47, fdr 2e-04), [[CSRP2]] (-0.46, fdr 3e-05).
> It is in [[Module 185]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DGKE]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1570.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.79×** | +19.9 | 0e+00 | 47/48 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.40×** | +17.0 | 0e+00 | 48/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.14×** | +14.8 | 0e+00 | 47/48 (AsPC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +8.9 | 8e-17 | 44/48 (NCI-H2347, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +7.7 | 2e-12 | 35/49 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +7.0 | 2e-10 | 36/48 (HepG2/C3A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.25×** | +6.1 | 9e-08 | 27/48 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +5.3 | 7e-06 | 37/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +5.0 | 5e-05 | 39/49 (AsPC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.5 | 3e-04 | 21/48 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.58×** | +4.3 | 7e-04 | 24/48 (HEC-1-A, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.002 | 25/48 (HT-29, C-33 A, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +4.1 | 0.002 | 24/47 (NCI-H2347, C32, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.9 | 0.003 | 21/48 (A-427, AsPC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.011 | 20/48 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.021 | 21/48 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.081 | 11/48 (LoVo, C-33 A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1570.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Auranofin (drug)]] 5 µM in 12 lines (SW480 0.305×, HOP62 0.279×, MIA PaCa-2 0.260×, LoVo 0.317×, …); [[Dinaciclib (drug)]] 5 µM in 5 lines (SHP-77 0.123×, HCT15 0.140×, LOX-IMVI 0.280×, SW480 0.354×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (KATO III 0.335×, SW480 0.344×, A-427 0.278×, SK-MEL-2 0.287×; ⚠ toxic; transcription drop); [[Naproxen (drug)]] 0.05 µM in 1 line (AN3 CA 0.177×); [[Saquinavir (drug)]] 0.5 µM in 1 line (SW 1088 0.0789×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.486×** | -14.0 | 8e-42 | 46/48 (SW480, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.608×** | -9.3 | 4e-18 | 29/44 (SHP-77, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.648×** | -7.8 | 1e-12 | 34/49 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **0.748×** | -5.7 | 2e-06 | 34/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.748×** | -5.4 | 6e-06 | 28/47 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.810×** | -3.8 | 0.014 | 21/45 (NCI-H661, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.854× | -3.1 | 0.17 | 17/47 (CFPAC-1, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1570. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 231 | 4 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.70× (z +14.4) | [[Auranofin (drug)]] 5 µM 0.305× (z -17.3) |
| [[KATO III (line)]] | alt | 220 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.61× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -14.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 216 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.29× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.123× (z -29.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.484× (z -10.5) |
| [[A-427 (line)]] | wt | 63.8 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.84× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -13.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 45.2 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.05× (z +16.1) | — |
| [[HEC-1-A (line)]] | alt | 126 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.06× (z +15.9) | [[Auranofin (drug)]] 5 µM 0.427× (z -12.3) |
| [[LoVo (line)]] | wt | 111 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.69× (z +15.7) | [[Auranofin (drug)]] 5 µM 0.317× (z -13.9) |
| [[NCI-H2347 (line)]] | alt | 77.6 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.30× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.498× (z -8.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 87.0 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.57× (z +12.2) | [[Docetaxel (drug)]] 0.05 µM 0.468× (z -9.8) ⚠ transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SW 900 (line)]] | alt | 64.0 | 4 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.98× (z +12.7) | [[Auranofin (drug)]] 5 µM 0.356× (z -9.5) |
| [[A498 (line)]] | wt | 96.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.80× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.464× (z -10.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 94.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.86× (z +9.6) | [[Lonafarnib (drug)]] 5 µM 0.134× (z -9.0) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 195 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.87× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.412× (z -9.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 134 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.59× (z +14.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.310× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 89.1 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.57× (z +11.0) | [[Auranofin (drug)]] 5 µM 0.279× (z -15.1) |
| [[HT-29 (line)]] | alt | 119 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.62× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -12.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 113 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.24× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -14.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 74.4 | 3 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.47× (z +13.0) | [[Auranofin (drug)]] 5 µM 0.260× (z -14.1) |
| [[Panc 03.27 (line)]] | alt | 95.2 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.50× (z +10.6) | [[Auranofin (drug)]] 5 µM 0.476× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 124 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.399× (z -10.4) |
| [[A549 (line)]] | wt | 114 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.65× (z +11.4) | — |
| [[CFPAC-1 (line)]] | alt | 121 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.49× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.372× (z -10.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 159 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.140× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.346× (z -11.1) |
| [[HS-578T (line)]] | alt | 73.9 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.90× (z +11.2) | [[Auranofin (drug)]] 5 µM 0.444× (z -8.6) |
| [[J82 (line)]] | alt | 59.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.06× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 88.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.55× (z +15.0) | — |
| [[NCI-H2030 (line)]] | alt | 39.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.63× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 95.7 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.480× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 82.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.30× (z +15.1) | — |
| [[SNU-1 (line)]] | wt | 88.5 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.03× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 64.5 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 2.79× (z +9.8) | [[Auranofin (drug)]] 5 µM 0.257× (z -13.0) |
| [[SW1417 (line)]] | alt | 74.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.26× (z +13.3) | — |
| [[C32 (line)]] | wt | 74.4 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.05× (z +10.4) | [[Auranofin (drug)]] 5 µM 0.323× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 75.5 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.42× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 33.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 148 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.338× (z -11.6) |
| [[SW 1088 (line)]] | alt | 103 | 0 | 2 (1 ⚠) | — | [[Fostamatinib (disodium hexahydrate) (drug)]] 0.5 µM 0.0760× (z -10.1) ⚠ unreliable plate only · without an alert: [[Saquinavir (drug)]] 0.5 µM 0.0789× (z -10.0) |
| [[SW48 (line)]] | wt | 104 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.61× (z +11.3) | — |
| [[A-172 (line)]] | wt | 47.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 111 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.177× (z -10.8) |
| [[C-33 A (line)]] | alt | 84.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.94× (z +9.9) | — |
| [[CHP-212 (line)]] | wt | 111 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.235× (z -8.9) |
| [[Hs 766T (line)]] | wt | 54.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.00× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 52.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.89× (z +8.8) | — |
| [[NCI-H661 (line)]] | alt | 76.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0662× (z -11.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 171 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.314× (z -11.0) |
| [[SW 1271 (line)]] | alt | 98.1 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0926× (z -9.8) |
| [[H4 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1570), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUBPL]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[DIS3L2]] | +0.68 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[NOL10]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[FAF1]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[FARS2]] | +0.63 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[VPS13B]] | +0.59 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[CSTPP1]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[DDX10]] | +0.59 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[ULK4]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[MIPEP]] | +0.58 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[CDKAL1]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[LCLAT1]] | +0.56 | +0.34 / +0.62 | both halves | 1e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIX4]] | -0.47 | -0.24 / -0.52 | both halves | 5e-04 |  |
| [[ERO1B]] | -0.47 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[CSRP2]] | -0.46 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[TGFBR1]] | -0.46 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[SNX31]] | -0.45 | -0.20 / -0.46 | ⚠ not reproduced | 7e-04 |  |
| [[NPHS1]] | -0.44 | -0.19 / -0.47 | ⚠ not reproduced | 8e-04 |  |
| [[MEX3B]] | -0.44 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[FAM117A]] | -0.44 | -0.24 / -0.46 | both halves | 4e-04 |  |
| [[DGKE]] | -0.43 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[FEZ1]] | -0.42 | -0.14 / -0.39 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DGKE]] | B | DGKE activity lowers TASP1's level | lines that do not express DGKE (12) vs lines expressing it (38) | 1.27× higher at baseline in the lines without DGKE | 0.089 | ⚠ within organs, on part of the lines; also absent: TNFRSF1B, TNFRSF10D, HHEX; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 185]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.725). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-11.1, -35.0); signed map (-10.1, -49.1). **Vector** length 107, 33.0% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.5 | +7.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.4 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +4.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.8 | +3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.2 | +2.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.9 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -12.4 | -14.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.2 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.0 | -2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | +1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | +3.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | taspase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.1 — chr20:13,389,392-13,638,932 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20212, dJ585I14.2; previously C20orf13 |
| Reactome | 3 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; Epigenetic regulation by WDR5-containing histone modifying complexes; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6P5](https://www.uniprot.org/uniprotkb/Q9H6P5) (Threonine aspartase 1):

> Protease responsible for KMT2A/MLL1 processing and activation. It also activates KMT2D/MLL2 (By similarity). Through substrate activation, it controls the expression of HOXA genes, and the expression of key cell cycle regulators including CCNA1, CCNB1, CCNE1 and CDKN2A (By similarity).

**Summary**, from NCBI Gene [55617](https://www.ncbi.nlm.nih.gov/gene/55617):

> This gene encodes an endopeptidase that cleaves specific substrates following aspartate residues. The encoded protein undergoes posttranslational autoproteolytic processing to generate alpha and beta subunits, which reassemble into the active alpha2-beta2 heterotetramer. It is required to cleave MLL, a protein required for the maintenance of HOX gene expression, and TFIIA, a basal transcription factor. Alternatively spliced transcript variants have been described, but their biological validity …

**Accessions** — [HGNC:15859](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15859) · Entrez [55617](https://www.ncbi.nlm.nih.gov/gene/55617) · UniProt [Q9H6P5](https://www.uniprot.org/uniprotkb/Q9H6P5) · Ensembl [ENSG00000089123](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089123)

## Data

Gene col 1570: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1570); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1570, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1570]; `tensor/DDL_lfc|DDL_z.npy` [1570]; `embed/gene_vectors.npy` [1570]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1570 or target_col == 1570). Every well: [[TASP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TASP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
