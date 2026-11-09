---
symbol: "PRR7"
type: "gene"
col: 5184
ensembl_id: "ENSG00000131188"
name: "proline rich 7, synaptic"
location: "5q35.3"
module: 206
arm: "+"
pooled_cpm: 7.55
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/206"]
generated_by: "tahoemap"
---

# PRR7

*proline rich 7, synaptic* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (9 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.03× (z +7.2, q 2e-10, up in 26 of 35 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.44× (z +5.4, q 7e-06, up in 21 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A549 5.67×, PANC-1 2.84×, NCI-H1573 6.30×; ⚠ cell-cycle shift, explains ~68% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1573 14.9×; ⚠ cell-cycle shift, explains ~50% of this change).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.619× (z -5.1, q 2e-04, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHLDB1]] (+0.62, fdr 1e-05), [[FIBP]] (+0.60, fdr 7e-06), [[S100A3]] (+0.58, fdr 1e-05); moves opposite to [[POLR2B]] (-0.53, fdr 4e-05), [[LAPTM4A]] (-0.51, fdr 3e-05), [[TTC14]] (-0.49, fdr 3e-05).
> It is in [[Module 206]], a single-armed module (Constitutive Signaling by Aberrant PI3K in Cancer).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5184.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A549 5.67×, PANC-1 2.84×, NCI-H1573 6.30×; ⚠ cell-cycle shift, explains ~68% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1573 14.9×; ⚠ cell-cycle shift, explains ~50% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +7.2 | 2e-10 | 26/35 (KATO III, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.62×** | +7.2 | 2e-10 | 24/42 (A549, PANC-1, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.78×** | +6.1 | 2e-07 | 20/38 (A-172, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.74×** | +5.6 | 3e-06 | 25/45 (NCI-H1573, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.4 | 7e-06 | 21/43 (A549, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.58×** | +4.8 | 1e-04 | 20/42 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.50×** | +4.3 | 0.001 | 14/30 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.49×** | +4.1 | 0.004 | 5/16 (HEC-1-A, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.39×** | +3.5 | 0.033 | 16/46 (A549, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.3 | 0.057 | 11/40 (KATO III, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5184.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.619×** | -5.1 | 2e-04 | 23/47 (SK-MEL-2, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.677×** | -4.1 | 0.010 | 20/45 (C-33 A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.678×** | -3.8 | 0.025 | 17/44 (C32, NCI-H2030, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.702×** | -3.8 | 0.025 | 16/47 (J82, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.707×** | -3.7 | 0.026 | 18/45 (NCI-H23, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.666×** | -3.5 | 0.038 | 10/47 (C32, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.703×** | -3.4 | 0.049 | 8/48 (C32, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.719×** | -3.4 | 0.053 | 18/44 (COLO 205, SK-MEL-2, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.571× | -3.1 | 0.12 | 10/47 (RPMI-7951, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.573× | -3.1 | 0.12 | 8/46 (C-33 A, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5184. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 3.77 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +8.6) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[A549 (line)]] | wt | 5.67 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.67× (z +10.2) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[C-33 A (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.195× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 9.31 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0777× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 13.4 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0463× (z -8.6) |
| [[PANC-1 (line)]] | alt | 8.93 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.4) ⚠ cell-cycle shift, explains ~68% of this change | — |
| [[SHP-77 (line)]] | alt | 5.84 | 0 | 1 | — | [[Bergenin (drug)]] 0.05 µM 0.0664× (z -10.3) |
| [[A-172 (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5184), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHLDB1]] | +0.62 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[FIBP]] | +0.60 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[S100A3]] | +0.58 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[PRR7-AS1]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[EPOP]] | +0.58 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[FBXL6]] | +0.58 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[N4BP3]] | +0.57 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[EGR3]] | +0.56 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[EGR2]] | +0.56 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[DOT1L]] | +0.56 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[BCL2L12]] | +0.54 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[F12]] | +0.54 | +0.49 / +0.57 | both halves | 1e-05 | ⚠ same locus (29.9 kb: neighbours can correlate without regulation) |
| [[FBXO41]] | +0.53 | +0.67 / +0.29 | both halves | 2e-04 |  |
| [[RIN1]] | +0.53 | +0.48 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2B]] | -0.53 | -0.40 / -0.60 | both halves | 4e-05 |  |
| [[LAPTM4A]] | -0.51 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[TTC14]] | -0.49 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ILRUN]] | -0.48 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[SOAT1]] | -0.48 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[MTPN]] | -0.47 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[WWP1]] | -0.46 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[SNX3]] | -0.45 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[LURAP1L]] | -0.45 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[PPHLN1]] | -0.45 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[TM9SF2]] | -0.45 | -0.41 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises PRR7's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 206]] — Constitutive Signaling by Aberrant PI3K in Cancer; 15 genes; every member is in the + arm (projection on the module's main direction 0.616). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.9, -2.7); signed map (9.3, 22.7). **Vector** length 65.7, 10.9% of its response variance represented; |z| ≥ 3 in 781 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +6.2 | +7.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +5.1 | +5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.8 | +4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.2 | +3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +1.6 |
|  | [[SBI-0640756 (drug)]] 5 µM |  | +0.9 | +0.6 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +0.8 | +1.2 |
|  | [[Pimitespib (drug)]] 5 µM |  | +0.8 | +1.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -3.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.5 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.4 | -4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | -2.4 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -2.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | proline rich 7, synaptic |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:177,446,445-177,456,286 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10772 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TB68](https://www.uniprot.org/uniprotkb/Q8TB68) (Proline-rich protein 7):

> Acts as a synapse-to-nucleus messenger to promote NMDA receptor-mediated excitotoxicity in neurons in a JUN-dependent manner (By similarity). Inhibits ubiquitination-mediated degradation and promotes phosphorylation and transcriptional activity of transcription factor JUN. Might play a redundant role in the regulation of T cell receptor signaling. Might promote apoptosis in T cells.

**Summary**, from NCBI Gene [80758](https://www.ncbi.nlm.nih.gov/gene/80758):

> Enables long-chain fatty acid binding activity; protein tyrosine kinase binding activity; and ubiquitin-like protein ligase binding activity. Involved in positive regulation of apoptotic process and regulation of transcription by RNA polymerase I. Located in several cellular components, including cytosol; nucleoplasm; and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28130](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28130) · Entrez [80758](https://www.ncbi.nlm.nih.gov/gene/80758) · UniProt [Q8TB68](https://www.uniprot.org/uniprotkb/Q8TB68) · Ensembl [ENSG00000131188](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131188)

## Data

Gene col 5184: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5184); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5184, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5184]; `tensor/DDL_lfc|DDL_z.npy` [5184]; `embed/gene_vectors.npy` [5184]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5184 or target_col == 5184). Every well: [[PRR7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRR7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
