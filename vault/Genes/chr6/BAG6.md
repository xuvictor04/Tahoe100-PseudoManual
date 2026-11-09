---
symbol: "BAG6"
type: "gene"
col: 12876
ensembl_id: "ENSG00000204463"
name: "BAG cochaperone 6"
location: "6p21.33"
module: 153
arm: "+"
pooled_cpm: 54.42
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# BAG6

*BAG cochaperone 6* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.08× (z +11.9, q 7e-30, up in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.72× (z +8.8, q 3e-16, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.734× (z -5.0, q 1e-04, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB11B]] (+0.77, fdr 7e-06), [[RAB1B]] (+0.76, fdr 7e-06), [[SF3A1]] (+0.75, fdr 7e-06); moves opposite to [[MTLN]] (-0.58, fdr 6e-05, ⚠ MTLN in the vector space only through flagged drug-doses), [[MRPL46]] (-0.55, fdr 6e-05), [[NSUN5P2-1]] (-0.55, fdr 5e-05, ⚠ NSUN5P2-1 in the vector space only through flagged drug-doses), [[MRPL36]] (-0.55, fdr 1e-04), [[RBM27]] (-0.55, fdr 1e-05).
> It is in [[Module 153]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12876.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +11.9 | 7e-30 | 45/49 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +11.3 | 6e-27 | 39/42 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +8.8 | 3e-16 | 41/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +6.9 | 1e-09 | 35/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +6.2 | 5e-08 | 32/45 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.01×** | +5.9 | 3e-07 | 34/48 (RKO, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +4.7 | 2e-04 | 30/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.24×** | +4.5 | 6e-04 | 24/48 (NCI-H1573, A-172, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +4.4 | 6e-04 | 28/49 (HT-29, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.25×** | +3.7 | 0.014 | 23/47 (H4, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.6 | 0.015 | 24/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.017 | 22/48 (J82, LS 180, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.23×** | +3.3 | 0.036 | 21/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Pentoxifylline (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.036 | 17/48 (NCI-H2347, J82, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.1 | 0.062 | 0/49 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12876.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.734×** | -5.0 | 1e-04 | 30/48 (SW 900, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.725×** | -5.0 | 1e-04 | 34/48 (A498, HT-29, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.800×** | -5.0 | 1e-04 | 27/48 (KATO III, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.777×** | -4.1 | 0.006 | 29/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.794×** | -3.7 | 0.021 | 20/48 (AsPC-1, A-172, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.790×** | -3.7 | 0.021 | 24/48 (LS 180, COLO 205, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.810×** | -3.4 | 0.048 | 24/48 (SW1417, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.805×** | -3.4 | 0.050 | 20/48 (CFPAC-1, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.804×** | -3.3 | 0.063 | 20/47 (HEC-1-A, COLO 205, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.818×** | -3.3 | 0.063 | 20/48 (AN3 CA, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.820×** | -3.2 | 0.064 | 17/48 (AsPC-1, COLO 205, …) | all doses, flat |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.824×** | -3.2 | 0.075 | 14/48 (SNU-423, LS 180, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.05 µM |  | 0.832× | -3.0 | 0.12 | 15/48 (HS-578T, NCI-H2030, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12876. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.4 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.41× (z +11.8) | — |
| [[PANC-1 (line)]] | alt | 58.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.27× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +10.7) | — |
| [[SW480 (line)]] | alt | 49.1 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.45× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +8.9) | — |
| [[A-172 (line)]] | wt | 43.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.32× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 70.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 85.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 53.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.38× (z +11.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 35.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.16× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 81.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.152× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 43.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 47.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.1) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[HEC-1-A (line)]] | alt | 44.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +10.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 53.1 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.128× (z -9.3) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 61.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +10.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 64.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +10.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 37.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.3) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[NCI-H1792 (line)]] | alt | 38.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 86.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.6) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[NCI-H23 (line)]] | alt | 79.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 47.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 50.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 90.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 76.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 45.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12876), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB11B]] | +0.77 | +0.70 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[RAB1B]] | +0.76 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[SF3A1]] | +0.75 | +0.64 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[AGPAT1]] | +0.70 | +0.71 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[ATP13A1]] | +0.69 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[CDK16]] | +0.68 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[PIGT]] | +0.68 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[PRKAR1A]] | +0.68 | +0.57 / +0.74 | both halves | 1e-05 |  |
| [[ZBED6]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[CNOT3]] | +0.67 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[TPP1]] | +0.67 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[HNRNPUL1]] | +0.66 | +0.55 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTLN]] ⚠ | -0.58 | -0.39 / -0.65 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL46]] | -0.55 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[NSUN5P2-1]] ⚠ | -0.55 | -0.39 / -0.60 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL36]] | -0.55 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[RBM27]] | -0.55 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[SLIRP]] | -0.54 | -0.36 / -0.62 | both halves | 1e-04 |  |
| [[ZNF593]] | -0.54 | -0.26 / -0.62 | both halves | 4e-04 |  |
| [[NOL7]] ⚠ | -0.54 | -0.38 / -0.55 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RDH14]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[FBXO45]] | -0.53 | -0.33 / -0.61 | both halves | 1e-04 |  |
| [[MRPS26]] | -0.53 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[RPP21]] | -0.53 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[PDCD5]] | -0.52 | -0.34 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises BAG6's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises BAG6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.2, -23.3); signed map (-15.2, -33.9). **Vector** length 104, 26.7% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.2 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.1 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.5 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +5.5 | +4.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | +4.8 | +3.7 |
|  | [[Pentoxifylline (drug)]] 0.5 µM |  | +2.3 | +3.3 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | +2.2 | +1.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.1 | +0.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +0.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.9 | -3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.8 | -1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.4 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -1.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.8 | -1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.5 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | BAG cochaperone 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,639,028-31,652,705 (-) |
| Ensembl biotype | protein_coding |
| Also known as | G3, D6S52E, Scythe; previously BAT3 |
| Gene groups (HGNC) | BAG cochaperones; BAG6 complex |
| Reactome | 2 pathways, smallest: Insertion of tail-anchored proteins into the endoplasmic reticulum membrane; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [P46379](https://www.uniprot.org/uniprotkb/P46379) (Large proline-rich protein BAG6):

> ATP-independent molecular chaperone preventing the aggregation of misfolded and hydrophobic patches-containing proteins. Functions as part of a cytosolic protein quality control complex, the BAG6/BAT3 complex, which maintains these client proteins in a soluble state and participates in their proper delivery to the endoplasmic reticulum or alternatively can promote their sorting to the proteasome where they undergo degradation. The BAG6/BAT3 complex is involved in the post-translational delivery …

**Summary**, from NCBI Gene [7917](https://www.ncbi.nlm.nih.gov/gene/7917):

> This gene was first characterized as part of a cluster of genes located within the human major histocompatibility complex class III region. This gene encodes a nuclear protein that is cleaved by caspase 3 and is implicated in the control of apoptosis. In addition, the protein forms a complex with E1A binding protein p300 and is required for the acetylation of p53 in response to DNA damage. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by …

**Accessions** — [HGNC:13919](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13919) · Entrez [7917](https://www.ncbi.nlm.nih.gov/gene/7917) · UniProt [P46379](https://www.uniprot.org/uniprotkb/P46379) · Ensembl [ENSG00000204463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204463)

## Data

Gene col 12876: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12876); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12876, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12876]; `tensor/DDL_lfc|DDL_z.npy` [12876]; `embed/gene_vectors.npy` [12876]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12876 or target_col == 12876). Every well: [[BAG6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAG6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
