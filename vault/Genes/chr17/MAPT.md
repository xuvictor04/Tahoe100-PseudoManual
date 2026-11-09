---
symbol: "MAPT"
type: "gene"
col: 11865
ensembl_id: "ENSG00000186868"
name: "microtubule associated protein tau"
location: "17q21.31"
module: 100
arm: "+"
pooled_cpm: 35.95
n_lines_expressing: 40
n_dd_up: 10
n_dd_down: 29
n_dd_up_clean: 10
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 12
direction_downstream: 6
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# MAPT

*microtubule associated protein tau* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.97× (z +17.1, q 0e+00, up in 27 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.215× (z -38.7, q 0e+00, down in 37 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB6B]] (+0.73, fdr 7e-06), [[MAST1]] (+0.72, fdr 1e-05), [[PDZD7]] (+0.71, fdr 1e-05); moves opposite to [[ARMCX4]] (-0.69, fdr 1e-05), [[RFX3-DT]] (-0.62, fdr 6e-05), [[ERMAP]] (-0.61, fdr 4e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[DPYSL5]] → it (grade B ⚠); 6 go from it, the strongest it → [[STOX2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11865.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.97×** | +17.1 | 0e+00 | 27/38 (NCI-H2030, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.27×** | +14.6 | 1e-45 | 29/38 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.19×** | +13.9 | 7e-42 | 28/38 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.00×** | +12.4 | 5e-33 | 25/38 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.99×** | +12.3 | 1e-32 | 25/37 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.89×** | +11.3 | 1e-27 | 25/37 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +7.9 | 3e-13 | 25/37 (NCI-H2030, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.32×** | +7.8 | 3e-13 | 22/38 (NCI-H2030, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.47×** | +4.9 | 7e-05 | 13/38 (SK-MEL-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.042 | 9/38 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.12 | 3/37 (HEC-1-A, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11865.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.215×** | -38.7 | 0e+00 | 37/38 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.228×** | -26.3 | 0e+00 | 38/38 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.292×** | -21.9 | 0e+00 | 36/38 (BT-474, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.282×** | -21.7 | 0e+00 | 34/38 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.365×** | -17.9 | 0e+00 | 33/37 (BT-474, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.396×** | -16.5 | 0e+00 | 35/37 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.406×** | -16.0 | 0e+00 | 33/37 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.403×** | -15.5 | 0e+00 | 32/37 (MIA PaCa-2, SNU-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.476×** | -13.2 | 6e-38 | 31/38 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.633×** | -11.5 | 1e-28 | 23/38 (A-172, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.331×** | -10.3 | 4e-23 | 32/38 (A-172, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.575×** | -9.5 | 2e-19 | 24/37 (SNU-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.604×** | -9.0 | 1e-17 | 25/37 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.625×** | -8.3 | 3e-15 | 21/35 (A-172, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.626×** | -8.3 | 3e-15 | 27/37 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.632×** | -8.2 | 1e-14 | 28/38 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.438×** | -7.7 | 6e-13 | 23/37 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.665×** | -7.2 | 1e-11 | 21/37 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.679×** | -6.9 | 2e-10 | 23/38 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.689×** | -6.4 | 6e-09 | 23/37 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11865. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 142 | 0 | 21 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0512× (z -48.3) |
| [[MIA PaCa-2 (line)]] | alt | 114 | 0 | 21 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0972× (z -34.8) |
| [[NCI-H460 (line)]] | wt | 37.1 | 3 | 16 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.05× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -28.9) |
| [[HEC-1-A (line)]] | alt | 117 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -36.0) |
| [[NCI-H1792 (line)]] | alt | 45.4 | 0 | 15 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0881× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.0871× (z -18.6) |
| [[PANC-1 (line)]] | alt | 13.0 | 5 | 9 | [[Panobinostat (drug)]] 0.5 µM 3.97× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -15.2) |
| [[SNU-1 (line)]] | wt | 122 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -20.3) |
| [[A549 (line)]] | wt | 47.9 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0344× (z -28.4) |
| [[C32 (line)]] | wt | 40.5 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0972× (z -19.0) |
| [[BT-474 (line)]] | alt | 100 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -29.3) |
| [[NCI-H2030 (line)]] | alt | 26.3 | 2 | 7 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.55× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -18.4) |
| [[NCI-H23 (line)]] | alt | 58.0 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -24.6) |
| [[HOP62 (line)]] | alt | 18.0 | 3 | 5 | [[Tucidinostat (drug)]] 5 µM 2.88× (z +9.7) | [[Digitoxin (drug)]] 0.5 µM 0.153× (z -12.0) |
| [[SW 900 (line)]] | alt | 34.3 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -19.3) |
| [[LOX-IMVI (line)]] | wt | 25.7 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -17.9) |
| [[A-427 (line)]] | wt | 60.4 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -25.8) |
| [[LoVo (line)]] | wt | 42.4 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -26.5) |
| [[C-33 A (line)]] | alt | 189 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.369× (z -12.4) |
| [[H4 (line)]] | wt | 27.7 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0743× (z -13.1) |
| [[SW480 (line)]] | alt | 26.9 | 1 | 4 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.27× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -10.0) |
| [[AN3 CA (line)]] | alt | 121 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0937× (z -21.2) |
| [[NCI-H1573 (line)]] | alt | 10.3 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 3.72× (z +9.4) | — |
| [[A498 (line)]] | wt | 13.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0273× (z -26.4) |
| [[hTERT-HPNE (line)]] | wt | 15.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -12.5) |
| [[J82 (line)]] | alt | 27.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.2) |
| [[NCI-H2347 (line)]] | alt | 15.2 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.72× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -14.8) |
| [[HCT15 (line)]] | alt | 26.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -10.6) |
| [[HS-578T (line)]] | alt | 14.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.164× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 34.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -15.7) |
| [[HT-29 (line)]] | alt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -8.9) |
| [[NCI-H661 (line)]] | alt | 39.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0549× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 9.34 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -11.1) |
| [[SW 1271 (line)]] | alt | 48.5 | 0 | 1 | — | [[Vismodegib (drug)]] 0.05 µM 0.0628× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 7.18 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.72 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.17 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.53 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.27 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11865), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB6B]] | +0.73 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[MAST1]] | +0.72 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[PDZD7]] | +0.71 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[WASF3]] | +0.70 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[UBE2O]] | +0.67 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[SH3GL3]] | +0.66 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[SLC29A4]] | +0.66 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[STK32C]] | +0.65 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[GPR155]] | +0.65 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[ANKRD27]] | +0.65 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[VKORC1]] | +0.64 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ARID3A]] | +0.64 | +0.58 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMCX4]] | -0.69 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[RFX3-DT]] | -0.62 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[ERMAP]] | -0.61 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[DECR1]] | -0.61 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[WARS2-AS1]] | -0.61 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[ST7L]] | -0.59 | -0.51 / -0.43 | both halves | 4e-05 |  |
| [[DPH5-DT]] | -0.59 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[AVEN]] | -0.59 | -0.48 / -0.37 | both halves | 8e-05 | pathway: Apoptosis |
| [[RIPK2-DT]] | -0.59 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[CDKN2B-AS1]] | -0.58 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[RGS5]] | -0.58 | -0.56 / -0.37 | both halves | 7e-05 |  |
| [[PARVA]] | -0.58 | -0.49 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPYSL5]] | B | DPYSL5 activity raises MAPT's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.82× lower at baseline in the lines without DPYSL5 | 0.006 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[KIF1A]] | B | KIF1A activity raises MAPT's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 3.15× lower at baseline in the lines without KIF1A | 0.038 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[KIF26A]] | B | KIF26A activity raises MAPT's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 2.80× lower at baseline in the lines without KIF26A | 0.039 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[LHX2]] | B | LHX2 activity raises MAPT's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 3.11× lower at baseline in the lines without LHX2 | 0.053 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR |
| [[STOX2]] | B | STOX2 activity raises MAPT's level | lines that do not express STOX2 (22) vs lines expressing it (28) | 2.18× lower at baseline in the lines without STOX2 | 0.054 | ⚠ within organs, on part of the lines; also absent: SLC47A1, RBM11, FBXO27 |
| [[KCNK13]] | B | KCNK13 activity raises MAPT's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 4.73× lower at baseline in the lines without KCNK13 | 0.055 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers MAPT's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers MAPT's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAP3K15]] | B | MAP3K15 activity raises MAPT's level | lines that do not express MAP3K15 (19) vs lines expressing it (31) | 2.60× lower at baseline in the lines without MAP3K15 | 0.073 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| [[LMX1B]] | B | LMX1B activity raises MAPT's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 3.19× lower at baseline in the lines without LMX1B | 0.076 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[CECR2]] | B | CECR2 activity raises MAPT's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 2.69× lower at baseline in the lines without CECR2 | 0.091 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent |
| [[FAM124A]] | C | FAM124A activity raises MAPT's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 3.83× lower at baseline in the lines without FAM124A | 0.076 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STOX2]] | B | MAPT activity raises STOX2's level | lines that do not express MAPT (10) vs lines expressing it (40) | 5.07× lower at baseline in the lines without MAPT | 0.023 | ⚠ within organs, on part of the lines; also absent: MYH10, HHIPL2, TRPC1 |
| [[SMAP1]] | B | MAPT activity raises SMAP1's level | lines that do not express MAPT (10) vs lines expressing it (40) | 1.32× lower at baseline in the lines without MAPT | 0.026 | ⚠ within organs, on part of the lines; also absent: MYH10, HHIPL2, TRPC1 |
| [[LMX1B]] | B | MAPT activity raises LMX1B's level | lines that do not express MAPT (10) vs lines expressing it (40) | 3.09× lower at baseline in the lines without MAPT | 0.064 | ⚠ within organs, on part of the lines; also absent: MYH10, HHIPL2, TRPC1 |
| [[TCF7L1]] | C | MAPT activity raises TCF7L1's level | lines that do not express MAPT (10) vs lines expressing it (40) | 4.93× lower at baseline in the lines without MAPT | 0.011 | ⚠ within organs, on part of the lines; also absent: MYH10, HHIPL2, TRPC1; co-absent with the target |
| [[FAM124A]] | C | MAPT activity raises FAM124A's level | lines that do not express MAPT (10) vs lines expressing it (40) | 2.74× lower at baseline in the lines without MAPT | 0.068 | ⚠ within organs, on part of the lines; also absent: MYH10, HHIPL2, TRPC1; co-absent with the target |
| [[RASGEF1C]] | C | MAPT activity raises RASGEF1C's level | lines that do not express MAPT (10) vs lines expressing it (40) | 2.73× lower at baseline in the lines without MAPT | 0.083 | ⚠ within organs, on part of the lines; also absent: MYH10, HHIPL2, TRPC1; co-absent with the target |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.9, -1.7); signed map (-28.4, 22.5). **Vector** length 115, 34.4% of its response variance represented; |z| ≥ 3 in 1,219 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +17.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.7 | +14.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +11.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +6.8 | +7.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.1 | +12.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.6 | +7.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +3.0 | +4.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -26.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.9 | -11.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -4.7 | -9.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.4 | -13.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -21.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.9 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -6.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.1 | -2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated protein tau |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:45,894,527-46,028,334 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MTBT1, tau, PPND, FTDP-17, TAU, MSTD, MTBT2, FLJ31424; previously DDPAC, MAPTL |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 15 pathways, smallest: Caspase-mediated cleavage of cytoskeletal proteins; Activation of AMPK downstream of NMDARs; Apoptotic cleavage of cellular proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P10636](https://www.uniprot.org/uniprotkb/P10636) (Microtubule-associated protein tau):

> Promotes microtubule assembly and stability, and might be involved in the establishment and maintenance of neuronal polarity. The C-terminus binds axonal microtubules while the N-terminus binds neural plasma membrane components, suggesting that tau functions as a linker protein between both. Axonal polarity is predetermined by TAU/MAPT localization (in the neuronal cell) in the domain of the cell body defined by the centrosome. The short isoforms allow plasticity of the cytoskeleton whereas the …

**Summary**, from NCBI Gene [4137](https://www.ncbi.nlm.nih.gov/gene/4137):

> This gene encodes the microtubule-associated protein tau (MAPT) whose transcript undergoes complex, regulated alternative splicing, giving rise to several mRNA species. MAPT transcripts are differentially expressed in the nervous system, depending on stage of neuronal maturation and neuron type. MAPT gene mutations have been associated with several neurodegenerative disorders such as Alzheimer's disease, Pick's disease, frontotemporal dementia, cortico-basal degeneration and progressive …

**Accessions** — [HGNC:6893](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6893) · Entrez [4137](https://www.ncbi.nlm.nih.gov/gene/4137) · UniProt [P10636](https://www.uniprot.org/uniprotkb/P10636) · Ensembl [ENSG00000186868](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186868)

## Data

Gene col 11865: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11865); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11865, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11865]; `tensor/DDL_lfc|DDL_z.npy` [11865]; `embed/gene_vectors.npy` [11865]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11865 or target_col == 11865). Every well: [[MAPT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
