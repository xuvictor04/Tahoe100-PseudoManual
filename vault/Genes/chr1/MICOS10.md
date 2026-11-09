---
symbol: "MICOS10"
type: "gene"
col: 10384
ensembl_id: "ENSG00000173436"
name: "mitochondrial contact site and cristae organizing system subunit 10"
location: "1p36.13"
module: 14
arm: "+"
pooled_cpm: 32.46
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# MICOS10

*mitochondrial contact site and cristae organizing system subunit 10* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.51× (z +10.3, q 7e-22, up in 43 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +5.2, q 2e-05, up in 38 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (PANC-1 7.77×, HOP62 8.94×, NCI-H460 7.91×, MIA PaCa-2 7.88×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Homoharringtonine (drug)]] 5 µM in 4 lines (HS-578T 7.92×, A-172 6.24×, SNU-423 6.80×, SK-MEL-2 5.68×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (HOP62 8.77×, NCI-H460 7.15×, PANC-1 5.51×, NCI-H1792 10.6×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[GSK1059615 (drug)]] 5 µM: 0.284× (z -3.8, q 0.081, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5MF]] (+0.68, fdr 7e-06), [[NDUFB1]] (+0.60, fdr 4e-05), [[GPHN]] (+0.57, fdr 1e-05); moves opposite to [[RNF216P1]] (-0.63, fdr 1e-05), [[INTS11]] (-0.61, fdr 1e-05), [[TPD52L2]] (-0.59, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAML2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10384.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (PANC-1 7.77×, HOP62 8.94×, NCI-H460 7.91×, MIA PaCa-2 7.88×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Homoharringtonine (drug)]] 5 µM in 4 lines (HS-578T 7.92×, A-172 6.24×, SNU-423 6.80×, SK-MEL-2 5.68×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 4 lines (HOP62 8.77×, NCI-H460 7.15×, PANC-1 5.51×, NCI-H1792 10.6×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **5.51×** | +10.3 | 7e-22 | 43/43 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **4.73×** | +9.4 | 2e-18 | 35/35 (HOP62, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.29×** | +7.0 | 6e-10 | 37/41 (PANC-1, C32, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +5.2 | 2e-05 | 38/47 (SK-MEL-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **1.87×** | +4.0 | 0.006 | 29/45 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.79×** | +3.8 | 0.016 | 30/46 (MIA PaCa-2, LOX-IMVI, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.85×** | +3.7 | 0.017 | 30/48 (A-172, HOP62, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | **1.72×** | +3.3 | 0.078 | 28/47 (C32, NCI-H1792, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.41× | +3.1 | 0.12 | 27/48 (A-172, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.67× | +3.1 | 0.12 | 29/48 (A549, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10384.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **0.284×** | -3.8 | 0.081 | 38/47 (A-427, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.352× | -3.2 | 0.34 | 32/48 (J82, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.596× | -3.0 | 0.34 | 31/48 (NCI-H460, HCT15, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.597× | -3.0 | 0.34 | 30/48 (KATO III, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, +0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10384. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 20.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.37× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HOP62 (line)]] | alt | 21.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.94× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H1792 (line)]] | alt | 17.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.6× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H460 (line)]] | wt | 24.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.91× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[PANC-1 (line)]] | alt | 61.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.77× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 28.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +13.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 41.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.78× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[C32 (line)]] | wt | 19.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.92× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[CFPAC-1 (line)]] | alt | 37.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.37× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[HS-578T (line)]] | alt | 48.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.92× (z +15.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HT-29 (line)]] | alt | 36.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.03× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[J82 (line)]] | alt | 37.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[LoVo (line)]] | wt | 24.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.35× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 32.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.88× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 18.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +11.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-423 (line)]] | alt | 19.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.80× (z +12.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 26.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.72× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW480 (line)]] | alt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.36× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A498 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 53.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10384), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MF]] | +0.68 | +0.59 / +0.76 | both halves | 7e-06 | pathway: Cristae formation; STRING 757 |
| [[NDUFB1]] | +0.60 | +0.42 / +0.73 | both halves | 4e-05 |  |
| [[GPHN]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[PFN1]] | +0.57 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[NDUFC1]] | +0.57 | +0.38 / +0.64 | both halves | 7e-05 |  |
| [[ZNF827]] | +0.57 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[LHFPL6]] | +0.57 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[SSH2]] | +0.56 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[RBX1]] | +0.56 | +0.39 / +0.61 | both halves | 5e-05 |  |
| [[ATAD2B]] | +0.55 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[UNK]] | +0.55 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[PSME2]] | +0.55 | +0.57 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF216P1]] | -0.63 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[INTS11]] | -0.61 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[TPD52L2]] | -0.59 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[ST6GALNAC6]] | -0.54 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[ZNF177]] | -0.54 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[YKT6]] | -0.53 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[CDK9]] | -0.52 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[MSTO2P]] | -0.52 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[FCHSD1]] | -0.52 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[CIZ1]] | -0.51 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[SIN3B]] | -0.51 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[HECTD3]] | -0.51 | -0.58 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAML2]] | B | MAML2 activity strengthens MICOS10's drug response | lines that do not express MAML2 (8) vs lines expressing it (40) | the lines without MAML2 respond 0.63× as strongly (z diff +0.95); strongest at Dinaciclib 5 µM: 2.06x vs 4.90x (z diff +2.4) | 0.093 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.443). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.3, -25.3); signed map (44.4, 0.7). **Vector** length 50.3, 14.5% of its response variance represented; |z| ≥ 3 in 506 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.0 | +0.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +3.5 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | +2.8 | +3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | -0.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | -0.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.0 | +1.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.2 | +0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.2 | +2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.2 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial contact site and cristae organizing system subunit 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:19,484,403-19,629,821 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RP5-1056L3.2, FLJ36999, MIO10, Mic10; previously C1orf151, MINOS1 |
| Gene groups (HGNC) | Mitochondrial contact site and cristae organizing system subunits |
| Reactome | 3 pathways, smallest: Cristae formation; Mitochondrial biogenesis; Organelle biogenesis and maintenance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TGZ0](https://www.uniprot.org/uniprotkb/Q5TGZ0) (MICOS complex subunit MIC10):

> Component of the MICOS complex, a large protein complex of the mitochondrial inner membrane that plays crucial roles in the maintenance of crista junctions, inner membrane architecture, and formation of contact sites to the outer membrane.

**Summary**, from NCBI Gene [440574](https://www.ncbi.nlm.nih.gov/gene/440574):

> Involved in cristae formation. Located in mitochondrion. Part of MIB complex; MICOS complex; and SAM complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:32068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32068) · Entrez [440574](https://www.ncbi.nlm.nih.gov/gene/440574) · UniProt [Q5TGZ0](https://www.uniprot.org/uniprotkb/Q5TGZ0) · Ensembl [ENSG00000173436](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173436)

## Data

Gene col 10384: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10384); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10384, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10384]; `tensor/DDL_lfc|DDL_z.npy` [10384]; `embed/gene_vectors.npy` [10384]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10384 or target_col == 10384). Every well: [[MICOS10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MICOS10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
