---
symbol: "DHRSX"
type: "gene"
col: 9749
ensembl_id: "ENSG00000169084"
name: "dehydrogenase/reductase X-linked"
location: "Xp22.33 and Yp11.2"
module: 29
arm: "-"
pooled_cpm: 142.12
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 39
n_dd_up_clean: 6
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# DHRSX

*dehydrogenase/reductase X-linked* — Xp22.33 and Yp11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.29× (z +8.8, q 6e-16, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (14 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.143× (z -47.4, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LARP7]] (+0.62, fdr 1e-05), [[ZBED1]] (+0.62, fdr 1e-05, ⚠ same locus), [[EIF4EBP3]] (+0.61, fdr 3e-05), [[CUX1]] (+0.60, fdr 1e-05); moves opposite to [[GRB2]] (-0.61, fdr 1e-05), [[PLEKHA8]] (-0.61, fdr 2e-05), [[TM9SF2]] (-0.57, fdr 9e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9749.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +8.8 | 6e-16 | 25/47 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.24×** | +5.0 | 1e-04 | 27/47 (CFPAC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.14× | +4.7 | 6e-04 | 10/47 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.41×** | +4.4 | 0.002 | 22/47 (NCI-H460, BT-474, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.19× | +4.3 | 0.002 | 19/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.40×** | +4.3 | 0.002 | 26/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.007 | 20/49 (NCI-H460, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.17× | +3.8 | 0.009 | 20/47 (CFPAC-1, SW 900, …) | inconsistent across doses |  |
| [[MK-3903 (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.013 | 15/47 (NCI-H460, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.015 | 14/48 (NCI-H460, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.16× | +3.6 | 0.019 | 14/47 (PANC-1, HOP62, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.15× | +3.5 | 0.021 | 14/48 (NCI-H2347, NCI-H2030, …) | all doses, flat |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.15× | +3.5 | 0.021 | 15/47 (SNU-423, A498, …) | inconsistent across doses |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.15× | +3.4 | 0.023 | 12/47 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.09× | +3.2 | 0.060 | 5/48 (RPMI-7951, H4, …) | all doses, flat |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.060 | 10/48 (HCT15, H4, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.060 | 19/46 (SW480, NCI-H1573, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.060 | 11/47 (C32, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9749.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.143×** | -47.4 | 0e+00 | 47/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.147×** | -46.8 | 0e+00 | 47/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.158×** | -45.1 | 0e+00 | 47/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.343×** | -37.0 | 0e+00 | 47/48 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.298×** | -29.6 | 0e+00 | 47/47 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.358×** | -25.1 | 0e+00 | 47/47 (SW48, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.246×** | -17.9 | 0e+00 | 48/48 (SW480, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.478×** | -17.3 | 0e+00 | 42/49 (SW480, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.504×** | -16.1 | 0e+00 | 41/47 (A-172, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.532×** | -14.8 | 0e+00 | 41/46 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.529×** | -14.4 | 4e-45 | 35/44 (RKO, SW48, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **0.575×** | -13.0 | 5e-37 | 31/43 (A-172, NCI-H460, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.377×** | -12.5 | 6e-34 | 43/48 (RKO, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.658×** | -10.2 | 7e-23 | 32/48 (A-172, NCI-H460, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.750×** | -9.9 | 1e-21 | 34/47 (RKO, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.498×** | -8.9 | 2e-17 | 31/47 (A-172, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.700×** | -8.7 | 1e-16 | 35/47 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.557×** | -7.5 | 2e-12 | 39/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.596×** | -6.6 | 9e-10 | 35/47 (NCI-H460, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.766×** | -6.5 | 2e-09 | 30/47 (PANC-1, COLO 205, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.605×** | -6.4 | 3e-09 | 36/47 (NCI-H460, A-172, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.69 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9749. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 347 | 6 (4 ⚠) | 14 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +29.9) | [[Panobinostat (drug)]] 5 µM 0.0903× (z -44.7) |
| [[SW480 (line)]] | alt | 208 | 1 | 18 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +11.2) | [[Belinostat (drug)]] 5 µM 0.0547× (z -48.5) |
| [[A-172 (line)]] | wt | 426 | 0 | 18 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -41.7) |
| [[PANC-1 (line)]] | alt | 80.2 | 0 | 18 (9 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.159× (z -25.7) |
| [[A549 (line)]] | wt | 225 | 1 | 16 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.4) | [[Belinostat (drug)]] 5 µM 0.103× (z -28.0) |
| [[SNU-423 (line)]] | alt | 158 | 0 | 17 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0623× (z -33.7) |
| [[C32 (line)]] | wt | 140 | 0 | 16 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.123× (z -25.5) |
| [[MIA PaCa-2 (line)]] | alt | 144 | 0 | 16 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0555× (z -37.8) |
| [[RKO (line)]] | wt | 156 | 2 (1 ⚠) | 13 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.0803× (z -32.3) |
| [[SW48 (line)]] | wt | 185 | 0 | 14 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0491× (z -34.4) |
| [[HepG2_C3A (line)]] | wt | 183 | 1 | 12 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.9) | [[Belinostat (drug)]] 5 µM 0.0909× (z -25.5) |
| [[H4 (line)]] | wt | 307 | 0 | 12 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0690× (z -30.8) |
| [[J82 (line)]] | alt | 132 | 1 | 10 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +12.9) | [[Belinostat (drug)]] 5 µM 0.139× (z -26.0) |
| [[KATO III (line)]] | alt | 117 | 1 (1 ⚠) | 10 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.37× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 0.5 µM 0.0965× (z -30.9) |
| [[NCI-H2030 (line)]] | alt | 266 | 0 | 11 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.139× (z -23.7) |
| [[HCT15 (line)]] | alt | 192 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0951× (z -26.8) |
| [[HEC-1-A (line)]] | alt | 206 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -26.3) |
| [[LoVo (line)]] | wt | 126 | 0 | 10 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.120× (z -29.8) |
| [[SK-MEL-2 (line)]] | alt | 97.2 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.125× (z -22.7) |
| [[C-33 A (line)]] | alt | 150 | 0 | 9 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.172× (z -20.4) |
| [[HOP62 (line)]] | alt | 83.2 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.115× (z -25.4) |
| [[Hs 766T (line)]] | wt | 85.5 | 1 | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +19.0) | [[Panobinostat (drug)]] 5 µM 0.118× (z -22.0) |
| [[NCI-H1573 (line)]] | alt | 118 | 1 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +16.5) | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -21.5) |
| [[NCI-H1792 (line)]] | alt | 104 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -24.6) |
| [[COLO 205 (line)]] | alt | 139 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0662× (z -24.6) |
| [[HS-578T (line)]] | alt | 79.0 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -19.4) |
| [[HT-29 (line)]] | alt | 70.9 | 0 | 8 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.179× (z -19.0) |
| [[hTERT-HPNE (line)]] | wt | 115 | 0 | 8 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.129× (z -21.4) |
| [[NCI-H23 (line)]] | alt | 64.6 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.137× (z -19.6) |
| [[Panc 03.27 (line)]] | alt | 86.3 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -21.7) |
| [[RPMI-7951 (line)]] | alt | 74.0 | 1 | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +13.0) | [[Belinostat (drug)]] 5 µM 0.117× (z -18.0) |
| [[SW 900 (line)]] | alt | 73.8 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.110× (z -20.0) |
| [[CFPAC-1 (line)]] | alt | 132 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.159× (z -23.7) |
| [[LS 180 (line)]] | wt | 72.2 | 0 | 7 | — | [[Belinostat (drug)]] 5 µM 0.134× (z -24.1) |
| [[SW1417 (line)]] | alt | 114 | 0 | 7 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.161× (z -22.1) |
| [[A498 (line)]] | wt | 81.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -17.9) |
| [[AsPC-1 (line)]] | alt | 64.4 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -20.7) |
| [[BT-474 (line)]] | alt | 248 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.113× (z -23.6) |
| [[A-427 (line)]] | wt | 58.8 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.6) | [[Belinostat (drug)]] 5 µM 0.305× (z -13.1) |
| [[AN3 CA (line)]] | alt | 138 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -13.9) |
| [[SNU-1 (line)]] | wt | 106 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +16.7) | [[Belinostat (drug)]] 5 µM 0.116× (z -19.1) |
| [[CHP-212 (line)]] | wt | 134 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -13.1) |
| [[NCI-H2347 (line)]] | alt | 67.8 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.262× (z -11.9) |
| [[SHP-77 (line)]] | alt | 44.2 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.223× (z -13.3) |
| [[SW 1088 (line)]] | alt | 230 | 0 | 4 | — | [[Naproxen (drug)]] 0.05 µM 0.0567× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 34.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9749), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARP7]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ZBED1]] | +0.62 | +0.65 / +0.50 | both halves | 1e-05 | same gene group; STRING 879; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[EIF4EBP3]] | +0.61 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[CUX1]] | +0.60 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[BPTF]] | +0.59 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[RSF1]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | +0.58 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ANGPT2]] | +0.58 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[AK6]] | +0.58 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[CDK3]] | +0.57 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[TTC27]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[CHMP4A]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[BOD1L1]] | +0.56 | +0.49 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRB2]] | -0.61 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[PLEKHA8]] | -0.61 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[TM9SF2]] | -0.57 | -0.58 / -0.36 | both halves | 9e-05 |  |
| [[POGLUT2]] | -0.57 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[SEC24C]] | -0.56 | -0.48 / -0.44 | both halves | 3e-05 | pathway: Asparagine N-linked glycosylation |
| [[TMED7]] | -0.56 | -0.52 / -0.39 | both halves | 5e-05 | pathway: Asparagine N-linked glycosylation |
| [[VDAC2]] | -0.56 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[BPNT2]] | -0.56 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[NOMO2]] | -0.56 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[PGAM1]] | -0.55 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[POMGNT2]] | -0.55 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[PDIA6]] | -0.55 | -0.50 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers DHRSX's level | compounds that target MTOR: 3 of 8 raise it (AZD-8055, Bimiralisib, Sapanisertib) | 38% of the class's compounds vs 1.7% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.488). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-12.5, -9.6); signed map (3.7, -14.1). **Vector** length 111, 36.9% of its response variance represented; |z| ≥ 3 in 1,787 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +15.3 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.8 | -1.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +9.2 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | -2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | +5.0 | -13.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +3.9 | +2.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.6 | +4.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.5 | +3.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.4 | +2.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.8 | -25.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.2 | -29.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.6 | -9.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.3 | -17.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.2 | -12.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.4 | -4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -9.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.0 | -6.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.6 | -7.5 |

## What is on record

|  |  |
|---|---|
| Name | dehydrogenase/reductase X-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.33 and Yp11.2 — chrX:2,219,506-2,502,805 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DHRS5X, DHRSXY, DHRSY, DHRS5Y, SDR46C1, SDR7C6 |
| Gene groups (HGNC) | Pseudoautosomal region 1; Short chain dehydrogenase/reductase superfamily |
| Reactome | 4 pathways, smallest: Synthesis of dolichyl-phosphate; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5I4](https://www.uniprot.org/uniprotkb/Q8N5I4) (Polyprenol dehydrogenase):

> Oxidoreductase that plays a key role in early steps of protein N-linked glycosylation by mediating two non-consecutive steps in dolichol biosynthesis. Acts both as a NAD(+)-dependent dehydrogenase and as a NADPH-dependent reductase during the conversion of polyprenol into dolichol. First catalyzes the NAD(+)-dependent dehydrogenation of polyprenol into polyprenal; polyprenal is then reduced into dolichal by SRD5A3. It then catalyzes the NADPH-dependent reduction of dolichal into dolichol. May …

**Summary**, from NCBI Gene [207063](https://www.ncbi.nlm.nih.gov/gene/207063):

> Enables alcohol dehydrogenase (NADP+) activity; dolichal reductase (NADPH) activity; and polyprenol dehydrogenase (NAD+) activity. Involved in dolichyl monophosphate biosynthetic process and positive regulation of autophagy. Located in extracellular region. Is active in lipid droplet. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18399](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18399) · Entrez [207063](https://www.ncbi.nlm.nih.gov/gene/207063) · UniProt [Q8N5I4](https://www.uniprot.org/uniprotkb/Q8N5I4) · Ensembl [ENSG00000169084](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169084)

## Data

Gene col 9749: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9749); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9749, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9749]; `tensor/DDL_lfc|DDL_z.npy` [9749]; `embed/gene_vectors.npy` [9749]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9749 or target_col == 9749). Every well: [[DHRSX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHRSX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
