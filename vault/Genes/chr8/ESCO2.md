---
symbol: "ESCO2"
type: "gene"
col: 10093
ensembl_id: "ENSG00000171320"
name: "establishment of sister chromatid cohesion N-acetyltransferase 2"
location: "8p21.1"
module: 91
arm: "+"
pooled_cpm: 14.83
n_lines_expressing: 49
n_dd_up: 43
n_dd_down: 21
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# ESCO2

*establishment of sister chromatid cohesion N-acetyltransferase 2* — 8p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (31 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.50× (z +22.1, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.660× (z -6.2, q 3e-07, down in 25 of 46 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.746× (z -4.4, q 0.001, down in 24 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[E2F8]] (+0.87, fdr 7e-06), [[FAM111B]] (+0.86, fdr 7e-06), [[ZWINT]] (+0.84, fdr 7e-06).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 32 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 31 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10093.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.50×** | +22.1 | 0e+00 | 43/45 (NCI-H2347, A549, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **4.13×** | +20.9 | 0e+00 | 37/45 (A549, NCI-H2347, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **5.35×** | +16.8 | 0e+00 | 46/46 (J82, HEC-1-A, …) | rises with dose | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **3.24×** | +11.8 | 8e-30 | 37/43 (HOP62, SW480, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **3.24×** | +11.8 | 8e-30 | 42/46 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **2.96×** | +11.3 | 2e-27 | 40/46 (A549, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.80×** | +10.7 | 1e-24 | 39/47 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.88×** | +9.3 | 1e-18 | 29/47 (NCI-H2347, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.43×** | +8.9 | 4e-17 | 22/28 (PANC-1, SHP-77, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.29×** | +8.6 | 4e-16 | 26/35 (SW480, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.22×** | +8.3 | 7e-15 | 33/46 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.29×** | +8.0 | 8e-14 | 24/32 (MIA PaCa-2, A-172, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.13×** | +7.8 | 2e-13 | 32/46 (A549, HEC-1-A, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +6.6 | 2e-09 | 25/45 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.20× | +6.2 | 2e-08 | 20/47 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +5.0 | 2e-05 | 23/45 (LoVo, SNU-423, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | **1.33×** | +4.1 | 8e-04 | 13/47 (A549, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +3.7 | 0.004 | 18/46 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **1.41×** | +3.5 | 0.007 | 8/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 5 µM |  | **1.53×** | +3.2 | 0.019 | 7/45 (A-427, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.33×** | +2.9 | 0.049 | 10/47 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **1.33×** | +2.9 | 0.055 | 8/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.22×** | +2.9 | 0.059 | 13/47 (SW480, J82, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +2.8 | 0.069 | 17/44 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10093.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.660×** | -6.2 | 3e-07 | 25/46 (LS 180, A-427, …) | all doses, flat | low cells (technical?) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.442×** | -6.1 | 3e-07 | 28/47 (SW480, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.669×** | -6.0 | 4e-07 | 32/47 (RKO, NCI-H2030, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.568×** | -5.9 | 4e-07 | 26/45 (Hs 766T, A-172, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.585×** | -5.6 | 2e-06 | 28/47 (RPMI-7951, Hs 766T, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.746×** | -4.4 | 0.001 | 24/47 (Hs 766T, SHP-77, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.588×** | -4.0 | 0.005 | 14/47 (NCI-H23, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.628×** | -4.0 | 0.005 | 22/45 (MIA PaCa-2, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.697×** | -3.8 | 0.009 | 19/44 (Hs 766T, HCT15, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.701×** | -3.7 | 0.010 | 15/47 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.657×** | -3.6 | 0.017 | 12/47 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 5 µM |  | **0.553×** | -3.3 | 0.054 | 8/45 (MIA PaCa-2, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.692×** | -3.2 | 0.054 | 17/47 (A-427, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.565×** | -3.1 | 0.068 | 11/47 (LS 180, KATO III, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.661×** | -3.1 | 0.069 | 14/47 (MIA PaCa-2, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.748×** | -3.1 | 0.074 | 13/44 (NCI-H460, Panc 03.27, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.577×** | -3.0 | 0.077 | 16/46 (A-427, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.577×** | -3.0 | 0.077 | 10/47 (COLO 205, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 5 µM |  | **0.578×** | -3.0 | 0.077 | 15/44 (KATO III, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.754×** | -3.0 | 0.077 | 13/45 (RKO, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 0.05 µM |  | **0.705×** | -3.0 | 0.077 | 4/46 (NCI-H460, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.57 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10093. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 10.6 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.7× (z +19.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +15.7) | — |
| [[A-172 (line)]] | wt | 26.8 | 4 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +12.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +9.1) | [[Selinexor (drug)]] 5 µM 0.251× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 22.0 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.64× (z +17.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 33.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.78× (z +16.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +14.7) | — |
| [[HOP62 (line)]] | alt | 8.56 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.25× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 9.08 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +14.4) | — |
| [[NCI-H2347 (line)]] | alt | 13.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.99× (z +18.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.83× (z +17.5) | — |
| [[A498 (line)]] | wt | 10.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +8.6) ⚠ cell-cycle shift, explains ~31% of this change | [[Selinexor (drug)]] 5 µM 0.253× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 12.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 11.5× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +8.8) | [[Selinexor (drug)]] 5 µM 0.258× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 15.6 | 2 (2 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +10.0) ⚠ cell-cycle shift, explains ~53% of this change | [[Bortezomib (drug)]] 0.05 µM 0.0416× (z -11.3) ⚠ cell-cycle shift, explains ~80% of this change |
| [[PANC-1 (line)]] | alt | 6.89 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.56× (z +14.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +12.5) | — |
| [[SW480 (line)]] | alt | 21.0 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +13.7) | — |
| [[A-427 (line)]] | wt | 41.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0753× (z -15.7) |
| [[BT-474 (line)]] | alt | 12.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.58× (z +13.5) | — |
| [[CFPAC-1 (line)]] | alt | 7.10 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +12.9) | — |
| [[Hs 766T (line)]] | wt | 17.2 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.188× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 5.39 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.9× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 16.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +12.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 11.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.92× (z +12.5) | — |
| [[RKO (line)]] | wt | 31.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +11.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[RPMI-7951 (line)]] | alt | 11.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +11.5) | — |
| [[SNU-423 (line)]] | alt | 6.37 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.99× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 7.69 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +11.2) | — |
| [[C-33 A (line)]] | alt | 30.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +8.9) | — |
| [[C32 (line)]] | wt | 4.99 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.90× (z +8.5) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.114× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0738× (z -15.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 4.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.5× (z +11.3) | — |
| [[NCI-H460 (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.276× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 42.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +12.2) | — |
| [[SK-MEL-2 (line)]] | alt | 15.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.56× (z +11.9) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SNU-1 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.146× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 8.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +10.3) | — |
| [[AN3 CA (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10093), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[E2F8]] | +0.87 | +0.83 / +0.89 | both halves | 7e-06 | STRING 407 |
| [[FAM111B]] | +0.86 | +0.82 / +0.89 | both halves | 7e-06 | STRING 508 |
| [[ZWINT]] | +0.84 | +0.81 / +0.86 | both halves | 7e-06 | STRING 413 |
| [[BRCA2]] | +0.84 | +0.87 / +0.81 | both halves | 7e-06 | STRING 480 |
| [[KIF24]] | +0.83 | +0.80 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[CENPH]] | +0.83 | +0.82 / +0.81 | both halves | 7e-06 | STRING 443 |
| [[BRIP1]] | +0.82 | +0.83 / +0.82 | both halves | 7e-06 | STRING 561 |
| [[GEN1]] | +0.82 | +0.85 / +0.79 | both halves | 7e-06 | STRING 415 |
| [[MASTL]] | +0.82 | +0.81 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CLSPN]] | +0.81 | +0.75 / +0.86 | both halves | 7e-06 | STRING 577 |
| [[MCM10]] | +0.81 | +0.77 / +0.87 | both halves | 7e-06 | STRING 801 |
| [[MCM4]] | +0.81 | +0.77 / +0.81 | both halves | 7e-06 | pathway: S Phase; STRING 642 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ESCO2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.8% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TCF19]] | B | TCF19 activity raises ESCO2's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.62× lower at baseline in the lines without TCF19 | 0.025 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises ESCO2's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.43× lower at baseline in the lines without CDC25A | 0.031 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[MYBL1]] | B | MYBL1 activity raises ESCO2's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.66× lower at baseline in the lines without MYBL1 | 0.053 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises ESCO2's level | compounds that target MTOR: 4 of 8 lower it (AZD-8055, Bimiralisib, Sapanisertib, Temsirolimus) | 50% of the class's compounds vs 3.9% of all compounds | 0.060 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[E2F8]] | B | E2F8 activity raises ESCO2's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.24× lower at baseline in the lines without E2F8 | 0.096 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[MYBL2]] | C | MYBL2 activity raises ESCO2's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.69× lower at baseline in the lines without MYBL2 | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises ESCO2's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.28× lower at baseline in the lines without MCM10 | 0.072 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.824). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-39.6, -47.5); signed map (-42.6, -47.1). **Vector** length 118, 38.0% of its response variance represented; |z| ≥ 3 in 1,326 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.72 to 5); *Resolution of D-loop Structures through Holliday Junction Intermediates* (reactome, mean cos +0.77 to 4); *Resolution of D-Loop Structures* (reactome, mean cos +0.77 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +6.9 | +16.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +6.6 | +11.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +6.1 | +11.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +22.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.0 | +9.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.1 | +2.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.8 | +2.6 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.5 | +1.6 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.4 | +1.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.2 | -6.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.8 | -5.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~80% of this change | -5.9 | -4.0 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | -4.3 | -5.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.1 | -4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.4 | -1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.1 | +0.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | establishment of sister chromatid cohesion N-acetyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.1 — chr8:27,771,949-27,812,640 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EFO2; previously RBS |
| Gene groups (HGNC) | Lysine acetyltransferases |
| Reactome | 4 pathways, smallest: Establishment of Sister Chromatid Cohesion; S Phase; Cell Cycle, Mitotic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q56NI9](https://www.uniprot.org/uniprotkb/Q56NI9) (N-acetyltransferase ESCO2):

> Acetyltransferase required for the establishment of sister chromatid cohesion. Couples the processes of cohesion and DNA replication to ensure that only sister chromatids become paired together. In contrast to the structural cohesins, the deposition and establishment factors are required only during the S phase. Acetylates the cohesin component SMC3.

**Summary**, from NCBI Gene [157570](https://www.ncbi.nlm.nih.gov/gene/157570):

> This gene encodes a protein that may have acetyltransferase activity and may be required for the establishment of sister chromatid cohesion during the S phase of mitosis. Mutations in this gene have been associated with Roberts syndrome. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:27230](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27230) · Entrez [157570](https://www.ncbi.nlm.nih.gov/gene/157570) · UniProt [Q56NI9](https://www.uniprot.org/uniprotkb/Q56NI9) · Ensembl [ENSG00000171320](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171320)

## Data

Gene col 10093: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10093); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10093, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10093]; `tensor/DDL_lfc|DDL_z.npy` [10093]; `embed/gene_vectors.npy` [10093]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10093 or target_col == 10093). Every well: [[ESCO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ESCO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
