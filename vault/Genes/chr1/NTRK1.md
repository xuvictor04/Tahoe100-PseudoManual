---
symbol: "NTRK1"
type: "gene"
col: 12585
ensembl_id: "ENSG00000198400"
name: "neurotrophic receptor tyrosine kinase 1"
location: "1q23.1"
module: 47
arm: "+"
pooled_cpm: 2.06
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# NTRK1

*neurotrophic receptor tyrosine kinase 1* — 1q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.18× (z +9.7, q 3e-19, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.11× (z +9.1, q 2e-17, up in 12 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.516× (z -5.8, q 4e-06, down in 19 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FERMT3]] (+0.70, fdr 7e-06), [[A3GALT2]] (+0.67, fdr 1e-05), [[BMP8A]] (+0.66, fdr 1e-05); moves opposite to [[RCOR3]] (-0.57, fdr 1e-05), [[CHPT1]] (-0.50, fdr 2e-04).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SSC5D]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12585.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.18×** | +9.7 | 3e-19 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +9.1 | 2e-17 | 12/26 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.81×** | +9.0 | 5e-17 | 26/40 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.52×** | +8.0 | 1e-13 | 19/37 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +7.3 | 3e-11 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.26×** | +7.1 | 1e-10 | 17/38 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.7 | 2e-09 | 7/23 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.70×** | +6.5 | 7e-09 | 15/40 (NCI-H2030, NCI-H1573, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.03×** | +6.1 | 5e-08 | 18/41 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.89×** | +5.5 | 2e-06 | 0/6 | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.09×** | +5.1 | 2e-05 | 10/31 (NCI-H460, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +4.4 | 4e-04 | 3/14 (NCI-H2030, PANC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +3.9 | 0.004 | 4/29 (SW480, NCI-H460, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.005 | 3/40 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +3.8 | 0.006 | 3/24 (NCI-H23, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.57×** | +3.7 | 0.008 | 5/31 (LOX-IMVI, LoVo, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +3.5 | 0.015 | 2/29 (SW480, HCT15) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.54×** | +3.5 | 0.016 | 2/11 (PANC-1, LoVo) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12585.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.516×** | -5.8 | 4e-06 | 19/43 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.525×** | -5.6 | 5e-06 | 18/35 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.594×** | -4.6 | 9e-04 | 12/25 (NCI-H23, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.658×** | -3.7 | 0.034 | 7/10 (HOP62, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.674×** | -3.5 | 0.060 | 12/43 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mozavaptan (drug)]] 5 µM |  | 0.697× | -3.1 | 0.21 | 5/19 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12585. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 5.07 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0860× (z -8.7) |
| [[A-172 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.555 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.864 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.575 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.622 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.623 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.806 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.690 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.833 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.853 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.759 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.700 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.556 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.947 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.790 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12585), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FERMT3]] | +0.70 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[A3GALT2]] | +0.67 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[BMP8A]] | +0.66 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[MSANTD1]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[PDE2A]] | +0.66 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[PTCH2]] | +0.63 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SMIM41]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[C13orf46]] | +0.62 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[MYO15A]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[UCKL1-AS1]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[GSG1L]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SPTBN5]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCOR3]] | -0.57 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CHPT1]] | -0.50 | -0.55 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSC5D]] | B | SSC5D activity raises NTRK1's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.57× lower at baseline in the lines without SSC5D | 0.026 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.8, -15.2); signed map (16.4, 15.4). **Vector** length 45.8, 6.27% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +3.2 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +6.5 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.5 | +3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +3.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +0.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -4.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -0.2 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | neurotrophic receptor tyrosine kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.1 — chr1:156,815,636-156,881,850 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TRK, TRKA, MTC |
| Gene groups (HGNC) | Immunoglobulin like domain containing; Neurotrophic receptor tyrosine kinase family |
| Reactome | 15 pathways, smallest: NGF-independant TRKA activation; PLC-gamma1 signalling; Signalling to STAT3 |
| Matched by | ensembl_id |

**Function**, from UniProt [P04629](https://www.uniprot.org/uniprotkb/P04629) (High affinity nerve growth factor receptor):

> Receptor tyrosine kinase involved in the development and the maturation of the central and peripheral nervous systems through regulation of proliferation, differentiation and survival of sympathetic and nervous neurons. High affinity receptor for NGF which is its primary ligand. Can also bind and be activated by NTF3/neurotrophin-3. However, NTF3 only supports axonal extension through NTRK1 but has no effect on neuron survival (By similarity). Upon dimeric NGF ligand-binding, undergoes …

**Summary**, from NCBI Gene [4914](https://www.ncbi.nlm.nih.gov/gene/4914):

> This gene encodes a member of the neurotrophic tyrosine kinase receptor (NTKR) family. This kinase is a membrane-bound receptor that, upon neurotrophin binding, phosphorylates itself and members of the MAPK pathway. The presence of this kinase leads to cell differentiation and may play a role in specifying sensory neuron subtypes. Mutations in this gene have been associated with congenital insensitivity to pain, anhidrosis, self-mutilating behavior, cognitive disability and cancer. Alternate …

**Accessions** — [HGNC:8031](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8031) · Entrez [4914](https://www.ncbi.nlm.nih.gov/gene/4914) · UniProt [P04629](https://www.uniprot.org/uniprotkb/P04629) · Ensembl [ENSG00000198400](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198400)

## Data

Gene col 12585: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12585); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12585, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12585]; `tensor/DDL_lfc|DDL_z.npy` [12585]; `embed/gene_vectors.npy` [12585]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12585 or target_col == 12585). Every well: [[NTRK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NTRK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
