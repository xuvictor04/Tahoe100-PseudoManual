---
symbol: "ZKSCAN8"
type: "gene"
col: 12570
ensembl_id: "ENSG00000198315"
name: "zinc finger with KRAB and SCAN domains 8"
location: "6p22.1"
module: 94
arm: "+"
pooled_cpm: 36.34
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# ZKSCAN8

*zinc finger with KRAB and SCAN domains 8* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.62× (z +7.6, q 1e-11, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.555× (z -6.4, q 9e-08, down in 25 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Azithromycin (hydrate) (drug)]] 5 µM: 0.803× (z -3.5, q 0.087, down in 22 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HCT15 0.0997×, C-33 A 0.171×, A-427 0.203×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HCT15 0.209×, Panc 03.27 0.280×, NCI-H23 0.354×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 2 lines (COLO 205 0.101×, CHP-212 0.126×); [[Hydroxyfasudil (drug)]] 5 µM in 1 line (HCT15 0.0631×); [[Berberine (chloride hydrate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0907×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF740]] (+0.60, fdr 4e-05), [[ALG10B]] (+0.58, fdr 4e-05), [[HINT3]] (+0.57, fdr 1e-05); moves opposite to [[ACAP2]] (-0.56, fdr 6e-05), [[RBM6]] (-0.55, fdr 8e-05), [[ADIPOR2]] (-0.51, fdr 4e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CFL2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12570.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +7.6 | 1e-11 | 35/46 (HT-29, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.68×** | +5.8 | 2e-06 | 31/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +5.0 | 9e-05 | 27/46 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.35×** | +4.8 | 2e-04 | 31/46 (Panc 03.27, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +4.6 | 6e-04 | 28/46 (HS-578T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +4.1 | 0.004 | 28/46 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.77×** | +3.4 | 0.063 | 21/46 (LS 180, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.2 | 0.095 | 15/46 (LOX-IMVI, RKO, …) | all doses, stronger at high dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.35× | +3.1 | 0.12 | 15/46 (J82, HEC-1-A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12570.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HCT15 0.0997×, C-33 A 0.171×, A-427 0.203×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HCT15 0.209×, Panc 03.27 0.280×, NCI-H23 0.354×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Glycyrrhizic acid (drug)]] 0.05 µM in 2 lines (COLO 205 0.101×, CHP-212 0.126×); [[Hydroxyfasudil (drug)]] 5 µM in 1 line (HCT15 0.0631×); [[Berberine (chloride hydrate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0907×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.555×** | -6.4 | 9e-08 | 25/39 (HCT15, C-33 A, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.611×** | -5.6 | 8e-06 | 33/44 (HCT15, Panc 03.27, …) | rises with dose | composition shift |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **0.803×** | -3.5 | 0.087 | 22/46 (HOP62, HCT15, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12570. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 54.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0997× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Hydroxyfasudil (drug)]] 5 µM 0.0631× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 51.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.12× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 35.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -11.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 60.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -12.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 58.3 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.126× (z -9.5) |
| [[COLO 205 (line)]] | alt | 18.7 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.101× (z -9.6) |
| [[HOP62 (line)]] | alt | 50.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 35.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 18.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +11.7) | — |
| [[J82 (line)]] | alt | 67.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 56.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SNU-1 (line)]] | wt | 51.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -9.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 60.6 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 0.5 µM 0.0907× (z -8.9) |
| [[A-172 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 43.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12570), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF740]] | +0.60 | +0.41 / +0.54 | both halves | 4e-05 | same gene group |
| [[ALG10B]] | +0.58 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[HINT3]] | +0.57 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ZNF627]] | +0.57 | +0.50 / +0.40 | both halves | 5e-05 | same gene group |
| [[ZBTB26]] | +0.57 | +0.41 / +0.48 | both halves | 4e-05 | same gene group |
| [[TBCEL]] | +0.56 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[ZC3HAV1L]] | +0.56 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[LINC00938]] | +0.56 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[CIPC]] | +0.55 | +0.36 / +0.59 | both halves | 1e-04 |  |
| [[ZNF391]] | +0.55 | +0.45 / +0.41 | both halves | 4e-05 | same gene group |
| [[ZNF564]] | +0.54 | +0.34 / +0.47 | both halves | 1e-04 | same gene group |
| [[LINC01139]] | +0.54 | +0.42 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACAP2]] | -0.56 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[RBM6]] | -0.55 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[ADIPOR2]] | -0.51 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[PI4KA]] | -0.51 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[MYO1E]] | -0.49 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[IL9RP3]] | -0.48 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[UCKL1-AS1]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[SLC66A2]] | -0.48 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[TYW1B]] | -0.48 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[RRBP1]] | -0.47 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[DNAJC1]] | -0.47 | -0.23 / -0.38 | both halves | 5e-04 |  |
| [[CORO2A]] | -0.47 | -0.40 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFL2]] | C | CFL2 activity raises ZKSCAN8's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 1.97× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.512). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.4, 20.8); signed map (-12.9, -38.7). **Vector** length 72.5, 15.3% of its response variance represented; |z| ≥ 3 in 726 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +6.0 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +2.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.0 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +1.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +1.5 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -2.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +1.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.9 | -1.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.8 | -1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger with KRAB and SCAN domains 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:28,141,883-28,159,460 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LD5-1, ZSCAN40; previously ZNF192 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15776](https://www.uniprot.org/uniprotkb/Q15776) (Zinc finger protein with KRAB and SCAN domains 8):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7745](https://www.ncbi.nlm.nih.gov/gene/7745):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in cytosol and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:12983](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12983) · Entrez [7745](https://www.ncbi.nlm.nih.gov/gene/7745) · UniProt [Q15776](https://www.uniprot.org/uniprotkb/Q15776) · Ensembl [ENSG00000198315](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198315)

## Data

Gene col 12570: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12570); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12570, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12570]; `tensor/DDL_lfc|DDL_z.npy` [12570]; `embed/gene_vectors.npy` [12570]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12570 or target_col == 12570). Every well: [[ZKSCAN8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZKSCAN8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
