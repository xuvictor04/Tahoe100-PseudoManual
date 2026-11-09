---
symbol: "CXCL8"
type: "gene"
col: 9805
ensembl_id: "ENSG00000169429"
name: "C-X-C motif chemokine ligand 8"
location: "4q13.3"
module: 112
arm: "+"
pooled_cpm: 329.86
n_lines_expressing: 30
n_dd_up: 37
n_dd_down: 40
n_dd_up_clean: 22
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 35
direction_downstream: 28
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# CXCL8

*C-X-C motif chemokine ligand 8* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 10.7× (z +28.9, q 0e+00, up in 28 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.340× (z -9.6, q 7e-19, down in 28 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFPI2]] (+0.75, fdr 7e-06), [[INHBA]] (+0.73, fdr 7e-06), [[IER3]] (+0.72, fdr 7e-06); moves opposite to [[ZDHHC7]] (-0.54, fdr 1e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 35 arrows point to it, the strongest [[DELEC1]] → it (grade B ⚠); 28 go from it, the strongest it → [[CXCL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9805.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **10.7×** | +28.9 | 0e+00 | 28/28 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **16.1×** | +23.8 | 0e+00 | 28/28 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.66×** | +16.9 | 0e+00 | 28/28 (hTERT-HPNE, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **5.36×** | +15.0 | 0e+00 | 27/28 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **4.97×** | +14.3 | 2e-44 | 26/28 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.10×** | +13.7 | 2e-40 | 28/28 (NCI-H2347, LS 180, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **4.17×** | +12.7 | 3e-35 | 27/28 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.05×** | +10.0 | 1e-21 | 27/29 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.91×** | +9.5 | 1e-19 | 27/28 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **2.96×** | +9.3 | 6e-19 | 25/27 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.63×** | +8.6 | 3e-16 | 26/28 (NCI-H460, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **10.4×** | +8.6 | 4e-16 | 26/29 (LoVo, BT-474, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.66×** | +8.1 | 3e-14 | 19/25 (LoVo, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **2.43×** | +7.9 | 8e-14 | 18/29 (LoVo, NCI-H460, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.24×** | +7.2 | 2e-11 | 22/28 (NCI-H460, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.07×** | +6.5 | 3e-09 | 20/28 (H4, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.97×** | +5.8 | 2e-07 | 24/27 (NCI-H1792, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.89×** | +5.7 | 3e-07 | 19/28 (H4, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **4.18×** | +5.3 | 4e-06 | 22/28 (BT-474, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.52×** | +5.1 | 9e-06 | 19/29 (CHP-212, NCI-H1792, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.80×** | +5.1 | 9e-06 | 21/28 (hTERT-HPNE, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.79×** | +4.9 | 2e-05 | 17/28 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +3.9 | 0.002 | 18/28 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 3 with an alert ⚠; shown: the 15 strongest. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9805.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.340×** | -9.6 | 7e-19 | 28/28 (HS-578T, H4, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.372×** | -8.0 | 4e-13 | 26/30 (NCI-H2030, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.396×** | -7.9 | 5e-13 | 27/28 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.481×** | -7.9 | 5e-13 | 25/28 (NCI-H2030, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.537×** | -7.6 | 2e-12 | 25/28 (NCI-H460, NCI-H2030, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.438×** | -7.0 | 2e-10 | 27/27 (NCI-H2030, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.470×** | -6.7 | 2e-09 | 23/29 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.471×** | -6.2 | 5e-08 | 24/28 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.537×** | -5.5 | 2e-06 | 23/28 (H4, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.541×** | -5.4 | 3e-06 | 25/28 (HS-578T, H4, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.617×** | -5.2 | 1e-05 | 18/28 (SK-MEL-2, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.561×** | -5.1 | 2e-05 | 21/27 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.572×** | -4.9 | 3e-05 | 22/28 (H4, SW 1088, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.573×** | -4.9 | 3e-05 | 24/28 (H4, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.678×** | -4.7 | 1e-04 | 20/28 (RPMI-7951, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.68 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9805. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 819 | 14 (7 ⚠) | 10 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 22.5× (z +19.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 16.2× (z +17.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.183× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 1,147 | 9 (5 ⚠) | 14 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 13.5× (z +17.0) | [[Adagrasib (drug)]] 0.05 µM 0.553× (z -13.8) ⚠ position not correctable · without an alert: [[Clobetasol propionate (drug)]] 5 µM 0.175× (z -11.9) |
| [[H4 (line)]] | wt | 1,080 | 3 | 19 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 7.08× (z +10.7) | [[Clobetasol propionate (drug)]] 5 µM 0.0485× (z -16.5) |
| [[HS-578T (line)]] | alt | 1,231 | 5 | 13 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +21.2) | [[Ponatinib (drug)]] 5 µM 0.0477× (z -19.1) |
| [[NCI-H2030 (line)]] | alt | 570 | 5 (1 ⚠) | 9 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 17.4× (z +17.8) | [[Adagrasib (drug)]] 0.05 µM 0.498× (z -15.5) ⚠ position not correctable · without an alert: [[Ponatinib (drug)]] 5 µM 0.157× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 333 | 10 (4 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.18× (z +20.4) | [[Adagrasib (drug)]] 0.05 µM 0.409× (z -20.2) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.344× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 149 | 12 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 26.3× (z +27.1) | — |
| [[hTERT-HPNE (line)]] | wt | 751 | 10 (5 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 33.6× (z +26.9) | [[Ponatinib (drug)]] 5 µM 0.137× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 83.7 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 108× (z +36.7) | — |
| [[BT-474 (line)]] | alt | 149 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 52.2× (z +28.6) | — |
| [[HOP62 (line)]] | alt | 757 | 9 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 29.5× (z +22.1) | [[Adagrasib (drug)]] 0.05 µM 0.537× (z -10.3) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 835 | 6 (2 ⚠) | 4 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 26.0× (z +19.8) | [[Trametinib (drug)]] 5 µM 0.173× (z -9.7) |
| [[A498 (line)]] | wt | 952 | 5 | 4 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +12.0) | [[Ponatinib (drug)]] 5 µM 0.152× (z -11.0) |
| [[SNU-423 (line)]] | alt | 194 | 8 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 31.1× (z +30.3) | [[Ponatinib (drug)]] 5 µM 0.168× (z -11.4) |
| [[SW 900 (line)]] | alt | 930 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.05× (z +13.2) | — |
| [[J82 (line)]] | alt | 288 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 30.4× (z +27.7) | [[Ponatinib (drug)]] 5 µM 0.179× (z -10.1) |
| [[LoVo (line)]] | wt | 103 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 23.6× (z +25.1) | — |
| [[SK-MEL-2 (line)]] | alt | 408 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.69× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.0716× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.0853× (z -10.3) |
| [[A549 (line)]] | wt | 256 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 20.7× (z +23.2) | [[Ponatinib (drug)]] 5 µM 0.201× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 114 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 32.8× (z +26.2) | — |
| [[RPMI-7951 (line)]] | alt | 849 | 5 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 27.8× (z +15.6) | — |
| [[CFPAC-1 (line)]] | alt | 508 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.4× (z +31.8) | — |
| [[LS 180 (line)]] | wt | 90.2 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 21.1× (z +18.0) | — |
| [[SW 1271 (line)]] | alt | 272 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.0× (z +13.8) | — |
| [[LOX-IMVI (line)]] | wt | 296 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 195 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.07× (z +11.2) | — |
| [[SW 1088 (line)]] | alt | 831 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0322× (z -9.2) |
| [[A-172 (line)]] | wt | 63.8 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 18.3 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 50.9 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 28.7 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 64.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 90.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.1 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 36.5 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 73.3 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 37.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 76.4 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 80.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 321 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 56.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 327 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.5 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 37.1 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 30.7 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 66.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 27.4 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 34.5 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 38.0 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 47.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9805), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFPI2]] | +0.75 | +0.73 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[INHBA]] | +0.73 | +0.68 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[IER3]] | +0.72 | +0.66 / +0.74 | both halves | 7e-06 | STRING 554 |
| [[TRAF1]] | +0.71 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[IL1A]] | +0.71 | +0.62 / +0.75 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 974 |
| [[CSF2]] | +0.71 | +0.68 / +0.74 | both halves | 7e-06 | pathway: Interleukin-10 signaling; STRING 972 |
| [[LIF]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 731 |
| [[PTGS2]] | +0.70 | +0.63 / +0.75 | both halves | 7e-06 | pathway: Interleukin-10 signaling; STRING 975 |
| [[CXCL1]] | +0.67 | +0.62 / +0.73 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 957 |
| [[LINC00973]] | +0.67 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[BCL2A1]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 | STRING 508 |
| [[CD44]] | +0.65 | +0.58 / +0.65 | both halves | 8e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 751 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC7]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 19, C 16. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DELEC1]] | B | DELEC1 activity raises CXCL8's level | lines that do not express DELEC1 (6) vs lines expressing it (44) | 6.46× lower at baseline in the lines without DELEC1 | 0.005 | ⚠ within organs, on part of the lines; also absent: NDRG1, SLC2A1, ZHX2; maybe low, not absent |
| [[SOX9]] | B | SOX9 activity raises CXCL8's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 3.64× lower at baseline in the lines without SOX9 | 0.007 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[KIAA1217]] | B | KIAA1217 activity raises CXCL8's level | lines that do not express KIAA1217 (10) vs lines expressing it (40) | 3.55× lower at baseline in the lines without KIAA1217 | 0.022 | ⚠ within organs, on part of the lines; also absent: FAM107B, MET, S100A16 |
| [[IER3]] | B | IER3 activity raises CXCL8's level | lines that do not express IER3 (5) vs lines expressing it (45) | 6.79× lower at baseline in the lines without IER3 | 0.027 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[CXCL5]] | B | CXCL5 activity raises CXCL8's level | lines that do not express CXCL5 (35) vs lines expressing it (15) | 3.07× lower at baseline in the lines without CXCL5 | 0.029 | ⚠ within organs, on part of the lines; also absent: ANXA10, IRAK3, TRBC2 |
| [[SERPIND1]] | B | SERPIND1 activity raises CXCL8's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 2.29× lower at baseline in the lines without SERPIND1 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[DUSP10]] | B | DUSP10 activity raises CXCL8's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 4.88× lower at baseline in the lines without DUSP10 | 0.035 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[SH2D2A]] | B | SH2D2A activity raises CXCL8's level | lines that do not express SH2D2A (20) vs lines expressing it (30) | 2.28× lower at baseline in the lines without SH2D2A | 0.035 | ⚠ within organs, on part of the lines; also absent: IL1R2, SLC17A9, MT1G; maybe low, not absent |
| [[TSC22D3]] | B | TSC22D3 activity raises CXCL8's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 4.19× lower at baseline in the lines without TSC22D3 | 0.037 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[GEM]] | B | GEM activity raises CXCL8's level | lines that do not express GEM (9) vs lines expressing it (41) | 4.16× lower at baseline in the lines without GEM | 0.041 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[GPR39]] | B | GPR39 activity raises CXCL8's level | lines that do not express GPR39 (11) vs lines expressing it (39) | 2.88× lower at baseline in the lines without GPR39 | 0.052 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[CD44]] | B | CD44 activity raises CXCL8's level | lines that do not express CD44 (15) vs lines expressing it (35) | 3.50× lower at baseline in the lines without CD44 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 20, C 8. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL1]] | B | CXCL8 activity raises CXCL1's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 3.15× lower at baseline in the lines without CXCL8 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[TSC22D3]] | B | CXCL8 activity raises TSC22D3's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 2.70× lower at baseline in the lines without CXCL8 | 0.008 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[GEM]] | B | CXCL8 activity raises GEM's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 2.65× lower at baseline in the lines without CXCL8 | 0.010 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[SHB]] | B | CXCL8 activity raises SHB's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 1.62× lower at baseline in the lines without CXCL8 | 0.012 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[BACH1]] | B | CXCL8 activity raises BACH1's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 1.72× lower at baseline in the lines without CXCL8 | 0.015 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[DUSP10]] | B | CXCL8 activity raises DUSP10's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 2.99× lower at baseline in the lines without CXCL8 | 0.026 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[C3orf52]] | B | CXCL8 activity raises C3orf52's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 1.84× lower at baseline in the lines without CXCL8 | 0.027 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[CSRNP1]] | B | CXCL8 activity raises CSRNP1's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 1.48× lower at baseline in the lines without CXCL8 | 0.041 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[KIAA1217]] | B | CXCL8 activity raises KIAA1217's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 2.20× lower at baseline in the lines without CXCL8 | 0.047 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[IRAK2]] | B | CXCL8 activity raises IRAK2's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 2.38× lower at baseline in the lines without CXCL8 | 0.049 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[SOX9]] | B | CXCL8 activity raises SOX9's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 1.53× lower at baseline in the lines without CXCL8 | 0.049 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[CD44]] | B | CXCL8 activity raises CD44's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 3.59× lower at baseline in the lines without CXCL8 | 0.060 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.820). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.3, 1.6); signed map (16.0, 44.3). **Vector** length 128, 42.5% of its response variance represented; |z| ≥ 3 in 1,545 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.65 to 11); *KRAS signaling up* (hallmark, mean cos +0.64 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +12.2 | +13.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +10.3 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | +8.2 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +7.8 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | +7.8 | +7.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.2 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.8 | +5.8 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -5.4 | -4.3 |
|  | [[NG25 (drug)]] 5 µM |  | -5.1 | -4.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.9 | -4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.7 | -9.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.6 | -4.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | C-X-C motif chemokine ligand 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:73,740,519-73,743,716 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SCYB8, LUCT, LECT, MDNCF, TSG-1, IL-8, NAP-1, 3-10C; previously IL8 |
| Gene groups (HGNC) | Chemokine ligands; Interleukins |
| Hallmark sets | INFLAMMATORY_RESPONSE, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 22 pathways, smallest: NFE2L2 regulating inflammation associated genes; Chemokine receptors bind chemokines; ATF4 activates genes in response to endoplasmic reticulum  stress |
| Matched by | ensembl_id |

**Function**, from UniProt [P10145](https://www.uniprot.org/uniprotkb/P10145) (Interleukin-8):

> Chemotactic factor that mediates inflammatory response by attracting neutrophils, basophils, and T-cells to clear pathogens and protect the host from infection. Also plays an important role in neutrophil activation. Released in response to an inflammatory stimulus, exerts its effect by binding to the G protein-coupled receptors CXCR1 and CXCR2, primarily found in neutrophils, monocytes and endothelial cells. G protein heterotrimer (alpha, beta, gamma subunits) constitutively binds to …

**Summary**, from NCBI Gene [3576](https://www.ncbi.nlm.nih.gov/gene/3576):

> The protein encoded by this gene is a member of the CXC chemokine family and is a major mediator of the inflammatory response. The encoded protein is commonly referred to as interleukin-8 (IL-8). IL-8 is secreted by mononuclear macrophages, neutrophils, eosinophils, T lymphocytes, epithelial cells, and fibroblasts. It functions as a chemotactic factor by guiding the neutrophils to the site of infection. Bacterial and viral products rapidly induce IL-8 expression. IL-8 also participates with …

**Accessions** — [HGNC:6025](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6025) · Entrez [3576](https://www.ncbi.nlm.nih.gov/gene/3576) · UniProt [P10145](https://www.uniprot.org/uniprotkb/P10145) · Ensembl [ENSG00000169429](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169429)

## Data

Gene col 9805: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9805); `tables/drug_effects.parquet` (78 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9805, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9805]; `tensor/DDL_lfc|DDL_z.npy` [9805]; `embed/gene_vectors.npy` [9805]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9805 or target_col == 9805). Every well: [[CXCL8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CXCL8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
