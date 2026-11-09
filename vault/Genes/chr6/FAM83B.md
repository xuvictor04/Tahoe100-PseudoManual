---
symbol: "FAM83B"
type: "gene"
col: 9605
ensembl_id: "ENSG00000168143"
name: "scaffolding CK1 anchoring protein B"
location: "6p12.1"
module: 31
arm: "+"
pooled_cpm: 44.51
n_lines_expressing: 20
n_dd_up: 17
n_dd_down: 10
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 75
direction_downstream: 117
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# FAM83B

*scaffolding CK1 anchoring protein B* — 6p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.63× (z +9.7, q 2e-19, up in 0 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 1.54× (z +8.1, q 2e-13, up in 8 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.281× (z -25.1, q 0e+00, down in 18 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DAPP1]] (+0.69, fdr 7e-06), [[INAVA]] (+0.68, fdr 7e-06), [[MYO5B]] (+0.62, fdr 7e-06); moves opposite to [[NKTR]] (-0.42, fdr 1e-04), [[MME]] (-0.41, fdr 5e-04), [[FAM20C]] (-0.41, fdr 3e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 75 arrows point to it, the strongest [[LRATD2]] → it (grade B ⚠); 117 go from it, the strongest it → [[EPS8L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9605.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +9.7 | 2e-19 | 0/19 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.54×** | +8.1 | 2e-13 | 8/18 (HT-29, LS 180, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +6.6 | 7e-09 | 0/17 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.84×** | +6.4 | 3e-08 | 10/18 (HT-29, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +6.1 | 1e-07 | 1/17 (AsPC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.71×** | +5.6 | 3e-06 | 4/14 (NCI-H1573, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.28×** | +4.9 | 7e-05 | 0/18 | inconsistent across doses | position effect removed |
| [[Pralsetinib (drug)]] 0.05 µM |  | **1.29×** | +4.8 | 9e-05 | 1/19 (NCI-H2122) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.27×** | +4.8 | 9e-05 | 13/18 (NCI-H2030, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.27×** | +4.6 | 2e-04 | 10/18 (NCI-H2030, COLO 205, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +4.5 | 4e-04 | 6/18 (AsPC-1, SW48, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.001 | 5/18 (SW1417, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.16× | +4.1 | 0.001 | 5/18 (BT-474, SW1417, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +4.1 | 0.002 | 9/18 (LoVo, LS 180, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.23×** | +4.1 | 0.002 | 0/18 | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.002 | 7/18 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +4.0 | 0.002 | 4/19 (LS 180, KATO III, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.013 | 2/19 (HT-29, LS 180) | all doses, flat | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.017 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.4 | 0.017 | 4/18 (COLO 205, LS 180, …) | top dose only |  |
| [[Verteporfin (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.024 | 0/18 | inconsistent across doses | position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.070 | 2/18 (BT-474, AsPC-1) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9605.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.281×** | -25.1 | 0e+00 | 18/18 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.298×** | -24.0 | 0e+00 | 18/18 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.322×** | -22.5 | 0e+00 | 18/18 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.518×** | -13.0 | 1e-36 | 18/18 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.681×** | -7.6 | 3e-12 | 13/18 (COLO 205, SW1417, …) | top dose only | cell-cycle shift (explains ~12% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.481×** | -7.6 | 3e-12 | 17/19 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.696×** | -7.2 | 6e-11 | 16/18 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -5.0 | 4e-05 | 1/19 (NCI-H2030) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.782×** | -4.9 | 7e-05 | 15/18 (HCT15, LoVo, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.772×** | -4.7 | 1e-04 | 3/18 (BT-474, AsPC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.848× | -4.6 | 2e-04 | 8/18 (CFPAC-1, SW1417, …) | top dose only |  |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.825×** | -3.6 | 0.015 | 1/18 (J82) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | 0.842× | -3.4 | 0.029 | 7/18 (BT-474, Panc 03.27, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.853× | -3.1 | 0.066 | 1/18 (NCI-H2030) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | 0.850× | -3.1 | 0.076 | 13/18 (C-33 A, NCI-H2347, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.856× | -3.1 | 0.076 | 1/18 (NCI-H2030) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9605. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 200 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0587× (z -31.2) |
| [[KATO III (line)]] | alt | 102 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0346× (z -33.6) |
| [[HEC-1-A (line)]] | alt | 118 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0590× (z -33.5) |
| [[HT-29 (line)]] | alt | 83.3 | 1 | 9 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.61× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.0473× (z -28.8) |
| [[NCI-H2347 (line)]] | alt | 107 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0698× (z -24.5) |
| [[BT-474 (line)]] | alt | 88.0 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0228× (z -26.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.0518× (z -21.4) |
| [[HCT15 (line)]] | alt | 107 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0603× (z -21.1) |
| [[LoVo (line)]] | wt | 77.9 | 2 | 6 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.23× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.0881× (z -28.0) |
| [[LS 180 (line)]] | wt | 129 | 1 | 7 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.49× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.0633× (z -28.2) |
| [[NCI-H2030 (line)]] | alt | 107 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.140× (z -18.0) |
| [[Panc 03.27 (line)]] | alt | 87.2 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0712× (z -23.4) |
| [[AsPC-1 (line)]] | alt | 136 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0441× (z -26.0) |
| [[SW48 (line)]] | wt | 183 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0400× (z -22.7) |
| [[C-33 A (line)]] | alt | 58.3 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0390× (z -21.2) |
| [[COLO 205 (line)]] | alt | 231 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0592× (z -28.6) |
| [[NCI-H1573 (line)]] | alt | 79.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0381× (z -29.5) |
| [[J82 (line)]] | alt | 23.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0867× (z -16.9) |
| [[SW1417 (line)]] | alt | 59.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0978× (z -21.7) |
| [[A-172 (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.25 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.88 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.89 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.66 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.71 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.42 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 9.74 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.35 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.40 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.73 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.91 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.36 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.90 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.50 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.57 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9605), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAPP1]] | +0.69 | +0.60 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[INAVA]] | +0.68 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[MYO5B]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[ARHGEF34P]] | +0.61 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[TMPRSS4]] | +0.60 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[C1orf116]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ARHGEF5]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[FAM110C]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[SLC28A3]] | +0.58 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[TTC9]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[EPS8L1]] | +0.57 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[CDH1]] | +0.57 | +0.38 / +0.64 | both halves | 7e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKTR]] | -0.42 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[MME]] | -0.41 | -0.29 / -0.23 | both halves | 5e-04 |  |
| [[FAM20C]] | -0.41 | -0.37 / -0.28 | both halves | 3e-04 |  |
| [[ADAMTS10]] | -0.41 | -0.40 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*75 arrows, 75 of them with an alert ⚠; grade A 0, B 10, C 65. Shown: the 12 strongest; 63 more arrows (63 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRATD2]] | B | LRATD2 activity raises FAM83B's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 4.35× lower at baseline in the lines without LRATD2 | 0.016 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[PLEKHG1]] | B | PLEKHG1 activity raises FAM83B's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 3.44× lower at baseline in the lines without PLEKHG1 | 0.026 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[MYO1D]] | B | MYO1D activity raises FAM83B's level | lines that do not express MYO1D (13) vs lines expressing it (37) | 4.14× lower at baseline in the lines without MYO1D | 0.040 | ⚠ within organs, on part of the lines; also absent: MOB3B, MBNL3, MAST4; maybe low, not absent |
| [[EPS8L1]] | B | EPS8L1 activity raises FAM83B's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 3.06× lower at baseline in the lines without EPS8L1 | 0.045 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[NOSTRIN]] | B | NOSTRIN activity raises FAM83B's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 4.78× lower at baseline in the lines without NOSTRIN | 0.053 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[PSORS1C1]] | B | PSORS1C1 activity raises FAM83B's level | lines that do not express PSORS1C1 (15) vs lines expressing it (35) | 3.01× lower at baseline in the lines without PSORS1C1 | 0.062 | ⚠ within organs, on part of the lines; also absent: IL15, MGLL, SH3TC2 |
| [[PKP3]] | B | PKP3 activity raises FAM83B's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 3.99× lower at baseline in the lines without PKP3 | 0.074 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent |
| [[MET]] | B | MET activity raises FAM83B's level | lines that do not express MET (9) vs lines expressing it (41) | 3.16× lower at baseline in the lines without MET | 0.089 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[HDAC6]] | B | HDAC6 activity raises FAM83B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SEMA3B]] | B | SEMA3B activity raises FAM83B's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 2.61× lower at baseline in the lines without SEMA3B | 0.098 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[TMPRSS4]] | C | TMPRSS4 activity raises FAM83B's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 14.42× lower at baseline in the lines without TMPRSS4 | 9e-06 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[C1orf116]] | C | C1orf116 activity raises FAM83B's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 11.22× lower at baseline in the lines without C1orf116 | 7e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |

### Downstream of this gene

*117 arrows, 117 of them with an alert ⚠; grade A 0, B 48, C 69. Shown: the 12 strongest; 105 more arrows (105 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | FAM83B activity raises EPS8L1's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 4.21× lower at baseline in the lines without FAM83B | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[FAM83E]] | B | FAM83B activity raises FAM83E's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 4.38× lower at baseline in the lines without FAM83B | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[ARHGAP27]] | B | FAM83B activity raises ARHGAP27's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 2.72× lower at baseline in the lines without FAM83B | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[PATJ]] | B | FAM83B activity raises PATJ's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 3.52× lower at baseline in the lines without FAM83B | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[LRATD2]] | B | FAM83B activity raises LRATD2's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 3.98× lower at baseline in the lines without FAM83B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[KPNA7]] | B | FAM83B activity raises KPNA7's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 2.64× lower at baseline in the lines without FAM83B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[PKP3]] | B | FAM83B activity raises PKP3's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 3.52× lower at baseline in the lines without FAM83B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[KLHL2P1]] | B | FAM83B activity raises KLHL2P1's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 1.76× lower at baseline in the lines without FAM83B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[PTK2B]] | B | FAM83B activity raises PTK2B's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 3.15× lower at baseline in the lines without FAM83B | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[RDH13]] | B | FAM83B activity raises RDH13's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 2.49× lower at baseline in the lines without FAM83B | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[MYO1D]] | B | FAM83B activity raises MYO1D's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 3.46× lower at baseline in the lines without FAM83B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[SEMA3B]] | B | FAM83B activity raises SEMA3B's level | lines that do not express FAM83B (30) vs lines expressing it (20) | 3.25× lower at baseline in the lines without FAM83B | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.574). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.6, 56.7); signed map (56.4, 7.6). **Vector** length 85.9, 30.5% of its response variance represented; |z| ≥ 3 in 647 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +3.7 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.4 | +8.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +3.0 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.0 | +2.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -7.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -5.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.4 | -7.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | -1.3 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.1 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[Rifaximin (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | -7.6 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.9 | -0.9 |
|  | [[Levobupivacaine (hydrochloride) (drug)]] 5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | scaffolding CK1 anchoring protein B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.1 — chr6:54,846,771-54,945,099 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30642; previously C6orf143, FAM83B |
| Gene groups (HGNC) | Scaffolding anchor of CK1 domain containing |
| Reactome | 8 pathways, smallest: RND1 GTPase cycle; RND2 GTPase cycle; RND3 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T0W9](https://www.uniprot.org/uniprotkb/Q5T0W9) (Scaffolding CK1 anchoring protein B):

> Probable proto-oncogene that functions in the epidermal growth factor receptor/EGFR signaling pathway. Activates both the EGFR itself and downstream RAS/MAPK and PI3K/AKT/TOR signaling cascades.

**Summary**, from NCBI Gene [222584](https://www.ncbi.nlm.nih.gov/gene/222584):

> Enables epidermal growth factor receptor binding activity; phosphatidylinositol 3-kinase binding activity; and protein kinase binding activity. Involved in cell population proliferation and positive regulation of epidermal growth factor receptor signaling pathway. Located in cytoplasm and membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21357](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21357) · Entrez [222584](https://www.ncbi.nlm.nih.gov/gene/222584) · UniProt [Q5T0W9](https://www.uniprot.org/uniprotkb/Q5T0W9) · Ensembl [ENSG00000168143](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168143)

## Data

Gene col 9605: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9605); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9605, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9605]; `tensor/DDL_lfc|DDL_z.npy` [9605]; `embed/gene_vectors.npy` [9605]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9605 or target_col == 9605). Every well: [[FAM83B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM83B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
