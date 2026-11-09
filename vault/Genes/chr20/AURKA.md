---
symbol: "AURKA"
type: "gene"
col: 1511
ensembl_id: "ENSG00000087586"
name: "aurora kinase A"
location: "20q13.2"
module: 22
arm: "+"
pooled_cpm: 53.83
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 37
n_dd_up_clean: 9
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# AURKA

*aurora kinase A* — 20q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.15× (z +14.0, q 6e-42, up in 37 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.77× (z +10.7, q 3e-24, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (16 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.497× (z -9.6, q 7e-19, down in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~57% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.594× (z -7.1, q 2e-10, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNB1]] (+0.92, fdr 7e-06), [[CCNB2]] (+0.89, fdr 7e-06), [[PLK1]] (+0.88, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1511.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.15×** | +14.0 | 6e-42 | 37/48 (PANC-1, RKO, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~66% of this change | **2.18×** | +10.7 | 3e-24 | 40/47 (HT-29, HOP62, …) | all doses, flat | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +10.7 | 3e-24 | 36/48 (NCI-H1792, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.94×** | +8.8 | 3e-16 | 35/48 (PANC-1, C32, …) | top dose only | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **3.30×** | +8.6 | 1e-15 | 42/47 (PANC-1, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.46×** | +7.2 | 7e-11 | 37/48 (NCI-H23, RKO, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.61×** | +6.6 | 4e-09 | 27/47 (HOP62, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.54×** | +6.0 | 2e-07 | 32/48 (HT-29, HOP62, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.56×** | +5.6 | 1e-06 | 32/48 (HOP62, SW 900, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.32×** | +5.1 | 2e-05 | 25/48 (HT-29, PANC-1, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.44×** | +5.0 | 3e-05 | 27/47 (HOP62, LOX-IMVI, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.37×** | +4.4 | 6e-04 | 22/48 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.36×** | +4.2 | 0.001 | 20/47 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.36×** | +4.2 | 0.001 | 25/48 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.35×** | +4.1 | 0.001 | 24/48 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.001 | 22/48 (LoVo, HOP62, …) | rises with dose |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.005 | 16/48 (HT-29, J82, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.014 | 18/48 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.040 | 20/47 (HOP62, LoVo, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 16 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1511.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.497×** | -9.6 | 7e-19 | 39/48 (SW480, BT-474, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.532×** | -8.3 | 3e-14 | 45/48 (C32, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.594×** | -7.1 | 2e-10 | 34/48 (SHP-77, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.595×** | -7.1 | 2e-10 | 32/48 (SHP-77, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.614×** | -6.7 | 3e-09 | 32/48 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.570×** | -6.3 | 2e-08 | 31/48 (SW480, SW 1271, …) | all doses, flat | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.621×** | -6.3 | 3e-08 | 37/48 (A549, SW48, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.634×** | -6.2 | 4e-08 | 23/48 (LOX-IMVI, SW48, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.638×** | -6.1 | 5e-08 | 39/48 (PANC-1, SW48, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.727×** | -6.0 | 1e-07 | 29/48 (A498, SW48, …) | rises with dose |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.645×** | -6.0 | 1e-07 | 37/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.649×** | -5.9 | 2e-07 | 30/48 (SHP-77, HOP62, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~72% of this change | **0.643×** | -5.8 | 3e-07 | 29/47 (RKO, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | **0.445×** | -5.8 | 3e-07 | 28/43 (A-427, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.743×** | -5.6 | 6e-07 | 27/48 (Hs 766T, SHP-77, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.672×** | -5.4 | 2e-06 | 30/48 (SHP-77, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.520×** | -4.7 | 9e-05 | 25/48 (RKO, C32, …) | top dose only | noisy plate (z scaled) |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.692×** | -4.7 | 1e-04 | 26/48 (SNU-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.725×** | -4.4 | 3e-04 | 22/48 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.726×** | -4.4 | 3e-04 | 21/48 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.771×** | -4.1 | 8e-04 | 21/48 (SNU-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.739×** | -4.1 | 9e-04 | 22/48 (SHP-77, A498, …) | two highest doses | position effect removed |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.723×** | -4.1 | 1e-03 | 24/48 (PANC-1, SW48, …) | all doses, stronger at high dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.805×** | -4.0 | 0.001 | 23/48 (A498, SW 900, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.734×** | -3.9 | 0.002 | 19/47 (A-172, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.817×** | -3.7 | 0.004 | 14/48 (A-427, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +1.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1511. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 61.3 | 5 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +14.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Peretinoin (drug)]] 0.5 µM 3.15× (z +9.6) | [[Belinostat (drug)]] 5 µM 0.336× (z -9.1) |
| [[A498 (line)]] | wt | 60.8 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.272× (z -15.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.429× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 46.0 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.139× (z -16.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.218× (z -9.3) |
| [[A-172 (line)]] | wt | 28.9 | 2 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.207× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 121 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +13.8) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 137 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -11.1) |
| [[C32 (line)]] | wt | 32.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +11.9) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.0933× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 53.0 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.160× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 50.9 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +15.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 39.5 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +14.8) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.120× (z -14.6) ⚠ toxic; cell-cycle shift, explains ~72% of this change |
| [[HS-578T (line)]] | alt | 28.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +12.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HT-29 (line)]] | alt | 52.2 | 2 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 4.48× (z +9.1) ⚠ transcription drop; cell-cycle shift, explains ~66% of this change · without an alert: [[Docetaxel (drug)]] 5 µM 3.00× (z +8.9) | — |
| [[LoVo (line)]] | wt | 24.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 27.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +12.0) | — |
| [[SW48 (line)]] | wt | 50.3 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.183× (z -9.8) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.315× (z -9.2) |
| [[A-427 (line)]] | wt | 69.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.290× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 47.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +14.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[BT-474 (line)]] | alt | 130 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.278× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 37.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HEC-1-A (line)]] | alt | 34.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 25.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 61.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 27.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[J82 (line)]] | alt | 58.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 58.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 54.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 51.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 59.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 34.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +13.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 63.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 58.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -9.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 51.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 38.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 92.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 56.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1511), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNB1]] | +0.92 | +0.91 / +0.94 | both halves | 7e-06 | pathway: APC/C-mediated degradation of cell cycle proteins; STRING 979 |
| [[CCNB2]] | +0.89 | +0.92 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 988 |
| [[PLK1]] | +0.88 | +0.91 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 997 |
| [[KNSTRN]] | +0.88 | +0.89 / +0.87 | both halves | 7e-06 | STRING 541 |
| [[DEPDC1]] | +0.87 | +0.94 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 782 |
| [[CDCA8]] | +0.86 | +0.83 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 952 |
| [[ASPM]] | +0.86 | +0.90 / +0.84 | both halves | 7e-06 | STRING 930 |
| [[FAM83D]] | +0.86 | +0.86 / +0.86 | both halves | 7e-06 | STRING 818 |
| [[CENPF]] | +0.85 | +0.90 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 902 |
| [[SGO2]] | +0.85 | +0.83 / +0.89 | both halves | 7e-06 | STRING 507 |
| [[KIF18A]] | +0.85 | +0.88 / +0.86 | both halves | 7e-06 | same gene group; STRING 683 |
| [[DLGAP5]] | +0.85 | +0.89 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 966 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises AURKA's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.78× lower at baseline in the lines without PIMREG | 0.078 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises AURKA's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.91× lower at baseline in the lines without AURKB | 0.077 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.858). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.1, -57.3); signed map (-51.3, -43.5). **Vector** length 164, 60.3% of its response variance represented; |z| ≥ 3 in 1,556 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitotic Prometaphase* (reactome, mean cos +0.64 to 48); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.67 to 41); *Mitotic Anaphase* (reactome, mean cos +0.67 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +11.5 | +14.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.8 | +10.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~66% of this change | +8.9 | +10.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +6.8 | +8.6 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +6.7 | +7.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | +4.8 | +5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +3.7 | +4.2 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +3.6 | +5.6 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +3.2 | +3.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.1 | +5.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -8.4 | -9.6 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -7.0 | -8.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~76% of this change | -6.8 | -6.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -6.2 | -6.1 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -5.8 | -6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -4.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.8 | -6.0 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -4.6 | -4.7 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -4.1 | -4.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -4.0 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | aurora kinase A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.2 — chr20:56,369,389-56,392,337 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BTAK, AurA, STK7, ARK1, PPP1R47, AIK; previously STK15, STK6 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Aurora kinase family |
| Hallmark sets | SPERMATOGENESIS, GLYCOLYSIS, MTORC1_SIGNALING, G2M_CHECKPOINT, MITOTIC_SPINDLE, E2F_TARGETS |
| Reactome | 18 pathways, smallest: TP53 Regulates Transcription of Genes Involved in G2 Cell Cycle Arrest; FBXL7 down-regulates AURKA during mitotic entry and in early mitosis; SUMOylation of DNA replication proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O14965](https://www.uniprot.org/uniprotkb/O14965) (Aurora kinase A):

> Mitotic serine/threonine kinase that contributes to the regulation of cell cycle progression. Associates with the centrosome and the spindle microtubules during mitosis and plays a critical role in various mitotic events including the establishment of mitotic spindle, centrosome duplication, centrosome separation as well as maturation, chromosomal alignment, spindle assembly checkpoint, and cytokinesis. Required for normal spindle positioning during mitosis and for the localization of NUMA1 and …

**Summary**, from NCBI Gene [6790](https://www.ncbi.nlm.nih.gov/gene/6790):

> The protein encoded by this gene is a cell cycle-regulated kinase that appears to be involved in microtubule formation and/or stabilization at the spindle pole during chromosome segregation. The encoded protein is found at the centrosome in interphase cells and at the spindle poles in mitosis. This gene may play a role in tumor development and progression. A processed pseudogene of this gene has been found on chromosome 1, and an unprocessed pseudogene has been found on chromosome 10. Multiple …

**Accessions** — [HGNC:11393](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11393) · Entrez [6790](https://www.ncbi.nlm.nih.gov/gene/6790) · UniProt [O14965](https://www.uniprot.org/uniprotkb/O14965) · Ensembl [ENSG00000087586](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087586)

## Data

Gene col 1511: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1511); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1511, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1511]; `tensor/DDL_lfc|DDL_z.npy` [1511]; `embed/gene_vectors.npy` [1511]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1511 or target_col == 1511). Every well: [[AURKA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AURKA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
