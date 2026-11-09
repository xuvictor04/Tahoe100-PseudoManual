---
symbol: "BCL11B"
type: "gene"
col: 4792
ensembl_id: "ENSG00000127152"
name: "BCL11 transcription factor B"
location: "14q32.2"
module: 13
arm: "+"
pooled_cpm: 23.8
n_lines_expressing: 32
n_dd_up: 13
n_dd_down: 21
n_dd_up_clean: 9
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 8
direction_downstream: 6
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# BCL11B

*BCL11 transcription factor B* — 14q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.37× (z +19.0, q 0e+00, up in 23 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.479× (z -11.3, q 1e-26, down in 25 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL4C]] (+0.66, fdr 1e-05), [[STC1]] (+0.62, fdr 8e-06), [[LINC03047]] (+0.61, fdr 1e-05); moves opposite to [[ATL3]] (-0.49, fdr 3e-05), [[NUDT16-DT]] (-0.48, fdr 5e-05), [[MKRN5P]] (-0.47, fdr 7e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[RFX8]] → it (grade B ⚠); 6 go from it, the strongest it → [[DPF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4792.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.37×** | +19.0 | 0e+00 | 23/30 (NCI-H2030, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.07×** | +11.4 | 2e-27 | 19/30 (LoVo, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +9.0 | 6e-17 | 17/30 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.42×** | +5.3 | 2e-05 | 6/21 (AsPC-1, SW480, …) | inconsistent across doses | composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.89×** | +5.2 | 3e-05 | 12/29 (LOX-IMVI, H4, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.83×** | +4.9 | 7e-05 | 12/30 (NCI-H2030, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.46×** | +4.2 | 0.002 | 7/30 (NCI-H460, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.004 | 10/29 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.29×** | +4.0 | 0.005 | 6/30 (NCI-H2030, CFPAC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.29×** | +3.9 | 0.005 | 9/30 (NCI-H2030, NCI-H2347, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.57×** | +3.7 | 0.011 | 8/30 (A549, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.028 | 1/30 (SW480) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.4 | 0.028 | 15/30 (A549, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4792.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.479×** | -11.3 | 1e-26 | 25/30 (LOX-IMVI, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.547×** | -9.0 | 7e-17 | 23/28 (LOX-IMVI, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.618×** | -7.4 | 2e-11 | 20/30 (LOX-IMVI, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.619×** | -7.0 | 3e-10 | 23/30 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.654×** | -6.5 | 1e-08 | 16/30 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.791×** | -5.1 | 3e-05 | 15/30 (A-427, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.739×** | -4.7 | 2e-04 | 11/30 (NCI-H23, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.819×** | -4.3 | 0.001 | 13/30 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.759×** | -4.3 | 0.001 | 9/30 (hTERT-HPNE, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.754×** | -4.2 | 0.001 | 12/29 (NCI-H1573, A-427, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.848× | -3.6 | 0.018 | 8/30 (SNU-423, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.795×** | -3.5 | 0.019 | 6/28 (NCI-H2030, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.799×** | -3.4 | 0.025 | 12/30 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.808×** | -3.3 | 0.041 | 10/29 (hTERT-HPNE, LOX-IMVI, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.785×** | -3.2 | 0.042 | 7/29 (hTERT-HPNE, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.808×** | -3.2 | 0.042 | 7/30 (H4, SNU-423, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.811×** | -3.2 | 0.042 | 10/30 (H4, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4792. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 275 | 0 | 19 (14 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -25.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.186× (z -19.5) |
| [[H4 (line)]] | wt | 177 | 0 | 17 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -17.4) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Clobetasol propionate (drug)]] 5 µM 0.165× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 97.9 | 0 | 15 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -17.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0699× (z -17.0) |
| [[SNU-423 (line)]] | alt | 41.4 | 0 | 14 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0848× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.240× (z -13.5) |
| [[KATO III (line)]] | alt | 62.8 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.261× (z -13.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.353× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 48.8 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.264× (z -9.9) |
| [[LoVo (line)]] | wt | 32.7 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.8) ⚠ cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.12× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[LS 180 (line)]] | wt | 50.9 | 2 | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.28× (z +10.0) | [[Ixazomib citrate (drug)]] 5 µM 0.240× (z -12.3) |
| [[A549 (line)]] | wt | 30.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 7.87 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.73× (z +8.9) | [[Nimesulide (drug)]] 5 µM 0.102× (z -9.2) ⚠ toxic; unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 7.97 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.92× (z +10.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0918× (z -10.5) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 15.2 | 0 | 2 (2 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0553× (z -15.1) ⚠ toxic |
| [[SW 900 (line)]] | alt | 52.4 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 19.0 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.01× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.122× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-427 (line)]] | wt | 23.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -11.1) |
| [[COLO 205 (line)]] | alt | 74.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.294× (z -9.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HCT15 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.143× (z -10.3) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.153× (z -9.6) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 9.06 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.58× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 8.33 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0668× (z -10.8) |
| [[SW480 (line)]] | alt | 9.09 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.06× (z +10.2) | — |
| [[A-172 (line)]] | wt | 4.82 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.95 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.27 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.18 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.46 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.09 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4792), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL4C]] | +0.66 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[STC1]] | +0.62 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[LINC03047]] | +0.61 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[TSHZ3]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 | same gene group |
| [[TMEM200A]] | +0.59 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[CACNA1A]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[ADAMTS18]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[SAMD3]] | +0.58 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[NPTX1]] | +0.58 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[GPR68]] | +0.57 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[CYTH4]] | +0.57 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[SHANK1]] | +0.57 | +0.54 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATL3]] | -0.49 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[NUDT16-DT]] | -0.48 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[MKRN5P]] | -0.47 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[GSR]] | -0.44 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFX8]] | B | RFX8 activity raises BCL11B's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.96× lower at baseline in the lines without RFX8 | 0.034 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[PTGS2]] | B | PTGS2 activity raises BCL11B's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.27× lower at baseline in the lines without PTGS2 | 0.048 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[TMEM200A]] | B | TMEM200A activity strengthens BCL11B's drug response | lines that do not express TMEM200A (19) vs lines expressing it (11) | the lines without TMEM200A respond 0.95× as strongly (z diff +0.14); strongest at Bortezomib 0.05 µM: 0.57x vs 0.35x (z diff +3.0) | 0.070 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615; target measured in part of the lines; both ways; artifact flags |
| [[MME]] | B | MME activity strengthens BCL11B's drug response | lines that do not express MME (17) vs lines expressing it (13) | the lines without MME respond 0.74× as strongly (z diff +1.12); strongest at Ixazomib citrate 5 µM: 0.56x vs 0.27x (z diff +3.7) | 0.075 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC; target measured in part of the lines; artifact flags |
| [[KCNMA1]] | B | KCNMA1 activity raises BCL11B's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 1.79× lower at baseline in the lines without KCNMA1 | 0.087 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[PKIA]] | B | PKIA activity raises BCL11B's level | lines that do not express PKIA (22) vs lines expressing it (28) | 1.58× lower at baseline in the lines without PKIA | 0.089 | ⚠ within organs, on part of the lines; also absent: EPHA6, GALNT13, CAMK4 |
| [[RAC2]] | B | RAC2 activity raises BCL11B's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 2.44× lower at baseline in the lines without RAC2 | 0.095 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[FZD8]] | B | FZD8 activity raises BCL11B's level | lines that do not express FZD8 (20) vs lines expressing it (30) | 1.51× lower at baseline in the lines without FZD8 | 0.098 | ⚠ within organs, on part of the lines; also absent: RNF182, NRG1, FBXL7 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPF1]] | B | BCL11B activity lowers DPF1's level | lines that do not express BCL11B (18) vs lines expressing it (32) | 1.75× higher at baseline in the lines without BCL11B | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000249111, HLA-V-1, ENSG00000272297; maybe low, not absent |
| [[TMEM145]] | B | BCL11B activity lowers TMEM145's level | lines that do not express BCL11B (18) vs lines expressing it (32) | 1.35× higher at baseline in the lines without BCL11B | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000249111, HLA-V-1, ENSG00000272297; maybe low, not absent |
| [[IER3]] | B | BCL11B activity raises IER3's level | lines that do not express BCL11B (18) vs lines expressing it (32) | 1.79× lower at baseline in the lines without BCL11B | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000249111, HLA-V-1, ENSG00000272297; maybe low, not absent |
| [[PTGS2]] | B | BCL11B activity raises PTGS2's level | lines that do not express BCL11B (18) vs lines expressing it (32) | 3.36× lower at baseline in the lines without BCL11B | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000249111, HLA-V-1, ENSG00000272297; maybe low, not absent |
| [[DOT1L]] | B | BCL11B activity lowers DOT1L's level | lines that do not express BCL11B (18) vs lines expressing it (32) | 1.23× higher at baseline in the lines without BCL11B | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000249111, HLA-V-1, ENSG00000272297; maybe low, not absent |
| [[BTG1]] | B | BCL11B activity raises BTG1's level | lines that do not express BCL11B (18) vs lines expressing it (32) | 1.73× lower at baseline in the lines without BCL11B | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000249111, HLA-V-1, ENSG00000272297; maybe low, not absent |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.559). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.9, 12.8); signed map (19.7, 46.5). **Vector** length 94.8, 22.8% of its response variance represented; |z| ≥ 3 in 953 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.2 | +19.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +9.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.8 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.2 | -1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +2.9 | +5.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.7 | +4.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.5 | +1.4 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.2 | +3.0 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -2.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.8 | -1.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -11.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -2.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | BCL11 transcription factor B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.2 — chr14:99,169,287-99,272,197 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CTIP-2, CTIP2, hRIT1-alpha, SMARCM2; previously ZNF856B |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BAF complex subunits |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 5 pathways, smallest: Formation of the embryonic stem cell BAF (esBAF) complex; Formation of neuronal progenitor and neuronal BAF (npBAF and nBAF); SWI/SNF chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0K0](https://www.uniprot.org/uniprotkb/Q9C0K0) (B-cell lymphoma/leukemia 11B):

> Key regulator of both differentiation and survival of T-lymphocytes during thymocyte development in mammals. Essential in controlling the responsiveness of hematopoietic stem cells to chemotactic signals by modulating the expression of the receptors CCR7 and CCR9, which direct the movement of progenitor cells from the bone marrow to the thymus. Is a regulator of IL2 promoter and enhances IL2 expression in activated CD4(+) T-lymphocytes. Tumor-suppressor that represses transcription through …

**Summary**, from NCBI Gene [64919](https://www.ncbi.nlm.nih.gov/gene/64919):

> This gene encodes a C2H2-type zinc finger protein and is closely related to BCL11A, a gene whose translocation may be associated with B-cell malignancies. Although the specific function of this gene has not been determined, the encoded protein is known to be a transcriptional repressor, and is regulated by the NURD nucleosome remodeling and histone deacetylase complex. Four alternatively spliced transcript variants encoding distinct isoforms have been found for this gene. [provided by RefSeq, …

**Accessions** — [HGNC:13222](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13222) · Entrez [64919](https://www.ncbi.nlm.nih.gov/gene/64919) · UniProt [Q9C0K0](https://www.uniprot.org/uniprotkb/Q9C0K0) · Ensembl [ENSG00000127152](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127152)

## Data

Gene col 4792: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4792); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4792, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4792]; `tensor/DDL_lfc|DDL_z.npy` [4792]; `embed/gene_vectors.npy` [4792]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4792 or target_col == 4792). Every well: [[BCL11B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL11B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
