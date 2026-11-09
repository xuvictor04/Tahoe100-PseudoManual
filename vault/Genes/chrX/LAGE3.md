---
symbol: "LAGE3"
type: "gene"
col: 12315
ensembl_id: "ENSG00000196976"
name: "L antigen family member 3"
location: "Xq28"
module: 24
arm: "+"
pooled_cpm: 9.78
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# LAGE3

*L antigen family member 3* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.79× (z +5.9, q 3e-06, up in 14 of 18 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.585× (z -4.5, q 0.004, down in 26 of 43 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIEN1]] (+0.78, fdr 7e-06), [[MRPL41]] (+0.76, fdr 1e-05, ⚠ MRPL41 in the vector space only through flagged drug-doses), [[SF3B5]] (+0.76, fdr 1e-05, ⚠ SF3B5 in the vector space only through flagged drug-doses), [[TRAPPC5]] (+0.75, fdr 1e-05), [[ANTKMT]] (+0.73, fdr 2e-05); moves opposite to [[PSME3IP1]] (-0.63, fdr 7e-05), [[U2AF2]] (-0.62, fdr 0.001, ⚠ one half only (not replicated)), [[STX16]] (-0.62, fdr 5e-05), [[HNRNPA2B1]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HES6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12315.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.79×** | +5.9 | 3e-06 | 14/18 (Hs 766T, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.45×** | +5.1 | 9e-05 | 29/36 (NCI-H2030, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **2.54×** | +5.0 | 1e-04 | 24/30 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **2.21×** | +4.7 | 4e-04 | 25/38 (SW 900, Panc 03.27, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.75× | +3.3 | 0.10 | 21/47 (KATO III, SW1417, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12315.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.585×** | -4.5 | 0.004 | 26/43 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.300× | -3.5 | 0.12 | 24/42 (HOP62, H4, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12315. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12315), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 11 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIEN1]] | +0.78 | +0.63 / +0.79 | both halves | 7e-06 |  |
| [[MRPL41]] ⚠ | +0.76 | +0.50 / +0.76 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SF3B5]] ⚠ | +0.76 | +0.56 / +0.78 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TRAPPC5]] | +0.75 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[ANTKMT]] | +0.73 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[POLR2H]] | +0.72 | +0.43 / +0.76 | both halves | 3e-05 |  |
| [[CIAO2B]] | +0.71 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[ANAPC11]] | +0.71 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[DPM3]] | +0.71 | +0.52 / +0.75 | both halves | 1e-05 |  |
| [[C4orf48]] | +0.71 | +0.36 / +0.75 | both halves | 9e-05 |  |
| [[RNF114]] | +0.71 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[LSM2]] | +0.71 | +0.39 / +0.71 | both halves | 6e-05 |  |
| [[NDUFA7]] | +0.70 | +0.37 / +0.74 | both halves | 8e-05 |  |
| [[DCTN6-DT]] | +0.70 | +0.52 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 2 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3IP1]] | -0.63 | -0.38 / -0.59 | both halves | 7e-05 |  |
| [[U2AF2]] | -0.62 | -0.17 / -0.65 | ⚠ one half (not replicated) | 0.001 |  |
| [[STX16]] | -0.62 | -0.40 / -0.65 | both halves | 5e-05 |  |
| [[HNRNPA2B1]] | -0.61 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[ILF3]] | -0.61 | -0.38 / -0.62 | both halves | 7e-05 |  |
| [[WASH8P]] ⚠ | -0.60 | -0.43 / -0.55 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EWSR1]] | -0.60 | -0.37 / -0.58 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HES6]] | B | HES6 activity raises LAGE3's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.56× lower at baseline in the lines without HES6 | 0.044 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.780). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-43.2, -19.1); signed map (-30.7, 9.5). **Vector** length 57.5, 12.9% of its response variance represented; |z| ≥ 3 in 500 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.52 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +2.9 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.6 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.0 | +2.0 |
|  | [[Bendamustine (drug)]] 5 µM |  | +1.0 | +2.5 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | +0.9 | +2.7 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -3.8 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.7 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | -3.2 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | +0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | L antigen family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,477,775-154,479,281 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ITBA2, CVG5, DXS9951E, DXS9879E, ESO3, Pcc1 |
| Gene groups (HGNC) | KEOPS complex |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14657](https://www.uniprot.org/uniprotkb/Q14657) (EKC/KEOPS complex subunit LAGE3):

> Component of the EKC/KEOPS complex that is required for the formation of a threonylcarbamoyl group on adenosine at position 37 (t(6)A37) in tRNAs that read codons beginning with adenine. The complex is probably involved in the transfer of the threonylcarbamoyl moiety of threonylcarbamoyl-AMP (TC-AMP) to the N6 group of A37. LAGE3 functions as a dimerization module for the complex.

**Summary**, from NCBI Gene [8270](https://www.ncbi.nlm.nih.gov/gene/8270):

> This gene belongs to the ESO/LAGE gene family, members of which are clustered together on chromosome Xq28, and have similar exon-intron structures. Unlike the other family members which are normally expressed only in testis and activated in a wide range of human tumors, this gene is ubiquitously expressed in somatic tissues. The latter, combined with the finding that it is highly conserved in mouse and rat, suggests that the encoded protein is functionally important. An intronless pseudogene …

**Accessions** — [HGNC:26058](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26058) · Entrez [8270](https://www.ncbi.nlm.nih.gov/gene/8270) · UniProt [Q14657](https://www.uniprot.org/uniprotkb/Q14657) · Ensembl [ENSG00000196976](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196976)

## Data

Gene col 12315: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12315); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12315, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12315]; `tensor/DDL_lfc|DDL_z.npy` [12315]; `embed/gene_vectors.npy` [12315]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12315 or target_col == 12315). Every well: [[LAGE3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAGE3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
