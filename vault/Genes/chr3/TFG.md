---
symbol: "TFG"
type: "gene"
col: 3543
ensembl_id: "ENSG00000114354"
name: "trafficking from ER to golgi regulator"
location: "3q12.2"
module: 56
arm: "+"
pooled_cpm: 255.07
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 32
n_dd_up_clean: 9
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# TFG

*trafficking from ER to golgi regulator* — 3q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.78× (z +7.8, q 3e-12, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.360× (z -14.3, q 7e-44, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.454× (z -11.5, q 2e-28, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB1A]] (+0.73, fdr 7e-06), [[PRRC1]] (+0.73, fdr 7e-06), [[TMEM39A]] (+0.70, fdr 7e-06); moves opposite to [[TNFRSF12A]] (-0.60, fdr 1e-05), [[REXO1]] (-0.59, fdr 2e-05), [[ZBTB38]] (-0.58, fdr 2e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3543.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.78×** | +7.8 | 3e-12 | 46/49 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.63×** | +7.1 | 4e-10 | 37/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.51×** | +7.0 | 4e-10 | 42/48 (SW480, hTERT-HPNE, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +5.5 | 4e-06 | 29/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +5.0 | 6e-05 | 37/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 7e-04 | 32/48 (A-427, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +4.1 | 0.003 | 32/48 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +4.0 | 0.004 | 30/47 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.29×** | +3.7 | 0.016 | 27/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.044 | 26/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.049 | 30/48 (NCI-H460, SNU-423, …) | rises with dose | plate-row cell shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.48× | +3.0 | 0.13 | 22/38 (NCI-H1573, SW480, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3543.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.360×** | -14.3 | 7e-44 | 44/44 (NCI-H23, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.448×** | -11.7 | 3e-29 | 46/49 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.454×** | -11.5 | 2e-28 | 47/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.468×** | -11.1 | 2e-26 | 48/48 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.512×** | -9.8 | 2e-20 | 47/48 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.648×** | -9.0 | 3e-17 | 42/49 (RPMI-7951, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.691×** | -5.4 | 5e-06 | 37/48 (A-172, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.694×** | -5.3 | 6e-06 | 37/48 (SW 900, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.687×** | -5.3 | 8e-06 | 35/47 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.789×** | -4.9 | 6e-05 | 35/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.728×** | -4.6 | 2e-04 | 29/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.732×** | -4.6 | 3e-04 | 31/48 (hTERT-HPNE, RPMI-7951, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.721×** | -4.4 | 4e-04 | 32/45 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.748×** | -4.2 | 9e-04 | 39/48 (SW 1088, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.747×** | -4.1 | 0.002 | 34/48 (NCI-H2347, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.760×** | -4.0 | 0.002 | 29/48 (NCI-H2347, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.762×** | -4.0 | 0.002 | 35/48 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.783×** | -3.6 | 0.011 | 30/49 (NCI-H2347, COLO 205, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.794×** | -3.4 | 0.021 | 33/48 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3543. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 327 | 4 (2 ⚠) | 5 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.52× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.465× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 186 | 6 (2 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.69× (z +18.4) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 361 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.301× (z -13.5) |
| [[PANC-1 (line)]] | alt | 207 | 8 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.47× (z +19.3) | — |
| [[NCI-H2347 (line)]] | alt | 528 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.370× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 414 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.159× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -15.0) |
| [[A-172 (line)]] | wt | 243 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -14.8) |
| [[AsPC-1 (line)]] | alt | 201 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -15.6) |
| [[HOP62 (line)]] | alt | 280 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -11.6) |
| [[KATO III (line)]] | alt | 213 | 2 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.344× (z -13.3) |
| [[NCI-H1792 (line)]] | alt | 194 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 251 | 4 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.135× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -9.7) |
| [[SW 900 (line)]] | alt | 326 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -12.2) |
| [[A-427 (line)]] | wt | 261 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.38× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.370× (z -12.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 266 | 1 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +8.9) ⚠ cell-cycle shift, explains ~1% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -12.6) |
| [[BT-474 (line)]] | alt | 181 | 1 | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.40× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.403× (z -9.1) |
| [[H4 (line)]] | wt | 309 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.304× (z -10.5) |
| [[HS-578T (line)]] | alt | 447 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 260 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -11.1) |
| [[COLO 205 (line)]] | alt | 207 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.361× (z -9.5) |
| [[Hs 766T (line)]] | wt | 219 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.402× (z -9.4) |
| [[HT-29 (line)]] | alt | 212 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.464× (z -9.6) |
| [[LoVo (line)]] | wt | 201 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.409× (z -9.9) |
| [[SW480 (line)]] | alt | 129 | 3 | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.525× (z -9.0) |
| [[A498 (line)]] | wt | 329 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.359× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 320 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -12.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 269 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.396× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 301 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.456× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 277 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -11.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 310 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -16.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 295 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -13.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 224 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -9.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 217 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -9.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 124 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +8.6) | — |
| [[J82 (line)]] | alt | 285 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.471× (z -8.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 215 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.363× (z -9.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 190 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -12.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 203 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -8.8) |
| [[SW 1271 (line)]] | alt | 232 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -10.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 192 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 153 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 256 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 270 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 288 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 208 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3543), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB1A]] | +0.73 | +0.79 / +0.66 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 574 |
| [[PRRC1]] | +0.73 | +0.84 / +0.66 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.70 | +0.82 / +0.59 | both halves | 7e-06 |  |
| [[SEC23A]] | +0.69 | +0.84 / +0.55 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation; STRING 591 |
| [[COPA]] | +0.69 | +0.83 / +0.53 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[CLINT1]] | +0.68 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.68 | +0.79 / +0.55 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation; STRING 666 |
| [[SRP54-AS1]] | +0.68 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[COPS4]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[FAM168A]] | +0.67 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[COG6]] | +0.65 | +0.76 / +0.55 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[SUCO]] | +0.65 | +0.75 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF12A]] | -0.60 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[REXO1]] | -0.59 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[ZBTB38]] | -0.58 | -0.67 / -0.48 | both halves | 2e-05 |  |
| [[AGO2]] | -0.58 | -0.47 / -0.57 | both halves | 2e-05 | pathway: Signaling by ALK fusions and activated point mutants |
| [[RESF1]] | -0.58 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[NOP14]] | -0.57 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[ASXL2]] | -0.57 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[SPEN]] | -0.55 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[ARHGAP39]] | -0.55 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[NIP7]] | -0.55 | -0.67 / -0.44 | both halves | 3e-05 |  |
| [[PURB]] | -0.54 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[ZC3H18]] | -0.54 | -0.54 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.5, -32.6); signed map (-50.7, 9.6). **Vector** length 102, 46.4% of its response variance represented; |z| ≥ 3 in 1,282 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *protein secretion* (hallmark, mean cos +0.51 to 10); *COPI-dependent Golgi-to-ER retrograde traffic* (reactome, mean cos +0.53 to 9); *COPI-mediated anterograde transport* (reactome, mean cos +0.55 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.7 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +4.8 | -4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | -11.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.6 | -0.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.6 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.4 | -0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | -0.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -6.6 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.5 | -4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.4 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.2 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.6 | -2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -5.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | trafficking from ER to golgi regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.2 — chr3:100,709,295-100,748,964 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TF6, FLJ36137, SPG57 |
| Reactome | 9 pathways, smallest: COPII-mediated vesicle transport; Signaling by ALK fusions and activated point mutants; Signaling by ALK in cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92734](https://www.uniprot.org/uniprotkb/Q92734) (Protein TFG):

> Plays a role in the normal dynamic function of the endoplasmic reticulum (ER) and its associated microtubules. Required for secretory cargo traffic from the endoplasmic reticulum to the Golgi apparatus.

**Summary**, from NCBI Gene [10342](https://www.ncbi.nlm.nih.gov/gene/10342):

> There are several documented fusion oncoproteins encoded partially by this gene. This gene also participates in several oncogenic rearrangements resulting in anaplastic lymphoma and mixoid chondrosarcoma, and may play a role in the NF-kappaB pathway. Multiple transcript variants have been found for this gene. [provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:11758](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11758) · Entrez [10342](https://www.ncbi.nlm.nih.gov/gene/10342) · UniProt [Q92734](https://www.uniprot.org/uniprotkb/Q92734) · Ensembl [ENSG00000114354](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114354)

## Data

Gene col 3543: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3543); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3543, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3543]; `tensor/DDL_lfc|DDL_z.npy` [3543]; `embed/gene_vectors.npy` [3543]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3543 or target_col == 3543). Every well: [[TFG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
