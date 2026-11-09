---
symbol: "UBE2Q2P13"
type: "gene"
col: 15222
ensembl_id: "ENSG00000259658"
name: "UBE2Q2 pseudogene 13"
location: "15q26.3"
module: 13
arm: "+"
pooled_cpm: 3.53
n_lines_expressing: 27
n_dd_up: 18
n_dd_down: 25
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 11
direction_downstream: 10
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# UBE2Q2P13

*UBE2Q2 pseudogene 13* — 15q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.81× (z +6.2, q 4e-07, up in 11 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.403× (z -13.3, q 1e-37, down in 18 of 20 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.235× (z -7.8, q 9e-13, down in 14 of 22 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LSP1P5-1]] (+0.64, fdr 1e-05), [[TSHZ3-AS1]] (+0.60, fdr 3e-05), [[BASP1-AS1]] (+0.58, fdr 2e-05); moves opposite to [[PROM1]] (-0.55, fdr 3e-05), [[PRR15]] (-0.50, fdr 3e-05), [[LINC01814]] (-0.50, fdr 8e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[ABO]] → it (grade B ⚠); 10 go from it, the strongest it → [[ABO]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15222.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +6.2 | 4e-07 | 11/23 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +6.0 | 4e-07 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +5.5 | 6e-06 | 8/23 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.45×** | +5.5 | 6e-06 | 10/24 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.7 | 3e-04 | 5/25 (NCI-H23, H4, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.19×** | +4.2 | 0.002 | 3/23 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.45×** | +3.9 | 0.009 | 3/23 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.43×** | +3.7 | 0.014 | 5/18 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +3.4 | 0.035 | 1/6 (HOP62) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Neratinib (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.035 | 1/21 (SW 900) | top dose only |  |
| [[Proglumide (drug)]] 0.05 µM |  | **1.39×** | +3.4 | 0.035 | 1/20 (HOP62) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.38×** | +3.3 | 0.039 | 0/23 | all doses, stronger at high dose |  |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.36×** | +3.2 | 0.069 | 4/19 (A549, NCI-H23, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.069 | 3/17 (A498, NCI-H2030, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +3.0 | 0.089 | 2/23 (NCI-H23, PANC-1) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.095 | 5/20 (PANC-1, RPMI-7951, …) | rises with dose | low cells (technical?); position effect removed |
| [[Erlotinib (drug)]] 5 µM |  | **1.35×** | +2.9 | 0.097 | 3/20 (A498, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15222.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.403×** | -13.3 | 1e-37 | 18/20 (RPMI-7951, A498, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.316×** | -11.4 | 2e-27 | 18/24 (NCI-H460, NCI-H23, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.235×** | -7.8 | 9e-13 | 14/22 (NCI-H460, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.489×** | -7.4 | 2e-11 | 10/18 (RPMI-7951, HOP62, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.513×** | -6.9 | 5e-10 | 14/25 (A549, H4, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.516×** | -6.8 | 1e-09 | 14/22 (HOP62, RPMI-7951, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.543×** | -6.3 | 2e-08 | 11/25 (H4, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.605×** | -5.1 | 2e-05 | 11/23 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.624×** | -4.9 | 7e-05 | 11/24 (HOP62, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.619×** | -4.7 | 1e-04 | 13/21 (LOX-IMVI, CFPAC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.642×** | -4.6 | 2e-04 | 10/21 (H4, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.661×** | -4.2 | 0.001 | 10/23 (A549, HOP62, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.491×** | -3.8 | 0.005 | 9/18 (HOP62, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.703×** | -3.6 | 0.011 | 10/24 (H4, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.715×** | -3.5 | 0.019 | 6/25 (NCI-H460, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.715×** | -3.3 | 0.034 | 7/20 (CFPAC-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | **0.812×** | -3.0 | 0.067 | 1/25 (SNU-423) | top dose only | position effect removed |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | **0.751×** | -3.0 | 0.081 | 2/24 (NCI-H2347, SNU-423) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.746×** | -2.9 | 0.094 | 7/21 (RPMI-7951, NCI-H23, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | **0.823×** | -2.8 | 0.099 | 3/24 (LOX-IMVI, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.56 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15222. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 15.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -11.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -9.0) |
| [[HOP62 (line)]] | alt | 13.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -10.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[LOX-IMVI (line)]] | wt | 8.77 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0492× (z -12.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[RPMI-7951 (line)]] | alt | 9.34 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0746× (z -14.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A498 (line)]] | wt | 4.96 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -12.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A549 (line)]] | wt | 4.38 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0607× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0989× (z -10.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H460 (line)]] | wt | 3.88 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0838× (z -10.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.277× (z -10.2) ⚠ transcription drop; cell-cycle shift, explains ~87% of this change |
| [[A-172 (line)]] | wt | 0.252 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.210 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.220 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.198 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.229 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.195 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.220 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.218 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.196 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.724 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.243 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.206 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.241 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.985 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.519 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.207 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.265 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.215 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15222), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSP1P5-1]] | +0.64 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[TSHZ3-AS1]] | +0.60 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[BASP1-AS1]] | +0.58 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[LSP1P4]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[BVES-AS1]] | +0.54 | +0.37 / +0.62 | both halves | 9e-05 |  |
| [[APH1B]] | +0.53 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[UBE2Q2P1]] | +0.53 | +0.43 / +0.53 | both halves | 4e-05 |  |
| [[EVC2]] | +0.51 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[CNRIP1]] | +0.51 | +0.54 / +0.34 | both halves | 1e-04 |  |
| [[IAH1]] | +0.51 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[ADAMTS10]] | +0.50 | +0.48 / +0.43 | both halves | 4e-05 |  |
| [[ARHGEF25]] | +0.49 | +0.42 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PROM1]] | -0.55 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[PRR15]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[LINC01814]] | -0.50 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[HSD17B2]] | -0.49 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[PRR15L]] | -0.49 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ABO]] | -0.49 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[PRR15-DT]] | -0.48 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[VIPR1]] | -0.47 | -0.44 / -0.37 | both halves | 9e-05 |  |
| [[LINC00299]] | -0.46 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[SYK]] | -0.46 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[POU5F1B]] | -0.46 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[BMP4]] | -0.45 | -0.48 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABO]] | B | ABO activity lowers UBE2Q2P13's level | lines that do not express ABO (32) vs lines expressing it (18) | 2.65× higher at baseline in the lines without ABO | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK |
| [[SYK]] | B | SYK activity lowers UBE2Q2P13's level | lines that do not express SYK (30) vs lines expressing it (20) | 2.56× higher at baseline in the lines without SYK | 0.020 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[FAAH2]] | B | FAAH2 activity lowers UBE2Q2P13's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.70× higher at baseline in the lines without FAAH2 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[HSH2D]] | B | HSH2D activity lowers UBE2Q2P13's level | lines that do not express HSH2D (27) vs lines expressing it (23) | 1.84× higher at baseline in the lines without HSH2D | 0.061 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM; maybe low, not absent |
| [[SAMD12-AS1]] | B | SAMD12-AS1 activity lowers UBE2Q2P13's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 2.30× higher at baseline in the lines without SAMD12-AS1 | 0.067 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4 |
| [[CRACDL]] | B | CRACDL activity lowers UBE2Q2P13's level | lines that do not express CRACDL (25) vs lines expressing it (25) | 2.36× higher at baseline in the lines without CRACDL | 0.069 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CGN, MARVELD3, CASC19 |
| [[APH1B]] | B | APH1B activity raises UBE2Q2P13's level | lines that do not express APH1B (6) vs lines expressing it (44) | 2.29× lower at baseline in the lines without APH1B | 0.071 | ⚠ within organs, on part of the lines; also absent: PER3, DLG4, CCDC3 |
| [[TMEM45B]] | B | TMEM45B activity lowers UBE2Q2P13's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 2.42× higher at baseline in the lines without TMEM45B | 0.072 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[TNFRSF14-AS1]] | B | TNFRSF14-AS1 activity lowers UBE2Q2P13's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 2.11× higher at baseline in the lines without TNFRSF14-AS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[TWIST2]] | C | TWIST2 activity raises UBE2Q2P13's level | lines that do not express TWIST2 (26) vs lines expressing it (24) | 2.35× lower at baseline in the lines without TWIST2 | 0.060 | ⚠ within organs, on part of the lines; also absent: TSHZ3, STAC, SALL1; co-absent with the target |
| [[OCA2]] | C | OCA2 activity raises UBE2Q2P13's level | lines that do not express OCA2 (18) vs lines expressing it (32) | 2.24× lower at baseline in the lines without OCA2 | 0.077 | ⚠ within organs, on part of the lines; also absent: BEX4, STAC, ATP10A; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABO]] | B | UBE2Q2P13 activity lowers ABO's level | lines that do not express UBE2Q2P13 (23) vs lines expressing it (27) | 3.61× higher at baseline in the lines without UBE2Q2P13 | 0.012 | ⚠ within organs, on part of the lines; also absent: ZFP82, CACNA2D1, BASP1-AS1 |
| [[ZNF703]] | B | UBE2Q2P13 activity lowers ZNF703's level | lines that do not express UBE2Q2P13 (23) vs lines expressing it (27) | 2.30× higher at baseline in the lines without UBE2Q2P13 | 0.013 | ⚠ within organs, on part of the lines; also absent: ZFP82, CACNA2D1, BASP1-AS1 |
| [[SYK]] | B | UBE2Q2P13 activity lowers SYK's level | lines that do not express UBE2Q2P13 (23) vs lines expressing it (27) | 4.05× higher at baseline in the lines without UBE2Q2P13 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZFP82, CACNA2D1, BASP1-AS1 |
| [[CRACDL]] | B | UBE2Q2P13 activity lowers CRACDL's level | lines that do not express UBE2Q2P13 (23) vs lines expressing it (27) | 2.29× higher at baseline in the lines without UBE2Q2P13 | 0.064 | ⚠ within organs, on part of the lines; also absent: ZFP82, CACNA2D1, BASP1-AS1 |
| [[UBE2Q2P1-1]] | B | UBE2Q2P13 activity raises UBE2Q2P1-1's level | lines that do not express UBE2Q2P13 (23) vs lines expressing it (27) | 1.45× lower at baseline in the lines without UBE2Q2P13 | 0.068 | ⚠ within organs, on part of the lines; also absent: ZFP82, CACNA2D1, BASP1-AS1 |
| [[LINC01814]] | B | UBE2Q2P13 activity lowers LINC01814's level | lines that do not express UBE2Q2P13 (23) vs lines expressing it (27) | 3.04× higher at baseline in the lines without UBE2Q2P13 | 0.099 | ⚠ within organs, on part of the lines; also absent: ZFP82, CACNA2D1, BASP1-AS1 |
| [[DNAAF9]] | C | UBE2Q2P13 activity raises DNAAF9's level | lines that do not express UBE2Q2P13 (23) vs lines expressing it (27) | 3.30× lower at baseline in the lines without UBE2Q2P13 | 0.048 | ⚠ within organs, on part of the lines; also absent: ZFP82, CACNA2D1, BASP1-AS1; co-absent with the target |
| [[TSHZ3]] | C | UBE2Q2P13 activity raises TSHZ3's level | lines that do not express UBE2Q2P13 (23) vs lines expressing it (27) | 4.26× lower at baseline in the lines without UBE2Q2P13 | 0.078 | ⚠ within organs, on part of the lines; also absent: ZFP82, CACNA2D1, BASP1-AS1; co-absent with the target |
| [[STAC]] | C | UBE2Q2P13 activity raises STAC's level | lines that do not express UBE2Q2P13 (23) vs lines expressing it (27) | 3.83× lower at baseline in the lines without UBE2Q2P13 | 0.080 | ⚠ within organs, on part of the lines; also absent: ZFP82, CACNA2D1, BASP1-AS1; co-absent with the target |
| [[BASP1-AS1]] | C | UBE2Q2P13 activity raises BASP1-AS1's level | lines that do not express UBE2Q2P13 (23) vs lines expressing it (27) | 3.14× lower at baseline in the lines without UBE2Q2P13 | 0.094 | ⚠ within organs, on part of the lines; also absent: ZFP82, CACNA2D1, BASP1-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.422). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (54.2, 15.8); signed map (26.3, 49.3). **Vector** length 41.0, 7.40% of its response variance represented; |z| ≥ 3 in 609 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +2.9 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.2 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.1 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.9 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.8 | +3.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.7 | -11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -1.5 | -13.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.1 | -6.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -0.9 | -2.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -0.8 | -7.8 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.6 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.6 | -3.8 |
|  | [[Quinestrol (drug)]] 5 µM |  | -0.6 | +1.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | UBE2Q2 pseudogene 13 |
| Locus type | pseudogene |
| Location | 15q26.3 — chr15:101,732,201-101,745,983 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56078](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56078) · Entrez [100128108](https://www.ncbi.nlm.nih.gov/gene/100128108) · Ensembl [ENSG00000259658](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259658)

## Data

Gene col 15222: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15222); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15222, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15222]; `tensor/DDL_lfc|DDL_z.npy` [15222]; `embed/gene_vectors.npy` [15222]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15222 or target_col == 15222). Every well: [[UBE2Q2P13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2Q2P13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
