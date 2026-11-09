---
symbol: "SAMD4A"
type: "gene"
col: 322
ensembl_id: "ENSG00000020577"
name: "sterile alpha motif domain containing 4A"
location: "14q22.2"
module: 202
arm: "+"
pooled_cpm: 421.33
n_lines_expressing: 48
n_dd_up: 22
n_dd_down: 15
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/202"]
generated_by: "tahoemap"
---

# SAMD4A

*sterile alpha motif domain containing 4A* — 14q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.80× (z +29.6, q 0e+00, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.371× (z -15.6, q 0e+00, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD4A-AS1]] (+0.70, fdr 7e-06, ⚠ same locus), [[RGS20]] (+0.63, fdr 1e-05), [[TRIO]] (+0.62, fdr 1e-05), [[FILIP1L]] (+0.59, fdr 1e-05); moves opposite to [[FHIP1B]] (-0.54, fdr 2e-05), [[NFATC3]] (-0.54, fdr 2e-05), [[SHQ1]] (-0.54, fdr 3e-05).
> It is in [[Module 202]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FRMD6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 322.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.80×** | +29.6 | 0e+00 | 41/46 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.28×** | +12.9 | 1e-35 | 41/46 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.76×** | +12.5 | 9e-34 | 39/47 (SK-MEL-2, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **2.18×** | +12.2 | 3e-32 | 44/46 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.99×** | +10.4 | 4e-23 | 42/45 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.94×** | +10.4 | 4e-23 | 43/45 (LS 180, HT-29, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.86×** | +9.7 | 2e-20 | 40/46 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.80×** | +9.2 | 2e-18 | 36/45 (LS 180, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +7.0 | 2e-10 | 34/46 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.2 | 1e-05 | 25/46 (A-172, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +5.0 | 2e-05 | 31/46 (MIA PaCa-2, LS 180, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +4.9 | 5e-05 | 32/46 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.36×** | +4.5 | 3e-04 | 29/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.33×** | +4.5 | 3e-04 | 31/46 (LS 180, A-427, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.52×** | +4.2 | 0.001 | 25/46 (HS-578T, LS 180, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.66×** | +4.2 | 0.001 | 28/44 (HS-578T, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.055 | 24/46 (A-172, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.079 | 23/45 (SNU-1, NCI-H460, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.21×** | +3.0 | 0.080 | 22/47 (NCI-H460, SNU-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 322.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.371×** | -15.6 | 0e+00 | 44/46 (NCI-H1573, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.382×** | -15.1 | 0e+00 | 46/46 (HepG2/C3A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.532×** | -9.9 | 7e-21 | 40/47 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.535×** | -9.8 | 1e-20 | 42/46 (NCI-H1573, HepG2/C3A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.530×** | -9.6 | 1e-19 | 36/42 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.546×** | -9.1 | 6e-18 | 40/45 (HepG2/C3A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.671×** | -5.7 | 9e-07 | 33/43 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.527×** | -5.3 | 1e-05 | 35/45 (C32, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.720×** | -5.2 | 1e-05 | 29/46 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.750×** | -4.5 | 3e-04 | 25/46 (HepG2/C3A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.777×** | -4.0 | 0.004 | 26/46 (SW48, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.792×** | -3.5 | 0.024 | 23/46 (HepG2/C3A, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **0.806×** | -3.4 | 0.030 | 24/46 (A498, BT-474, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.808×** | -3.4 | 0.031 | 22/46 (C32, HepG2/C3A, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.814×** | -3.2 | 0.044 | 22/46 (HepG2/C3A, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 322. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 289 | 21 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +23.2) | — |
| [[HepG2_C3A (line)]] | wt | 1,623 | 0 | 17 (11 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -22.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.160× (z -19.2) |
| [[LS 180 (line)]] | wt | 303 | 14 (5 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.36× (z +30.7) | [[Dinaciclib (drug)]] 5 µM 0.440× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.459× (z -8.5) |
| [[A-172 (line)]] | wt | 247 | 11 (3 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +26.8) | [[Dinaciclib (drug)]] 0.05 µM 0.394× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.454× (z -9.0) |
| [[C32 (line)]] | wt | 487 | 4 (1 ⚠) | 10 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +22.1) | [[Panobinostat (drug)]] 5 µM 0.278× (z -15.5) |
| [[BT-474 (line)]] | alt | 242 | 7 (2 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +12.4) | [[Belinostat (drug)]] 5 µM 0.193× (z -12.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.209× (z -11.7) |
| [[PANC-1 (line)]] | alt | 346 | 8 (3 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.420× (z -10.8) |
| [[HS-578T (line)]] | alt | 230 | 10 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 6.25× (z +26.1) | [[Panobinostat (drug)]] 0.5 µM 0.329× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 590 | 5 (2 ⚠) | 7 (5 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.77× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.0996× (z -20.8) |
| [[CFPAC-1 (line)]] | alt | 1,323 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.215× (z -15.5) |
| [[MIA PaCa-2 (line)]] | alt | 182 | 10 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 17.5× (z +34.4) | [[Panobinostat (drug)]] 5 µM 0.357× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 361 | 6 (2 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +23.4) | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 633 | 5 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.282× (z -12.3) |
| [[LoVo (line)]] | wt | 252 | 9 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +29.8) | [[Panobinostat (drug)]] 5 µM 0.385× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 440 | 6 (2 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.316× (z -11.0) |
| [[A549 (line)]] | wt | 457 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.208× (z -17.8) |
| [[HT-29 (line)]] | alt | 281 | 8 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +27.3) | [[Panobinostat (drug)]] 0.5 µM 0.441× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 254 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.60× (z +33.2) | — |
| [[SNU-1 (line)]] | wt | 443 | 5 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +22.1) | [[Belinostat (drug)]] 5 µM 0.219× (z -14.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.229× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 930 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.317× (z -12.4) |
| [[RKO (line)]] | wt | 849 | 1 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.391× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 169 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +16.9) | — |
| [[SW480 (line)]] | alt | 251 | 3 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +18.7) | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -14.8) |
| [[A498 (line)]] | wt | 307 | 5 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +14.5) | [[Panobinostat (drug)]] 0.5 µM 0.380× (z -9.5) |
| [[J82 (line)]] | alt | 363 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +23.1) | [[Panobinostat (drug)]] 5 µM 0.282× (z -13.7) |
| [[NCI-H2030 (line)]] | alt | 1,075 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -15.7) |
| [[hTERT-HPNE (line)]] | wt | 408 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 7.84× (z +26.0) | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 313 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.22× (z +31.5) | — |
| [[SW48 (line)]] | wt | 358 | 2 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +17.0) | [[Panobinostat (drug)]] 0.5 µM 0.329× (z -11.2) |
| [[A-427 (line)]] | wt | 155 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +24.1) | — |
| [[C-33 A (line)]] | alt | 170 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.295× (z -12.7) |
| [[COLO 205 (line)]] | alt | 263 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 7.83× (z +22.0) | [[Panobinostat (drug)]] 5 µM 0.219× (z -11.5) |
| [[HOP62 (line)]] | alt | 388 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.37× (z +29.6) | [[Panobinostat (drug)]] 5 µM 0.396× (z -9.7) |
| [[Hs 766T (line)]] | wt | 167 | 3 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +19.4) | [[Panobinostat (drug)]] 0.5 µM 0.393× (z -9.1) |
| [[H4 (line)]] | wt | 379 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.65× (z +22.8) | — |
| [[HEC-1-A (line)]] | alt | 120 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +21.8) | [[Panobinostat (drug)]] 0.5 µM 0.363× (z -12.7) |
| [[NCI-H2347 (line)]] | alt | 950 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -14.3) |
| [[SNU-423 (line)]] | alt | 184 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.72× (z +28.7) | [[Panobinostat (drug)]] 0.5 µM 0.427× (z -9.9) |
| [[SW 1271 (line)]] | alt | 514 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.250× (z -8.7) |
| [[HCT15 (line)]] | alt | 377 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +17.5) | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[AsPC-1 (line)]] | alt | 350 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +22.0) | — |
| [[CHP-212 (line)]] | wt | 111 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +12.2) | — |
| [[NCI-H661 (line)]] | alt | 597 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.236× (z -9.1) |
| [[SW1417 (line)]] | alt | 466 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.415× (z -9.3) |
| [[AN3 CA (line)]] | alt | 401 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.3) | — |
| [[SW 1088 (line)]] | alt | 385 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +12.3) | — |
| [[KATO III (line)]] | alt | 30.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1,022 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 399 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 322), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD4A-AS1]] | +0.70 | +0.68 / +0.65 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[RGS20]] | +0.63 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[TRIO]] | +0.62 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[FILIP1L]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MGLL]] | +0.58 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[PGM5P2-1]] | +0.57 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[SMCO2]] | +0.56 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[ETS1]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[RAB30-DT]] | +0.56 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[CREB5]] | +0.55 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[HIVEP2]] | +0.55 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[CREB1]] | +0.55 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[CFLAR-AS1]] | +0.54 | +0.51 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FHIP1B]] | -0.54 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[NFATC3]] | -0.54 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[SHQ1]] | -0.54 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[PPT2]] | -0.53 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[PIK3R2]] | -0.53 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[LPCAT3]] | -0.52 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[NUDT21]] | -0.52 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[USPL1]] | -0.52 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[NUP160]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[ATPAF2]] | -0.51 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[PLA2G12A]] | -0.51 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[MARCHF6]] | -0.51 | -0.51 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMD6]] | B | FRMD6 activity raises SAMD4A's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 1.95× lower at baseline in the lines without FRMD6 | 0.035 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[LY6K]] | B | LY6K activity raises SAMD4A's level | lines that do not express LY6K (32) vs lines expressing it (18) | 1.85× lower at baseline in the lines without LY6K | 0.064 | ⚠ within organs, on part of the lines; also absent: IL6, STEAP1B-AS1, TNIP3 |
| [[MAP2K1]] | B | MAP2K1 activity lowers SAMD4A's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 202]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.5, 12.9); signed map (27.2, 10.3). **Vector** length 139, 48.7% of its response variance represented; |z| ≥ 3 in 2,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +12.7 | +12.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +12.3 | +10.4 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +12.0 | +12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +11.9 | +29.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +11.3 | +12.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +10.9 | +9.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +10.2 | +9.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +7.7 | +4.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -15.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.9 | -1.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.7 | -15.6 |
|  | [[NG25 (drug)]] 5 µM |  | -4.6 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.1 | -4.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.3 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | sterile alpha motif domain containing 4A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.2 — chr14:54,566,117-54,793,315 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1053, DKFZP434H0350, Smaug, SMG, SMGA, hSmaug1; previously SAMD4 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPU9](https://www.uniprot.org/uniprotkb/Q9UPU9) (Protein Smaug homolog 1):

> Acts as a translational repressor of SRE-containing messengers.

**Summary**, from NCBI Gene [23034](https://www.ncbi.nlm.nih.gov/gene/23034):

> Sterile alpha motifs (SAMs) in proteins such as SAMD4A are part of an RNA-binding domain that functions as a posttranscriptional regulator by binding to an RNA sequence motif known as the Smaug recognition element, which was named after the Drosophila Smaug protein (Baez and Boccaccio, 2005 [PubMed 16221671]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:23023](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23023) · Entrez [23034](https://www.ncbi.nlm.nih.gov/gene/23034) · UniProt [Q9UPU9](https://www.uniprot.org/uniprotkb/Q9UPU9) · Ensembl [ENSG00000020577](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000020577)

## Data

Gene col 322: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 322); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 322, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 322]; `tensor/DDL_lfc|DDL_z.npy` [322]; `embed/gene_vectors.npy` [322]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 322 or target_col == 322). Every well: [[SAMD4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAMD4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
