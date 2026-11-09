---
symbol: "SLC35B2"
type: "gene"
col: 8086
ensembl_id: "ENSG00000157593"
name: "solute carrier family 35 member B2"
location: "6p21.1"
module: 135
arm: "-"
pooled_cpm: 16.53
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# SLC35B2

*solute carrier family 35 member B2* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.36× (z +7.2, q 3e-10, up in 28 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (RPMI-7951 6.66×, HOP62 3.51×, hTERT-HPNE 5.42×, C32 6.19×, …; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 4.68×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.534× (z -5.3, q 6e-05, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VWA1]] (+0.59, fdr 1e-04), [[CYBA]] (+0.59, fdr 9e-05), [[ZDHHC12]] (+0.58, fdr 2e-05); moves opposite to [[ZNF343]] (-0.61, fdr 2e-04), [[CCT6P1]] (-0.61, fdr 3e-05), [[ZFR]] (-0.58, fdr 2e-05).
> It sits in the **-** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8086.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (RPMI-7951 6.66×, HOP62 3.51×, hTERT-HPNE 5.42×, C32 6.19×, …; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 4.68×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.36×** | +7.2 | 3e-10 | 28/36 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.22×** | +6.4 | 3e-08 | 25/30 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.76×** | +4.8 | 4e-04 | 32/44 (SW1417, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.67×** | +4.3 | 0.002 | 28/46 (NCI-H460, PANC-1, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.65×** | +3.9 | 0.010 | 18/33 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8086.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.534×** | -5.3 | 6e-05 | 32/47 (LS 180, HCT15, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.531×** | -5.1 | 1e-04 | 34/48 (A-172, A498, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.333×** | -4.9 | 2e-04 | 31/43 (NCI-H1792, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.554×** | -4.8 | 2e-04 | 32/47 (SK-MEL-2, HT-29, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.617×** | -4.1 | 0.005 | 27/47 (C32, RKO, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.674×** | -3.3 | 0.078 | 19/48 (H4, A498, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.686× | -3.0 | 0.21 | 19/47 (AN3 CA, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.62 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8086. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 21.7 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.390× (z -8.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -8.7) |
| [[A-172 (line)]] | wt | 31.0 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.238× (z -9.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 10.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 31.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.151× (z -8.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 14.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -10.3) |
| [[HOP62 (line)]] | alt | 23.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +11.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HT-29 (line)]] | alt | 21.1 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.205× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +11.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 8.66 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0178× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 13.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.68× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[RPMI-7951 (line)]] | alt | 20.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.66× (z +12.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 1 | — | [[Almonertinib (hydrochloride) (drug)]] 5 µM 0.253× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.156× (z -8.5) |
| [[SNU-423 (line)]] | alt | 21.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-427 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.72 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8086), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VWA1]] | +0.59 | +0.55 / +0.35 | both halves | 1e-04 |  |
| [[CYBA]] | +0.59 | +0.58 / +0.36 | both halves | 9e-05 |  |
| [[ZDHHC12]] | +0.58 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[NRM]] | +0.57 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[GDF11]] | +0.55 | +0.56 / +0.29 | both halves | 2e-04 |  |
| [[A2MP1]] | +0.54 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[TTYH3]] | +0.53 | +0.62 / +0.30 | both halves | 2e-04 |  |
| [[HYAL2]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 | pathway: Glycosaminoglycan metabolism |
| [[EML4]] | +0.52 | +0.43 / +0.23 | both halves | 5e-04 |  |
| [[STX10]] | +0.51 | +0.58 / +0.28 | both halves | 3e-04 |  |
| [[JPT1]] | +0.51 | +0.31 / +0.54 | both halves | 2e-04 |  |
| [[GUSBP18]] | +0.51 | +0.30 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF343]] | -0.61 | -0.62 / -0.30 | both halves | 2e-04 |  |
| [[CCT6P1]] | -0.61 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[ZFR]] | -0.58 | -0.58 / -0.47 | both halves | 2e-05 | same gene group |
| [[ANGEL2]] | -0.56 | -0.56 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[SMARCAL1]] | -0.55 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[TSR2]] | -0.55 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[RNF6]] | -0.54 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[FAIM]] | -0.53 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[ZNF391]] | -0.53 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[ANKAR]] | -0.52 | -0.42 / -0.24 | both halves | 5e-04 |  |
| [[TYW3]] | -0.52 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[C8orf33]] | -0.51 | -0.32 / -0.20 | both halves | 7e-04 |  |
| [[PSMC5]] | -0.51 | -0.46 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises SLC35B2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **-** arm (projection on the module's main direction -0.602). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-17.9, 18.1); signed map (-37.8, 14.1). **Vector** length 73.6, 16.9% of its response variance represented; |z| ≥ 3 in 648 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | +4.6 | +4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.4 | +0.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | -0.5 |
|  | [[Flutamide (drug)]] 5 µM |  | +1.3 | +1.6 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.2 | +2.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.1 | +2.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.3 | -5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | -5.3 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.6 | -4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.3 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:44,254,096-44,257,890 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UGTrel4 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Solute carrier family 35 |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME |
| Reactome | 7 pathways, smallest: Transport and metabolism of PAPS; Transport of nucleotide sugars; Transport of vitamins, nucleosides, and related molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TB61](https://www.uniprot.org/uniprotkb/Q8TB61) (Adenosine 3'-phospho 5'-phosphosulfate transporter 1):

> Probably functions as a 3'-phosphoadenylyl sulfate:adenosine 3',5'-bisphosphate antiporter at the Golgi membranes. Mediates the transport from the cytosol into the lumen of the Golgi of 3'-phosphoadenylyl sulfate/adenosine 3'-phospho 5'-phosphosulfate (PAPS), a universal sulfuryl donor for sulfation events that take place in that compartment.

**Summary**, from NCBI Gene [347734](https://www.ncbi.nlm.nih.gov/gene/347734):

> Sulfotransferases (e.g., SULT4A1; MIM 608359) use an activated form of sulfate, 3-prime-phosphoadenosine 5-prime-phosphosulfate (PAPS), as a common sulfate donor for sulfation of glycoproteins, proteoglycans, and glycolipids in the endoplasmic reticulum and Golgi apparatus. SLC35B2 is located in the microsomal membrane and transports PAPS from the cytosol, where it is synthesized, into the Golgi lumen (Kamiyama et al., 2003 [PubMed 12716889]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:16872](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16872) · Entrez [347734](https://www.ncbi.nlm.nih.gov/gene/347734) · UniProt [Q8TB61](https://www.uniprot.org/uniprotkb/Q8TB61) · Ensembl [ENSG00000157593](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157593)

## Data

Gene col 8086: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8086); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8086, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8086]; `tensor/DDL_lfc|DDL_z.npy` [8086]; `embed/gene_vectors.npy` [8086]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8086 or target_col == 8086). Every well: [[SLC35B2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35B2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
