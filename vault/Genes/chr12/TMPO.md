---
symbol: "TMPO"
type: "gene"
col: 4223
ensembl_id: "ENSG00000120802"
name: "thymopoietin"
location: "12q23.1"
module: 22
arm: "+"
pooled_cpm: 85.77
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 24
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# TMPO

*thymopoietin* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.77× (z +21.9, q 0e+00, up in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.24× (z +3.6, q 0.012, up in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (SW 900 5.84×, PANC-1 3.43×, Panc 03.27 5.12×, NCI-H460 4.74×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H460 6.23×, PANC-1 3.58×, J82 3.21×, A498 3.89×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.591× (z -8.7, q 3e-15, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FOXM1]] (+0.86, fdr 7e-06), [[KIF11]] (+0.84, fdr 7e-06), [[ECT2]] (+0.82, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 21 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4223.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (SW 900 5.84×, PANC-1 3.43×, Panc 03.27 5.12×, NCI-H460 4.74×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H460 6.23×, PANC-1 3.58×, J82 3.21×, A498 3.89×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **3.77×** | +21.9 | 0e+00 | 47/49 (SW 900, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.48×** | +19.8 | 0e+00 | 44/44 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.52×** | +14.1 | 4e-43 | 42/45 (SW 900, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~65% of this change | **1.59×** | +7.6 | 3e-12 | 39/48 (HT-29, SW 900, …) | all doses, flat | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +6.9 | 7e-10 | 3/49 (SNU-1, HCT15, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~66% of this change | **1.53×** | +6.8 | 1e-09 | 38/47 (LoVo, A549, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.32×** | +6.5 | 8e-09 | 28/48 (J82, NCI-H1792, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.44×** | +5.8 | 5e-07 | 32/48 (PANC-1, HEC-1-A, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.38×** | +5.3 | 6e-06 | 30/48 (C32, HEC-1-A, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.24×** | +5.1 | 2e-05 | 30/48 (NCI-H23, HT-29, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.33×** | +4.8 | 1e-04 | 27/47 (KATO III, H4, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.26×** | +3.9 | 0.005 | 25/48 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.27×** | +3.8 | 0.006 | 25/50 (A-172, SNU-423, …) | top dose only | position effect removed |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.25×** | +3.7 | 0.010 | 16/48 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.012 | 22/48 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.5 | 0.015 | 19/48 (J82, SW480, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.026 | 20/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Riluzole hydrochloride (drug)]] 5 µM |  | 1.13× | +3.0 | 0.069 | 7/49 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.19× | +2.9 | 0.087 | 14/48 (NCI-H460, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4223.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.591×** | -8.7 | 3e-15 | 38/48 (SW1417, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.639×** | -7.4 | 5e-11 | 33/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.682×** | -5.9 | 5e-07 | 33/48 (A-427, SW48, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.704×** | -5.8 | 1e-06 | 32/48 (A498, A-427, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **0.729×** | -5.2 | 2e-05 | 24/48 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.800×** | -5.2 | 2e-05 | 24/48 (H4, A-427, …) | all doses, flat | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.803×** | -5.1 | 3e-05 | 24/48 (HCT15, Hs 766T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.742×** | -4.9 | 7e-05 | 29/48 (HOP62, PANC-1, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.815×** | -4.7 | 1e-04 | 27/48 (SW480, LS 180, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.752×** | -4.5 | 4e-04 | 29/47 (COLO 205, RKO, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.762×** | -4.5 | 4e-04 | 30/48 (MIA PaCa-2, SNU-1, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.763×** | -4.4 | 4e-04 | 26/48 (KATO III, SW 1271, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -4.1 | 0.002 | 23/48 (SW1417, H4, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.716×** | -3.9 | 0.004 | 20/48 (A-427, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.779×** | -3.9 | 0.004 | 18/48 (RKO, SW480, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **0.801×** | -3.4 | 0.019 | 16/49 (SW480, HOP62, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.679×** | -3.3 | 0.027 | 23/49 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.820×** | -3.3 | 0.033 | 17/47 (SK-MEL-2, RKO, …) | rises with dose | low cells (technical?) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.825×** | -3.2 | 0.046 | 12/48 (NCI-H2347, SW1417, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.827×** | -3.1 | 0.051 | 18/48 (SW1417, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belzutifan (drug)]] 5 µM |  | **0.700×** | -3.1 | 0.054 | 18/46 (HEC-1-A, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 0.878× | -3.0 | 0.062 | 8/49 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.879× | -3.0 | 0.064 | 19/49 (KATO III, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4223. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 155 | 2 (2 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Selinexor (drug)]] 5 µM 0.385× (z -15.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.471× (z -8.5) |
| [[A498 (line)]] | wt | 76.4 | 3 (3 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.89× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Selinexor (drug)]] 5 µM 0.420× (z -13.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.459× (z -8.6) |
| [[A-172 (line)]] | wt | 61.6 | 3 (3 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Selinexor (drug)]] 5 µM 0.404× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 127 | 4 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Panobinostat (drug)]] 0.5 µM 0.459× (z -10.0) |
| [[SW1417 (line)]] | alt | 112 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Panobinostat (drug)]] 0.5 µM 0.374× (z -11.3) |
| [[SW480 (line)]] | alt | 115 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.55× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Panobinostat (drug)]] 5 µM 0.408× (z -10.5) |
| [[A549 (line)]] | wt | 52.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[C-33 A (line)]] | alt | 104 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Panobinostat (drug)]] 0.5 µM 0.400× (z -9.2) |
| [[HT-29 (line)]] | alt | 88.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[KATO III (line)]] | alt | 89.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[PANC-1 (line)]] | alt | 91.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SNU-423 (line)]] | alt | 41.5 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.28× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[C32 (line)]] | wt | 52.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.13× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[CFPAC-1 (line)]] | alt | 54.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.37× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[H4 (line)]] | wt | 63.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Selinexor (drug)]] 5 µM 0.122× (z -17.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 116 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Panobinostat (drug)]] 5 µM 0.444× (z -8.9) |
| [[HOP62 (line)]] | alt | 72.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[Hs 766T (line)]] | wt | 48.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.70× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 28.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.29× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[LOX-IMVI (line)]] | wt | 74.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.01× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LS 180 (line)]] | wt | 79.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.37× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Selinexor (drug)]] 5 µM 0.391× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 84.5 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.05× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 34.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.07× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H23 (line)]] | alt | 171 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Panobinostat (drug)]] 5 µM 0.434× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 106 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Panobinostat (drug)]] 0.5 µM 0.416× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 52.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SHP-77 (line)]] | alt | 125 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.22× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Panobinostat (drug)]] 0.5 µM 0.400× (z -10.3) |
| [[SNU-1 (line)]] | wt | 85.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 6.36× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Selinexor (drug)]] 5 µM 0.320× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 71.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[AsPC-1 (line)]] | alt | 63.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.35× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HS-578T (line)]] | alt | 32.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[LoVo (line)]] | wt | 111 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H1573 (line)]] | alt | 40.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H460 (line)]] | wt | 86.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.23× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW48 (line)]] | wt | 116 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Bortezomib (drug)]] 0.05 µM 0.330× (z -8.7) ⚠ cell-cycle shift, explains ~71% of this change |
| [[AN3 CA (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -13.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 147 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H2030 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[RKO (line)]] | wt | 108 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[RPMI-7951 (line)]] | alt | 45.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.14× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 69.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[BT-474 (line)]] | alt | 96.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 121 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4223), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXM1]] | +0.86 | +0.81 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[KIF11]] | +0.84 | +0.84 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 575 |
| [[ECT2]] | +0.82 | +0.77 / +0.85 | both halves | 7e-06 | pathway: CDC42 GTPase cycle; STRING 541 |
| [[MAD2L1]] | +0.82 | +0.82 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 469 |
| [[NCAPG]] | +0.81 | +0.80 / +0.85 | both halves | 7e-06 |  |
| [[PRC1]] | +0.81 | +0.80 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 494 |
| [[KIF15]] | +0.80 | +0.82 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[CENPH]] | +0.79 | +0.76 / +0.81 | both halves | 7e-06 | pathway: Mitotic Anaphase |
| [[PLK4]] | +0.79 | +0.74 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 400 |
| [[HASPIN]] | +0.79 | +0.77 / +0.79 | both halves | 7e-06 |  |
| [[LMNB1]] | +0.78 | +0.75 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 981 |
| [[ARHGAP11A]] | +0.77 | +0.82 / +0.82 | both halves | 7e-06 | pathway: RHOA GTPase cycle |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises TMPO's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.89× lower at baseline in the lines without E2F8 | 0.056 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.746). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.4, -52.0); signed map (-45.3, -45.7). **Vector** length 141, 53.5% of its response variance represented; |z| ≥ 3 in 1,411 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.63 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.58 to 48); *Resolution of Sister Chromatid Cohesion* (reactome, mean cos +0.59 to 33).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.7 | +1.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.7 | +5.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +3.8 | +3.1 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +3.7 | +3.7 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | +3.6 | +5.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.3 | +2.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.2 | +3.6 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.9 | +1.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.8 | +0.9 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.8 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.1 | -4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | -7.1 | -5.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.4 | -5.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.5 | -5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.5 | -8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.1 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.1 | -3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.5 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | thymopoietin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:98,515,579-98,550,351 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TP, LAP2, LEMD4 |
| Gene groups (HGNC) | LEM domain containing |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 23 pathways, smallest: Depolymerization of the Nuclear Lamina; Initiation of Nuclear Envelope (NE) Reformation; RHOF GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [P42166](https://www.uniprot.org/uniprotkb/P42166) (Lamina-associated polypeptide 2, isoform alpha):

> May be involved in the structural organization of the nucleus and in the post-mitotic nuclear assembly. Plays an important role, together with LMNA, in the nuclear anchorage of RB1.; TP and TP5 may play a role in T-cell development and function. TP5 is an immunomodulating pentapeptide.

**Summary**, from NCBI Gene [7112](https://www.ncbi.nlm.nih.gov/gene/7112):

> Through alternative splicing, this gene encodes several distinct LEM domain containing protein isoforms. LEM domain proteins include inner nuclear membrane and intranuclear proteins, and are involved in a variety of cellular functions including gene expression, chromatin organization, and replication and cell cycle control. The encoded alpha isoform is broadly diffuse in the nucleus and contains a lamin binding domain, while the beta and gamma isoforms are localized to the nuclear membrane and …

**Accessions** — [HGNC:11875](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11875) · Entrez [7112](https://www.ncbi.nlm.nih.gov/gene/7112) · UniProt [P42166](https://www.uniprot.org/uniprotkb/P42166) · Ensembl [ENSG00000120802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120802)

## Data

Gene col 4223: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4223); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4223, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4223]; `tensor/DDL_lfc|DDL_z.npy` [4223]; `embed/gene_vectors.npy` [4223]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4223 or target_col == 4223). Every well: [[TMPO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMPO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
