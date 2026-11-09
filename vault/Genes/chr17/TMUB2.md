---
symbol: "TMUB2"
type: "gene"
col: 9673
ensembl_id: "ENSG00000168591"
name: "transmembrane and ubiquitin like domain containing 2"
location: "17q21.31"
module: 118
arm: "+"
pooled_cpm: 14.12
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 32
n_dd_up_clean: 9
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# TMUB2

*transmembrane and ubiquitin like domain containing 2* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.23× (z +5.4, q 4e-05, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.518× (z -17.0, q 0e+00, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USF3]] (+0.68, fdr 7e-06), [[EMC3]] (+0.66, fdr 1e-05), [[ATP6V1E1]] (+0.65, fdr 3e-05); moves opposite to [[CEP83]] (-0.62, fdr 1e-05), [[CARNMT1]] (-0.55, fdr 3e-05), [[POLR3G]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TCTN2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9673.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.4 | 4e-05 | 20/48 (A-427, RKO, …) | top dose only | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.32×** | +5.0 | 2e-04 | 14/47 (HOP62, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.19× | +4.5 | 0.001 | 15/48 (LOX-IMVI, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +4.4 | 0.001 | 7/47 (RPMI-7951, A549, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.007 | 10/46 (NCI-H23, A498, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.017 | 5/47 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.017 | 9/45 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.018 | 6/45 (Hs 766T, PANC-1, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.029 | 3/47 (LOX-IMVI, NCI-H2347, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.045 | 12/47 (NCI-H2030, LoVo, …) | two highest doses | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.20×** | +3.3 | 0.058 | 6/48 (HOP62, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9673.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.518×** | -17.0 | 0e+00 | 37/47 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.499×** | -12.4 | 4e-33 | 33/46 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.557×** | -10.9 | 2e-25 | 34/48 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.570×** | -10.5 | 2e-23 | 36/47 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.582×** | -10.1 | 7e-22 | 30/45 (MIA PaCa-2, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.618×** | -9.0 | 2e-17 | 31/48 (HT-29, AN3 CA, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.647×** | -8.1 | 3e-14 | 27/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.648×** | -8.1 | 4e-14 | 29/48 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.649×** | -8.1 | 5e-14 | 27/48 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.680×** | -7.2 | 4e-11 | 20/46 (SW 900, COLO 205, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.692×** | -6.9 | 3e-10 | 26/47 (NCI-H460, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.773×** | -6.8 | 6e-10 | 21/48 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.709×** | -6.4 | 6e-09 | 25/47 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.710×** | -6.4 | 6e-09 | 21/46 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.720×** | -6.1 | 3e-08 | 22/47 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.773×** | -4.8 | 4e-05 | 17/47 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.790×** | -4.4 | 3e-04 | 10/45 (SW480, HS-578T, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.793×** | -4.3 | 4e-04 | 11/47 (H4, NCI-H2030, …) | two highest doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.786×** | -4.3 | 5e-04 | 13/47 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.798×** | -4.2 | 6e-04 | 13/47 (HCT15, AN3 CA, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.809×** | -3.8 | 0.003 | 11/47 (C-33 A, RPMI-7951, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.820×** | -3.5 | 0.009 | 17/47 (SK-MEL-2, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.876× | -3.5 | 0.009 | 15/48 (SHP-77, LOX-IMVI, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9673. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 19.2 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.307× (z -10.8) |
| [[COLO 205 (line)]] | alt | 22.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 13.3 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.255× (z -10.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HCT15 (line)]] | alt | 17.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -13.0) |
| [[hTERT-HPNE (line)]] | wt | 22.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 14.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0653× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[BT-474 (line)]] | alt | 8.77 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.0640× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 26.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -15.5) |
| [[CHP-212 (line)]] | wt | 19.4 | 0 | 1 | — | [[Sunitinib (drug)]] 0.05 µM 0.0723× (z -8.9) |
| [[H4 (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.6) |
| [[KATO III (line)]] | alt | 22.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -9.0) |
| [[LoVo (line)]] | wt | 10.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.226× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.140× (z -9.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[SHP-77 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 16.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -11.4) |
| [[A-172 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9673), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USF3]] | +0.68 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[EMC3]] | +0.66 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[ATP6V1E1]] | +0.65 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[WBP1L]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[SYNRG]] | +0.63 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[TOX4]] | +0.59 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[GRN]] | +0.59 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ATP6V1G1]] | +0.58 | +0.32 / +0.59 | both halves | 2e-04 |  |
| [[VPS4B]] | +0.58 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[GET3]] | +0.58 | +0.37 / +0.56 | both halves | 7e-05 |  |
| [[ZSWIM8]] | +0.58 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[RBM48]] | +0.58 | +0.41 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP83]] | -0.62 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[CARNMT1]] | -0.55 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[POLR3G]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[OSBPL10]] | -0.53 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[CMSS1]] | -0.53 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[GALNT10]] | -0.52 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[NIN]] | -0.52 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[SLC35F2]] | -0.52 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[RBFA]] | -0.52 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[GPR63]] | -0.51 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[GMDS]] | -0.51 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[ANKS6]] | -0.51 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCTN2]] | C | TCTN2's natural level strengthens TMUB2's drug response | TCTN2's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.25; direction not clear | 0.098 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.747). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-27.6, -10.0); signed map (-3.5, -4.9). **Vector** length 64.0, 10.0% of its response variance represented; |z| ≥ 3 in 969 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +2.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +3.6 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | -1.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.4 | -4.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.6 | -8.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -12.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.5 | -17.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane and ubiquitin like domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:44,186,970-44,191,929 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3123 |
| Matched by | ensembl_id |

UniProt [Q71RG4](https://www.uniprot.org/uniprotkb/Q71RG4) carries no function annotation.

**Summary**, from NCBI Gene [79089](https://www.ncbi.nlm.nih.gov/gene/79089):

> Predicted to be involved in ERAD pathway. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28459](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28459) · Entrez [79089](https://www.ncbi.nlm.nih.gov/gene/79089) · UniProt [Q71RG4](https://www.uniprot.org/uniprotkb/Q71RG4) · Ensembl [ENSG00000168591](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168591)

## Data

Gene col 9673: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9673); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9673, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9673]; `tensor/DDL_lfc|DDL_z.npy` [9673]; `embed/gene_vectors.npy` [9673]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9673 or target_col == 9673). Every well: [[TMUB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMUB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
