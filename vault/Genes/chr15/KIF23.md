---
symbol: "KIF23"
type: "gene"
col: 6069
ensembl_id: "ENSG00000137807"
name: "kinesin family member 23"
location: "15q23"
module: 22
arm: "+"
pooled_cpm: 66.2
n_lines_expressing: 49
n_dd_up: 30
n_dd_down: 37
n_dd_up_clean: 10
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# KIF23

*kinesin family member 23* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.02× (z +15.7, q 0e+00, up in 37 of 47 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.03× (z +5.8, q 3e-07, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (17 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.592× (z -11.7, q 1e-28, down in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~93% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.534× (z -9.9, q 9e-21, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF4A]] (+0.94, fdr 7e-06), [[MKI67]] (+0.94, fdr 7e-06), [[BUB1B]] (+0.94, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 22 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6069.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.02×** | +15.7 | 0e+00 | 37/47 (Panc 03.27, NCI-H2347, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.90×** | +10.1 | 2e-21 | 40/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **1.90×** | +9.7 | 4e-20 | 36/46 (J82, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **1.73×** | +8.6 | 8e-16 | 37/46 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.76×** | +8.5 | 1e-15 | 35/47 (Panc 03.27, RKO, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.67×** | +8.1 | 7e-14 | 39/47 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.60×** | +7.4 | 1e-11 | 31/47 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.38×** | +7.1 | 7e-11 | 36/47 (J82, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.50×** | +6.4 | 9e-09 | 33/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.32×** | +6.2 | 2e-08 | 30/47 (NCI-H23, HS-578T, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.47×** | +6.0 | 8e-08 | 30/46 (PANC-1, SW 900, …) | all doses, flat | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **2.03×** | +5.8 | 3e-07 | 27/47 (HEC-1-A, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.49×** | +5.8 | 3e-07 | 28/44 (RKO, NCI-H23, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.36×** | +4.8 | 6e-05 | 24/46 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.35×** | +4.8 | 7e-05 | 26/46 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.002 | 24/46 (HOP62, H4, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.002 | 24/46 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.004 | 23/47 (LoVo, J82, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.26×** | +3.7 | 0.006 | 18/47 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.25×** | +3.5 | 0.013 | 19/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.16× | +3.2 | 0.026 | 14/47 (HT-29, PANC-1, …) | all doses, flat |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.030 | 15/47 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.036 | 16/47 (SW 900, NCI-H23, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.038 | 16/47 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.044 | 11/47 (NCI-H23, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6069.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.592×** | -11.7 | 1e-28 | 39/47 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.511×** | -10.6 | 1e-23 | 39/47 (A498, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.534×** | -9.9 | 9e-21 | 36/47 (A-427, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.697×** | -8.0 | 2e-13 | 26/47 (H4, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.635×** | -7.1 | 1e-10 | 38/47 (A498, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **0.660×** | -6.0 | 2e-07 | 30/47 (LOX-IMVI, HOP62, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.712×** | -5.3 | 7e-06 | 25/47 (A-172, A549, …) | two highest doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.795×** | -5.1 | 3e-05 | 22/47 (A498, SW48, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~73% of this change | **0.543×** | -5.0 | 3e-05 | 24/43 (SW48, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.666×** | -4.6 | 3e-04 | 23/47 (SW480, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.747×** | -4.4 | 5e-04 | 25/47 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.766×** | -4.2 | 0.001 | 19/47 (A549, PANC-1, …) | all doses, flat |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.604×** | -4.2 | 0.001 | 20/47 (PANC-1, C32, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.771×** | -4.1 | 0.002 | 21/47 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.773×** | -4.1 | 0.002 | 17/47 (SNU-1, J82, …) | two highest doses | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.840× | -3.9 | 0.003 | 20/47 (HCT15, COLO 205, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.845× | -3.7 | 0.005 | 25/47 (SNU-1, A498, …) | two highest doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.665×** | -3.4 | 0.019 | 17/45 (COLO 205, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.794×** | -3.4 | 0.019 | 11/47 (PANC-1, SNU-423, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.666×** | -3.3 | 0.019 | 15/47 (HEC-1-A, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.798×** | -3.3 | 0.023 | 9/47 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Saquinavir (drug)]] 0.05 µM |  | **0.819×** | -3.1 | 0.036 | 12/47 (Hs 766T, SW 900, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.820×** | -3.1 | 0.036 | 15/46 (RKO, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.816×** | -3.1 | 0.040 | 14/46 (LOX-IMVI, LoVo, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.823×** | -3.1 | 0.040 | 14/47 (KATO III, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +1.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6069. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 56.9 | 1 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.231× (z -13.6) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.235× (z -9.5) |
| [[A498 (line)]] | wt | 72.3 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.197× (z -21.8) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.424× (z -11.5) |
| [[A549 (line)]] | wt | 91.9 | 1 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +13.8) ⚠ cell-cycle shift, would explain all of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.317× (z -10.1) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.493× (z -8.8) |
| [[LoVo (line)]] | wt | 53.2 | 4 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +12.5) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.403× (z -11.5) ⚠ cell-cycle shift, explains ~93% of this change |
| [[KATO III (line)]] | alt | 48.9 | 5 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.67× (z +14.8) ⚠ cell-cycle shift, explains ~83% of this change | — |
| [[SNU-1 (line)]] | wt | 103 | 0 | 4 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.229× (z -12.6) |
| [[SW48 (line)]] | wt | 84.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.415× (z -9.2) |
| [[A-427 (line)]] | wt | 95.5 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.220× (z -18.5) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.483× (z -8.9) |
| [[J82 (line)]] | alt | 97.4 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 72.9 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +15.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 51.5 | 0 | 2 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.207× (z -11.0) ⚠ cell-cycle shift, explains ~71% of this change |
| [[HS-578T (line)]] | alt | 40.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +14.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 32.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.127× (z -14.7) ⚠ cell-cycle shift, explains ~93% of this change |
| [[LS 180 (line)]] | wt | 32.5 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.226× (z -12.0) ⚠ cell-cycle shift, explains ~93% of this change |
| [[NCI-H23 (line)]] | alt | 90.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 53.9 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.357× (z -12.9) ⚠ cell-cycle shift, explains ~93% of this change |
| [[Panc 03.27 (line)]] | alt | 51.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +18.1) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.434× (z -8.8) ⚠ cell-cycle shift, explains ~93% of this change |
| [[C32 (line)]] | wt | 49.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +12.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CFPAC-1 (line)]] | alt | 41.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +13.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 72.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 121 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -9.3) |
| [[HOP62 (line)]] | alt | 79.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +12.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HT-29 (line)]] | alt | 77.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.379× (z -10.0) ⚠ cell-cycle shift, explains ~93% of this change |
| [[NCI-H1792 (line)]] | alt | 29.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +10.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 139 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +14.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2122 (line)]] | alt | 28.0 | 1 (1 ⚠) | 0 | [[Raltitrexed (drug)]] 5 µM 1.77× (z +9.3) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[NCI-H2347 (line)]] | alt | 72.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +16.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 55.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +15.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 79.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 79.2 | 1 (1 ⚠) | 0 | [[Lonafarnib (drug)]] 5 µM 7.40× (z +8.6) ⚠ toxic | — |
| [[SNU-423 (line)]] | alt | 39.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 43.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 84.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW480 (line)]] | alt | 68.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.354× (z -10.4) ⚠ cell-cycle shift, explains ~84% of this change |
| [[AN3 CA (line)]] | alt | 135 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 107 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.2 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 126 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6069), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF4A]] | +0.94 | +0.95 / +0.91 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 955 |
| [[MKI67]] | +0.94 | +0.94 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 880 |
| [[BUB1B]] | +0.94 | +0.92 / +0.94 | both halves | 7e-06 | STRING 926 |
| [[TPX2]] | +0.94 | +0.93 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 906 |
| [[ARHGAP11A]] | +0.93 | +0.94 / +0.92 | both halves | 7e-06 | STRING 625 |
| [[NCAPG]] | +0.92 | +0.93 / +0.91 | both halves | 7e-06 | STRING 949 |
| [[CCNA2]] | +0.92 | +0.91 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 914 |
| [[KIF11]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 994 |
| [[NCAPH]] | +0.92 | +0.91 / +0.91 | both halves | 7e-06 | STRING 716 |
| [[BIRC5]] | +0.92 | +0.93 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 885 |
| [[TOP2A]] | +0.92 | +0.92 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 927 |
| [[PRC1]] | +0.92 | +0.94 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 992 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises KIF23's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.40× lower at baseline in the lines without PIMREG | 0.009 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises KIF23's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.08× lower at baseline in the lines without NEURL1B | 0.051 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[HYLS1]] | B | HYLS1 activity raises KIF23's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 2.09× lower at baseline in the lines without HYLS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent; its own permutation p |
| [[PBK]] | C | PBK activity raises KIF23's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.91× lower at baseline in the lines without PBK | 0.014 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises KIF23's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.63× lower at baseline in the lines without AURKB | 0.031 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises KIF23's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.55× lower at baseline in the lines without NDC80 | 0.033 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises KIF23's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.24× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[MYLK2]] | C | MYLK2 activity raises KIF23's level | lines that do not express MYLK2 (3) vs lines expressing it (47) | 2.91× lower at baseline in the lines without MYLK2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, NDC80, SMARCD3; maybe low, not absent |
| [[SKA3]] | C | SKA3 activity raises KIF23's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 2.84× lower at baseline in the lines without SKA3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p |
| [[CDC20]] | C | CDC20 activity raises KIF23's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.81× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.958). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.4, -55.2); signed map (-48.9, -43.4). **Vector** length 158, 60.5% of its response variance represented; |z| ≥ 3 in 1,472 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitotic Prometaphase* (reactome, mean cos +0.73 to 48); *E2F targets* (hallmark, mean cos +0.74 to 46); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.75 to 41).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.5 | +15.7 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +6.2 | +6.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +5.4 | +6.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~97% of this change | +5.1 | +4.8 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | +4.3 | +4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +1.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.2 | +3.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.1 | +3.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +3.0 | +3.5 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +2.8 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.5 | -9.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -9.1 | -10.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | -8.9 | -6.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | -8.6 | -11.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.3 | -4.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.6 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.6 | -2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.5 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 23 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:69,414,246-69,448,427 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MKLP1, MKLP-1; previously KNSL5 |
| Gene groups (HGNC) | Kinesins |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 17 pathways, smallest: Mitotic Telophase/Cytokinesis; Kinesins; Processing of antigen in germinal center B cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02241](https://www.uniprot.org/uniprotkb/Q02241) (Kinesin-like protein KIF23):

> Component of the centralspindlin complex that serves as a microtubule-dependent and Rho-mediated signaling required for the myosin contractile ring formation during the cell cycle cytokinesis. Essential for cytokinesis in Rho-mediated signaling. Required for the localization of ECT2 to the central spindle. Plus-end-directed motor enzyme that moves antiparallel microtubules in vitro.

**Summary**, from NCBI Gene [9493](https://www.ncbi.nlm.nih.gov/gene/9493):

> The protein encoded by this gene is a member of kinesin-like protein family. This family includes microtubule-dependent molecular motors that transport organelles within cells and move chromosomes during cell division. This protein has been shown to cross-bridge antiparallel microtubules and drive microtubule movement in vitro. Alternate splicing of this gene results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:6392](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6392) · Entrez [9493](https://www.ncbi.nlm.nih.gov/gene/9493) · UniProt [Q02241](https://www.uniprot.org/uniprotkb/Q02241) · Ensembl [ENSG00000137807](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137807)

## Data

Gene col 6069: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6069); `tables/drug_effects.parquet` (81 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6069, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6069]; `tensor/DDL_lfc|DDL_z.npy` [6069]; `embed/gene_vectors.npy` [6069]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6069 or target_col == 6069). Every well: [[KIF23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
