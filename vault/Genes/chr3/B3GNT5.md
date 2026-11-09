---
symbol: "B3GNT5"
type: "gene"
col: 10734
ensembl_id: "ENSG00000176597"
name: "UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 5"
location: "3q27.1"
module: 98
arm: "+"
pooled_cpm: 59.81
n_lines_expressing: 43
n_dd_up: 53
n_dd_down: 27
n_dd_up_clean: 46
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# B3GNT5

*UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 5* — 3q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 53 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.43× (z +20.1, q 0e+00, up in 35 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.310× (z -19.4, q 0e+00, down in 41 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAMTS9]] (+0.67, fdr 7e-06), [[STXBP5-AS1]] (+0.66, fdr 7e-06), [[MAFB]] (+0.66, fdr 1e-05); moves opposite to [[USP48]] (-0.51, fdr 6e-05), [[TP53BP1]] (-0.47, fdr 3e-05), [[CDON]] (-0.46, fdr 2e-04).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SGPP2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ABLIM3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 70 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 53 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10734.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +20.1 | 0e+00 | 35/42 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.73×** | +9.1 | 4e-17 | 24/40 (RPMI-7951, Panc 03.27, …) | all doses, flat |  |
| [[Econazole (drug)]] 5 µM |  | **1.71×** | +8.9 | 1e-16 | 24/41 (HOP62, SW 900, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.68×** | +8.5 | 2e-15 | 25/41 (AsPC-1, A498, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +8.3 | 8e-15 | 26/41 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.65×** | +8.2 | 1e-14 | 25/41 (Panc 03.27, HOP62, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.43×** | +8.2 | 1e-14 | 22/41 (HOP62, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +8.0 | 8e-14 | 25/41 (HOP62, A498, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +7.8 | 5e-13 | 28/41 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dexamethasone (drug)]] 5 µM |  | **1.58×** | +7.6 | 2e-12 | 23/41 (A498, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.57×** | +7.5 | 3e-12 | 25/41 (A498, CFPAC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +7.4 | 7e-12 | 23/40 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.54×** | +7.2 | 4e-11 | 24/41 (A498, CFPAC-1, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.52×** | +7.0 | 1e-10 | 23/41 (RPMI-7951, SHP-77, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.50×** | +6.7 | 9e-10 | 23/41 (A498, Panc 03.27, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.52×** | +6.7 | 9e-10 | 23/42 (A498, HOP62, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10734.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.310×** | -19.4 | 0e+00 | 41/41 (AsPC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.357×** | -17.0 | 0e+00 | 39/41 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.466×** | -12.6 | 3e-34 | 36/41 (AsPC-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.670×** | -6.6 | 5e-09 | 27/41 (COLO 205, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.665×** | -6.5 | 9e-09 | 21/33 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.763×** | -5.7 | 1e-06 | 20/41 (NCI-H23, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.708×** | -5.5 | 3e-06 | 22/40 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.726×** | -5.2 | 1e-05 | 23/43 (NCI-H23, A-427, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.731×** | -5.2 | 1e-05 | 23/40 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.715×** | -5.1 | 2e-05 | 22/41 (NCI-H23, NCI-H2347, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **0.810×** | -4.8 | 8e-05 | 19/41 (NCI-H23, HT-29, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.800×** | -4.8 | 9e-05 | 21/41 (NCI-H23, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.787×** | -4.6 | 2e-04 | 19/42 (NCI-H23, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.751×** | -4.6 | 2e-04 | 18/40 (NCI-H23, NCI-H1573, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.826×** | -4.4 | 4e-04 | 19/42 (NCI-H2347, SHP-77, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.768×** | -4.4 | 4e-04 | 19/40 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.828×** | -4.3 | 5e-04 | 18/41 (NCI-H23, PANC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10734. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 76.2 | 6 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +14.3) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.47× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -13.6) |
| [[AsPC-1 (line)]] | alt | 151 | 6 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +13.4) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.80× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.163× (z -15.5) |
| [[NCI-H460 (line)]] | wt | 37.2 | 8 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +13.3) | — |
| [[A-172 (line)]] | wt | 40.3 | 3 (2 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.94× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.208× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 29.7 | 0 | 6 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.426× (z -16.6) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.187× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 134 | 2 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.243× (z -12.0) |
| [[SW1417 (line)]] | alt | 85.0 | 3 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +14.6) | [[Panobinostat (drug)]] 5 µM 0.295× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 89.3 | 3 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +12.1) ⚠ cell-cycle shift, explains ~76% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.306× (z -11.3) |
| [[COLO 205 (line)]] | alt | 209 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.193× (z -12.8) |
| [[LoVo (line)]] | wt | 65.1 | 2 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -14.2) |
| [[LS 180 (line)]] | wt | 141 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -14.5) |
| [[SHP-77 (line)]] | alt | 94.0 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.262× (z -10.8) |
| [[SW480 (line)]] | alt | 50.8 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +15.8) | [[Panobinostat (drug)]] 5 µM 0.291× (z -14.5) |
| [[A549 (line)]] | wt | 59.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -13.1) |
| [[HOP62 (line)]] | alt | 24.9 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +13.2) | — |
| [[SNU-423 (line)]] | alt | 32.3 | 2 (1 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +14.4) | [[Panobinostat (drug)]] 5 µM 0.245× (z -10.5) |
| [[BT-474 (line)]] | alt | 31.6 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 107 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -14.4) |
| [[KATO III (line)]] | alt | 108 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 159 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 13.3× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.212× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 128 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.273× (z -12.9) |
| [[SW 900 (line)]] | alt | 40.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +12.1) | — |
| [[A-427 (line)]] | wt | 65.7 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.2) ⚠ cell-cycle shift, explains ~76% of this change | [[Panobinostat (drug)]] 5 µM 0.349× (z -9.7) |
| [[H4 (line)]] | wt | 40.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.20× (z +10.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -11.1) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HS-578T (line)]] | alt | 27.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +11.1) ⚠ cell-cycle shift, explains ~76% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 81.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 40.5 | 2 | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.96× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 48.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.355× (z -9.5) |
| [[RKO (line)]] | wt | 44.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.304× (z -9.8) |
| [[AN3 CA (line)]] | alt | 38.8 | 0 | 1 | — | [[Bexarotene (drug)]] 0.5 µM 0.113× (z -9.4) |
| [[C32 (line)]] | wt | 31.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +14.5) | — |
| [[CHP-212 (line)]] | wt | 30.6 | 0 | 1 | — | [[Cabozantinib (S-malate) (drug)]] 0.5 µM 0.0572× (z -10.2) |
| [[HCT15 (line)]] | alt | 59.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 27.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -9.8) |
| [[J82 (line)]] | alt | 17.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +12.4) | — |
| [[C-33 A (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.43 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.55 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.84 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.27 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10734), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTS9]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 | pathway: O-linked glycosylation |
| [[STXBP5-AS1]] | +0.66 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[MAFB]] | +0.66 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[TBXAS1]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[HS3ST3B1]] | +0.61 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[TOP1]] | +0.61 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[VSTM2L]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[IRX3]] | +0.60 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[FOXN2]] | +0.59 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ITGA10]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[FOXC2]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[LINC00607]] | +0.57 | +0.43 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP48]] | -0.51 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[TP53BP1]] | -0.47 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[CDON]] | -0.46 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[LRIG1]] | -0.45 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[EHMT2]] | -0.45 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[CBX1]] | -0.45 | -0.27 / -0.36 | both halves | 3e-04 |  |
| [[RPGRIP1L]] | -0.44 | -0.29 / -0.43 | both halves | 3e-04 |  |
| [[IFT172]] | -0.44 | -0.21 / -0.44 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SGPP2]] | B | SGPP2 activity raises B3GNT5's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 2.59× lower at baseline in the lines without SGPP2 | 0.050 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[THRB]] | B | THRB activity raises B3GNT5's level | lines that do not express THRB (21) vs lines expressing it (29) | 1.83× lower at baseline in the lines without THRB | 0.060 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SIDT1, P2RY2 |
| [[RTN4RL1]] | B | RTN4RL1 activity lowers B3GNT5's level | lines that do not express RTN4RL1 (14) vs lines expressing it (36) | 2.07× higher at baseline in the lines without RTN4RL1 | 0.063 | ⚠ within organs, on part of the lines; also absent: EFR3B, B4GALNT1, HS6ST3; maybe low, not absent |
| [[ADGRG2]] | B | ADGRG2 activity lowers B3GNT5's level | lines that do not express ADGRG2 (10) vs lines expressing it (40) | 2.19× higher at baseline in the lines without ADGRG2 | 0.065 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |
| [[ITGA10]] | B | ITGA10 activity lowers B3GNT5's level | lines that do not express ITGA10 (9) vs lines expressing it (41) | 2.35× higher at baseline in the lines without ITGA10 | 0.080 | ⚠ within organs, on part of the lines; also absent: SLC17A7, ZEB1, BOLA3-DT; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises B3GNT5's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[SLC26A2]] | C | SLC26A2 activity lowers B3GNT5's level | lines that do not express SLC26A2 (4) vs lines expressing it (46) | 2.53× higher at baseline in the lines without SLC26A2 | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR4435-2HG, EPB41L2, CEP85L; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABLIM3]] | B | B3GNT5 activity raises ABLIM3's level | lines that do not express B3GNT5 (7) vs lines expressing it (43) | 2.58× lower at baseline in the lines without B3GNT5 | 0.048 | ⚠ within organs, on part of the lines; also absent: MCF2L2, SOX4, RND3 |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.4, 15.0); signed map (16.9, 33.0). **Vector** length 130, 41.0% of its response variance represented; |z| ≥ 3 in 1,712 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +13.8 | +20.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +7.0 | +5.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +6.7 | +5.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +6.1 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +2.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +5.7 | +9.1 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.4 | -19.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.8 | -4.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -2.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.6 | -4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -17.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -3.0 | -4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:183,253,253-183,298,504 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B3GN-T5, beta3Gn-T5 |
| Gene groups (HGNC) | Beta 3-glycosyltransferases |
| Reactome | 6 pathways, smallest: Glycosphingolipid biosynthesis; Glycosphingolipid metabolism; O-linked glycosylation of mucins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BYG0](https://www.uniprot.org/uniprotkb/Q9BYG0) (Lactosylceramide 1,3-N-acetyl-beta-D-glucosaminyltransferase):

> Beta-1,3-N-acetylglucosaminyltransferase that plays a key role in the synthesis of lacto- or neolacto-series carbohydrate chains on glycolipids, notably by participating in biosynthesis of HNK-1 and Lewis X carbohydrate structures. Has strong activity toward lactosylceramide (LacCer) and neolactotetraosylceramide (nLc(4)Cer; paragloboside), resulting in the synthesis of Lc(3)Cer and neolactopentaosylceramide (nLc(5)Cer), respectively. Probably plays a central role in regulating neolacto-series …

**Summary**, from NCBI Gene [84002](https://www.ncbi.nlm.nih.gov/gene/84002):

> This gene encodes a member of the beta-1,3-N-acetylglucosaminyltransferase family. This enzyme is a type II membrane protein. It exhibits strong activity to transfer GlcNAc to glycolipid substrates and is identified as the most likely candidate for lactotriaosylceramide synthase. This enzyme is essential for the expression of Lewis X epitopes on glycolipids. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15684](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15684) · Entrez [84002](https://www.ncbi.nlm.nih.gov/gene/84002) · UniProt [Q9BYG0](https://www.uniprot.org/uniprotkb/Q9BYG0) · Ensembl [ENSG00000176597](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176597)

## Data

Gene col 10734: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10734); `tables/drug_effects.parquet` (101 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10734, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10734]; `tensor/DDL_lfc|DDL_z.npy` [10734]; `embed/gene_vectors.npy` [10734]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10734 or target_col == 10734). Every well: [[B3GNT5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B3GNT5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
