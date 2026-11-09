---
symbol: "NAXD"
type: "gene"
col: 13159
ensembl_id: "ENSG00000213995"
name: "NAD(P)HX dehydratase"
location: "13q34"
module: 20
arm: "+"
pooled_cpm: 17.6
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# NAXD

*NAD(P)HX dehydratase* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.34× (z +5.1, q 9e-05, up in 29 of 48 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.22× (z +5.1, q 9e-05, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.706× (z -4.3, q 0.012, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 0.156×, SHP-77 0.191×, SW480 0.302×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Thymol (drug)]] 0.5 µM in 2 lines (SNU-1 0.130×, SW 900 0.204×); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (SNU-1 0.0801×); [[Allantoin (drug)]] 0.5 µM in 1 line (SNU-1 0.116×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIPC]] (+0.74, fdr 7e-06), [[COPS7B]] (+0.72, fdr 7e-06), [[MTX1]] (+0.69, fdr 2e-05); moves opposite to [[KLF2]] (-0.62, fdr 2e-05), [[METTL23]] (-0.61, fdr 8e-06), [[CCDC88A]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CTSZ]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13159.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.34×** | +5.1 | 9e-05 | 29/48 (Panc 03.27, Hs 766T, …) | top dose only | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **2.22×** | +5.1 | 9e-05 | 27/47 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +5.0 | 1e-04 | 22/47 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.09×** | +4.7 | 3e-04 | 11/22 (NCI-H1573, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.50×** | +4.7 | 3e-04 | 26/46 (PANC-1, COLO 205, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.05×** | +4.6 | 4e-04 | 25/44 (LoVo, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +4.4 | 0.001 | 21/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +4.1 | 0.002 | 20/47 (HT-29, COLO 205, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.004 | 21/46 (COLO 205, LoVo, …) | top dose only | position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.37×** | +3.5 | 0.022 | 18/46 (NCI-H2030, SW1417, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.025 | 14/45 (PANC-1, HS-578T, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.71×** | +3.4 | 0.027 | 11/47 (A498, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.044 | 12/46 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.094 | 14/46 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13159.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 0.156×, SHP-77 0.191×, SW480 0.302×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Thymol (drug)]] 0.5 µM in 2 lines (SNU-1 0.130×, SW 900 0.204×); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (SNU-1 0.0801×); [[Allantoin (drug)]] 0.5 µM in 1 line (SNU-1 0.116×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.706×** | -4.3 | 0.012 | 21/48 (A-427, SW 1088, …) | two highest doses | cell-cycle shift (explains ~22% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.727×** | -3.9 | 0.026 | 23/39 (SW48, NCI-H1573, …) | two highest doses | composition shift |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.839× | -3.0 | 0.46 | 17/48 (C-33 A, SW48, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13159. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 23.2 | 0 | 3 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0801× (z -11.5) |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.106× (z -8.9) |
| [[LS 180 (line)]] | wt | 22.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[SHP-77 (line)]] | alt | 42.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.204× (z -8.7) |
| [[SW48 (line)]] | wt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[SW480 (line)]] | alt | 46.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change |
| [[A-172 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13159), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIPC]] | +0.74 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[COPS7B]] | +0.72 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[MTX1]] | +0.69 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[NCSTN]] | +0.67 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[USF1]] | +0.66 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[SDHD]] | +0.66 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[C1D]] | +0.64 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[EIF3F]] | +0.64 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[WASH8P]] ⚠ | +0.63 | +0.45 / +0.62 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[WASH9P]] | +0.63 | +0.42 / +0.72 | both halves | 4e-05 |  |
| [[LDB1]] | +0.63 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[STX16]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[GPN1]] | +0.63 | +0.60 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLF2]] | -0.62 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[METTL23]] | -0.61 | -0.57 / -0.61 | both halves | 8e-06 |  |
| [[CCDC88A]] | -0.58 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[NBPF10]] | -0.58 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[BTG1]] | -0.57 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[PPP1R13B]] | -0.57 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[BAIAP2L1]] | -0.57 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[NBPF14]] | -0.57 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[HES1]] | -0.56 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[KRTCAP2]] | -0.56 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[CDKN2D]] | -0.56 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[NBPF19]] | -0.55 | -0.53 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSZ]] | B | CTSZ activity lowers NAXD's level | lines that do not express CTSZ (8) vs lines expressing it (42) | 1.31× higher at baseline in the lines without CTSZ | 0.028 | ⚠ within organs, on part of the lines; also absent: LRRK1, CAV2, PIWIL4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-19.5, -16.0); signed map (-18.6, -31.4). **Vector** length 62.7, 10.1% of its response variance represented; |z| ≥ 3 in 784 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +4.7 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.5 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +4.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +1.5 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.0 | -1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.2 | -1.8 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | NAD(P)HX dehydratase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:110,615,545-110,639,996 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LP3298, FLJ10769; previously CARKD |
| Gene groups (HGNC) | Carbon-oxygen lyases |
| Reactome | 3 pathways, smallest: Nicotinate metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IW45](https://www.uniprot.org/uniprotkb/Q8IW45) (ATP-dependent):

> Catalyzes the dehydration of the S-form of NAD(P)HX at the expense of ATP, which is converted to ADP. Together with NAD(P)HX epimerase, which catalyzes the epimerization of the S- and R-forms, the enzyme allows the repair of both epimers of NAD(P)HX, a damaged form of NAD(P)H that is a result of enzymatic or heat-dependent hydration.

**Summary**, from NCBI Gene [55739](https://www.ncbi.nlm.nih.gov/gene/55739):

> Enables ATP-dependent NAD(P)H-hydrate dehydratase activity. Predicted to be involved in metabolite repair. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25576](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25576) · Entrez [55739](https://www.ncbi.nlm.nih.gov/gene/55739) · UniProt [Q8IW45](https://www.uniprot.org/uniprotkb/Q8IW45) · Ensembl [ENSG00000213995](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213995)

## Data

Gene col 13159: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13159); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13159, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13159]; `tensor/DDL_lfc|DDL_z.npy` [13159]; `embed/gene_vectors.npy` [13159]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13159 or target_col == 13159). Every well: [[NAXD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAXD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
