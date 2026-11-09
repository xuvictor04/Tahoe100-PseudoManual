---
symbol: "SUGCT"
type: "gene"
col: 10630
ensembl_id: "ENSG00000175600"
name: "succinyl-CoA:glutarate-CoA transferase"
location: "7p14.1"
module: 102
arm: "+"
pooled_cpm: 38.23
n_lines_expressing: 46
n_dd_up: 19
n_dd_down: 21
n_dd_up_clean: 14
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# SUGCT

*succinyl-CoA:glutarate-CoA transferase* — 7p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.97× (z +14.4, q 4e-44, up in 32 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.388× (z -14.2, q 5e-43, down in 37 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MEGF11]] (+0.65, fdr 1e-05), [[LINC01088]] (+0.61, fdr 1e-05), [[LINC02643]] (+0.55, fdr 1e-05); moves opposite to [[IFT122]] (-0.46, fdr 2e-04), [[HAUS3]] (-0.45, fdr 1e-04), [[BAD]] (-0.44, fdr 1e-04).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[FAM184A]] → it (grade B ⚠); 3 go from it, the strongest it → [[NPL]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10630.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +14.4 | 4e-44 | 32/44 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.95×** | +14.2 | 2e-43 | 38/44 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.15×** | +11.5 | 3e-28 | 33/44 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.11×** | +11.2 | 3e-27 | 36/44 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +10.2 | 2e-22 | 29/44 (A-172, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.94×** | +10.0 | 2e-21 | 32/44 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.54×** | +9.2 | 4e-18 | 30/44 (LOX-IMVI, A-427, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.59×** | +6.7 | 2e-09 | 25/44 (A498, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.51×** | +6.2 | 5e-08 | 24/44 (A-172, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +6.1 | 6e-08 | 26/44 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.3 | 5e-06 | 25/44 (A-172, A498, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +5.2 | 8e-06 | 22/44 (BT-474, HOP62, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +5.1 | 1e-05 | 21/44 (HS-578T, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.1 | 1e-05 | 22/44 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.35×** | +3.8 | 0.006 | 16/44 (HOP62, A-172, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.25×** | +3.4 | 0.026 | 10/44 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.3 | 0.033 | 5/44 (LOX-IMVI, LoVo, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.22×** | +3.0 | 0.079 | 13/44 (J82, A-172, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10630.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.388×** | -14.2 | 5e-43 | 37/44 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.417×** | -13.1 | 9e-37 | 38/44 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.436×** | -12.4 | 3e-33 | 31/44 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.566×** | -8.5 | 2e-15 | 33/44 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.418×** | -6.8 | 9e-10 | 28/44 (RPMI-7951, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.580×** | -6.8 | 9e-10 | 26/44 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.424×** | -6.7 | 1e-09 | 27/44 (C-33 A, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.649×** | -6.2 | 3e-08 | 25/44 (PANC-1, A-427, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.676×** | -5.6 | 1e-06 | 26/43 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | **0.691×** | -5.5 | 2e-06 | 26/43 (NCI-H23, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Vilanterol (drug)]] 5 µM |  | **0.772×** | -5.5 | 2e-06 | 28/44 (C-33 A, Panc 03.27, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.664×** | -5.1 | 1e-05 | 22/43 (PANC-1, SW 1271, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.749×** | -4.3 | 7e-04 | 20/44 (A-427, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.780×** | -3.7 | 0.008 | 21/44 (SNU-1, LoVo, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.788×** | -3.6 | 0.014 | 15/44 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.790×** | -3.4 | 0.025 | 17/43 (J82, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.799×** | -3.3 | 0.027 | 16/44 (NCI-H2030, SW 900, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.806×** | -3.2 | 0.040 | 17/44 (PANC-1, LoVo, …) | rises with dose |  |
| [[Cyclosporin A (drug)]] 5 µM |  | **0.811×** | -3.1 | 0.049 | 10/44 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.866× | -3.0 | 0.067 | 15/44 (CHP-212, SNU-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.820×** | -3.0 | 0.077 | 8/44 (PANC-1, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.62 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10630. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 72.1 | 1 (1 ⚠) | 13 (7 ⚠) | [[Selinexor (drug)]] 5 µM 2.23× (z +10.2) ⚠ cell-cycle shift, explains ~52% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0761× (z -23.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.253× (z -12.4) |
| [[NCI-H460 (line)]] | wt | 12.5 | 10 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.68× (z +13.9) | — |
| [[PANC-1 (line)]] | alt | 64.0 | 0 | 10 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.116× (z -18.9) |
| [[C-33 A (line)]] | alt | 145 | 0 | 9 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0897× (z -21.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -15.6) |
| [[NCI-H23 (line)]] | alt | 108 | 1 (1 ⚠) | 7 (4 ⚠) | [[Selinexor (drug)]] 5 µM 1.91× (z +8.7) ⚠ cell-cycle shift, explains ~52% of this change | [[Dinaciclib (drug)]] 5 µM 0.123× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.199× (z -15.5) |
| [[SNU-1 (line)]] | wt | 93.9 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0914× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -13.4) |
| [[A-172 (line)]] | wt | 16.6 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.56× (z +12.9) | — |
| [[LoVo (line)]] | wt | 99.7 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -15.5) |
| [[A498 (line)]] | wt | 33.5 | 5 (3 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.05× (z +14.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +11.4) | [[Harringtonine (drug)]] 5 µM 0.193× (z -12.0) ⚠ cell-cycle shift, explains ~70% of this change |
| [[AN3 CA (line)]] | alt | 109 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0487× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -11.2) |
| [[BT-474 (line)]] | alt | 26.4 | 5 | 1 | [[Tucidinostat (drug)]] 5 µM 8.92× (z +12.8) | [[Cobimetinib (drug)]] 0.5 µM 0.128× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 83.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -10.7) |
| [[SW480 (line)]] | alt | 28.1 | 3 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.55× (z +14.8) | [[Digitoxin (drug)]] 5 µM 0.332× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.342× (z -8.9) |
| [[HOP62 (line)]] | alt | 19.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +10.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.2 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +10.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 20.8 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 47.2 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.144× (z -15.0) |
| [[A549 (line)]] | wt | 9.56 | 3 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +9.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +8.8) | — |
| [[AsPC-1 (line)]] | alt | 17.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.13× (z +8.9) | — |
| [[C32 (line)]] | wt | 22.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +11.1) | — |
| [[CHP-212 (line)]] | wt | 78.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.116× (z -10.7) |
| [[H4 (line)]] | wt | 24.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 13.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 30.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 48.1 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.167× (z -13.0) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 18.6 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.86× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 79.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +9.2) | [[PH-797804 (drug)]] 5 µM 0.0718× (z -10.5) |
| [[SW1417 (line)]] | alt | 14.4 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.19× (z +11.7) | — |
| [[HCT15 (line)]] | alt | 10.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.28× (z +11.6) | — |
| [[HepG2_C3A (line)]] | wt | 28.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.24× (z +9.8) | — |
| [[HS-578T (line)]] | alt | 30.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +12.2) | — |
| [[hTERT-HPNE (line)]] | wt | 57.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 76.9 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.28× (z +10.6) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[NCI-H2122 (line)]] | alt | 29.1 | 0 | 1 | — | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.194× (z -31.4) |
| [[NCI-H661 (line)]] | alt | 60.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0794× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 22.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.01× (z +8.8) | — |
| [[SW48 (line)]] | wt | 78.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.27× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.41 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.44 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.31 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.18 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10630), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEGF11]] | +0.65 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[LINC01088]] | +0.61 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[LINC02643]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[NKAIN1]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[LAMA2]] | +0.54 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ADAMTS7]] | +0.54 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[GPM6B]] | +0.53 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[GNAL]] | +0.52 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[SYN2]] | +0.51 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[MED12L]] | +0.51 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[DZIP1]] | +0.51 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ZNF536]] | +0.50 | +0.43 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT122]] | -0.46 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[HAUS3]] | -0.45 | -0.32 / -0.37 | both halves | 1e-04 |  |
| [[BAD]] | -0.44 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[DZANK1]] | -0.43 | -0.24 / -0.38 | both halves | 5e-04 |  |
| [[MIGA2]] | -0.42 | -0.30 / -0.33 | both halves | 2e-04 |  |
| [[CDAN1]] | -0.42 | -0.41 / -0.31 | both halves | 2e-04 |  |
| [[DHTKD1]] | -0.42 | -0.41 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM184A]] | B | FAM184A activity raises SUGCT's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 2.63× lower at baseline in the lines without FAM184A | 0.003 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SUGCT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00839]] | B | LINC00839 activity raises SUGCT's level | lines that do not express LINC00839 (24) vs lines expressing it (26) | 1.87× lower at baseline in the lines without LINC00839 | 0.018 | ⚠ within organs, on part of the lines; also absent: PRR16, CCNYL2, PCDH10 |
| [[DOCK3]] | B | DOCK3 activity raises SUGCT's level | lines that do not express DOCK3 (22) vs lines expressing it (28) | 2.01× lower at baseline in the lines without DOCK3 | 0.061 | ⚠ within organs, on part of the lines; also absent: RBM20, LHX2, ADCY1 |
| [[SYN2]] | B | SYN2 activity raises SUGCT's level | lines that do not express SYN2 (23) vs lines expressing it (27) | 1.61× lower at baseline in the lines without SYN2 | 0.068 | ⚠ within organs, on part of the lines; also absent: ACP7, PRRX2, LINC01357; maybe low, not absent |
| [[LINC01088]] | B | LINC01088 activity raises SUGCT's level | lines that do not express LINC01088 (9) vs lines expressing it (41) | 2.59× lower at baseline in the lines without LINC01088 | 0.070 | ⚠ within organs, on part of the lines; also absent: PPP4R4, GPR155, PKIG; maybe low, not absent |
| [[KATNAL2]] | B | KATNAL2 activity raises SUGCT's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 2.58× lower at baseline in the lines without KATNAL2 | 0.092 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPL]] | C | SUGCT activity lowers NPL's level | lines that do not express SUGCT (4) vs lines expressing it (46) | 1.38× higher at baseline in the lines without SUGCT | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, CABYR, HHAT; maybe low, not absent; its own permutation p |
| [[SALL4]] | C | SUGCT activity raises SALL4's level | lines that do not express SUGCT (4) vs lines expressing it (46) | 1.00× lower at baseline in the lines without SUGCT | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, CABYR, HHAT; maybe low, not absent; its own permutation p |
| [[TRAF3]] | C | SUGCT activity raises TRAF3's level | lines that do not express SUGCT (4) vs lines expressing it (46) | 2.01× lower at baseline in the lines without SUGCT | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, CABYR, HHAT; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.611). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.3, 34.3); signed map (41.5, -5.8). **Vector** length 101, 27.8% of its response variance represented; |z| ≥ 3 in 1,421 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.5 | +14.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.5 | +11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.5 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.9 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +3.4 |
|  | [[Norepinephrine (hydrochloride) (drug)]] 5 µM |  | +1.7 | +2.7 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -3.5 | -3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -3.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.7 | -5.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.7 | +5.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -1.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -0.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | succinyl-CoA:glutarate-CoA transferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.1 — chr7:40,135,005-40,860,763 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11808, ORF19, DERP13; previously C7orf10 |
| Gene groups (HGNC) | Flavoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAC7](https://www.uniprot.org/uniprotkb/Q9HAC7) (Succinyl-CoA:glutarate CoA-transferase):

> Coenzyme A (CoA) transferase that reversibly catalyzes the transfer of a CoA moiety from a dicarboxyl-CoA to a dicarboxylate in a metabolite recycling process. Displays preference for succinyl-CoA and glutarate-CoA as dicarboxyl-CoA donors and glutarate, succinate, adipate/hexanedioate, itaconate and 3-hydroxy-3-methylglutarate as dicarboxylate acceptors. Acts on intermediates or end products of lysine and tryptophan degradation pathway, in particular catalyzes succinyl-CoA-dependent …

**Summary**, from NCBI Gene [79783](https://www.ncbi.nlm.nih.gov/gene/79783):

> This gene encodes a protein that is similar to members of the CaiB/baiF CoA-transferase protein family. Mutations in this gene are associated with glutaric aciduria type III. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jul 2010]

**Accessions** — [HGNC:16001](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16001) · Entrez [79783](https://www.ncbi.nlm.nih.gov/gene/79783) · UniProt [Q9HAC7](https://www.uniprot.org/uniprotkb/Q9HAC7) · Ensembl [ENSG00000175600](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175600)

## Data

Gene col 10630: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10630); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10630, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10630]; `tensor/DDL_lfc|DDL_z.npy` [10630]; `embed/gene_vectors.npy` [10630]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10630 or target_col == 10630). Every well: [[SUGCT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUGCT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
