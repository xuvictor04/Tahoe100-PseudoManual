---
symbol: "SMC4"
type: "gene"
col: 3504
ensembl_id: "ENSG00000113810"
name: "structural maintenance of chromosomes 4"
location: "3q25.33"
module: 22
arm: "+"
pooled_cpm: 316.06
n_lines_expressing: 49
n_dd_up: 26
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# SMC4

*structural maintenance of chromosomes 4* — 3q25.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.34× (z +31.6, q 0e+00, up in 46 of 47 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.36× (z +5.8, q 4e-07, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.564× (z -15.0, q 0e+00, down in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~72% of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.798× (z -5.9, q 4e-07, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGO1]] (+0.94, fdr 7e-06), [[KNL1]] (+0.91, fdr 7e-06), [[NDC80]] (+0.90, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MYBL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 21 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3504.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **3.34×** | +31.6 | 0e+00 | 46/47 (PANC-1, J82, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **2.66×** | +17.5 | 0e+00 | 47/47 (PANC-1, J82, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.24×** | +15.0 | 0e+00 | 43/47 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.94×** | +12.3 | 2e-32 | 45/47 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | **1.78×** | +10.7 | 8e-25 | 44/48 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **1.72×** | +9.7 | 3e-20 | 33/43 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **1.68×** | +9.6 | 6e-20 | 42/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.29×** | +6.7 | 1e-09 | 37/47 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.41×** | +6.4 | 7e-09 | 31/47 (SW 900, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.41×** | +6.4 | 1e-08 | 38/47 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.39×** | +6.1 | 5e-08 | 33/47 (HEC-1-A, LOX-IMVI, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +6.0 | 1e-07 | 35/47 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +5.8 | 4e-07 | 29/47 (LoVo, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.37×** | +5.4 | 3e-06 | 30/44 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | **1.26×** | +4.2 | 0.001 | 27/46 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.53×** | +4.1 | 0.001 | 31/47 (A549, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.002 | 23/46 (HOP62, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Thymol (drug)]] 5 µM |  | 1.16× | +3.9 | 0.002 | 12/47 (MIA PaCa-2, HCT15, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.23×** | +3.9 | 0.003 | 26/47 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.010 | 21/48 (NCI-H23, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.011 | 22/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.011 | 19/46 (HOP62, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.011 | 22/47 (hTERT-HPNE, HT-29, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 1.20× | +3.4 | 0.016 | 22/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.13× | +3.3 | 0.018 | 11/47 (HT-29, PANC-1, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 0.5 µM |  | 1.16× | +2.8 | 0.081 | 11/47 (NCI-H23, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3504.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.564×** | -15.0 | 0e+00 | 39/47 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.537×** | -11.5 | 4e-28 | 44/47 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.678×** | -6.7 | 4e-09 | 34/47 (A-427, SNU-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.702×** | -6.5 | 9e-09 | 43/48 (Hs 766T, A498, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.798×** | -5.9 | 4e-07 | 30/47 (HCT15, RKO, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.776×** | -4.7 | 3e-04 | 31/47 (A498, A-427, …) | two highest doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.705×** | -4.6 | 3e-04 | 29/47 (A-427, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.638×** | -4.4 | 1e-03 | 29/47 (KATO III, AN3 CA, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.802×** | -4.1 | 0.003 | 25/47 (Hs 766T, HCT15, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.860× | -3.9 | 0.005 | 17/47 (MIA PaCa-2, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.804×** | -3.9 | 0.005 | 27/46 (H4, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -3.8 | 0.007 | 19/48 (HEC-1-A, A498, …) | two highest doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.687×** | -3.6 | 0.012 | 25/46 (KATO III, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.782×** | -3.2 | 0.049 | 24/47 (RKO, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.886× | -3.2 | 0.058 | 9/47 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.882× | -3.1 | 0.058 | 16/47 (HOP62, A-427, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.728×** | -3.1 | 0.071 | 19/47 (A-427, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.80 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3504. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 236 | 3 (3 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +17.2) ⚠ cell-cycle shift, explains ~51% of this change | [[Selinexor (drug)]] 5 µM 0.265× (z -21.0) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.527× (z -10.1) |
| [[A549 (line)]] | wt | 268 | 6 (6 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +25.9) ⚠ cell-cycle shift, explains ~51% of this change | [[Selinexor (drug)]] 5 µM 0.462× (z -12.9) ⚠ cell-cycle shift, explains ~72% of this change |
| [[NCI-H460 (line)]] | wt | 178 | 6 (6 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +20.1) ⚠ cell-cycle shift, explains ~51% of this change | [[Selinexor (drug)]] 5 µM 0.442× (z -12.8) ⚠ cell-cycle shift, explains ~72% of this change |
| [[A-172 (line)]] | wt | 331 | 3 (3 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +11.6) ⚠ cell-cycle shift, explains ~51% of this change | [[Selinexor (drug)]] 5 µM 0.319× (z -16.1) ⚠ cell-cycle shift, explains ~72% of this change |
| [[A-427 (line)]] | wt | 749 | 1 (1 ⚠) | 6 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 2.28× (z +8.9) ⚠ cell-cycle shift, explains ~53% of this change | [[Selinexor (drug)]] 5 µM 0.233× (z -23.5) ⚠ cell-cycle shift, explains ~72% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.401× (z -14.7) |
| [[AsPC-1 (line)]] | alt | 117 | 6 (6 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +25.3) ⚠ cell-cycle shift, explains ~51% of this change | [[Selinexor (drug)]] 5 µM 0.497× (z -11.0) ⚠ cell-cycle shift, explains ~72% of this change |
| [[HEC-1-A (line)]] | alt | 567 | 5 (5 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +24.6) ⚠ cell-cycle shift, explains ~51% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 393 | 5 (5 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +20.1) ⚠ cell-cycle shift, explains ~51% of this change | [[Selinexor (drug)]] 5 µM 0.521× (z -12.2) ⚠ cell-cycle shift, explains ~72% of this change |
| [[LoVo (line)]] | wt | 241 | 5 (5 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +24.4) ⚠ cell-cycle shift, explains ~51% of this change | [[Selinexor (drug)]] 5 µM 0.432× (z -13.6) ⚠ cell-cycle shift, explains ~72% of this change |
| [[HOP62 (line)]] | alt | 415 | 5 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +24.5) ⚠ cell-cycle shift, explains ~51% of this change | [[Selinexor (drug)]] 5 µM 0.537× (z -10.9) ⚠ cell-cycle shift, explains ~72% of this change |
| [[Panc 03.27 (line)]] | alt | 460 | 5 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +26.8) ⚠ cell-cycle shift, explains ~51% of this change | [[Selinexor (drug)]] 5 µM 0.556× (z -10.8) ⚠ cell-cycle shift, explains ~72% of this change |
| [[SW48 (line)]] | wt | 272 | 3 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +17.8) ⚠ cell-cycle shift, explains ~51% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.387× (z -9.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.526× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 219 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +27.1) ⚠ cell-cycle shift, explains ~51% of this change | [[Selinexor (drug)]] 5 µM 0.508× (z -12.0) ⚠ cell-cycle shift, explains ~72% of this change |
| [[H4 (line)]] | wt | 470 | 1 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +9.3) ⚠ cell-cycle shift, explains ~72% of this change | [[Selinexor (drug)]] 5 µM 0.313× (z -13.4) ⚠ cell-cycle shift, explains ~72% of this change |
| [[HS-578T (line)]] | alt | 285 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +25.6) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 198 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +20.2) ⚠ cell-cycle shift, explains ~51% of this change | [[Selinexor (drug)]] 5 µM 0.364× (z -12.7) ⚠ cell-cycle shift, explains ~72% of this change |
| [[J82 (line)]] | alt | 632 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +33.0) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[LOX-IMVI (line)]] | wt | 295 | 3 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +27.0) ⚠ cell-cycle shift, explains ~51% of this change | [[Selinexor (drug)]] 5 µM 0.421× (z -13.6) ⚠ cell-cycle shift, explains ~72% of this change |
| [[LS 180 (line)]] | wt | 199 | 2 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +10.8) ⚠ cell-cycle shift, explains ~51% of this change | [[Selinexor (drug)]] 5 µM 0.319× (z -14.1) ⚠ cell-cycle shift, explains ~72% of this change |
| [[MIA PaCa-2 (line)]] | alt | 364 | 4 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | [[Selinexor (drug)]] 5 µM 0.493× (z -8.9) ⚠ cell-cycle shift, explains ~72% of this change |
| [[NCI-H1792 (line)]] | alt | 132 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.32× (z +23.8) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[HT-29 (line)]] | alt | 258 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +15.3) ⚠ cell-cycle shift, explains ~51% of this change | [[Selinexor (drug)]] 5 µM 0.535× (z -9.4) ⚠ cell-cycle shift, explains ~72% of this change |
| [[NCI-H1573 (line)]] | alt | 167 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +21.8) ⚠ cell-cycle shift, explains ~51% of this change | [[Selinexor (drug)]] 5 µM 0.508× (z -9.9) ⚠ cell-cycle shift, explains ~72% of this change |
| [[NCI-H2347 (line)]] | alt | 356 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +25.3) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[SW 900 (line)]] | alt | 192 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +18.8) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[SW1417 (line)]] | alt | 384 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +25.8) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[C-33 A (line)]] | alt | 243 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +14.6) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[C32 (line)]] | wt | 183 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +23.6) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[Hs 766T (line)]] | wt | 180 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~92% of this change | [[Selinexor (drug)]] 5 µM 0.441× (z -11.8) ⚠ cell-cycle shift, explains ~72% of this change |
| [[NCI-H23 (line)]] | alt | 459 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.9) ⚠ cell-cycle shift, explains ~51% of this change | [[Selinexor (drug)]] 5 µM 0.508× (z -11.4) ⚠ cell-cycle shift, explains ~72% of this change |
| [[PANC-1 (line)]] | alt | 347 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +34.3) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[RKO (line)]] | wt | 300 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +25.4) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 330 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +16.9) ⚠ cell-cycle shift, explains ~51% of this change | [[Selinexor (drug)]] 5 µM 0.431× (z -13.0) ⚠ cell-cycle shift, explains ~72% of this change |
| [[SNU-1 (line)]] | wt | 312 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.427× (z -9.1) ⚠ cell-cycle shift, explains ~72% of this change |
| [[SW480 (line)]] | alt | 462 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +14.9) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[COLO 205 (line)]] | alt | 183 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +20.2) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H2030 (line)]] | alt | 199 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +31.7) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[BT-474 (line)]] | alt | 320 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +16.1) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[CHP-212 (line)]] | wt | 218 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +10.1) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[RPMI-7951 (line)]] | alt | 375 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.9) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[SHP-77 (line)]] | alt | 307 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +13.6) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[SNU-423 (line)]] | alt | 247 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +19.8) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[SW 1088 (line)]] | alt | 189 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0654× (z -9.9) ⚠ transcription drop |
| [[SW 1271 (line)]] | alt | 498 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +13.5) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[AN3 CA (line)]] | alt | 336 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 335 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 74.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 353 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3504), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGO1]] | +0.94 | +0.93 / +0.92 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 617 |
| [[KNL1]] | +0.91 | +0.88 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 566 |
| [[NDC80]] | +0.90 | +0.87 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 867 |
| [[MKI67]] | +0.90 | +0.87 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 648 |
| [[NCAPG]] | +0.89 | +0.87 / +0.89 | both halves | 7e-06 | same gene group; pathway: Condensation of Prometaphase Chromosomes; STRING 999 |
| [[KIF4A]] | +0.88 | +0.85 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 725 |
| [[PRC1]] | +0.87 | +0.84 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 790 |
| [[TPX2]] | +0.87 | +0.79 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 616 |
| [[ASPM]] | +0.86 | +0.85 / +0.86 | both halves | 7e-06 | STRING 809 |
| [[KIF15]] | +0.86 | +0.83 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 860 |
| [[CKAP2L]] | +0.86 | +0.81 / +0.85 | both halves | 7e-06 |  |
| [[CENPE]] | +0.86 | +0.85 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 899 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYBL1]] | B | MYBL1 activity raises SMC4's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.56× lower at baseline in the lines without MYBL1 | 0.069 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises SMC4's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.33× lower at baseline in the lines without NDC80 | 0.021 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises SMC4's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.51× lower at baseline in the lines without AURKB | 0.061 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[SKA3]] | C | SKA3 activity raises SMC4's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 2.78× lower at baseline in the lines without SKA3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p |
| [[PBK]] | C | PBK activity raises SMC4's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.30× lower at baseline in the lines without PBK | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.873). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.6, -55.4); signed map (-49.2, -44.7). **Vector** length 159, 69.4% of its response variance represented; |z| ≥ 3 in 1,706 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.75 to 28); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.67 to 41); *Mitotic Anaphase* (reactome, mean cos +0.67 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +8.7 | +31.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +6.9 | +17.5 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | +6.0 | +6.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | +5.0 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.4 | +15.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +3.4 | +3.9 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +3.2 | +3.4 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | +2.9 | +1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.9 | +4.1 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.9 | +3.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -14.1 | -15.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -10.7 | -11.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~92% of this change | -9.4 | -6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | -8.5 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.5 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.2 | -3.1 |
|  | [[EX229 (drug)]] 5 µM |  | -5.0 | -4.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.9 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | +0.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | -4.2 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | structural maintenance of chromosomes 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.33 — chr3:160,399,274-160,434,954 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hCAP-C, CAP-C; previously SMC4L1 |
| Gene groups (HGNC) | Structural maintenance of chromosomes proteins; Condensin I subunits; Condensin II subunits; MicroRNA protein coding host genes |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE, E2F_TARGETS |
| Reactome | 7 pathways, smallest: Condensation of Prometaphase Chromosomes; Condensation of Prophase Chromosomes; Mitotic Prophase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NTJ3](https://www.uniprot.org/uniprotkb/Q9NTJ3) (Structural maintenance of chromosomes protein 4):

> Central component of the condensin complex, a complex required for conversion of interphase chromatin into mitotic-like condense chromosomes. The condensin complex probably introduces positive supercoils into relaxed DNA in the presence of type I topoisomerases and converts nicked DNA into positive knotted forms in the presence of type II topoisomerases.

**Summary**, from NCBI Gene [10051](https://www.ncbi.nlm.nih.gov/gene/10051):

> This gene belongs to the 'structural maintenance of chromosomes' (SMC) gene family. Members of this gene family play a role in two changes in chromosome structure during mitotic segregation of chromosomes- chromosome condensation and sister chromatid cohesion. The protein encoded by this gene is likely a subunit of the 13S condensin complex, which is involved in chromosome condensation. A pseudogene related to this gene is located on chromosome 2. [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:14013](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14013) · Entrez [10051](https://www.ncbi.nlm.nih.gov/gene/10051) · UniProt [Q9NTJ3](https://www.uniprot.org/uniprotkb/Q9NTJ3) · Ensembl [ENSG00000113810](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113810)

## Data

Gene col 3504: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3504); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3504, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3504]; `tensor/DDL_lfc|DDL_z.npy` [3504]; `embed/gene_vectors.npy` [3504]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3504 or target_col == 3504). Every well: [[SMC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
