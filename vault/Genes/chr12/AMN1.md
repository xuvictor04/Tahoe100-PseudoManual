---
symbol: "AMN1"
type: "gene"
col: 7561
ensembl_id: "ENSG00000151743"
name: "antagonist of mitotic exit network 1 homolog"
location: "12p11.21"
module: 158
arm: "+"
pooled_cpm: 53.04
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 24
n_dd_up_clean: 17
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# AMN1

*antagonist of mitotic exit network 1 homolog* — 12p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.13× (z +16.5, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.512× (z -9.9, q 3e-20, down in 32 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.751× (z -5.5, q 9e-06, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KYAT1]] (+0.60, fdr 1e-05), [[TMSB10]] (+0.60, fdr 2e-05), [[B3GAT3]] (+0.59, fdr 2e-05); moves opposite to [[CTPS2]] (-0.60, fdr 2e-05), [[COPS3]] (-0.54, fdr 3e-05), [[PSMD11]] (-0.53, fdr 2e-05).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7561.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.13×** | +16.5 | 0e+00 | 45/46 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.36×** | +13.2 | 2e-37 | 42/46 (HepG2/C3A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.14×** | +11.7 | 2e-29 | 41/46 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.02×** | +10.8 | 4e-25 | 43/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.99×** | +10.6 | 3e-24 | 39/46 (HT-29, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.88×** | +9.7 | 2e-20 | 38/46 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.83×** | +9.3 | 9e-19 | 37/46 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.83×** | +9.2 | 3e-18 | 38/46 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +8.7 | 2e-16 | 39/46 (BT-474, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +7.8 | 3e-13 | 32/46 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.95×** | +5.4 | 4e-06 | 27/47 (LS 180, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.28×** | +5.3 | 5e-06 | 23/46 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +5.2 | 7e-06 | 26/46 (RKO, A498, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.39×** | +5.0 | 2e-05 | 25/45 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.71×** | +4.3 | 6e-04 | 24/46 (SHP-77, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.32×** | +4.2 | 1e-03 | 22/46 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7561.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.512×** | -9.9 | 3e-20 | 32/37 (SNU-423, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.643×** | -6.8 | 3e-09 | 31/45 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.751×** | -5.5 | 9e-06 | 27/46 (SHP-77, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.703×** | -5.2 | 3e-05 | 28/46 (BT-474, A549, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.727×** | -4.9 | 1e-04 | 26/47 (NCI-H2347, BT-474, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -4.5 | 6e-04 | 1/47 (NCI-H1792) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.740×** | -4.5 | 6e-04 | 27/45 (A549, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.788×** | -4.4 | 6e-04 | 19/47 (NCI-H1792, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.738×** | -4.3 | 1e-03 | 23/40 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.794×** | -4.3 | 1e-03 | 21/46 (KATO III, BT-474, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.773×** | -4.0 | 0.004 | 22/45 (A549, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.776×** | -3.9 | 0.004 | 17/46 (NCI-H460, KATO III, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.769×** | -3.8 | 0.006 | 20/46 (SNU-423, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.814×** | -3.7 | 0.008 | 23/47 (KATO III, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.05 µM |  | **0.787×** | -3.6 | 0.010 | 17/46 (SNU-423, AsPC-1, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.790×** | -3.5 | 0.017 | 19/46 (PANC-1, NCI-H1792, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.650×** | -3.5 | 0.017 | 19/45 (SHP-77, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.853× | -3.4 | 0.021 | 19/46 (SHP-77, AsPC-1, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | **0.797×** | -3.3 | 0.028 | 15/47 (NCI-H460, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7561. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 68.3 | 7 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 6.24× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 5.65× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -10.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 66.6 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.42× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -9.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 58.0 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.69× (z +22.8) | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -10.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 43.2 | 6 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.08× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.196× (z -15.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 41.1 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 6.07× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 85.6 | 3 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.51× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.112× (z -16.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 83.1 | 4 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.82× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -14.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 48.6 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.28× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.84× (z +10.4) | — |
| [[KATO III (line)]] | alt | 85.5 | 4 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.00× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.191× (z -13.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 43.1 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 3.52× (z +13.7) | — |
| [[NCI-H1792 (line)]] | alt | 52.6 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.75× (z +9.2) | [[venetoclax (drug)]] 5 µM 0.0278× (z -12.9) |
| [[PANC-1 (line)]] | alt | 93.9 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.06× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.449× (z -13.5) |
| [[SHP-77 (line)]] | alt | 121 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.04× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -11.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 100 | 2 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.78× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -12.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 61.6 | 3 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.29× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 39.3 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 2.80× (z +12.5) | — |
| [[COLO 205 (line)]] | alt | 23.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 113 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 33.8 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.78× (z +12.6) | — |
| [[RKO (line)]] | wt | 27.0 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 4.16× (z +12.2) | — |
| [[A549 (line)]] | wt | 85.4 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.74× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -9.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 39.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 40.5 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.98× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 71.3 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.69× (z +9.0) | — |
| [[A-172 (line)]] | wt | 31.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.46× (z +9.4) | — |
| [[A-427 (line)]] | wt | 49.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +13.5) | — |
| [[A498 (line)]] | wt | 25.1 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.69× (z +8.8) | — |
| [[J82 (line)]] | alt | 23.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.76× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 54.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.11× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 36.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.76× (z +11.7) | — |
| [[RPMI-7951 (line)]] | alt | 34.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.78× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 31.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.48× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 36.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.57× (z +11.6) | — |
| [[AN3 CA (line)]] | alt | 9.00 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 69.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7561), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KYAT1]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[TMSB10]] | +0.60 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[B3GAT3]] | +0.59 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[MYL12A]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[RGS17]] | +0.57 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[TPT1-AS1]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SYP]] | +0.56 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[BAIAP2L1]] | +0.55 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[SLC25A37]] | +0.55 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[AREG]] | +0.54 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[GOLT1A]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[CCK]] | +0.53 | +0.38 / +0.51 | both halves | 7e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTPS2]] | -0.60 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[COPS3]] | -0.54 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[PSMD11]] | -0.53 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[FARS2]] | -0.53 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[WDR46]] | -0.53 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[TARBP2]] | -0.53 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[GANC]] | -0.52 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[PSMC3]] | -0.52 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[HSPB8]] | -0.51 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[MRPL9]] | -0.51 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[TACO1]] | -0.51 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[CUL1]] | -0.50 | -0.51 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises AMN1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.326). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.2, 15.5); signed map (46.3, -13.2). **Vector** length 128, 40.2% of its response variance represented; |z| ≥ 3 in 1,496 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +13.4 | +16.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +11.1 | +10.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +6.6 | +13.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +8.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.8 | +9.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.5 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +5.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.8 | +0.4 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +2.6 | +0.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.4 | -1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.2 | -3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.8 | -5.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.5 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.3 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | antagonist of mitotic exit network 1 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.21 — chr12:31,671,142-31,729,121 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [Q8IY45](https://www.uniprot.org/uniprotkb/Q8IY45) carries no function annotation.

**Summary**, from NCBI Gene [196394](https://www.ncbi.nlm.nih.gov/gene/196394):

> Predicted to be involved in SCF-dependent proteasomal ubiquitin-dependent protein catabolic process. Predicted to be part of SCF ubiquitin ligase complex. Predicted to be active in microvillus membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27281](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27281) · Entrez [196394](https://www.ncbi.nlm.nih.gov/gene/196394) · UniProt [Q8IY45](https://www.uniprot.org/uniprotkb/Q8IY45) · Ensembl [ENSG00000151743](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151743)

## Data

Gene col 7561: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7561); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7561, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7561]; `tensor/DDL_lfc|DDL_z.npy` [7561]; `embed/gene_vectors.npy` [7561]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7561 or target_col == 7561). Every well: [[AMN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
