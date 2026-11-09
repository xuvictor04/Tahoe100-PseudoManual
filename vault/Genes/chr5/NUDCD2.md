---
symbol: "NUDCD2"
type: "gene"
col: 9979
ensembl_id: "ENSG00000170584"
name: "NudC domain containing 2"
location: "5q34"
module: 12
arm: "+"
pooled_cpm: 29.36
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# NUDCD2

*NudC domain containing 2* — 5q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.47× (z +8.1, q 2e-13, up in 38 of 43 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 3.90×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.630× (z -4.7, q 0.002, down in 31 of 47 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.641× (z -4.5, q 0.002, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EBAG9]] (+0.66, fdr 1e-05), [[PPP4R2]] (+0.63, fdr 1e-05), [[CETN3]] (+0.62, fdr 7e-06); moves opposite to [[UFD1]] (-0.58, fdr 1e-05), [[SERPINH1]] (-0.55, fdr 1e-04), [[IL18BP]] (-0.54, fdr 5e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TXNIP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9979.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 3.90×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.47×** | +8.1 | 2e-13 | 38/43 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +8.1 | 2e-13 | 32/36 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **1.65×** | +5.1 | 7e-05 | 29/46 (SW1417, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.63×** | +4.6 | 7e-04 | 26/41 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.50×** | +4.0 | 0.009 | 25/48 (SW1417, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.52×** | +3.7 | 0.018 | 28/48 (SW1417, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9979.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.630×** | -4.7 | 0.002 | 31/47 (J82, PANC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.641×** | -4.5 | 0.002 | 28/48 (RKO, BT-474, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.644×** | -4.4 | 0.002 | 29/48 (NCI-H460, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.625×** | -4.2 | 0.004 | 28/48 (SW48, SK-MEL-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.456×** | -4.1 | 0.004 | 23/41 (A-427, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.494×** | -3.7 | 0.019 | 26/47 (LoVo, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.694×** | -3.5 | 0.033 | 23/48 (SW 1088, NCI-H2347, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.786×** | -3.4 | 0.047 | 24/47 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.724×** | -3.2 | 0.074 | 22/48 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.72 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9979. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 65.9 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0440× (z -12.1) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[NCI-H460 (line)]] | wt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.90× (z +9.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 33.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9979), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EBAG9]] | +0.66 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[PPP4R2]] | +0.63 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[CETN3]] | +0.62 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[GEMIN2]] | +0.60 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[ATP5PO]] ⚠ | +0.59 | +0.55 / +0.60 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LCOR]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[EMC9]] | +0.58 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[CDC20]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TMEM42]] | +0.57 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ARL4A]] | +0.56 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[COMMD3]] | +0.56 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[GTF2H5]] | +0.55 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[ARMC1]] | +0.54 | +0.49 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UFD1]] | -0.58 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[SERPINH1]] | -0.55 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[IL18BP]] | -0.54 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[ERVK13-1]] | -0.54 | -0.12 / -0.61 | ⚠ one half (not replicated) | 0.002 |  |
| [[DNAJB6]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[MBOAT7]] | -0.54 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[NPLOC4]] | -0.53 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[NECAB3]] | -0.53 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[LY6G5B]] | -0.53 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ZNF731P]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[SLC25A53]] | -0.51 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[MTCH1]] | -0.50 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[SFXN5]] | -0.50 | -0.33 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TXNIP]] | B | TXNIP activity lowers NUDCD2's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.43× higher at baseline in the lines without TXNIP | 0.072 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises NUDCD2's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 1.54× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.448). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-30.1, 2.9); signed map (5.8, -24.7). **Vector** length 74.5, 19.8% of its response variance represented; |z| ≥ 3 in 597 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +4.7 | +4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +4.4 | +3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | -0.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +0.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +0.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.0 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -4.4 | -4.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | -3.4 | -4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | -3.4 | -4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -3.2 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.0 | -1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | NudC domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q34 — chr5:163,446,526-163,460,102 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686E10109, NudCL2 |
| Gene groups (HGNC) | NudC family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WVJ2](https://www.uniprot.org/uniprotkb/Q8WVJ2) (NudC domain-containing protein 2):

> May regulate the LIS1/dynein pathway by stabilizing LIS1 with Hsp90 chaperone.

**Summary**, from NCBI Gene [134492](https://www.ncbi.nlm.nih.gov/gene/134492):

> Predicted to enable unfolded protein binding activity. Predicted to be involved in protein folding. Located in mitotic spindle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30535](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30535) · Entrez [134492](https://www.ncbi.nlm.nih.gov/gene/134492) · UniProt [Q8WVJ2](https://www.uniprot.org/uniprotkb/Q8WVJ2) · Ensembl [ENSG00000170584](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170584)

## Data

Gene col 9979: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9979); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9979, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9979]; `tensor/DDL_lfc|DDL_z.npy` [9979]; `embed/gene_vectors.npy` [9979]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9979 or target_col == 9979). Every well: [[NUDCD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDCD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
