---
symbol: "NDUFS7"
type: "gene"
col: 3651
ensembl_id: "ENSG00000115286"
name: "NADH:ubiquinone oxidoreductase core subunit S7"
location: "19p13.3"
module: 58
arm: "+"
pooled_cpm: 13.53
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# NDUFS7

*NADH:ubiquinone oxidoreductase core subunit S7* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.25× (z +8.1, q 3e-13, up in 33 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 1.94× (z +3.9, q 0.006, up in 21 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.743× (z -3.9, q 0.058, down in 19 of 48 measured lines) ⚠ cell-cycle shift, explains ~64% of this change.
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA3]] (+0.79, fdr 7e-06), [[NDUFS8]] (+0.69, fdr 7e-06), [[DPM3]] (+0.67, fdr 7e-06); moves opposite to [[EIF4G2]] (-0.57, fdr 5e-05), [[NCR3LG1]] (-0.57, fdr 6e-05), [[ADSS2]] (-0.56, fdr 3e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3651.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.25×** | +8.1 | 3e-13 | 33/36 (SW480, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **2.00×** | +6.4 | 4e-08 | 19/30 (MIA PaCa-2, HS-578T, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.82×** | +5.8 | 2e-06 | 14/27 (HT-29, J82, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.71×** | +5.4 | 1e-05 | 32/47 (LS 180, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.68×** | +5.2 | 3e-05 | 26/42 (KATO III, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.66×** | +5.1 | 3e-05 | 32/47 (SW480, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.51×** | +4.1 | 0.003 | 22/46 (KATO III, SW480, …) | top dose only | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.94×** | +3.9 | 0.006 | 21/45 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.85×** | +3.6 | 0.017 | 18/43 (SNU-423, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.43×** | +3.6 | 0.017 | 16/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.43×** | +3.5 | 0.028 | 17/41 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.40×** | +3.2 | 0.061 | 15/48 (RKO, SW 1088, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.70×** | +3.1 | 0.072 | 8/45 (NCI-H1792, NCI-H2347, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.072 | 13/46 (H4, HT-29, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.36×** | +3.1 | 0.072 | 12/47 (SW480, PANC-1, …) | rises with dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3651.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.743×** | -3.9 | 0.058 | 19/48 (LOX-IMVI, RPMI-7951, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3651. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 15.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | — |
| [[A-172 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3651), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 6 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA3]] | +0.79 | +0.77 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[NDUFS8]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[DPM3]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[TMEM160]] | +0.67 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[PIN1]] | +0.67 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[ANAPC11]] | +0.65 | +0.51 / +0.57 | both halves | 1e-05 | STRING 427 |
| [[AKR7A2]] | +0.65 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[PTOV1]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[NDUFAB1]] | +0.63 | +0.56 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[MRPL41]] ⚠ | +0.62 | +0.51 / +0.53 | both halves | 1e-05 | STRING 434; ⚠ in the vector space only through flagged drug-doses |
| [[UNC45A]] | +0.62 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[LAMTOR4]] | +0.61 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[ALKBH7]] | +0.61 | +0.53 / +0.54 | both halves | 1e-05 | STRING 548 |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.57 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[NCR3LG1]] | -0.57 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[ADSS2]] | -0.56 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[EIF4G1]] | -0.55 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[EIF5]] | -0.55 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[KRT8P12]] | -0.55 | -0.37 / -0.47 | both halves | 9e-05 |  |
| [[HNRNPA2B1]] | -0.54 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[HNRNPU]] | -0.53 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[ZNF300]] | -0.52 | -0.26 / -0.44 | both halves | 4e-04 |  |
| [[TASOR]] | -0.52 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[FNBP1P1]] | -0.52 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[C22orf46]] | -0.51 | -0.37 / -0.44 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.3, -19.1); signed map (-37.1, 6.7). **Vector** length 56.6, 10.7% of its response variance represented; |z| ≥ 3 in 505 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +2.6 | +5.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +2.6 | +5.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +2.4 | +4.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +3.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.3 | +1.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.1 | +3.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.7 | -0.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -2.3 | -3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -1.3 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.1 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase core subunit S7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,383,527-1,395,589 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PSST, FLJ46880, FLJ45860, CI-20 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase core subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O75251](https://www.uniprot.org/uniprotkb/O75251) (NADH dehydrogenase):

> Core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I) which catalyzes electron transfer from NADH through the respiratory chain, using ubiquinone as an electron acceptor. Essential for the catalytic activity of complex I.

**Summary**, from NCBI Gene [374291](https://www.ncbi.nlm.nih.gov/gene/374291):

> This gene encodes a protein that is a subunit of one of the complexes that forms the mitochondrial respiratory chain. This protein is one of over 40 subunits found in complex I, the nicotinamide adenine dinucleotide (NADH):ubiquinone oxidoreductase. This complex functions in the transfer of electrons from NADH to the respiratory chain, and ubiquinone is believed to be the immediate electron acceptor for the enzyme. Mutations in this gene cause Leigh syndrome due to mitochondrial complex I …

**Accessions** — [HGNC:7714](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7714) · Entrez [374291](https://www.ncbi.nlm.nih.gov/gene/374291) · UniProt [O75251](https://www.uniprot.org/uniprotkb/O75251) · Ensembl [ENSG00000115286](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115286)

## Data

Gene col 3651: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3651); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3651, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3651]; `tensor/DDL_lfc|DDL_z.npy` [3651]; `embed/gene_vectors.npy` [3651]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3651 or target_col == 3651). Every well: [[NDUFS7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFS7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
