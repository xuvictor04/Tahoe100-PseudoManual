---
symbol: "PHKB"
type: "gene"
col: 2284
ensembl_id: "ENSG00000102893"
name: "phosphorylase kinase regulatory subunit beta"
location: "16q12.1"
module: 57
arm: "+"
pooled_cpm: 125.08
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 19
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# PHKB

*phosphorylase kinase regulatory subunit beta* — 16q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.76× (z +9.7, q 2e-19, up in 43 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.69× (z +9.5, q 5e-19, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (15 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.406× (z -16.3, q 0e+00, down in 44 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.546× (z -15.4, q 0e+00, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSD17B4]] (+0.71, fdr 7e-06), [[NDRG3]] (+0.68, fdr 7e-06), [[USP14]] (+0.68, fdr 7e-06); moves opposite to [[ERF]] (-0.64, fdr 8e-06), [[EP300]] (-0.61, fdr 1e-04), [[KDM6B]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2284.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.76×** | +9.7 | 2e-19 | 43/48 (COLO 205, C32, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.69×** | +9.5 | 5e-19 | 41/48 (C32, NCI-H1573, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +7.9 | 5e-13 | 35/48 (NCI-H1573, C32, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.29×** | +4.3 | 0.003 | 30/48 (AsPC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.28×** | +3.9 | 0.009 | 25/50 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.095 | 23/49 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.10 | 12/48 (AsPC-1, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 17 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2284.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.406×** | -16.3 | 0e+00 | 44/48 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.546×** | -15.4 | 0e+00 | 46/49 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.536×** | -11.2 | 6e-27 | 41/48 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.563×** | -9.9 | 4e-21 | 35/48 (A498, J82, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.590×** | -9.5 | 3e-19 | 40/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.701×** | -9.0 | 2e-17 | 29/48 (A498, J82, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.619×** | -8.6 | 5e-16 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.642×** | -8.0 | 1e-13 | 33/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.638×** | -7.8 | 4e-13 | 37/47 (RKO, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.684×** | -6.3 | 1e-08 | 27/45 (SW1417, LS 180, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.794×** | -5.9 | 2e-07 | 30/48 (MIA PaCa-2, Hs 766T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.729×** | -5.7 | 6e-07 | 28/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | **0.740×** | -5.4 | 3e-06 | 32/48 (NCI-H661, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.753×** | -5.1 | 1e-05 | 29/48 (RPMI-7951, A498, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.750×** | -5.0 | 2e-05 | 32/50 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.684×** | -3.4 | 0.017 | 20/48 (RKO, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.876× | -3.3 | 0.023 | 8/49 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.840× | -3.1 | 0.046 | 20/48 (NCI-H23, SW 900, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.849× | -2.9 | 0.080 | 19/48 (NCI-H460, A498, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2284. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 136 | 1 | 10 (8 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.90× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.287× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -12.7) |
| [[SW480 (line)]] | alt | 122 | 1 | 8 (6 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.95× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.192× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -14.8) |
| [[HS-578T (line)]] | alt | 101 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -14.9) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.547× (z -9.9) |
| [[HOP62 (line)]] | alt | 99.2 | 2 | 5 (5 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.49× (z +11.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.280× (z -12.0) ⚠ cell-cycle shift, explains ~38% of this change |
| [[LoVo (line)]] | wt | 128 | 1 | 6 (4 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.94× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -15.8) |
| [[SW1417 (line)]] | alt | 154 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.292× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -11.4) |
| [[A498 (line)]] | wt | 214 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -23.5) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -11.1) |
| [[J82 (line)]] | alt | 104 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -17.6) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -12.6) |
| [[NCI-H2347 (line)]] | alt | 84.0 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.429× (z -10.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 115 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -14.4) |
| [[SK-MEL-2 (line)]] | alt | 70.5 | 0 | 6 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.300× (z -12.1) |
| [[C32 (line)]] | wt | 70.2 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.54× (z +13.5) | [[Harringtonine (drug)]] 0.5 µM 0.323× (z -10.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[COLO 205 (line)]] | alt | 124 | 3 (1 ⚠) | 2 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.29× (z +11.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.65× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -8.6) |
| [[SNU-423 (line)]] | alt | 91.3 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -14.6) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.516× (z -10.0) |
| [[SW 900 (line)]] | alt | 128 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -14.0) |
| [[A-172 (line)]] | wt | 125 | 1 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.97× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -12.8) ⚠ cell-cycle shift, explains ~78% of this change |
| [[A549 (line)]] | wt | 163 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -16.1) |
| [[AsPC-1 (line)]] | alt | 77.1 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -12.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -10.7) |
| [[BT-474 (line)]] | alt | 136 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.319× (z -12.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 188 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.98× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -13.4) |
| [[Hs 766T (line)]] | wt | 184 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 150 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.230× (z -15.4) |
| [[RKO (line)]] | wt | 107 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.160× (z -18.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 129 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -14.0) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -11.1) |
| [[SW48 (line)]] | wt | 137 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -17.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 80.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.21× (z +12.8) ⚠ cell-cycle shift, explains ~38% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 107 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.327× (z -9.3) |
| [[HT-29 (line)]] | alt | 131 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.377× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -9.6) |
| [[KATO III (line)]] | alt | 205 | 1 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.15× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -15.4) |
| [[LOX-IMVI (line)]] | wt | 78.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.344× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 137 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.62× (z +13.0) | — |
| [[NCI-H23 (line)]] | alt | 69.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +15.6) ⚠ cell-cycle shift, explains ~78% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -11.9) |
| [[SNU-1 (line)]] | wt | 104 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.242× (z -11.4) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 112 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -14.4) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 189 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.331× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -10.8) |
| [[LS 180 (line)]] | wt | 192 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -15.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 204 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -11.2) |
| [[PANC-1 (line)]] | alt | 78.7 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 1.97× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 78.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.9) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[NCI-H1792 (line)]] | alt | 77.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -12.7) |
| [[NCI-H661 (line)]] | alt | 87.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.180× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~64% of this change |
| [[SHP-77 (line)]] | alt | 88.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.347× (z -10.8) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 130 | 0 | 1 | — | [[Decitabine (drug)]] 5 µM 0.0909× (z -9.6) |
| [[AN3 CA (line)]] | alt | 120 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 71.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 96.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2284), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSD17B4]] | +0.71 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[NDRG3]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[USP14]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[GNPDA2]] | +0.66 | +0.75 / +0.56 | both halves | 1e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[HTT]] | +0.65 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[BLMH]] | +0.64 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[NXPE3]] | +0.64 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[TALDO1]] | +0.64 | +0.62 / +0.54 | both halves | 1e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[RTCA]] | +0.63 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[ATP5F1C]] | +0.63 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[OPA1]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[VPS50]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERF]] | -0.64 | -0.58 / -0.62 | both halves | 8e-06 |  |
| [[EP300]] | -0.61 | -0.65 / -0.34 | both halves | 1e-04 |  |
| [[KDM6B]] | -0.58 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[IBA57]] | -0.57 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[KBTBD2]] | -0.54 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[LINC01128]] | -0.54 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[FAM43A]] | -0.53 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[HIVEP1]] | -0.53 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[KDSR]] | -0.53 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[DPH1-AS1]] | -0.52 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[PNRC2]] | -0.52 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[OSMR-DT]] | -0.52 | -0.36 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PHKB's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers PHKB's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.652). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.2, -7.7); signed map (-28.2, -21.7). **Vector** length 124, 43.0% of its response variance represented; |z| ≥ 3 in 1,249 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.9 | +9.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | +10.8 | +9.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +10.4 | +7.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.6 | +1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.4 | +4.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.6 | -15.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.9 | -16.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.7 | -7.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -6.3 | -8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.1 | -5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.6 | -2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | phosphorylase kinase regulatory subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.1 — chr16:47,461,123-47,701,523 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phosphorylase kinase subunits |
| Reactome | 3 pathways, smallest: Glycogen breakdown (glycogenolysis); Glycogen metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93100](https://www.uniprot.org/uniprotkb/Q93100) (Phosphorylase b kinase regulatory subunit beta):

> Phosphorylase b kinase catalyzes the phosphorylation of serine in certain substrates, including troponin I. The beta chain acts as a regulatory unit and modulates the activity of the holoenzyme in response to phosphorylation.

**Summary**, from NCBI Gene [5257](https://www.ncbi.nlm.nih.gov/gene/5257):

> Phosphorylase kinase is a polymer of 16 subunits, four each of alpha, beta, gamma and delta. The alpha subunit includes the skeletal muscle and hepatic isoforms, encoded by two different genes. The beta subunit is the same in both the muscle and hepatic isoforms, encoded by this gene, which is a member of the phosphorylase b kinase regulatory subunit family. The gamma subunit also includes the skeletal muscle and hepatic isoforms, encoded by two different genes. The delta subunit is a …

**Accessions** — [HGNC:8927](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8927) · Entrez [5257](https://www.ncbi.nlm.nih.gov/gene/5257) · UniProt [Q93100](https://www.uniprot.org/uniprotkb/Q93100) · Ensembl [ENSG00000102893](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102893)

## Data

Gene col 2284: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2284); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2284, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2284]; `tensor/DDL_lfc|DDL_z.npy` [2284]; `embed/gene_vectors.npy` [2284]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2284 or target_col == 2284). Every well: [[PHKB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHKB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
