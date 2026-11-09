---
symbol: "COMMD2"
type: "gene"
col: 3581
ensembl_id: "ENSG00000114744"
name: "COMM domain containing 2"
location: "3q25.1"
module: 17
arm: "+"
pooled_cpm: 32.85
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# COMMD2

*COMM domain containing 2* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.89× (z +10.0, q 9e-21, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.494× (z -15.7, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA12]] (+0.76, fdr 7e-06), [[METTL5]] (+0.72, fdr 1e-05), [[DNAJC19]] (+0.71, fdr 2e-05); moves opposite to [[STARD4-AS1]] (-0.71, fdr 2e-05), [[SIAH2-AS1]] (-0.71, fdr 4e-05), [[PPP1R15B-AS1]] (-0.70, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3581.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +10.0 | 9e-21 | 46/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +9.2 | 1e-17 | 45/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.79×** | +9.1 | 1e-17 | 45/48 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.55×** | +6.9 | 8e-10 | 26/44 (SW480, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +5.4 | 6e-06 | 29/48 (PANC-1, LS 180, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.32×** | +4.2 | 0.003 | 18/37 (SHP-77, A498, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.29×** | +4.0 | 0.005 | 19/47 (SNU-423, hTERT-HPNE, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +3.8 | 0.009 | 15/44 (NCI-H2030, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.056 | 20/48 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.22×** | +3.1 | 0.087 | 8/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.087 | 11/47 (A-427, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.087 | 10/48 (SHP-77, CFPAC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.23×** | +3.1 | 0.087 | 14/48 (NCI-H23, A-427, …) | two highest doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3581.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.494×** | -15.7 | 0e+00 | 41/47 (MIA PaCa-2, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.606×** | -7.6 | 1e-11 | 30/47 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -3.9 | 0.013 | 25/48 (SW1417, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -3.9 | 0.013 | 1/48 (SW 1271) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.860× | -3.3 | 0.092 | 17/47 (A-172, J82, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.823× | -3.1 | 0.20 | 17/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.824× | -3.0 | 0.20 | 15/48 (RKO, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3581. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 65.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.349× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[NCI-H23 (line)]] | alt | 44.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -11.1) |
| [[SHP-77 (line)]] | alt | 61.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.67× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -13.8) |
| [[SW1417 (line)]] | alt | 39.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -16.8) |
| [[SW480 (line)]] | alt | 32.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -9.9) |
| [[A498 (line)]] | wt | 27.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -10.0) |
| [[A549 (line)]] | wt | 29.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -12.5) |
| [[BT-474 (line)]] | alt | 27.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -11.5) |
| [[C32 (line)]] | wt | 21.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -10.0) |
| [[H4 (line)]] | wt | 24.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0906× (z -16.3) |
| [[HEC-1-A (line)]] | alt | 43.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -8.8) |
| [[HOP62 (line)]] | alt | 22.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -13.7) |
| [[HS-578T (line)]] | alt | 47.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -9.7) |
| [[HT-29 (line)]] | alt | 33.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -8.6) |
| [[LoVo (line)]] | wt | 20.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 36.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -17.8) |
| [[NCI-H2347 (line)]] | alt | 40.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 22.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -13.9) |
| [[NCI-H661 (line)]] | alt | 54.1 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0755× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 57.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -12.6) |
| [[PANC-1 (line)]] | alt | 45.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -9.0) |
| [[RKO (line)]] | wt | 22.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -14.0) |
| [[SW 900 (line)]] | alt | 21.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -9.3) |
| [[A-172 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3581), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA12]] | +0.76 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[METTL5]] | +0.72 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[DNAJC19]] | +0.71 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[MRPS31P4]] | +0.70 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[GPATCH11]] | +0.70 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[DPY30]] | +0.69 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[PUS3]] | +0.68 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[KBTBD6]] | +0.67 | +0.46 / +0.69 | both halves | 2e-05 | pathway: Neddylation; STRING 517 |
| [[NSUN5]] | +0.66 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[WRAP73]] | +0.66 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[UBXN2B]] | +0.66 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[FITM2]] | +0.66 | +0.57 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STARD4-AS1]] | -0.71 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[SIAH2-AS1]] | -0.71 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[PPP1R15B-AS1]] | -0.70 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[ALG1L9P]] | -0.66 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[SAXO1]] | -0.66 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[CPEB2-DT]] | -0.65 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[LINC02955]] | -0.65 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[LNP1]] | -0.63 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[LRP2BP]] | -0.63 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | -0.63 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[CCDC90B-AS1]] | -0.62 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[SNHG31]] | -0.62 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises COMMD2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 0.8% of all compounds | 0.010 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GOLGA2P5-1]] | B | GOLGA2P5-1 activity raises COMMD2's level | lines that do not express GOLGA2P5-1 (8) vs lines expressing it (42) | 1.41× lower at baseline in the lines without GOLGA2P5-1 | 0.022 | ⚠ within organs, on part of the lines; also absent: GOLGA2P5, ENSG00000257489, KCNIP3; maybe low, not absent |
| [[SOGA3]] | B | SOGA3 activity raises COMMD2's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 1.25× lower at baseline in the lines without SOGA3 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.767). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.7, -3.6); signed map (-22.6, -13.4). **Vector** length 98.1, 24.5% of its response variance represented; |z| ≥ 3 in 714 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.5 | +10.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.0 | +9.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.6 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.7 | +5.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.8 | -15.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.4 | -7.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -1.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | COMM domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.1 — chr3:149,738,472-149,752,495 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC042 |
| Gene groups (HGNC) | COMM domain containing |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86X83](https://www.uniprot.org/uniprotkb/Q86X83) (COMM domain-containing protein 2):

> Scaffold protein in the commander complex that is essential for endosomal recycling of transmembrane cargos; the commander complex is composed of the CCC subcomplex and the retriever subcomplex. May modulate activity of cullin-RING E3 ubiquitin ligase (CRL) complexes. May down-regulate activation of NF-kappa-B.

**Summary**, from NCBI Gene [51122](https://www.ncbi.nlm.nih.gov/gene/51122):

> Predicted to be involved in endocytic recycling. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24993](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24993) · Entrez [51122](https://www.ncbi.nlm.nih.gov/gene/51122) · UniProt [Q86X83](https://www.uniprot.org/uniprotkb/Q86X83) · Ensembl [ENSG00000114744](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114744)

## Data

Gene col 3581: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3581); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3581, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3581]; `tensor/DDL_lfc|DDL_z.npy` [3581]; `embed/gene_vectors.npy` [3581]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3581 or target_col == 3581). Every well: [[COMMD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COMMD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
