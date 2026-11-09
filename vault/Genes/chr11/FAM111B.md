---
symbol: "FAM111B"
type: "gene"
col: 12083
ensembl_id: "ENSG00000189057"
name: "FAM111 trypsin like peptidase B"
location: "11q12.1"
module: 6
arm: "+"
pooled_cpm: 16.48
n_lines_expressing: 40
n_dd_up: 51
n_dd_down: 25
n_dd_up_clean: 21
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 10
direction_downstream: 39
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# FAM111B

*FAM111 trypsin like peptidase B* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 51 drug-doses (30 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.48× (z +12.9, q 1e-35, up in 34 of 38 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.90× (z +7.8, q 3e-13, up in 22 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.517× (z -8.1, q 3e-13, down in 32 of 38 measured lines) ⚠ cell-cycle shift, explains ~59% of this change. The strongest without an alert is [[Dihydroartemisinin (drug)]] 5 µM: 0.554× (z -5.1, q 3e-05, down in 26 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM10]] (+0.91, fdr 7e-06), [[CLSPN]] (+0.90, fdr 7e-06), [[E2F1]] (+0.88, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[ZNF724]] → it (grade B ⚠); 39 go from it, the strongest it → [[ASF1B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 30 with an alert ⚠; shown: the 15 strongest and the 14 next strongest without an alert. 51 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 30 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12083.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **4.48×** | +12.9 | 1e-35 | 34/38 (PANC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **4.28×** | +12.6 | 1e-33 | 35/37 (PANC-1, SW1417, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **2.64×** | +11.9 | 3e-30 | 31/36 (J82, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **3.61×** | +11.1 | 2e-26 | 33/38 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **3.13×** | +9.9 | 7e-21 | 33/37 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **2.99×** | +9.1 | 9e-18 | 27/36 (SW480, J82, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **2.89×** | +8.8 | 9e-17 | 27/35 (SW480, J82, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.90×** | +7.8 | 3e-13 | 22/37 (J82, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.52×** | +7.7 | 1e-12 | 24/37 (J82, PANC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **2.32×** | +7.3 | 2e-11 | 26/38 (SW1417, HT-29, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~91% of this change | **2.22×** | +6.6 | 2e-09 | 22/33 (J82, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.58×** | +5.6 | 1e-06 | 17/38 (J82, NCI-H2347, …) | top dose only | composition shift |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.95×** | +5.5 | 1e-06 | 24/36 (A-427, SW480, …) | all doses, stronger at high dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.56×** | +5.4 | 2e-06 | 22/38 (HT-29, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.83×** | +5.0 | 2e-05 | 8/21 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.62×** | +4.2 | 7e-04 | 15/38 (SW1417, Panc 03.27, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **2.35×** | +3.9 | 0.003 | 11/38 (SW1417, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.55×** | +3.8 | 0.003 | 15/38 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Brimonidine (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.004 | 12/38 (KATO III, SW480, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.52×** | +3.6 | 0.006 | 10/38 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.52×** | +3.6 | 0.006 | 15/38 (BT-474, KATO III, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.50×** | +3.5 | 0.009 | 9/38 (Panc 03.27, NCI-H1573, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.012 | 10/37 (SW1417, KATO III, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.52×** | +3.3 | 0.015 | 13/36 (A-427, HCT15, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.023 | 11/37 (A-427, C-33 A, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.44×** | +3.2 | 0.024 | 8/38 (KATO III, SK-MEL-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.46×** | +3.0 | 0.039 | 9/35 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +2.9 | 0.044 | 13/36 (NCI-H2347, SW480, …) | top dose only |  |
| [[Omeprazole (drug)]] 5 µM |  | **1.40×** | +2.9 | 0.047 | 6/38 (KATO III, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12083.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.517×** | -8.1 | 3e-13 | 32/38 (PANC-1, COLO 205, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.362×** | -6.3 | 9e-08 | 27/37 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **0.547×** | -5.2 | 3e-05 | 19/37 (A-172, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.524×** | -5.2 | 3e-05 | 21/38 (A-427, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.554×** | -5.1 | 3e-05 | 26/37 (A-172, KATO III, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.598×** | -4.5 | 7e-04 | 21/38 (A-172, A-427, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.588×** | -4.4 | 0.001 | 14/37 (COLO 205, Panc 03.27, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.504×** | -4.2 | 0.002 | 17/38 (NCI-H23, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.610×** | -4.1 | 0.003 | 18/37 (KATO III, A-427, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.631×** | -4.0 | 0.003 | 17/36 (KATO III, NCI-H2030, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.631×** | -4.0 | 0.003 | 20/35 (HCT15, NCI-H23, …) | rises with dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.438×** | -3.7 | 0.008 | 13/35 (KATO III, HEC-1-A, …) | two highest doses | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.560×** | -3.6 | 0.014 | 14/38 (MIA PaCa-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.749×** | -3.6 | 0.015 | 18/38 (HCT15, HT-29, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.754×** | -3.5 | 0.019 | 13/37 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.471×** | -3.4 | 0.022 | 10/38 (COLO 205, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | **0.493×** | -3.2 | 0.041 | 13/38 (HOP62, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.697×** | -3.1 | 0.048 | 10/38 (COLO 205, HEC-1-A, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **0.698×** | -3.1 | 0.048 | 14/36 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.05 µM |  | **0.700×** | -3.1 | 0.048 | 8/37 (NCI-H23, Panc 03.27, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.511×** | -3.0 | 0.057 | 15/33 (HCT15, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.787×** | -3.0 | 0.072 | 14/38 (COLO 205, KATO III, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.700×** | -2.9 | 0.077 | 7/36 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +2.36 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12083. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 50.7 | 10 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.42× (z +21.6) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 3.43× (z +12.5) | — |
| [[SW480 (line)]] | alt | 36.3 | 6 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +12.3) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.62× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 10.3 | 5 (5 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 9.14× (z +9.9) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[A-427 (line)]] | wt | 51.3 | 1 (1 ⚠) | 2 (2 ⚠) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 4.45× (z +8.6) ⚠ cell-cycle shift, explains ~63% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 8.41 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.83× (z +12.1) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 4.21× (z +8.5) | — |
| [[A-172 (line)]] | wt | 16.5 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM 0.0419× (z -12.1) |
| [[BT-474 (line)]] | alt | 36.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.18× (z +10.9) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[CFPAC-1 (line)]] | alt | 13.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +9.4) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[HEC-1-A (line)]] | alt | 53.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +8.8) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[HT-29 (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +8.6) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[KATO III (line)]] | alt | 41.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.129× (z -8.7) ⚠ cell-cycle shift, explains ~66% of this change |
| [[LoVo (line)]] | wt | 5.79 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.135× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 16.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.150× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 9.93 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 20.0× (z +9.7) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 1 | — | [[Cepharanthine (drug)]] 5 µM 0.202× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 17.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +8.6) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[A498 (line)]] | wt | 3.30 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.54 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.12 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.14 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12083), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM10]] | +0.91 | +0.88 / +0.94 | both halves | 7e-06 | **novel candidate** |
| [[CLSPN]] | +0.90 | +0.87 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[E2F1]] | +0.88 | +0.84 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[E2F2]] | +0.88 | +0.84 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[MCM4]] | +0.87 | +0.87 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[DTL]] | +0.87 | +0.82 / +0.89 | both halves | 7e-06 |  |
| [[CCNE2]] | +0.87 | +0.82 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[EXO1]] | +0.86 | +0.83 / +0.89 | both halves | 7e-06 |  |
| [[ESCO2]] | +0.86 | +0.82 / +0.89 | both halves | 7e-06 | STRING 508 |
| [[E2F8]] | +0.86 | +0.81 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[CDC25A]] | +0.84 | +0.80 / +0.86 | both halves | 7e-06 |  |
| [[CDC45]] | +0.84 | +0.80 / +0.86 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 5, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF724]] | B | ZNF724 activity raises FAM111B's level | lines that do not express ZNF724 (8) vs lines expressing it (42) | 1.99× lower at baseline in the lines without ZNF724 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000283201, ENSG00000269237, ZNF577 |
| [[TCF19]] | B | TCF19 activity raises FAM111B's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 3.43× lower at baseline in the lines without TCF19 | 0.036 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises FAM111B's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.43× lower at baseline in the lines without CDC25A | 0.050 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises FAM111B's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.52× lower at baseline in the lines without E2F2 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDCA7]] | B | CDCA7 activity raises FAM111B's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.43× lower at baseline in the lines without CDCA7 | 0.089 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[E2F8]] | C | E2F8 activity raises FAM111B's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 3.31× lower at baseline in the lines without E2F8 | 0.042 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent; co-absent with the target |
| [[BRME1]] | C | BRME1 activity raises FAM111B's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 2.56× lower at baseline in the lines without BRME1 | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent |
| [[CDC45]], [[CENPM]], [[SKA3]] | C | CDC45, CENPM, SKA3 activity raises FAM111B's level | lines that do not express CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 3.39× lower at baseline in the lines without CDC45, CENPM, SKA3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[MCM10]] | C | MCM10 activity raises FAM111B's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 3.04× lower at baseline in the lines without MCM10 | 0.092 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[TP53]] | C | TP53 activity weakens FAM111B's drug response | recorded loss-of-function mutation of TP53 in 27 lines vs 11 not recorded | the TP53-altered lines respond 1.31× as strongly (z diff -1.37); strongest at Mitoxantrone (dihydrochloride) 5 µM: 2.03x vs 1.15x (z diff -3.2) | 0.847 over the table, 0.066 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 37, C 2. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASF1B]] | B | FAM111B activity raises ASF1B's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 2.15× lower at baseline in the lines without FAM111B | 0.005 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[SKA3]] | B | FAM111B activity raises SKA3's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.79× lower at baseline in the lines without FAM111B | 0.013 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[RAD51AP1]] | B | FAM111B activity raises RAD51AP1's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 2.01× lower at baseline in the lines without FAM111B | 0.029 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[ZWINT]] | B | FAM111B activity raises ZWINT's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.60× lower at baseline in the lines without FAM111B | 0.031 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[SPC24]] | B | FAM111B activity raises SPC24's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without FAM111B | 0.031 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[FEN1]] | B | FAM111B activity raises FEN1's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.61× lower at baseline in the lines without FAM111B | 0.033 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[RMI1]] | B | FAM111B activity raises RMI1's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.44× lower at baseline in the lines without FAM111B | 0.037 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[GINS1]] | B | FAM111B activity raises GINS1's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.79× lower at baseline in the lines without FAM111B | 0.038 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[CDC6]] | B | FAM111B activity raises CDC6's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.67× lower at baseline in the lines without FAM111B | 0.040 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[DYNC2I2]] | B | FAM111B activity raises DYNC2I2's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.61× lower at baseline in the lines without FAM111B | 0.040 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[ZNF724]] | B | FAM111B activity raises ZNF724's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.77× lower at baseline in the lines without FAM111B | 0.040 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[MYBL2]] | B | FAM111B activity raises MYBL2's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.84× lower at baseline in the lines without FAM111B | 0.046 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.849). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.0, -44.8); signed map (-38.4, -46.0). **Vector** length 134, 44.0% of its response variance represented; |z| ≥ 3 in 1,185 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.65 to 65); *DNA strand elongation* (reactome, mean cos +0.70 to 28); *DNA Replication* (reactome, mean cos +0.70 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +6.7 | +9.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +4.8 | +11.9 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +4.8 | +5.5 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.7 | +4.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +4.5 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +7.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.7 | +3.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +3.2 | +1.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.1 | +4.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.9 | +3.6 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -5.1 | -8.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | -5.0 | -5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.5 | -3.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.3 | -3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | -4.2 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.2 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.0 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.3 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.1 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | FAM111 trypsin like peptidase B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:59,107,185-59,127,412 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CANP |
| Gene groups (HGNC) | FAM111 trypsin like peptidase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6SJ93](https://www.uniprot.org/uniprotkb/Q6SJ93) (Serine protease FAM111B):

> Serine protease.

**Summary**, from NCBI Gene [374393](https://www.ncbi.nlm.nih.gov/gene/374393):

> This gene encodes a protein with a trypsin-like cysteine/serine peptidase domain in the C-terminus. Mutations in this gene are associated with an autosomal dominant form of hereditary fibrosing poikiloderma (HFP). Affected individuals display mottled pigmentation, telangiectasia, epidermal atrophy, tendon contractures, and progressive pulmonary fibrosis. Alternative splicing results in multiple transcript variants encoding distinct isoforms. A paralog of this gene which also has a …

**Accessions** — [HGNC:24200](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24200) · Entrez [374393](https://www.ncbi.nlm.nih.gov/gene/374393) · UniProt [Q6SJ93](https://www.uniprot.org/uniprotkb/Q6SJ93) · Ensembl [ENSG00000189057](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189057)

## Data

Gene col 12083: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12083); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12083, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12083]; `tensor/DDL_lfc|DDL_z.npy` [12083]; `embed/gene_vectors.npy` [12083]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12083 or target_col == 12083). Every well: [[FAM111B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM111B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
