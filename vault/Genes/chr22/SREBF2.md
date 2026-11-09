---
symbol: "SREBF2"
type: "gene"
col: 12732
ensembl_id: "ENSG00000198911"
name: "sterol regulatory element binding transcription factor 2"
location: "22q13.2"
module: 86
arm: "+"
pooled_cpm: 185.22
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 37
n_dd_up_clean: 17
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# SREBF2

*sterol regulatory element binding transcription factor 2* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Cepharanthine (drug)]] 5 µM: 1.60× (z +10.9, q 1e-24, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.532× (z -14.5, q 4e-45, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MVD]] (+0.85, fdr 7e-06), [[FDFT1]] (+0.84, fdr 7e-06), [[FDPS]] (+0.80, fdr 7e-06); moves opposite to [[TRMT5]] (-0.57, fdr 3e-05), [[CLHC1]] (-0.54, fdr 3e-04), [[KRR1]] (-0.52, fdr 4e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12732.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **1.60×** | +10.9 | 1e-24 | 46/48 (NCI-H23, HOP62, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | **1.50×** | +9.4 | 2e-18 | 44/49 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +8.8 | 3e-16 | 40/48 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +6.8 | 2e-09 | 38/48 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +6.7 | 2e-09 | 35/48 (LoVo, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Posaconazole (drug)]] 5 µM |  | **1.51×** | +6.5 | 1e-08 | 43/48 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +5.9 | 3e-07 | 31/48 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.85×** | +5.2 | 1e-05 | 41/49 (A-172, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.8 | 1e-04 | 33/48 (HOP62, SNU-423, …) | top dose only | plate-row cell shift |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.34×** | +4.6 | 3e-04 | 34/49 (HOP62, C32, …) | rises with dose | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +4.5 | 4e-04 | 27/47 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +4.0 | 0.003 | 25/49 (H4, Panc 03.27, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.17× | +3.7 | 0.009 | 18/48 (A549, H4, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.53×** | +3.6 | 0.011 | 25/48 (HCT15, RKO, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Berbamine (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.013 | 27/48 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.17× | +3.5 | 0.015 | 17/49 (C-33 A, H4, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.015 | 24/48 (NCI-H1573, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12732.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.532×** | -14.5 | 4e-45 | 46/49 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.547×** | -9.8 | 3e-20 | 37/48 (CFPAC-1, BT-474, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.564×** | -9.3 | 2e-18 | 40/48 (RKO, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.558×** | -9.1 | 9e-18 | 46/47 (SNU-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.546×** | -9.1 | 9e-18 | 40/45 (C-33 A, NCI-H1792, …) | all doses, flat | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.692×** | -8.5 | 2e-15 | 43/48 (HS-578T, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.707×** | -8.0 | 1e-13 | 43/48 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.619×** | -7.8 | 4e-13 | 39/48 (RKO, PANC-1, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.612×** | -7.7 | 1e-12 | 41/48 (hTERT-HPNE, HS-578T, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.628×** | -7.6 | 2e-12 | 36/48 (HCT15, A-172, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.627×** | -7.3 | 1e-11 | 40/48 (LS 180, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.648×** | -7.1 | 8e-11 | 39/49 (COLO 205, CHP-212, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.663×** | -6.4 | 5e-09 | 35/44 (SK-MEL-2, SW 900, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.693×** | -6.0 | 1e-07 | 43/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.773×** | -5.9 | 1e-07 | 26/48 (NCI-H1792, A-427, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.717×** | -5.0 | 2e-05 | 33/47 (RKO, C32, …) | all doses, flat | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.779×** | -4.1 | 0.001 | 26/48 (hTERT-HPNE, NCI-H1792, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.779×** | -4.1 | 0.001 | 33/48 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.789×** | -3.9 | 0.003 | 31/49 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.790×** | -3.8 | 0.003 | 29/48 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.784×** | -3.8 | 0.004 | 26/47 (RPMI-7951, RKO, …) | inconsistent across doses |  |
| [[Belumosudil (mesylate) (drug)]] 5 µM |  | **0.658×** | -3.6 | 0.008 | 28/48 (KATO III, RPMI-7951, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12732. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 208 | 2 | 7 (2 ⚠) | [[Berbamine (drug)]] 5 µM 1.97× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -16.3) |
| [[HT-29 (line)]] | alt | 207 | 5 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +11.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.378× (z -11.4) |
| [[KATO III (line)]] | alt | 303 | 3 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.583× (z -10.2) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.498× (z -9.3) |
| [[LoVo (line)]] | wt | 188 | 7 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.33× (z +16.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -10.4) |
| [[LS 180 (line)]] | wt | 270 | 3 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 545 | 1 | 6 (4 ⚠) | [[Cepharanthine (drug)]] 5 µM 1.82× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.403× (z -9.6) |
| [[SNU-1 (line)]] | wt | 284 | 5 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.87× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.273× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 226 | 2 | 4 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 2.04× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -15.2) |
| [[HOP62 (line)]] | alt | 175 | 4 | 2 | [[Berbamine (drug)]] 5 µM 2.52× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 168 | 1 | 5 (3 ⚠) | [[Cepharanthine (drug)]] 5 µM 1.87× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 260 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -19.4) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 147 | 4 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 170 | 2 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -10.0) |
| [[SNU-423 (line)]] | alt | 145 | 2 | 3 | [[Cepharanthine (drug)]] 5 µM 2.07× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 211 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -13.9) |
| [[COLO 205 (line)]] | alt | 340 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.77× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -13.4) |
| [[HEC-1-A (line)]] | alt | 222 | 4 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.56× (z +11.7) ⚠ toxic · without an alert: [[Berbamine (drug)]] 5 µM 1.75× (z +10.2) | — |
| [[RKO (line)]] | wt | 206 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -14.0) |
| [[RPMI-7951 (line)]] | alt | 159 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -13.7) |
| [[SW 900 (line)]] | alt | 152 | 1 | 3 (2 ⚠) | [[Berbamine (drug)]] 5 µM 1.96× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -10.7) |
| [[SW480 (line)]] | alt | 153 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -16.6) |
| [[A549 (line)]] | wt | 136 | 2 | 1 | [[Cepharanthine (drug)]] 5 µM 2.30× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -8.6) |
| [[H4 (line)]] | wt | 99.5 | 2 | 1 | [[Cepharanthine (drug)]] 5 µM 2.44× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -10.3) |
| [[HCT15 (line)]] | alt | 241 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.320× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 196 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.369× (z -9.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 114 | 2 | 1 | [[Cepharanthine (drug)]] 5 µM 3.31× (z +14.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 196 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.413× (z -10.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -9.5) |
| [[A-427 (line)]] | wt | 170 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -14.8) ⚠ cell-cycle shift, explains ~15% of this change |
| [[BT-474 (line)]] | alt | 300 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.371× (z -10.8) |
| [[C-33 A (line)]] | alt | 234 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[CHP-212 (line)]] | wt | 261 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 192 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -9.5) |
| [[PANC-1 (line)]] | alt | 144 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.421× (z -9.7) |
| [[A-172 (line)]] | wt | 102 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.368× (z -11.0) |
| [[AN3 CA (line)]] | alt | 251 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -9.4) ⚠ cell-cycle shift, explains ~15% of this change |
| [[J82 (line)]] | alt | 131 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 114 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.423× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 180 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.361× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[SW1417 (line)]] | alt | 101 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.18× (z +8.7) | — |
| [[A498 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 149 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 173 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 235 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12732), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MVD]] | +0.85 | +0.83 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 894 |
| [[FDFT1]] | +0.84 | +0.80 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 888 |
| [[FDPS]] | +0.80 | +0.82 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 896 |
| [[ACSS2]] | +0.79 | +0.74 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 476 |
| [[EBP]] | +0.78 | +0.72 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[ERG28]] | +0.76 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[DHCR7]] | +0.76 | +0.70 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 907 |
| [[INSIG1]] | +0.76 | +0.73 / +0.67 | both halves | 7e-06 | pathway: Metabolism of steroids; STRING 997 |
| [[MSMO1]] | +0.73 | +0.74 / +0.69 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 772 |
| [[HMGCR]] | +0.73 | +0.68 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 985 |
| [[SQLE]] | +0.72 | +0.72 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 892 |
| [[MVK]] | +0.72 | +0.60 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 820 |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT5]] | -0.57 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[CLHC1]] | -0.54 | -0.61 / -0.27 | both halves | 3e-04 |  |
| [[KRR1]] | -0.52 | -0.57 / -0.25 | both halves | 4e-04 |  |
| [[C8orf33]] | -0.51 | -0.59 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[CYREN]] | -0.50 | -0.62 / -0.27 | both halves | 3e-04 |  |
| [[ZNF507]] | -0.50 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[MTHFSD]] | -0.50 | -0.53 / -0.23 | both halves | 5e-04 |  |
| [[ZXDB]] | -0.50 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[KICS2]] | -0.49 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[DDX20]] | -0.49 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[ERAL1]] | -0.49 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[GTF3C4]] | -0.49 | -0.46 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SREBF2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.831). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.4, -48.8); signed map (-53.1, 32.3). **Vector** length 138, 54.6% of its response variance represented; |z| ≥ 3 in 1,862 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *cholesterol synthesis* (control, mean cos +0.67 to 22); *mTORC1 signaling* (hallmark, mean cos +0.60 to 19); *Lanosterol biosynthesis* (reactome, mean cos +0.72 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | +11.0 | -6.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | +10.4 | -7.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +9.8 | +10.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +9.1 | -1.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.8 | -3.8 |
|  | [[Berbamine (drug)]] 5 µM |  | +8.5 | +9.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +6.8 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | -1.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.9 | +2.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -10.4 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.7 | -9.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -9.2 | -7.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.2 | -8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -8.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.4 | -7.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.7 | -3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.6 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | sterol regulatory element binding transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:41,833,105-41,907,306 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SREBP2, bHLHd2 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; MicroRNA protein coding host genes; Sterol regulatory element binding transcription factor family |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS |
| Reactome | 12 pathways, smallest: Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway); EGR2 and SOX10-mediated initiation of Schwann cell myelination; Cholesterol biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12772](https://www.uniprot.org/uniprotkb/Q12772) (Sterol regulatory element-binding protein 2):

> [Sterol regulatory element-binding protein 2]: Precursor of the transcription factor form (Processed sterol regulatory element-binding protein 2), which is embedded in the endoplasmic reticulum membrane. Low sterol concentrations promote processing of this form, releasing the transcription factor form that translocates into the nucleus and activates transcription of genes involved in cholesterol biosynthesis.; [Processed sterol regulatory element-binding protein 2]: Key transcription factor …

**Summary**, from NCBI Gene [6721](https://www.ncbi.nlm.nih.gov/gene/6721):

> This gene encodes a member of the a ubiquitously expressed transcription factor that controls cholesterol homeostasis by regulating transcription of sterol-regulated genes. The encoded protein contains a basic helix-loop-helix-leucine zipper (bHLH-Zip) domain and binds the sterol regulatory element 1 motif. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:11290](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11290) · Entrez [6721](https://www.ncbi.nlm.nih.gov/gene/6721) · UniProt [Q12772](https://www.uniprot.org/uniprotkb/Q12772) · Ensembl [ENSG00000198911](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198911)

## Data

Gene col 12732: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12732); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12732, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12732]; `tensor/DDL_lfc|DDL_z.npy` [12732]; `embed/gene_vectors.npy` [12732]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12732 or target_col == 12732). Every well: [[SREBF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SREBF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
