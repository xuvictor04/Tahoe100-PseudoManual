---
symbol: "ANLN"
type: "gene"
col: 240
ensembl_id: "ENSG00000011426"
name: "anillin, actin binding protein"
location: "7p14.2"
module: 22
arm: "+"
pooled_cpm: 229.69
n_lines_expressing: 48
n_dd_up: 22
n_dd_down: 32
n_dd_up_clean: 3
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# ANLN

*anillin, actin binding protein* — 7p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.96× (z +13.1, q 1e-36, up in 33 of 46 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.77× (z +4.1, q 0.001, up in 24 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.571× (z -10.9, q 5e-25, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF11]] (+0.90, fdr 7e-06), [[TPX2]] (+0.89, fdr 7e-06), [[NCAPG]] (+0.89, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MYBL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 19 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 240.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.96×** | +13.1 | 1e-36 | 33/46 (RKO, HS-578T, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **2.17×** | +10.8 | 1e-24 | 44/46 (LoVo, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.90×** | +8.9 | 9e-17 | 43/46 (NCI-H23, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.81×** | +8.2 | 2e-14 | 41/46 (LoVo, C-33 A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.79×** | +7.8 | 7e-13 | 33/46 (RKO, A-427, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.60×** | +6.9 | 4e-10 | 37/47 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.63×** | +6.8 | 9e-10 | 39/46 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.59×** | +6.4 | 1e-08 | 32/45 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.54×** | +6.0 | 2e-07 | 35/46 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | **1.56×** | +5.9 | 2e-07 | 28/42 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.50×** | +5.7 | 8e-07 | 33/47 (NCI-H23, C32, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +4.6 | 2e-04 | 26/46 (HT-29, HOP62, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~90% of this change | **1.40×** | +4.5 | 4e-04 | 29/45 (C32, NCI-H23, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.77×** | +4.1 | 0.001 | 24/46 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | **1.35×** | +3.9 | 0.004 | 24/43 (A-172, C32, …) | all doses, stronger at high dose | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.023 | 21/45 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.025 | 22/46 (SW480, H4, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.3 | 0.025 | 19/46 (RKO, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 240.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.571×** | -10.9 | 5e-25 | 38/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.580×** | -10.6 | 6e-24 | 39/46 (A498, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.502×** | -9.6 | 2e-19 | 42/46 (LS 180, A-427, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.628×** | -6.5 | 1e-08 | 31/46 (A498, H4, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.753×** | -5.5 | 4e-06 | 28/46 (SW48, A498, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.658×** | -5.1 | 3e-05 | 33/46 (SW48, H4, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.720×** | -4.6 | 4e-04 | 36/47 (COLO 205, LoVo, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.723×** | -4.5 | 4e-04 | 31/46 (HT-29, LoVo, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.799×** | -4.4 | 7e-04 | 26/46 (HCT15, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.736×** | -4.3 | 0.001 | 23/47 (A-172, H4, …) | two highest doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | **0.813×** | -4.0 | 0.003 | 26/47 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.750×** | -4.0 | 0.003 | 35/46 (hTERT-HPNE, A549, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.594×** | -3.8 | 0.007 | 25/46 (LoVo, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **0.824×** | -3.8 | 0.007 | 23/46 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.757×** | -3.7 | 0.007 | 25/45 (SW480, SW48, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.770×** | -3.6 | 0.009 | 26/46 (A549, NCI-H2347, …) | inconsistent across doses |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.743×** | -3.6 | 0.009 | 26/47 (Hs 766T, RKO, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.830×** | -3.6 | 0.010 | 20/46 (H4, LoVo, …) | two highest doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.611×** | -3.6 | 0.010 | 27/45 (Hs 766T, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.792×** | -3.3 | 0.031 | 23/46 (A549, SW480, …) | all doses, flat |  |
| [[Belumosudil (mesylate) (drug)]] 5 µM |  | **0.652×** | -3.1 | 0.045 | 21/46 (MIA PaCa-2, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **0.801×** | -3.1 | 0.047 | 22/46 (SW48, KATO III, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 5 µM |  | **0.660×** | -3.0 | 0.056 | 22/46 (SW480, KATO III, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.93 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 240. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 166 | 9 (9 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +12.4) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -12.2) |
| [[H4 (line)]] | wt | 344 | 0 | 9 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.197× (z -13.3) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -13.2) |
| [[LoVo (line)]] | wt | 152 | 5 (5 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.05× (z +13.2) ⚠ cell-cycle shift, explains ~64% of this change | [[Selinexor (drug)]] 5 µM 0.358× (z -13.6) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.504× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 183 | 1 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +13.3) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.318× (z -12.9) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.424× (z -9.6) |
| [[LS 180 (line)]] | wt | 137 | 1 (1 ⚠) | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +8.6) ⚠ cell-cycle shift, explains ~64% of this change | [[Selinexor (drug)]] 5 µM 0.142× (z -19.9) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -10.9) |
| [[A498 (line)]] | wt | 285 | 1 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +12.2) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.191× (z -21.1) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -12.3) |
| [[A-172 (line)]] | wt | 194 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.254× (z -16.3) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.409× (z -10.5) |
| [[A549 (line)]] | wt | 201 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +16.6) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.402× (z -11.7) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 110 | 4 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +13.2) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.326× (z -10.2) ⚠ cell-cycle shift, explains ~83% of this change |
| [[KATO III (line)]] | alt | 467 | 4 (4 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 3.10× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 218 | 4 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +14.5) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -8.8) |
| [[PANC-1 (line)]] | alt | 422 | 3 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +14.0) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -16.9) |
| [[SW48 (line)]] | wt | 288 | 0 | 5 (3 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.338× (z -13.2) |
| [[RKO (line)]] | wt | 125 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.61× (z +20.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW480 (line)]] | alt | 511 | 2 (2 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 0.05 µM 2.69× (z +10.3) ⚠ cell-cycle shift, explains ~60% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -16.7) |
| [[A-427 (line)]] | wt | 147 | 1 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.03× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.254× (z -18.6) ⚠ cell-cycle shift, explains ~83% of this change |
| [[C32 (line)]] | wt | 86.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +13.1) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.411× (z -9.4) ⚠ cell-cycle shift, explains ~83% of this change |
| [[HOP62 (line)]] | alt | 209 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -13.9) |
| [[HT-29 (line)]] | alt | 171 | 1 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +8.8) ⚠ cell-cycle shift, explains ~64% of this change | [[Selinexor (drug)]] 5 µM 0.446× (z -9.5) ⚠ cell-cycle shift, explains ~83% of this change |
| [[NCI-H460 (line)]] | wt | 150 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -11.2) |
| [[HCT15 (line)]] | alt | 211 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -9.8) |
| [[Hs 766T (line)]] | wt | 383 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 129 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +16.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[J82 (line)]] | alt | 217 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +16.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 258 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -9.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 318 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +13.0) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.498× (z -9.6) ⚠ cell-cycle shift, explains ~83% of this change |
| [[SK-MEL-2 (line)]] | alt | 281 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 130 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[BT-474 (line)]] | alt | 205 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C-33 A (line)]] | alt | 99.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.50× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | — |
| [[CFPAC-1 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.481× (z -9.0) ⚠ cell-cycle shift, explains ~83% of this change |
| [[HEC-1-A (line)]] | alt | 429 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 59.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +15.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 227 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 224 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 230 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.357× (z -10.8) ⚠ cell-cycle shift, explains ~83% of this change |
| [[SW 1271 (line)]] | alt | 265 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 183 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 164 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +16.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 188 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.1 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 39.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 253 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 269 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 240), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF11]] | +0.90 | +0.89 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 947 |
| [[TPX2]] | +0.89 | +0.88 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 923 |
| [[NCAPG]] | +0.89 | +0.89 / +0.88 | both halves | 7e-06 | STRING 681 |
| [[BIRC5]] | +0.89 | +0.85 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 781 |
| [[NCAPH]] | +0.89 | +0.89 / +0.86 | both halves | 7e-06 | STRING 707 |
| [[PRC1]] | +0.88 | +0.88 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 839 |
| [[KIF4A]] | +0.88 | +0.87 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 782 |
| [[RACGAP1]] | +0.88 | +0.87 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 997 |
| [[KIF23]] | +0.87 | +0.87 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 989 |
| [[MKI67]] | +0.87 | +0.86 / +0.85 | both halves | 7e-06 | STRING 745 |
| [[BUB1B]] | +0.87 | +0.86 / +0.85 | both halves | 7e-06 | STRING 800 |
| [[TOP2A]] | +0.87 | +0.85 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 861 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYBL1]] | B | MYBL1 activity raises ANLN's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.75× lower at baseline in the lines without MYBL1 | 0.064 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises ANLN's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.01× lower at baseline in the lines without NEURL1B | 0.078 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[AURKB]] | C | AURKB activity raises ANLN's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.20× lower at baseline in the lines without AURKB | 0.033 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[PBK]] | C | PBK activity raises ANLN's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.93× lower at baseline in the lines without PBK | 0.034 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[CDC20]] | C | CDC20 activity raises ANLN's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.18× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[DIAPH3]], [[MELK]] | C | DIAPH3, MELK activity raises ANLN's level | lines that do not express DIAPH3, MELK (3) vs lines expressing them (47) | 3.11× lower at baseline in the lines without DIAPH3, MELK | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.882). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.5, -54.4); signed map (-48.1, -43.6). **Vector** length 166, 68.0% of its response variance represented; |z| ≥ 3 in 1,711 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.71 to 60); *DREAM G2/M down* (control, mean cos +0.78 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.68 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.5 | +13.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.4 | +3.7 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.1 | +4.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | +5.1 | +6.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +1.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.2 | +1.7 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +3.1 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +0.9 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -9.0 | -9.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | -8.6 | -10.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~94% of this change | -8.1 | -5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -10.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.9 | -4.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.9 | -5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -2.5 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -3.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.8 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | anillin, actin binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.2 — chr7:36,389,821-36,453,791 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ANILLIN, Scraps, scra |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 6 pathways, smallest: RHOB GTPase cycle; RHOC GTPase cycle; RHOA GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQW6](https://www.uniprot.org/uniprotkb/Q9NQW6) (Anillin):

> Required for cytokinesis. Essential for the structural integrity of the cleavage furrow and for completion of cleavage furrow ingression. Plays a role in bleb assembly during metaphase and anaphase of mitosis. May play a significant role in podocyte cell migration.

**Summary**, from NCBI Gene [54443](https://www.ncbi.nlm.nih.gov/gene/54443):

> This gene encodes an actin-binding protein that plays a role in cell growth and migration, and in cytokinesis. The encoded protein is thought to regulate actin cytoskeletal dynamics in podocytes, components of the glomerulus. Mutations in this gene are associated with focal segmental glomerulosclerosis 8. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Oct 2014]

**Accessions** — [HGNC:14082](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14082) · Entrez [54443](https://www.ncbi.nlm.nih.gov/gene/54443) · UniProt [Q9NQW6](https://www.uniprot.org/uniprotkb/Q9NQW6) · Ensembl [ENSG00000011426](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011426)

## Data

Gene col 240: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 240); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 240, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 240]; `tensor/DDL_lfc|DDL_z.npy` [240]; `embed/gene_vectors.npy` [240]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 240 or target_col == 240). Every well: [[ANLN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANLN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
