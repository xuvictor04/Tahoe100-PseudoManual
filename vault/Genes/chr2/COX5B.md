---
symbol: "COX5B"
type: "gene"
col: 5785
ensembl_id: "ENSG00000135940"
name: "cytochrome c oxidase subunit 5B"
location: "2q11.2"
module: 48
arm: "+"
pooled_cpm: 39.83
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# COX5B

*cytochrome c oxidase subunit 5B* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.56× (z +7.8, q 4e-12, up in 46 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.52× (z +4.2, q 0.004, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.499× (z -6.9, q 3e-09, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA2]] (+0.76, fdr 5e-05), [[OST4]] (+0.71, fdr 3e-05), [[RNF181]] (+0.70, fdr 1e-05); moves opposite to [[SFPQ]] (-0.68, fdr 2e-05), [[SRRM2]] (-0.64, fdr 5e-05), [[THOC6]] (-0.62, fdr 4e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5785.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.56×** | +7.8 | 4e-12 | 46/46 (NCI-H460, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.18×** | +5.3 | 4e-05 | 32/39 (NCI-H460, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.95×** | +4.3 | 0.003 | 32/43 (PANC-1, A549, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.2 | 0.004 | 32/48 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.75×** | +3.9 | 0.009 | 36/46 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.54× | +3.0 | 0.22 | 30/48 (SW480, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5785.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.499×** | -6.9 | 3e-09 | 46/47 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.489×** | -5.0 | 1e-04 | 42/48 (BT-474, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.493×** | -5.0 | 1e-04 | 40/48 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.567×** | -4.0 | 0.009 | 32/47 (SNU-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.631× | -3.2 | 0.14 | 27/48 (SNU-1, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5785. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 69.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 34.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 37.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 34.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -9.1) |
| [[A-172 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 49.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 58.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 40.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5785), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 7 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA2]] | +0.76 | +0.40 / +0.82 | both halves | 5e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 994 |
| [[OST4]] | +0.71 | +0.46 / +0.84 | both halves | 3e-05 |  |
| [[RNF181]] | +0.70 | +0.53 / +0.74 | both halves | 1e-05 |  |
| [[COX14]] | +0.70 | +0.44 / +0.72 | both halves | 3e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 868 |
| [[NDUFA7]] | +0.70 | +0.41 / +0.73 | both halves | 4e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 982 |
| [[MRPL55]] | +0.69 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[DDT]] | +0.68 | +0.42 / +0.76 | both halves | 4e-05 |  |
| [[ATP5PF]] | +0.68 | +0.45 / +0.83 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 834 |
| [[TMEM256]] | +0.68 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[C19orf53]] | +0.68 | +0.44 / +0.73 | both halves | 3e-05 |  |
| [[COX6A1]] | +0.67 | +0.42 / +0.76 | both halves | 4e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[LAMTOR2]] | +0.67 | +0.32 / +0.73 | both halves | 2e-04 | pathway: TP53 Regulates Metabolic Genes; STRING 404 |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SFPQ]] | -0.68 | -0.46 / -0.69 | both halves | 2e-05 |  |
| [[SRRM2]] | -0.64 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[THOC6]] | -0.62 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[SRSF1]] | -0.61 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[ANKRD18A]] | -0.61 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[PIEZO1]] | -0.60 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[NCR3LG1]] | -0.59 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[SRSF6]] | -0.59 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[ST7L]] | -0.59 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[SRSF10]] | -0.57 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[TEX261]] | -0.57 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[COA7]] | -0.57 | -0.44 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.695). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-45.3, -20.3); signed map (-37.3, 8.5). **Vector** length 67.2, 23.9% of its response variance represented; |z| ≥ 3 in 532 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.55 to 7); *Cristae formation* (reactome, mean cos +0.55 to 7); *adipogenesis* (hallmark, mean cos +0.52 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | -2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +2.3 | +3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +1.1 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | +1.1 | +0.9 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | +1.0 | +0.8 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.0 | +2.7 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | -5.7 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -5.1 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -4.8 | +7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.7 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase subunit 5B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:97,646,062-97,648,383 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Mitochondrial complex IV: cytochrome c oxidase subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 10 pathways, smallest: Complex IV assembly; Cytoprotection by HMOX1; TP53 Regulates Metabolic Genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P10606](https://www.uniprot.org/uniprotkb/P10606) (Cytochrome c oxidase subunit 5B, mitochondrial):

> Component of the cytochrome c oxidase, the last enzyme in the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular oxygen, creating an electrochemical gradient over …

**Summary**, from NCBI Gene [1329](https://www.ncbi.nlm.nih.gov/gene/1329):

> Cytochrome C oxidase (COX) is the terminal enzyme of the mitochondrial respiratory chain. It is a multi-subunit enzyme complex that couples the transfer of electrons from cytochrome c to molecular oxygen and contributes to a proton electrochemical gradient across the inner mitochondrial membrane. The complex consists of 13 mitochondrial- and nuclear-encoded subunits. The mitochondrially-encoded subunits perform the electron transfer and proton pumping activities. The functions of the …

**Accessions** — [HGNC:2269](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2269) · Entrez [1329](https://www.ncbi.nlm.nih.gov/gene/1329) · UniProt [P10606](https://www.uniprot.org/uniprotkb/P10606) · Ensembl [ENSG00000135940](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135940)

## Data

Gene col 5785: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5785); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5785, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5785]; `tensor/DDL_lfc|DDL_z.npy` [5785]; `embed/gene_vectors.npy` [5785]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5785 or target_col == 5785). Every well: [[COX5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
