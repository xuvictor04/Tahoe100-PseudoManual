---
symbol: "PHF20"
type: "gene"
col: 361
ensembl_id: "ENSG00000025293"
name: "PHD finger protein 20"
location: "20q11.22-q11.23"
module: 20
arm: "-"
pooled_cpm: 192.13
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# PHF20

*PHD finger protein 20* — 20q11.22-q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.27× (z +12.5, q 5e-33, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.489× (z -24.3, q 0e+00, down in 40 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.555× (z -11.3, q 2e-27, down in 34 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP7D3]] (+0.59, fdr 2e-05), [[DTNB]] (+0.59, fdr 1e-05), [[ZNF609]] (+0.58, fdr 1e-05); moves opposite to [[EDEM1]] (-0.54, fdr 4e-05), [[RPN1]] (-0.53, fdr 9e-05), [[IL18BP]] (-0.53, fdr 1e-04).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 361.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +12.5 | 5e-33 | 33/48 (HT-29, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.38×** | +11.8 | 2e-29 | 34/48 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +11.1 | 3e-26 | 33/48 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +9.4 | 7e-19 | 29/49 (HT-29, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.18× | +8.7 | 3e-16 | 20/48 (PANC-1, J82, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +8.1 | 4e-14 | 27/48 (HT-29, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +6.3 | 3e-08 | 21/48 (NCI-H1792, BT-474, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.13× | +4.6 | 3e-04 | 12/48 (Hs 766T, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.13× | +4.4 | 7e-04 | 4/48 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.13× | +4.4 | 7e-04 | 12/47 (NCI-H1573, BT-474, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.13× | +4.4 | 7e-04 | 15/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.12× | +4.2 | 0.002 | 8/48 (BT-474, H4, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.08× | +4.1 | 0.002 | 6/49 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.12× | +4.1 | 0.002 | 17/48 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.11× | +3.7 | 0.009 | 13/48 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | 1.10× | +3.7 | 0.009 | 12/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.009 | 19/48 (KATO III, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 1.10× | +3.5 | 0.016 | 13/49 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 5 µM |  | 1.18× | +3.2 | 0.040 | 9/48 (HOP62, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.09× | +3.1 | 0.047 | 10/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 361.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.489×** | -24.3 | 0e+00 | 40/45 (A-427, C32, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.576×** | -19.4 | 0e+00 | 39/44 (NCI-H23, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.590×** | -19.4 | 0e+00 | 43/49 (RKO, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.555×** | -11.3 | 2e-27 | 34/49 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.754×** | -10.3 | 5e-23 | 34/48 (C32, HOP62, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.631×** | -8.8 | 9e-17 | 25/48 (SW48, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.850× | -8.5 | 2e-15 | 23/49 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.811×** | -7.4 | 1e-11 | 24/47 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | 0.854× | -5.6 | 2e-06 | 19/47 (HepG2/C3A, MIA PaCa-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.855× | -5.5 | 2e-06 | 22/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.905× | -5.2 | 1e-05 | 13/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.803×** | -4.2 | 0.001 | 16/38 (Panc 03.27, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.893× | -4.0 | 0.003 | 22/50 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.911× | -3.4 | 0.026 | 10/48 (CHP-212, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | 0.918× | -3.2 | 0.060 | 3/47 (NCI-H2347, COLO 205, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.916× | -3.1 | 0.066 | 8/48 (HOP62, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 361. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 369 | 7 (1 ⚠) | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +11.6) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Triamcinolone (drug)]] 0.5 µM 1.66× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.570× (z -10.8) |
| [[Hs 766T (line)]] | wt | 271 | 7 (3 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.458× (z -12.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 155 | 7 (4 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.561× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.616× (z -9.0) |
| [[C32 (line)]] | wt | 140 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.196× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.362× (z -14.6) |
| [[NCI-H2030 (line)]] | alt | 378 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -22.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 191 | 4 (3 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +21.0) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -25.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.441× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 264 | 1 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 1.67× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.355× (z -16.6) ⚠ toxic; cell-cycle shift, explains ~18% of this change |
| [[NCI-H1792 (line)]] | alt | 312 | 4 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -17.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 459 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -26.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.543× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 165 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.417× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.568× (z -11.0) |
| [[HOP62 (line)]] | alt | 208 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.411× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.554× (z -12.3) |
| [[KATO III (line)]] | alt | 150 | 3 (3 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.81× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.362× (z -16.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 220 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -33.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.337× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 158 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.406× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.541× (z -10.2) |
| [[RKO (line)]] | wt | 191 | 2 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +13.4) ⚠ cell-cycle shift, explains ~15% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0589× (z -45.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 156 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.505× (z -9.7) |
| [[SNU-423 (line)]] | alt | 199 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -14.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 289 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +18.9) ⚠ cell-cycle shift, explains ~15% of this change | [[Dinaciclib (drug)]] 5 µM 0.582× (z -11.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 99.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.16× (z +18.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.84× (z +10.3) | — |
| [[SNU-1 (line)]] | wt | 203 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.421× (z -11.5) |
| [[BT-474 (line)]] | alt | 174 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -11.2) ⚠ cell-cycle shift, explains ~10% of this change |
| [[HS-578T (line)]] | alt | 147 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.516× (z -10.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 184 | 0 | 3 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.253× (z -11.8) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.370× (z -8.6) |
| [[A549 (line)]] | wt | 158 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -16.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 155 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +18.5) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[CFPAC-1 (line)]] | alt | 125 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.53× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.582× (z -8.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 148 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +11.1) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +10.2) | — |
| [[HepG2_C3A (line)]] | wt | 142 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.161× (z -21.9) ⚠ toxic; cell-cycle shift, explains ~18% of this change |
| [[RPMI-7951 (line)]] | alt | 203 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.378× (z -12.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 188 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.469× (z -12.2) |
| [[SW1417 (line)]] | alt | 182 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.399× (z -13.5) ⚠ toxic; cell-cycle shift, explains ~18% of this change |
| [[SW48 (line)]] | wt | 115 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.153× (z -10.4) |
| [[SW480 (line)]] | alt | 146 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.489× (z -13.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 189 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +13.9) ⚠ cell-cycle shift, explains ~15% of this change | — |
| [[A498 (line)]] | wt | 172 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.64× (z +8.8) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[C-33 A (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -19.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 141 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0750× (z -18.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 93.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.441× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 167 | 0 | 1 | — | [[Methylthiouracil (drug)]] 0.05 µM 0.0575× (z -14.6) |
| [[SW 1271 (line)]] | alt | 441 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -15.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 192 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 131 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 161 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 361), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP7D3]] | +0.59 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[DTNB]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[ZNF609]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 | same gene group |
| [[RAB11FIP3]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[SPTSSA]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[COX5A]] ⚠ | +0.55 | +0.50 / +0.49 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ARID3A]] | +0.54 | +0.37 / +0.57 | both halves | 7e-05 |  |
| [[MT1E]] | +0.54 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[ARL4A]] | +0.53 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[EIF1B]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[MT2A]] | +0.53 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[KRTCAP2]] | +0.53 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[TUT4]] | +0.52 | +0.39 / +0.50 | both halves | 6e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDEM1]] | -0.54 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[RPN1]] | -0.53 | -0.36 / -0.60 | both halves | 9e-05 |  |
| [[IL18BP]] | -0.53 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[PAPOLA]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[SDF4]] | -0.52 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[STT3A]] | -0.51 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[AGBL5]] | -0.50 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[CRYZ]] | -0.50 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[NAXD]] | -0.50 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[DDOST]] | -0.50 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[NCSTN]] | -0.50 | -0.27 / -0.61 | both halves | 3e-04 |  |
| [[TMEM30A]] | -0.49 | -0.38 / -0.58 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.529). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.5, 2.9); signed map (-10.5, 18.5). **Vector** length 132, 38.4% of its response variance represented; |z| ≥ 3 in 1,358 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +12.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +7.3 | +11.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +9.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.5 | +11.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | +6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.3 | +4.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.3 | +4.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +4.2 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +3.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -10.9 | -24.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.6 | -19.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -8.8 | -11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.6 | -19.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -7.3 | -8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.0 | -10.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -5.2 |
|  | [[Folic acid (drug)]] 5 µM |  | -2.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | PHD finger protein 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.22-q11.23 — chr20:35,771,974-35,950,370 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1121G12.1, TDRD20A; previously C20orf104 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; PHD finger proteins; Tudor domain containing; NSL histone acetyltransferase complex |
| Reactome | 17 pathways, smallest: Regulation of TP53 Activity through Association with Co-factors; Regulation of TP53 Degradation; Regulation of TP53 Expression and Degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVI0](https://www.uniprot.org/uniprotkb/Q9BVI0) (PHD finger protein 20):

> Methyllysine-binding protein, component of the MOF histone acetyltransferase protein complex. Not required for maintaining the global histone H4 'Lys-16' acetylation (H4K16ac) levels or locus specific histone acetylation, but instead works downstream in transcriptional regulation of MOF target genes (By similarity). As part of the NSL complex it may be involved in acetylation of nucleosomal histone H4 on several lysine residues. Contributes to methyllysine-dependent p53/TP53 stabilization and …

**Summary**, from NCBI Gene [51230](https://www.ncbi.nlm.nih.gov/gene/51230):

> Predicted to enable DNA binding activity and zinc ion binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Located in nuclear membrane and nucleoplasm. Part of MLL1 complex and histone acetyltransferase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16098](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16098) · Entrez [51230](https://www.ncbi.nlm.nih.gov/gene/51230) · UniProt [Q9BVI0](https://www.uniprot.org/uniprotkb/Q9BVI0) · Ensembl [ENSG00000025293](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000025293)

## Data

Gene col 361: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 361); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 361, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 361]; `tensor/DDL_lfc|DDL_z.npy` [361]; `embed/gene_vectors.npy` [361]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 361 or target_col == 361). Every well: [[PHF20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHF20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
