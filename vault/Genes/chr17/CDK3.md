---
symbol: "CDK3"
type: "gene"
col: 14697
ensembl_id: "ENSG00000250506"
name: "cyclin dependent kinase 3"
location: "17q25.1"
module: 29
arm: "-"
pooled_cpm: 3.01
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# CDK3

*cyclin dependent kinase 3* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.61× (z +10.2, q 9e-22, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.01× (z +8.1, q 7e-14, up in 24 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.404× (z -7.5, q 3e-11, down in 29 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASHC1]] (+0.76, fdr 7e-06), [[AGER]] (+0.74, fdr 7e-06), [[EIF4EBP3]] (+0.74, fdr 7e-06); moves opposite to [[LSM4]] (-0.63, fdr 3e-05), [[HAUS6]] (-0.63, fdr 1e-05), [[TMED7]] (-0.62, fdr 3e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14697.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.61×** | +10.2 | 9e-22 | 3/4 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.42×** | +10.2 | 9e-22 | 9/13 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.01×** | +8.1 | 7e-14 | 24/36 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.45×** | +6.8 | 1e-09 | 3/5 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **3.18×** | +4.0 | 0.005 | 2/27 (SW480, PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +4.0 | 0.005 | 15/42 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +3.6 | 0.029 | 5/27 (NCI-H460, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +3.3 | 0.065 | 5/18 (A-172, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.3 | 0.065 | 3/25 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.77×** | +3.2 | 0.065 | 2/30 (NCI-H460, SW480) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.52×** | +3.2 | 0.065 | 0/32 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.51×** | +3.1 | 0.078 | 4/30 (A549, A498, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.41×** | +3.1 | 0.095 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14697.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.404×** | -7.5 | 3e-11 | 29/44 (SNU-1, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.408×** | -7.4 | 3e-11 | 31/44 (LOX-IMVI, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.491×** | -5.9 | 6e-07 | 22/45 (Panc 03.27, LOX-IMVI, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.545×** | -5.1 | 6e-05 | 18/44 (LS 180, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.571×** | -4.7 | 3e-04 | 16/32 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.295×** | -4.2 | 0.003 | 10/39 (A-427, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tazarotene (drug)]] 5 µM |  | **0.613×** | -4.1 | 0.004 | 9/45 (SW48, A-427, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.307×** | -4.0 | 0.004 | 11/31 (A498, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.644×** | -3.5 | 0.026 | 11/31 (LoVo, NCI-H460, …) | top dose only | position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.650×** | -3.3 | 0.051 | 8/44 (SHP-77, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14697. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 2.46 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0482× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 2.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +9.5) | — |
| [[A-172 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14697), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASHC1]] | +0.76 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[AGER]] | +0.74 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[EIF4EBP3]] | +0.74 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[LIME1]] | +0.73 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[DXO]] | +0.68 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[TCF25]] | +0.68 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[TTC36-AS1]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[PAQR6]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[APBA3]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[COL11A2]] | +0.66 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[AKT1S1]] | +0.65 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[CLDN15]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSM4]] | -0.63 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[HAUS6]] | -0.63 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[TMED7]] | -0.62 | -0.67 / -0.45 | both halves | 3e-05 |  |
| [[WRNIP1]] | -0.62 | -0.68 / -0.44 | both halves | 3e-05 |  |
| [[NHP2]] | -0.62 | -0.63 / -0.29 | both halves | 3e-04 |  |
| [[PAFAH1B2]] | -0.62 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[GRB2]] | -0.61 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[PGAM1]] | -0.61 | -0.71 / -0.54 | both halves | 1e-05 |  |
| [[BLTP2]] | -0.61 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[MDH2]] | -0.61 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[SDHAF3]] | -0.60 | -0.59 / -0.43 | both halves | 4e-05 |  |
| [[PAICS]] | -0.59 | -0.61 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CDK3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZDHHC1]] | C | ZDHHC1 activity raises CDK3's level | lines that do not express ZDHHC1 (4) vs lines expressing it (46) | 1.47× lower at baseline in the lines without ZDHHC1 | 0.073 | ⚠ few lines (4 vs 46); across organs; also absent: PDE4C, KIF5A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.542). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (24.1, -9.1); signed map (2.9, -10.4). **Vector** length 53.8, 8.15% of its response variance represented; |z| ≥ 3 in 775 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +10.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.1 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +4.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +3.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.9 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +1.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +3.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.1 | -7.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -4.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.9 | -5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -4.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -1.7 | -4.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.5 | -3.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:76,000,855-76,005,999 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cyclin dependent kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00526](https://www.uniprot.org/uniprotkb/Q00526) (Cyclin-dependent kinase 3):

> Serine/threonine-protein kinase that plays a critical role in the control of the eukaryotic cell cycle; involved in G0-G1 and G1-S cell cycle transitions. Interacts with CCNC/cyclin-C during interphase. Phosphorylates histone H1, ATF1, RB1 and CABLES1. ATF1 phosphorylation triggers ATF1 transactivation and transcriptional activities, and promotes cell proliferation and transformation. CDK3/cyclin-C mediated RB1 phosphorylation is required for G0-G1 transition. Promotes G1-S transition probably …

**Summary**, from NCBI Gene [1018](https://www.ncbi.nlm.nih.gov/gene/1018):

> This gene encodes a member of the cyclin-dependent protein kinase family. The protein promotes entry into S phase, in part by activating members of the E2F family of transcription factors. The protein also associates with cyclin C and phosphorylates the retinoblastoma 1 protein to promote exit from G0. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1772](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1772) · Entrez [1018](https://www.ncbi.nlm.nih.gov/gene/1018) · UniProt [Q00526](https://www.uniprot.org/uniprotkb/Q00526) · Ensembl [ENSG00000250506](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250506)

## Data

Gene col 14697: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14697); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14697, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14697]; `tensor/DDL_lfc|DDL_z.npy` [14697]; `embed/gene_vectors.npy` [14697]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14697 or target_col == 14697). Every well: [[CDK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
