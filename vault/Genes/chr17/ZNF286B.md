---
symbol: "ZNF286B"
type: "gene"
col: 14613
ensembl_id: "ENSG00000249459"
name: "zinc finger protein 286B (pseudogene)"
location: "17p11.2"
module: 11
arm: "+"
pooled_cpm: 2.95
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ZNF286B

*zinc finger protein 286B (pseudogene)* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.90× (z +11.1, q 4e-26, up in 25 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.485× (z -4.6, q 0.002, down in 17 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[palbociclib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0835×); [[Vandetanib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0795×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NME6]] (+0.70, fdr 1e-05), [[ARL14EP]] (+0.67, fdr 1e-05), [[C3orf20]] (+0.64, fdr 3e-05); moves opposite to [[GUSB]] (-0.63, fdr 2e-05), [[GGH]] (-0.62, fdr 4e-05), [[RCN2]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF382]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14613.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.90×** | +11.1 | 4e-26 | 25/38 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.37×** | +8.9 | 2e-16 | 18/35 (NCI-H2030, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.91×** | +8.0 | 3e-13 | 22/44 (LS 180, C-33 A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +7.5 | 1e-11 | 1/4 (HOP62) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.82×** | +7.3 | 2e-11 | 16/45 (NCI-H23, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +7.0 | 3e-10 | 6/16 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +5.7 | 1e-06 | 11/46 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +5.5 | 2e-06 | 9/42 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.002 | 9/43 (SK-MEL-2, MIA PaCa-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.35×** | +3.5 | 0.025 | 2/40 (SHP-77, NCI-H2030) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +3.5 | 0.025 | 2/14 (NCI-H2030, A-172) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.085 | 4/45 (RKO, PANC-1, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.1 | 0.085 | 0/3 | top dose only | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.087 | 6/46 (NCI-H460, CHP-212, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14613.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[palbociclib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0835×); [[Vandetanib (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0795×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.485×** | -4.6 | 0.002 | 17/40 (LOX-IMVI, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.718×** | -3.9 | 0.025 | 10/35 (MIA PaCa-2, HepG2/C3A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.735×** | -3.8 | 0.029 | 13/30 (A498, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.744×** | -3.6 | 0.041 | 10/44 (hTERT-HPNE, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.766× | -3.3 | 0.12 | 9/43 (hTERT-HPNE, SW 900, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14613. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 6.40 | 0 | 1 | — | [[palbociclib (drug)]] 0.05 µM 0.0835× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 3.72 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0795× (z -9.8) |
| [[A-172 (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.859 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.897 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.797 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.837 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14613), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NME6]] | +0.70 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[ARL14EP]] | +0.67 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[C3orf20]] | +0.64 | +0.72 / +0.43 | both halves | 3e-05 |  |
| [[NSRP1]] | +0.63 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[ZNF197]] | +0.62 | +0.72 / +0.45 | both halves | 3e-05 | same gene group |
| [[CDKL1]] | +0.62 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[CLDN15]] | +0.62 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[FOXO3B]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF181]] | +0.61 | +0.69 / +0.38 | both halves | 7e-05 | same gene group |
| [[CCDC59]] | +0.61 | +0.67 / +0.39 | both halves | 6e-05 |  |
| [[GFER]] | +0.59 | +0.71 / +0.45 | both halves | 3e-05 |  |
| [[LINC00486]] | +0.59 | +0.73 / +0.30 | both halves | 2e-04 |  |
| [[WASHC1]] | +0.59 | +0.70 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUSB]] | -0.63 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[GGH]] | -0.62 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[RCN2]] | -0.62 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[HAT1]] | -0.62 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[CTXN1]] | -0.60 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[ITM2C]] | -0.60 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[CETN2]] | -0.59 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[RPN2]] | -0.59 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[MYCBP]] | -0.58 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[NAGA]] | -0.57 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[MLEC]] | -0.57 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[DPY19L1]] | -0.57 | -0.62 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF382]] | B | ZNF382 activity raises ZNF286B's level | lines that do not express ZNF382 (18) vs lines expressing it (32) | 1.49× lower at baseline in the lines without ZNF382 | 0.074 | ⚠ within organs, on part of the lines; also absent: AFF3, DZIP1, MMP16 |
| [[SCUBE2]] | B | SCUBE2 activity raises ZNF286B's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 1.79× lower at baseline in the lines without SCUBE2 | 0.095 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-39.3, 15.0); signed map (3.7, -21.7). **Vector** length 43.5, 4.60% of its response variance represented; |z| ≥ 3 in 1,014 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +8.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +11.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.4 | +7.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.1 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +4.1 |
|  | [[EX229 (drug)]] 5 µM |  | +1.2 | +2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.1 | +3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.1 | +2.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.5 | -4.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -1.8 | -3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -0.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -0.9 | -2.1 |
|  | [[Elagolix sodium (drug)]] 0.5 µM |  | -0.8 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -0.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 286B (pseudogene) |
| Locus type | pseudogene |
| Location | 17p11.2 — chr17:18,661,937-18,681,846 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ZNF590; previously ZNF286L, ZNF286C |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [P0CG31](https://www.uniprot.org/uniprotkb/P0CG31) (Putative zinc finger protein 286B):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [729288](https://www.ncbi.nlm.nih.gov/gene/729288):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33241](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33241) · Entrez [729288](https://www.ncbi.nlm.nih.gov/gene/729288) · UniProt [P0CG31](https://www.uniprot.org/uniprotkb/P0CG31) · Ensembl [ENSG00000249459](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249459)

## Data

Gene col 14613: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14613); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14613, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14613]; `tensor/DDL_lfc|DDL_z.npy` [14613]; `embed/gene_vectors.npy` [14613]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14613 or target_col == 14613). Every well: [[ZNF286B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF286B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
