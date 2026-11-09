---
symbol: "PIBF1"
type: "gene"
col: 1373
ensembl_id: "ENSG00000083535"
name: "progesterone immunomodulatory binding factor 1"
location: "13q21.33-q22.1"
module: 135
arm: "-"
pooled_cpm: 228.09
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# PIBF1

*progesterone immunomodulatory binding factor 1* — 13q21.33-q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.94× (z +16.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.465× (z -18.4, q 0e+00, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.683× (z -13.1, q 1e-36, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZCCHC7]] (+0.69, fdr 7e-06), [[ANAPC11]] (+0.68, fdr 3e-05), [[SNRPD2]] (+0.67, fdr 1e-05); moves opposite to [[PRDM11]] (-0.68, fdr 1e-05), [[FAIM]] (-0.67, fdr 3e-05), [[SLC25A21]] (-0.65, fdr 3e-05).
> It sits in the **-** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1373.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.94×** | +16.0 | 0e+00 | 48/48 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +14.7 | 0e+00 | 47/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.77×** | +13.7 | 1e-40 | 48/48 (Panc 03.27, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +7.8 | 1e-12 | 38/48 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.76×** | +7.1 | 1e-10 | 37/49 (LoVo, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.58×** | +5.8 | 7e-07 | 27/48 (LS 180, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.21×** | +4.5 | 5e-04 | 25/48 (NCI-H1573, A498, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.20× | +4.4 | 9e-04 | 24/48 (J82, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.19× | +4.2 | 0.002 | 24/48 (NCI-H1573, NCI-H2030, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.13× | +4.1 | 0.002 | 13/48 (Panc 03.27, SW1417, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.16× | +3.5 | 0.023 | 17/48 (PANC-1, NCI-H1573, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.035 | 19/49 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.14× | +3.1 | 0.076 | 12/47 (SNU-1, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1373.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.465×** | -18.4 | 0e+00 | 46/49 (COLO 205, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.467×** | -17.7 | 0e+00 | 43/44 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -13.1 | 1e-36 | 38/49 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.612×** | -11.0 | 6e-26 | 37/45 (J82, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.698×** | -8.7 | 4e-16 | 36/48 (HT-29, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.691×** | -8.6 | 7e-16 | 33/48 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.746×** | -6.8 | 8e-10 | 35/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.769×** | -6.3 | 2e-08 | 32/48 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.785×** | -5.8 | 3e-07 | 31/48 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.810×** | -5.1 | 2e-05 | 27/48 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.809×** | -4.9 | 4e-05 | 26/47 (C32, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.814×** | -4.8 | 8e-05 | 25/48 (NCI-H1792, J82, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.870× | -4.8 | 8e-05 | 16/48 (A498, NCI-H1573, …) | top dose only | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.823×** | -4.7 | 1e-04 | 26/48 (A498, A-172, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | **0.827×** | -4.6 | 2e-04 | 25/48 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.696×** | -4.6 | 2e-04 | 34/48 (AsPC-1, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.821×** | -4.4 | 3e-04 | 25/47 (H4, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.883× | -4.3 | 6e-04 | 15/48 (HEC-1-A, A498, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.841× | -4.2 | 8e-04 | 22/48 (CFPAC-1, HEC-1-A, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.851× | -3.8 | 0.005 | 21/47 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 0.856× | -3.6 | 0.009 | 16/48 (H4, A498, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.874× | -3.3 | 0.025 | 15/48 (HepG2/C3A, C32, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.780×** | -3.1 | 0.038 | 19/48 (AsPC-1, A-172, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.842× | -3.0 | 0.066 | 15/47 (MIA PaCa-2, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1373. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 269 | 3 | 9 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 1.83× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -18.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.373× (z -17.3) |
| [[SW1417 (line)]] | alt | 168 | 4 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.10× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.425× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.573× (z -8.6) |
| [[HT-29 (line)]] | alt | 274 | 4 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.35× (z +14.4) | [[Dinaciclib (drug)]] 0.05 µM 0.361× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.409× (z -15.1) |
| [[KATO III (line)]] | alt | 301 | 3 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.42× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -12.1) |
| [[Panc 03.27 (line)]] | alt | 239 | 4 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.43× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -24.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.579× (z -9.0) |
| [[SW480 (line)]] | alt | 465 | 3 | 6 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.94× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -13.6) |
| [[J82 (line)]] | alt | 297 | 3 | 5 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.35× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -14.8) |
| [[LoVo (line)]] | wt | 269 | 4 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.18× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.447× (z -14.9) |
| [[LS 180 (line)]] | wt | 226 | 4 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.22× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.360× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -13.7) |
| [[NCI-H1573 (line)]] | alt | 264 | 6 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.439× (z -12.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 157 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.22× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.413× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.458× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 199 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.17× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -13.3) |
| [[A549 (line)]] | wt | 197 | 2 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.03× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -15.6) |
| [[COLO 205 (line)]] | alt | 478 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.22× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -23.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 348 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.63× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 106 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.21× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 183 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.51× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.415× (z -13.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 269 | 2 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 1.83× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -22.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.542× (z -8.9) |
| [[A-427 (line)]] | wt | 150 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.35× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.520× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.560× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 266 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.85× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -18.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 107 | 3 | 2 | [[Panobinostat (drug)]] 0.5 µM 2.60× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -12.0) |
| [[C32 (line)]] | wt | 189 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.93× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.509× (z -9.3) |
| [[HOP62 (line)]] | alt | 229 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.475× (z -12.1) |
| [[HS-578T (line)]] | alt | 173 | 1 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.91× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.359× (z -12.9) |
| [[hTERT-HPNE (line)]] | wt | 250 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.387× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 152 | 4 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.88× (z +14.3) | [[Auranofin (drug)]] 5 µM 0.478× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 156 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.82× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.451× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.545× (z -8.8) |
| [[H4 (line)]] | wt | 252 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.390× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -8.7) |
| [[HCT15 (line)]] | alt | 267 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.399× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.504× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 282 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.461× (z -10.7) |
| [[SNU-423 (line)]] | alt | 148 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.12× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.441× (z -10.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 187 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.89× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -10.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 122 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.15× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 325 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 287 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -12.5) |
| [[HepG2_C3A (line)]] | wt | 157 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.19× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 145 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 164 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.409× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 226 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.90× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.507× (z -9.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 205 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -13.5) |
| [[SNU-1 (line)]] | wt | 206 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -11.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 227 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -12.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 214 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.262× (z -11.9) |
| [[SHP-77 (line)]] | alt | 186 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -15.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 157 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -9.6) |
| [[NCI-H2122 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 255 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 280 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1373), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC7]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[ANAPC11]] | +0.68 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[SNRPD2]] | +0.67 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[ERLEC1]] | +0.66 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[NME7]] | +0.65 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[SEC22A]] | +0.64 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[KIAA1328]] | +0.64 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[COG5]] | +0.63 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[LCMT1]] | +0.63 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[EFHC1]] | +0.62 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[GBF1]] | +0.62 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[ATG4B]] | +0.62 | +0.52 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDM11]] | -0.68 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[FAIM]] | -0.67 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[SLC25A21]] | -0.65 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[DLG5]] | -0.64 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[FBXO30]] | -0.63 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[RNF6]] | -0.63 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[ARFGAP2]] | -0.63 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[TBKBP1]] | -0.62 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[SEPTIN8]] | -0.62 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ZNF564]] | -0.61 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[STRN4]] | -0.61 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[BRPF3]] | -0.60 | -0.44 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers PIBF1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF626]] | B | ZNF626 activity weakens PIBF1's drug response | lines that do not express ZNF626 (28) vs lines expressing it (21) | the lines without ZNF626 respond 1.17× as strongly (z diff -0.54); strongest at Panobinostat 0.5 µM: 1.83x vs 1.67x (z diff -1.7) | 0.086 | ⚠ within organs, on part of the lines; also absent: ROS1, GDNF, HTRA3; target measured in part of the lines; artifact flags |
| [[SCART1]] | C | SCART1 activity raises PIBF1's level | lines that do not express SCART1 (3) vs lines expressing it (47) | 1.61× lower at baseline in the lines without SCART1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: AHRR, ARHGAP15, FAT1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **-** arm (projection on the module's main direction -0.723). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-6.8, 8.0); signed map (-39.5, 13.8). **Vector** length 150, 54.6% of its response variance represented; |z| ≥ 3 in 1,398 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +8.2 | +14.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.7 | +13.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.7 | +16.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.5 | +7.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | +4.6 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +5.8 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +3.2 | +1.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +3.4 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.9 | +0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.0 | -13.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -9.3 | -8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.4 | -1.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.3 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.9 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.9 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.6 | -4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.1 | -4.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.9 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | progesterone immunomodulatory binding factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q21.33-q22.1 — chr13:72,782,133-73,016,461 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CEP90, PIBF; previously C13orf24 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXW3](https://www.uniprot.org/uniprotkb/Q8WXW3) (Progesterone-induced-blocking factor 1):

> Plays a role in ciliogenesis.; [Isoform 1]: Pericentriolar protein required to maintain mitotic spindle pole integrity. Required for the centrosomal accumulation of PCM1 and the recruitment of centriolar satellite proteins such as BBS4. Via association with PCM1 may be involved in primary cilia formation. Required for CEP63 centrosomal localization and its interaction with WDR62. Together with CEP63 promotes centriole duplication. Promotes the centrosomal localization of CDK2.; [Isoform 4]: The …

**Summary**, from NCBI Gene [10464](https://www.ncbi.nlm.nih.gov/gene/10464):

> This gene encodes a protein that is induced by the steroid hormone progesterone and plays a role in the maintenance of pregnancy. The encoded protein regulates multiple facets of the immune system to promote normal pregnancy including cytokine synthesis, natural killer (NK) cell activity, and arachidonic acid metabolism. Low serum levels of this protein have been associated with spontaneous pre-term labor in humans. This protein may promote the proliferation, migration and invasion of glioma. …

**Accessions** — [HGNC:23352](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23352) · Entrez [10464](https://www.ncbi.nlm.nih.gov/gene/10464) · UniProt [Q8WXW3](https://www.uniprot.org/uniprotkb/Q8WXW3) · Ensembl [ENSG00000083535](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083535)

## Data

Gene col 1373: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1373); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1373, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1373]; `tensor/DDL_lfc|DDL_z.npy` [1373]; `embed/gene_vectors.npy` [1373]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1373 or target_col == 1373). Every well: [[PIBF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIBF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
