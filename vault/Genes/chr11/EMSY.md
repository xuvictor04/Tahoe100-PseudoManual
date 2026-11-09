---
symbol: "EMSY"
type: "gene"
col: 8178
ensembl_id: "ENSG00000158636"
name: "EMSY transcriptional repressor, BRCA2 interacting"
location: "11q13.5"
module: 144
arm: "+"
pooled_cpm: 119.6
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 16
n_dd_up_clean: 14
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# EMSY

*EMSY transcriptional repressor, BRCA2 interacting* — 11q13.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.36× (z +18.0, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.360× (z -20.5, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.646× (z -9.1, q 1e-17, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM2A]] (+0.64, fdr 7e-06), [[SSR4]] (+0.61, fdr 1e-05), [[BCKDHA]] (+0.61, fdr 7e-06); moves opposite to [[N6AMT1]] (-0.60, fdr 1e-05), [[GMFB]] (-0.60, fdr 1e-05), [[RRP15]] (-0.59, fdr 1e-05).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8178.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.36×** | +18.0 | 0e+00 | 46/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.82×** | +12.6 | 6e-34 | 45/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +11.2 | 1e-26 | 42/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.72×** | +11.0 | 9e-26 | 41/49 (BT-474, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +10.4 | 4e-23 | 43/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +9.6 | 7e-20 | 30/49 (MIA PaCa-2, AsPC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.15×** | +8.4 | 5e-15 | 35/48 (BT-474, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +7.4 | 1e-11 | 35/48 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.38×** | +6.8 | 8e-10 | 31/47 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +6.2 | 3e-08 | 35/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.29×** | +5.4 | 4e-06 | 30/48 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +5.3 | 4e-06 | 35/48 (PANC-1, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +5.2 | 7e-06 | 34/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.7 | 9e-05 | 25/50 (SK-MEL-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.48×** | +4.3 | 7e-04 | 26/48 (HOP62, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.20× | +3.6 | 0.010 | 18/49 (BT-474, SHP-77, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8178.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.360×** | -20.5 | 0e+00 | 43/44 (NCI-H1792, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.390×** | -19.7 | 0e+00 | 48/49 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.393×** | -18.0 | 0e+00 | 45/45 (C32, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.646×** | -9.1 | 1e-17 | 41/48 (AN3 CA, C32, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.766×** | -7.9 | 4e-13 | 37/48 (C32, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.783×** | -7.2 | 6e-11 | 33/48 (SW 900, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.731×** | -6.5 | 5e-09 | 39/48 (A-427, NCI-H2030, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.730×** | -6.3 | 2e-08 | 36/47 (NCI-H2030, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.761×** | -5.7 | 8e-07 | 30/48 (KATO III, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.775×** | -5.3 | 6e-06 | 32/48 (hTERT-HPNE, SW 1088, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.777×** | -5.0 | 2e-05 | 30/48 (C32, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.805×** | -4.5 | 3e-04 | 26/48 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.864× | -4.3 | 7e-04 | 22/48 (NCI-H1792, Hs 766T, …) | all doses, flat | composition shift |
| [[Belzutifan (drug)]] 5 µM |  | **0.699×** | -3.9 | 0.004 | 24/47 (NCI-H661, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.834× | -3.8 | 0.006 | 20/49 (RPMI-7951, NCI-H23, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.836× | -3.7 | 0.007 | 19/48 (SW 900, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.828×** | -3.6 | 0.010 | 22/47 (AsPC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | 0.845× | -3.5 | 0.014 | 18/48 (NCI-H1792, LS 180, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.750×** | -3.1 | 0.043 | 19/48 (KATO III, SW480, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.808×** | -2.9 | 0.073 | 18/48 (HT-29, NCI-H2030, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.868× | -2.9 | 0.073 | 16/49 (A549, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8178. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 151 | 3 (1 ⚠) | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.25× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.135× (z -24.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.619× (z -8.5) |
| [[PANC-1 (line)]] | alt | 143 | 6 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +14.7) | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -18.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 237 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.511× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 84.8 | 5 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.06× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -16.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 107 | 3 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -12.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 97.3 | 3 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -15.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 156 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -19.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 122 | 3 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -14.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 120 | 3 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.36× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -15.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 91.5 | 2 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +15.7) | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.428× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 97.4 | 2 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -14.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 105 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.09× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.587× (z -8.9) |
| [[A-427 (line)]] | wt | 143 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.172× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.453× (z -10.4) |
| [[C32 (line)]] | wt | 189 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0912× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.352× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 101 | 3 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.393× (z -12.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 85.9 | 3 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.95× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.291× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.463× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 121 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 97.9 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.90× (z +14.6) | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -14.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 185 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.197× (z -20.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 260 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -18.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 165 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -16.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 118 | 2 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +10.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.386× (z -12.2) ⚠ toxic |
| [[A549 (line)]] | wt | 130 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -21.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 121 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -13.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 120 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -12.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 131 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.498× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 102 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.361× (z -13.3) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 109 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -12.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 187 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.0704× (z -22.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -9.5) |
| [[C-33 A (line)]] | alt | 156 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -12.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 111 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.472× (z -9.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 174 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0833× (z -19.9) |
| [[AsPC-1 (line)]] | alt | 103 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.451× (z -9.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 66.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +11.0) | — |
| [[H4 (line)]] | wt | 116 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -12.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 97.9 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 113 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -17.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 105 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.75× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.266× (z -11.9) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 91.7 | 0 | 2 (1 ⚠) | — | [[Talc (drug)]] 0.05 µM 0.0883× (z -9.4) |
| [[COLO 205 (line)]] | alt | 86.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.19× (z +11.6) | — |
| [[HCT15 (line)]] | alt | 198 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -14.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 83.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -11.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 62.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -10.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 84.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -9.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 182 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8178), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM2A]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[SSR4]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[BCKDHA]] | +0.61 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[NARF]] | +0.61 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[GPBP1L1]] | +0.60 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[SUZ12P1]] | +0.60 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[COG7]] | +0.60 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[HIGD2A]] | +0.60 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[BMT2]] | +0.59 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[UBE4B]] | +0.59 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[FANCM]] | +0.59 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[SPICE1]] | +0.58 | +0.65 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N6AMT1]] | -0.60 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[GMFB]] | -0.60 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[RRP15]] | -0.59 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[HUS1]] | -0.59 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[C12orf29]] | -0.58 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[AIMP2]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[TMEM185B]] | -0.56 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[POGK]] | -0.55 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[QDPR]] | -0.54 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[COA7]] | -0.54 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[SUGT1P3]] | -0.53 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[SFPQ]] | -0.52 | -0.55 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EMSY's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.522). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.8, -39.4); signed map (-30.3, 26.4). **Vector** length 127, 46.1% of its response variance represented; |z| ≥ 3 in 1,374 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.2 | +9.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.2 | +7.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.4 | +4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.8 | +18.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.6 | +12.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.0 | +5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.2 | +2.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.1 | +2.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.3 | -9.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -8.0 | -4.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.7 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.8 | -6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -7.2 |
|  | [[EX229 (drug)]] 5 µM |  | -4.0 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -5.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | EMSY transcriptional repressor, BRCA2 interacting |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.5 — chr11:76,444,923-76,553,031 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C11orf30 |
| Gene groups (HGNC) | EMSY complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z589](https://www.uniprot.org/uniprotkb/Q7Z589) (BRCA2-interacting transcriptional repressor EMSY):

> Regulator which is able to repress transcription, possibly via its interaction with a multiprotein chromatin remodeling complex that modifies the chromatin. Its interaction with BRCA2 suggests that it may play a central role in the DNA repair function of BRCA2. Mediates ligand-dependent transcriptional activation by nuclear hormone receptors.

**Summary**, from NCBI Gene [56946](https://www.ncbi.nlm.nih.gov/gene/56946):

> Predicted to enable identical protein binding activity. Predicted to be involved in several processes, including DNA repair; DNA-templated transcription; and regulation of DNA-templated transcription. Located in nucleoplasm. Implicated in allergic rhinitis and asthma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18071](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18071) · Entrez [56946](https://www.ncbi.nlm.nih.gov/gene/56946) · UniProt [Q7Z589](https://www.uniprot.org/uniprotkb/Q7Z589) · Ensembl [ENSG00000158636](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158636)

## Data

Gene col 8178: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8178); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8178, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8178]; `tensor/DDL_lfc|DDL_z.npy` [8178]; `embed/gene_vectors.npy` [8178]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8178 or target_col == 8178). Every well: [[EMSY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMSY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
