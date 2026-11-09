---
symbol: "PSMB1"
type: "gene"
col: 156
ensembl_id: "ENSG00000008018"
name: "proteasome 20S subunit beta 1"
location: "6q27"
module: 12
arm: "+"
pooled_cpm: 80.62
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# PSMB1

*proteasome 20S subunit beta 1* — 6q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 1.91× (z +8.3, q 5e-14, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.702× (z -6.4, q 6e-08, down in 41 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 0.254×, NCI-H23 0.294×, C-33 A 0.262×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (PANC-1 0.568×, LoVo 0.530×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW 1271 0.0710×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NMT1]] (+0.67, fdr 8e-06), [[MMADHC]] (+0.67, fdr 7e-06), [[NDUFA8]] (+0.66, fdr 2e-05); moves opposite to [[CERS2]] (-0.60, fdr 5e-05), [[UBQLN4]] (-0.58, fdr 3e-05), [[PTPN18]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 156.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.91×** | +8.3 | 5e-14 | 48/48 (LoVo, KATO III, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.74×** | +7.1 | 4e-10 | 43/48 (LoVo, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.63×** | +5.9 | 5e-07 | 42/48 (RKO, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.46×** | +4.8 | 2e-04 | 30/48 (LS 180, LoVo, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.45×** | +4.8 | 2e-04 | 34/48 (LS 180, LoVo, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.47×** | +4.8 | 2e-04 | 36/48 (NCI-H460, LS 180, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +4.4 | 8e-04 | 35/48 (C32, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.39×** | +4.2 | 0.002 | 27/48 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.39×** | +4.2 | 0.002 | 33/48 (NCI-H460, PANC-1, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **1.37×** | +3.9 | 0.005 | 29/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | **1.35×** | +3.8 | 0.007 | 28/49 (NCI-H460, A549, …) | inconsistent across doses | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~93% of this change | **1.32×** | +3.6 | 0.016 | 28/48 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.75×** | +3.3 | 0.042 | 25/49 (RKO, RPMI-7951, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.20× | +3.2 | 0.048 | 22/48 (NCI-H460, LOX-IMVI, …) | two highest doses | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.50×** | +3.1 | 0.085 | 28/47 (J82, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 156.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 0.254×, NCI-H23 0.294×, C-33 A 0.262×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (PANC-1 0.568×, LoVo 0.530×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW 1271 0.0710×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -6.4 | 6e-08 | 41/49 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.716×** | -4.1 | 0.010 | 32/48 (hTERT-HPNE, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 156. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 130 | 3 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +11.6) ⚠ cell-cycle shift, explains ~75% of this change | [[Dinaciclib (drug)]] 5 µM 0.254× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 83.6 | 2 (2 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.61× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 57.6 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW48 (line)]] | wt | 106 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 3.30× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 136 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +9.0) ⚠ cell-cycle shift, explains ~75% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -9.2) |
| [[C-33 A (line)]] | alt | 65.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 42.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 63.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1271 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0710× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 77.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 132 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 81.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 70.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 68.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 137 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 86.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 74.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 85.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 156), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMT1]] | +0.67 | +0.58 / +0.71 | both halves | 8e-06 | pathway: Apoptosis |
| [[MMADHC]] | +0.67 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[NDUFA8]] | +0.66 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[MRFAP1]] | +0.63 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[PSMD3]] | +0.63 | +0.64 / +0.57 | both halves | 1e-05 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[CYB5R1]] | +0.63 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[DCTN6]] | +0.63 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[KIAA1143]] | +0.63 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[COA3]] | +0.63 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[ATP5PO]] ⚠ | +0.62 | +0.41 / +0.56 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TRAPPC2B]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[POLR2C]] | +0.62 | +0.61 / +0.52 | both halves | 1e-05 | pathway: HIV Infection |
| [[BRF2]] | +0.62 | +0.66 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CERS2]] | -0.60 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[UBQLN4]] | -0.58 | -0.43 / -0.50 | both halves | 3e-05 | STRING 995 |
| [[PTPN18]] | -0.56 | -0.43 / -0.52 | both halves | 3e-05 | pathway: Interleukin-1 family signaling |
| [[PAXIP1]] | -0.56 | -0.45 / -0.39 | both halves | 5e-05 | pathway: DNA Double-Strand Break Repair |
| [[SEPTIN8]] | -0.54 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[PIGX]] | -0.54 | -0.66 / -0.35 | both halves | 1e-04 |  |
| [[SEPTIN11]] | -0.54 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[GALNT7]] | -0.53 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[CDK2AP1]] | -0.53 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[BCL2L2]] | -0.52 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[RCC2]] | -0.52 | -0.44 / -0.31 | both halves | 2e-04 | pathway: Cell Cycle Checkpoints |
| [[UBTF]] | -0.52 | -0.37 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PSMB1's level | compounds that target TOP2A: 2 of 5 lower it (Doxorubicin, Idarubicin) | 40% of the class's compounds vs 0.6% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.571). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-42.3, -5.9); signed map (-17.9, -8.3). **Vector** length 85.0, 26.6% of its response variance represented; |z| ≥ 3 in 663 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.2 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.2 | +7.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.0 | +2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.6 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.9 | -6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.1 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.1 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.3 | -0.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.2 | -0.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | +0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 20S subunit beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q27 — chr6:170,535,120-170,553,307 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PMSB1, HC5 |
| Gene groups (HGNC) | Proteasome |
| Reactome | 171 pathways, smallest: Antigen processing: Ub, ATP-independent proteasomal degradation; Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC) |
| Matched by | ensembl_id |

**Function**, from UniProt [P20618](https://www.uniprot.org/uniprotkb/P20618) (Proteasome subunit beta type-1):

> Non-catalytic component of the 20S core proteasome complex involved in the proteolytic degradation of most intracellular proteins. This complex plays numerous essential roles within the cell by associating with different regulatory particles. Associated with two 19S regulatory particles, forms the 26S proteasome and thus participates in the ATP-dependent degradation of ubiquitinated proteins. The 26S proteasome plays a key role in the maintenance of protein homeostasis by removing misfolded or …

**Summary**, from NCBI Gene [5689](https://www.ncbi.nlm.nih.gov/gene/5689):

> The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent process in a non-lysosomal pathway. An essential function of a modified proteasome, the …

**Accessions** — [HGNC:9537](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9537) · Entrez [5689](https://www.ncbi.nlm.nih.gov/gene/5689) · UniProt [P20618](https://www.uniprot.org/uniprotkb/P20618) · Ensembl [ENSG00000008018](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008018)

## Data

Gene col 156: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 156); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 156, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 156]; `tensor/DDL_lfc|DDL_z.npy` [156]; `embed/gene_vectors.npy` [156]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 156 or target_col == 156). Every well: [[PSMB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
