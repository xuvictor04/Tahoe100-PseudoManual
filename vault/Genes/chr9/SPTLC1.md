---
symbol: "SPTLC1"
type: "gene"
col: 1609
ensembl_id: "ENSG00000090054"
name: "serine palmitoyltransferase long chain base subunit 1"
location: "9q22.31"
module: 20
arm: "+"
pooled_cpm: 105.41
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# SPTLC1

*serine palmitoyltransferase long chain base subunit 1* — 9q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.37× (z +5.0, q 4e-04, up in 29 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.160×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.145×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.335×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SW 1088 0.0985×); [[Doxycycline (monohydrate) (drug)]] 0.05 µM in 1 line (SW 1088 0.0946×); [[Tetracycline (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1088 0.106×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMU1]] (+0.72, fdr 7e-06), [[LY6G5B]] (+0.72, fdr 1e-05), [[IL18BP]] (+0.69, fdr 2e-05); moves opposite to [[C16orf87]] (-0.63, fdr 1e-05), [[TENT4B]] (-0.61, fdr 1e-05), [[FOXA2]] (-0.59, fdr 6e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SMAD7]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1609.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +5.0 | 4e-04 | 29/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.71×** | +4.5 | 0.002 | 33/49 (NCI-H460, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.1 | 0.007 | 22/48 (COLO 205, A-427, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.007 | 27/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.9 | 0.011 | 1/50 (NCI-H661) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.075 | 23/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.29× | +3.2 | 0.13 | 27/48 (NCI-H2030, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.21× | +3.1 | 0.14 | 22/47 (KATO III, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1609.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.160×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.145×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 0.335×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SW 1088 0.0985×); [[Doxycycline (monohydrate) (drug)]] 0.05 µM in 1 line (SW 1088 0.0946×); [[Tetracycline (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1088 0.106×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.805× | -3.4 | 0.18 | 26/48 (Panc 03.27, AsPC-1, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.864× | -3.3 | 0.18 | 18/48 (A498, HS-578T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.815× | -3.3 | 0.18 | 24/48 (H4, SW1417, …) | rises with dose |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.876× | -3.0 | 0.33 | 10/49 (SHP-77, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1609. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 1088 (line)]] | alt | 115 | 0 | 3 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0985× (z -9.4) |
| [[A-427 (line)]] | wt | 61.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 119 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 133 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.123× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~63% of this change |
| [[NCI-H23 (line)]] | alt | 97.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 105 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 93.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 132 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 188 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 83.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 116 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 85.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 128 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 117 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 110 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 121 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 103 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 159 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 140 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1609), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMU1]] | +0.72 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[LY6G5B]] | +0.72 | +0.55 / +0.78 | both halves | 1e-05 |  |
| [[IL18BP]] | +0.69 | +0.48 / +0.75 | both halves | 2e-05 |  |
| [[AGBL5]] | +0.67 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[GOLGA3]] | +0.67 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[GCN1]] | +0.66 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[FAM91A1]] | +0.66 | +0.45 / +0.75 | both halves | 3e-05 |  |
| [[PIGG]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[RPN1]] | +0.65 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[HDLBP]] | +0.64 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[NDUFA10]] | +0.63 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[ZNF587B]] | +0.63 | +0.55 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C16orf87]] | -0.63 | -0.52 / -0.71 | both halves | 1e-05 |  |
| [[TENT4B]] | -0.61 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[FOXA2]] | -0.59 | -0.38 / -0.68 | both halves | 6e-05 |  |
| [[ZNF592]] | -0.58 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[TBC1D12]] | -0.58 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[C15orf61]] ⚠ | -0.57 | -0.31 / -0.65 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[PIM3]] | -0.57 | -0.38 / -0.66 | both halves | 7e-05 |  |
| [[DSTYK]] | -0.56 | -0.40 / -0.64 | both halves | 5e-05 |  |
| [[RAB9A]] | -0.55 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[IRF2BPL]] | -0.55 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[MTF2]] | -0.54 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[ST3GAL2]] | -0.53 | -0.42 / -0.53 | both halves | 4e-05 | pathway: Sphingolipid metabolism |
| [[RNF114]] | -0.53 | -0.25 / -0.62 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMAD7]] | C | SMAD7's natural level weakens SPTLC1's drug response | SMAD7's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.71, reverse -0.24; direction not clear | 0.016 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.576). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-20.1, -25.1); signed map (-17.4, -33.2). **Vector** length 89.5, 25.1% of its response variance represented; |z| ≥ 3 in 610 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.2 | -0.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.1 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +6.1 | +0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +0.7 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +1.4 | +1.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -5.1 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -4.3 | -3.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | serine palmitoyltransferase long chain base subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.31 — chr9:92,000,087-92,115,413 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LCB1, SPTI, HSAN1, hLCB1; previously HSN1 |
| Gene groups (HGNC) | Serine palmitoyltransferase long chain base subunits |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [O15269](https://www.uniprot.org/uniprotkb/O15269) (Serine palmitoyltransferase 1):

> Component of the serine palmitoyltransferase multisubunit enzyme (SPT) that catalyzes the initial and rate-limiting step in sphingolipid biosynthesis by condensing L-serine and activated acyl-CoA (most commonly palmitoyl-CoA) to form long-chain bases. The SPT complex is also composed of SPTLC2 or SPTLC3 and SPTSSA or SPTSSB. Within this complex, the heterodimer with SPTLC2 or SPTLC3 forms the catalytic core. The composition of the serine palmitoyltransferase (SPT) complex determines the …

**Summary**, from NCBI Gene [10558](https://www.ncbi.nlm.nih.gov/gene/10558):

> This gene encodes a member of the class-II pyridoxal-phosphate-dependent aminotransferase family. The encoded protein is the long chain base subunit 1 of serine palmitoyltransferase. Serine palmitoyltransferase converts L-serine and palmitoyl-CoA to 3-oxosphinganine with pyridoxal 5'-phosphate and is the key enzyme in sphingolipid biosynthesis. Mutations in this gene were identified in patients with hereditary sensory neuropathy type 1. Alternatively spliced variants encoding different isoforms …

**Accessions** — [HGNC:11277](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11277) · Entrez [10558](https://www.ncbi.nlm.nih.gov/gene/10558) · UniProt [O15269](https://www.uniprot.org/uniprotkb/O15269) · Ensembl [ENSG00000090054](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090054)

## Data

Gene col 1609: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1609); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1609, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1609]; `tensor/DDL_lfc|DDL_z.npy` [1609]; `embed/gene_vectors.npy` [1609]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1609 or target_col == 1609). Every well: [[SPTLC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPTLC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
