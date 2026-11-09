---
symbol: "PRC1"
type: "gene"
col: 12728
ensembl_id: "ENSG00000198901"
name: "protein regulator of cytokinesis 1"
location: "15q26.1"
module: 22
arm: "+"
pooled_cpm: 84.94
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 25
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# PRC1

*protein regulator of cytokinesis 1* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (23 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.16× (z +16.6, q 0e+00, up in 47 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Docetaxel (drug)]] 5 µM: 1.24× (z +4.4, q 4e-04, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (13 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.512× (z -13.7, q 5e-40, down in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~75% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.551× (z -8.6, q 1e-15, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BIRC5]] (+0.94, fdr 7e-06), [[TPX2]] (+0.94, fdr 7e-06), [[KIF4A]] (+0.94, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MYEF2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 23 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12728.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **3.16×** | +16.6 | 0e+00 | 47/48 (PANC-1, A-172, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.90×** | +13.0 | 2e-36 | 38/48 (A549, NCI-H2030, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.50×** | +12.7 | 1e-34 | 42/44 (A-172, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.47×** | +12.0 | 3e-31 | 43/45 (A-172, SW1417, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **2.00×** | +10.0 | 2e-21 | 43/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.92×** | +9.4 | 6e-19 | 43/48 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **1.90×** | +8.9 | 6e-17 | 41/47 (C32, NCI-H23, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.77×** | +7.9 | 2e-13 | 42/48 (A549, LoVo, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~97% of this change | **1.69×** | +7.5 | 4e-12 | 40/48 (HT-29, HS-578T, …) | all doses, flat | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.65×** | +7.2 | 4e-11 | 39/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.56×** | +6.4 | 8e-09 | 38/48 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.50×** | +5.8 | 3e-07 | 29/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.33×** | +5.8 | 3e-07 | 37/48 (RKO, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.44×** | +5.2 | 7e-06 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.94×** | +5.0 | 2e-05 | 33/47 (J82, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | **1.24×** | +4.4 | 4e-04 | 28/48 (HT-29, HEC-1-A, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.002 | 25/47 (HOP62, NCI-H460, …) | all doses, flat | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.30×** | +3.8 | 0.004 | 28/47 (HOP62, H4, …) | all doses, flat | position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.011 | 21/48 (NCI-H460, SW 900, …) | all doses, flat | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.011 | 23/48 (LoVo, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.024 | 20/48 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.062 | 15/48 (H4, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12728.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.512×** | -13.7 | 5e-40 | 43/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.501×** | -10.0 | 5e-21 | 43/48 (A498, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.551×** | -8.6 | 1e-15 | 45/48 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.621×** | -6.9 | 7e-10 | 38/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.630×** | -6.7 | 3e-09 | 36/48 (SHP-77, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.657×** | -6.1 | 1e-07 | 28/48 (H4, SW48, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.657×** | -6.1 | 1e-07 | 40/48 (Hs 766T, SNU-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.764×** | -5.5 | 2e-06 | 32/48 (SW1417, NCI-H460, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.779×** | -5.1 | 2e-05 | 31/48 (A498, SW48, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.709×** | -5.0 | 4e-05 | 26/48 (A498, SNU-1, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.723×** | -4.7 | 1e-04 | 33/48 (HOP62, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **0.703×** | -4.6 | 2e-04 | 27/48 (SW48, KATO III, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.644×** | -4.5 | 2e-04 | 30/48 (SW480, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.807×** | -4.4 | 4e-04 | 27/48 (HCT15, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.760×** | -4.0 | 0.002 | 25/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 0.847× | -3.4 | 0.017 | 19/48 (CHP-212, NCI-H661, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.814×** | -3.0 | 0.065 | 14/48 (C-33 A, C32, …) | inconsistent across doses | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.815×** | -3.0 | 0.067 | 23/48 (A-427, HCT15, …) | top dose only |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.870× | -2.9 | 0.089 | 15/48 (NCI-H1573, SW 1088, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.824×** | -2.8 | 0.099 | 17/48 (Hs 766T, H4, …) | rises with dose |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **0.825×** | -2.8 | 0.099 | 15/48 (C32, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +1.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12728. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 94.6 | 5 (5 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +19.5) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.451× (z -11.2) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.467× (z -10.7) |
| [[A498 (line)]] | wt | 110 | 3 (3 ⚠) | 6 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Selinexor (drug)]] 5 µM 0.200× (z -23.2) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.435× (z -12.1) |
| [[LoVo (line)]] | wt | 80.7 | 7 (7 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +13.0) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.380× (z -12.5) ⚠ cell-cycle shift, explains ~75% of this change |
| [[A-172 (line)]] | wt | 89.1 | 3 (3 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Selinexor (drug)]] 5 µM 0.338× (z -11.9) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.379× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 75.3 | 2 (2 ⚠) | 6 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Selinexor (drug)]] 5 µM 0.223× (z -16.1) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.421× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 61.3 | 4 (4 ⚠) | 4 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.95× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | [[Selinexor (drug)]] 5 µM 0.334× (z -14.1) ⚠ cell-cycle shift, explains ~75% of this change |
| [[PANC-1 (line)]] | alt | 104 | 8 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +14.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LS 180 (line)]] | wt | 65.2 | 2 (2 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Selinexor (drug)]] 5 µM 0.176× (z -16.3) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.346× (z -9.9) |
| [[A-427 (line)]] | wt | 72.5 | 2 (2 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Selinexor (drug)]] 5 µM 0.162× (z -22.8) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.369× (z -12.5) |
| [[HOP62 (line)]] | alt | 115 | 3 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.443× (z -10.5) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.381× (z -8.8) |
| [[KATO III (line)]] | alt | 80.7 | 6 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.59× (z +13.7) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[SW1417 (line)]] | alt | 97.5 | 5 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.5) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.571× (z -8.9) ⚠ cell-cycle shift, explains ~75% of this change |
| [[SW48 (line)]] | wt | 112 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.166× (z -13.2) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.329× (z -11.6) |
| [[C32 (line)]] | wt | 64.7 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.269× (z -8.9) ⚠ cell-cycle shift, explains ~76% of this change |
| [[HS-578T (line)]] | alt | 51.8 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +11.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 76.5 | 4 (4 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Selinexor (drug)]] 5 µM 0.435× (z -10.2) ⚠ cell-cycle shift, explains ~75% of this change |
| [[H4 (line)]] | wt | 95.9 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0779× (z -15.6) ⚠ cell-cycle shift, explains ~60% of this change |
| [[HT-29 (line)]] | alt | 108 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Selinexor (drug)]] 5 µM 0.375× (z -10.8) ⚠ cell-cycle shift, explains ~75% of this change |
| [[J82 (line)]] | alt | 123 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Panobinostat (drug)]] 0.5 µM 0.458× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 122 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +12.0) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 0.5 µM 0.274× (z -9.3) ⚠ cell-cycle shift, explains ~84% of this change |
| [[SNU-1 (line)]] | wt | 103 | 0 | 3 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.133× (z -11.7) ⚠ cell-cycle shift, explains ~76% of this change |
| [[SNU-423 (line)]] | alt | 60.6 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +13.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CFPAC-1 (line)]] | alt | 70.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[COLO 205 (line)]] | alt | 52.8 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.255× (z -11.2) ⚠ cell-cycle shift, explains ~75% of this change |
| [[HCT15 (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.342× (z -10.7) ⚠ cell-cycle shift, explains ~75% of this change |
| [[HEC-1-A (line)]] | alt | 116 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[Hs 766T (line)]] | wt | 57.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 50.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Selinexor (drug)]] 5 µM 0.333× (z -9.6) ⚠ cell-cycle shift, explains ~75% of this change |
| [[MIA PaCa-2 (line)]] | alt | 81.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 128 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +14.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 57.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +14.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 84.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +12.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW480 (line)]] | alt | 85.9 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +10.8) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[HepG2_C3A (line)]] | wt | 25.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1573 (line)]] | alt | 50.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.362× (z -10.4) ⚠ cell-cycle shift, explains ~75% of this change |
| [[NCI-H1792 (line)]] | alt | 45.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 98.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 133 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.393× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 76.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.365× (z -11.7) ⚠ cell-cycle shift, explains ~75% of this change |
| [[AN3 CA (line)]] | alt | 156 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 66.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 109 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 59.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12728), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BIRC5]] | +0.94 | +0.94 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 940 |
| [[TPX2]] | +0.94 | +0.95 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 999 |
| [[KIF4A]] | +0.94 | +0.95 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 995 |
| [[KIF23]] | +0.92 | +0.94 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 992 |
| [[ARHGAP11A]] | +0.92 | +0.92 / +0.92 | both halves | 7e-06 | STRING 535 |
| [[KIF11]] | +0.92 | +0.94 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 972 |
| [[MKI67]] | +0.91 | +0.92 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 873 |
| [[NCAPG]] | +0.91 | +0.93 / +0.88 | both halves | 7e-06 | STRING 921 |
| [[BUB1B]] | +0.91 | +0.90 / +0.91 | both halves | 7e-06 | pathway: RHO GTPase Effectors; STRING 893 |
| [[ASPM]] | +0.90 | +0.88 / +0.88 | both halves | 7e-06 | STRING 921 |
| [[NDC80]] | +0.89 | +0.91 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 828 |
| [[RACGAP1]] | +0.89 | +0.89 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 973 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYEF2]] | B | MYEF2 activity raises PRC1's level | lines that do not express MYEF2 (16) vs lines expressing it (34) | 1.27× lower at baseline in the lines without MYEF2 | 0.067 | ⚠ within organs, on part of the lines; also absent: SDK2, MAP6, RBM20 |
| [[HYLS1]] | B | HYLS1 activity raises PRC1's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without HYLS1 | 0.099 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises PRC1's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.11× lower at baseline in the lines without NDC80 | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[PBK]] | C | PBK activity raises PRC1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without PBK | 0.042 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises PRC1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.24× lower at baseline in the lines without AURKB | 0.051 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[MYLK2]] | C | MYLK2 activity raises PRC1's level | lines that do not express MYLK2 (3) vs lines expressing it (47) | 2.53× lower at baseline in the lines without MYLK2 | 0.075 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, NDC80, SMARCD3; maybe low, not absent |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises PRC1's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.33× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[SKA3]] | C | SKA3 activity raises PRC1's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 2.45× lower at baseline in the lines without SKA3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; its own permutation p |
| [[CDC20]] | C | CDC20 activity raises PRC1's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.05× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.928). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.0, -55.1); signed map (-49.0, -43.9). **Vector** length 143, 61.1% of its response variance represented; |z| ≥ 3 in 1,672 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitotic Prometaphase* (reactome, mean cos +0.72 to 48); *E2F targets* (hallmark, mean cos +0.73 to 46); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.72 to 41).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +9.5 | +13.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +6.8 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +6.2 | +16.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +6.0 | +12.0 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +5.3 | +5.8 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.0 | +4.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.5 | +2.3 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.5 | -0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +0.8 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | +2.5 | +2.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | -9.6 | -13.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -8.7 | -10.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | -6.7 | -4.6 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~76% of this change | -5.2 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -0.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.4 | -5.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.4 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -0.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.9 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | protein regulator of cytokinesis 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:90,966,040-90,995,629 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ASE1, MAP65 |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE |
| Reactome | 4 pathways, smallest: RHO GTPases activate CIT; RHO GTPase Effectors; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [O43663](https://www.uniprot.org/uniprotkb/O43663) (Protein regulator of cytokinesis 1):

> Key regulator of cytokinesis that cross-links antiparrallel microtubules at an average distance of 35 nM. Essential for controlling the spatiotemporal formation of the midzone and successful cytokinesis. Required for KIF14 localization to the central spindle and midbody. Required to recruit PLK1 to the spindle. Stimulates PLK1 phosphorylation of RACGAP1 to allow recruitment of ECT2 to the central spindle. Acts as an oncogene for promoting bladder cancer cells proliferation, apoptosis inhibition …

**Summary**, from NCBI Gene [9055](https://www.ncbi.nlm.nih.gov/gene/9055):

> This gene encodes a protein that is involved in cytokinesis. The protein is present at high levels during the S and G2/M phases of mitosis but its levels drop dramatically when the cell exits mitosis and enters the G1 phase. It is located in the nucleus during interphase, becomes associated with mitotic spindles in a highly dynamic manner during mitosis, and localizes to the cell mid-body during cytokinesis. This protein has been shown to be a substrate of several cyclin-dependent kinases …

**Accessions** — [HGNC:9341](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9341) · Entrez [9055](https://www.ncbi.nlm.nih.gov/gene/9055) · UniProt [O43663](https://www.uniprot.org/uniprotkb/O43663) · Ensembl [ENSG00000198901](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198901)

## Data

Gene col 12728: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12728); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12728, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12728]; `tensor/DDL_lfc|DDL_z.npy` [12728]; `embed/gene_vectors.npy` [12728]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12728 or target_col == 12728). Every well: [[PRC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
