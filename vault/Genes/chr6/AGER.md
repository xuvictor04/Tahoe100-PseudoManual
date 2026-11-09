---
symbol: "AGER"
type: "gene"
col: 12847
ensembl_id: "ENSG00000204305"
name: "advanced glycosylation end-product specific receptor"
location: "6p21.32"
module: 181
arm: "+"
pooled_cpm: 2.3
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# AGER

*advanced glycosylation end-product specific receptor* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.39× (z +7.1, q 5e-10, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.44× (z +4.4, q 0.002, up in 13 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.253× (z -11.7, q 4e-29, down in 33 of 45 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK3]] (+0.74, fdr 7e-06), [[PPP1R3F]] (+0.73, fdr 1e-05), [[COL11A2]] (+0.68, fdr 1e-05); moves opposite to [[VPS35]] (-0.54, fdr 4e-05), [[SPTLC2]] (-0.53, fdr 7e-05), [[NHP2]] (-0.53, fdr 3e-04).
> It is in [[Module 181]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12847.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.39×** | +7.1 | 5e-10 | 1/1 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +5.6 | 6e-06 | 2/2 (CFPAC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +4.5 | 0.002 | 4/12 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +4.4 | 0.002 | 13/34 (HepG2/C3A, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +3.6 | 0.038 | 1/11 (A-427) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.21×** | +3.5 | 0.038 | 0/3 | top dose only | noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.064 | 3/22 (LOX-IMVI, A-427, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.50×** | +3.3 | 0.073 | 1/40 (SNU-1) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +3.2 | 0.073 | 6/23 (KATO III, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12847.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.253×** | -11.7 | 4e-29 | 33/45 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.312×** | -10.0 | 6e-21 | 34/44 (HOP62, C-33 A, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.337×** | -9.3 | 3e-18 | 29/42 (HOP62, RKO, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.346×** | -4.7 | 2e-04 | 16/37 (HOP62, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.562×** | -4.7 | 2e-04 | 17/38 (NCI-H2030, PANC-1, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.624×** | -4.0 | 0.005 | 13/43 (HS-578T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.728×** | -3.8 | 0.010 | 13/32 (MIA PaCa-2, NCI-H1792, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.644×** | -3.8 | 0.012 | 10/44 (NCI-H2030, A498, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.492×** | -3.2 | 0.094 | 5/38 (SW480, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.683× | -3.1 | 0.11 | 11/40 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.703× | -3.0 | 0.13 | 11/45 (SW48, HOP62, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.55 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12847. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 2.20 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0317× (z -11.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1573 (line)]] | alt | 2.31 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0565× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 4.78 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.5 µM 0.0729× (z -9.6) |
| [[A-172 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.928 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.921 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12847), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK3]] | +0.74 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[PPP1R3F]] | +0.73 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[COL11A2]] | +0.68 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[CPT1B]] | +0.67 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[NLGN3]] | +0.66 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[GPRASP1]] | +0.64 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[PAQR6]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[CCDC17]] | +0.62 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[NPR2]] | +0.61 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[ZNF547]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TTC32]] | +0.60 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[MMRN2]] | +0.60 | +0.60 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS35]] | -0.54 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[SPTLC2]] | -0.53 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[NHP2]] | -0.53 | -0.46 / -0.27 | both halves | 3e-04 |  |
| [[ATG5]] | -0.51 | -0.50 / -0.27 | both halves | 3e-04 | pathway: DDX58/IFIH1-mediated induction of interferon-alpha/beta |
| [[GPS1]] | -0.50 | -0.40 / -0.32 | both halves | 2e-04 |  |
| [[ENDOD1]] | -0.50 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[TMEM147]] | -0.50 | -0.49 / -0.21 | both halves | 7e-04 |  |
| [[FAM210B]] | -0.50 | -0.56 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.725). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.2, -9.6); signed map (3.4, -10.0). **Vector** length 48.1, 5.72% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | -0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.3 | +3.4 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +1.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.1 | +2.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.5 | -9.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.4 | -10.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.1 | -11.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.6 | -3.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | advanced glycosylation end-product specific receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:32,180,968-32,184,322 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAGE, SCARJ1, sRAGE |
| Gene groups (HGNC) | C2-set domain containing; Scavenger receptors |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 25 pathways, smallest: Advanced glycosylation endproduct receptor signaling; TRAF6 mediated NF-kB activation; TAK1-dependent IKK and NF-kappa-B activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15109](https://www.uniprot.org/uniprotkb/Q15109) (Advanced glycation end product-specific receptor):

> Cell surface pattern recognition receptor that senses endogenous stress signals with a broad ligand repertoire including advanced glycation end products, S100 proteins, high-mobility group box 1 protein/HMGB1, amyloid beta/APP oligomers, nucleic acids, histones, phospholipids and glycosaminoglycans. Advanced glycation end products (AGEs) are nonenzymatically glycosylated proteins which accumulate in vascular tissue in aging and at an accelerated rate in diabetes. These ligands accumulate at …

**Summary**, from NCBI Gene [177](https://www.ncbi.nlm.nih.gov/gene/177):

> The advanced glycosylation end product (AGE) receptor encoded by this gene is a member of the immunoglobulin superfamily of cell surface receptors. It is a multiligand receptor, and besides AGE, interacts with other molecules implicated in homeostasis, development, and inflammation, and certain diseases, such as diabetes and Alzheimer's disease. Many alternatively spliced transcript variants encoding different isoforms, as well as non-protein-coding variants, have been described for this gene …

**Accessions** — [HGNC:320](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:320) · Entrez [177](https://www.ncbi.nlm.nih.gov/gene/177) · UniProt [Q15109](https://www.uniprot.org/uniprotkb/Q15109) · Ensembl [ENSG00000204305](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204305)

## Data

Gene col 12847: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12847); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12847, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12847]; `tensor/DDL_lfc|DDL_z.npy` [12847]; `embed/gene_vectors.npy` [12847]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12847 or target_col == 12847). Every well: [[AGER — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGER.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
