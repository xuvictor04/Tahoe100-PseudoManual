---
symbol: "POMT2"
type: "gene"
col: 192
ensembl_id: "ENSG00000009830"
name: "protein O-mannosyltransferase 2"
location: "14q24.3"
module: 36
arm: "+"
pooled_cpm: 12.52
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# POMT2

*protein O-mannosyltransferase 2* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.86× (z +9.5, q 1e-18, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.631× (z -7.3, q 2e-10, down in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.208×, Panc 03.27 0.235×, SW48 0.305×; ⚠ cell-cycle shift, explains ~85% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW48 0.102×, SK-MEL-2 0.213×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SW48 0.125×, A-427 0.263×; ⚠ cell-cycle shift, explains ~26% of this change); [[Vilanterol (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0663×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0863×); [[Orlistat (drug)]] 0.05 µM in 1 line (SNU-1 0.0750×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP5]] (+0.69, fdr 7e-06), [[HSF1]] (+0.66, fdr 7e-06), [[POLR3E]] (+0.65, fdr 7e-06); moves opposite to [[SNAPC1]] (-0.55, fdr 1e-05), [[PIM3]] (-0.55, fdr 2e-05), [[TXNIP]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TXNIP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 192.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.86×** | +9.5 | 1e-18 | 36/47 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.76×** | +9.2 | 2e-17 | 32/47 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +6.6 | 6e-09 | 23/47 (SW480, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.13×** | +6.4 | 2e-08 | 25/44 (C32, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +5.1 | 3e-05 | 16/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +4.4 | 1e-03 | 14/47 (LoVo, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.9 | 0.007 | 9/38 (HOP62, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.011 | 13/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.18× | +3.7 | 0.016 | 12/46 (NCI-H2347, HEC-1-A, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.079 | 6/47 (HT-29, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[crizotinib (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.079 | 5/47 (NCI-H1573, HepG2/C3A, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.100 | 6/45 (NCI-H1792, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 192.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.208×, Panc 03.27 0.235×, SW48 0.305×; ⚠ cell-cycle shift, explains ~85% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW48 0.102×, SK-MEL-2 0.213×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SW48 0.125×, A-427 0.263×; ⚠ cell-cycle shift, explains ~26% of this change); [[Vilanterol (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0663×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0863×); [[Orlistat (drug)]] 0.05 µM in 1 line (SNU-1 0.0750×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.631×** | -7.3 | 2e-10 | 28/47 (MIA PaCa-2, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.666×** | -6.6 | 8e-09 | 26/47 (AN3 CA, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.777×** | -4.1 | 0.006 | 19/45 (SW48, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | 0.847× | -3.9 | 0.014 | 22/47 (MIA PaCa-2, Panc 03.27, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | 0.829× | -3.1 | 0.22 | 10/47 (KATO III, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | 0.826× | -3.0 | 0.23 | 8/47 (AN3 CA, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 192. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -11.4) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.174× (z -8.6) |
| [[SW48 (line)]] | wt | 34.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 0 | 2 | — | [[Vilanterol (drug)]] 0.05 µM 0.0663× (z -11.2) |
| [[A-427 (line)]] | wt | 19.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 26.5 | 0 | 1 | — | [[Sulfatinib (drug)]] 5 µM 0.0775× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 4.99 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0938× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 21.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +8.8) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[J82 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -8.8) ⚠ cell-cycle shift, explains ~85% of this change |
| [[LOX-IMVI (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0423× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[NCI-H2030 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[Panc 03.27 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -11.3) ⚠ cell-cycle shift, explains ~85% of this change |
| [[SK-MEL-2 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 13.7 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0750× (z -9.9) |
| [[SNU-423 (line)]] | alt | 11.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +10.3) ⚠ cell-cycle shift, explains ~85% of this change | — |
| [[A-172 (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 192), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP5]] | +0.69 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[HSF1]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[POLR3E]] | +0.65 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[DDX54]] | +0.63 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[HERC2]] | +0.62 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[THOC5]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.62 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ERI3]] | +0.62 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[ELAC2]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[PEMT]] | +0.61 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[NCK2]] | +0.61 | +0.63 / +0.57 | both halves | 9e-06 | pathway: Cell-Cell communication |
| [[TRRAP]] | +0.60 | +0.64 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAPC1]] | -0.55 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[PIM3]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[TXNIP]] | -0.55 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[METTL23]] | -0.55 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[RNF19A]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[H3-3B]] | -0.54 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[ABCA5]] | -0.53 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[HMGCL]] | -0.52 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[BTG1]] | -0.51 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[H2AJ]] | -0.51 | -0.53 / -0.48 | both halves | 2e-05 | pathway: Adherens junctions interactions |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TXNIP]] | B | TXNIP activity lowers POMT2's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.51× higher at baseline in the lines without TXNIP | 0.006 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.642). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-8.2, -30.7); signed map (-16.2, -51.1). **Vector** length 75.7, 12.6% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.0 | +9.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.3 | +9.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +6.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +6.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +2.9 | +3.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +2.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.8 | +3.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.6 | -7.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.0 | -6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | -3.5 | -3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | protein O-mannosyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:77,274,956-77,320,883 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LGMD2N |
| Gene groups (HGNC) | Dolichyl D-mannosyl phosphate dependent mannosyltransferases |
| Reactome | 18 pathways, smallest: Defective POMT1 causes MDDGA1, MDDGB1 and MDDGC1; Defective POMT2 causes MDDGA2, MDDGB2 and MDDGC2; DAG1 core M1 glycosylations |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKY4](https://www.uniprot.org/uniprotkb/Q9UKY4) (Protein O-mannosyl-transferase 2):

> Transfers mannosyl residues to the hydroxyl group of serine or threonine residues. Coexpression of both POMT1 and POMT2 is necessary for enzyme activity, expression of either POMT1 or POMT2 alone is insufficient. Essentially dedicated to O-mannosylation of alpha-DAG1 and few other proteins but not of cadherins and protocaherins.

**Summary**, from NCBI Gene [29954](https://www.ncbi.nlm.nih.gov/gene/29954):

> The protein encoded by this gene is an O-mannosyltransferase that requires interaction with the product of the POMT1 gene for enzymatic function. The encoded protein is found in the membrane of the endoplasmic reticulum. Defects in this gene are a cause of Walker-Warburg syndrome (WWS).[provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:19743](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19743) · Entrez [29954](https://www.ncbi.nlm.nih.gov/gene/29954) · UniProt [Q9UKY4](https://www.uniprot.org/uniprotkb/Q9UKY4) · Ensembl [ENSG00000009830](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000009830)

## Data

Gene col 192: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 192); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 192, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 192]; `tensor/DDL_lfc|DDL_z.npy` [192]; `embed/gene_vectors.npy` [192]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 192 or target_col == 192). Every well: [[POMT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POMT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
