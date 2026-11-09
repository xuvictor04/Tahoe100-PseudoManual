---
symbol: "NDC80"
type: "gene"
col: 1299
ensembl_id: "ENSG00000080986"
name: "NDC80 kinetochore complex component"
location: "18p11.32"
module: 22
arm: "+"
pooled_cpm: 50.85
n_lines_expressing: 47
n_dd_up: 20
n_dd_down: 37
n_dd_up_clean: 4
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 8
direction_downstream: 77
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# NDC80

*NDC80 kinetochore complex component* — 18p11.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.98× (z +13.6, q 1e-39, up in 32 of 45 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 0.05 µM: 1.25× (z +3.5, q 0.021, up in 11 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (20 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.444× (z -12.6, q 2e-33, down in 39 of 45 measured lines) ⚠ cell-cycle shift, explains ~72% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.625× (z -7.3, q 3e-11, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KNL1]] (+0.94, fdr 7e-06), [[SGO1]] (+0.94, fdr 7e-06), [[CDCA8]] (+0.93, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); 77 go from it, the strongest it → [[FOXM1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1299.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.98×** | +13.6 | 1e-39 | 32/45 (RKO, NCI-H2030, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **2.35×** | +13.2 | 1e-37 | 38/45 (KATO III, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **2.05×** | +11.1 | 1e-26 | 38/44 (KATO III, C-33 A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.88×** | +9.8 | 2e-20 | 35/45 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.78×** | +9.0 | 3e-17 | 36/45 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.77×** | +8.9 | 6e-17 | 36/44 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.77×** | +8.5 | 1e-15 | 34/45 (NCI-H2347, PANC-1, …) | inconsistent across doses | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **2.31×** | +6.8 | 8e-10 | 31/44 (J82, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.38×** | +6.7 | 1e-09 | 36/45 (NCI-H23, NCI-H1573, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.47×** | +6.0 | 1e-07 | 31/45 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.39×** | +5.2 | 1e-05 | 18/43 (NCI-H2030, PANC-1, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +4.5 | 4e-04 | 20/45 (HS-578T, NCI-H2030, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +3.8 | 0.007 | 19/45 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.021 | 11/45 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +3.4 | 0.022 | 12/45 (NCI-H2030, HT-29, …) | all doses, flat |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.037 | 14/45 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.037 | 13/45 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.17× | +3.2 | 0.040 | 15/45 (HT-29, NCI-H2030, …) | all doses, flat |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.042 | 12/45 (MIA PaCa-2, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 20 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1299.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.444×** | -12.6 | 2e-33 | 39/45 (A-172, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.556×** | -11.7 | 6e-29 | 34/45 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.410×** | -11.5 | 2e-28 | 39/45 (PANC-1, HEC-1-A, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.541×** | -9.5 | 3e-19 | 34/45 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.597×** | -8.0 | 2e-13 | 38/45 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **0.376×** | -7.9 | 2e-13 | 30/40 (A-427, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.625×** | -7.3 | 3e-11 | 29/45 (HOP62, HCT15, …) | top dose only |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.593×** | -5.8 | 6e-07 | 27/45 (SW480, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.698×** | -5.6 | 2e-06 | 25/45 (SW48, A-172, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.699×** | -5.5 | 2e-06 | 28/45 (HEC-1-A, J82, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.699×** | -5.5 | 2e-06 | 24/45 (SW48, H4, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.785×** | -5.4 | 4e-06 | 21/45 (A-427, A498, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.798×** | -4.7 | 1e-04 | 19/45 (LOX-IMVI, LS 180, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.795×** | -4.7 | 1e-04 | 23/45 (NCI-H23, H4, …) | two highest doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.754×** | -4.4 | 5e-04 | 19/44 (PANC-1, NCI-H1573, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.693×** | -4.0 | 0.002 | 19/45 (HOP62, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.608×** | -4.0 | 0.002 | 22/45 (SNU-1, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.777×** | -3.9 | 0.003 | 23/45 (SW48, HEC-1-A, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.832×** | -3.8 | 0.004 | 17/45 (RKO, HCT15, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.784×** | -3.8 | 0.004 | 16/44 (RKO, NCI-H2030, …) | two highest doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.851× | -3.5 | 0.012 | 15/45 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.660×** | -3.4 | 0.018 | 15/43 (KATO III, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.804×** | -3.2 | 0.025 | 15/45 (NCI-H661, HS-578T, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.670×** | -3.2 | 0.025 | 18/45 (A-427, AN3 CA, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.814×** | -3.2 | 0.030 | 15/45 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.823×** | -3.0 | 0.048 | 9/45 (SHP-77, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.825×** | -3.0 | 0.050 | 15/45 (A-427, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +1.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1299. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 59.5 | 0 | 8 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.224× (z -15.2) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM 0.324× (z -9.0) |
| [[LoVo (line)]] | wt | 31.9 | 3 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.275× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 52.0 | 1 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.173× (z -12.2) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.377× (z -9.3) |
| [[A-427 (line)]] | wt | 191 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.176× (z -20.0) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.330× (z -14.0) |
| [[H4 (line)]] | wt | 56.1 | 0 | 5 (4 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0928× (z -12.2) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.223× (z -10.9) |
| [[HOP62 (line)]] | alt | 118 | 2 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +12.6) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.373× (z -12.2) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.387× (z -9.3) |
| [[LS 180 (line)]] | wt | 31.7 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.197× (z -12.3) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.340× (z -8.6) |
| [[PANC-1 (line)]] | alt | 51.4 | 3 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +13.6) ⚠ cell-cycle shift, would explain all of this change | [[Bortezomib (drug)]] 0.05 µM 0.265× (z -10.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A498 (line)]] | wt | 32.8 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.214× (z -16.9) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.384× (z -11.2) |
| [[HT-29 (line)]] | alt | 60.9 | 2 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +9.9) ⚠ cell-cycle shift, explains ~63% of this change | [[Selinexor (drug)]] 0.5 µM 0.301× (z -8.7) ⚠ cell-cycle shift, explains ~72% of this change |
| [[KATO III (line)]] | alt | 36.9 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.62× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[RKO (line)]] | wt | 48.8 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.62× (z +18.3) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 63.6 | 0 | 4 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0664× (z -16.3) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.212× (z -9.3) |
| [[A549 (line)]] | wt | 25.0 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.326× (z -9.3) ⚠ cell-cycle shift, explains ~87% of this change |
| [[HEC-1-A (line)]] | alt | 74.0 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.262× (z -12.9) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.390× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 103 | 1 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +8.9) ⚠ cell-cycle shift, explains ~63% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -9.4) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.383× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 30.8 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.312× (z -11.1) ⚠ cell-cycle shift, explains ~87% of this change |
| [[HS-578T (line)]] | alt | 37.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +11.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 54.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +16.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 40.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +13.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 45.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +13.0) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.336× (z -9.9) ⚠ cell-cycle shift, explains ~87% of this change |
| [[SNU-1 (line)]] | wt | 66.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 74.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 79.0 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.11× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[C32 (line)]] | wt | 39.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HCT15 (line)]] | alt | 66.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.237× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 28.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.107× (z -12.6) ⚠ cell-cycle shift, explains ~87% of this change |
| [[J82 (line)]] | alt | 66.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 66.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 64.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 52.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.220× (z -9.1) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SW480 (line)]] | alt | 66.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.402× (z -9.3) ⚠ cell-cycle shift, explains ~72% of this change |
| [[AsPC-1 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1299), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KNL1]] | +0.94 | +0.94 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 995 |
| [[SGO1]] | +0.94 | +0.91 / +0.93 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 932 |
| [[CDCA8]] | +0.93 | +0.94 / +0.93 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 907 |
| [[MKI67]] | +0.93 | +0.92 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 796 |
| [[KIF18A]] | +0.93 | +0.91 / +0.92 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 853 |
| [[DLGAP5]] | +0.93 | +0.93 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 957 |
| [[KIF4A]] | +0.92 | +0.94 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 821 |
| [[KIF2C]] | +0.92 | +0.90 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 934 |
| [[TPX2]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 788 |
| [[KIF23]] | +0.92 | +0.90 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 866 |
| [[CDK1]] | +0.92 | +0.91 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 957 |
| [[TOP2A]] | +0.92 | +0.92 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 876 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises NDC80's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.49× lower at baseline in the lines without PIMREG | 0.044 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises NDC80's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HYLS1]] | B | HYLS1 activity raises NDC80's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 1.99× lower at baseline in the lines without HYLS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent; its own permutation p |
| [[CDC20]] | C | CDC20 activity raises NDC80's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.04× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[AURKB]] | C | AURKB activity raises NDC80's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.99× lower at baseline in the lines without AURKB | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises NDC80's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.04× lower at baseline in the lines without PBK | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[FAM72D]] | C | FAM72D activity raises NDC80's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 3.50× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; co-absent with the target; its own permutation p |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises NDC80's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.45× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |

### Downstream of this gene

*77 arrows, 77 of them with an alert ⚠; grade A 0, B 0, C 77. Shown: the 12 strongest; 65 more arrows (65 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FOXM1]] | C | NDC80 activity raises FOXM1's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 3.36× lower at baseline in the lines without NDC80 | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; co-absent with the target |
| [[CKAP2]] | C | NDC80 activity raises CKAP2's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 3.00× lower at baseline in the lines without NDC80 | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[SGO1]] | C | NDC80 activity raises SGO1's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.79× lower at baseline in the lines without NDC80 | 0.007 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[KIF18B]] | C | NDC80 activity raises KIF18B's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 3.60× lower at baseline in the lines without NDC80 | 0.008 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; co-absent with the target |
| [[SPAG5]] | C | NDC80 activity raises SPAG5's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.78× lower at baseline in the lines without NDC80 | 0.009 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[KIF18A]] | C | NDC80 activity raises KIF18A's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.55× lower at baseline in the lines without NDC80 | 0.014 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[KNSTRN]] | C | NDC80 activity raises KNSTRN's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.43× lower at baseline in the lines without NDC80 | 0.014 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[CEP192]] | C | NDC80 activity raises CEP192's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.34× lower at baseline in the lines without NDC80 | 0.014 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[ASPM]] | C | NDC80 activity raises ASPM's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.80× lower at baseline in the lines without NDC80 | 0.015 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[DEPDC1]] | C | NDC80 activity raises DEPDC1's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 3.06× lower at baseline in the lines without NDC80 | 0.016 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; co-absent with the target |
| [[TROAP]] | C | NDC80 activity raises TROAP's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.56× lower at baseline in the lines without NDC80 | 0.016 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[CIT]] | C | NDC80 activity raises CIT's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.63× lower at baseline in the lines without NDC80 | 0.016 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.956). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.7, -55.7); signed map (-49.5, -43.6). **Vector** length 164, 61.1% of its response variance represented; |z| ≥ 3 in 1,422 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.85 to 28); *E2F targets* (hallmark, mean cos +0.73 to 46); *G2/M Transition* (reactome, mean cos +0.73 to 28).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.1 | +13.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +6.8 | +9.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | +6.5 | +8.9 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +6.4 | +6.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +6.3 | +13.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +1.4 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.9 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.6 | +3.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.6 | +2.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | -9.4 | -11.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -9.2 | -11.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -8.8 | -12.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -8.1 | -9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.1 | -7.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.1 | -4.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.0 | -3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.9 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | NDC80 kinetochore complex component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.32 — chr18:2,571,557-2,616,635 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HEC, HEC1, hsNDC80, TID3; previously KNTC2 |
| Gene groups (HGNC) | NDC80 kinetochore complex |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 17 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [O14777](https://www.uniprot.org/uniprotkb/O14777) (Kinetochore protein NDC80 homolog):

> Acts as a component of the essential kinetochore-associated NDC80 complex, which is required for chromosome segregation and spindle checkpoint activity. Required for kinetochore integrity and the organization of stable microtubule binding sites in the outer plate of the kinetochore. The NDC80 complex synergistically enhances the affinity of the SKA1 complex for microtubules and may allow the NDC80 complex to track depolymerizing microtubules. Plays a role in chromosome congression and is …

**Summary**, from NCBI Gene [10403](https://www.ncbi.nlm.nih.gov/gene/10403):

> This gene encodes a component of the NDC80 kinetochore complex. The encoded protein consists of an N-terminal microtubule binding domain and a C-terminal coiled-coiled domain that interacts with other components of the complex. This protein functions to organize and stabilize microtubule-kinetochore interactions and is required for proper chromosome segregation. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:16909](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16909) · Entrez [10403](https://www.ncbi.nlm.nih.gov/gene/10403) · UniProt [O14777](https://www.uniprot.org/uniprotkb/O14777) · Ensembl [ENSG00000080986](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080986)

## Data

Gene col 1299: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1299); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1299, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1299]; `tensor/DDL_lfc|DDL_z.npy` [1299]; `embed/gene_vectors.npy` [1299]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1299 or target_col == 1299). Every well: [[NDC80 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDC80.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
