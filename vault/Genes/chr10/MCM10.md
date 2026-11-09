---
symbol: "MCM10"
type: "gene"
col: 782
ensembl_id: "ENSG00000065328"
name: "minichromosome maintenance 10 replication initiation factor"
location: "10p13"
module: 6
arm: "+"
pooled_cpm: 16.59
n_lines_expressing: 46
n_dd_up: 50
n_dd_down: 35
n_dd_up_clean: 13
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 7
direction_downstream: 69
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MCM10

*minichromosome maintenance 10 replication initiation factor* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 50 drug-doses (37 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 4.26× (z +16.6, q 0e+00, up in 40 of 43 measured lines) ⚠ cell-cycle shift, explains ~77% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.38× (z +5.1, q 7e-06, up in 17 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (13 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.663× (z -6.6, q 2e-08, down in 30 of 44 measured lines) ⚠ cell-cycle shift, explains ~79% of this change. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.732× (z -4.1, q 0.003, down in 17 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLSPN]] (+0.92, fdr 7e-06), [[CDC45]] (+0.92, fdr 7e-06), [[DTL]] (+0.92, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); 69 go from it, the strongest it → [[PCLAF]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 37 with an alert ⚠; shown: the 15 strongest and the 14 next strongest without an alert. 50 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 37 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 782.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **4.26×** | +16.6 | 0e+00 | 40/43 (A549, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **4.12×** | +16.2 | 0e+00 | 39/43 (A549, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **3.85×** | +15.4 | 0e+00 | 39/43 (A549, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **2.22×** | +9.1 | 1e-17 | 32/43 (J82, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **2.15×** | +8.7 | 3e-16 | 29/43 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~73% of this change | **2.20×** | +8.7 | 3e-16 | 26/34 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.07×** | +8.3 | 7e-15 | 30/41 (HOP62, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.05×** | +8.2 | 1e-14 | 32/40 (SW480, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.04×** | +7.8 | 3e-13 | 30/43 (J82, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.02×** | +7.7 | 6e-13 | 17/23 (NCI-H460, A498, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.93×** | +7.5 | 2e-12 | 29/43 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.98×** | +7.5 | 3e-12 | 23/40 (PANC-1, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.99×** | +7.3 | 1e-11 | 17/30 (A549, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.89×** | +7.3 | 2e-11 | 20/35 (A498, HT-29, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.88×** | +6.9 | 2e-10 | 25/42 (SW480, J82, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.1 | 7e-06 | 17/44 (J82, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.42×** | +3.7 | 0.004 | 14/39 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.007 | 13/43 (LOX-IMVI, SNU-423, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.024 | 10/44 (SHP-77, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.024 | 15/43 (HOP62, A549, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.028 | 9/44 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +2.9 | 0.053 | 9/43 (SW480, A-427, …) | top dose only | plate-row cell shift |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.30×** | +2.9 | 0.057 | 6/43 (BT-474, PANC-1, …) | top dose only |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.28×** | +2.8 | 0.062 | 10/41 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Olanzapine (drug)]] 5 µM |  | 1.18× | +2.7 | 0.083 | 3/44 (CFPAC-1, SW 1271, …) | top dose only | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.29×** | +2.7 | 0.083 | 5/43 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **1.26×** | +2.7 | 0.090 | 7/43 (A498, A-427, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.26×** | +2.7 | 0.090 | 5/43 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.26×** | +2.7 | 0.091 | 5/41 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 13 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 782.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.663×** | -6.6 | 2e-08 | 30/44 (COLO 205, RKO, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.469×** | -6.2 | 2e-07 | 23/44 (SW480, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.612×** | -5.6 | 4e-06 | 22/42 (A-427, A498, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.726×** | -5.1 | 4e-05 | 22/44 (A-427, NCI-H460, …) | all doses, flat | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.580×** | -5.1 | 4e-05 | 22/44 (A-427, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.652×** | -4.7 | 2e-04 | 21/41 (SK-MEL-2, RKO, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.670×** | -4.6 | 4e-04 | 17/44 (PANC-1, LOX-IMVI, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.658×** | -4.5 | 4e-04 | 19/44 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.732×** | -4.1 | 0.003 | 17/44 (A-427, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.692×** | -4.1 | 0.003 | 15/41 (A-427, HEC-1-A, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.609×** | -4.0 | 0.003 | 12/44 (NCI-H23, NCI-H2030, …) | two highest doses | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.622×** | -3.9 | 0.005 | 15/44 (SW480, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.718×** | -3.8 | 0.006 | 19/43 (RKO, KATO III, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.707×** | -3.8 | 0.007 | 17/41 (A-427, KATO III, …) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.723×** | -3.5 | 0.017 | 9/43 (RKO, NCI-H460, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.755×** | -3.2 | 0.046 | 13/43 (RKO, KATO III, …) | top dose only |  |
| [[Rifaximin (drug)]] 5 µM |  | **0.749×** | -3.2 | 0.049 | 7/42 (AN3 CA, H4, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.818×** | -3.2 | 0.050 | 13/44 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.761×** | -3.1 | 0.053 | 10/43 (A-172, A498, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.763×** | -3.1 | 0.054 | 13/43 (A-427, SW 900, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.766×** | -3.1 | 0.054 | 19/43 (H4, A-172, …) | rises with dose | low cells (technical?) |
| [[Rapamycin (drug)]] 5 µM |  | **0.828×** | -3.0 | 0.054 | 11/44 (NCI-H2030, NCI-H23, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.520×** | -3.0 | 0.062 | 5/44 (Hs 766T, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Posaconazole (drug)]] 5 µM |  | **0.762×** | -3.0 | 0.062 | 13/43 (HT-29, A-172, …) | top dose only | plate-row cell shift |
| [[palbociclib (drug)]] 5 µM |  | **0.527×** | -2.9 | 0.069 | 9/41 (SW480, HEC-1-A, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.91 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 782. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 49.7 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -14.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ponatinib (drug)]] 0.5 µM 0.277× (z -8.6) |
| [[J82 (line)]] | alt | 44.8 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +14.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW480 (line)]] | alt | 26.8 | 5 (5 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.79× (z +12.3) ⚠ toxic; cell-cycle shift, explains ~73% of this change | — |
| [[A549 (line)]] | wt | 6.78 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 16.3× (z +10.5) ⚠ cell-cycle shift, explains ~91% of this change | [[Canagliflozin (drug)]] 0.05 µM 0.0728× (z -9.1) |
| [[PANC-1 (line)]] | alt | 13.6 | 3 (3 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.59× (z +9.2) ⚠ toxic; cell-cycle shift, explains ~73% of this change | — |
| [[A498 (line)]] | wt | 12.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.36× (z +8.8) ⚠ cell-cycle shift, explains ~91% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.158× (z -8.9) ⚠ cell-cycle shift, explains ~41% of this change |
| [[LoVo (line)]] | wt | 10.7 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.57× (z +8.8) ⚠ cell-cycle shift, explains ~91% of this change | — |
| [[LOX-IMVI (line)]] | wt | 8.62 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.29× (z +9.1) ⚠ cell-cycle shift, explains ~91% of this change | — |
| [[SW48 (line)]] | wt | 24.3 | 0 | 2 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0777× (z -10.6) ⚠ cell-cycle shift, explains ~58% of this change |
| [[A-172 (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.155× (z -8.6) ⚠ cell-cycle shift, explains ~58% of this change |
| [[C-33 A (line)]] | alt | 55.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 10.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.08× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[Hs 766T (line)]] | wt | 6.41 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0605× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 15.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 782), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLSPN]] | +0.92 | +0.92 / +0.92 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 977 |
| [[CDC45]] | +0.92 | +0.91 / +0.90 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 999 |
| [[DTL]] | +0.92 | +0.90 / +0.91 | both halves | 7e-06 | STRING 915 |
| [[EXO1]] | +0.92 | +0.91 / +0.91 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 954 |
| [[E2F1]] | +0.92 | +0.89 / +0.92 | both halves | 7e-06 | pathway: G1/S Transition; STRING 458 |
| [[WDR76]] | +0.91 | +0.92 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[CDC25A]] | +0.91 | +0.91 / +0.91 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 850 |
| [[FAM111B]] | +0.91 | +0.88 / +0.94 | both halves | 7e-06 | **novel candidate** |
| [[GINS1]] | +0.90 | +0.87 / +0.89 | both halves | 7e-06 | pathway: DNA Replication; STRING 965 |
| [[E2F2]] | +0.89 | +0.86 / +0.90 | both halves | 7e-06 | pathway: Mitotic G1 phase and G1/S transition; STRING 502 |
| [[CHAF1A]] | +0.88 | +0.90 / +0.86 | both halves | 7e-06 | STRING 456 |
| [[CENPM]] | +0.88 | +0.86 / +0.87 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 684 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises MCM10's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.51× lower at baseline in the lines without E2F2 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MCM10's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TERT]] | B | TERT activity raises MCM10's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.60× lower at baseline in the lines without TERT | 0.095 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[CDC25A]] | C | CDC25A activity raises MCM10's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.85× lower at baseline in the lines without CDC25A | 0.048 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent; co-absent with the target |
| [[TCF19]] | C | TCF19 activity raises MCM10's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.79× lower at baseline in the lines without TCF19 | 0.060 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent; co-absent with the target |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises MCM10's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 3.18× lower at baseline in the lines without E2F1, MCM3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[MYBL2]] | C | MYBL2 activity raises MCM10's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 3.02× lower at baseline in the lines without MYBL2 | 0.0996 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent |

### Downstream of this gene

*69 arrows, 69 of them with an alert ⚠; grade A 0, B 0, C 69. Shown: the 12 strongest; 57 more arrows (57 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCLAF]] | C | MCM10 activity raises PCLAF's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.71× lower at baseline in the lines without MCM10 | 0.004 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target |
| [[PCNA]] | C | MCM10 activity raises PCNA's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.78× lower at baseline in the lines without MCM10 | 0.006 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target |
| [[BRIP1]] | C | MCM10 activity raises BRIP1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.72× lower at baseline in the lines without MCM10 | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[DIAPH3]] | C | MCM10 activity raises DIAPH3's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 3.07× lower at baseline in the lines without MCM10 | 0.013 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[SKA3]] | C | MCM10 activity raises SKA3's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.92× lower at baseline in the lines without MCM10 | 0.014 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[MND1]] | C | MCM10 activity raises MND1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.60× lower at baseline in the lines without MCM10 | 0.020 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[MCM4]] | C | MCM10 activity raises MCM4's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 3.01× lower at baseline in the lines without MCM10 | 0.020 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target |
| [[ZWINT]] | C | MCM10 activity raises ZWINT's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.47× lower at baseline in the lines without MCM10 | 0.021 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[GMNN]] | C | MCM10 activity raises GMNN's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.28× lower at baseline in the lines without MCM10 | 0.022 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[UBE2T]] | C | MCM10 activity raises UBE2T's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.35× lower at baseline in the lines without MCM10 | 0.027 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[CDCA4]] | C | MCM10 activity raises CDCA4's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.22× lower at baseline in the lines without MCM10 | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[RMI1]] | C | MCM10 activity raises RMI1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without MCM10 | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.916). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.3, -45.0); signed map (-38.3, -45.1). **Vector** length 126, 40.2% of its response variance represented; |z| ≥ 3 in 1,393 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.69 to 65); *DNA strand elongation* (reactome, mean cos +0.76 to 28); *E2F G1/S* (control, mean cos +0.76 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +5.8 | +8.7 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.4 | +3.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.3 | +8.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~73% of this change | +4.3 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.2 | +7.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.1 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.7 | +3.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.7 | +2.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.7 | +3.1 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +2.6 | +2.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.0 | -5.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -4.5 | -6.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.3 | -5.6 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | -4.2 | -6.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.1 | -2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.0 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.9 | -1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | minichromosome maintenance 10 replication initiation factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:13,161,558-13,211,110 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRO2249, CNA43, DNA43 |
| Reactome | 10 pathways, smallest: Activation of the pre-replicative complex; Activation of ATR in response to replication stress; DNA Replication Pre-Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L590](https://www.uniprot.org/uniprotkb/Q7L590) (Protein MCM10 homolog):

> Acts as a replication initiation factor that brings together the MCM2-7 helicase and the DNA polymerase alpha/primase complex in order to initiate DNA replication. Additionally, plays a role in preventing DNA damage during replication. Key effector of the RBBP6 and ZBTB38-mediated regulation of DNA-replication and common fragile sites stability; acts as a direct target of transcriptional repression by ZBTB38.

**Summary**, from NCBI Gene [55388](https://www.ncbi.nlm.nih.gov/gene/55388):

> The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre-RC) and it may be involved in the formation of replication forks and in the recruitment of other DNA replication related proteins. This protein can interact with MCM2 and MCM6, as well as with the origin …

**Accessions** — [HGNC:18043](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18043) · Entrez [55388](https://www.ncbi.nlm.nih.gov/gene/55388) · UniProt [Q7L590](https://www.uniprot.org/uniprotkb/Q7L590) · Ensembl [ENSG00000065328](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065328)

## Data

Gene col 782: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 782); `tables/drug_effects.parquet` (89 rows, flagged included); `relations/gene_relations.parquet` (col_a == 782, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 782]; `tensor/DDL_lfc|DDL_z.npy` [782]; `embed/gene_vectors.npy` [782]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 782 or target_col == 782). Every well: [[MCM10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCM10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
