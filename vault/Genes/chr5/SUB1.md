---
symbol: "SUB1"
type: "gene"
col: 3458
ensembl_id: "ENSG00000113387"
name: "SUB1 regulator of transcription"
location: "5p13.3"
module: 3
arm: "-"
pooled_cpm: 128.08
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SUB1

*SUB1 regulator of transcription* — 5p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.69× (z +18.6, q 0e+00, up in 46 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.60× (z +8.8, q 1e-16, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.911× (z -5.8, q 3e-06, down in 2 of 50 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 1 line (Panc 03.27 0.129×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.608×; ⚠ cell-cycle shift, explains ~23% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.812×; ⚠ position not correctable).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRKAR1A]] (+0.55, fdr 3e-05), [[BIRC2]] (+0.53, fdr 2e-05), [[DZIP3]] (+0.52, fdr 3e-05); moves opposite to [[GID4]] (-0.63, fdr 1e-05), [[PTDSS2]] (-0.55, fdr 3e-05), [[HIRA]] (-0.54, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 19 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3458.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.69×** | +18.6 | 0e+00 | 46/49 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.81×** | +15.8 | 0e+00 | 46/48 (NCI-H1573, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.30×** | +15.1 | 0e+00 | 44/44 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.94×** | +11.5 | 1e-28 | 42/45 (MIA PaCa-2, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.88×** | +11.4 | 3e-28 | 44/48 (NCI-H1573, J82, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.67×** | +9.6 | 6e-20 | 43/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +8.8 | 1e-16 | 43/48 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.49×** | +7.5 | 3e-12 | 39/48 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +7.3 | 1e-11 | 40/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.27×** | +6.5 | 5e-09 | 28/49 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.42×** | +6.3 | 1e-08 | 35/47 (LoVo, SHP-77, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.03×** | +6.1 | 7e-08 | 43/49 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.37×** | +5.7 | 4e-07 | 30/50 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.34×** | +5.5 | 1e-06 | 36/48 (HS-578T, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.31×** | +5.2 | 9e-06 | 34/48 (SW1417, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.008 | 25/48 (LS 180, Panc 03.27, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.009 | 24/48 (MIA PaCa-2, C32, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.014 | 25/48 (A-427, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.017 | 15/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.062 | 17/48 (NCI-H1573, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3458.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Lonafarnib (drug)]] 5 µM in 1 line (Panc 03.27 0.129×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.608×; ⚠ cell-cycle shift, explains ~23% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.812×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.911× | -5.8 | 3e-06 | 2/50 (NCI-H23, NCI-H661) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.747×** | -4.0 | 0.016 | 29/50 (NCI-H596, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.862× | -3.7 | 0.034 | 12/48 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |
| [[Pentagastrin (drug)]] 5 µM |  | 0.879× | -3.4 | 0.11 | 6/48 (SW48, MIA PaCa-2, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.881× | -3.3 | 0.11 | 7/48 (SW48, RKO, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.686× | -3.2 | 0.14 | 25/50 (NCI-H460, NCI-H596, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3458. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 102 | 9 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +11.3) | — |
| [[A-172 (line)]] | wt | 110 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +15.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.61× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 124 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +19.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.20× (z +14.3) | — |
| [[PANC-1 (line)]] | alt | 128 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.01× (z +10.4) | — |
| [[C32 (line)]] | wt | 70.6 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +15.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.80× (z +12.4) | — |
| [[NCI-H1792 (line)]] | alt | 95.1 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW 900 (line)]] | alt | 157 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +15.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +10.5) | — |
| [[A549 (line)]] | wt | 109 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HOP62 (line)]] | alt | 109 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +13.0) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[J82 (line)]] | alt | 174 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +15.7) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[SW480 (line)]] | alt | 140 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-427 (line)]] | wt | 130 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[AsPC-1 (line)]] | alt | 118 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +14.9) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[COLO 205 (line)]] | alt | 91.1 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +13.0) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[LOX-IMVI (line)]] | wt | 122 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[Panc 03.27 (line)]] | alt | 122 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Lonafarnib (drug)]] 5 µM 0.129× (z -11.3) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 86.7 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +14.0) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[HT-29 (line)]] | alt | 105 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 97.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[KATO III (line)]] | alt | 105 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.15× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LoVo (line)]] | wt | 108 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H23 (line)]] | alt | 143 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H460 (line)]] | wt | 191 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -8.8) ⚠ cell-cycle shift, explains ~23% of this change |
| [[BT-474 (line)]] | alt | 155 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +10.5) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[CFPAC-1 (line)]] | alt | 139 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +11.6) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[Hs 766T (line)]] | wt | 99.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +12.9) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[HS-578T (line)]] | alt | 115 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LS 180 (line)]] | wt | 104 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2347 (line)]] | alt | 153 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +10.5) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[SNU-1 (line)]] | wt | 83.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A498 (line)]] | wt | 248 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.06× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[C-33 A (line)]] | alt | 73.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.37× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[H4 (line)]] | wt | 160 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HCT15 (line)]] | alt | 113 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HEC-1-A (line)]] | alt | 89.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +8.7) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[HepG2_C3A (line)]] | wt | 135 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2030 (line)]] | alt | 164 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RKO (line)]] | wt | 95.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SHP-77 (line)]] | alt | 156 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 54.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW1417 (line)]] | alt | 124 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.8) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[SW48 (line)]] | wt | 77.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.0) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[AN3 CA (line)]] | alt | 127 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 100 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 109 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3458), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKAR1A]] | +0.55 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[BIRC2]] | +0.53 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[DZIP3]] | +0.52 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[EXTL2]] | +0.51 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[IFT80]] | +0.50 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[TADA3]] | +0.49 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[NFKBIE]] | +0.48 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[RIPK2-DT]] | +0.48 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[IL6ST]] | +0.47 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[ZNF641]] | +0.47 | +0.56 / +0.39 | both halves | 6e-05 |  |
| [[GRIPAP1]] | +0.47 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[CDK17]] | +0.47 | +0.35 / +0.52 | both halves | 1e-04 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GID4]] | -0.63 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[PTDSS2]] | -0.55 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[HIRA]] | -0.54 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[ANKRD13B]] | -0.53 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[RILPL1]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[CLPP]] | -0.53 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[MANEAL]] | -0.53 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[CMTM8]] | -0.52 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[SIMC1]] | -0.52 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[PRKX]] | -0.51 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[DEXI]] | -0.50 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[GPR89A]] | -0.50 | -0.36 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.378). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-10.9, -2.5); signed map (17.5, -8.9). **Vector** length 69.2, 18.2% of its response variance represented; |z| ≥ 3 in 1,000 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +4.5 | +18.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +3.7 | +15.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.7 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +3.3 | +11.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +3.4 |
|  | [[Berbamine (drug)]] 5 µM |  | +1.3 | +2.2 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +1.1 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | +3.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.8 | +1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.6 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.0 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.0 | +0.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | +1.6 |

## What is on record

|  |  |
|---|---|
| Name | SUB1 regulator of transcription |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.3 — chr5:32,531,633-32,604,079 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PC4, p15, p14 |
| Matched by | ensembl_id |

**Function**, from UniProt [P53999](https://www.uniprot.org/uniprotkb/P53999) (Activated RNA polymerase II transcriptional coactivator p15):

> General coactivator that functions cooperatively with TAFs and mediates functional interactions between upstream activators and the general transcriptional machinery. May be involved in stabilizing the multiprotein transcription complex. Binds single-stranded DNA. Also binds, in vitro, non-specifically to double-stranded DNA (ds DNA).

**Summary**, from NCBI Gene [10923](https://www.ncbi.nlm.nih.gov/gene/10923):

> Enables DNA binding activity; identical protein binding activity; and transcription coactivator activity. Involved in RNA polymerase II promoter clearance; negative regulation of DNA metabolic process; and regulation of transcription by RNA polymerase II. Located in nucleolus and nucleoplasm. Part of transcription regulator complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19985](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19985) · Entrez [10923](https://www.ncbi.nlm.nih.gov/gene/10923) · UniProt [P53999](https://www.uniprot.org/uniprotkb/P53999) · Ensembl [ENSG00000113387](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113387)

## Data

Gene col 3458: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3458); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3458, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3458]; `tensor/DDL_lfc|DDL_z.npy` [3458]; `embed/gene_vectors.npy` [3458]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3458 or target_col == 3458). Every well: [[SUB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
