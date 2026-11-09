---
symbol: "DIAPH3"
type: "gene"
col: 6342
ensembl_id: "ENSG00000139734"
name: "diaphanous related formin 3"
location: "13q21.2"
module: 22
arm: "+"
pooled_cpm: 231.72
n_lines_expressing: 47
n_dd_up: 31
n_dd_down: 20
n_dd_up_clean: 15
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 11
direction_downstream: 39
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# DIAPH3

*diaphanous related formin 3* — 13q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (16 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.76× (z +12.1, q 5e-31, up in 40 of 45 measured lines) ⚠ cell-cycle shift, explains ~62% of this change. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 1.30× (z +5.4, q 3e-06, up in 28 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.552× (z -17.5, q 0e+00, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLQ]] (+0.86, fdr 7e-06), [[MELK]] (+0.85, fdr 7e-06), [[NCAPG]] (+0.84, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); 39 go from it, the strongest it → [[MYBL1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 22 with an alert ⚠; shown: the 15 strongest and the 14 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6342.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.76×** | +12.1 | 5e-31 | 40/45 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.51×** | +12.1 | 5e-31 | 28/45 (HS-578T, J82, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.72×** | +11.1 | 1e-26 | 35/46 (NCI-H460, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.58×** | +9.7 | 3e-20 | 38/45 (SNU-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.54×** | +9.2 | 3e-18 | 37/45 (SNU-1, RKO, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.49×** | +8.5 | 2e-15 | 35/45 (SNU-1, C32, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.41×** | +7.4 | 1e-11 | 31/44 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~72% of this change | **1.41×** | +7.1 | 9e-11 | 30/44 (SNU-1, C32, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.34×** | +6.3 | 3e-08 | 32/45 (NCI-H23, SNU-1, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.33×** | +6.1 | 7e-08 | 30/44 (NCI-H23, SNU-1, …) | all doses, stronger at high dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.22×** | +5.8 | 4e-07 | 25/45 (A549, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.31×** | +5.7 | 6e-07 | 29/45 (NCI-H23, SNU-1, …) | all doses, stronger at high dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.30×** | +5.6 | 8e-07 | 29/45 (MIA PaCa-2, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.30×** | +5.4 | 3e-06 | 28/44 (NCI-H23, HT-29, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.27×** | +5.2 | 9e-06 | 25/45 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.26×** | +4.9 | 3e-05 | 24/45 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +4.9 | 3e-05 | 22/45 (SW480, PANC-1, …) | two highest doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +4.4 | 3e-04 | 24/45 (NCI-H23, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.22×** | +4.2 | 9e-04 | 21/45 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.05 µM |  | **1.23×** | +4.1 | 0.001 | 21/45 (SK-MEL-2, HT-29, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.001 | 20/45 (NCI-H23, HT-29, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.001 | 22/45 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.21×** | +4.1 | 0.001 | 20/46 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.21×** | +4.0 | 0.001 | 16/45 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.29×** | +3.9 | 0.002 | 20/45 (SW480, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 0.5 µM |  | 1.19× | +3.7 | 0.004 | 17/46 (SNU-423, PANC-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.19× | +3.7 | 0.004 | 20/44 (NCI-H23, HT-29, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.004 | 15/45 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.13× | +3.6 | 0.005 | 9/45 (LoVo, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6342.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.552×** | -17.5 | 0e+00 | 38/46 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.578×** | -16.2 | 0e+00 | 39/45 (A498, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.548×** | -12.8 | 2e-35 | 39/45 (H4, A498, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.562×** | -12.3 | 1e-32 | 35/45 (A498, SW48, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.605×** | -10.3 | 7e-23 | 37/44 (SW48, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.550×** | -9.1 | 8e-18 | 33/45 (SW480, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.677×** | -8.3 | 6e-15 | 33/45 (NCI-H2030, Panc 03.27, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.674×** | -8.0 | 1e-13 | 29/45 (KATO III, LS 180, …) | all doses, flat |  |
| [[palbociclib (drug)]] 5 µM |  | **0.493×** | -7.9 | 2e-13 | 35/45 (SW480, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.738×** | -6.5 | 4e-09 | 26/45 (hTERT-HPNE, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.577×** | -6.1 | 4e-08 | 27/42 (SW48, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.757×** | -5.9 | 1e-07 | 32/46 (NCI-H460, COLO 205, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.597×** | -5.8 | 4e-07 | 26/44 (SW480, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.05 µM |  | **0.768×** | -5.3 | 4e-06 | 29/45 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.802×** | -4.7 | 9e-05 | 22/45 (SHP-77, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.861× | -4.4 | 3e-04 | 16/45 (NCI-H2030, CFPAC-1, …) | top dose only |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.674×** | -4.4 | 3e-04 | 21/45 (HOP62, HCT15, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | **0.698×** | -4.0 | 0.002 | 20/45 (A-427, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.831×** | -4.0 | 0.002 | 18/46 (A-427, HOP62, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.874× | -3.9 | 0.002 | 17/45 (SW48, H4, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.837× | -3.8 | 0.003 | 15/45 (RKO, A-427, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.882× | -3.7 | 0.006 | 17/45 (HCT15, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6342. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 150 | 0 | 11 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.175× (z -20.6) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -13.9) |
| [[A549 (line)]] | wt | 119 | 2 (2 ⚠) | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.2) ⚠ cell-cycle shift, explains ~84% of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.309× (z -12.7) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 294 | 1 (1 ⚠) | 9 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 6.59× (z +10.0) ⚠ cell-cycle shift, explains ~25% of this change | [[Selinexor (drug)]] 5 µM 0.275× (z -18.1) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.472× (z -10.4) |
| [[SW48 (line)]] | wt | 235 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.178× (z -16.0) |
| [[A-172 (line)]] | wt | 246 | 2 (2 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +13.3) ⚠ cell-cycle shift, explains ~84% of this change | [[Selinexor (drug)]] 5 µM 0.324× (z -14.5) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -11.8) |
| [[A498 (line)]] | wt | 364 | 0 | 8 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.149× (z -25.2) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -17.8) |
| [[C32 (line)]] | wt | 133 | 6 (6 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +11.8) ⚠ cell-cycle shift, explains ~84% of this change | [[Selinexor (drug)]] 5 µM 0.393× (z -11.1) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.322× (z -9.8) |
| [[H4 (line)]] | wt | 210 | 0 | 8 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.216× (z -15.2) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.234× (z -14.2) |
| [[LoVo (line)]] | wt | 170 | 1 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +9.2) ⚠ cell-cycle shift, explains ~62% of this change | [[Selinexor (drug)]] 5 µM 0.269× (z -20.7) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.309× (z -13.4) |
| [[NCI-H23 (line)]] | alt | 294 | 7 (5 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +12.1) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Peretinoin (drug)]] 5 µM 2.15× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -14.9) |
| [[SNU-1 (line)]] | wt | 392 | 5 (5 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.96× (z +13.0) ⚠ cell-cycle shift, explains ~62% of this change | [[Selinexor (drug)]] 5 µM 0.177× (z -22.8) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 532 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -19.6) |
| [[KATO III (line)]] | alt | 247 | 4 (4 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.45× (z +9.8) ⚠ cell-cycle shift, explains ~53% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -13.6) |
| [[NCI-H460 (line)]] | wt | 176 | 1 (1 ⚠) | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.55× (z +12.5) ⚠ cell-cycle shift, explains ~25% of this change | [[Selinexor (drug)]] 5 µM 0.324× (z -17.5) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -13.9) |
| [[RKO (line)]] | wt | 524 | 3 (3 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +14.7) ⚠ cell-cycle shift, explains ~84% of this change | [[Selinexor (drug)]] 5 µM 0.484× (z -10.7) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -9.9) |
| [[HCT15 (line)]] | alt | 387 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -14.3) |
| [[hTERT-HPNE (line)]] | wt | 139 | 2 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.49× (z +14.6) ⚠ cell-cycle shift, explains ~84% of this change | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.200× (z -11.3) |
| [[J82 (line)]] | alt | 843 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +16.9) ⚠ cell-cycle shift, explains ~84% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -15.0) |
| [[MIA PaCa-2 (line)]] | alt | 276 | 3 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +14.2) ⚠ cell-cycle shift, explains ~84% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 283 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +12.2) ⚠ cell-cycle shift, explains ~84% of this change | [[Selinexor (drug)]] 5 µM 0.451× (z -12.8) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.448× (z -9.2) |
| [[A-427 (line)]] | wt | 270 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.372× (z -14.4) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.398× (z -9.7) |
| [[COLO 205 (line)]] | alt | 191 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.220× (z -13.2) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H2347 (line)]] | alt | 99.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.1) ⚠ cell-cycle shift, explains ~84% of this change | [[Selinexor (drug)]] 5 µM 0.560× (z -9.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[PANC-1 (line)]] | alt | 148 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.3) ⚠ cell-cycle shift, explains ~84% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.631× (z -8.5) |
| [[SW480 (line)]] | alt | 389 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -10.7) |
| [[HOP62 (line)]] | alt | 254 | 1 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 4.61× (z +9.4) ⚠ cell-cycle shift, explains ~25% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -20.3) |
| [[Hs 766T (line)]] | wt | 218 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.489× (z -8.6) ⚠ cell-cycle shift, explains ~48% of this change |
| [[HS-578T (line)]] | alt | 134 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.79× (z +20.4) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[HT-29 (line)]] | alt | 224 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.346× (z -15.6) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H2030 (line)]] | alt | 161 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +8.6) ⚠ cell-cycle shift, explains ~84% of this change | [[Auranofin (drug)]] 5 µM 0.442× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 203 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +11.6) ⚠ cell-cycle shift, explains ~84% of this change | [[Selinexor (drug)]] 0.5 µM 0.330× (z -9.1) ⚠ cell-cycle shift, explains ~56% of this change |
| [[BT-474 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.2) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[CFPAC-1 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.377× (z -12.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[CHP-212 (line)]] | wt | 128 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.245× (z -9.2) |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.137× (z -10.8) |
| [[SHP-77 (line)]] | alt | 163 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.448× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 133 | 1 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.60× (z +9.3) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[SNU-423 (line)]] | alt | 192 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.3) ⚠ cell-cycle shift, explains ~84% of this change | — |
| [[SW1417 (line)]] | alt | 141 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +8.6) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[AN3 CA (line)]] | alt | 368 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 47.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 135 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.3 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 49.6 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 333 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 168 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6342), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLQ]] | +0.86 | +0.87 / +0.84 | both halves | 7e-06 |  |
| [[MELK]] | +0.85 | +0.82 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 605 |
| [[NCAPG]] | +0.84 | +0.84 / +0.82 | both halves | 7e-06 | same gene group; STRING 467 |
| [[KIF15]] | +0.84 | +0.83 / +0.82 | both halves | 7e-06 | STRING 470 |
| [[BRIP1]] | +0.84 | +0.86 / +0.80 | both halves | 7e-06 |  |
| [[SKA3]] | +0.83 | +0.84 / +0.80 | both halves | 7e-06 | STRING 528 |
| [[NCAPG2]] | +0.82 | +0.78 / +0.84 | both halves | 7e-06 | same gene group |
| [[ZGRF1]] | +0.82 | +0.85 / +0.80 | both halves | 7e-06 |  |
| [[SMC4]] | +0.82 | +0.79 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[ANLN]] | +0.81 | +0.80 / +0.78 | both halves | 7e-06 | pathway: RHOA GTPase cycle; STRING 988 |
| [[KNL1]] | +0.81 | +0.80 / +0.77 | both halves | 7e-06 | pathway: RHO GTPase Effectors; STRING 502 |
| [[CENPK]] | +0.80 | +0.79 / +0.82 | both halves | 7e-06 | pathway: RHO GTPase Effectors |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises DIAPH3's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.28× lower at baseline in the lines without E2F8 | 0.065 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[MYBL1]] | B | MYBL1 activity raises DIAPH3's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.75× lower at baseline in the lines without MYBL1 | 0.087 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[TLCD3B]] | B | TLCD3B activity raises DIAPH3's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.24× lower at baseline in the lines without TLCD3B | 0.095 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises DIAPH3's level | lines that do not express AURKB (4) vs lines expressing it (46) | 4.09× lower at baseline in the lines without AURKB | 0.005 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[MCM10]] | C | MCM10 activity raises DIAPH3's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 3.07× lower at baseline in the lines without MCM10 | 0.013 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises DIAPH3's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 3.16× lower at baseline in the lines without NDC80 | 0.019 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; co-absent with the target |
| [[CENPP]] | C | CENPP activity raises DIAPH3's level | lines that do not express CENPP (4) vs lines expressing it (46) | 2.81× lower at baseline in the lines without CENPP | 0.044 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[PBK]] | C | PBK activity raises DIAPH3's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.97× lower at baseline in the lines without PBK | 0.057 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[C21orf58]], [[SKA3]] | C | C21orf58, SKA3 activity raises DIAPH3's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 3.95× lower at baseline in the lines without C21orf58, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[PKMYT1]] | C | PKMYT1 activity raises DIAPH3's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 3.89× lower at baseline in the lines without PKMYT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; co-absent with the target; its own permutation p |
| [[MYBL2]] | C | MYBL2 activity raises DIAPH3's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 3.24× lower at baseline in the lines without MYBL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 0, C 39. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYBL1]] | C | DIAPH3 activity raises MYBL1's level | lines that do not express DIAPH3 (3) vs lines expressing it (47) | 4.59× lower at baseline in the lines without DIAPH3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[CENPP]] | C | DIAPH3, [[MELK]] activity raises CENPP's level | lines that do not express DIAPH3, MELK (3) vs lines expressing them (47) | 4.14× lower at baseline in the lines without DIAPH3, MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[PBK]] | C | DIAPH3, [[MELK]], [[TK1]] activity raises PBK's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 4.05× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[TOP2A]] | C | DIAPH3 activity raises TOP2A's level | lines that do not express DIAPH3 (3) vs lines expressing it (47) | 3.99× lower at baseline in the lines without DIAPH3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; its own permutation p |
| [[IQGAP3]] | C | DIAPH3, [[MELK]], [[TK1]] activity raises IQGAP3's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 3.79× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[KIF15]] | C | DIAPH3, [[MELK]] activity raises KIF15's level | lines that do not express DIAPH3, MELK (3) vs lines expressing them (47) | 3.41× lower at baseline in the lines without DIAPH3, MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[EME1]] | C | DIAPH3, [[MELK]], [[TK1]] activity raises EME1's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 3.22× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[BIRC5]] | C | DIAPH3 activity raises BIRC5's level | lines that do not express DIAPH3 (3) vs lines expressing it (47) | 3.20× lower at baseline in the lines without DIAPH3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[FANCI]] | C | DIAPH3, [[MELK]], [[TK1]] activity raises FANCI's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 3.15× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CIT]] | C | DIAPH3, [[MELK]] activity raises CIT's level | lines that do not express DIAPH3, MELK (3) vs lines expressing them (47) | 3.09× lower at baseline in the lines without DIAPH3, MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[TPX2]] | C | DIAPH3 activity raises TPX2's level | lines that do not express DIAPH3 (3) vs lines expressing it (47) | 2.81× lower at baseline in the lines without DIAPH3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[ZWINT]] | C | DIAPH3, [[MELK]], [[TK1]] activity raises ZWINT's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 2.80× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.7, -51.4); signed map (-45.2, -44.7). **Vector** length 170, 66.0% of its response variance represented; |z| ≥ 3 in 1,924 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.60 to 60); *DREAM G2/M down* (control, mean cos +0.62 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.59 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.1 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.0 | +1.4 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.0 | +3.8 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +6.0 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.7 | +2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.3 | +5.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +4.4 | +4.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +4.2 | +4.9 |
|  | [[vincristine (drug)]] 0.5 µM |  | +4.0 | +4.1 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +3.7 | +3.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -9.0 | -16.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -8.3 | -12.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | -7.3 | -8.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.0 | -10.3 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -6.8 | -9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -8.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -5.0 | -3.7 |
|  | [[palbociclib (drug)]] 5 µM |  | -4.3 | -7.9 |
|  | [[Terfenadine (drug)]] 5 µM |  | -3.6 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | diaphanous related formin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q21.2 — chr13:59,665,583-60,163,928 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DRF3, FLJ34705, AN, NSDAN; previously AUNA1 |
| Gene groups (HGNC) | Armadillo like helical domain containing; Formins |
| Hallmark sets | E2F_TARGETS |
| Reactome | 17 pathways, smallest: RHOF GTPase cycle; RHOD GTPase cycle; RHOJ GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NSV4](https://www.uniprot.org/uniprotkb/Q9NSV4) (Protein diaphanous homolog 3):

> Actin nucleation and elongation factor required for the assembly of F-actin structures, such as actin cables and stress fibers. Required for cytokinesis, stress fiber formation and transcriptional activation of the serum response factor. Binds to GTP-bound form of Rho and to profilin: acts in a Rho-dependent manner to recruit profilin to the membrane, where it promotes actin polymerization. DFR proteins couple Rho and Src tyrosine kinase during signaling and the regulation of actin dynamics. …

**Summary**, from NCBI Gene [81624](https://www.ncbi.nlm.nih.gov/gene/81624):

> This gene encodes a member of the diaphanous subfamily of the formin family. Members of this family are involved in actin remodeling and regulate cell movement and adhesion. Mutations in this gene are associated with autosomal dominant auditory neuropathy 1. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012]

**Accessions** — [HGNC:15480](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15480) · Entrez [81624](https://www.ncbi.nlm.nih.gov/gene/81624) · UniProt [Q9NSV4](https://www.uniprot.org/uniprotkb/Q9NSV4) · Ensembl [ENSG00000139734](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139734)

## Data

Gene col 6342: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6342); `tables/drug_effects.parquet` (93 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6342, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6342]; `tensor/DDL_lfc|DDL_z.npy` [6342]; `embed/gene_vectors.npy` [6342]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6342 or target_col == 6342). Every well: [[DIAPH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIAPH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
