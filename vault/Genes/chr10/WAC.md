---
symbol: "WAC"
type: "gene"
col: 1755
ensembl_id: "ENSG00000095787"
name: "WW domain containing adaptor with coiled-coil"
location: "10p12.1"
module: 130
arm: "+"
pooled_cpm: 376.29
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 12
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# WAC

*WW domain containing adaptor with coiled-coil* — 10p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.86× (z +19.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.426× (z -15.2, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.554× (z -11.0, q 1e-25, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DYRK1A]] (+0.73, fdr 7e-06), [[VAPA]] (+0.72, fdr 7e-06), [[RBM33]] (+0.64, fdr 7e-06); moves opposite to [[DPP9]] (-0.61, fdr 1e-04), [[ATAD3B]] (-0.55, fdr 4e-05), [[MPP3]] (-0.54, fdr 1e-04).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1755.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.86×** | +19.6 | 0e+00 | 48/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.59×** | +17.7 | 0e+00 | 48/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **5.09×** | +15.8 | 0e+00 | 48/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +13.6 | 4e-40 | 46/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.06×** | +13.4 | 7e-39 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.95×** | +12.4 | 2e-33 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.55×** | +12.3 | 6e-33 | 48/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +11.9 | 8e-31 | 44/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +10.0 | 7e-22 | 42/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.47×** | +7.1 | 8e-11 | 36/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.38×** | +5.9 | 2e-07 | 30/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.36×** | +5.7 | 5e-07 | 37/48 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +4.9 | 4e-05 | 30/48 (LoVo, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 4e-04 | 28/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.029 | 32/48 (NCI-H1573, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.034 | 23/49 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Verteporfin (drug)]] 5 µM |  | 1.18× | +3.0 | 0.092 | 18/49 (AN3 CA, SHP-77, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.35×** | +2.9 | 0.096 | 27/49 (NCI-H2030, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1755.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.426×** | -15.2 | 0e+00 | 43/44 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.477×** | -13.7 | 2e-40 | 48/49 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.554×** | -11.0 | 1e-25 | 48/48 (A549, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.586×** | -9.9 | 6e-21 | 46/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.563×** | -9.9 | 6e-21 | 44/45 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.643×** | -7.9 | 3e-13 | 47/47 (NCI-H2347, CHP-212, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.746×** | -7.7 | 1e-12 | 36/49 (A549, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.665×** | -7.6 | 3e-12 | 44/48 (A549, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.724×** | -5.9 | 2e-07 | 43/48 (SW 900, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.759×** | -5.1 | 2e-05 | 37/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.806×** | -4.0 | 0.003 | 29/48 (Panc 03.27, SW 900, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.819×** | -3.6 | 0.017 | 24/48 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.841× | -3.2 | 0.056 | 20/48 (LS 180, AsPC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.839× | -3.2 | 0.056 | 22/48 (HOP62, SW48, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.844× | -3.1 | 0.065 | 19/47 (SW 1271, A498, …) | top dose only |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.849× | -3.0 | 0.085 | 21/48 (A498, HOP62, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.850× | -3.0 | 0.085 | 17/48 (NCI-H1792, NCI-H1573, …) | two highest doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.850× | -3.0 | 0.085 | 16/48 (HOP62, C32, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.852× | -3.0 | 0.094 | 17/48 (hTERT-HPNE, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1755. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 333 | 12 (3 ⚠) | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.66× (z +25.7) | [[Panobinostat (drug)]] 0.5 µM 0.428× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 326 | 10 (2 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +18.3) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.530× (z -10.5) |
| [[SW480 (line)]] | alt | 385 | 10 (2 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.80× (z +25.2) | [[Dinaciclib (drug)]] 5 µM 0.260× (z -24.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.579× (z -10.3) |
| [[A549 (line)]] | wt | 424 | 7 (2 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +18.6) | [[Dinaciclib (drug)]] 5 µM 0.180× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.346× (z -13.7) |
| [[KATO III (line)]] | alt | 282 | 9 (2 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.83× (z +24.8) | [[Dinaciclib (drug)]] 5 µM 0.526× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.581× (z -8.6) |
| [[LoVo (line)]] | wt | 368 | 10 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.73× (z +29.3) | [[Dinaciclib (drug)]] 5 µM 0.452× (z -12.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 372 | 10 (4 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.16× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 510 | 9 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.44× (z +19.6) | [[Dinaciclib (drug)]] 5 µM 0.320× (z -14.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 223 | 12 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.21× (z +28.2) | — |
| [[SW 900 (line)]] | alt | 538 | 7 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.272× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.424× (z -11.0) |
| [[BT-474 (line)]] | alt | 400 | 10 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.10× (z +18.0) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.561× (z -9.2) ⚠ cell-cycle shift, explains ~99% of this change |
| [[HT-29 (line)]] | alt | 353 | 6 (2 ⚠) | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.91× (z +15.7) | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.465× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 435 | 8 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -11.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 418 | 5 (2 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +16.6) | [[Dinaciclib (drug)]] 5 µM 0.370× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.422× (z -11.0) |
| [[C-33 A (line)]] | alt | 385 | 9 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.477× (z -10.2) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 324 | 6 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.31× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.432× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.471× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 347 | 4 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.539× (z -9.2) |
| [[COLO 205 (line)]] | alt | 226 | 8 (2 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 5.57× (z +22.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.09× (z +19.2) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -12.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 371 | 7 (2 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +15.5) | [[Panobinostat (drug)]] 5 µM 0.490× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 251 | 8 (2 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 5.80× (z +20.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.73× (z +20.0) | [[Panobinostat (drug)]] 0.5 µM 0.467× (z -8.6) |
| [[RKO (line)]] | wt | 480 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.509× (z -9.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 385 | 7 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +16.6) | [[Dinaciclib (drug)]] 0.5 µM 0.531× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.553× (z -8.6) |
| [[H4 (line)]] | wt | 261 | 8 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +14.2) | — |
| [[HepG2_C3A (line)]] | wt | 500 | 6 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.528× (z -8.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.532× (z -8.7) |
| [[LS 180 (line)]] | wt | 437 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.86× (z +19.0) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -12.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 386 | 5 (1 ⚠) | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.62× (z +13.3) | [[Panobinostat (drug)]] 5 µM 0.448× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 479 | 6 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.88× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.436× (z -11.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 369 | 4 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -11.2) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A-172 (line)]] | wt | 345 | 2 (1 ⚠) | 5 (4 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.19× (z +10.6) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 3.50× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -13.9) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.616× (z -9.7) |
| [[A-427 (line)]] | wt | 315 | 6 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.12× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.516× (z -9.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 562 | 3 (1 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.05× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.391× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.535× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 348 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.370× (z -10.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 474 | 5 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.60× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -16.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 496 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.17× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.391× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 433 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -14.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 236 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +14.0) | — |
| [[HS-578T (line)]] | alt | 302 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +12.9) | — |
| [[NCI-H2030 (line)]] | alt | 602 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 437 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -15.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 305 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -12.2) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 753 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.69× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -9.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 475 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.01× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -11.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 390 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +17.4) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -10.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 506 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.305× (z -9.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 371 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.32× (z +8.6) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.355× (z -10.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 193 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +8.6) | — |
| [[SW 1088 (line)]] | alt | 301 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.14× (z +8.6) | — |
| [[NCI-H2122 (line)]] | alt | 489 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 435 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 312 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1755), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYRK1A]] | +0.73 | +0.79 / +0.67 | both halves | 7e-06 | STRING 442 |
| [[VAPA]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[RBM33]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[PUM1]] | +0.63 | +0.52 / +0.62 | both halves | 1e-05 | STRING 527 |
| [[PUM2]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 | STRING 605 |
| [[QKI]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[RAF1]] | +0.62 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[KDM6A]] | +0.62 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[HINT2]] | +0.62 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[CNOT4]] | +0.62 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[CHASERR]] | +0.61 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[GPBP1]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPP9]] | -0.61 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[ATAD3B]] | -0.55 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[MPP3]] | -0.54 | -0.36 / -0.59 | both halves | 1e-04 |  |
| [[TPD52L2]] | -0.54 | -0.18 / -0.49 | ⚠ not reproduced | 0.001 |  |
| [[NOM1]] | -0.51 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[AP1M1]] | -0.51 | -0.29 / -0.47 | both halves | 3e-04 |  |
| [[EHD4]] | -0.51 | -0.36 / -0.38 | both halves | 9e-05 |  |
| [[BRD9]] | -0.50 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[RER1]] | -0.49 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[LRRC59]] | -0.49 | -0.37 / -0.37 | both halves | 8e-05 |  |
| [[ENTPD7]] | -0.49 | -0.18 / -0.51 | ⚠ one half (not replicated) | 9e-04 |  |
| [[GPSM1]] | -0.49 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[SLC25A44]] | -0.49 | -0.57 / -0.40 | both halves | 5e-05 |  |
| [[PPM1F]] | -0.49 | -0.23 / -0.48 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises WAC's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.604). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-17.7, 1.2); signed map (29.7, -24.0). **Vector** length 78.0, 36.8% of its response variance represented; |z| ≥ 3 in 1,544 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.8 | +11.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.2 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | -1.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | -0.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | +0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | -2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.2 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.1 | +0.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -5.1 | +13.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.2 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.9 | +4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | +1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.2 | +19.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -0.7 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -2.2 | -0.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | +12.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -1.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | WW domain containing adaptor with coiled-coil |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.1 — chr10:28,532,493-28,623,112 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Wwp4, FLJ31290, PRO1741, BM-016, MGC10753 |
| Reactome | 2 pathways, smallest: E3 ubiquitin ligases ubiquitinate target proteins; Protein ubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTA9](https://www.uniprot.org/uniprotkb/Q9BTA9) (WW domain-containing adapter protein with coiled-coil):

> Acts as a linker between gene transcription and histone H2B monoubiquitination at 'Lys-120' (H2BK120ub1). Interacts with the RNA polymerase II transcriptional machinery via its WW domain and with RNF20-RNF40 via its coiled coil region, thereby linking and regulating H2BK120ub1 and gene transcription. Regulates the cell-cycle checkpoint activation in response to DNA damage. Positive regulator of amino acid starvation-induced autophagy. Also acts as a negative regulator of basal autophagy. …

**Summary**, from NCBI Gene [51322](https://www.ncbi.nlm.nih.gov/gene/51322):

> The protein encoded by this gene contains a WW domain, which is a protein module found in a wide range of signaling proteins. This domain mediates protein-protein interactions and binds proteins containing short linear peptide motifs that are proline-rich or contain at least one proline. This gene product shares 94% sequence identity with the WAC protein in mouse, however, its exact function is not known. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec …

**Accessions** — [HGNC:17327](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17327) · Entrez [51322](https://www.ncbi.nlm.nih.gov/gene/51322) · UniProt [Q9BTA9](https://www.uniprot.org/uniprotkb/Q9BTA9) · Ensembl [ENSG00000095787](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095787)

## Data

Gene col 1755: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1755); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1755, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1755]; `tensor/DDL_lfc|DDL_z.npy` [1755]; `embed/gene_vectors.npy` [1755]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1755 or target_col == 1755). Every well: [[WAC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WAC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
