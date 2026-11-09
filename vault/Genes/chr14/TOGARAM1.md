---
symbol: "TOGARAM1"
type: "gene"
col: 12650
ensembl_id: "ENSG00000198718"
name: "TOG array regulator of axonemal microtubules 1"
location: "14q21.2"
module: 11
arm: "+"
pooled_cpm: 87.89
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 18
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# TOGARAM1

*TOG array regulator of axonemal microtubules 1* — 14q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.73× (z +20.0, q 0e+00, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.425× (z -22.1, q 0e+00, down in 36 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.763× (z -7.0, q 2e-10, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OSCP1]] (+0.64, fdr 7e-06), [[RSPRY1]] (+0.63, fdr 1e-05), [[MORN2]] (+0.63, fdr 1e-05); moves opposite to [[TTL]] (-0.58, fdr 1e-05), [[KLC2]] (-0.55, fdr 1e-05), [[FAM20B]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12650.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +20.0 | 0e+00 | 38/45 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.03×** | +17.3 | 0e+00 | 43/47 (Panc 03.27, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.16×** | +14.3 | 3e-44 | 39/45 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +9.8 | 1e-20 | 37/46 (RKO, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +9.5 | 2e-19 | 28/45 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.25×** | +8.0 | 9e-14 | 27/46 (SW480, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +7.7 | 1e-12 | 23/47 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.34×** | +7.4 | 7e-12 | 29/46 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.33×** | +7.3 | 2e-11 | 31/46 (J82, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +7.0 | 1e-10 | 27/46 (RKO, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.24×** | +5.5 | 2e-06 | 24/46 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.20×** | +4.7 | 1e-04 | 21/46 (RKO, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +4.4 | 5e-04 | 17/46 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 1.17× | +4.0 | 0.003 | 10/46 (KATO III, NCI-H2030, …) | all doses, flat |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.17× | +3.8 | 0.006 | 11/45 (SNU-423, PANC-1, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.093 | 9/47 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | 1.17× | +2.9 | 0.099 | 7/46 (A549, J82, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12650.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.425×** | -22.1 | 0e+00 | 36/47 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.423×** | -21.3 | 0e+00 | 36/40 (CFPAC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.539×** | -14.8 | 0e+00 | 37/42 (SW 900, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.583×** | -13.4 | 1e-38 | 38/45 (CFPAC-1, RKO, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.747×** | -7.6 | 5e-12 | 30/46 (COLO 205, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.763×** | -7.0 | 2e-10 | 27/46 (C32, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.832×** | -6.7 | 1e-09 | 26/46 (NCI-H460, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.777×** | -6.3 | 2e-08 | 29/45 (RKO, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.786×** | -6.2 | 3e-08 | 29/46 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.845× | -6.2 | 3e-08 | 20/47 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.805×** | -5.6 | 1e-06 | 23/46 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.812×** | -5.4 | 3e-06 | 22/46 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.825×** | -5.0 | 3e-05 | 21/45 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.767×** | -4.9 | 4e-05 | 24/46 (BT-474, RKO, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.830×** | -4.8 | 5e-05 | 20/46 (SNU-423, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.830×** | -4.8 | 5e-05 | 22/47 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.836× | -4.7 | 1e-04 | 20/45 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.831×** | -4.6 | 1e-04 | 20/45 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.855× | -3.9 | 0.003 | 17/46 (NCI-H1573, C32, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **0.744×** | -3.7 | 0.005 | 17/44 (MIA PaCa-2, H4, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.878× | -3.2 | 0.035 | 13/46 (Hs 766T, CHP-212, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.882× | -3.2 | 0.038 | 12/46 (CFPAC-1, C-33 A, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.920× | -3.1 | 0.045 | 1/46 (H4) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12650. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 74.3 | 8 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +22.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0779× (z -24.2) ⚠ toxic |
| [[A-427 (line)]] | wt | 91.8 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +19.7) | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -16.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 201 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -26.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.481× (z -10.3) |
| [[HOP62 (line)]] | alt | 120 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 120 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -16.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 148 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.343× (z -14.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 81.3 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.437× (z -11.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 78.3 | 5 | 1 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.84× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -12.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 138 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 160 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 6.26× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -19.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 109 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.125× (z -23.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 90.2 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +20.9) | [[Dinaciclib (drug)]] 0.5 µM 0.507× (z -10.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 94.7 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -11.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 103 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -11.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 115 | 2 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.36× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -12.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 97.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +12.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.297× (z -13.8) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 191 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.81× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.420× (z -12.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 108 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.45× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -24.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 173 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.159× (z -20.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 67.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.425× (z -10.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 87.9 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.73× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -13.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 65.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -10.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 93.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -11.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 58.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.8) | [[Lonafarnib (drug)]] 5 µM 0.117× (z -9.7) ⚠ toxic |
| [[J82 (line)]] | alt | 80.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +19.2) | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 110 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.63× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -18.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 96.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -17.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 77.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -16.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 87.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.384× (z -11.1) |
| [[CHP-212 (line)]] | wt | 160 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0663× (z -18.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -16.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 40.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.4) | [[Digitoxin (drug)]] 0.5 µM 0.454× (z -8.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A498 (line)]] | wt | 51.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.446× (z -10.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -8.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 85.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -11.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -13.3) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 75.8 | 0 | 1 | — | [[Adagrasib (drug)]] 0.5 µM 0.0790× (z -8.8) |
| [[SW 1271 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0877× (z -13.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.1 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 13.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12650), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSCP1]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[RSPRY1]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[MORN2]] | +0.63 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[PDCD7]] | +0.62 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[LINS1]] | +0.61 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[GPATCH1]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[TTF1]] | +0.59 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[CIR1]] | +0.59 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[VIRMA]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PPIL4]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[NBPF11]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[PEX13]] | +0.57 | +0.55 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTL]] | -0.58 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[KLC2]] | -0.55 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[FAM20B]] | -0.55 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[MAPK9]] | -0.54 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[USB1]] | -0.54 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ME2]] | -0.53 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ACSL4]] | -0.53 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[DIAPH1]] | -0.53 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[PANK3]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[C1orf198]] | -0.52 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[SELENOI]] | -0.50 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[NUTM2A-AS1]] | -0.50 | -0.56 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.414). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-34.5, 2.1); signed map (-9.0, -2.4). **Vector** length 112, 31.4% of its response variance represented; |z| ≥ 3 in 1,202 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +11.5 | +17.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +7.9 | +14.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +9.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +4.7 | +7.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +4.6 | +8.0 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +3.3 | +4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +2.4 |
|  | [[Sulfatinib (drug)]] 5 µM |  | +2.5 | -0.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.5 | -6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.0 | -21.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.0 | -4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.6 | -14.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.5 | -22.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.5 | -7.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.9 | -6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.5 | -4.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | TOG array regulator of axonemal microtubules 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.2 — chr14:44,962,190-45,074,431 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Crescerin-1, crescerin; previously KIAA0423, FAM179B |
| Gene groups (HGNC) | TOG domain containing |
| Hallmark sets | UV_RESPONSE_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4F4](https://www.uniprot.org/uniprotkb/Q9Y4F4) (TOG array regulator of axonemal microtubules protein 1):

> Involved in ciliogenesis. It is required for appropriate acetylation and polyglutamylation of ciliary microtubules, and regulation of cilium length. Interacts with microtubules and promotes microtubule polymerization via its HEAT repeat domains, especially those in TOG region 2 and 4 (By similarity).

**Summary**, from NCBI Gene [23116](https://www.ncbi.nlm.nih.gov/gene/23116):

> Predicted to enable microtubule binding activity. Involved in cilium assembly. Located in axoneme. Implicated in Joubert syndrome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19959](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19959) · Entrez [23116](https://www.ncbi.nlm.nih.gov/gene/23116) · UniProt [Q9Y4F4](https://www.uniprot.org/uniprotkb/Q9Y4F4) · Ensembl [ENSG00000198718](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198718)

## Data

Gene col 12650: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12650); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12650, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12650]; `tensor/DDL_lfc|DDL_z.npy` [12650]; `embed/gene_vectors.npy` [12650]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12650 or target_col == 12650). Every well: [[TOGARAM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOGARAM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
