---
symbol: "CENPP"
type: "gene"
col: 12000
ensembl_id: "ENSG00000188312"
name: "centromere protein P"
location: "9q22.31"
module: 6
arm: "+"
pooled_cpm: 77.77
n_lines_expressing: 46
n_dd_up: 34
n_dd_down: 22
n_dd_up_clean: 18
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 6
direction_downstream: 26
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CENPP

*centromere protein P* — 9q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.01× (z +20.2, q 0e+00, up in 42 of 44 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.65× (z +10.3, q 7e-23, up in 32 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.371× (z -7.5, q 2e-11, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRIP1]] (+0.77, fdr 7e-06), [[DNA2]] (+0.77, fdr 7e-06), [[WDHD1]] (+0.76, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 26 go from it, the strongest it → [[ZRANB3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 17 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12000.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **4.01×** | +20.2 | 0e+00 | 42/44 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **3.28×** | +17.3 | 0e+00 | 42/44 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **2.88×** | +15.4 | 0e+00 | 40/44 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.07×** | +15.0 | 0e+00 | 39/44 (NCI-H1792, LoVo, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **2.13×** | +10.6 | 5e-24 | 35/44 (NCI-H460, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +10.3 | 7e-23 | 32/44 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.66×** | +7.1 | 1e-10 | 28/44 (LS 180, NCI-H460, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.5 | 7e-09 | 29/44 (A549, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.58×** | +6.1 | 5e-08 | 29/44 (RKO, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.50×** | +5.7 | 8e-07 | 30/44 (NCI-H23, C32, …) | top dose only |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.47×** | +5.4 | 4e-06 | 29/44 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.44×** | +5.2 | 7e-06 | 26/44 (J82, NCI-H460, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.44×** | +5.2 | 7e-06 | 31/44 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +5.1 | 1e-05 | 27/44 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.39×** | +4.8 | 7e-05 | 26/44 (J82, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.82×** | +4.6 | 2e-04 | 25/44 (SW480, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +4.3 | 6e-04 | 20/44 (J82, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Afatinib (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.003 | 17/45 (HEC-1-A, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.004 | 21/44 (SNU-423, A-427, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.007 | 20/44 (A-427, NCI-H460, …) | rises with dose | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.009 | 19/44 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.19× | +3.5 | 0.009 | 20/44 (J82, PANC-1, …) | rises with dose |  |
| [[Amsacrine (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.017 | 18/44 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.018 | 14/44 (HEC-1-A, SW1417, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.023 | 15/44 (NCI-H460, J82, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.023 | 15/44 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12000.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.371×** | -7.5 | 2e-11 | 39/45 (SW480, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.415×** | -6.7 | 6e-09 | 32/44 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.640×** | -6.5 | 1e-08 | 30/44 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.619×** | -6.5 | 1e-08 | 25/41 (A-427, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.682×** | -5.3 | 1e-05 | 26/44 (HT-29, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.704×** | -5.1 | 3e-05 | 27/44 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.791×** | -4.8 | 1e-04 | 28/44 (KATO III, COLO 205, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.719×** | -4.8 | 1e-04 | 28/44 (NCI-H23, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.729×** | -4.6 | 2e-04 | 24/44 (HT-29, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.554×** | -4.5 | 4e-04 | 19/33 (HT-29, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.807×** | -4.4 | 5e-04 | 21/44 (LS 180, HCT15, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.821×** | -4.1 | 0.002 | 19/44 (LS 180, KATO III, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.757×** | -4.1 | 0.002 | 23/44 (SHP-77, SW 1088, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.680×** | -4.0 | 0.002 | 22/44 (KATO III, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.770×** | -3.7 | 0.009 | 19/43 (Panc 03.27, COLO 205, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.787×** | -3.5 | 0.016 | 23/44 (HEC-1-A, C-33 A, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.802×** | -3.2 | 0.037 | 19/43 (COLO 205, HT-29, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.858× | -3.2 | 0.040 | 11/44 (NCI-H23, Panc 03.27, …) | rises with dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.863× | -3.1 | 0.056 | 15/44 (HCT15, COLO 205, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.868× | -2.9 | 0.078 | 9/45 (SW 1271, HEC-1-A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.12 per unit of S-phase module lfc, -0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12000. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 160 | 11 (7 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +21.2) | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.394× (z -9.2) |
| [[HT-29 (line)]] | alt | 77.9 | 7 (6 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +13.0) | [[Lonafarnib (drug)]] 5 µM 0.0773× (z -11.5) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.291× (z -10.7) |
| [[A-427 (line)]] | wt | 97.0 | 4 (4 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.61× (z +9.1) ⚠ cell-cycle shift, explains ~69% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.0978× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.180× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 76.4 | 7 (6 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.27× (z +14.3) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.99× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.245× (z -12.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 54.7 | 6 (5 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +13.7) | [[Ixazomib citrate (drug)]] 5 µM 0.211× (z -10.3) |
| [[PANC-1 (line)]] | alt | 81.6 | 2 (2 ⚠) | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +10.6) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 5 µM 0.330× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.229× (z -9.8) |
| [[RKO (line)]] | wt | 144 | 6 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -9.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 122 | 5 (4 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.00× (z +15.2) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.77× (z +8.9) | [[TAK-901 (drug)]] 5 µM 0.178× (z -9.9) |
| [[LoVo (line)]] | wt | 68.4 | 6 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +17.4) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[A498 (line)]] | wt | 114 | 4 (4 ⚠) | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.58× (z +10.9) ⚠ cell-cycle shift, explains ~59% of this change | [[Selinexor (drug)]] 5 µM 0.434× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 153 | 1 (1 ⚠) | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.24× (z +8.6) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.425× (z -9.2) |
| [[HS-578T (line)]] | alt | 40.9 | 5 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +11.8) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SW 900 (line)]] | alt | 29.1 | 4 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.91× (z +11.4) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.51× (z +9.8) | [[AZD2858 (drug)]] 0.5 µM 0.0463× (z -12.1) ⚠ toxic |
| [[A549 (line)]] | wt | 90.9 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.34× (z +13.0) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[AN3 CA (line)]] | alt | 235 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.241× (z -9.8) |
| [[C32 (line)]] | wt | 67.0 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.06× (z +10.2) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[Hs 766T (line)]] | wt | 64.8 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.95× (z +11.6) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[KATO III (line)]] | alt | 122 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.27× (z +12.4) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 132 | 1 (1 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +9.0) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 5 µM 0.107× (z -23.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 28.1 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 11.1× (z +11.6) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[LOX-IMVI (line)]] | wt | 51.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.27× (z +11.8) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 88.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +11.5) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H1792 (line)]] | alt | 40.1 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.68× (z +17.9) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[Panc 03.27 (line)]] | alt | 53.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 84.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.82× (z +10.9) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[H4 (line)]] | wt | 35.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.83× (z +9.9) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[HepG2_C3A (line)]] | wt | 24.6 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +12.0) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[HOP62 (line)]] | alt | 58.7 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.95× (z +11.5) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[RPMI-7951 (line)]] | alt | 47.9 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +10.9) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 72.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.2) ⚠ cell-cycle shift, explains ~38% of this change | [[Lonafarnib (drug)]] 5 µM 0.117× (z -9.0) ⚠ toxic |
| [[SW48 (line)]] | wt | 88.2 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +9.6) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[A-172 (line)]] | wt | 89.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.31× (z +8.8) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[C-33 A (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -10.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 68.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.348× (z -9.0) |
| [[SHP-77 (line)]] | alt | 102 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.107× (z -9.8) |
| [[SW1417 (line)]] | alt | 113 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.37× (z +11.3) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[AsPC-1 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 91.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.1 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 165 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12000), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRIP1]] | +0.77 | +0.70 / +0.79 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[DNA2]] | +0.77 | +0.71 / +0.78 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[WDHD1]] | +0.76 | +0.65 / +0.82 | both halves | 7e-06 |  |
| [[MIR924HG]] | +0.75 | +0.64 / +0.77 | both halves | 7e-06 |  |
| [[KIF24]] | +0.74 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[BRCA1]] | +0.73 | +0.71 / +0.73 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[GINS1]] | +0.72 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[MCM10]] | +0.72 | +0.64 / +0.74 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[ATAD5]] | +0.71 | +0.55 / +0.78 | both halves | 1e-05 |  |
| [[ZNF367]] | +0.71 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[BRCA2]] | +0.71 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[PKMYT1]] | +0.71 | +0.59 / +0.72 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CENPP's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.9% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[E2F2]] | B | E2F2 activity raises CENPP's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.34× lower at baseline in the lines without E2F2 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDC25A]] | C | CDC25A activity raises CENPP's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 3.44× lower at baseline in the lines without CDC25A | 0.032 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent; co-absent with the target |
| [[DIAPH3]], [[MELK]] | C | DIAPH3, MELK activity raises CENPP's level | lines that do not express DIAPH3, MELK (3) vs lines expressing them (47) | 4.14× lower at baseline in the lines without DIAPH3, MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[MCM10]] | C | MCM10 activity raises CENPP's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.96× lower at baseline in the lines without MCM10 | 0.072 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises CENPP's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 3.50× lower at baseline in the lines without E2F1, MCM3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 0, C 26. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZRANB3]] | C | CENPP activity raises ZRANB3's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.67× lower at baseline in the lines without CENPP | 0.007 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[C9orf40]] | C | CENPP activity raises C9orf40's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.31× lower at baseline in the lines without CENPP | 0.010 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[KIF24]] | C | CENPP activity raises KIF24's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.61× lower at baseline in the lines without CENPP | 0.016 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[MMS22L]] | C | CENPP activity raises MMS22L's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.89× lower at baseline in the lines without CENPP | 0.017 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[SCMH1]] | C | CENPP activity raises SCMH1's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.05× lower at baseline in the lines without CENPP | 0.020 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[FANCC]] | C | CENPP activity raises FANCC's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.25× lower at baseline in the lines without CENPP | 0.023 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[NCAPG2]] | C | CENPP activity raises NCAPG2's level | lines that do not express CENPP (4) vs lines expressing it (46) | 1.90× lower at baseline in the lines without CENPP | 0.025 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[WDR62]] | C | CENPP activity raises WDR62's level | lines that do not express CENPP (4) vs lines expressing it (46) | 3.34× lower at baseline in the lines without CENPP | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent; co-absent with the target |
| [[CASP8AP2]] | C | CENPP activity raises CASP8AP2's level | lines that do not express CENPP (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without CENPP | 0.034 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[DIAPH3]] | C | CENPP activity raises DIAPH3's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.81× lower at baseline in the lines without CENPP | 0.044 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[RFWD3]] | C | CENPP activity raises RFWD3's level | lines that do not express CENPP (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without CENPP | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[DTL]] | C | CENPP activity raises DTL's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.34× lower at baseline in the lines without CENPP | 0.050 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.685). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.2, -46.4); signed map (-39.9, -45.3). **Vector** length 121, 41.4% of its response variance represented; |z| ≥ 3 in 1,430 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.52 to 65); *DNA strand elongation* (reactome, mean cos +0.58 to 28); *DNA Replication* (reactome, mean cos +0.56 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.9 | +2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | +1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +2.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | -1.1 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.5 | +4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.4 | +3.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +3.0 | +3.2 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.0 | +3.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.7 | +3.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.8 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.8 | -1.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | -7.0 | -2.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -6.7 | -5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.2 | -5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.7 | -6.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.0 | -4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.4 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | centromere protein P |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.31 — chr9:92,325,953-92,620,529 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RP11-19J3.3, CENP-P |
| Gene groups (HGNC) | Constitutive centromere associated network |
| Reactome | 20 pathways, smallest: Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IPU0](https://www.uniprot.org/uniprotkb/Q6IPU0) (Centromere protein P):

> Component of the CENPA-CAD (nucleosome distal) complex, a complex recruited to centromeres which is involved in assembly of kinetochore proteins, mitotic progression and chromosome segregation. May be involved in incorporation of newly synthesized CENPA into centromeres via its interaction with the CENPA-NAC complex.

**Summary**, from NCBI Gene [401541](https://www.ncbi.nlm.nih.gov/gene/401541):

> CENPP is a subunit of a CENPH (MIM 605607)-CENPI (MIM 300065)-associated centromeric complex that targets CENPA (MIM 117139) to centromeres and is required for proper kinetochore function and mitotic progression (Okada et al., 2006 [PubMed 16622420]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:32933](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32933) · Entrez [401541](https://www.ncbi.nlm.nih.gov/gene/401541) · UniProt [Q6IPU0](https://www.uniprot.org/uniprotkb/Q6IPU0) · Ensembl [ENSG00000188312](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188312)

## Data

Gene col 12000: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12000); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12000, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12000]; `tensor/DDL_lfc|DDL_z.npy` [12000]; `embed/gene_vectors.npy` [12000]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12000 or target_col == 12000). Every well: [[CENPP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
