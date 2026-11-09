---
symbol: "KIF4A"
type: "gene"
col: 1641
ensembl_id: "ENSG00000090889"
name: "kinesin family member 4A"
location: "Xq13.1"
module: 22
arm: "+"
pooled_cpm: 102.07
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 33
n_dd_up_clean: 9
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# KIF4A

*kinesin family member 4A* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (19 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.20× (z +13.7, q 4e-40, up in 46 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Docetaxel (drug)]] 5 µM: 1.21× (z +4.5, q 2e-04, up in 21 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (18 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.476× (z -17.8, q 0e+00, down in 44 of 47 measured lines) ⚠ cell-cycle shift, explains ~62% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.529× (z -15.3, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPX2]] (+0.96, fdr 7e-06), [[TOP2A]] (+0.95, fdr 7e-06), [[DLGAP5]] (+0.94, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 20 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1641.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.20×** | +13.7 | 4e-40 | 46/47 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.03×** | +11.8 | 7e-30 | 41/43 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.56×** | +10.6 | 4e-24 | 32/47 (PANC-1, NCI-H2030, …) | rises with dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.38×** | +7.7 | 2e-12 | 37/47 (NCI-H23, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.53×** | +6.8 | 9e-10 | 31/44 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **2.05×** | +6.5 | 6e-09 | 32/46 (J82, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.42×** | +5.9 | 3e-07 | 27/47 (PANC-1, NCI-H23, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +5.6 | 1e-06 | 31/47 (PANC-1, KATO III, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.38×** | +5.6 | 1e-06 | 27/46 (PANC-1, A549, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.37×** | +5.4 | 3e-06 | 28/47 (HT-29, HOP62, …) | all doses, flat | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.35×** | +5.2 | 1e-05 | 27/47 (KATO III, PANC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.32×** | +4.8 | 6e-05 | 29/47 (PANC-1, NCI-H23, …) | all doses, flat |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.31×** | +4.8 | 9e-05 | 22/47 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +4.6 | 2e-04 | 26/47 (KATO III, PANC-1, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.21×** | +4.5 | 2e-04 | 21/47 (HT-29, PANC-1, …) | all doses, flat |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.018 | 17/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.022 | 13/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.031 | 18/47 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.031 | 18/47 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.20×** | +3.2 | 0.031 | 15/47 (HT-29, C32, …) | two highest doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.033 | 16/47 (NCI-H460, LS 180, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.040 | 18/46 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Thymol (drug)]] 5 µM |  | 1.14× | +3.1 | 0.040 | 11/47 (A-427, Hs 766T, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.046 | 10/47 (A549, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 1.18× | +2.9 | 0.063 | 12/47 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.18× | +2.9 | 0.074 | 15/47 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Cysteamine (hydrochloride) (drug)]] 5 µM |  | 1.12× | +2.8 | 0.097 | 4/47 (Hs 766T, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 20 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1641.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.476×** | -17.8 | 0e+00 | 44/47 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.529×** | -15.3 | 0e+00 | 41/47 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.432×** | -14.7 | 0e+00 | 46/47 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.448×** | -14.0 | 2e-42 | 42/47 (HEC-1-A, A-427, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.326×** | -10.2 | 2e-22 | 38/44 (NCI-H23, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.569×** | -9.8 | 7e-21 | 38/47 (H4, A549, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.526×** | -8.5 | 2e-15 | 36/47 (HT-29, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **0.614×** | -8.2 | 2e-14 | 39/46 (C32, A498, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.720×** | -8.2 | 2e-14 | 29/47 (H4, A549, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.634×** | -8.0 | 9e-14 | 38/47 (Hs 766T, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.667×** | -7.1 | 7e-11 | 32/47 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.608×** | -6.2 | 3e-08 | 30/47 (SW480, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.714×** | -5.9 | 2e-07 | 29/47 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.798×** | -5.5 | 1e-06 | 27/47 (A549, A498, …) | top dose only |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **0.731×** | -5.3 | 5e-06 | 33/47 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.826×** | -4.6 | 1e-04 | 23/47 (HCT15, LoVo, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.758×** | -4.5 | 2e-04 | 24/47 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.775×** | -4.5 | 2e-04 | 21/47 (H4, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.770×** | -4.4 | 3e-04 | 19/47 (A549, A498, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.779×** | -4.4 | 3e-04 | 21/47 (SHP-77, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.792×** | -4.1 | 0.001 | 21/47 (SHP-77, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 5 µM |  | **0.643×** | -4.0 | 0.001 | 22/47 (A-427, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.654×** | -3.9 | 0.002 | 18/47 (PANC-1, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.852× | -3.8 | 0.002 | 18/47 (AsPC-1, SW 900, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.753×** | -3.5 | 0.007 | 18/47 (KATO III, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.818×** | -3.4 | 0.013 | 17/47 (A498, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +1.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1641. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 104 | 1 (1 ⚠) | 13 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +14.5) ⚠ cell-cycle shift, would explain all of this change | [[Amsacrine (drug)]] 5 µM 0.293× (z -17.5) |
| [[H4 (line)]] | wt | 138 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0469× (z -19.2) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.207× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 102 | 1 (1 ⚠) | 9 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.178× (z -18.0) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.287× (z -13.3) |
| [[A498 (line)]] | wt | 97.9 | 0 | 9 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0982× (z -32.9) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.383× (z -13.8) |
| [[C32 (line)]] | wt | 84.2 | 1 (1 ⚠) | 7 (6 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.192× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~39% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.441× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 93.9 | 0 | 8 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.249× (z -16.9) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.414× (z -10.9) |
| [[A-172 (line)]] | wt | 88.0 | 2 (2 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.72× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | [[Selinexor (drug)]] 5 µM 0.266× (z -15.2) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.389× (z -11.0) |
| [[A-427 (line)]] | wt | 172 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.192× (z -22.1) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.404× (z -12.5) |
| [[LS 180 (line)]] | wt | 60.3 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.138× (z -17.2) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.305× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 87.1 | 3 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +16.5) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.357× (z -13.8) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.373× (z -9.7) |
| [[PANC-1 (line)]] | alt | 134 | 5 (5 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +20.7) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -11.4) |
| [[HOP62 (line)]] | alt | 159 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.7) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -17.0) |
| [[KATO III (line)]] | alt | 109 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.331× (z -10.4) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -10.3) |
| [[LoVo (line)]] | wt | 50.8 | 2 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.76× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | [[Selinexor (drug)]] 5 µM 0.366× (z -12.2) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 163 | 2 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | [[Selinexor (drug)]] 5 µM 0.458× (z -10.4) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.421× (z -8.5) |
| [[SNU-1 (line)]] | wt | 76.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -11.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.199× (z -8.7) |
| [[SW1417 (line)]] | alt | 116 | 2 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -10.1) |
| [[SW48 (line)]] | wt | 91.0 | 0 | 5 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.223× (z -10.9) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.355× (z -10.5) |
| [[HT-29 (line)]] | alt | 97.5 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.218× (z -12.3) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 71.6 | 2 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +18.4) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -8.8) |
| [[RKO (line)]] | wt | 86.3 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +17.7) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 0.5 µM 0.257× (z -11.3) ⚠ cell-cycle shift, explains ~63% of this change |
| [[HEC-1-A (line)]] | alt | 119 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -13.4) |
| [[HS-578T (line)]] | alt | 55.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +12.9) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.349× (z -10.8) ⚠ cell-cycle shift, explains ~62% of this change |
| [[NCI-H2347 (line)]] | alt | 94.8 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +15.2) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.464× (z -11.2) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SK-MEL-2 (line)]] | alt | 155 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.448× (z -9.6) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.361× (z -8.9) |
| [[HCT15 (line)]] | alt | 99.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 119 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 123 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.371× (z -9.0) |
| [[SW480 (line)]] | alt | 172 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | [[Auranofin (drug)]] 5 µM 0.436× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 36.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C-33 A (line)]] | alt | 103 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.303× (z -9.5) |
| [[Hs 766T (line)]] | wt | 86.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.375× (z -9.8) ⚠ cell-cycle shift, explains ~62% of this change |
| [[hTERT-HPNE (line)]] | wt | 49.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.335× (z -9.0) ⚠ cell-cycle shift, explains ~62% of this change |
| [[J82 (line)]] | alt | 148 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.10× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[RPMI-7951 (line)]] | alt | 141 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-423 (line)]] | alt | 170 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 129 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 64.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1641), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPX2]] | +0.96 | +0.96 / +0.96 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 965 |
| [[TOP2A]] | +0.95 | +0.96 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 915 |
| [[DLGAP5]] | +0.94 | +0.94 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 962 |
| [[ARHGAP11A]] | +0.94 | +0.93 / +0.93 | both halves | 7e-06 | STRING 682 |
| [[KIF23]] | +0.94 | +0.95 / +0.91 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 955 |
| [[PRC1]] | +0.94 | +0.95 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 995 |
| [[BUB1B]] | +0.93 | +0.92 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 968 |
| [[BIRC5]] | +0.93 | +0.94 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 925 |
| [[KNL1]] | +0.93 | +0.92 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 588 |
| [[MKI67]] | +0.93 | +0.94 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 871 |
| [[NDC80]] | +0.92 | +0.94 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 821 |
| [[NCAPG]] | +0.92 | +0.94 / +0.90 | both halves | 7e-06 | STRING 934 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 6, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KIF4A's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PIMREG]] | B | PIMREG activity raises KIF4A's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.26× lower at baseline in the lines without PIMREG | 0.045 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[FAM72B]] | B | FAM72B activity raises KIF4A's level | lines that do not express FAM72B (6) vs lines expressing it (44) | 1.54× lower at baseline in the lines without FAM72B | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC02798, SRGAP2C, ZNF512B; its own permutation p |
| [[PIMREG]] | B | PIMREG activity strengthens KIF4A's drug response | lines that do not express PIMREG (5) vs lines expressing it (42) | the lines without PIMREG respond 0.62× as strongly (z diff +2.11); strongest at Idarubicin (hydrochloride) 5 µM: 0.92x vs 0.52x (z diff +5.9) | 0.069 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MYEF2]] | B | MYEF2 activity raises KIF4A's level | lines that do not express MYEF2 (16) vs lines expressing it (34) | 1.50× lower at baseline in the lines without MYEF2 | 0.084 | ⚠ within organs, on part of the lines; also absent: SDK2, MAP6, RBM20 |
| [[NEURL1B]] | B | NEURL1B activity raises KIF4A's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.96× lower at baseline in the lines without NEURL1B | 0.099 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[NDC80]] | C | NDC80 activity raises KIF4A's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.45× lower at baseline in the lines without NDC80 | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[SAPCD2]] | C | SAPCD2 activity raises KIF4A's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.30× lower at baseline in the lines without SAPCD2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |
| [[AURKB]] | C | AURKB activity raises KIF4A's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.77× lower at baseline in the lines without AURKB | 0.070 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[FAM72D]] | C | FAM72D activity raises KIF4A's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 1.95× lower at baseline in the lines without FAM72D | 0.094 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |
| [[SKA3]] | C | SKA3 activity raises KIF4A's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 3.08× lower at baseline in the lines without SKA3 | 0.098 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises KIF4A's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.92× lower at baseline in the lines without CDC20 | 0.0998 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.955). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.5, -55.4); signed map (-49.2, -43.4). **Vector** length 173, 70.7% of its response variance represented; |z| ≥ 3 in 1,687 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitotic Prometaphase* (reactome, mean cos +0.74 to 48); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.75 to 41); *Mitotic Anaphase* (reactome, mean cos +0.75 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.7 | +10.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~85% of this change | +5.8 | +5.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | +5.6 | +6.5 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +5.5 | +7.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.0 | +5.9 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.8 | +4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.9 | +3.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.8 | +3.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.7 | +3.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.7 | +2.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -12.1 | -17.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -11.8 | -14.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -10.1 | -14.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | -9.5 | -8.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | -8.3 | -8.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -6.2 | -5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -8.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.3 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 4A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:70,290,104-70,420,886 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIF4-G1, KIF4, HSA271784, FLJ12530, FLJ12655, FLJ14204, FLJ20631, MRX100 |
| Gene groups (HGNC) | Kinesins |
| Hallmark sets | G2M_CHECKPOINT, MITOTIC_SPINDLE, E2F_TARGETS |
| Reactome | 17 pathways, smallest: Recycling pathway of L1; Kinesins; Processing of antigen in germinal center B cells |
| Matched by | ensembl_id |

**Function**, from UniProt [O95239](https://www.uniprot.org/uniprotkb/O95239) (Chromosome-associated kinesin KIF4A):

> Iron-sulfur (Fe-S) cluster binding motor protein that has a role in chromosome segregation during mitosis. Translocates PRC1 to the plus ends of interdigitating spindle microtubules during the metaphase to anaphase transition, an essential step for the formation of an organized central spindle midzone and midbody and for successful cytokinesis. May play a role in mitotic chromosomal positioning and bipolar spindle stabilization (By similarity).

**Summary**, from NCBI Gene [24137](https://www.ncbi.nlm.nih.gov/gene/24137):

> This gene encodes a member of the kinesin 4 subfamily of kinesin related proteins. The encoded protein is an ATP dependent microtubule-based motor protein that is involved in the intracellular transport of membranous organelles. This protein also associates with condensed chromosome arms and may be involved in maintaining chromosome integrity during mitosis. This protein may also be involved in the organization of the central spindle prior to cytokinesis. A pseudogene of this gene is found on …

**Accessions** — [HGNC:13339](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13339) · Entrez [24137](https://www.ncbi.nlm.nih.gov/gene/24137) · UniProt [O95239](https://www.uniprot.org/uniprotkb/O95239) · Ensembl [ENSG00000090889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090889)

## Data

Gene col 1641: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1641); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1641, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1641]; `tensor/DDL_lfc|DDL_z.npy` [1641]; `embed/gene_vectors.npy` [1641]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1641 or target_col == 1641). Every well: [[KIF4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
