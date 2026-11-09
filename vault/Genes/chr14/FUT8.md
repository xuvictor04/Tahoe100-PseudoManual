---
symbol: "FUT8"
type: "gene"
col: 413
ensembl_id: "ENSG00000033170"
name: "fucosyltransferase 8"
location: "14q23.3"
module: 34
arm: "+"
pooled_cpm: 184.96
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# FUT8

*fucosyltransferase 8* — 14q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.29× (z +8.7, q 3e-15, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.513× (z -14.9, q 0e+00, down in 34 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.712× (z -8.2, q 3e-14, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPIN4]] (+0.53, fdr 2e-05), [[ARHGAP10]] (+0.53, fdr 2e-05), [[EHF]] (+0.52, fdr 3e-05); moves opposite to [[ACOX3]] (-0.50, fdr 4e-05), [[TRMT44]] (-0.43, fdr 6e-05), [[CIAO3]] (-0.42, fdr 1e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ACSL5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 413.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +8.7 | 3e-15 | 28/47 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +6.8 | 2e-09 | 25/48 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.21×** | +6.6 | 7e-09 | 25/48 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +6.3 | 4e-08 | 23/47 (HEC-1-A, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +6.2 | 5e-08 | 24/47 (HEC-1-A, RPMI-7951, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.26×** | +5.3 | 1e-05 | 24/47 (A549, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.15× | +4.8 | 2e-04 | 16/47 (PANC-1, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +4.1 | 0.003 | 22/48 (HEC-1-A, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.026 | 18/46 (NCI-H1573, H4, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.16× | +3.5 | 0.026 | 16/47 (RPMI-7951, A549, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.14× | +3.1 | 0.11 | 23/47 (NCI-H460, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 413.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.513×** | -14.9 | 0e+00 | 34/44 (NCI-H23, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.584×** | -13.0 | 5e-36 | 37/48 (NCI-H23, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.576×** | -12.8 | 4e-35 | 33/43 (LoVo, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.702×** | -8.2 | 3e-14 | 29/46 (SW1417, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.712×** | -8.2 | 3e-14 | 29/47 (LS 180, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.745×** | -7.1 | 1e-10 | 33/47 (SW 900, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.721×** | -7.0 | 2e-10 | 28/47 (LS 180, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.810×** | -5.1 | 3e-05 | 24/47 (LS 180, NCI-H2347, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.846× | -4.0 | 0.003 | 22/47 (SNU-423, AN3 CA, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.734×** | -3.9 | 0.005 | 20/48 (LOX-IMVI, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.734×** | -3.9 | 0.005 | 18/37 (C32, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~1% of this change | 0.848× | -3.8 | 0.006 | 20/46 (SNU-1, NCI-H2030, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.898× | -3.7 | 0.011 | 6/48 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.809×** | -3.4 | 0.029 | 14/47 (LS 180, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.868× | -3.1 | 0.063 | 12/46 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.826×** | -3.1 | 0.081 | 15/46 (NCI-H1573, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 413. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 226 | 0 | 12 (1 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.339× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 784 | 3 (2 ⚠) | 8 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +14.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.79× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -13.9) ⚠ cell-cycle shift, explains ~14% of this change |
| [[LS 180 (line)]] | wt | 305 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.429× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 120 | 6 (5 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 5.94× (z +16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.42× (z +11.0) | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.372× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 699 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -18.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 270 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -22.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.541× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 379 | 0 | 7 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -16.3) ⚠ cell-cycle shift, explains ~14% of this change |
| [[SW1417 (line)]] | alt | 211 | 2 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -16.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 55.8 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +13.8) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.11× (z +11.4) | — |
| [[SW480 (line)]] | alt | 262 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -14.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 96.8 | 3 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.31× (z +16.1) | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -13.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 387 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0713× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.316× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 142 | 3 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.08× (z +14.0) | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -13.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 198 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.61× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.174× (z -21.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 367 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -15.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 206 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -21.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 65.6 | 3 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +19.2) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.63× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.502× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 268 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.422× (z -9.6) |
| [[A498 (line)]] | wt | 92.8 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.390× (z -10.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 204 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -10.2) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.432× (z -8.5) |
| [[C32 (line)]] | wt | 137 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -16.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 205 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.357× (z -11.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 121 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.19× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.385× (z -12.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 336 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -12.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 126 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.51× (z +9.4) ⚠ cell-cycle shift, explains ~23% of this change | [[Homoharringtonine (drug)]] 5 µM 0.648× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 78.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +13.2) ⚠ cell-cycle shift, explains ~14% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -14.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 118 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.317× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~1% of this change |
| [[SW48 (line)]] | wt | 103 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +8.5) ⚠ cell-cycle shift, explains ~14% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.322× (z -9.0) |
| [[A-172 (line)]] | wt | 50.6 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.67× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[COLO 205 (line)]] | alt | 274 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.466× (z -8.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 93.0 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.46× (z +9.4) | — |
| [[HepG2_C3A (line)]] | wt | 74.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -9.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.516× (z -8.7) ⚠ transcription drop |
| [[LOX-IMVI (line)]] | wt | 89.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.597× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 58.3 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +13.6) ⚠ cell-cycle shift, explains ~14% of this change | — |
| [[RPMI-7951 (line)]] | alt | 106 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.70× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 93.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +10.7) ⚠ cell-cycle shift, explains ~14% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -10.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 163 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 133 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.5 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 413), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPIN4]] | +0.53 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ARHGAP10]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 | same gene group |
| [[EHF]] | +0.52 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[DHRS9]] | +0.48 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[B3GALT1]] | +0.47 | +0.39 / +0.42 | both halves | 6e-05 |  |
| [[CRACD]] | +0.47 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[B4GALT6]] | +0.46 | +0.51 / +0.38 | both halves | 6e-05 | pathway: Asparagine N-linked glycosylation |
| [[FERMT1]] | +0.46 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[STK39]] | +0.45 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[CALM2]] | +0.45 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[KLF12]] | +0.45 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[NRG2]] | +0.45 | +0.43 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACOX3]] | -0.50 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[TRMT44]] | -0.43 | -0.41 / -0.38 | both halves | 6e-05 |  |
| [[CIAO3]] | -0.42 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[FBXL8]] | -0.42 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[HSF4]] | -0.41 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[BSCL2]] | -0.40 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[VPS51]] | -0.40 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[SNED1-AS1]] | -0.40 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[STK19]] | -0.40 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[LINC02432]] | -0.39 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[MTERF1]] | -0.38 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[SAMD4B]] | -0.38 | -0.31 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACSL5]] | B | ACSL5 activity raises FUT8's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 1.50× lower at baseline in the lines without ACSL5 | 0.016 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1 |
| [[TRBC2]] | B | TRBC2 activity raises FUT8's level | lines that do not express TRBC2 (39) vs lines expressing it (11) | 2.01× lower at baseline in the lines without TRBC2 | 0.067 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1 |
| [[TFF2]] | B | TFF2 activity raises FUT8's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 2.15× lower at baseline in the lines without TFF2 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers FUT8's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.369). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.1, 39.7); signed map (9.6, 37.0). **Vector** length 127, 37.0% of its response variance represented; |z| ≥ 3 in 1,608 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +6.6 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +6.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +6.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.7 | +6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +4.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | -0.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.2 | -14.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.1 | -12.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.0 | -7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.8 | -13.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.4 | -8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | -5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.7 | -0.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.2 | -0.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.2 | -1.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | fucosyltransferase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.3 — chr14:65,410,592-65,744,121 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Fucosyltransferases; MicroRNA protein coding host genes; SH3 domain containing |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 10 pathways, smallest: Reactions specific to the complex N-glycan synthesis pathway; N-glycan antennae elongation in the medial/trans-Golgi; Maturation of spike protein_9694548 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYC5](https://www.uniprot.org/uniprotkb/Q9BYC5) (Alpha-(1,6)-fucosyltransferase):

> Catalyzes the addition of fucose in alpha 1-6 linkage to the first GlcNAc residue, next to the peptide chains in N-glycans. Fucosylates the reducing GlcNAc residue in complex-type N-glycans attached on the fragment crystallizable (Fc) of IgGs. Fully converts Fc glycoforms containing one or two terminal GlcNAc moieties (G0-GlcNAc and G0).

**Summary**, from NCBI Gene [2530](https://www.ncbi.nlm.nih.gov/gene/2530):

> This gene encodes an enzyme belonging to the family of fucosyltransferases. The product of this gene catalyzes the transfer of fucose from GDP-fucose to N-linked type complex glycopeptides. This enzyme is distinct from other fucosyltransferases which catalyze alpha1-2, alpha1-3, and alpha1-4 fucose addition. The expression of this gene may contribute to the malignancy of cancer cells and to their invasive and metastatic capabilities. Alternative splicing results in multiple transcript variants. …

**Accessions** — [HGNC:4019](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4019) · Entrez [2530](https://www.ncbi.nlm.nih.gov/gene/2530) · UniProt [Q9BYC5](https://www.uniprot.org/uniprotkb/Q9BYC5) · Ensembl [ENSG00000033170](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000033170)

## Data

Gene col 413: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 413); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 413, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 413]; `tensor/DDL_lfc|DDL_z.npy` [413]; `embed/gene_vectors.npy` [413]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 413 or target_col == 413). Every well: [[FUT8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FUT8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
