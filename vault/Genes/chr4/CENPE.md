---
symbol: "CENPE"
type: "gene"
col: 6237
ensembl_id: "ENSG00000138778"
name: "centromere protein E"
location: "4q24"
module: 22
arm: "+"
pooled_cpm: 136.25
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 29
n_dd_up_clean: 14
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CENPE

*centromere protein E* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.39× (z +36.3, q 0e+00, up in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~56% of this change. The strongest without an alert is [[Docetaxel (drug)]] 5 µM: 1.23× (z +5.1, q 2e-05, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (18 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.573× (z -13.6, q 1e-39, down in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~90% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.605× (z -12.3, q 2e-32, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPF]] (+0.94, fdr 7e-06), [[DLGAP5]] (+0.93, fdr 7e-06), [[CKAP2]] (+0.92, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 20 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6237.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **4.39×** | +36.3 | 0e+00 | 45/48 (NCI-H2347, NCI-H2030, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **2.96×** | +18.1 | 0e+00 | 45/48 (PANC-1, NCI-H2347, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **2.22×** | +13.8 | 4e-41 | 41/48 (HEC-1-A, NCI-H2347, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.63×** | +8.5 | 2e-15 | 38/48 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.63×** | +8.5 | 2e-15 | 40/48 (HOP62, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **1.53×** | +7.4 | 1e-11 | 30/48 (KATO III, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.32×** | +6.8 | 8e-10 | 35/48 (NCI-H23, SW 900, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.44×** | +6.3 | 2e-08 | 34/48 (KATO III, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.41×** | +6.0 | 2e-07 | 27/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.91×** | +5.9 | 3e-07 | 33/47 (J82, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | **1.23×** | +5.1 | 2e-05 | 26/48 (HT-29, PANC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.33×** | +5.0 | 3e-05 | 29/47 (A549, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +5.0 | 3e-05 | 30/48 (NCI-H23, A-172, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.33×** | +4.9 | 3e-05 | 30/49 (NCI-H2030, HT-29, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +4.9 | 3e-05 | 25/48 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +4.5 | 2e-04 | 22/48 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.26×** | +4.0 | 0.002 | 18/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.006 | 21/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.006 | 21/48 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[AZD1390 (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.007 | 20/48 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.009 | 18/48 (KATO III, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.018 | 16/48 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.019 | 21/47 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.019 | 17/48 (SW 900, HOP62, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.019 | 21/47 (HOP62, H4, …) | all doses, flat |  |
| [[Thymol (drug)]] 5 µM |  | 1.14× | +3.2 | 0.021 | 9/48 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.030 | 13/48 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.031 | 11/49 (PANC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 19 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6237.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.573×** | -13.6 | 1e-39 | 42/48 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.605×** | -12.3 | 2e-32 | 40/49 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.575×** | -9.6 | 2e-19 | 41/48 (H4, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.578×** | -9.5 | 3e-19 | 32/48 (A498, SW48, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.607×** | -8.7 | 6e-16 | 42/48 (PANC-1, A549, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.606×** | -8.4 | 6e-15 | 39/48 (J82, H4, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.726×** | -7.8 | 4e-13 | 32/48 (LS 180, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.624×** | -7.5 | 4e-12 | 30/48 (PANC-1, J82, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.664×** | -7.1 | 8e-11 | 39/48 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.755×** | -6.9 | 3e-10 | 29/48 (A498, A-427, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.674×** | -6.8 | 4e-10 | 30/49 (H4, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.674×** | -6.8 | 4e-10 | 30/48 (C32, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.676×** | -6.8 | 5e-10 | 39/49 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~74% of this change | **0.678×** | -6.5 | 4e-09 | 29/47 (C32, A498, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.683×** | -6.3 | 8e-09 | 37/48 (SNU-1, A549, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.700×** | -5.7 | 4e-07 | 36/48 (HOP62, PANC-1, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.721×** | -5.2 | 5e-06 | 27/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.577×** | -5.0 | 2e-05 | 33/48 (PANC-1, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.817×** | -4.6 | 1e-04 | 18/48 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.794×** | -4.0 | 0.002 | 21/48 (NCI-H2030, SHP-77, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.854× | -3.9 | 0.003 | 17/48 (A-427, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.789×** | -3.8 | 0.003 | 18/47 (LS 180, HS-578T, …) | all doses, stronger at high dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.860× | -3.7 | 0.005 | 14/48 (SW 900, Hs 766T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.810×** | -3.6 | 0.005 | 24/48 (A-172, SW48, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.874× | -3.3 | 0.019 | 12/48 (HS-578T, NCI-H23, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.832×** | -3.2 | 0.027 | 20/48 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.844× | -2.9 | 0.057 | 10/48 (RKO, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +1.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6237. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 149 | 3 (3 ⚠) | 10 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +25.9) ⚠ cell-cycle shift, explains ~56% of this change | [[Selinexor (drug)]] 5 µM 0.382× (z -14.0) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -12.5) |
| [[A498 (line)]] | wt | 153 | 2 (2 ⚠) | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +15.8) ⚠ cell-cycle shift, explains ~56% of this change | [[Selinexor (drug)]] 5 µM 0.190× (z -25.7) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -15.8) |
| [[LOX-IMVI (line)]] | wt | 140 | 3 (3 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +22.8) ⚠ cell-cycle shift, explains ~56% of this change | [[Selinexor (drug)]] 5 µM 0.246× (z -17.5) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -11.1) |
| [[C32 (line)]] | wt | 128 | 4 (4 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.85× (z +22.0) ⚠ cell-cycle shift, explains ~56% of this change | [[Selinexor (drug)]] 5 µM 0.343× (z -11.5) ⚠ cell-cycle shift, explains ~90% of this change |
| [[A-172 (line)]] | wt | 127 | 3 (3 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +19.4) ⚠ cell-cycle shift, explains ~56% of this change | [[Selinexor (drug)]] 5 µM 0.357× (z -14.2) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.478× (z -10.2) |
| [[A-427 (line)]] | wt | 230 | 2 (2 ⚠) | 6 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 3.23× (z +11.4) ⚠ cell-cycle shift, explains ~61% of this change | [[Selinexor (drug)]] 5 µM 0.252× (z -19.8) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.406× (z -13.0) |
| [[H4 (line)]] | wt | 215 | 0 | 8 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.115× (z -19.6) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.267× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 187 | 6 (6 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +26.6) ⚠ cell-cycle shift, explains ~56% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.475× (z -9.4) ⚠ cell-cycle shift, explains ~97% of this change |
| [[LS 180 (line)]] | wt | 149 | 0 | 7 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.224× (z -14.5) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.260× (z -13.0) |
| [[NCI-H460 (line)]] | wt | 122 | 2 (2 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +20.5) ⚠ cell-cycle shift, explains ~56% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -12.2) |
| [[PANC-1 (line)]] | alt | 163 | 3 (3 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.71× (z +32.7) ⚠ cell-cycle shift, explains ~56% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -15.1) |
| [[KATO III (line)]] | alt | 85.0 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +17.2) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[HOP62 (line)]] | alt | 204 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +28.0) ⚠ cell-cycle shift, explains ~56% of this change | [[Selinexor (drug)]] 5 µM 0.447× (z -12.1) ⚠ cell-cycle shift, explains ~90% of this change |
| [[LoVo (line)]] | wt | 80.6 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +19.1) ⚠ cell-cycle shift, explains ~56% of this change | [[Selinexor (drug)]] 5 µM 0.443× (z -9.6) ⚠ cell-cycle shift, explains ~90% of this change |
| [[SW48 (line)]] | wt | 173 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.163× (z -13.8) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -10.1) |
| [[HT-29 (line)]] | alt | 140 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +13.2) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Docetaxel (drug)]] 5 µM 2.27× (z +8.7) | [[Selinexor (drug)]] 5 µM 0.404× (z -9.6) ⚠ cell-cycle shift, explains ~90% of this change |
| [[hTERT-HPNE (line)]] | wt | 123 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.5× (z +21.7) ⚠ cell-cycle shift, explains ~56% of this change | [[Selinexor (drug)]] 5 µM 0.337× (z -10.1) ⚠ cell-cycle shift, explains ~90% of this change |
| [[NCI-H2030 (line)]] | alt | 151 | 2 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +33.2) ⚠ cell-cycle shift, explains ~56% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -13.8) |
| [[NCI-H2347 (line)]] | alt | 186 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.80× (z +33.9) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[Panc 03.27 (line)]] | alt | 128 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.09× (z +30.5) ⚠ cell-cycle shift, explains ~56% of this change | [[Lonafarnib (drug)]] 5 µM 0.145× (z -9.9) ⚠ toxic |
| [[HS-578T (line)]] | alt | 130 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.05× (z +22.3) ⚠ cell-cycle shift, explains ~56% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.295× (z -9.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[J82 (line)]] | alt | 166 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +22.5) ⚠ cell-cycle shift, explains ~56% of this change | [[Bortezomib (drug)]] 0.05 µM 0.444× (z -8.5) ⚠ cell-cycle shift, explains ~92% of this change |
| [[NCI-H23 (line)]] | alt | 145 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +15.1) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[RKO (line)]] | wt | 125 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +28.8) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[SNU-1 (line)]] | wt | 172 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -11.8) |
| [[SW 900 (line)]] | alt | 122 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +18.7) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[SW1417 (line)]] | alt | 134 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +21.9) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[AN3 CA (line)]] | alt | 332 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0371× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~77% of this change |
| [[AsPC-1 (line)]] | alt | 51.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +20.6) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[C-33 A (line)]] | alt | 244 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +12.5) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[CFPAC-1 (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.86× (z +25.0) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[HCT15 (line)]] | alt | 150 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +10.1) ⚠ cell-cycle shift, explains ~56% of this change | [[Selinexor (drug)]] 0.5 µM 0.265× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 74.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +12.3) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[RPMI-7951 (line)]] | alt | 155 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +16.7) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 148 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +19.1) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[SW480 (line)]] | alt | 114 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +15.7) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[BT-474 (line)]] | alt | 86.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +10.6) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[COLO 205 (line)]] | alt | 43.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +9.0) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[Hs 766T (line)]] | wt | 107 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.6) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 139 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.89× (z +10.6) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[NCI-H1792 (line)]] | alt | 100 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.61× (z +19.2) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[NCI-H661 (line)]] | alt | 264 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +9.0) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[SNU-423 (line)]] | alt | 83.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +16.7) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[SW 1271 (line)]] | alt | 196 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.61× (z +12.0) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[CHP-212 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 138 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6237), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPF]] | +0.94 | +0.93 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 999 |
| [[DLGAP5]] | +0.93 | +0.89 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 957 |
| [[CKAP2]] | +0.92 | +0.89 / +0.92 | both halves | 7e-06 | STRING 831 |
| [[CDKN3]] | +0.92 | +0.90 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 808 |
| [[KIF4A]] | +0.91 | +0.90 / +0.89 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 957 |
| [[DEPDC1]] | +0.91 | +0.92 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 828 |
| [[NDC80]] | +0.90 | +0.90 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 979 |
| [[TOP2A]] | +0.90 | +0.88 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 926 |
| [[ASPM]] | +0.90 | +0.91 / +0.93 | both halves | 7e-06 | STRING 981 |
| [[CCNB1]] | +0.89 | +0.87 / +0.88 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 967 |
| [[TPX2]] | +0.89 | +0.85 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 894 |
| [[KIF18A]] | +0.88 | +0.87 / +0.88 | both halves | 7e-06 | same gene group; pathway: Affinity selection of immunoglobulins; STRING 985 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CENPE's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.2% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PBK]] | C | PBK activity raises CENPE's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.73× lower at baseline in the lines without PBK | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises CENPE's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.28× lower at baseline in the lines without NDC80 | 0.029 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises CENPE's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.18× lower at baseline in the lines without AURKB | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[FAM72D]] | C | FAM72D activity raises CENPE's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.17× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises CENPE's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 3.06× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[CDC20]] | C | CDC20 activity raises CENPE's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.43× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[ACBD7]] | C | ACBD7 activity raises CENPE's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.61× lower at baseline in the lines without ACBD7 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.904). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.1, -56.7); signed map (-50.6, -43.6). **Vector** length 177, 72.0% of its response variance represented; |z| ≥ 3 in 1,741 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M Transition* (reactome, mean cos +0.69 to 28); *Mitotic G2-G2/M phases* (reactome, mean cos +0.69 to 28); *Cyclin A/B1/B2 associated events during G2/M transition* (reactome, mean cos +0.72 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +11.5 | +36.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +8.2 | +18.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.8 | +5.9 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | +6.2 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +5.7 | +13.8 |
|  | [[Docetaxel (drug)]] 5 µM |  | +4.8 | +5.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +3.7 | +3.7 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +3.7 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +2.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | -10.3 | -13.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.7 | -12.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -8.9 | -9.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | -8.8 | -6.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~92% of this change | -8.8 | -7.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.0 | -4.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | -6.9 | -7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.4 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.3 | -3.2 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -4.8 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | centromere protein E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q24 — chr4:103,105,349-103,198,445 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIF10, PPP1R61 |
| Gene groups (HGNC) | Kinesins; Protein phosphatase 1 regulatory subunits |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE, E2F_TARGETS |
| Reactome | 30 pathways, smallest: Kinesins; Processing of antigen in germinal center B cells; COPI-dependent Golgi-to-ER retrograde traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02224](https://www.uniprot.org/uniprotkb/Q02224) (Centromere-associated protein E):

> Microtubule plus-end-directed kinetochore motor which plays an important role in chromosome congression, microtubule-kinetochore conjugation and spindle assembly checkpoint activation. Drives chromosome congression (alignment of chromosomes at the spindle equator resulting in the formation of the metaphase plate) by mediating the lateral sliding of polar chromosomes along spindle microtubules towards the spindle equator and by aiding the establishment and maintenance of connections between …

**Summary**, from NCBI Gene [1062](https://www.ncbi.nlm.nih.gov/gene/1062):

> Centrosome-associated protein E (CENPE) is a kinesin-like motor protein that accumulates in the G2 phase of the cell cycle. Unlike other centrosome-associated proteins, it is not present during interphase and first appears at the centromere region of chromosomes during prometaphase. This protein is required for stable spindle microtubule capture at kinetochores which is a necessary step in chromosome alignment during prometaphase. This protein also couples chromosome position to microtubule …

**Accessions** — [HGNC:1856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1856) · Entrez [1062](https://www.ncbi.nlm.nih.gov/gene/1062) · UniProt [Q02224](https://www.uniprot.org/uniprotkb/Q02224) · Ensembl [ENSG00000138778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138778)

## Data

Gene col 6237: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6237); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6237, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6237]; `tensor/DDL_lfc|DDL_z.npy` [6237]; `embed/gene_vectors.npy` [6237]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6237 or target_col == 6237). Every well: [[CENPE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
