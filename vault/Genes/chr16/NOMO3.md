---
symbol: "NOMO3"
type: "gene"
col: 2338
ensembl_id: "ENSG00000103226"
name: "NODAL modulator 3"
location: "16p13.11"
module: 50
arm: "+"
pooled_cpm: 3.67
n_lines_expressing: 48
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# NOMO3

*NODAL modulator 3* — 16p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.09× (z +13.8, q 3e-40, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ciclopirox (drug)]] 5 µM: 0.772× (z -4.5, q 0.004, down in 14 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOMO2]] (+0.79, fdr 7e-06), [[NOMO1]] (+0.76, fdr 7e-06), [[CS]] (+0.74, fdr 1e-05); moves opposite to [[LINC02307]] (-0.68, fdr 1e-05), [[PBDC1]] (-0.65, fdr 3e-05), [[ZNF341-AS1]] (-0.64, fdr 2e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2338.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.09×** | +13.8 | 3e-40 | 41/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.05×** | +13.6 | 1e-39 | 39/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.73×** | +12.2 | 4e-32 | 35/44 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.76×** | +6.9 | 6e-10 | 15/44 (LS 180, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +6.5 | 9e-09 | 1/4 (J82) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +5.7 | 1e-06 | 2/8 (PANC-1, AsPC-1) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +5.4 | 4e-06 | 17/34 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.07×** | +4.6 | 3e-04 | 8/30 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +4.4 | 7e-04 | 4/21 (NCI-H2030, HT-29, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.42×** | +4.1 | 0.002 | 4/20 (SW480, LS 180, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.87×** | +4.0 | 0.004 | 4/38 (KATO III, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2338.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ciclopirox (drug)]] 5 µM |  | **0.772×** | -4.5 | 0.004 | 14/42 (SK-MEL-2, CFPAC-1, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.701×** | -4.3 | 0.004 | 16/42 (KATO III, HS-578T, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.817×** | -3.5 | 0.098 | 7/42 (NCI-H460, BT-474, …) | rises with dose | position effect removed |
| [[Sulfatinib (drug)]] 5 µM |  | 0.758× | -3.2 | 0.17 | 11/42 (AsPC-1, HCT15, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.771× | -3.2 | 0.17 | 3/44 (HCT15, CHP-212, …) | rises with dose |  |
| [[Bicalutamide (drug)]] 0.5 µM |  | 0.774× | -3.1 | 0.17 | 9/42 (HCT15, COLO 205, …) | inconsistent across doses |  |
| [[Rucaparib (phosphate) (drug)]] 5 µM |  | 0.772× | -3.0 | 0.19 | 1/44 (MIA PaCa-2) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2338. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.95 | 0 | 2 (1 ⚠) | — | [[Artemether (drug)]] 0.5 µM 0.0578× (z -9.0) |
| [[A498 (line)]] | wt | 6.93 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0849× (z -12.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 8.89 | 0 | 1 | — | [[Nafamostat (mesylate) (drug)]] 0.5 µM 0.0829× (z -8.7) |
| [[A-427 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2338), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOMO2]] | +0.79 | +0.67 / +0.77 | both halves | 7e-06 | same gene group; pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |
| [[NOMO1]] | +0.76 | +0.62 / +0.64 | both halves | 7e-06 | same gene group; pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 637 |
| [[CS]] | +0.74 | +0.56 / +0.70 | both halves | 1e-05 | pathway: Protein localization |
| [[BLTP2]] | +0.70 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[STIMATE]] | +0.69 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[SLC25A39]] | +0.69 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ACTR5]] | +0.68 | +0.62 / +0.57 | both halves | 8e-06 |  |
| [[INTS11]] | +0.67 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[LRFN3]] | +0.67 | +0.60 / +0.40 | both halves | 4e-05 |  |
| [[WDR5]] | +0.66 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[TSFM]] | +0.66 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[COLGALT1]] | +0.66 | +0.60 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02307]] | -0.68 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[PBDC1]] | -0.65 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ZNF341-AS1]] | -0.64 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ANGPT2]] | -0.63 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[EIF4EBP3]] | -0.62 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | -0.61 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[N4BP2L1]] | -0.61 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[OFD1]] | -0.60 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[LINC01004]] | -0.60 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[NPHS1]] | -0.60 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[SPATC1]] | -0.59 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[KANSL1L]] | -0.59 | -0.45 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers NOMO3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.595). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.5, -25.6); signed map (-43.7, -13.6). **Vector** length 42.1, 4.29% of its response variance represented; |z| ≥ 3 in 1,038 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +2.5 | +13.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.4 | +12.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.4 | +13.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.7 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | +4.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +0.7 | +1.9 |
|  | [[EX229 (drug)]] 5 µM |  | +0.6 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.6 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.6 | +2.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.8 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | +1.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | +0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -0.8 | +0.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -0.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | NODAL modulator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.11 — chr16:16,232,506-16,300,806 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | BOS complex subunits |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [P69849](https://www.uniprot.org/uniprotkb/P69849) (BOS complex subunit NOMO3):

> Component of the multi-pass translocon (MPT) complex that mediates insertion of multi-pass membrane proteins into the lipid bilayer of membranes. The MPT complex takes over after the SEC61 complex: following membrane insertion of the first few transmembrane segments of proteins by the SEC61 complex, the MPT complex occludes the lateral gate of the SEC61 complex to promote insertion of subsequent transmembrane regions.

**Summary**, from NCBI Gene [408050](https://www.ncbi.nlm.nih.gov/gene/408050):

> This gene encodes a protein originally thought to be related to the collagenase gene family. This gene is one of three highly similar genes in a duplicated region on the short arm of chromosome 16. These three genes encode closely related proteins that may have the same function. The protein encoded by one of these genes has been identified as part of a protein complex that participates in the Nodal signaling pathway during vertebrate development. Mutations in ABCC6, which is located nearby, …

**Accessions** — [HGNC:25242](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25242) · Entrez [408050](https://www.ncbi.nlm.nih.gov/gene/408050) · UniProt [P69849](https://www.uniprot.org/uniprotkb/P69849) · Ensembl [ENSG00000103226](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103226)

## Data

Gene col 2338: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2338); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2338, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2338]; `tensor/DDL_lfc|DDL_z.npy` [2338]; `embed/gene_vectors.npy` [2338]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2338 or target_col == 2338). Every well: [[NOMO3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOMO3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
