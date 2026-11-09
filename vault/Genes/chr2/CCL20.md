---
symbol: "CCL20"
type: "gene"
col: 3613
ensembl_id: "ENSG00000115009"
name: "C-C motif chemokine ligand 20"
location: "2q36.3"
module: 113
arm: "+"
pooled_cpm: 31.91
n_lines_expressing: 34
n_dd_up: 30
n_dd_down: 10
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 7
direction_downstream: 33
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# CCL20

*C-C motif chemokine ligand 20* — 2q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 11.1× (z +23.7, q 0e+00, up in 31 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.811× (z -5.2, q 9e-05, down in 18 of 32 measured lines) ⚠ position not correctable. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.489× (z -5.0, q 1e-04, down in 24 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BIRC3]] (+0.74, fdr 7e-06), [[EBI3]] (+0.72, fdr 7e-06), [[CEBPB]] (+0.67, fdr 7e-06); moves opposite to [[GFM2]] (-0.52, fdr 1e-05), [[BABAM1]] (-0.51, fdr 2e-05), [[STX16]] (-0.50, fdr 1e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TGFBR2]] → it (grade B ⚠); 33 go from it, the strongest it → [[UGCG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3613.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **11.1×** | +23.7 | 0e+00 | 31/32 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **17.9×** | +19.3 | 0e+00 | 30/31 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **3.92×** | +13.5 | 5e-39 | 29/32 (A498, HT-29, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.55×** | +10.5 | 8e-24 | 21/31 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **4.40×** | +10.3 | 7e-23 | 28/30 (AsPC-1, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.99×** | +9.4 | 8e-19 | 25/31 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **3.58×** | +8.9 | 5e-17 | 25/31 (AsPC-1, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.12×** | +7.9 | 2e-13 | 21/31 (A498, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.08×** | +7.8 | 3e-13 | 30/31 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **2.73×** | +6.8 | 7e-10 | 15/28 (NCI-H23, LS 180, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.73×** | +6.5 | 6e-09 | 16/26 (NCI-H460, A549, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.38×** | +6.0 | 8e-08 | 24/31 (AsPC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.19×** | +5.4 | 2e-06 | 20/31 (A549, A498, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **2.09×** | +5.1 | 1e-05 | 19/31 (AsPC-1, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.02×** | +4.8 | 7e-05 | 16/31 (CFPAC-1, AsPC-1, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.1 | 0.001 | 11/32 (AsPC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.84×** | +4.1 | 0.001 | 19/31 (CFPAC-1, Panc 03.27, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.71×** | +3.7 | 0.005 | 15/31 (CFPAC-1, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **1.67×** | +3.6 | 0.009 | 15/31 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.69×** | +3.5 | 0.010 | 12/31 (NCI-H23, A-427, …) | inconsistent across doses | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.013 | 17/32 (A498, J82, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.63×** | +3.3 | 0.023 | 15/31 (NCI-H1792, KATO III, …) | top dose only |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +2.9 | 0.063 | 14/31 (CFPAC-1, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3613.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.811×** | -5.2 | 9e-05 | 18/32 (NCI-H1792, NCI-H23, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.489×** | -5.0 | 1e-04 | 24/31 (A498, SW 900, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.490×** | -5.0 | 1e-04 | 22/31 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.498×** | -4.6 | 5e-04 | 18/32 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.592×** | -3.7 | 0.028 | 19/31 (KATO III, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.575×** | -3.6 | 0.032 | 13/31 (HepG2/C3A, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 5 µM |  | **0.382×** | -3.5 | 0.035 | 17/32 (HEC-1-A, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.709×** | -3.3 | 0.056 | 14/32 (SW480, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.611×** | -3.3 | 0.056 | 16/30 (HepG2/C3A, NCI-H1573, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **0.579×** | -3.1 | 0.099 | 16/32 (NCI-H1573, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, +0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3613. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.4 | 11 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +16.1) | — |
| [[AsPC-1 (line)]] | alt | 85.4 | 10 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 47.4× (z +28.2) | — |
| [[LOX-IMVI (line)]] | wt | 141 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -14.3) |
| [[A498 (line)]] | wt | 41.8 | 6 (3 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 22.9× (z +17.7) | [[Auranofin (drug)]] 5 µM 0.0470× (z -12.2) |
| [[A549 (line)]] | wt | 57.9 | 6 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.48× (z +15.6) | [[Ixazomib citrate (drug)]] 5 µM 0.172× (z -8.6) ⚠ cell-cycle shift, explains ~76% of this change |
| [[CFPAC-1 (line)]] | alt | 17.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 60.1× (z +25.2) | — |
| [[BT-474 (line)]] | alt | 17.3 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 87.6× (z +21.1) | — |
| [[HEC-1-A (line)]] | alt | 41.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +17.5) | — |
| [[HepG2_C3A (line)]] | wt | 570 | 4 (3 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 5.50× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.15× (z +10.0) | [[Cobimetinib (drug)]] 5 µM 0.215× (z -9.1) |
| [[J82 (line)]] | alt | 11.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 83.9× (z +19.8) | — |
| [[NCI-H2347 (line)]] | alt | 16.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +12.9) | — |
| [[SW 900 (line)]] | alt | 59.2 | 5 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 9.40× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 53.3 | 3 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 21.8× (z +13.0) | [[Adagrasib (drug)]] 0.05 µM 0.523× (z -9.6) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 18.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.6× (z +18.5) | — |
| [[SW1417 (line)]] | alt | 25.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.0× (z +17.5) | — |
| [[HOP62 (line)]] | alt | 8.37 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 33.4× (z +17.9) | — |
| [[HT-29 (line)]] | alt | 22.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +17.8) | — |
| [[hTERT-HPNE (line)]] | wt | 12.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 126× (z +16.7) | — |
| [[LS 180 (line)]] | wt | 12.8 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 66.7× (z +13.8) | — |
| [[NCI-H1792 (line)]] | alt | 61.5 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 17.6× (z +11.2) | [[Adagrasib (drug)]] 0.05 µM 0.403× (z -12.5) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 84.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 71.0 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.479× (z -11.5) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -10.4) |
| [[SNU-423 (line)]] | alt | 8.32 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.5× (z +15.8) | — |
| [[SW480 (line)]] | alt | 9.68 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 7.35× (z +12.1) | — |
| [[COLO 205 (line)]] | alt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 8.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.55× (z +8.7) | — |
| [[KATO III (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 8.47 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 28.8× (z +8.5) | — |
| [[A-172 (line)]] | wt | 6.32 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.41 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.06 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.04 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.71 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.84 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.15 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.05 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.33 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.15 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.98 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.81 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3613), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BIRC3]] | +0.74 | +0.72 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP; STRING 576 |
| [[EBI3]] | +0.72 | +0.69 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[CEBPB]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[MT1A]] | +0.67 | +0.47 / +0.72 | both halves | 2e-05 |  |
| [[MT2A]] | +0.66 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[CSF3]] | +0.65 | +0.60 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 799 |
| [[MT1E]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[TNFAIP3]] | +0.63 | +0.58 / +0.62 | both halves | 8e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP; STRING 698 |
| [[MT1M]] | +0.62 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[SAA1]] | +0.59 | +0.45 / +0.64 | both halves | 3e-05 | pathway: Class A/1 (Rhodopsin-like receptors); STRING 579 |
| [[IRAK2]] | +0.57 | +0.46 / +0.55 | both halves | 3e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 458 |
| [[MT1X]] | +0.57 | +0.49 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GFM2]] | -0.52 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[BABAM1]] | -0.51 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[STX16]] | -0.50 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[GDAP2]] | -0.49 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[UBFD1]] | -0.47 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[MFN2]] | -0.47 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[GHITM]] | -0.46 | -0.35 / -0.49 | both halves | 1e-04 | STRING 491 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGFBR2]] | B | TGFBR2 activity raises CCL20's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 2.77× lower at baseline in the lines without TGFBR2 | 0.031 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[SLPI]] | B | SLPI activity raises CCL20's level | lines that do not express SLPI (25) vs lines expressing it (25) | 1.52× lower at baseline in the lines without SLPI | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, CYP4F3, P2RY2 |
| [[KLF5]] | B | KLF5 activity raises CCL20's level | lines that do not express KLF5 (18) vs lines expressing it (32) | 2.39× lower at baseline in the lines without KLF5 | 0.045 | ⚠ within organs, on part of the lines; also absent: LAMA3, IFNLR1, NCMAP; maybe low, not absent |
| [[ZC3H12A]] | B | ZC3H12A activity raises CCL20's level | lines that do not express ZC3H12A (5) vs lines expressing it (45) | 2.45× lower at baseline in the lines without ZC3H12A | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[NEDD9]] | B | NEDD9 activity strengthens CCL20's drug response | lines that do not express NEDD9 (6) vs lines expressing it (26) | the lines without NEDD9 respond 0.53× as strongly (z diff +2.23); strongest at Homoharringtonine 5 µM: 3.45x vs 14x (z diff +4.6) | 0.091 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG; target measured in part of the lines; artifact flags |
| [[CXCL2]] | C | CXCL2 activity raises CCL20's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 2.67× lower at baseline in the lines without CXCL2 | 0.054 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3; co-absent with the target |
| [[YBX3]] | C | YBX3 activity raises CCL20's level | lines that do not express YBX3 (4) vs lines expressing it (46) | 3.19× lower at baseline in the lines without YBX3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPATA13, RNF103-CHMP3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 30, C 3. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UGCG]] | B | CCL20 activity raises UGCG's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 1.94× lower at baseline in the lines without CCL20 | 0.002 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[ZC3H12A]] | B | CCL20 activity raises ZC3H12A's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 2.17× lower at baseline in the lines without CCL20 | 0.003 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[SDC4]] | B | CCL20 activity raises SDC4's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 2.79× lower at baseline in the lines without CCL20 | 0.003 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[TGFBR2]] | B | CCL20 activity raises TGFBR2's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 2.74× lower at baseline in the lines without CCL20 | 0.006 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[NEDD9]] | B | CCL20 activity raises NEDD9's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 3.40× lower at baseline in the lines without CCL20 | 0.007 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[SLPI]] | B | CCL20 activity raises SLPI's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 2.99× lower at baseline in the lines without CCL20 | 0.008 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[TNFAIP3]] | B | CCL20 activity raises TNFAIP3's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 2.18× lower at baseline in the lines without CCL20 | 0.014 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[ZC3H12A-DT]] | B | CCL20 activity raises ZC3H12A-DT's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 1.55× lower at baseline in the lines without CCL20 | 0.015 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[CEBPB]] | B | CCL20 activity raises CEBPB's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 1.85× lower at baseline in the lines without CCL20 | 0.025 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[TMEM265]] | B | CCL20 activity raises TMEM265's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 1.77× lower at baseline in the lines without CCL20 | 0.029 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[TRIB1]] | B | CCL20 activity raises TRIB1's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 1.92× lower at baseline in the lines without CCL20 | 0.031 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[FAM227A]] | B | CCL20 activity lowers FAM227A's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 1.48× higher at baseline in the lines without CCL20 | 0.035 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (27.0, 9.8); signed map (13.3, 29.1). **Vector** length 112, 32.3% of its response variance represented; |z| ≥ 3 in 1,117 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Metallothioneins bind metals* (reactome, mean cos +0.62 to 5); *metallothionein* (control, mean cos +0.62 to 5); *Response to metal ions* (reactome, mean cos +0.62 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.1 | +13.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.7 | +7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +23.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.6 | +19.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.3 | +3.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.5 | +2.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.3 | +4.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.3 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.7 | -5.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | -4.0 | -1.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.8 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.7 | -1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | C-C motif chemokine ligand 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.3 — chr2:227,805,739-227,817,564 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LARC, MIP-3a, exodus-1, ST38, CKb4; previously SCYA20 |
| Gene groups (HGNC) | Chemokine ligands |
| Hallmark sets | INFLAMMATORY_RESPONSE, KRAS_SIGNALING_UP, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 10 pathways, smallest: Chemokine receptors bind chemokines; Interleukin-10 signaling; Peptide ligand-binding receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P78556](https://www.uniprot.org/uniprotkb/P78556) (C-C motif chemokine 20):

> Acts as a ligand for C-C chemokine receptor CCR6. Signals through binding and activation of CCR6 and induces a strong chemotactic response and mobilization of intracellular calcium ions. The ligand-receptor pair CCL20-CCR6 is responsible for the chemotaxis of dendritic cells (DC), effector/memory T-cells and B-cells and plays an important role at skin and mucosal surfaces under homeostatic and inflammatory conditions, as well as in pathology, including cancer and various autoimmune diseases. …

**Summary**, from NCBI Gene [6364](https://www.ncbi.nlm.nih.gov/gene/6364):

> This antimicrobial gene belongs to the subfamily of small cytokine CC genes. Cytokines are a family of secreted proteins involved in immunoregulatory and inflammatory processes. The CC cytokines are proteins characterized by two adjacent cysteines. The protein encoded by this gene displays chemotactic activity for lymphocytes and can repress proliferation of myeloid progenitors. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2014]

**Accessions** — [HGNC:10619](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10619) · Entrez [6364](https://www.ncbi.nlm.nih.gov/gene/6364) · UniProt [P78556](https://www.uniprot.org/uniprotkb/P78556) · Ensembl [ENSG00000115009](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115009)

## Data

Gene col 3613: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3613); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3613, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3613]; `tensor/DDL_lfc|DDL_z.npy` [3613]; `embed/gene_vectors.npy` [3613]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3613 or target_col == 3613). Every well: [[CCL20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCL20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
