---
symbol: "COX5A"
type: "gene"
col: 10955
ensembl_id: "ENSG00000178741"
name: "cytochrome c oxidase subunit 5A"
location: "15q24.2"
module: 43
arm: "+"
pooled_cpm: 70.65
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# COX5A

*cytochrome c oxidase subunit 5A* — 15q24.2

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.91× (z +7.0, q 2e-09, up in 37 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX4I1]] (+0.83, fdr 7e-06, ⚠ COX4I1 in the vector space only through flagged drug-doses), [[ATP5ME]] (+0.78, fdr 1e-05), [[TOMM7]] (+0.78, fdr 8e-06), [[RPL36]] (+0.77, fdr 8e-06); moves opposite to [[NRAS]] (-0.75, fdr 7e-06), [[ZNF460]] (-0.72, fdr 1e-05), [[SMU1]] (-0.71, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10955.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.91×** | +7.0 | 2e-09 | 37/42 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **3.22×** | +6.7 | 5e-09 | 47/49 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.11×** | +5.1 | 8e-05 | 45/47 (SW480, COLO 205, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **2.00×** | +4.7 | 3e-04 | 44/48 (PANC-1, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.97×** | +4.3 | 0.002 | 38/45 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **1.66×** | +3.3 | 0.087 | 32/47 (C32, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10955.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Folic acid (drug)]] 5 µM |  | 0.724× | -3.1 | 0.53 | 34/48 (Hs 766T, SHP-77, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10955. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 63.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 98.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 50.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 60.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 112 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 120 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 92.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 67.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 97.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 79.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10955), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 24 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX4I1]] ⚠ | +0.83 | +0.70 / +0.86 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5ME]] | +0.78 | +0.52 / +0.85 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 935 |
| [[TOMM7]] | +0.78 | +0.58 / +0.79 | both halves | 8e-06 | STRING 403 |
| [[RPL36]] | +0.77 | +0.58 / +0.80 | both halves | 8e-06 |  |
| [[LAMTOR5]] | +0.77 | +0.49 / +0.78 | both halves | 1e-05 | pathway: TP53 Regulates Metabolic Genes |
| [[ATP5MK]] | +0.77 | +0.58 / +0.82 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 762 |
| [[RPL36AL]] ⚠ | +0.77 | +0.66 / +0.76 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ROMO1]] | +0.76 | +0.60 / +0.82 | both halves | 7e-06 |  |
| [[RPS27A]] ⚠ | +0.76 | +0.63 / +0.77 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MJ]] | +0.75 | +0.44 / +0.84 | both halves | 3e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[UQCRB]] ⚠ | +0.75 | +0.59 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5F1E]] | +0.74 | +0.70 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 620 |
| [[NDUFA1]] | +0.74 | +0.64 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 934 |
| [[COX6B1]] | +0.74 | +0.55 / +0.83 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[RPS29]] | +0.73 | +0.57 / +0.77 | both halves | 1e-05 |  |
| [[C4orf48]] | +0.73 | +0.47 / +0.70 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRAS]] | -0.75 | -0.63 / -0.76 | both halves | 7e-06 |  |
| [[ZNF460]] | -0.72 | -0.55 / -0.71 | both halves | 1e-05 |  |
| [[SMU1]] | -0.71 | -0.49 / -0.76 | both halves | 1e-05 |  |
| [[SF3B4]] | -0.69 | -0.48 / -0.69 | both halves | 2e-05 |  |
| [[PEX19]] | -0.68 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[EIF4G2]] | -0.65 | -0.43 / -0.63 | both halves | 3e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[GBA1]] | -0.64 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[PDAP1]] | -0.63 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[C17orf80]] | -0.63 | -0.41 / -0.46 | both halves | 4e-05 | STRING 674 |
| [[LIN7C]] | -0.63 | -0.43 / -0.68 | both halves | 3e-05 |  |
| [[U2AF2]] | -0.62 | -0.40 / -0.64 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.631). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-45.0, -23.4); signed map (-34.4, 8.3). **Vector** length 59.7, 25.2% of its response variance represented; |z| ≥ 3 in 404 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.52 to 55); *Peptide chain elongation* (reactome, mean cos +0.53 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.52 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +2.7 | +5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | -0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.6 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | -0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.1 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | -0.1 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.0 | -0.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -5.4 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | -4.8 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -4.5 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.5 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase subunit 5A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.2 — chr15:74,919,791-74,938,083 (-) |
| Ensembl biotype | protein_coding |
| Also known as | COX-VA |
| Gene groups (HGNC) | Mitochondrial complex IV: cytochrome c oxidase subunits |
| Hallmark sets | MYC_TARGETS_V1, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 10 pathways, smallest: Complex IV assembly; Cytoprotection by HMOX1; TP53 Regulates Metabolic Genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P20674](https://www.uniprot.org/uniprotkb/P20674) (Cytochrome c oxidase subunit 5A, mitochondrial):

> Component of the cytochrome c oxidase, the last enzyme in the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular oxygen, creating an electrochemical gradient over …

**Summary**, from NCBI Gene [9377](https://www.ncbi.nlm.nih.gov/gene/9377):

> Cytochrome c oxidase (COX) is the terminal enzyme of the mitochondrial respiratory chain. It is a multi-subunit enzyme complex that couples the transfer of electrons from cytochrome c to molecular oxygen and contributes to a proton electrochemical gradient across the inner mitochondrial membrane. The complex consists of 13 mitochondrial- and nuclear-encoded subunits. The mitochondrially-encoded subunits perform the electron transfer of proton pumping activities. The functions of the …

**Accessions** — [HGNC:2267](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2267) · Entrez [9377](https://www.ncbi.nlm.nih.gov/gene/9377) · UniProt [P20674](https://www.uniprot.org/uniprotkb/P20674) · Ensembl [ENSG00000178741](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178741)

## Data

Gene col 10955: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10955); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10955, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10955]; `tensor/DDL_lfc|DDL_z.npy` [10955]; `embed/gene_vectors.npy` [10955]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10955 or target_col == 10955). Every well: [[COX5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
