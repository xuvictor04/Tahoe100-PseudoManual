---
symbol: "HIVEP2"
type: "gene"
col: 217
ensembl_id: "ENSG00000010818"
name: "HIVEP zinc finger 2"
location: "6q24.2"
module: 14
arm: "+"
pooled_cpm: 404.71
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 22
n_dd_up_clean: 13
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# HIVEP2

*HIVEP zinc finger 2* — 6q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.18× (z +29.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.305× (z -17.2, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFKB1]] (+0.72, fdr 7e-06), [[ZC3H12C]] (+0.70, fdr 1e-05), [[HIVEP2-DT]] (+0.70, fdr 7e-06, ⚠ same locus), [[HIVEP1]] (+0.69, fdr 7e-06); moves opposite to [[INPP5B]] (-0.67, fdr 1e-05), [[NFATC3]] (-0.66, fdr 1e-05), [[PPIL2]] (-0.66, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZC3H12C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 217.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.18×** | +29.2 | 0e+00 | 47/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.15×** | +19.7 | 0e+00 | 48/48 (RPMI-7951, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.89×** | +12.0 | 9e-31 | 46/49 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.98×** | +9.8 | 1e-20 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +8.5 | 2e-15 | 40/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.79×** | +8.4 | 6e-15 | 41/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +7.2 | 7e-11 | 42/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +6.5 | 7e-09 | 39/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.8 | 3e-07 | 32/47 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +5.5 | 2e-06 | 33/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.92×** | +4.9 | 5e-05 | 35/48 (hTERT-HPNE, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.84×** | +4.6 | 2e-04 | 38/48 (C32, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.32×** | +4.0 | 0.003 | 33/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.58×** | +3.4 | 0.026 | 34/48 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.077 | 25/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.079 | 27/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 217.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.305×** | -17.2 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.334×** | -15.9 | 0e+00 | 48/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.385×** | -13.8 | 3e-41 | 46/49 (NCI-H23, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.412×** | -12.9 | 1e-35 | 48/48 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.421×** | -12.1 | 2e-31 | 42/44 (A-427, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.521×** | -9.1 | 9e-18 | 47/47 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.723×** | -6.7 | 2e-09 | 39/49 (A549, NCI-H1792, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.670×** | -5.8 | 4e-07 | 38/48 (HT-29, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.679×** | -5.6 | 1e-06 | 42/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.686×** | -5.5 | 2e-06 | 40/48 (AN3 CA, SW1417, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.702×** | -5.2 | 1e-05 | 41/48 (HT-29, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.506×** | -5.2 | 1e-05 | 36/45 (LOX-IMVI, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.523×** | -4.9 | 4e-05 | 40/47 (MIA PaCa-2, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.701×** | -4.8 | 7e-05 | 31/45 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.721×** | -4.8 | 7e-05 | 38/48 (HepG2/C3A, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.747×** | -4.0 | 0.002 | 31/48 (A549, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.643×** | -3.4 | 0.025 | 29/49 (AsPC-1, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.808×** | -3.1 | 0.052 | 27/49 (SNU-423, HS-578T, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.820×** | -2.9 | 0.096 | 25/48 (A-427, SNU-423, …) | top dose only |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.811×** | -2.9 | 0.096 | 24/47 (CHP-212, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 217. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 291 | 14 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 7.90× (z +30.9) | [[Panobinostat (drug)]] 0.5 µM 0.429× (z -9.0) |
| [[HS-578T (line)]] | alt | 624 | 9 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +24.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -14.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.317× (z -13.5) |
| [[SW 900 (line)]] | alt | 522 | 8 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.8) | [[Panobinostat (drug)]] 5 µM 0.336× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 716 | 8 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +22.5) | [[Dinaciclib (drug)]] 5 µM 0.293× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.313× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 755 | 6 | 7 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 5.89× (z +19.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -15.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.261× (z -15.2) |
| [[A549 (line)]] | wt | 357 | 7 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +27.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -16.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.240× (z -14.8) |
| [[HOP62 (line)]] | alt | 541 | 7 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.72× (z +21.0) | [[Panobinostat (drug)]] 5 µM 0.258× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 280 | 6 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +24.2) | [[Panobinostat (drug)]] 0.5 µM 0.308× (z -13.7) |
| [[PANC-1 (line)]] | alt | 299 | 9 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.64× (z +32.8) | [[Dinaciclib (drug)]] 0.5 µM 0.479× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.480× (z -9.0) |
| [[SNU-423 (line)]] | alt | 727 | 6 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.86× (z +27.4) | [[Panobinostat (drug)]] 5 µM 0.269× (z -13.2) |
| [[A-427 (line)]] | wt | 446 | 6 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +21.8) | [[Panobinostat (drug)]] 5 µM 0.234× (z -16.3) |
| [[A498 (line)]] | wt | 359 | 6 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.23× (z +32.2) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.374× (z -11.3) |
| [[BT-474 (line)]] | alt | 242 | 9 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +22.2) | [[Panobinostat (drug)]] 5 µM 0.387× (z -9.5) |
| [[C32 (line)]] | wt | 468 | 4 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +18.8) | [[Panobinostat (drug)]] 5 µM 0.331× (z -12.6) |
| [[HEC-1-A (line)]] | alt | 444 | 5 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +29.3) | [[Panobinostat (drug)]] 5 µM 0.253× (z -17.3) |
| [[NCI-H1573 (line)]] | alt | 539 | 6 (1 ⚠) | 4 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.37× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.217× (z -14.7) |
| [[CFPAC-1 (line)]] | alt | 353 | 4 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +28.7) | [[Panobinostat (drug)]] 5 µM 0.321× (z -13.8) |
| [[RPMI-7951 (line)]] | alt | 423 | 6 | 3 | [[Harringtonine (drug)]] 5 µM 11.6× (z +24.8) | [[Panobinostat (drug)]] 0.5 µM 0.343× (z -11.3) |
| [[SW480 (line)]] | alt | 354 | 1 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.146× (z -24.1) |
| [[H4 (line)]] | wt | 350 | 4 | 4 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +20.8) | [[Panobinostat (drug)]] 5 µM 0.280× (z -12.3) |
| [[HepG2_C3A (line)]] | wt | 829 | 1 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.180× (z -17.0) |
| [[LoVo (line)]] | wt | 284 | 5 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +25.7) | [[Panobinostat (drug)]] 5 µM 0.300× (z -14.5) |
| [[NCI-H2030 (line)]] | alt | 526 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +19.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.302× (z -12.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.336× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 424 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.263× (z -14.8) |
| [[A-172 (line)]] | wt | 400 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.51× (z +25.5) | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -12.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 406 | 2 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.243× (z -12.5) |
| [[HCT15 (line)]] | alt | 387 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.294× (z -13.0) |
| [[Hs 766T (line)]] | wt | 372 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +21.1) | [[Panobinostat (drug)]] 5 µM 0.268× (z -13.3) |
| [[HT-29 (line)]] | alt | 468 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +14.0) | [[Panobinostat (drug)]] 0.5 µM 0.254× (z -13.8) |
| [[J82 (line)]] | alt | 315 | 3 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +28.4) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.443× (z -9.4) |
| [[KATO III (line)]] | alt | 190 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +26.4) | [[Panobinostat (drug)]] 5 µM 0.281× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 438 | 3 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +22.5) | [[Panobinostat (drug)]] 5 µM 0.315× (z -11.7) |
| [[RKO (line)]] | wt | 727 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.195× (z -17.6) |
| [[AN3 CA (line)]] | alt | 359 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +15.4) | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 568 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -17.6) |
| [[LS 180 (line)]] | wt | 288 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +17.1) | [[Panobinostat (drug)]] 5 µM 0.312× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 410 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +22.9) | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -12.9) |
| [[SW1417 (line)]] | alt | 353 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +22.2) | [[Panobinostat (drug)]] 0.5 µM 0.308× (z -13.0) |
| [[SW48 (line)]] | wt | 429 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +17.5) | — |
| [[AsPC-1 (line)]] | alt | 384 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +20.7) | [[Panobinostat (drug)]] 5 µM 0.284× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 123 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +28.1) | — |
| [[SHP-77 (line)]] | alt | 358 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -17.2) |
| [[SW 1271 (line)]] | alt | 644 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.201× (z -11.1) |
| [[COLO 205 (line)]] | alt | 241 | 2 | 2 | [[Harringtonine (drug)]] 5 µM 5.78× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.260× (z -11.3) |
| [[SNU-1 (line)]] | wt | 374 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +15.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.313× (z -12.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.390× (z -10.1) |
| [[C-33 A (line)]] | alt | 143 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.05 µM 2.92× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | [[Panobinostat (drug)]] 5 µM 0.316× (z -11.2) |
| [[NCI-H661 (line)]] | alt | 257 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.224× (z -9.7) |
| [[SW 1088 (line)]] | alt | 393 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +13.6) | — |
| [[NCI-H2122 (line)]] | alt | 525 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 430 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 217), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKB1]] | +0.72 | +0.70 / +0.66 | both halves | 7e-06 | STRING 559 |
| [[ZC3H12C]] | +0.70 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[HIVEP2-DT]] | +0.70 | +0.67 / +0.59 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[HIVEP1]] | +0.69 | +0.67 / +0.58 | both halves | 7e-06 | same gene group; STRING 460 |
| [[CXCL2]] | +0.65 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[BIRC2]] | +0.65 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[KDM6B]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[APLF]] | +0.64 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[SKIL]] | +0.64 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[IRF2]] | +0.63 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[NFKB2]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[TNFAIP3]] | +0.62 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | +0.62 | +0.45 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP5B]] | -0.67 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[NFATC3]] | -0.66 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[PPIL2]] | -0.66 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[SCAI]] | -0.63 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.63 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[JKAMP]] | -0.62 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[HIBCH]] | -0.62 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[NFRKB]] | -0.61 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[SLC9A6]] | -0.61 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[CDK5RAP1]] | -0.61 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[TNPO3]] | -0.61 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[ATPAF2]] | -0.61 | -0.47 / -0.61 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZC3H12C]] | B | ZC3H12C activity raises HIVEP2's level | lines that do not express ZC3H12C (7) vs lines expressing it (43) | 1.71× lower at baseline in the lines without ZC3H12C | 0.024 | ⚠ within organs, on part of the lines; also absent: TMOD2, KLF12, DPF1 |
| [[C1QTNF1]] | B | C1QTNF1 activity raises HIVEP2's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 1.36× lower at baseline in the lines without C1QTNF1 | 0.096 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3 |
| [[NFKBIZ]] | C | NFKBIZ activity raises HIVEP2's level | lines that do not express NFKBIZ (3) vs lines expressing it (47) | 1.93× lower at baseline in the lines without NFKBIZ | 0.051 | ⚠ few lines (3 vs 47); across organs; also absent: CPEB2, PKIA-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.622). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.2, 9.5); signed map (16.8, -8.9). **Vector** length 114, 50.1% of its response variance represented; |z| ≥ 3 in 1,677 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NF-kB* (control, mean cos +0.57 to 12); *IkBA variant leads to EDA-ID* (reactome, mean cos +0.55 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +11.7 | +19.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +11.2 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.6 | +29.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.7 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +7.1 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.4 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | -2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.9 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | -1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +2.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -9.7 | -3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -8.6 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.2 | -2.2 |
|  | [[NG25 (drug)]] 5 µM |  | -6.0 | -4.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -5.5 | -5.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.5 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -5.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -2.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | HIVEP zinc finger 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.2 — chr6:142,751,469-142,956,698 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MBP-2, HIV-EP2, MIBP1, ZAS2, Schnurri-2, ZNF40B |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [P31629](https://www.uniprot.org/uniprotkb/P31629) (Transcription factor HIVEP2):

> This protein specifically binds to the DNA sequence 5'-GGGACTTTCC-3' which is found in the enhancer elements of numerous viral promoters such as those of SV40, CMV, or HIV1. In addition, related sequences are found in the enhancer elements of a number of cellular promoters, including those of the class I MHC, interleukin-2 receptor, somatostatin receptor II, and interferon-beta genes. It may act in T-cell activation.

**Summary**, from NCBI Gene [3097](https://www.ncbi.nlm.nih.gov/gene/3097):

> This gene encodes a member of a family of closely related, large, zinc finger-containing transcription factors. The encoded protein regulates transcription by binding to regulatory regions of various cellular and viral genes that maybe involved in growth, development and metastasis. The protein contains the ZAS domain comprised of two widely separated regions of zinc finger motifs, a stretch of highly acidic amino acids and a serine/threonine-rich sequence. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:4921](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4921) · Entrez [3097](https://www.ncbi.nlm.nih.gov/gene/3097) · UniProt [P31629](https://www.uniprot.org/uniprotkb/P31629) · Ensembl [ENSG00000010818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010818)

## Data

Gene col 217: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 217); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 217, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 217]; `tensor/DDL_lfc|DDL_z.npy` [217]; `embed/gene_vectors.npy` [217]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 217 or target_col == 217). Every well: [[HIVEP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIVEP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
