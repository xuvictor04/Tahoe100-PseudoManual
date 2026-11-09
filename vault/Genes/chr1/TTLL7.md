---
symbol: "TTLL7"
type: "gene"
col: 6094
ensembl_id: "ENSG00000137941"
name: "tubulin tyrosine ligase like 7"
location: "1p31.1"
module: 30
arm: "+"
pooled_cpm: 41.72
n_lines_expressing: 40
n_dd_up: 31
n_dd_down: 24
n_dd_up_clean: 29
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 15
direction_downstream: 12
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# TTLL7

*tubulin tyrosine ligase like 7* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.07× (z +20.0, q 0e+00, up in 36 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.361× (z -19.9, q 0e+00, down in 32 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NXPE3]] (+0.63, fdr 1e-05), [[SH3PXD2B]] (+0.62, fdr 1e-05), [[CAMK2G]] (+0.61, fdr 3e-05); moves opposite to [[GNG12-AS1]] (-0.56, fdr 3e-05), [[ITPRIPL2]] (-0.55, fdr 3e-05), [[EP300]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[SOGA3]] → it (grade B ⚠); 12 go from it, the strongest it → [[SGTB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 2 with an alert ⚠; shown: the 15 strongest. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6094.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.07×** | +20.0 | 0e+00 | 36/38 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.48×** | +17.7 | 0e+00 | 38/38 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.41×** | +17.2 | 0e+00 | 28/38 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.28×** | +16.1 | 0e+00 | 29/38 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.26×** | +15.9 | 0e+00 | 28/38 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.12×** | +14.6 | 0e+00 | 28/38 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.91×** | +12.6 | 2e-34 | 30/38 (C32, hTERT-HPNE, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.90×** | +12.5 | 7e-34 | 29/38 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.86×** | +11.4 | 2e-28 | 30/38 (C32, A498, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.59×** | +9.7 | 2e-20 | 28/38 (PANC-1, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.41×** | +7.2 | 4e-11 | 23/38 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +6.8 | 6e-10 | 19/38 (SW480, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +6.6 | 1e-09 | 22/38 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +6.6 | 2e-09 | 22/37 (SW480, A-172, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.41×** | +6.4 | 6e-09 | 21/37 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6094.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.361×** | -19.9 | 0e+00 | 32/38 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.388×** | -18.5 | 0e+00 | 30/38 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.525×** | -17.8 | 0e+00 | 27/38 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.463×** | -15.1 | 0e+00 | 33/38 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.478×** | -14.4 | 4e-45 | 31/38 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.652×** | -11.8 | 3e-30 | 27/37 (NCI-H1792, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.564×** | -10.8 | 3e-25 | 28/37 (J82, HOP62, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.600×** | -10.0 | 1e-21 | 28/38 (HS-578T, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.635×** | -8.9 | 4e-17 | 25/38 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.438×** | -8.4 | 2e-15 | 30/39 (HS-578T, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.652×** | -8.0 | 5e-14 | 21/38 (NCI-H1792, AN3 CA, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.665×** | -8.0 | 8e-14 | 20/38 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.682×** | -7.2 | 3e-11 | 21/35 (NCI-H460, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.699×** | -7.0 | 9e-11 | 24/38 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **0.706×** | -6.8 | 4e-10 | 22/37 (HS-578T, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.714×** | -6.4 | 7e-09 | 22/38 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.546×** | -6.2 | 2e-08 | 21/38 (Panc 03.27, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -5.7 | 5e-07 | 22/38 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.820×** | -5.5 | 1e-06 | 16/38 (A-172, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.834× | -5.1 | 1e-05 | 19/38 (A-427, NCI-H1792, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.769×** | -4.8 | 5e-05 | 19/37 (A-172, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.862× | -4.1 | 9e-04 | 9/38 (PANC-1, SW 900, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.830×** | -3.7 | 0.006 | 20/38 (SNU-423, SW 1271, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6094. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.2 | 7 | 9 (7 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.65× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -16.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -10.5) |
| [[PANC-1 (line)]] | alt | 56.7 | 6 | 9 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.07× (z +17.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -14.9) |
| [[HS-578T (line)]] | alt | 130 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -22.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.207× (z -16.0) |
| [[NCI-H1792 (line)]] | alt | 133 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -29.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -27.5) |
| [[HOP62 (line)]] | alt | 33.5 | 2 | 9 (6 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.91× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -20.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.248× (z -12.7) |
| [[NCI-H2030 (line)]] | alt | 55.6 | 5 | 5 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.28× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -15.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.322× (z -10.9) |
| [[A-172 (line)]] | wt | 76.1 | 0 | 9 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.273× (z -15.0) |
| [[J82 (line)]] | alt | 101 | 0 | 9 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.317× (z -13.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.364× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 26.1 | 6 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.11× (z +10.5) | [[Homoharringtonine (drug)]] 0.05 µM 0.217× (z -10.1) |
| [[C32 (line)]] | wt | 53.3 | 4 | 4 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 5.03× (z +14.5) | [[Harringtonine (drug)]] 0.5 µM 0.277× (z -11.6) |
| [[LS 180 (line)]] | wt | 11.9 | 8 | 0 | [[Tucidinostat (drug)]] 5 µM 7.44× (z +14.4) | — |
| [[Panc 03.27 (line)]] | alt | 16.6 | 8 | 0 | [[Tucidinostat (drug)]] 5 µM 4.03× (z +11.4) | — |
| [[A498 (line)]] | wt | 51.3 | 7 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.94× (z +11.7) | — |
| [[SNU-423 (line)]] | alt | 71.3 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -20.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.235× (z -13.8) |
| [[NCI-H2347 (line)]] | alt | 11.6 | 6 | 0 | [[Tucidinostat (drug)]] 5 µM 6.20× (z +16.7) | — |
| [[CFPAC-1 (line)]] | alt | 26.7 | 2 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.52× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -10.0) |
| [[LoVo (line)]] | wt | 19.4 | 3 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.66× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.177× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.310× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 69.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -19.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.322× (z -9.9) |
| [[SW 900 (line)]] | alt | 45.0 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.87× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.299× (z -10.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 40.0 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.67× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -13.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HT-29 (line)]] | alt | 15.6 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 4.83× (z +11.8) | — |
| [[AN3 CA (line)]] | alt | 104 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0739× (z -16.3) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.252× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 52.2 | 2 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.73× (z +11.6) | [[Digitoxin (drug)]] 5 µM 0.230× (z -11.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 72.9 | 3 | 0 | [[Binimetinib (drug)]] 0.05 µM 2.05× (z +10.1) | — |
| [[A-427 (line)]] | wt | 56.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.400× (z -12.2) |
| [[A549 (line)]] | wt | 18.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -11.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -10.4) |
| [[NCI-H23 (line)]] | alt | 41.8 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.23× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 53.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -16.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.358× (z -9.2) |
| [[BT-474 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.179× (z -8.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 52.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.256× (z -8.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 17.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.57× (z +9.1) | — |
| [[SW48 (line)]] | wt | 11.9 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 0.05 µM 0.0815× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 3.93 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.77 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.95 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.87 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6094), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NXPE3]] | +0.63 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[SH3PXD2B]] | +0.62 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[CAMK2G]] | +0.61 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[MBOAT2]] | +0.60 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[KIF1B]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[TMOD1]] | +0.59 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[CLTCL1]] | +0.59 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[SNTA1]] | +0.58 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[MGST3]] | +0.58 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[ASAP3]] | +0.57 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[REEP1]] | +0.57 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[HACE1]] | +0.57 | +0.44 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNG12-AS1]] | -0.56 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ITPRIPL2]] | -0.55 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[EP300]] | -0.55 | -0.40 / -0.45 | both halves | 4e-05 |  |
| [[TNRC18]] | -0.54 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[GABPB1-AS1]] | -0.53 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[LINC01145-1]] | -0.52 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[IGF2BP1]] | -0.51 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[DPY19L3-DT]] | -0.51 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[HSPBAP1]] | -0.51 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[TRIM8]] | -0.50 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[TTC32]] | -0.50 | -0.37 / -0.29 | both halves | 2e-04 |  |
| [[RXYLT1]] | -0.50 | -0.39 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 12, C 3. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOGA3]] | B | SOGA3 activity raises TTLL7's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 3.83× lower at baseline in the lines without SOGA3 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1 |
| [[SYT11]] | B | SYT11 activity raises TTLL7's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 3.41× lower at baseline in the lines without SYT11 | 0.008 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1 |
| [[PRKD1]] | B | PRKD1 activity raises TTLL7's level | lines that do not express PRKD1 (13) vs lines expressing it (37) | 3.90× lower at baseline in the lines without PRKD1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SPART, KCTD16, DMD |
| [[OSBPL6]] | B | OSBPL6 activity raises TTLL7's level | lines that do not express OSBPL6 (12) vs lines expressing it (38) | 4.52× lower at baseline in the lines without OSBPL6 | 0.013 | ⚠ within organs, on part of the lines; also absent: RECK, LHFPL6, GLIPR2; maybe low, not absent |
| [[GXYLT2]] | B | GXYLT2 activity raises TTLL7's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 3.84× lower at baseline in the lines without GXYLT2 | 0.014 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[MPP2]] | B | MPP2 activity raises TTLL7's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 3.84× lower at baseline in the lines without MPP2 | 0.025 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[MAP1A]] | B | MAP1A activity raises TTLL7's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 3.69× lower at baseline in the lines without MAP1A | 0.036 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent |
| [[FAM229B]] | B | FAM229B activity raises TTLL7's level | lines that do not express FAM229B (5) vs lines expressing it (45) | 4.33× lower at baseline in the lines without FAM229B | 0.056 | ⚠ within organs, on part of the lines; also absent: PYGL, MPP2, CNN3-DT |
| [[LINC01145-1]] | B | LINC01145-1 activity raises TTLL7's level | lines that do not express LINC01145-1 (6) vs lines expressing it (44) | 3.87× lower at baseline in the lines without LINC01145-1 | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC00623, ENSG00000290569, DLX2; its own permutation p |
| [[PKIG]] | B | PKIG activity raises TTLL7's level | lines that do not express PKIG (6) vs lines expressing it (44) | 4.47× lower at baseline in the lines without PKIG | 0.063 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers TTLL7's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DPYSL3]] | B | DPYSL3 activity raises TTLL7's level | lines that do not express DPYSL3 (20) vs lines expressing it (30) | 3.11× lower at baseline in the lines without DPYSL3 | 0.098 | ⚠ within organs, on part of the lines; also absent: SNAP25, SNAI2, ADAM7-AS1 |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 9, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SGTB]] | B | TTLL7 activity raises SGTB's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 1.73× lower at baseline in the lines without TTLL7 | 0.029 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725 |
| [[ARL6]] | B | TTLL7 activity raises ARL6's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 2.09× lower at baseline in the lines without TTLL7 | 0.031 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725 |
| [[MPP2]] | B | TTLL7 activity raises MPP2's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 2.01× lower at baseline in the lines without TTLL7 | 0.042 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725 |
| [[SOGA3]] | B | TTLL7 activity raises SOGA3's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 4.77× lower at baseline in the lines without TTLL7 | 0.047 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725 |
| [[P4HA2]] | B | TTLL7 activity raises P4HA2's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 2.35× lower at baseline in the lines without TTLL7 | 0.048 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725 |
| [[NXPE3]] | B | TTLL7 activity raises NXPE3's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 2.32× lower at baseline in the lines without TTLL7 | 0.051 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725 |
| [[KREMEN1]] | B | TTLL7 activity weakens KREMEN1's drug response | lines that do not express TTLL7 (9) vs lines expressing it (37) | the lines without TTLL7 respond 1.41× as strongly (z diff -1.51); strongest at Homoharringtonine 0.5 µM: 0.20x vs 0.40x (z diff -4.0) | 0.063 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725; target measured in part of the lines; artifact flags |
| [[SH3PXD2B]] | B | TTLL7 activity raises SH3PXD2B's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 2.28× lower at baseline in the lines without TTLL7 | 0.089 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725 |
| [[HACE1]] | B | TTLL7 activity raises HACE1's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 1.81× lower at baseline in the lines without TTLL7 | 0.093 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725 |
| [[JAZF1]] | C | TTLL7 activity raises JAZF1's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 3.03× lower at baseline in the lines without TTLL7 | 0.014 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725; co-absent with the target |
| [[TUBA1A]] | C | TTLL7 activity raises TUBA1A's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 4.52× lower at baseline in the lines without TTLL7 | 0.043 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725; co-absent with the target |
| [[MAP1B]] | C | TTLL7 activity raises MAP1B's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 6.12× lower at baseline in the lines without TTLL7 | 0.069 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725; co-absent with the target |

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.495). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (2.1, 6.9); signed map (-19.0, 29.6). **Vector** length 120, 35.2% of its response variance represented; |z| ≥ 3 in 1,434 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.9 | +12.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.2 | +12.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +9.6 | +20.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.4 | +17.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.4 | +11.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.0 | +9.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.7 | +4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.9 | +6.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -5.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.1 | -5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -11.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.6 | -6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -10.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -4.8 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -2.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | tubulin tyrosine ligase like 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:83,865,024-83,999,150 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23033 |
| Gene groups (HGNC) | Tubulin tyrosine ligase family |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZT98](https://www.uniprot.org/uniprotkb/Q6ZT98) (Tubulin polyglutamylase TTLL7):

> Polyglutamylase which modifies tubulin, generating polyglutamate side chains of variable lengths on the gamma-carboxyl group of specific glutamate residues within the C-terminal tail of tubulin. Mediates both ATP-dependent initiation and elongation steps of the polyglutamylation reaction. Preferentially modifies the beta-tubulin tail over an alpha-tail. Competes with monoglycylase TTLL3 for modification site on beta-tubulin substrate, thereby creating an anticorrelation between glycylation and …

**Summary**, from NCBI Gene [79739](https://www.ncbi.nlm.nih.gov/gene/79739):

> Enables alpha-tubulin binding activity; beta-tubulin binding activity; and tubulin-glutamic acid ligase activity. Involved in protein polyglutamylation. Predicted to be located in 9+0 non-motile cilium. Predicted to be active in ciliary basal body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26242](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26242) · Entrez [79739](https://www.ncbi.nlm.nih.gov/gene/79739) · UniProt [Q6ZT98](https://www.uniprot.org/uniprotkb/Q6ZT98) · Ensembl [ENSG00000137941](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137941)

## Data

Gene col 6094: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6094); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6094, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6094]; `tensor/DDL_lfc|DDL_z.npy` [6094]; `embed/gene_vectors.npy` [6094]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6094 or target_col == 6094). Every well: [[TTLL7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTLL7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
