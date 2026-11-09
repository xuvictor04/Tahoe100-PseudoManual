---
symbol: "LIN7B"
type: "gene"
col: 2509
ensembl_id: "ENSG00000104863"
name: "lin-7 cell polarity scaffold B"
location: "19q13.33"
module: 3
arm: "+"
pooled_cpm: 4.35
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# LIN7B

*lin-7 cell polarity scaffold B* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.17× (z +5.9, q 2e-06, up in 26 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.480× (z -5.6, q 7e-06, down in 22 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAMLG]] (+0.74, fdr 1e-05), [[RPP21]] (+0.73, fdr 8e-06), [[CCDC107]] (+0.73, fdr 1e-05); moves opposite to [[SRSF1]] (-0.71, fdr 1e-05), [[DARS2]] (-0.70, fdr 3e-05), [[EIF4G1]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2509.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.17×** | +5.9 | 2e-06 | 26/45 (KATO III, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +5.5 | 1e-05 | 23/47 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.94×** | +5.1 | 8e-05 | 23/47 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +4.6 | 7e-04 | 15/28 (NCI-H1792, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +3.5 | 0.044 | 14/41 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.51× | +3.2 | 0.13 | 7/38 (HS-578T, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | 1.51× | +3.1 | 0.13 | 2/24 (PANC-1, SNU-423) | inconsistent across doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2509.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.480×** | -5.6 | 7e-06 | 22/47 (SNU-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.232×** | -5.6 | 7e-06 | 27/37 (NCI-H2030, HT-29, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.506×** | -5.2 | 5e-05 | 21/45 (HS-578T, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.381×** | -3.7 | 0.033 | 19/43 (SW480, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.606×** | -3.6 | 0.038 | 11/44 (Panc 03.27, LOX-IMVI, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.629×** | -3.5 | 0.042 | 13/46 (A549, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.638×** | -3.4 | 0.053 | 16/36 (C32, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.620×** | -3.3 | 0.058 | 10/34 (HEC-1-A, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.667× | -3.1 | 0.14 | 17/44 (SNU-423, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2509. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 5.18 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.0575× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 3.24 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0567× (z -11.2) |
| [[A-172 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2509), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMLG]] | +0.74 | +0.49 / +0.75 | both halves | 1e-05 |  |
| [[RPP21]] | +0.73 | +0.58 / +0.70 | both halves | 8e-06 |  |
| [[CCDC107]] | +0.73 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[A1BG]] | +0.72 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[RAB40C]] | +0.72 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[SLC17A5]] | +0.71 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[CDKN2D]] | +0.70 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[USP42]] | +0.70 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[ALKBH7]] | +0.70 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[DENND6B]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[ZFAND2B]] | +0.70 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[VPS37D]] | +0.70 | +0.62 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF1]] | -0.71 | -0.54 / -0.68 | both halves | 1e-05 |  |
| [[DARS2]] | -0.70 | -0.46 / -0.71 | both halves | 3e-05 |  |
| [[EIF4G1]] | -0.68 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[HNRNPA2B1]] | -0.68 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[PSME3]] | -0.67 | -0.52 / -0.65 | both halves | 1e-05 |  |
| [[TARDBP]] | -0.67 | -0.48 / -0.70 | both halves | 2e-05 |  |
| [[U2AF2]] | -0.66 | -0.39 / -0.63 | both halves | 5e-05 |  |
| [[HNRNPK]] | -0.66 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[TRIP12]] | -0.66 | -0.38 / -0.66 | both halves | 7e-05 |  |
| [[DDX39B]] | -0.65 | -0.38 / -0.63 | both halves | 7e-05 |  |
| [[TRIM44]] | -0.65 | -0.42 / -0.67 | both halves | 4e-05 |  |
| [[MOB1A]] | -0.65 | -0.45 / -0.67 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers LIN7B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.819). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.1, -17.5); signed map (-29.1, 11.9). **Vector** length 65.3, 12.0% of its response variance represented; |z| ≥ 3 in 715 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +2.5 | +3.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.2 | +5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.0 | +5.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.6 | +5.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +1.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.2 | +1.8 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.2 | +2.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.0 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -3.6 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.5 | +1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.0 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -5.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | lin-7 cell polarity scaffold B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,114,324-49,118,460 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MALS-2, LIN-7B, VELI2 |
| Gene groups (HGNC) | PDZ domain containing; Crumbs complex components |
| Reactome | 13 pathways, smallest: RHO GTPases Activate Rhotekin and Rhophilins; Dopamine Neurotransmitter Release Cycle; Assembly and cell surface presentation of NMDA receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAP6](https://www.uniprot.org/uniprotkb/Q9HAP6) (Protein lin-7 homolog B):

> Plays a role in establishing and maintaining the asymmetric distribution of channels and receptors at the plasma membrane of polarized cells. Forms membrane-associated multiprotein complexes that may regulate delivery and recycling of proteins to the correct membrane domains. The tripartite complex composed of LIN7 (LIN7A, LIN7B or LIN7C), CASK and APBA1 associates with the motor protein KIF17 to transport vesicles containing N-methyl-D-aspartate (NMDA) receptor subunit NR2B along microtubules …

**Summary**, from NCBI Gene [64130](https://www.ncbi.nlm.nih.gov/gene/64130):

> Enables protein domain specific binding activity. Predicted to be involved in neurotransmitter secretion; regulation of synaptic assembly at neuromuscular junction; and synaptic vesicle transport. Predicted to be located in plasma membrane. Predicted to be part of MPP7-DLG1-LIN7 complex. Predicted to be active in basolateral plasma membrane; cell-cell junction; and postsynaptic density, intracellular component. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17788](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17788) · Entrez [64130](https://www.ncbi.nlm.nih.gov/gene/64130) · UniProt [Q9HAP6](https://www.uniprot.org/uniprotkb/Q9HAP6) · Ensembl [ENSG00000104863](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104863)

## Data

Gene col 2509: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2509); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2509, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2509]; `tensor/DDL_lfc|DDL_z.npy` [2509]; `embed/gene_vectors.npy` [2509]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2509 or target_col == 2509). Every well: [[LIN7B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIN7B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
