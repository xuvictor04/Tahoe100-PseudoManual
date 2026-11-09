---
symbol: "MYBL1"
type: "gene"
col: 11718
ensembl_id: "ENSG00000185697"
name: "MYB proto-oncogene like 1"
location: "8q13.1"
module: 22
arm: "+"
pooled_cpm: 46.02
n_lines_expressing: 42
n_dd_up: 33
n_dd_down: 8
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 9
direction_downstream: 39
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# MYBL1

*MYB proto-oncogene like 1* — 8q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.27× (z +30.5, q 0e+00, up in 32 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.558× (z -10.7, q 9e-24, down in 28 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ECT2]] (+0.69, fdr 1e-05), [[CIP2A]] (+0.68, fdr 7e-06), [[HELLS]] (+0.67, fdr 7e-06); moves opposite to [[MRPL32]] (-0.59, fdr 3e-05), [[ZNF581]] (-0.59, fdr 3e-05), [[DNLZ]] (-0.57, fdr 2e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 39 go from it, the strongest it → [[BIRC5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 26 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11718.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.27×** | +30.5 | 0e+00 | 32/39 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **3.23×** | +21.4 | 0e+00 | 37/38 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **3.35×** | +21.2 | 0e+00 | 30/31 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +20.8 | 0e+00 | 31/39 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.74×** | +18.4 | 0e+00 | 37/40 (NCI-H460, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.64×** | +17.7 | 0e+00 | 36/40 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.60×** | +16.1 | 0e+00 | 30/34 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **2.15×** | +13.9 | 3e-42 | 34/40 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.06×** | +12.7 | 4e-35 | 33/39 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +12.1 | 3e-32 | 28/39 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.97×** | +11.8 | 1e-30 | 31/40 (RKO, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.81×** | +10.8 | 1e-25 | 31/40 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +10.4 | 2e-23 | 28/40 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.70×** | +9.3 | 4e-19 | 26/37 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.61×** | +8.4 | 2e-15 | 22/39 (MIA PaCa-2, HS-578T, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.27×** | +7.8 | 2e-13 | 28/40 (A498, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +6.7 | 6e-10 | 22/40 (A549, J82, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +6.1 | 3e-08 | 18/40 (HEC-1-A, RKO, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.64×** | +4.7 | 7e-05 | 13/40 (SW480, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.003 | 12/40 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.007 | 13/40 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.007 | 10/40 (C32, SW 900, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.008 | 8/40 (HOP62, AN3 CA, …) | all doses, flat |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.015 | 7/40 (SW480, J82, …) | top dose only | plate-row cell shift |
| [[Ponatinib (drug)]] 5 µM |  | 1.20× | +3.3 | 0.018 | 12/40 (HS-578T, A549, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11718.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.558×** | -10.7 | 9e-24 | 28/40 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.587×** | -9.2 | 1e-17 | 27/40 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.700×** | -6.5 | 1e-08 | 27/40 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -4.4 | 0.001 | 2/40 (SW48, CHP-212) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | 0.854× | -4.1 | 0.004 | 13/40 (SHP-77, PANC-1, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.854× | -4.1 | 0.004 | 12/40 (HCT15, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.687×** | -3.6 | 0.027 | 13/33 (A-427, C32, …) | all doses, flat | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.875× | -3.4 | 0.041 | 10/40 (LOX-IMVI, H4, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.831×** | -3.4 | 0.045 | 11/39 (A549, NCI-H2030, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.704×** | -3.4 | 0.045 | 16/40 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.837× | -3.2 | 0.064 | 14/40 (H4, HCT15, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.719×** | -3.2 | 0.073 | 7/37 (SW480, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.842× | -3.1 | 0.073 | 9/39 (NCI-H2030, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | 0.842× | -3.1 | 0.073 | 14/38 (Panc 03.27, NCI-H1792, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.844× | -3.1 | 0.074 | 10/40 (HCT15, SK-MEL-2, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.790×** | -3.1 | 0.074 | 9/38 (RPMI-7951, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.892× | -3.0 | 0.089 | 6/40 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.72 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11718. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 233 | 2 (2 ⚠) | 10 (6 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.56× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.277× (z -14.3) |
| [[A498 (line)]] | wt | 110 | 10 (6 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +23.3) | [[Bortezomib (drug)]] 0.05 µM 0.306× (z -9.8) |
| [[HS-578T (line)]] | alt | 49.0 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +23.8) | — |
| [[SW480 (line)]] | alt | 27.4 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +14.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 76.5 | 6 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +15.2) | [[Ixazomib citrate (drug)]] 5 µM 0.280× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 19.5 | 7 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +15.1) | — |
| [[HOP62 (line)]] | alt | 46.3 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +20.9) | — |
| [[J82 (line)]] | alt | 72.6 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +23.1) | — |
| [[NCI-H1792 (line)]] | alt | 14.8 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.1× (z +24.0) | — |
| [[A-172 (line)]] | wt | 28.3 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +12.1) | — |
| [[A549 (line)]] | wt | 23.9 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.61× (z +14.4) | — |
| [[NCI-H2347 (line)]] | alt | 28.6 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +11.5) | — |
| [[C32 (line)]] | wt | 21.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +17.2) | — |
| [[CFPAC-1 (line)]] | alt | 24.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +11.7) | — |
| [[hTERT-HPNE (line)]] | wt | 42.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +14.5) | — |
| [[NCI-H2030 (line)]] | alt | 98.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.23× (z +12.1) | — |
| [[RPMI-7951 (line)]] | alt | 52.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +17.9) | — |
| [[SW 900 (line)]] | alt | 32.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +13.8) | — |
| [[SW1417 (line)]] | alt | 29.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.31× (z +8.7) | — |
| [[A-427 (line)]] | wt | 35.1 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.53× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[TAK-901 (drug)]] 5 µM 0.0595× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 70.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.85× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.09× (z +8.6) | — |
| [[RKO (line)]] | wt | 17.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.11× (z +14.3) | — |
| [[SNU-423 (line)]] | alt | 37.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +16.9) | — |
| [[HEC-1-A (line)]] | alt | 33.1 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.313× (z -10.2) |
| [[Hs 766T (line)]] | wt | 32.9 | 2 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.82× (z +8.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 44.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +13.9) | [[Bortezomib (drug)]] 0.05 µM 0.230× (z -10.5) |
| [[LS 180 (line)]] | wt | 11.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +8.9) | [[Selinexor (drug)]] 5 µM 0.296× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 16.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.03× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 35.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +14.8) | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0711× (z -9.7) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 48.7 | 0 | 1 (1 ⚠) | — | [[Artesunate (drug)]] 5 µM 0.426× (z -8.5) ⚠ cell-cycle shift, explains ~80% of this change |
| [[AN3 CA (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.89 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.84 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.31 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.63 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.40 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11718), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECT2]] | +0.69 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[CIP2A]] | +0.68 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[HELLS]] | +0.67 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[EPB41L2]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[CBX5]] | +0.66 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[ANLN]] | +0.65 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[ESCO2]] | +0.65 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[NEMP1]] | +0.65 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[CENPH]] | +0.64 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[ZWILCH]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[C18orf54]] | +0.63 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[STMN1]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL32]] | -0.59 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[ZNF581]] | -0.59 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[DNLZ]] | -0.57 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[CCDC12]] | -0.57 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[PEX16]] | -0.57 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[MRPS12]] | -0.56 | -0.36 / -0.50 | both halves | 9e-05 | STRING 400 |
| [[JOSD2]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[RPP21]] | -0.55 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[NOL7]] ⚠ | -0.55 | -0.42 / -0.53 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF235]] | -0.55 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[ALKBH7]] | -0.54 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[C19orf53]] | -0.54 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[NCBP2AS2]] | -0.54 | -0.31 / -0.53 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MYBL1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[POGLUT3]] | B | POGLUT3 activity raises MYBL1's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 2.31× lower at baseline in the lines without POGLUT3 | 0.062 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |
| [[LMO7]] | B | LMO7 activity lowers MYBL1's level | lines that do not express LMO7 (11) vs lines expressing it (39) | 1.85× higher at baseline in the lines without LMO7 | 0.069 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[ZNF726]] | B | ZNF726 activity raises MYBL1's level | lines that do not express ZNF726 (20) vs lines expressing it (30) | 2.08× lower at baseline in the lines without ZNF726 | 0.071 | ⚠ within organs, on part of the lines; also absent: SUSD5, RNF150, BVES |
| [[EPB41L2]] | B | EPB41L2 activity raises MYBL1's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 2.32× lower at baseline in the lines without EPB41L2 | 0.078 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers MYBL1's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 6.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises MYBL1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[DPY19L2P1]] | B | DPY19L2P1 activity raises MYBL1's level | lines that do not express DPY19L2P1 (26) vs lines expressing it (24) | 2.14× lower at baseline in the lines without DPY19L2P1 | 0.084 | ⚠ within organs, on part of the lines; also absent: STAC, RNF180, SRGN |
| [[DIAPH3]] | C | DIAPH3 activity raises MYBL1's level | lines that do not express DIAPH3 (3) vs lines expressing it (47) | 4.59× lower at baseline in the lines without DIAPH3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 39, C 0. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BIRC5]] | B | MYBL1 activity raises BIRC5's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 2.43× lower at baseline in the lines without MYBL1 | 0.001 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[TPX2]] | B | MYBL1 activity raises TPX2's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.90× lower at baseline in the lines without MYBL1 | 0.014 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[STMN1]] | B | MYBL1 activity raises STMN1's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 2.31× lower at baseline in the lines without MYBL1 | 0.014 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[MCM4]] | B | MYBL1 activity raises MCM4's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.73× lower at baseline in the lines without MYBL1 | 0.019 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[DNMT1]] | B | MYBL1 activity raises DNMT1's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.75× lower at baseline in the lines without MYBL1 | 0.023 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[KIF11]] | B | MYBL1 activity raises KIF11's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.89× lower at baseline in the lines without MYBL1 | 0.025 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[MAD2L1]] | B | MYBL1 activity raises MAD2L1's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.80× lower at baseline in the lines without MYBL1 | 0.027 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[TMEM107]] | B | MYBL1 activity raises TMEM107's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 2.05× lower at baseline in the lines without MYBL1 | 0.030 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[DEK]] | B | MYBL1 activity raises DEK's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.24× lower at baseline in the lines without MYBL1 | 0.031 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[FANCD2]] | B | MYBL1 activity raises FANCD2's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.69× lower at baseline in the lines without MYBL1 | 0.034 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[SMC2]] | B | MYBL1 activity raises SMC2's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.83× lower at baseline in the lines without MYBL1 | 0.036 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[NOL7]] | B | MYBL1 activity raises NOL7's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.14× lower at baseline in the lines without MYBL1 | 0.043 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.539). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.6, -49.2); signed map (-45.1, -47.5). **Vector** length 106, 28.9% of its response variance represented; |z| ≥ 3 in 1,339 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Condensation of Prometaphase Chromosomes* (reactome, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +30.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +4.4 | +16.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +3.6 | +21.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.4 | +11.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.4 | +3.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.3 | +1.6 |
|  | [[Ralimetinib dimesylate (drug)]] 5 µM |  | +2.2 | +2.2 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +2.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -8.3 | -9.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -7.1 | -10.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -6.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.6 | -3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.2 | -2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -3.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.4 | -3.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | MYB proto-oncogene like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q13.1 — chr8:66,562,175-66,614,247 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AMYB, A-myb |
| Gene groups (HGNC) | Myb/SANT domain containing |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 2 pathways, smallest: PIWI-interacting RNA (piRNA) biogenesis; Gene Silencing by RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P10243](https://www.uniprot.org/uniprotkb/P10243) (Myb-related protein A):

> Transcription factor that specifically recognizes the sequence 5'-YAAC[GT]G-3'. Acts as a master regulator of male meiosis by promoting expression of piRNAs: activates expression of both piRNA precursor RNAs and expression of protein-coding genes involved in piRNA metabolism (By similarity). The piRNA metabolic process mediates the repression of transposable elements during meiosis by forming complexes composed of piRNAs and Piwi proteins and governs the methylation and subsequent repression of …

**Summary**, from NCBI Gene [4603](https://www.ncbi.nlm.nih.gov/gene/4603):

> Enables DNA-binding transcription activator activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Involved in positive regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7547](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7547) · Entrez [4603](https://www.ncbi.nlm.nih.gov/gene/4603) · UniProt [P10243](https://www.uniprot.org/uniprotkb/P10243) · Ensembl [ENSG00000185697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185697)

## Data

Gene col 11718: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11718); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11718, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11718]; `tensor/DDL_lfc|DDL_z.npy` [11718]; `embed/gene_vectors.npy` [11718]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11718 or target_col == 11718). Every well: [[MYBL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYBL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
