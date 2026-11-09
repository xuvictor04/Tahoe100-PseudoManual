---
symbol: "ZYG11B"
type: "gene"
col: 8505
ensembl_id: "ENSG00000162378"
name: "zyg-11 family member B, cell cycle regulator"
location: "1p32.3"
module: 17
arm: "+"
pooled_cpm: 63.67
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 19
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ZYG11B

*zyg-11 family member B, cell cycle regulator* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.72× (z +14.1, q 3e-42, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.431× (z -21.7, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRA]] (+0.66, fdr 1e-05), [[ACTR10]] (+0.66, fdr 1e-05), [[DPY30]] (+0.65, fdr 3e-05); moves opposite to [[SRSF1]] (-0.59, fdr 6e-05), [[SLC9A5]] (-0.57, fdr 1e-04), [[HNRNPA2B1]] (-0.56, fdr 5e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8505.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +14.1 | 3e-42 | 43/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.65×** | +13.0 | 2e-36 | 43/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +11.8 | 1e-29 | 42/48 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.31×** | +6.9 | 6e-10 | 38/49 (PANC-1, HEC-1-A, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +5.4 | 6e-06 | 23/48 (PANC-1, A-427, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.45×** | +5.1 | 4e-05 | 23/49 (A498, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.19× | +4.7 | 2e-04 | 20/49 (SW480, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.16× | +4.7 | 2e-04 | 16/48 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.13× | +4.6 | 3e-04 | 14/48 (LS 180, A498, …) | rises with dose | low cells (technical?) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.39×** | +4.5 | 4e-04 | 21/48 (HEC-1-A, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.15× | +4.3 | 9e-04 | 14/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.16× | +4.0 | 0.003 | 15/48 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.17× | +3.9 | 0.005 | 11/48 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.11× | +3.8 | 0.006 | 6/48 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.15× | +3.6 | 0.010 | 11/47 (SW480, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.15× | +3.6 | 0.011 | 20/47 (A549, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.15× | +3.5 | 0.012 | 14/48 (SW480, C-33 A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8505.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.431×** | -21.7 | 0e+00 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.467×** | -19.6 | 0e+00 | 47/48 (SW48, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.541×** | -15.9 | 0e+00 | 42/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.553×** | -15.3 | 0e+00 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.576×** | -14.2 | 5e-44 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.696×** | -13.2 | 1e-37 | 33/48 (SNU-423, H4, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.396×** | -12.5 | 7e-34 | 37/49 (HOP62, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.642×** | -10.6 | 3e-24 | 35/45 (A-427, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.665×** | -10.1 | 3e-22 | 36/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.581×** | -7.3 | 1e-11 | 33/48 (HOP62, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.818×** | -7.3 | 1e-11 | 26/48 (HOP62, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.751×** | -7.1 | 6e-11 | 27/48 (H4, NCI-H460, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | 0.840× | -6.3 | 1e-08 | 23/48 (HOP62, HCT15, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.796×** | -5.9 | 2e-07 | 22/49 (Panc 03.27, LoVo, …) | all doses, flat | composition shift; position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.655×** | -5.7 | 5e-07 | 23/37 (HEC-1-A, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.825×** | -4.9 | 3e-05 | 22/48 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.830×** | -4.8 | 5e-05 | 22/48 (J82, PANC-1, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.888× | -3.1 | 0.052 | 12/48 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[SBI-0640756 (drug)]] 5 µM |  | **0.800×** | -3.0 | 0.059 | 13/48 (RPMI-7951, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.894× | -2.9 | 0.087 | 7/47 (NCI-H2347, A549, …) | top dose only |  |
| [[Procainamide (hydrochloride) (drug)]] 0.5 µM |  | 0.895× | -2.8 | 0.095 | 6/47 (HEC-1-A, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8505. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 55.0 | 0 | 11 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -23.6) |
| [[HOP62 (line)]] | alt | 80.8 | 0 | 10 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.250× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -17.2) |
| [[PANC-1 (line)]] | alt | 72.8 | 3 | 6 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +13.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -19.0) |
| [[SW480 (line)]] | alt | 65.3 | 3 | 6 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.88× (z +9.8) | [[Digitoxin (drug)]] 5 µM 0.327× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.351× (z -16.2) |
| [[H4 (line)]] | wt | 98.9 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -20.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.289× (z -11.6) |
| [[HS-578T (line)]] | alt | 86.5 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -17.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.388× (z -11.7) |
| [[J82 (line)]] | alt | 54.5 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -15.2) |
| [[A-172 (line)]] | wt | 79.7 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -14.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.595× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 63.2 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.09× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.500× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 47.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -15.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.286× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 93.3 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.05× (z +8.7) | [[Auranofin (drug)]] 5 µM 0.274× (z -15.7) |
| [[CFPAC-1 (line)]] | alt | 63.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -11.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.447× (z -9.1) |
| [[Hs 766T (line)]] | wt | 79.0 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -15.1) |
| [[hTERT-HPNE (line)]] | wt | 63.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.229× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.323× (z -10.2) |
| [[LoVo (line)]] | wt | 54.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -12.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LS 180 (line)]] | wt | 62.6 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.215× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.360× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 80.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.479× (z -8.8) |
| [[SNU-423 (line)]] | alt | 68.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -24.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.394× (z -11.3) |
| [[SW 900 (line)]] | alt | 47.8 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.223× (z -13.7) |
| [[A-427 (line)]] | wt | 78.9 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.01× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -23.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 57.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.78× (z +12.8) | — |
| [[AsPC-1 (line)]] | alt | 30.2 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.96× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -14.3) |
| [[KATO III (line)]] | alt | 55.0 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.321× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 59.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.332× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.463× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 81.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.426× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 63.6 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.393× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 56.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -11.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.154× (z -8.8) |
| [[SNU-1 (line)]] | wt | 58.5 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.209× (z -12.0) |
| [[COLO 205 (line)]] | alt | 50.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 45.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.217× (z -15.5) |
| [[SW48 (line)]] | wt | 61.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0452× (z -22.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.255× (z -9.9) |
| [[A549 (line)]] | wt | 58.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -10.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[AN3 CA (line)]] | alt | 103 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.240× (z -8.5) |
| [[C-33 A (line)]] | alt | 100 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.398× (z -9.9) |
| [[C32 (line)]] | wt | 59.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.318× (z -11.6) |
| [[HCT15 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -9.1) ⚠ cell-cycle shift, explains <1% of this change |
| [[HepG2_C3A (line)]] | wt | 40.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.286× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 59.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.401× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 57.5 | 1 | 0 | [[Salicylic acid (drug)]] 0.5 µM 2.18× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 59.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.436× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 51.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -9.5) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 101 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0719× (z -11.4) |
| [[SW 1271 (line)]] | alt | 61.7 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0765× (z -9.2) |
| [[BT-474 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 61.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 52.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8505), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRA]] | +0.66 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ACTR10]] | +0.66 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[DPY30]] | +0.65 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[ARMC1]] | +0.65 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[GPATCH11]] | +0.64 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[ZNHIT3]] | +0.64 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ISCA2]] | +0.64 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[MTIF3]] | +0.64 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[RAD17]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[COMMD2]] | +0.63 | +0.55 / +0.46 | both halves | 2e-05 |  |
| [[ASB8]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[HEATR5B]] | +0.63 | +0.50 / +0.46 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF1]] | -0.59 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[SLC9A5]] | -0.57 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[HNRNPA2B1]] | -0.56 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[ADAMTS3]] | -0.56 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[THOC6]] | -0.55 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[HCFC1]] | -0.55 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[NIPBL-DT]] | -0.54 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[SECISBP2]] | -0.54 | -0.21 / -0.52 | both halves | 6e-04 |  |
| [[STARD4-AS1]] | -0.54 | -0.32 / -0.38 | both halves | 1e-04 |  |
| [[PARD6G-AS1]] | -0.53 | -0.24 / -0.44 | both halves | 5e-04 |  |
| [[DDX39A]] | -0.53 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[HCG20]] | -0.53 | -0.38 / -0.47 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ZYG11B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.8, -2.8); signed map (-21.1, -13.4). **Vector** length 96.5, 26.2% of its response variance represented; |z| ≥ 3 in 1,275 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.7 | +14.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.3 | +11.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.1 | +13.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.0 | +6.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.5 | +3.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.3 | +2.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.7 | -15.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | -9.3 | -6.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.2 | -10.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | -6.8 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.6 | -7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -1.0 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -2.3 | -0.7 |
|  | [[Arbutin (drug)]] 0.05 µM |  | -2.0 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | zyg-11 family member B, cell cycle regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:52,726,453-52,827,336 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13456; previously ZYG11 |
| Gene groups (HGNC) | ZYG11 cell cycle regulator family; Armadillo like helical domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0D3](https://www.uniprot.org/uniprotkb/Q9C0D3) (Protein zyg-11 homolog B):

> Serves as substrate adapter subunit in the E3 ubiquitin ligase complex ZYG11B-CUL2-Elongin BC. Acts to target substrates bearing N-terminal degrons for proteasomal degradation with the first four residues of substrates being the key recognition elements. Prefers Nt-Gly but also has the capacity to recognize Nt-Ser, -Ala and -Cys. Involved in the clearance of proteolytic fragments generated by caspase cleavage during apoptosis since N-terminal glycine degrons are strongly enriched at caspase …

**Summary**, from NCBI Gene [79699](https://www.ncbi.nlm.nih.gov/gene/79699):

> Involved in positive regulation of proteasomal ubiquitin-dependent protein catabolic process and protein quality control for misfolded or incompletely synthesized proteins. Part of Cul2-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25820](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25820) · Entrez [79699](https://www.ncbi.nlm.nih.gov/gene/79699) · UniProt [Q9C0D3](https://www.uniprot.org/uniprotkb/Q9C0D3) · Ensembl [ENSG00000162378](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162378)

## Data

Gene col 8505: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8505); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8505, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8505]; `tensor/DDL_lfc|DDL_z.npy` [8505]; `embed/gene_vectors.npy` [8505]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8505 or target_col == 8505). Every well: [[ZYG11B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZYG11B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
