---
symbol: "GART"
type: "gene"
col: 8219
ensembl_id: "ENSG00000159131"
name: "phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase"
location: "21q22.11"
module: 18
arm: "+"
pooled_cpm: 81.63
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# GART

*phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase* — 21q22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.99× (z +15.3, q 0e+00, up in 42 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.58× (z +10.6, q 3e-24, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.700× (z -8.0, q 9e-13, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMTC4]] (+0.74, fdr 7e-06), [[ADCY3]] (+0.73, fdr 7e-06), [[DKC1]] (+0.72, fdr 7e-06); moves opposite to [[PI4KB]] (-0.64, fdr 7e-06), [[ASB8]] (-0.63, fdr 7e-06), [[IFT22]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PHLDA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 24 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8219.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +15.3 | 0e+00 | 42/47 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.87×** | +14.5 | 3e-45 | 38/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.75×** | +13.0 | 2e-36 | 42/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.73×** | +12.2 | 3e-32 | 33/44 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.67×** | +11.9 | 2e-30 | 35/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +11.3 | 1e-27 | 33/47 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +10.6 | 3e-24 | 37/48 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.55×** | +10.1 | 3e-22 | 38/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.51×** | +9.5 | 1e-19 | 35/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.51×** | +8.8 | 6e-17 | 33/45 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.29×** | +6.0 | 1e-07 | 24/47 (HS-578T, NCI-H23, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +5.8 | 3e-07 | 20/49 (MIA PaCa-2, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.29×** | +5.6 | 1e-06 | 25/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.27×** | +5.4 | 3e-06 | 26/50 (C32, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 1.18× | +5.3 | 4e-06 | 23/49 (HS-578T, CFPAC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +5.2 | 8e-06 | 26/48 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.25×** | +5.1 | 1e-05 | 22/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.35×** | +4.9 | 2e-05 | 23/48 (NCI-H23, SK-MEL-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +4.3 | 4e-04 | 21/48 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.19× | +3.9 | 0.003 | 20/47 (MIA PaCa-2, H4, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.19× | +3.8 | 0.003 | 14/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.003 | 21/46 (MIA PaCa-2, NCI-H460, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.7 | 0.004 | 19/48 (MIA PaCa-2, HCT15, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.012 | 14/48 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.16× | +3.4 | 0.013 | 18/48 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.034 | 12/48 (SW480, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8219.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.700×** | -8.0 | 9e-13 | 27/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.732×** | -7.0 | 7e-10 | 25/47 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.812×** | -6.9 | 1e-09 | 23/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.822×** | -6.3 | 4e-08 | 21/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.778×** | -6.2 | 9e-08 | 27/50 (A-427, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -5.6 | 3e-06 | 24/48 (RKO, A498, …) | top dose only | composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.826×** | -5.4 | 5e-06 | 20/48 (A-427, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.841× | -4.9 | 5e-05 | 17/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.815×** | -4.8 | 1e-04 | 23/48 (A498, CHP-212, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.841× | -4.4 | 7e-04 | 22/49 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.834× | -4.2 | 0.001 | 19/47 (NCI-H2030, A549, …) | rises with dose | low cells (technical?) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.710×** | -4.2 | 0.001 | 16/50 (CHP-212, A-427, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.836× | -4.2 | 0.001 | 19/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.835× | -4.2 | 0.001 | 20/48 (A-427, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.841× | -4.0 | 0.002 | 15/49 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.843× | -4.0 | 0.002 | 18/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.840× | -3.7 | 0.005 | 18/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.853× | -3.6 | 0.010 | 17/47 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.879× | -3.0 | 0.062 | 9/48 (KATO III, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8219. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 115 | 7 (7 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.38× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -16.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.616× (z -9.2) |
| [[RKO (line)]] | wt | 160 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -19.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.436× (z -10.5) |
| [[A-427 (line)]] | wt | 134 | 1 (1 ⚠) | 7 (6 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.19× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Harringtonine (drug)]] 5 µM 0.232× (z -19.9) |
| [[MIA PaCa-2 (line)]] | alt | 165 | 5 (4 ⚠) | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.30× (z +10.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.391× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.415× (z -10.8) |
| [[PANC-1 (line)]] | alt | 128 | 2 (2 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.73× (z +9.1) ⚠ cell-cycle shift, explains ~26% of this change | [[Harringtonine (drug)]] 5 µM 0.387× (z -15.4) |
| [[NCI-H1573 (line)]] | alt | 64.8 | 6 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.85× (z +16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[A498 (line)]] | wt | 135 | 1 (1 ⚠) | 4 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.74× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -19.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 103 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.361× (z -13.7) |
| [[NCI-H460 (line)]] | wt | 62.9 | 3 (3 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.68× (z +11.1) ⚠ toxic | [[Harringtonine (drug)]] 5 µM 0.369× (z -11.2) |
| [[SW48 (line)]] | wt | 92.6 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.251× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 110 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +9.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 41.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H23 (line)]] | alt | 129 | 2 (2 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.00× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.375× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 59.1 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +10.3) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[CFPAC-1 (line)]] | alt | 38.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[LoVo (line)]] | wt | 89.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.40× (z +10.1) ⚠ toxic | [[Selinexor (drug)]] 5 µM 0.521× (z -11.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.424× (z -9.9) |
| [[SHP-77 (line)]] | alt | 132 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.477× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 33.7 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +9.5) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[C-33 A (line)]] | alt | 123 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[C32 (line)]] | wt | 33.4 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.58× (z +9.6) | — |
| [[H4 (line)]] | wt | 78.7 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.31× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[Hs 766T (line)]] | wt | 39.0 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.45× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[HS-578T (line)]] | alt | 53.3 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +10.9) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[HT-29 (line)]] | alt | 35.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H2347 (line)]] | alt | 44.4 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +10.2) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 116 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.483× (z -8.8) |
| [[SNU-423 (line)]] | alt | 28.6 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +10.1) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[SW1417 (line)]] | alt | 88.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.491× (z -9.0) |
| [[BT-474 (line)]] | alt | 69.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 69.2 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0969× (z -12.3) |
| [[HCT15 (line)]] | alt | 62.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.24× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[KATO III (line)]] | alt | 41.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[LS 180 (line)]] | wt | 59.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.462× (z -9.2) ⚠ cell-cycle shift, explains ~44% of this change |
| [[NCI-H2030 (line)]] | alt | 107 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.07× (z +8.7) ⚠ toxic | — |
| [[Panc 03.27 (line)]] | alt | 57.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[A-172 (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 76.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 79.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8219), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMTC4]] | +0.74 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[ADCY3]] | +0.73 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[DKC1]] | +0.72 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[UCK2]] | +0.72 | +0.78 / +0.67 | both halves | 7e-06 | pathway: Metabolism of nucleotides; STRING 473 |
| [[URB2]] | +0.72 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[PRMT3]] | +0.72 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[ADAT2]] | +0.71 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[WDR4]] | +0.71 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[SEH1L]] | +0.70 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[MDN1]] | +0.70 | +0.79 / +0.63 | both halves | 7e-06 |  |
| [[LETM1]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[UBE2G2]] | +0.69 | +0.76 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PI4KB]] | -0.64 | -0.66 / -0.63 | both halves | 7e-06 |  |
| [[ASB8]] | -0.63 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[IFT22]] | -0.59 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[ATG4D]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[GALT]] | -0.58 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[DNAJB2]] | -0.58 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[OSCP1]] | -0.58 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[ATP5IF1]] | -0.58 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[CTR9]] | -0.57 | -0.67 / -0.49 | both halves | 1e-05 |  |
| [[SECISBP2L]] | -0.57 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[DNAL4]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PHLDA3]] | B | PHLDA3 activity lowers GART's level | lines that do not express PHLDA3 (8) vs lines expressing it (42) | 1.76× higher at baseline in the lines without PHLDA3 | 0.043 | ⚠ within organs, on part of the lines; also absent: EFNB2, PELI1, RPLP0P2 |
| [[NT5M]] | B | NT5M activity raises GART's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.65× lower at baseline in the lines without NT5M | 0.076 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[NUP210]] | B | NUP210 activity raises GART's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 1.42× lower at baseline in the lines without NUP210 | 0.092 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.781). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-8.8, -36.9); signed map (-3.4, -52.9). **Vector** length 129, 43.8% of its response variance represented; |z| ≥ 3 in 1,546 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.7 | +15.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +10.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +4.1 | +8.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.0 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +5.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -10.1 | -8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.0 | -5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.8 | -3.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -5.1 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.2 | -4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.9 | -4.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.7 | -4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.6 | -7.0 |

## What is on record

|  |  |
|---|---|
| Name | phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:33,503,931-33,543,491 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GARS-AIRS-GART; previously PRGS, PGFT |
| Gene groups (HGNC) | Purinosome; ATP-grasp fold containing; Ligases |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 3 pathways, smallest: Purine ribonucleoside monophosphate biosynthesis; Nucleotide biosynthesis; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [P22102](https://www.uniprot.org/uniprotkb/P22102) (Trifunctional purine biosynthetic protein adenosine-3):

> Trifunctional enzyme that catalyzes three distinct reactions as part of the 'de novo' inosine monophosphate biosynthetic pathway.

**Summary**, from NCBI Gene [2618](https://www.ncbi.nlm.nih.gov/gene/2618):

> The protein encoded by this gene is a trifunctional polypeptide. It has phosphoribosylglycinamide formyltransferase, phosphoribosylglycinamide synthetase, phosphoribosylaminoimidazole synthetase activity which is required for de novo purine biosynthesis. This enzyme is highly conserved in vertebrates. Alternative splicing of this gene results in two transcript variants encoding different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4163](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4163) · Entrez [2618](https://www.ncbi.nlm.nih.gov/gene/2618) · UniProt [P22102](https://www.uniprot.org/uniprotkb/P22102) · Ensembl [ENSG00000159131](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159131)

## Data

Gene col 8219: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8219); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8219, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8219]; `tensor/DDL_lfc|DDL_z.npy` [8219]; `embed/gene_vectors.npy` [8219]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8219 or target_col == 8219). Every well: [[GART — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GART.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
