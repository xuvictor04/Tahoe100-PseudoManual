---
symbol: "MCTP1"
type: "gene"
col: 10614
ensembl_id: "ENSG00000175471"
name: "multiple C2 and transmembrane domain containing 1"
location: "5q15"
module: 92
arm: "+"
pooled_cpm: 187.93
n_lines_expressing: 37
n_dd_up: 32
n_dd_down: 40
n_dd_up_clean: 25
n_dd_down_clean: 34
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# MCTP1

*multiple C2 and transmembrane domain containing 1* — 5q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 4.28× (z +24.3, q 0e+00, up in 32 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (6 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.5 µM: 0.513× (z -13.3, q 7e-38, down in 30 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOCK4]] (+0.63, fdr 1e-05), [[DUSP6]] (+0.61, fdr 1e-05), [[TFPI2]] (+0.61, fdr 1e-05); moves opposite to [[PSMC2]] (-0.48, fdr 4e-05), [[SETD7]] (-0.48, fdr 6e-05), [[LRRC47]] (-0.47, fdr 3e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10614.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **4.28×** | +24.3 | 0e+00 | 32/35 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.61×** | +22.7 | 0e+00 | 33/35 (NCI-H2347, SW1417, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.70×** | +21.9 | 0e+00 | 33/35 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.12×** | +17.8 | 0e+00 | 23/35 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.78×** | +17.1 | 0e+00 | 27/35 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.62×** | +16.1 | 0e+00 | 31/35 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.59×** | +15.9 | 0e+00 | 32/35 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **7.79×** | +14.9 | 0e+00 | 32/36 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **2.10×** | +12.4 | 2e-33 | 25/35 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.98×** | +11.4 | 2e-28 | 32/36 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.95×** | +11.2 | 3e-27 | 27/35 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +10.0 | 5e-22 | 29/35 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +9.8 | 4e-21 | 24/34 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.79×** | +9.4 | 2e-19 | 25/35 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.67×** | +8.6 | 2e-16 | 24/35 (NCI-H2030, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.62×** | +8.1 | 2e-14 | 23/35 (A-172, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.94×** | +4.8 | 4e-05 | 18/35 (NCI-H460, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.31×** | +4.6 | 1e-04 | 16/35 (PANC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10614.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **0.513×** | -13.3 | 7e-38 | 30/35 (NCI-H1573, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.443×** | -13.2 | 1e-37 | 31/37 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.467×** | -12.2 | 6e-32 | 28/34 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.492×** | -11.4 | 9e-28 | 30/35 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.509×** | -11.2 | 3e-27 | 28/34 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.508×** | -11.1 | 2e-26 | 30/36 (C32, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.574×** | -11.0 | 3e-26 | 30/35 (C32, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.523×** | -10.8 | 3e-25 | 29/36 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.520×** | -10.0 | 6e-22 | 29/35 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.648×** | -9.6 | 3e-20 | 29/35 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.594×** | -8.7 | 3e-16 | 27/36 (RKO, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.694×** | -8.6 | 4e-16 | 23/36 (RKO, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.711×** | -6.9 | 2e-10 | 25/36 (C32, SHP-77, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.656×** | -6.7 | 7e-10 | 21/31 (NCI-H1573, A549, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.581×** | -6.7 | 9e-10 | 27/35 (C32, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.410×** | -6.4 | 5e-09 | 26/35 (NCI-H1573, A549, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.679×** | -5.9 | 9e-08 | 22/34 (C32, SHP-77, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10614. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 751 | 10 (1 ⚠) | 19 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.00× (z +18.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -22.5) |
| [[NCI-H460 (line)]] | wt | 307 | 13 (5 ⚠) | 16 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.29× (z +22.8) | [[Trametinib (drug)]] 0.5 µM 0.330× (z -15.4) |
| [[NCI-H23 (line)]] | alt | 266 | 7 (2 ⚠) | 19 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +12.7) | [[Adagrasib (drug)]] 0.05 µM 0.556× (z -21.1) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -20.8) |
| [[C32 (line)]] | wt | 298 | 6 (1 ⚠) | 18 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.39× (z +14.9) | [[Binimetinib (drug)]] 0.5 µM 0.184× (z -20.3) |
| [[A549 (line)]] | wt | 325 | 2 | 13 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +9.9) | [[Trametinib (drug)]] 0.5 µM 0.180× (z -20.2) |
| [[SW 900 (line)]] | alt | 203 | 9 (2 ⚠) | 6 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.70× (z +16.5) | [[Binimetinib (drug)]] 5 µM 0.295× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 173 | 10 (2 ⚠) | 4 | [[Tucidinostat (drug)]] 5 µM 2.18× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -13.0) |
| [[A-172 (line)]] | wt | 80.9 | 13 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.3× (z +27.2) | — |
| [[NCI-H2347 (line)]] | alt | 63.6 | 12 (3 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 5.10× (z +18.1) | [[Cobimetinib (drug)]] 0.5 µM 0.337× (z -8.6) |
| [[BT-474 (line)]] | alt | 63.9 | 9 (3 ⚠) | 3 | [[Digitoxin (drug)]] 0.5 µM 12.2× (z +14.0) | [[Trametinib (drug)]] 0.05 µM 0.223× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 274 | 5 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 0.5 µM 0.322× (z -10.5) |
| [[RKO (line)]] | wt | 1,048 | 3 | 8 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -23.1) |
| [[H4 (line)]] | wt | 190 | 10 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.24× (z +14.5) | — |
| [[J82 (line)]] | alt | 81.3 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.40× (z +17.6) | — |
| [[PANC-1 (line)]] | alt | 412 | 7 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.61× (z +15.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -23.1) |
| [[SHP-77 (line)]] | alt | 257 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -16.7) |
| [[SNU-423 (line)]] | alt | 157 | 5 (1 ⚠) | 5 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.90× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -10.5) |
| [[A498 (line)]] | wt | 147 | 7 (1 ⚠) | 2 | [[Panobinostat (drug)]] 5 µM 3.95× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 116 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +22.1) | — |
| [[HOP62 (line)]] | alt | 86.7 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +21.6) | [[Adagrasib (drug)]] 0.05 µM 0.597× (z -9.8) ⚠ position not correctable |
| [[HT-29 (line)]] | alt | 78.0 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +19.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 327 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.96× (z +13.2) | [[Adagrasib (drug)]] 0.05 µM 0.603× (z -16.0) ⚠ position not correctable |
| [[NCI-H1792 (line)]] | alt | 125 | 5 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.63× (z +13.3) | [[Adagrasib (drug)]] 0.05 µM 0.581× (z -14.6) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.262× (z -10.0) |
| [[A-427 (line)]] | wt | 62.2 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +20.7) | — |
| [[COLO 205 (line)]] | alt | 208 | 2 | 5 | [[Homoharringtonine (drug)]] 5 µM 6.10× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.167× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 528 | 5 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 88.8 | 5 | 2 | [[Tucidinostat (drug)]] 5 µM 3.33× (z +14.9) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.354× (z -8.8) |
| [[C-33 A (line)]] | alt | 417 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.198× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 162 | 2 | 4 | [[Tucidinostat (drug)]] 5 µM 2.08× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 118 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +11.9) | — |
| [[SW1417 (line)]] | alt | 115 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 3.21× (z +17.0) | — |
| [[SW480 (line)]] | alt | 51.3 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.33× (z +15.7) | — |
| [[NCI-H596 (line)]] | alt | 207 | 0 | 1 | — | [[Trametinib (drug)]] 5 µM 0.0662× (z -11.8) |
| [[SW 1271 (line)]] | alt | 382 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -10.8) |
| [[AN3 CA (line)]] | alt | 31.2 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 24.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 26.1 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 36.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 19.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 32.1 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 32.4 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 14.9 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 26.4 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 40.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 26.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10614), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOCK4]] | +0.63 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[TFPI2]] | +0.61 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ZFPM2-AS1]] | +0.59 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[MAP3K5]] | +0.59 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[TMEM251]] | +0.58 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[EGR1]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SPRY2]] | +0.57 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[ETV4]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[B4GALT6]] | +0.57 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[CSF2RA]] | +0.56 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[RGS17]] | +0.56 | +0.51 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMC2]] | -0.48 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[SETD7]] | -0.48 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[LRRC47]] | -0.47 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[NRBP1]] | -0.46 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[ARHGEF6]] | -0.46 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[NCOA2]] | -0.46 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises MCTP1's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 7.0% of all compounds | 0.030 | ⚠ off-target possible; 4 compounds |
| [[ANKRD29]] | B | ANKRD29 activity lowers MCTP1's level | lines that do not express ANKRD29 (19) vs lines expressing it (31) | 1.16× higher at baseline in the lines without ANKRD29 | 0.064 | ⚠ within organs, on part of the lines; also absent: NHS, PI3, GPR37 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.9, 7.0); signed map (8.3, 49.1). **Vector** length 138, 46.4% of its response variance represented; |z| ≥ 3 in 1,811 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MAPK output* (control, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +14.2 | +22.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +11.5 | +11.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.9 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.2 | -1.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +21.9 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +3.4 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +4.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.2 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.0 | +2.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -9.0 | -13.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -8.0 | -10.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.7 | -10.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.6 | -13.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -7.4 | -11.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -7.2 | -9.6 |

## What is on record

|  |  |
|---|---|
| Name | multiple C2 and transmembrane domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q15 — chr5:94,703,690-95,285,094 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22344 |
| Gene groups (HGNC) | Multiple C2 and transmembrane domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6DN14](https://www.uniprot.org/uniprotkb/Q6DN14) (Multiple C2 and transmembrane domain-containing protein 1):

> Calcium sensor which is essential for the stabilization of normal baseline neurotransmitter release and for the induction and long-term maintenance of presynaptic homeostatic plasticity.

**Summary**, from NCBI Gene [79772](https://www.ncbi.nlm.nih.gov/gene/79772):

> Enables calcium ion binding activity. Predicted to be involved in several processes, including modulation of chemical synaptic transmission; negative regulation of endocytosis; and negative regulation of response to oxidative stress. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26183](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26183) · Entrez [79772](https://www.ncbi.nlm.nih.gov/gene/79772) · UniProt [Q6DN14](https://www.uniprot.org/uniprotkb/Q6DN14) · Ensembl [ENSG00000175471](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175471)

## Data

Gene col 10614: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10614); `tables/drug_effects.parquet` (79 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10614, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10614]; `tensor/DDL_lfc|DDL_z.npy` [10614]; `embed/gene_vectors.npy` [10614]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10614 or target_col == 10614). Every well: [[MCTP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCTP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
