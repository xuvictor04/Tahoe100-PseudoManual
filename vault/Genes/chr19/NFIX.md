---
symbol: "NFIX"
type: "gene"
col: 174
ensembl_id: "ENSG00000008441"
name: "nuclear factor I X"
location: "19p13.13"
module: 14
arm: "+"
pooled_cpm: 79.26
n_lines_expressing: 42
n_dd_up: 9
n_dd_down: 19
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# NFIX

*nuclear factor I X* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.52× (z +11.7, q 1e-28, up in 27 of 40 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.05 µM: 1.28× (z +5.0, q 6e-05, up in 18 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.465× (z -15.3, q 0e+00, down in 37 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCOR]] (+0.71, fdr 7e-06), [[TNFAIP2]] (+0.64, fdr 1e-05), [[CILK1]] (+0.64, fdr 7e-06); moves opposite to [[ZNF731P]] (-0.54, fdr 2e-04), [[FBXW7]] (-0.54, fdr 2e-05), [[CAP1]] (-0.52, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CCL5]] → it (grade B ⚠); 2 go from it, the strongest it → [[YY1AP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 174.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.52×** | +11.7 | 1e-28 | 27/40 (J82, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +9.0 | 9e-17 | 26/35 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +7.3 | 5e-11 | 25/40 (HEC-1-A, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.44×** | +7.1 | 1e-10 | 21/40 (J82, PANC-1, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +5.0 | 6e-05 | 18/40 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +4.9 | 1e-04 | 21/40 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.26×** | +4.7 | 2e-04 | 19/39 (RPMI-7951, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.26×** | +4.3 | 0.001 | 17/36 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.005 | 13/40 (KATO III, HepG2/C3A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +3.6 | 0.015 | 7/40 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.16× | +3.5 | 0.023 | 10/41 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +3.5 | 0.023 | 10/40 (SK-MEL-2, NCI-H1792, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.5 | 0.023 | 11/40 (KATO III, HS-578T, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.034 | 12/40 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.037 | 8/40 (MIA PaCa-2, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | 1.16× | +3.2 | 0.043 | 13/41 (SW480, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 174.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.465×** | -15.3 | 0e+00 | 37/40 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.483×** | -14.5 | 1e-45 | 38/40 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.505×** | -13.6 | 4e-40 | 37/40 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.602×** | -9.5 | 2e-19 | 28/40 (C32, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.623×** | -9.4 | 5e-19 | 30/40 (LS 180, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.639×** | -8.9 | 4e-17 | 33/40 (SW480, LS 180, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.695×** | -7.0 | 3e-10 | 26/40 (C32, H4, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.705×** | -7.0 | 3e-10 | 27/40 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.802×** | -6.2 | 3e-08 | 22/40 (A498, PANC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.822×** | -5.4 | 4e-06 | 20/40 (HEC-1-A, SNU-1, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.784×** | -4.8 | 7e-05 | 23/40 (SW1417, A-427, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.796×** | -4.5 | 3e-04 | 18/40 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.852× | -4.4 | 5e-04 | 21/40 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.660×** | -4.3 | 6e-04 | 17/41 (SK-MEL-2, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.773×** | -4.3 | 6e-04 | 19/40 (PANC-1, C32, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.813×** | -3.9 | 0.003 | 15/39 (C32, COLO 205, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.796×** | -3.8 | 0.004 | 14/40 (C32, H4, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.826×** | -3.2 | 0.040 | 14/40 (H4, hTERT-HPNE, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 174. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 182 | 6 (5 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +17.6) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.47× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -19.6) |
| [[C32 (line)]] | wt | 196 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.201× (z -17.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.201× (z -16.8) |
| [[SW480 (line)]] | alt | 80.7 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -20.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.240× (z -18.3) |
| [[MIA PaCa-2 (line)]] | alt | 159 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.284× (z -15.3) |
| [[HT-29 (line)]] | alt | 64.1 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -13.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.289× (z -12.9) |
| [[LS 180 (line)]] | wt | 166 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -26.0) |
| [[AN3 CA (line)]] | alt | 238 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0575× (z -23.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.153× (z -15.5) |
| [[C-33 A (line)]] | alt | 61.5 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.44× (z +9.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.201× (z -12.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.223× (z -11.9) |
| [[HEC-1-A (line)]] | alt | 77.1 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.476× (z -9.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.485× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 31.3 | 2 (1 ⚠) | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.55× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.303× (z -12.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.321× (z -12.0) |
| [[J82 (line)]] | alt | 78.9 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +23.6) ⚠ cell-cycle shift, explains ~53% of this change | [[Panobinostat (drug)]] 5 µM 0.480× (z -9.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 28.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +9.0) ⚠ toxic; transcription drop | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -8.6) ⚠ cell-cycle shift, explains ~60% of this change |
| [[A498 (line)]] | wt | 179 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.9) ⚠ cell-cycle shift, explains ~53% of this change | [[Panobinostat (drug)]] 0.5 µM 0.326× (z -11.3) |
| [[BT-474 (line)]] | alt | 22.9 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +10.2) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[H4 (line)]] | wt | 130 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -10.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.376× (z -8.6) |
| [[LoVo (line)]] | wt | 63.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.248× (z -16.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.276× (z -15.4) |
| [[RKO (line)]] | wt | 54.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -12.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.209× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 136 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +11.7) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[SNU-1 (line)]] | wt | 126 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.245× (z -12.7) |
| [[SNU-423 (line)]] | alt | 127 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +12.0) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 40.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -11.2) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.342× (z -10.5) |
| [[A-172 (line)]] | wt | 237 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.1) ⚠ cell-cycle shift, explains ~53% of this change | [[Panobinostat (drug)]] 0.5 µM 0.390× (z -9.4) |
| [[CHP-212 (line)]] | wt | 162 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -9.5) |
| [[COLO 205 (line)]] | alt | 55.8 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.213× (z -12.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.282× (z -9.6) |
| [[HOP62 (line)]] | alt | 27.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.42× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 42.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.12× (z +18.7) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[Panc 03.27 (line)]] | alt | 89.4 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.3) ⚠ cell-cycle shift, explains ~53% of this change | [[Ixazomib citrate (drug)]] 0.5 µM 0.430× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 21.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +8.9) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[HepG2_C3A (line)]] | wt | 31.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -9.5) |
| [[HS-578T (line)]] | alt | 216 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.65× (z +9.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 50.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 68.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.403× (z -8.9) |
| [[SW48 (line)]] | wt | 66.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.299× (z -9.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A549 (line)]] | wt | 16.2 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 106 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.1 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.8 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 19.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.79 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 174), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCOR]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[TNFAIP2]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[CILK1]] | +0.64 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[ANO9]] | +0.62 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[GSE1]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[STAT5A]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ZNF608]] | +0.61 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[AJUBA]] | +0.61 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[BAHCC1]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[TEF]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[GLIS2]] | +0.59 | +0.67 / +0.43 | both halves | 3e-05 |  |
| [[REPIN1]] | +0.59 | +0.60 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF731P]] | -0.54 | -0.70 / -0.31 | both halves | 2e-04 |  |
| [[FBXW7]] | -0.54 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[CAP1]] | -0.52 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[GBA2]] | -0.52 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[S100A16]] | -0.51 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ITGA2]] | -0.51 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[POMP]] | -0.50 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[DOCK5]] | -0.50 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[TANGO2]] | -0.49 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[SLC35C1]] | -0.49 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[NAPG]] | -0.49 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[ABTB3]] | -0.49 | -0.47 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCL5]] | B | CCL5 activity raises NFIX's level | lines that do not express CCL5 (22) vs lines expressing it (28) | 1.21× lower at baseline in the lines without CCL5 | 0.057 | ⚠ within organs, on part of the lines; also absent: SRGN, FLI1, KCNMA1 |
| [[KREMEN2]] | B | KREMEN2 activity weakens NFIX's drug response | lines that do not express KREMEN2 (11) vs lines expressing it (30) | the lines without KREMEN2 respond 1.25× as strongly (z diff -0.75); strongest at Dinaciclib 5 µM: 2.52x vs 1.37x (z diff -5.6) | 0.060 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[YY1AP1]] | B | NFIX activity lowers YY1AP1's level | lines that do not express NFIX (8) vs lines expressing it (42) | 1.46× higher at baseline in the lines without NFIX | 0.038 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SLC39A1]] | B | NFIX activity lowers SLC39A1's level | lines that do not express NFIX (8) vs lines expressing it (42) | 1.36× higher at baseline in the lines without NFIX | 0.096 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.7, -2.2); signed map (45.3, 5.2). **Vector** length 112, 29.4% of its response variance represented; |z| ≥ 3 in 1,084 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +10.1 | +11.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +6.4 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.1 | +3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.0 | +3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.1 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +3.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.5 | +3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.5 | +3.5 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.6 | -8.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.6 | -9.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -5.3 | -9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -3.2 | -4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.9 | -3.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.6 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | nuclear factor I X |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,995,475-13,098,796 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NF1A |
| Gene groups (HGNC) | Nuclear factor I family |
| Reactome | 3 pathways, smallest: RNA Polymerase III Transcription Termination; RNA Polymerase III Abortive And Retractive Initiation; RNA Polymerase III Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14938](https://www.uniprot.org/uniprotkb/Q14938) (Nuclear factor 1 X-type):

> Recognizes and binds the palindromic sequence 5'-TTGGCNNNNNGCCAA-3' present in viral and cellular promoters and in the origin of replication of adenovirus type 2. These proteins are individually capable of activating transcription and replication.

**Summary**, from NCBI Gene [4784](https://www.ncbi.nlm.nih.gov/gene/4784):

> The protein encoded by this gene is a transcription factor that binds the palindromic sequence 5'-TTGGCNNNNNGCCAA-3 in viral and cellular promoters. The encoded protein can also stimulate adenovirus replication in vitro. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:7788](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7788) · Entrez [4784](https://www.ncbi.nlm.nih.gov/gene/4784) · UniProt [Q14938](https://www.uniprot.org/uniprotkb/Q14938) · Ensembl [ENSG00000008441](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008441)

## Data

Gene col 174: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 174); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 174, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 174]; `tensor/DDL_lfc|DDL_z.npy` [174]; `embed/gene_vectors.npy` [174]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 174 or target_col == 174). Every well: [[NFIX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFIX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
