---
symbol: "CASKIN2"
type: "gene"
col: 10810
ensembl_id: "ENSG00000177303"
name: "CASK interacting protein 2"
location: "17q25.1"
module: 11
arm: "+"
pooled_cpm: 6.51
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# CASKIN2

*CASK interacting protein 2* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.70× (z +6.2, q 4e-07, up in 5 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.44× (z +4.2, q 0.004, up in 16 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.660× (z -5.1, q 2e-04, down in 22 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (RKO 0.0878×, NCI-H460 0.151×, HS-578T 0.0933×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.0573×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0706×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GFER]] (+0.71, fdr 7e-06), [[DOLPP1]] (+0.61, fdr 7e-06), [[EGLN2]] (+0.59, fdr 1e-05); moves opposite to [[LYRM7]] (-0.53, fdr 9e-05), [[EIF1AX]] (-0.49, fdr 2e-04), [[FAM81A]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLEKHG4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10810.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +6.2 | 4e-07 | 5/14 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.5 | 0.002 | 9/30 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +4.4 | 0.002 | 10/31 (PANC-1, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.004 | 16/45 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +4.1 | 0.004 | 10/47 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +4.1 | 0.004 | 11/42 (A-172, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.26×** | +4.0 | 0.006 | 12/42 (A549, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.9 | 0.007 | 8/32 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.007 | 12/42 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.031 | 7/47 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.4 | 0.039 | 0/18 | rises with dose | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.44× | +3.0 | 0.11 | 5/30 (J82, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10810.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (RKO 0.0878×, NCI-H460 0.151×, HS-578T 0.0933×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.0573×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0706×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.660×** | -5.1 | 2e-04 | 22/46 (Hs 766T, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.543×** | -3.9 | 0.028 | 12/46 (HOP62, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.734×** | -3.8 | 0.028 | 16/42 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.589× | -3.4 | 0.10 | 18/40 (Hs 766T, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10810. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.20 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +12.5) | — |
| [[A549 (line)]] | wt | 3.40 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.05× (z +8.5) ⚠ cell-cycle shift, explains ~12% of this change | — |
| [[HS-578T (line)]] | alt | 3.87 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0933× (z -8.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 7.33 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0573× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 2.98 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0706× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 4.05 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -9.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 10.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0878× (z -10.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10810), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GFER]] | +0.71 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[DOLPP1]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[EGLN2]] | +0.59 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[KMT2B]] | +0.59 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[UCK1]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[GORASP1]] | +0.57 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ARHGEF40]] | +0.57 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[PPP1R37]] | +0.56 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[PRR14]] | +0.56 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[GPKOW]] | +0.55 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[ZNF579]] | +0.55 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[TSSC4]] | +0.54 | +0.62 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYRM7]] | -0.53 | -0.37 / -0.42 | both halves | 9e-05 |  |
| [[EIF1AX]] | -0.49 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[FAM81A]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[BTAF1]] | -0.47 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[RPL6]] | -0.44 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[TPP2]] | -0.44 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[HNRNPA3]] | -0.43 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[PDIA6]] | -0.43 | -0.40 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHG4]] | B | PLEKHG4 activity lowers CASKIN2's level | lines that do not express PLEKHG4 (11) vs lines expressing it (39) | 1.24× higher at baseline in the lines without PLEKHG4 | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC2A12, PPP1R1C, TMEM51-AS1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.389). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-38.4, -2.5); signed map (0.6, -11.3). **Vector** length 54.2, 7.12% of its response variance represented; |z| ≥ 3 in 758 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.3 | +4.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.2 | +4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.4 | +4.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +3.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.5 | +2.5 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.5 | -0.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | CASK interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:75,500,261-75,515,537 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1139, FLJ21609, ANKS5B |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Sterile alpha motif domain containing; SH3 domain containing |
| Matched by | ensembl_id |

UniProt [Q8WXE0](https://www.uniprot.org/uniprotkb/Q8WXE0) carries no function annotation.

**Summary**, from NCBI Gene [57513](https://www.ncbi.nlm.nih.gov/gene/57513):

> This gene encodes a large protein that contains six ankyrin repeats, as well as a Src homology 3 (SH3) domain and two sterile alpha motif (SAM) domains, which may be involved in protein-protein interactions. The C-terminal portion of this protein is proline-rich and contains a conserved region. A related protein interacts with calcium/calmodulin-dependent serine protein kinase (CASK). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2013]

**Accessions** — [HGNC:18200](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18200) · Entrez [57513](https://www.ncbi.nlm.nih.gov/gene/57513) · UniProt [Q8WXE0](https://www.uniprot.org/uniprotkb/Q8WXE0) · Ensembl [ENSG00000177303](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177303)

## Data

Gene col 10810: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10810); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10810, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10810]; `tensor/DDL_lfc|DDL_z.npy` [10810]; `embed/gene_vectors.npy` [10810]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10810 or target_col == 10810). Every well: [[CASKIN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASKIN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
