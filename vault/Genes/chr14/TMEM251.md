---
symbol: "TMEM251"
type: "gene"
col: 7723
ensembl_id: "ENSG00000153485"
name: "lysosomal enzyme trafficking factor"
location: "14q32.12"
module: 162
arm: "+"
pooled_cpm: 3.76
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# TMEM251

*lysosomal enzyme trafficking factor* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.06× (z +8.7, q 2e-15, up in 25 of 37 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.62× (z +8.2, q 8e-14, up in 39 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.171×; ⚠ cell-cycle shift, explains ~65% of this change); [[Canagliflozin (drug)]] 5 µM in 1 line (A549 0.0860×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GON7]] (+0.63, fdr 1e-05, ⚠ same locus), [[METTL23]] (+0.61, fdr 7e-06), [[NFKBIE]] (+0.60, fdr 1e-05), [[DUSP2]] (+0.59, fdr 1e-05); moves opposite to [[ATL3]] (-0.58, fdr 3e-05), [[CMPK1]] (-0.57, fdr 1e-05), [[CLCC1]] (-0.57, fdr 2e-05).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HES6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7723.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.06×** | +8.7 | 2e-15 | 25/37 (SNU-423, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.62×** | +8.2 | 8e-14 | 39/44 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **2.40×** | +7.5 | 2e-11 | 14/21 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.51×** | +7.4 | 2e-11 | 5/7 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.34×** | +7.2 | 5e-11 | 34/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.15×** | +6.2 | 7e-08 | 27/42 (SNU-423, COLO 205, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.02×** | +6.0 | 2e-07 | 31/47 (SW480, H4, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.94×** | +5.7 | 1e-06 | 24/46 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +5.2 | 1e-05 | 19/36 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.76×** | +4.8 | 9e-05 | 13/33 (NCI-H1573, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.73×** | +4.2 | 0.001 | 5/9 (A498, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +4.2 | 0.001 | 14/43 (SNU-423, NCI-H2347, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.61×** | +4.0 | 0.002 | 11/36 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.003 | 6/44 (NCI-H460, J82, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.003 | 5/46 (PANC-1, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7723.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.171×; ⚠ cell-cycle shift, explains ~65% of this change); [[Canagliflozin (drug)]] 5 µM in 1 line (A549 0.0860×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.430× | -3.4 | 0.35 | 10/40 (HCT15, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7723. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.47 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.95× (z +9.1) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[A549 (line)]] | wt | 4.77 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0860× (z -8.7) |
| [[RKO (line)]] | wt | 5.98 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -9.2) ⚠ cell-cycle shift, explains ~65% of this change |
| [[SNU-423 (line)]] | alt | 3.75 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +11.0) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[A-427 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7723), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GON7]] | +0.63 | +0.57 / +0.64 | both halves | 1e-05 | ⚠ same locus (14.4 kb: neighbours can correlate without regulation) |
| [[METTL23]] | +0.61 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[NFKBIE]] | +0.60 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[DUSP2]] | +0.59 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ARL4C]] | +0.59 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[GALE]] | +0.59 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[CMTR2]] | +0.59 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[MCTP1]] | +0.58 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[IRF2BP2]] | +0.58 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[BTG1]] | +0.57 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[IER2]] | +0.57 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[N4BP3]] | +0.56 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[IRAK2]] | +0.56 | +0.45 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATL3]] | -0.58 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[CMPK1]] | -0.57 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[CLCC1]] | -0.57 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[NAP1L4]] | -0.54 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[SAP30L-AS1]] | -0.53 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[CSDE1]] | -0.52 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[METTL4]] | -0.51 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SETD7]] | -0.50 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[XNDC1N]] | -0.50 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[RPN1]] | -0.49 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[RBBP4]] | -0.49 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[SELENOF]] | -0.48 | -0.36 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES6]] | B | HES6 activity raises TMEM251's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.46× lower at baseline in the lines without HES6 | 0.005 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.582). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.0, -0.8); signed map (8.1, 29.7). **Vector** length 49.9, 6.85% of its response variance represented; |z| ≥ 3 in 796 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.7 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +2.4 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | +2.2 | +7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.1 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.0 | +5.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.9 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +4.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +0.9 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.4 | +0.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | +1.3 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | lysosomal enzyme trafficking factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:93,184,951-93,188,463 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564F1123, GCAF; previously C14orf109, TMEM251 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N6I4](https://www.uniprot.org/uniprotkb/Q8N6I4) (Lysosomal enzyme trafficking factor):

> Required for mannose-6-phosphate-dependent trafficking of lysosomal enzymes. LYSET bridges GlcNAc-1-phosphate transferase (GNPTAB), to the membrane-bound transcription factor site-1 protease (MBTPS1), thus allowing proteolytic activation of the GNPTAB. GNPTAB is involved in the regulation of M6P-dependent Golgi-to-lysosome trafficking of lysosomal enzymes. LYSET is thus an essential factor for maturation and delivery of lysosomal hydrolases.; (Microbial infection) Essential for infection by …

**Summary**, from NCBI Gene [26175](https://www.ncbi.nlm.nih.gov/gene/26175):

> Involved in lysosomal transport; lysosome organization; and regulation of vesicle-mediated transport. Located in Golgi cisterna. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20218](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20218) · Entrez [26175](https://www.ncbi.nlm.nih.gov/gene/26175) · UniProt [Q8N6I4](https://www.uniprot.org/uniprotkb/Q8N6I4) · Ensembl [ENSG00000153485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153485)

## Data

Gene col 7723: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7723); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7723, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7723]; `tensor/DDL_lfc|DDL_z.npy` [7723]; `embed/gene_vectors.npy` [7723]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7723 or target_col == 7723). Every well: [[TMEM251 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM251.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
