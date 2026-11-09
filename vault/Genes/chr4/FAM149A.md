---
symbol: "FAM149A"
type: "gene"
col: 3083
ensembl_id: "ENSG00000109794"
name: "family with sequence similarity 149 member A"
location: "4q35.1"
module: 8
arm: "+"
pooled_cpm: 10.26
n_lines_expressing: 25
n_dd_up: 38
n_dd_down: 10
n_dd_up_clean: 25
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 7
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# FAM149A

*family with sequence similarity 149 member A* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.02× (z +15.1, q 0e+00, up in 2 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.45× (z +12.3, q 3e-32, up in 16 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.411× (z -12.2, q 3e-31, down in 19 of 23 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.411× (z -6.4, q 3e-08, down in 16 of 21 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC39A]] (+0.63, fdr 4e-05), [[KCP]] (+0.60, fdr 1e-05), [[SEL1L3]] (+0.59, fdr 1e-05); moves opposite to [[SLX4]] (-0.53, fdr 1e-04), [[CCNF]] (-0.52, fdr 1e-04), [[TXNDC17]] (-0.52, fdr 2e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NIBAN1]] → it (grade B ⚠); 7 go from it, the strongest it → [[SEL1L3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3083.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.02×** | +15.1 | 0e+00 | 2/14 (HEC-1-A, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.87×** | +13.9 | 3e-41 | 3/13 (HEC-1-A, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.45×** | +12.3 | 3e-32 | 16/23 (HT-29, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +9.5 | 3e-19 | 3/14 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +8.9 | 5e-17 | 9/21 (A549, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.47×** | +7.4 | 1e-11 | 11/22 (LoVo, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +5.6 | 1e-06 | 3/22 (LS 180, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.19×** | +5.6 | 1e-06 | 9/15 (LoVo, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +5.6 | 1e-06 | 13/22 (A498, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.52×** | +5.4 | 4e-06 | 12/21 (NCI-H2347, A498, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +5.1 | 2e-05 | 3/19 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.43×** | +4.9 | 5e-05 | 6/22 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.38×** | +4.4 | 4e-04 | 5/21 (SW480, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +4.0 | 0.002 | 8/22 (H4, A498, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.003 | 6/22 (CFPAC-1, A498, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.003 | 4/23 (A-427, HOP62, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.004 | 5/22 (KATO III, HT-29, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.004 | 5/23 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +3.7 | 0.006 | 5/22 (SW480, HT-29, …) | all doses, flat |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.05 µM |  | **1.34×** | +3.7 | 0.007 | 3/22 (A-427, Panc 03.27, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.007 | 3/22 (NCI-H2347, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.007 | 4/23 (KATO III, CFPAC-1, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.020 | 4/19 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3083.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.411×** | -12.2 | 3e-31 | 19/23 (KATO III, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.512×** | -9.2 | 1e-17 | 19/23 (LoVo, KATO III, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.562×** | -7.9 | 5e-13 | 19/23 (KATO III, LoVo, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.411×** | -6.4 | 3e-08 | 16/21 (HT-29, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.644×** | -6.0 | 2e-07 | 11/19 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.684×** | -5.2 | 2e-05 | 14/23 (KATO III, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.485×** | -5.2 | 2e-05 | 13/20 (KATO III, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -4.7 | 2e-04 | 4/23 (LS 180, A-172, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.731×** | -4.3 | 0.001 | 16/22 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.784×** | -3.3 | 0.049 | 13/22 (NCI-H1792, KATO III, …) | all doses, stronger at high dose |  |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | **0.795×** | -3.1 | 0.086 | 0/23 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | 0.800× | -3.1 | 0.11 | 5/22 (HOP62, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3083. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 76.8 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0734× (z -20.4) ⚠ cell-cycle shift, explains ~47% of this change |
| [[NCI-H1792 (line)]] | alt | 32.3 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.121× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.304× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 34.0 | 1 (1 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -17.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 23.8 | 1 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 5.55× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -11.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0726× (z -8.5) |
| [[LoVo (line)]] | wt | 48.0 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.125× (z -19.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW48 (line)]] | wt | 35.1 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.107× (z -11.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[Panc 03.27 (line)]] | alt | 23.9 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.158× (z -11.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-427 (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0712× (z -13.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 18.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -10.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[HOP62 (line)]] | alt | 4.01 | 1 | 0 | [[Auranofin (drug)]] 5 µM 13.6× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 5.64 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0809× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 11.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.49× (z +9.0) | — |
| [[SW480 (line)]] | alt | 5.67 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.61× (z +9.5) | — |
| [[A-172 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.952 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.973 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.791 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.938 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.977 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.980 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.975 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.933 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3083), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC39A]] | +0.63 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[KCP]] | +0.60 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[SEL1L3]] | +0.59 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[SLC44A3-AS1]] | +0.59 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[PLEKHG1]] | +0.59 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[SGK2]] | +0.57 | +0.38 / +0.45 | both halves | 7e-05 |  |
| [[GIPC2]] | +0.56 | +0.37 / +0.36 | both halves | 1e-04 |  |
| [[CLIC2]] | +0.56 | +0.28 / +0.42 | both halves | 3e-04 |  |
| [[ACTR3C]] | +0.55 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[DMGDH]] | +0.54 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[MCOLN3]] | +0.54 | +0.34 / +0.42 | both halves | 1e-04 |  |
| [[PTOV1-AS1]] | +0.54 | +0.20 / +0.53 | ⚠ one half (not replicated) | 8e-04 |  |
| [[MMP24]] | +0.54 | +0.37 / +0.51 | both halves | 8e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLX4]] | -0.53 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[CCNF]] | -0.52 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[TXNDC17]] | -0.52 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[WDPCP]] | -0.51 | -0.24 / -0.39 | both halves | 4e-04 |  |
| [[LIX1L]] | -0.49 | -0.39 / -0.22 | both halves | 6e-04 |  |
| [[SLC25A11]] | -0.49 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[DOP1A]] | -0.48 | -0.16 / -0.45 | ⚠ not reproduced | 0.001 |  |
| [[IFT122]] | -0.48 | -0.34 / -0.24 | both halves | 5e-04 |  |
| [[POT1]] | -0.48 | -0.25 / -0.33 | both halves | 4e-04 |  |
| [[ZBTB48]] | -0.47 | -0.25 / -0.31 | both halves | 4e-04 |  |
| [[NUP98]] | -0.47 | -0.20 / -0.43 | both halves | 7e-04 |  |
| [[CEP57L1]] | -0.47 | -0.28 / -0.24 | both halves | 5e-04 |  |
| [[GGA1]] | -0.47 | -0.27 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NIBAN1]] | B | NIBAN1 activity raises FAM149A's level | lines that do not express NIBAN1 (11) vs lines expressing it (39) | 2.51× lower at baseline in the lines without NIBAN1 | 0.028 | ⚠ within organs, on part of the lines; also absent: CAV1, FGF2, PCOLCE2 |
| [[MCOLN3]] | B | MCOLN3 activity raises FAM149A's level | lines that do not express MCOLN3 (18) vs lines expressing it (32) | 2.05× lower at baseline in the lines without MCOLN3 | 0.056 | ⚠ within organs, on part of the lines; also absent: PNMA2, STOX2, NTN1 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEL1L3]] | B | FAM149A activity raises SEL1L3's level | lines that do not express FAM149A (25) vs lines expressing it (25) | 3.09× lower at baseline in the lines without FAM149A | 0.031 | ⚠ within organs, on part of the lines; also absent: SKAP1, ENSG00000286133, CSRNP3 |
| [[HLA-V-1]] | B | FAM149A activity raises HLA-V-1's level | lines that do not express FAM149A (25) vs lines expressing it (25) | 2.08× lower at baseline in the lines without FAM149A | 0.033 | ⚠ within organs, on part of the lines; also absent: SKAP1, ENSG00000286133, CSRNP3 |
| [[NIBAN1]] | B | FAM149A activity raises NIBAN1's level | lines that do not express FAM149A (25) vs lines expressing it (25) | 2.44× lower at baseline in the lines without FAM149A | 0.040 | ⚠ within organs, on part of the lines; also absent: SKAP1, ENSG00000286133, CSRNP3 |
| [[MATN2]] | B | FAM149A activity raises MATN2's level | lines that do not express FAM149A (25) vs lines expressing it (25) | 1.28× lower at baseline in the lines without FAM149A | 0.055 | ⚠ within organs, on part of the lines; also absent: SKAP1, ENSG00000286133, CSRNP3 |
| [[ACTR3C]] | B | FAM149A activity raises ACTR3C's level | lines that do not express FAM149A (25) vs lines expressing it (25) | 1.77× lower at baseline in the lines without FAM149A | 0.069 | ⚠ within organs, on part of the lines; also absent: SKAP1, ENSG00000286133, CSRNP3 |
| [[PRRG2]] | B | FAM149A activity raises PRRG2's level | lines that do not express FAM149A (25) vs lines expressing it (25) | 1.68× lower at baseline in the lines without FAM149A | 0.096 | ⚠ within organs, on part of the lines; also absent: SKAP1, ENSG00000286133, CSRNP3 |
| [[NSUN7]] | C | FAM149A activity raises NSUN7's level | lines that do not express FAM149A (25) vs lines expressing it (25) | 2.26× lower at baseline in the lines without FAM149A | 0.050 | ⚠ within organs, on part of the lines; also absent: SKAP1, ENSG00000286133, CSRNP3; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.459). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.6, 41.3); signed map (54.2, 4.5). **Vector** length 57.4, 12.9% of its response variance represented; |z| ≥ 3 in 622 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.3 | +12.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +15.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +0.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.0 | -12.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.9 | -9.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.7 | -7.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -1.4 | -4.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -5.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 149 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:186,104,419-186,175,337 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564J102, MST119, MSTP119 |
| Matched by | ensembl_id |

UniProt [A5PLN7](https://www.uniprot.org/uniprotkb/A5PLN7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:24527](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24527) · Entrez [25854](https://www.ncbi.nlm.nih.gov/gene/25854) · UniProt [A5PLN7](https://www.uniprot.org/uniprotkb/A5PLN7) · Ensembl [ENSG00000109794](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109794)

## Data

Gene col 3083: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3083); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3083, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3083]; `tensor/DDL_lfc|DDL_z.npy` [3083]; `embed/gene_vectors.npy` [3083]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3083 or target_col == 3083). Every well: [[FAM149A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM149A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
