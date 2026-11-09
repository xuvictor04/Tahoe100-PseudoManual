---
symbol: "ITGA6"
type: "gene"
col: 1661
ensembl_id: "ENSG00000091409"
name: "integrin subunit alpha 6"
location: "2q31.1"
module: 34
arm: "+"
pooled_cpm: 316.02
n_lines_expressing: 41
n_dd_up: 20
n_dd_down: 29
n_dd_up_clean: 9
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 56
direction_downstream: 22
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# ITGA6

*integrin subunit alpha 6* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.19× (z +14.1, q 4e-42, up in 32 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.55× (z +11.1, q 3e-26, up in 28 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.571× (z -9.2, q 2e-17, down in 34 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITPRID2]] (+0.76, fdr 7e-06), [[MYEOV]] (+0.70, fdr 7e-06), [[EPHA2]] (+0.69, fdr 7e-06); moves opposite to [[HEIH]] (-0.55, fdr 1e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 56 arrows point to it, the strongest [[FAM110C]] → it (grade B ⚠); 22 go from it, the strongest it → [[CD59]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1661.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.19×** | +14.1 | 4e-42 | 32/40 (SK-MEL-2, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.10×** | +12.8 | 6e-35 | 30/36 (SK-MEL-2, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.97×** | +11.3 | 3e-27 | 29/36 (SK-MEL-2, C32, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +11.1 | 3e-26 | 28/39 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +6.0 | 3e-07 | 23/39 (NCI-H23, HCT15, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.37×** | +5.6 | 1e-06 | 18/39 (NCI-H2030, HCT15, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +5.6 | 1e-06 | 18/40 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.4 | 4e-06 | 17/39 (hTERT-HPNE, NCI-H2347, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +4.7 | 2e-04 | 29/39 (COLO 205, SK-MEL-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.28×** | +4.5 | 5e-04 | 19/39 (HCT15, NCI-H23, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.27×** | +4.4 | 7e-04 | 21/38 (NCI-H1573, HepG2/C3A, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.006 | 19/38 (NCI-H460, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.23×** | +3.8 | 0.007 | 20/39 (AsPC-1, HepG2/C3A, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.018 | 16/39 (HepG2/C3A, Panc 03.27, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.21×** | +3.4 | 0.021 | 17/39 (AsPC-1, hTERT-HPNE, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.037 | 18/38 (NCI-H1573, HepG2/C3A, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.50×** | +3.0 | 0.065 | 17/39 (HT-29, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.073 | 14/39 (HepG2/C3A, HCT15, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 1.17× | +2.9 | 0.093 | 6/39 (HCT15, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1661.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.571×** | -9.2 | 2e-17 | 34/41 (LOX-IMVI, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.661×** | -9.1 | 2e-17 | 33/39 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.601×** | -9.1 | 2e-17 | 33/40 (SW480, LOX-IMVI, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.622×** | -7.8 | 6e-13 | 30/39 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.653×** | -7.6 | 4e-12 | 30/40 (SW480, SW48, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.646×** | -7.5 | 6e-12 | 32/39 (LOX-IMVI, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.660×** | -7.1 | 7e-11 | 31/38 (LOX-IMVI, SW48, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.721×** | -7.1 | 7e-11 | 29/39 (SW480, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.739×** | -7.1 | 1e-10 | 30/39 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.701×** | -6.3 | 1e-08 | 27/38 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.771×** | -5.8 | 4e-07 | 28/40 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.814×** | -5.2 | 1e-05 | 23/39 (KATO III, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 5 µM |  | **0.534×** | -4.6 | 2e-04 | 25/41 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.710×** | -4.6 | 2e-04 | 25/39 (SW480, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -4.6 | 2e-04 | 4/41 (NCI-H23, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.777×** | -4.5 | 2e-04 | 21/39 (CFPAC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1661. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 693 | 1 | 17 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.62× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.399× (z -14.2) |
| [[LOX-IMVI (line)]] | wt | 351 | 2 (2 ⚠) | 9 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.04× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Trametinib (drug)]] 5 µM 0.271× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 222 | 4 (2 ⚠) | 6 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.03× (z +9.5) | [[Harringtonine (drug)]] 5 µM 0.425× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.576× (z -10.5) |
| [[SW48 (line)]] | wt | 567 | 0 | 10 (2 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.299× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 330 | 0 | 9 | — | [[Trametinib (drug)]] 5 µM 0.331× (z -10.5) |
| [[Hs 766T (line)]] | wt | 1,006 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -16.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.328× (z -16.1) |
| [[AsPC-1 (line)]] | alt | 753 | 6 (4 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +14.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.97× (z +12.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.472× (z -9.4) ⚠ toxic · without an alert: [[Cobimetinib (drug)]] 5 µM 0.503× (z -8.6) |
| [[KATO III (line)]] | alt | 1,019 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -20.8) |
| [[LoVo (line)]] | wt | 864 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -13.3) |
| [[LS 180 (line)]] | wt | 1,502 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.426× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 143 | 0 | 7 | — | [[Trametinib (drug)]] 5 µM 0.278× (z -9.8) |
| [[PANC-1 (line)]] | alt | 186 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 505 | 0 | 6 | — | [[Trametinib (drug)]] 5 µM 0.303× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 79.3 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.85× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.63× (z +11.0) | — |
| [[A-172 (line)]] | wt | 183 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.82× (z +9.4) | — |
| [[C32 (line)]] | wt | 90.6 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.05× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.40× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 110 | 4 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Adagrasib (drug)]] 0.05 µM 0.664× (z -13.5) ⚠ position not correctable |
| [[SK-MEL-2 (line)]] | alt | 132 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.17× (z +17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -10.0) |
| [[A-427 (line)]] | wt | 163 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.2) | — |
| [[A549 (line)]] | wt | 150 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Trametinib (drug)]] 5 µM 0.412× (z -9.5) |
| [[H4 (line)]] | wt | 145 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -15.0) |
| [[NCI-H23 (line)]] | alt | 146 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.98× (z +12.0) | [[Ixazomib citrate (drug)]] 5 µM 0.400× (z -10.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H2347 (line)]] | alt | 105 | 4 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 1.91× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 91.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.46× (z +10.7) | — |
| [[C-33 A (line)]] | alt | 103 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HOP62 (line)]] | alt | 95.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[SNU-1 (line)]] | wt | 190 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.214× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.477× (z -8.8) |
| [[BT-474 (line)]] | alt | 82.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.71× (z +13.8) | — |
| [[COLO 205 (line)]] | alt | 718 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 180 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.81× (z +9.7) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[HT-29 (line)]] | alt | 380 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.365× (z -8.9) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 213 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.54× (z +8.8) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[Panc 03.27 (line)]] | alt | 331 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW 1088 (line)]] | alt | 115 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0894× (z -8.6) |
| [[SW1417 (line)]] | alt | 438 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 64.4 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 146 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 66.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 296 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 48.8 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 58.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 303 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.6 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 47.4 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 76.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 21.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 70.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1661), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITPRID2]] | +0.76 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[MYEOV]] | +0.70 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[EPHA2]] | +0.69 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[PRAG1]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[PSD3]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[LAMC2]] | +0.68 | +0.69 / +0.64 | both halves | 7e-06 | pathway: Assembly of collagen fibrils and other multimeric structures; STRING 898 |
| [[ITGB1]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 | same gene group; pathway: Basigin interactions; STRING 999 |
| [[ASAP2]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[MPRIP]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[PLEK2]] | +0.66 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[TINAGL1]] | +0.66 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[EMP1]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEIH]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*56 arrows, 56 of them with an alert ⚠; grade A 0, B 55, C 1. Shown: the 12 strongest; 44 more arrows (44 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM110C]] | B | FAM110C activity raises ITGA6's level | lines that do not express FAM110C (26) vs lines expressing it (24) | 3.45× lower at baseline in the lines without FAM110C | 6e-04 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |
| [[SERPINB5]] | B | SERPINB5 activity raises ITGA6's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 3.76× lower at baseline in the lines without SERPINB5 | 0.001 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[KRT15]] | B | KRT15 activity raises ITGA6's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.84× lower at baseline in the lines without KRT15 | 0.003 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[GPR39]] | B | GPR39 activity raises ITGA6's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 2.66× lower at baseline in the lines without GPR39 | 0.003 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[ITGA2]] | B | ITGA2 activity raises ITGA6's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without ITGA2 | 0.004 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[SH2D3A]] | B | SH2D3A activity raises ITGA6's level | lines that do not express SH2D3A (24) vs lines expressing it (26) | 2.75× lower at baseline in the lines without SH2D3A | 0.004 | ⚠ within organs, on part of the lines; also absent: GRB7, MYO5B, CRB3 |
| [[TNS4]] | B | TNS4 activity raises ITGA6's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 3.84× lower at baseline in the lines without TNS4 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[SHH]] | B | SHH activity raises ITGA6's level | lines that do not express SHH (29) vs lines expressing it (21) | 3.49× lower at baseline in the lines without SHH | 0.005 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3 |
| [[ITGB4]] | B | ITGB4 activity raises ITGA6's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 3.14× lower at baseline in the lines without ITGB4 | 0.006 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[PRKCA]] | B | PRKCA activity raises ITGA6's level | lines that do not express PRKCA (5) vs lines expressing it (45) | 3.78× lower at baseline in the lines without PRKCA | 0.006 | ⚠ within organs, on part of the lines; also absent: TMEM51, ITGA2-AS1; maybe low, not absent |
| [[LAMA3]] | B | LAMA3 activity raises ITGA6's level | lines that do not express LAMA3 (22) vs lines expressing it (28) | 2.64× lower at baseline in the lines without LAMA3 | 0.006 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B |
| [[PPARG]] | B | PPARG activity raises ITGA6's level | lines that do not express PPARG (20) vs lines expressing it (30) | 1.97× lower at baseline in the lines without PPARG | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000271933, LINC01589, NUP62CL |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 21, C 1. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD59]] | B | ITGA6 activity raises CD59's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 2.00× lower at baseline in the lines without ITGA6 | 0.007 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ITGA2]] | B | ITGA6 activity raises ITGA2's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 2.93× lower at baseline in the lines without ITGA6 | 0.008 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DIAPH1]] | B | ITGA6 activity raises DIAPH1's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 1.54× lower at baseline in the lines without ITGA6 | 0.021 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MAML3]] | B | ITGA6 activity raises MAML3's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 1.99× lower at baseline in the lines without ITGA6 | 0.024 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ITPRID2]] | B | ITGA6 activity raises ITPRID2's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 1.48× lower at baseline in the lines without ITGA6 | 0.026 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PLCXD2]] | B | ITGA6 activity raises PLCXD2's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 2.27× lower at baseline in the lines without ITGA6 | 0.034 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ANXA2]] | B | ITGA6 activity raises ANXA2's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 1.60× lower at baseline in the lines without ITGA6 | 0.037 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[GPR39]] | B | ITGA6 activity raises GPR39's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 2.35× lower at baseline in the lines without ITGA6 | 0.041 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SH2D3A]] | B | ITGA6 activity raises SH2D3A's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 3.21× lower at baseline in the lines without ITGA6 | 0.048 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PLEK2]] | B | ITGA6 activity raises PLEK2's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 3.13× lower at baseline in the lines without ITGA6 | 0.052 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PRKCA]] | B | ITGA6 activity raises PRKCA's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 1.59× lower at baseline in the lines without ITGA6 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TNS4]] | B | ITGA6 activity raises TNS4's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 3.74× lower at baseline in the lines without ITGA6 | 0.063 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.736). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.5, 4.1); signed map (3.6, 42.0). **Vector** length 155, 54.1% of its response variance represented; |z| ≥ 3 in 1,689 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +14.0 | +11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +10.1 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +10.0 | +14.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.5 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +9.3 | +11.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.4 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.1 | +4.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +3.0 | +2.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -9.1 | -9.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.7 | -9.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.5 | -9.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -7.5 | -7.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -7.1 | -7.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -6.9 | -7.1 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit alpha 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:172,234,216-172,506,459 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD49f, VLA-6, ITGA6A, ITGA6B |
| Gene groups (HGNC) | CD molecules; Integrin alpha subunits |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 13 pathways, smallest: Type I hemidesmosome assembly; Basigin interactions; Syndecan interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P23229](https://www.uniprot.org/uniprotkb/P23229) (Integrin alpha-6):

> Integrin alpha-6/beta-1 (ITGA6:ITGB1) is a receptor for laminin on platelets (By similarity). Integrin alpha-6/beta-1 (ITGA6:ITGB1) is present in oocytes and is involved in sperm-egg fusion (By similarity). Integrin alpha-6/beta-4 (ITGA6:ITGB4) is a receptor for laminin in epithelial cells and it plays a critical structural role in the hemidesmosome (By similarity). ITGA6:ITGB4 binds to NRG1 (via EGF domain) and this binding is essential for NRG1-ERBB signaling. ITGA6:ITGB4 binds to IGF1 and …

**Summary**, from NCBI Gene [3655](https://www.ncbi.nlm.nih.gov/gene/3655):

> The gene encodes a member of the integrin alpha chain family of proteins. Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain that function in cell surface adhesion and signaling. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha 6 subunit. This subunit may associate with a beta 1 or beta 4 subunit to form an integrin that interacts with extracellular matrix proteins including members …

**Accessions** — [HGNC:6142](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6142) · Entrez [3655](https://www.ncbi.nlm.nih.gov/gene/3655) · UniProt [P23229](https://www.uniprot.org/uniprotkb/P23229) · Ensembl [ENSG00000091409](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091409)

## Data

Gene col 1661: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1661); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1661, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1661]; `tensor/DDL_lfc|DDL_z.npy` [1661]; `embed/gene_vectors.npy` [1661]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1661 or target_col == 1661). Every well: [[ITGA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
