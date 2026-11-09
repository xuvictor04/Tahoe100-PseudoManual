---
symbol: "ACAD11"
type: "gene"
col: 14231
ensembl_id: "ENSG00000240303"
name: "acyl-CoA dehydrogenase family member 11"
location: "3q22.1"
module: 28
arm: "+"
pooled_cpm: 53.04
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 21
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# ACAD11

*acyl-CoA dehydrogenase family member 11* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +10.1, q 2e-21, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (14 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.440× (z -14.5, q 1e-44, down in 40 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.525× (z -11.8, q 4e-30, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF563]] (+0.65, fdr 5e-05), [[IFT46]] (+0.64, fdr 1e-05), [[DCP1B]] (+0.63, fdr 3e-05); moves opposite to [[KANK2]] (-0.62, fdr 2e-04), [[GATAD2B]] (-0.56, fdr 1e-05), [[SPATA13]] (-0.54, fdr 2e-04).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ZNF675]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14231.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +10.1 | 2e-21 | 33/47 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.34×** | +7.6 | 9e-12 | 34/47 (J82, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +4.6 | 9e-04 | 20/47 (LOX-IMVI, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.4 | 0.002 | 19/47 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.25×** | +4.2 | 0.003 | 20/47 (A498, RKO, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.004 | 21/47 (LS 180, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +3.7 | 0.015 | 19/47 (RKO, LoVo, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.020 | 18/46 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.023 | 16/47 (SW480, KATO III, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.16× | +3.1 | 0.10 | 14/47 (SW480, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.12× | +3.1 | 0.10 | 7/47 (LS 180, A-427, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.1 | 0.11 | 8/47 (SW480, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 19 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14231.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.440×** | -14.5 | 1e-44 | 40/46 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.470×** | -13.8 | 4e-41 | 39/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.478×** | -13.5 | 2e-39 | 42/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.493×** | -13.0 | 3e-36 | 39/47 (SK-MEL-2, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.525×** | -11.8 | 4e-30 | 41/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.519×** | -11.6 | 6e-29 | 33/42 (Panc 03.27, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.565×** | -9.7 | 3e-20 | 27/44 (RPMI-7951, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.591×** | -9.6 | 4e-20 | 39/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.613×** | -9.0 | 2e-17 | 37/47 (SNU-423, H4, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.700×** | -6.5 | 4e-09 | 32/47 (PANC-1, NCI-H460, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.728×** | -5.8 | 4e-07 | 27/47 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.734×** | -5.7 | 8e-07 | 30/47 (PANC-1, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.745×** | -5.4 | 3e-06 | 26/47 (MIA PaCa-2, SK-MEL-2, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **0.767×** | -4.8 | 5e-05 | 24/47 (SW 1271, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.774×** | -4.5 | 3e-04 | 22/47 (J82, PANC-1, …) | top dose only | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **0.746×** | -3.8 | 0.004 | 17/47 (H4, SNU-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.833×** | -3.1 | 0.051 | 14/47 (NCI-H23, HEC-1-A, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.842× | -3.0 | 0.060 | 7/47 (PANC-1, J82, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.733×** | -3.0 | 0.065 | 10/47 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.891× | -3.0 | 0.065 | 9/47 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.848× | -2.9 | 0.076 | 13/46 (H4, SW 900, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.854× | -2.9 | 0.076 | 15/46 (NCI-H460, NCI-H2030, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14231. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 36.9 | 1 | 8 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +13.0) | [[Digitoxin (drug)]] 5 µM 0.215× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.286× (z -14.2) |
| [[H4 (line)]] | wt | 97.9 | 0 | 8 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0398× (z -25.6) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.276× (z -10.6) |
| [[J82 (line)]] | alt | 48.6 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.428× (z -8.9) |
| [[PANC-1 (line)]] | alt | 74.5 | 0 | 8 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.192× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.289× (z -16.0) |
| [[RKO (line)]] | wt | 55.6 | 3 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.402× (z -8.6) |
| [[A-172 (line)]] | wt | 56.0 | 1 | 4 (4 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.09× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -13.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 40.6 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +9.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -10.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.247× (z -10.2) |
| [[SNU-423 (line)]] | alt | 55.2 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.301× (z -12.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.368× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 149 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 101 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW480 (line)]] | alt | 51.8 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.338× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.376× (z -11.8) |
| [[C-33 A (line)]] | alt | 68.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.377× (z -8.5) |
| [[HOP62 (line)]] | alt | 54.5 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.332× (z -11.5) ⚠ toxic |
| [[LoVo (line)]] | wt | 43.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 74.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.54× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 56.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 38.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +12.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.299× (z -11.9) ⚠ toxic |
| [[C32 (line)]] | wt | 56.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.347× (z -8.6) ⚠ toxic |
| [[HCT15 (line)]] | alt | 51.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 57.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +10.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.377× (z -9.8) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 38.0 | 0 | 2 (2 ⚠) | — | [[Torkinib (drug)]] 5 µM 0.0736× (z -10.1) ⚠ toxic |
| [[HS-578T (line)]] | alt | 84.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[KATO III (line)]] | alt | 39.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 41.0 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.328× (z -9.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 49.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[RPMI-7951 (line)]] | alt | 88.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0338× (z -29.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 90.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -12.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 42.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[COLO 205 (line)]] | alt | 36.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 47.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[NCI-H2030 (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -8.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0583× (z -28.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW1417 (line)]] | alt | 35.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +10.2) | — |
| [[SW48 (line)]] | wt | 39.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14231), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF563]] | +0.65 | +0.70 / +0.40 | both halves | 5e-05 |  |
| [[IFT46]] | +0.64 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[DCP1B]] | +0.63 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[ZNF25]] | +0.61 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[KCTD18]] | +0.61 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[SLC16A14]] | +0.60 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[RAD52]] | +0.60 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[DNAJC27]] | +0.60 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[DHRS4-AS1]] | +0.59 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[FAM216A]] | +0.59 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[UBA5]] | +0.58 | +0.48 / +0.65 | both halves | 2e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CCDC90B]] | +0.58 | +0.68 / +0.35 | both halves | 1e-04 |  |
| [[RWDD2B]] | +0.58 | +0.53 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KANK2]] | -0.62 | -0.62 / -0.29 | both halves | 2e-04 |  |
| [[GATAD2B]] | -0.56 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[SPATA13]] | -0.54 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[DIAPH1]] | -0.54 | -0.63 / -0.36 | both halves | 9e-05 |  |
| [[SPIRE2]] | -0.52 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[ACTN4]] | -0.52 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[KIAA0930]] | -0.52 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[PLXND1]] | -0.52 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[FOXK1]] | -0.51 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[LLGL2]] | -0.51 | -0.36 / -0.24 | both halves | 5e-04 |  |
| [[BCR]] | -0.51 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[MYRF]] | -0.51 | -0.50 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF675]] | B | ZNF675 activity raises ACAD11's level | lines that do not express ZNF675 (5) vs lines expressing it (45) | 1.57× lower at baseline in the lines without ZNF675 | 0.061 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF573, ZNF420 |
| [[ZNF391]] | B | ZNF391 activity raises ACAD11's level | lines that do not express ZNF391 (5) vs lines expressing it (45) | 2.00× lower at baseline in the lines without ZNF391 | 0.072 | ⚠ within organs, on part of the lines; also absent: LINC00159, ENSG00000283491, ASIC1; maybe low, not absent |
| [[SESTD1]] | C | SESTD1 activity lowers ACAD11's level | lines that do not express SESTD1 (4) vs lines expressing it (46) | 1.72× higher at baseline in the lines without SESTD1 | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |
| [[DCP1B]] | C | DCP1B activity raises ACAD11's level | lines that do not express DCP1B (3) vs lines expressing it (47) | 2.55× lower at baseline in the lines without DCP1B | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPRASP3, DISC1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.520). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.9, 19.5); signed map (7.7, -22.8). **Vector** length 90.5, 22.9% of its response variance represented; |z| ≥ 3 in 1,167 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +10.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +6.7 | +7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +4.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.5 | +3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | +1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.2 | +2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +1.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.6 | +1.5 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.4 | -14.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.2 | -4.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.9 | -5.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -4.6 | -4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.2 | -11.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -9.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.2 | -0.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.1 | -0.3 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA dehydrogenase family member 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1 — chr3:132,558,138-132,660,082 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12592 |
| Gene groups (HGNC) | Acyl-CoA dehydrogenase family; Flavoproteins |
| Reactome | 3 pathways, smallest: Mitochondrial Fatty Acid Beta-Oxidation; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q709F0](https://www.uniprot.org/uniprotkb/Q709F0) (Acyl-CoA dehydrogenase family member 11):

> Functions as an atypical peroxisomal acyl-CoA dehydrogenase (ACAD) that contributes to the catabolism of 4-hydroxy fatty acyl-CoAs by catalyzing their conversion into 4-hydroxy-trans-2-enoyl-CoA intermediates compatible with beta-oxidation. The underlying mechanism is proposed to involve sequential enzymatic steps including ATP-dependent phosphorylation of the 4-hydroxy group to form 4-phosphohydroxyacyl-CoA (such as 4-phosphodocosahexaenoyl-CoA), and subsequent conversion into …

**Summary**, from NCBI Gene [84129](https://www.ncbi.nlm.nih.gov/gene/84129):

> This gene encodes an acyl-CoA dehydrogenase enzyme with a preference for carbon chain lengths between 20 and 26. Naturally occurring read-through transcription occurs between the upstream gene NPHP3 (nephronophthisis 3 (adolescent)) and this gene. [provided by RefSeq, Aug 2015]

**Accessions** — [HGNC:30211](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30211) · Entrez [84129](https://www.ncbi.nlm.nih.gov/gene/84129) · UniProt [Q709F0](https://www.uniprot.org/uniprotkb/Q709F0) · Ensembl [ENSG00000240303](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240303)

## Data

Gene col 14231: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14231); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14231, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14231]; `tensor/DDL_lfc|DDL_z.npy` [14231]; `embed/gene_vectors.npy` [14231]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14231 or target_col == 14231). Every well: [[ACAD11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACAD11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
