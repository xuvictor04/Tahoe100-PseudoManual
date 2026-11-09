---
symbol: "HPS4"
type: "gene"
col: 1865
ensembl_id: "ENSG00000100099"
name: "HPS4 biogenesis of lysosomal organelles complex 3 subunit 2"
location: "22q12.1"
module: 122
arm: "+"
pooled_cpm: 40.12
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 25
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# HPS4

*HPS4 biogenesis of lysosomal organelles complex 3 subunit 2* — 22q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 1.30× (z +4.9, q 4e-04, up in 25 of 48 measured lines) ⚠ cell-cycle shift, explains ~86% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 2.20×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.506× (z -12.8, q 1e-34, down in 37 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.677× (z -7.3, q 1e-11, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHC3]] (+0.63, fdr 1e-05), [[MITD1]] (+0.61, fdr 1e-05), [[TRPM7]] (+0.60, fdr 1e-05); moves opposite to [[YWHAB]] (-0.54, fdr 2e-05), [[DIAPH1]] (-0.51, fdr 4e-05), [[ZSWIM6]] (-0.51, fdr 4e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF563]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1865.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-172 2.20×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.30×** | +4.9 | 4e-04 | 25/48 (LS 180, C32, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.18× | +4.4 | 0.004 | 18/48 (C32, NCI-H1573, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.25×** | +4.1 | 0.008 | 20/48 (Hs 766T, HOP62, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.21× | +3.4 | 0.10 | 12/47 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.17 | 14/48 (NCI-H460, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 21 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1865.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.506×** | -12.8 | 1e-34 | 37/47 (SW480, SNU-423, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.551×** | -10.3 | 1e-22 | 32/43 (Panc 03.27, NCI-H460, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.619×** | -8.7 | 8e-16 | 32/47 (SNU-423, Hs 766T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **0.622×** | -8.6 | 1e-15 | 27/40 (NCI-H1792, Panc 03.27, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.640×** | -8.4 | 5e-15 | 39/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.649×** | -8.1 | 4e-14 | 34/48 (SHP-77, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.658×** | -7.9 | 3e-13 | 36/48 (SNU-423, HCT15, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.670×** | -7.5 | 4e-12 | 39/48 (SW1417, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.677×** | -7.3 | 1e-11 | 37/48 (SNU-423, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.678×** | -7.3 | 2e-11 | 33/48 (SNU-423, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.715×** | -6.3 | 1e-08 | 31/48 (HCT15, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.792×** | -6.2 | 2e-08 | 29/48 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.748×** | -5.5 | 2e-06 | 22/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.740×** | -5.4 | 2e-06 | 28/47 (RKO, NCI-H2030, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **0.759×** | -5.2 | 8e-06 | 25/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.769×** | -5.0 | 3e-05 | 25/48 (SNU-423, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.787×** | -4.5 | 2e-04 | 24/48 (HEC-1-A, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.851× | -4.3 | 4e-04 | 18/48 (A-172, HOP62, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.681×** | -3.8 | 0.004 | 12/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.684×** | -3.7 | 0.004 | 22/48 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.851× | -2.9 | 0.065 | 12/48 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.862× | -2.8 | 0.090 | 8/48 (SW 900, CHP-212, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1865. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 46.2 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.462× (z -9.1) |
| [[SNU-423 (line)]] | alt | 63.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.177× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.263× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 117 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[HEC-1-A (line)]] | alt | 50.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[A-427 (line)]] | wt | 21.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[NCI-H1792 (line)]] | alt | 37.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0534× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[NCI-H460 (line)]] | wt | 31.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SW1417 (line)]] | alt | 48.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.379× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[SW48 (line)]] | wt | 38.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[A-172 (line)]] | wt | 32.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 34.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[AsPC-1 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[HCT15 (line)]] | alt | 48.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[HOP62 (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.347× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[HS-578T (line)]] | alt | 41.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[J82 (line)]] | alt | 25.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0682× (z -11.2) ⚠ toxic |
| [[LoVo (line)]] | wt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[MIA PaCa-2 (line)]] | alt | 39.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -13.3) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 46.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[NCI-H2030 (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.299× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~24% of this change |
| [[NCI-H23 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[PANC-1 (line)]] | alt | 35.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[RKO (line)]] | wt | 40.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.146× (z -15.6) ⚠ toxic; cell-cycle shift, explains ~24% of this change |
| [[SHP-77 (line)]] | alt | 45.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[SNU-1 (line)]] | wt | 48.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[SW 900 (line)]] | alt | 43.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[A498 (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1865), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHC3]] | +0.63 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[MITD1]] | +0.61 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[TRPM7]] | +0.60 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[EXOC1]] | +0.59 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[RRAGB]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[FLCN]] | +0.58 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[METTL22]] | +0.58 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[VPS41]] | +0.57 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[PAAF1]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[MCCC1]] | +0.56 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[WASHC2C]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[WASHC2A]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAB]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[DIAPH1]] | -0.51 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[ZSWIM6]] | -0.51 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[PSME4]] | -0.49 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[ACOT7]] | -0.48 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[PPP3CA]] | -0.48 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[MAPKAPK2]] | -0.47 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[ARPC1B]] | -0.46 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[GATAD2A]] | -0.46 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[CHUK]] | -0.45 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[G6PD]] | -0.45 | -0.40 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF563]] | B | ZNF563 activity raises HPS4's level | lines that do not express ZNF563 (9) vs lines expressing it (41) | 1.26× lower at baseline in the lines without ZNF563 | 0.078 | ⚠ within organs, on part of the lines; also absent: ZNF442, ZNF433, ENSG00000269755 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.559). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-19.7, 15.2); signed map (-5.5, 0.3). **Vector** length 84.5, 19.2% of its response variance represented; |z| ≥ 3 in 1,087 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.3 | +4.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +4.6 | +4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.1 | -1.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +3.4 | -4.6 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | +3.4 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +1.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.7 | +1.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.3 | +0.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +0.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.2 | -7.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -2.4 | -6.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -3.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -7.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | HPS4 biogenesis of lysosomal organelles complex 3 subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.1 — chr22:26,443,107-26,483,931 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1667, LE, BLOC3S2 |
| Gene groups (HGNC) | Biogenesis of lysosomal organelles complex 3 |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQG7](https://www.uniprot.org/uniprotkb/Q9NQG7) (BLOC-3 complex member HPS4):

> Component of the BLOC-3 complex, a complex that acts as a guanine exchange factor (GEF) for RAB32 and RAB38, promotes the exchange of GDP to GTP, converting them from an inactive GDP-bound form into an active GTP-bound form. The BLOC-3 complex plays an important role in the control of melanin production and melanosome biogenesis and promotes the membrane localization of RAB32 and RAB38.

**Summary**, from NCBI Gene [89781](https://www.ncbi.nlm.nih.gov/gene/89781):

> This gene encodes a protein component of biogenesis of lysosome-related organelles complexes (BLOC). BLOC complexes are important for the formation of endosomal-lysosomal organelles such as melanosomes and platelet dense granules. Mutations in this gene result in subtype 4 of Hermansky-Pudlak syndrome, a form of albinism. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:15844](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15844) · Entrez [89781](https://www.ncbi.nlm.nih.gov/gene/89781) · UniProt [Q9NQG7](https://www.uniprot.org/uniprotkb/Q9NQG7) · Ensembl [ENSG00000100099](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100099)

## Data

Gene col 1865: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1865); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1865, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1865]; `tensor/DDL_lfc|DDL_z.npy` [1865]; `embed/gene_vectors.npy` [1865]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1865 or target_col == 1865). Every well: [[HPS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HPS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
