---
symbol: "NCAPH"
type: "gene"
col: 4256
ensembl_id: "ENSG00000121152"
name: "non-SMC condensin I complex subunit H"
location: "2q11.2"
module: 22
arm: "+"
pooled_cpm: 32.86
n_lines_expressing: 49
n_dd_up: 29
n_dd_down: 28
n_dd_up_clean: 8
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 10
direction_downstream: 1
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# NCAPH

*non-SMC condensin I complex subunit H* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (21 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.60× (z +10.4, q 2e-22, up in 25 of 47 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Thymol (drug)]] 5 µM: 1.22× (z +4.4, q 4e-04, up in 13 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.369× (z -21.9, q 0e+00, down in 42 of 47 measured lines) ⚠ cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.649× (z -9.5, q 5e-19, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAPG]] (+0.93, fdr 7e-06), [[KIF15]] (+0.92, fdr 7e-06), [[KIF23]] (+0.92, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Auranofin (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 24 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4256.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.60×** | +10.4 | 2e-22 | 25/47 (A549, J82, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.97×** | +10.1 | 2e-21 | 38/47 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.80×** | +9.1 | 1e-17 | 36/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~70% of this change | **1.68×** | +7.7 | 2e-12 | 34/46 (C32, H4, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.55×** | +6.8 | 1e-09 | 28/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.54×** | +6.7 | 1e-09 | 32/46 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.45×** | +5.8 | 5e-07 | 22/44 (SW480, HT-29, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.43×** | +5.6 | 2e-06 | 26/46 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.41×** | +5.4 | 4e-06 | 21/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +5.3 | 8e-06 | 25/47 (NCI-H23, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.39×** | +5.1 | 1e-05 | 23/46 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.35×** | +4.7 | 1e-04 | 21/47 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.36×** | +4.5 | 4e-04 | 16/40 (NCI-H23, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Thymol (drug)]] 5 µM |  | **1.22×** | +4.4 | 4e-04 | 13/47 (NCI-H23, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.32×** | +4.4 | 5e-04 | 23/47 (A549, NCI-H1792, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.79×** | +4.2 | 1e-03 | 17/46 (A549, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.26×** | +3.6 | 0.009 | 13/47 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.010 | 12/47 (NCI-H23, C32, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.57×** | +3.2 | 0.029 | 13/47 (NCI-H23, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.039 | 7/47 (NCI-H23, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.20×** | +2.9 | 0.071 | 15/47 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.20×** | +2.9 | 0.075 | 13/47 (NCI-H460, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4256.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.369×** | -21.9 | 0e+00 | 42/47 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.398×** | -14.3 | 7e-44 | 40/47 (A498, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.649×** | -9.5 | 5e-19 | 33/47 (A-427, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.674×** | -8.6 | 8e-16 | 36/46 (A498, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.521×** | -7.7 | 2e-12 | 35/47 (HEC-1-A, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.616×** | -7.5 | 6e-12 | 40/47 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.650×** | -6.7 | 2e-09 | 27/46 (NCI-H2030, HEC-1-A, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.758×** | -6.1 | 9e-08 | 31/47 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.605×** | -5.6 | 2e-06 | 28/47 (SW480, HT-29, …) | two highest doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **0.477×** | -5.3 | 7e-06 | 25/40 (A-427, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.713×** | -5.0 | 2e-05 | 20/46 (A498, AN3 CA, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.744×** | -4.6 | 2e-04 | 19/46 (HEC-1-A, NCI-H1573, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.748×** | -4.5 | 3e-04 | 21/46 (A-427, Hs 766T, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.822×** | -4.3 | 7e-04 | 20/47 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.762×** | -4.2 | 0.001 | 19/46 (H4, NCI-H460, …) | two highest doses |  |
| [[palbociclib (drug)]] 5 µM |  | **0.579×** | -3.9 | 0.003 | 20/46 (SW480, H4, …) | two highest doses | noisy plate (z scaled) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **0.786×** | -3.7 | 0.005 | 12/46 (NCI-H2347, SNU-423, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.791×** | -3.6 | 0.008 | 16/46 (HepG2/C3A, NCI-H661, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.827×** | -3.3 | 0.025 | 16/47 (A-427, AN3 CA, …) | all doses, flat | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.753×** | -3.1 | 0.042 | 15/47 (SW480, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **0.832×** | -2.8 | 0.096 | 7/47 (hTERT-HPNE, SNU-423, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.879× | -2.8 | 0.099 | 9/47 (MIA PaCa-2, A549, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.776×** | -2.8 | 0.099 | 9/47 (HEC-1-A, HOP62, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.82 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4256. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 40.6 | 1 (1 ⚠) | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.0487× (z -39.2) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -16.1) |
| [[A-427 (line)]] | wt | 56.0 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0676× (z -21.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.234× (z -16.7) |
| [[LOX-IMVI (line)]] | wt | 26.4 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.183× (z -13.9) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.321× (z -9.3) |
| [[H4 (line)]] | wt | 33.4 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0607× (z -18.4) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -13.5) |
| [[NCI-H2030 (line)]] | alt | 51.4 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.311× (z -13.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.413× (z -9.8) |
| [[A-172 (line)]] | wt | 33.6 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0902× (z -15.9) ⚠ cell-cycle shift, explains ~69% of this change |
| [[LS 180 (line)]] | wt | 21.1 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.157× (z -14.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.249× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 26.7 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.197× (z -16.7) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -8.7) |
| [[PANC-1 (line)]] | alt | 33.0 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +14.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 31.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0469× (z -13.0) |
| [[C32 (line)]] | wt | 26.9 | 0 | 3 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.156× (z -11.2) ⚠ cell-cycle shift, explains ~69% of this change |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0544× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ciclopirox (drug)]] 5 µM 0.174× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 32.5 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.189× (z -14.5) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SW48 (line)]] | wt | 38.0 | 0 | 3 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.164× (z -9.4) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.294× (z -9.0) |
| [[A549 (line)]] | wt | 28.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +16.6) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.345× (z -10.2) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HS-578T (line)]] | alt | 19.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.174× (z -14.9) ⚠ cell-cycle shift, explains ~46% of this change |
| [[J82 (line)]] | alt | 45.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +15.1) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.546× (z -8.8) ⚠ cell-cycle shift, explains ~46% of this change |
| [[LoVo (line)]] | wt | 20.7 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.261× (z -12.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[NCI-H23 (line)]] | alt | 111 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.412× (z -11.4) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -11.4) |
| [[RKO (line)]] | wt | 33.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +13.8) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.347× (z -9.6) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SW480 (line)]] | alt | 45.8 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.413× (z -12.0) ⚠ cell-cycle shift, explains ~46% of this change |
| [[AN3 CA (line)]] | alt | 60.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.290× (z -9.7) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HCT15 (line)]] | alt | 39.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.324× (z -8.7) ⚠ cell-cycle shift, explains ~46% of this change |
| [[HT-29 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.131× (z -18.5) ⚠ cell-cycle shift, explains ~46% of this change |
| [[hTERT-HPNE (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.138× (z -11.1) ⚠ cell-cycle shift, explains ~46% of this change |
| [[KATO III (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.178× (z -9.7) ⚠ cell-cycle shift, explains ~61% of this change |
| [[NCI-H1792 (line)]] | alt | 15.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.302× (z -11.2) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SK-MEL-2 (line)]] | alt | 35.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.280× (z -11.4) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SNU-423 (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.312× (z -12.8) ⚠ cell-cycle shift, explains ~46% of this change |
| [[AsPC-1 (line)]] | alt | 8.11 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4256), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAPG]] | +0.93 | +0.94 / +0.93 | both halves | 7e-06 | same gene group; pathway: Condensation of Prometaphase Chromosomes; STRING 999 |
| [[KIF15]] | +0.92 | +0.92 / +0.93 | both halves | 7e-06 | STRING 892 |
| [[KIF23]] | +0.92 | +0.91 / +0.91 | both halves | 7e-06 | STRING 716 |
| [[RACGAP1]] | +0.92 | +0.90 / +0.91 | both halves | 7e-06 | STRING 660 |
| [[AURKB]] | +0.92 | +0.92 / +0.87 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 909 |
| [[BUB1B]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 915 |
| [[KIF11]] | +0.91 | +0.90 / +0.93 | both halves | 7e-06 | STRING 908 |
| [[SKA3]] | +0.91 | +0.88 / +0.90 | both halves | 7e-06 | STRING 814 |
| [[KNL1]] | +0.90 | +0.87 / +0.91 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 538 |
| [[MKI67]] | +0.90 | +0.91 / +0.89 | both halves | 7e-06 | STRING 700 |
| [[KIF4A]] | +0.89 | +0.90 / +0.86 | both halves | 7e-06 | STRING 945 |
| [[CDK1]] | +0.89 | +0.89 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_SPERMATOGENESIS; STRING 907 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises NCAPH's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.22× lower at baseline in the lines without PIMREG | 0.027 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises NCAPH's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.30× lower at baseline in the lines without E2F8 | 0.033 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[RGS3]] | B | RGS3 activity lowers NCAPH's level | lines that do not express RGS3 (7) vs lines expressing it (43) | 1.92× higher at baseline in the lines without RGS3 | 0.073 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises NCAPH's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.95× lower at baseline in the lines without NEURL1B | 0.099 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[NDC80]] | C | NDC80 activity raises NCAPH's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.69× lower at baseline in the lines without NDC80 | 0.032 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[PBK]] | C | PBK activity raises NCAPH's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.61× lower at baseline in the lines without PBK | 0.044 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises NCAPH's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.56× lower at baseline in the lines without AURKB | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CDCA3]] | C | CDCA3 activity raises NCAPH's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.91× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |
| [[SKA3]] | C | SKA3 activity raises NCAPH's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 2.83× lower at baseline in the lines without SKA3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p |
| [[CDC20]] | C | CDC20 activity raises NCAPH's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.37× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Auranofin (drug)]] 5 µM | C | NCAPH's natural level lowers the cells' numbers under Auranofin 5 µM (makes them more sensitive) | NCAPH's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.70 | 0.268 over the table, 0.045 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.907). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.8, -54.0); signed map (-47.7, -43.1). **Vector** length 147, 50.6% of its response variance represented; |z| ≥ 3 in 1,293 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.74 to 60); *DREAM G2/M down* (control, mean cos +0.78 to 28); *E2F targets* (hallmark, mean cos +0.70 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.7 | +5.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +4.7 | +10.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.5 | +4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.4 | +10.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +4.3 | +4.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.2 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +1.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.7 | +2.9 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | +2.3 | +2.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -11.3 | -21.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -10.8 | -14.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | -8.3 | -7.7 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | -6.5 | -7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -6.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.9 | -6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -9.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -1.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | non-SMC condensin I complex subunit H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:96,335,766-96,377,091 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAP-H, hCAP-H, NCAPH1; previously BRRN1 |
| Gene groups (HGNC) | Kleisins; Condensin I subunits |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 5 pathways, smallest: Condensation of Prometaphase Chromosomes; Mitotic Prometaphase; M Phase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15003](https://www.uniprot.org/uniprotkb/Q15003) (Condensin complex subunit 2):

> Regulatory subunit of the condensin complex, a complex required for conversion of interphase chromatin into mitotic-like condense chromosomes. The condensin complex probably introduces positive supercoils into relaxed DNA in the presence of type I topoisomerases and converts nicked DNA into positive knotted forms in the presence of type II topoisomerases. Early in neurogenesis, may play an essential role to ensure accurate mitotic chromosome condensation in neuron stem cells, ultimately …

**Summary**, from NCBI Gene [23397](https://www.ncbi.nlm.nih.gov/gene/23397):

> This gene encodes a member of the barr gene family and a regulatory subunit of the condensin complex. This complex is required for the conversion of interphase chromatin into condensed chromosomes. The protein encoded by this gene is associated with mitotic chromosomes, except during the early phase of chromosome condensation. During interphase, the protein has a distinct punctate nucleolar localization. Alternatively spliced transcript variants encoding different proteins have been described. …

**Accessions** — [HGNC:1112](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1112) · Entrez [23397](https://www.ncbi.nlm.nih.gov/gene/23397) · UniProt [Q15003](https://www.uniprot.org/uniprotkb/Q15003) · Ensembl [ENSG00000121152](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121152)

## Data

Gene col 4256: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4256); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4256, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4256]; `tensor/DDL_lfc|DDL_z.npy` [4256]; `embed/gene_vectors.npy` [4256]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4256 or target_col == 4256). Every well: [[NCAPH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCAPH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
