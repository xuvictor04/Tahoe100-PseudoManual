---
symbol: "PLCG1"
type: "gene"
col: 4493
ensembl_id: "ENSG00000124181"
name: "phospholipase C gamma 1"
location: "20q12"
module: 50
arm: "+"
pooled_cpm: 35.62
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# PLCG1

*phospholipase C gamma 1* — 20q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.52× (z +7.9, q 1e-12, up in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Selinexor (drug)]] 0.05 µM: 1.78× (z +7.8, q 3e-12, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.685× (z -5.1, q 2e-04, down in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.731× (z -4.3, q 0.006, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (AN3 CA 0.264×, BT-474 0.353×; ⚠ cell-cycle shift, would explain all of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (HCT15 0.189×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.374×; ⚠ cell-cycle shift, explains ~51% of this change); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (CHP-212 0.114×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHANK3]] (+0.63, fdr 1e-05), [[NECAB3]] (+0.63, fdr 1e-05), [[PFKM]] (+0.63, fdr 7e-06); moves opposite to [[ZKSCAN1]] (-0.59, fdr 1e-05), [[RAB33B-AS1]] (-0.56, fdr 1e-05), [[IGIP]] (-0.54, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[DZIP1L]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4493.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.52×** | +7.9 | 1e-12 | 40/48 (PANC-1, HT-29, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.78×** | +7.8 | 3e-12 | 43/48 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.61×** | +6.4 | 3e-08 | 31/48 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.60×** | +6.3 | 4e-08 | 31/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.38×** | +6.1 | 9e-08 | 26/48 (A498, A549, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.50×** | +5.4 | 5e-06 | 28/48 (CFPAC-1, AsPC-1, …) | rises with dose | position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.41×** | +4.7 | 2e-04 | 27/48 (HT-29, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +4.7 | 2e-04 | 24/48 (A549, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.41×** | +4.6 | 2e-04 | 30/48 (PANC-1, HT-29, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +4.6 | 3e-04 | 28/48 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **1.36×** | +4.0 | 0.003 | 20/38 (A-172, PANC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.34×** | +4.0 | 0.004 | 26/48 (HOP62, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.007 | 20/48 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.30×** | +3.3 | 0.038 | 20/48 (SNU-423, NCI-H460, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4493.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (AN3 CA 0.264×, BT-474 0.353×; ⚠ cell-cycle shift, would explain all of this change); [[Saquinavir (drug)]] 0.5 µM in 1 line (HCT15 0.189×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.374×; ⚠ cell-cycle shift, explains ~51% of this change); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (CHP-212 0.114×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.685×** | -5.1 | 2e-04 | 28/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.731×** | -4.3 | 0.006 | 25/48 (LoVo, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~20% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.752×** | -3.9 | 0.020 | 25/47 (NCI-H2030, LOX-IMVI, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.774×** | -3.5 | 0.058 | 21/48 (NCI-H2030, LOX-IMVI, …) | all doses, flat | composition shift; position effect removed |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.837× | -3.4 | 0.058 | 21/48 (MIA PaCa-2, SW 900, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.778×** | -3.4 | 0.058 | 18/48 (SNU-1, PANC-1, …) | all doses, flat | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.710×** | -3.3 | 0.074 | 19/48 (HS-578T, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4493. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 95.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 13.0 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 0.05 µM 5.24× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 26.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.26× (z +10.2) ⚠ cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.374× (z -8.6) ⚠ cell-cycle shift, explains ~51% of this change |
| [[A498 (line)]] | wt | 26.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.9) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A549 (line)]] | wt | 14.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +8.6) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[BT-474 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 42.3 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.114× (z -8.6) |
| [[HCT15 (line)]] | alt | 28.5 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.189× (z -8.8) |
| [[SW1417 (line)]] | alt | 72.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 99.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 71.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 68.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 74.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 56.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4493), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHANK3]] | +0.63 | +0.70 / +0.55 | both halves | 1e-05 | same gene group; pathway: RET signaling |
| [[NECAB3]] | +0.63 | +0.68 / +0.49 | both halves | 1e-05 | same gene group |
| [[PFKM]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 | same gene group |
| [[KAT2A]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[RPSA]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[LLGL1]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[PTGFRN]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[CNPY3]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[TATDN2]] | +0.59 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[PLBD2]] | +0.59 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[MAPK12]] | +0.58 | +0.64 / +0.47 | both halves | 2e-05 | pathway: Signaling by NTRK1 (TRKA) |
| [[USP5]] | +0.57 | +0.66 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZKSCAN1]] | -0.59 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[RAB33B-AS1]] | -0.56 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[IGIP]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SMIM14]] | -0.54 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[XIAP]] | -0.53 | -0.57 / -0.45 | both halves | 3e-05 | pathway: Intracellular signaling by second messengers |
| [[BTG1]] | -0.53 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[KRT10]] ⚠ | -0.52 | -0.59 / -0.45 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PURA]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[CCDC186]] | -0.52 | -0.44 / -0.55 | both halves | 3e-05 | same gene group |
| [[RNF19A]] | -0.52 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[EIF1]] | -0.52 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[BET1]] | -0.51 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[CREB1]] | -0.50 | -0.49 / -0.49 | both halves | 1e-05 | pathway: Anti-inflammatory response favouring Leishmania parasite infection; STRING 418 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DZIP1L]] | B | DZIP1L activity raises PLCG1's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 1.93× lower at baseline in the lines without DZIP1L | 0.007 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[AGR2]] | B | AGR2 activity lowers PLCG1's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.82× higher at baseline in the lines without AGR2 | 0.020 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[DZIP1L]] | B | DZIP1L activity weakens PLCG1's drug response | lines that do not express DZIP1L (8) vs lines expressing it (40) | the lines without DZIP1L respond 1.70× as strongly (z diff -1.75); strongest at Idarubicin (hydrochloride) 5 µM: 2.10x vs 1.31x (z diff -3.2) | 0.026 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SEPTIN5]] | B | SEPTIN5 activity raises PLCG1's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.31× lower at baseline in the lines without SEPTIN5 | 0.075 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[FGD1]] | B | FGD1 activity raises PLCG1's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.64× lower at baseline in the lines without FGD1 | 0.084 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[TEAD2]] | B | TEAD2 activity raises PLCG1's level | lines that do not express TEAD2 (9) vs lines expressing it (41) | 1.56× lower at baseline in the lines without TEAD2 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, SLC6A16, FBXO17 |
| [[MAPK9]] | C | MAPK9's natural level weakens PLCG1's drug response | MAPK9's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.37; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.6, -27.2); signed map (-27.9, -32.5). **Vector** length 106, 26.5% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +8.7 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | +6.0 | +4.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +5.5 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +5.1 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.0 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.8 | +2.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.7 | +1.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.7 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -6.7 | -5.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.7 | -2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.5 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.2 | -4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.1 | -3.3 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase C gamma 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q12 — chr20:41,136,960-41,196,801 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PLC148, PLC-II, PLCgamma1, NCKAP3; previously PLC1 |
| Gene groups (HGNC) | Phospholipases; Pleckstrin homology domain containing; SH2 domain containing; C2 domain containing phospholipases; EF-hand domain containing; MicroRNA protein coding host genes |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, APICAL_JUNCTION |
| Reactome | 82 pathways, smallest: Activated NTRK2 signals through PLCG1; Activated NTRK3 signals through PLCG1; PLC-gamma1 signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [P19174](https://www.uniprot.org/uniprotkb/P19174) (1-phosphatidylinositol 4,5-bisphosphate phosphodiesterase gamma-1):

> Mediates the production of the second messenger molecules diacylglycerol (DAG) and inositol 1,4,5-trisphosphate (IP3). Plays an important role in the regulation of intracellular signaling cascades. Becomes activated in response to ligand-mediated activation of receptor-type tyrosine kinases, such as PDGFRA, PDGFRB, EGFR, FGFR1, FGFR2, FGFR3 and FGFR4 (By similarity). Plays a role in actin reorganization and cell migration. Guanine nucleotide exchange factor that binds the GTPase DNM1 and …

**Summary**, from NCBI Gene [5335](https://www.ncbi.nlm.nih.gov/gene/5335):

> The protein encoded by this gene catalyzes the formation of inositol 1,4,5-trisphosphate and diacylglycerol from phosphatidylinositol 4,5-bisphosphate. This reaction uses calcium as a cofactor and plays an important role in the intracellular transduction of receptor-mediated tyrosine kinase activators. For example, when activated by SRC, the encoded protein causes the Ras guanine nucleotide exchange factor RasGRP1 to translocate to the Golgi, where it activates Ras. Also, this protein has been …

**Accessions** — [HGNC:9065](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9065) · Entrez [5335](https://www.ncbi.nlm.nih.gov/gene/5335) · UniProt [P19174](https://www.uniprot.org/uniprotkb/P19174) · Ensembl [ENSG00000124181](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124181)

## Data

Gene col 4493: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4493); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4493, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4493]; `tensor/DDL_lfc|DDL_z.npy` [4493]; `embed/gene_vectors.npy` [4493]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4493 or target_col == 4493). Every well: [[PLCG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLCG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
