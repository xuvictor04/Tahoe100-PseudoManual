---
symbol: "MOCS3"
type: "gene"
col: 4504
ensembl_id: "ENSG00000124217"
name: "molybdenum cofactor synthesis 3"
location: "20q13.13"
module: 7
arm: "+"
pooled_cpm: 3.48
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 4
n_dd_up_clean: 22
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# MOCS3

*molybdenum cofactor synthesis 3* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.23× (z +10.9, q 6e-25, up in 27 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.533× (z -6.3, q 1e-07, down in 20 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.564× (z -5.7, q 3e-06, down in 20 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX28]] (+0.80, fdr 7e-06), [[RBM15B]] (+0.78, fdr 7e-06), [[ZNF646]] (+0.77, fdr 7e-06); moves opposite to [[KYAT1]] (-0.63, fdr 1e-05), [[SLC25A5]] (-0.60, fdr 8e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF502]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4504.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +10.9 | 6e-25 | 27/39 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.63×** | +9.0 | 7e-17 | 5/9 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.11×** | +7.5 | 1e-11 | 20/35 (A498, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.70×** | +7.4 | 2e-11 | 22/44 (BT-474, PANC-1, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +7.1 | 1e-10 | 17/37 (A498, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.94×** | +6.7 | 2e-09 | 23/40 (NCI-H460, A498, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +6.5 | 6e-09 | 13/46 (SW480, SW1417, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +6.4 | 9e-09 | 0/6 | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +6.0 | 1e-07 | 6/21 (NCI-H2030, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.09×** | +5.9 | 2e-07 | 13/39 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.77×** | +5.7 | 6e-07 | 13/44 (BT-474, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.73×** | +5.5 | 2e-06 | 16/47 (CFPAC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +5.2 | 9e-06 | 10/43 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.17×** | +4.1 | 0.002 | 7/34 (SW480, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.9 | 0.004 | 7/32 (CFPAC-1, SW480, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.72×** | +3.9 | 0.004 | 5/21 (SW480, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.004 | 11/42 (A-172, HT-29, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.005 | 8/43 (A498, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4504.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.533×** | -6.3 | 1e-07 | 20/34 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.564×** | -5.7 | 3e-06 | 20/46 (LoVo, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.666×** | -4.1 | 0.009 | 13/42 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.702×** | -3.6 | 0.053 | 17/42 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4504. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 7.69 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0917× (z -9.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 6.46 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0595× (z -11.6) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 3.03 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.0675× (z -9.0) ⚠ transcription drop |
| [[RPMI-7951 (line)]] | alt | 5.69 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0602× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 6.39 | 0 | 1 | — | [[Talc (drug)]] 0.5 µM 0.0763× (z -9.5) |
| [[A-172 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4504), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX28]] | +0.80 | +0.84 / +0.74 | both halves | 7e-06 |  |
| [[RBM15B]] | +0.78 | +0.81 / +0.68 | both halves | 7e-06 |  |
| [[ZNF646]] | +0.77 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.77 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[CENPBD1P]] | +0.75 | +0.79 / +0.64 | both halves | 7e-06 |  |
| [[UTP3]] | +0.74 | +0.81 / +0.59 | both halves | 7e-06 |  |
| [[FBXO38]] | +0.74 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[CSTF2T]] | +0.73 | +0.82 / +0.62 | both halves | 7e-06 |  |
| [[ZNF268]] | +0.73 | +0.81 / +0.62 | both halves | 7e-06 |  |
| [[SMG8]] | +0.73 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[ZSCAN29]] | +0.72 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[CBLL1]] | +0.72 | +0.73 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KYAT1]] | -0.63 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[SLC25A5]] | -0.60 | -0.57 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF502]] | B | ZNF502 activity raises MOCS3's level | lines that do not express ZNF502 (18) vs lines expressing it (32) | 1.21× lower at baseline in the lines without ZNF502 | 0.036 | ⚠ within organs, on part of the lines; also absent: CXCR4, LINC01611, ZNF506 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.841). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-37.5, 11.0); signed map (-2.3, -27.2). **Vector** length 50.9, 6.32% of its response variance represented; |z| ≥ 3 in 942 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.4 | +5.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.5 | +5.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +7.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +2.6 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.3 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.7 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | +0.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Tomivosertib (drug)]] 5 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | molybdenum cofactor synthesis 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.13 — chr20:50,958,818-50,963,929 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UBA4, dJ914P20.3 |
| Gene groups (HGNC) | Ubiquitin like modifier activating enzymes; Molybdenum cofactor synthesis proteins |
| Reactome | 3 pathways, smallest: Molybdenum cofactor biosynthesis; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [O95396](https://www.uniprot.org/uniprotkb/O95396) (Adenylyltransferase and sulfurtransferase MOCS3):

> Plays a central role in 2-thiolation of mcm(5)S(2)U at tRNA wobble positions of cytosolic tRNA(Lys), tRNA(Glu) and tRNA(Gln). Also essential during biosynthesis of the molybdenum cofactor. Acts by mediating the C-terminal thiocarboxylation of sulfur carriers URM1 and MOCS2A. Its N-terminus first activates URM1 and MOCS2A as acyl-adenylates (-COAMP), then the persulfide sulfur on the catalytic cysteine is transferred to URM1 and MOCS2A to form thiocarboxylation (-COSH) of their C-terminus. The …

**Summary**, from NCBI Gene [27304](https://www.ncbi.nlm.nih.gov/gene/27304):

> Molybdenum cofactor (MoCo) is necessary for the function of all molybdoenzymes. The protein encoded by this gene adenylates and activates molybdopterin synthase, an enzyme required for biosynthesis of MoCo. This gene contains no introns. A pseudogene of this gene is present on chromosome 14. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:15765](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15765) · Entrez [27304](https://www.ncbi.nlm.nih.gov/gene/27304) · UniProt [O95396](https://www.uniprot.org/uniprotkb/O95396) · Ensembl [ENSG00000124217](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124217)

## Data

Gene col 4504: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4504); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4504, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4504]; `tensor/DDL_lfc|DDL_z.npy` [4504]; `embed/gene_vectors.npy` [4504]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4504 or target_col == 4504). Every well: [[MOCS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOCS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
