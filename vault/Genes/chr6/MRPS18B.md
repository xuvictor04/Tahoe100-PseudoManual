---
symbol: "MRPS18B"
type: "gene"
col: 12890
ensembl_id: "ENSG00000204568"
name: "mitochondrial ribosomal protein S18B"
location: "6p21.33"
module: 11
arm: "+"
pooled_cpm: 44.09
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# MRPS18B

*mitochondrial ribosomal protein S18B* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.82× (z +4.5, q 0.003, up in 38 of 48 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.06× (z +4.4, q 0.003, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.638× (z -5.0, q 3e-04, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEBPZ]] (+0.81, fdr 7e-06), [[PIGBOS1]] (+0.79, fdr 7e-06), [[COIL]] (+0.78, fdr 7e-06); moves opposite to [[AKT1]] (-0.66, fdr 7e-06), [[MAN2B2]] (-0.65, fdr 1e-05), [[CTSZ]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12890.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.82×** | +4.5 | 0.003 | 38/48 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.06×** | +4.4 | 0.003 | 43/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.66×** | +4.0 | 0.013 | 36/46 (HOP62, AsPC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.61×** | +3.7 | 0.025 | 37/48 (LoVo, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.60×** | +3.7 | 0.026 | 33/47 (LoVo, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 1.33× | +3.2 | 0.15 | 30/48 (KATO III, J82, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.32× | +3.1 | 0.16 | 31/48 (J82, PANC-1, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.1 | 0.16 | 2/48 (RKO, C-33 A) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12890.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.638×** | -5.0 | 3e-04 | 40/48 (H4, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.536×** | -4.9 | 3e-04 | 41/48 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.578×** | -4.3 | 0.003 | 37/48 (KATO III, PANC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.671× | -3.1 | 0.26 | 29/48 (NCI-H661, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12890. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 34.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 41.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -9.2) |
| [[A-172 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 99.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 94.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 57.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12890), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEBPZ]] | +0.81 | +0.79 / +0.81 | both halves | 7e-06 |  |
| [[PIGBOS1]] | +0.79 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[COIL]] | +0.78 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.76 | +0.72 / +0.82 | both halves | 7e-06 |  |
| [[PHAX]] | +0.76 | +0.68 / +0.81 | both halves | 7e-06 |  |
| [[ESF1]] | +0.76 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[PEX12]] | +0.74 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.74 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[PPIG]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[SURF6]] | +0.73 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[SEC62]] | +0.72 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[AGGF1]] | +0.72 | +0.70 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT1]] | -0.66 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[MAN2B2]] | -0.65 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[CTSZ]] | -0.65 | -0.52 / -0.71 | both halves | 1e-05 |  |
| [[ANKRD30BL]] | -0.63 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[PGRMC1]] | -0.62 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[ADAM15]] | -0.62 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[SDC1]] | -0.62 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[NUCB1]] | -0.62 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[RNPEP]] | -0.62 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[TECR]] | -0.62 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[BCAP31]] | -0.61 | -0.60 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MRPS18B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TXNIP]] | B | TXNIP activity lowers MRPS18B's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.16× higher at baseline in the lines without TXNIP | 0.083 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[ZNF573]] | C | ZNF573 activity raises MRPS18B's level | lines that do not express ZNF573 (4) vs lines expressing it (46) | 1.26× lower at baseline in the lines without ZNF573 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with FBXW7; also absent: ZNF540, ZNF675, ZNF571 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.795). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.9, 2.2); signed map (-0.7, -19.5). **Vector** length 93.4, 34.0% of its response variance represented; |z| ≥ 3 in 567 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +7.3 | +3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.8 | +4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +6.1 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +0.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.3 | +1.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -1.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.6 | +0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.4 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.3 | +2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -5.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -0.8 |
|  | [[Folic acid (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -1.6 | -2.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.6 | -0.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein S18B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:30,617,840-30,626,395 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRPS18-2, PTD017, C6orf14, HSPC183, mS40 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Small subunit mitochondrial ribosomal proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9Y676](https://www.uniprot.org/uniprotkb/Q9Y676) carries no function annotation.

**Summary**, from NCBI Gene [28973](https://www.ncbi.nlm.nih.gov/gene/28973):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14516](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14516) · Entrez [28973](https://www.ncbi.nlm.nih.gov/gene/28973) · UniProt [Q9Y676](https://www.uniprot.org/uniprotkb/Q9Y676) · Ensembl [ENSG00000204568](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204568)

## Data

Gene col 12890: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12890); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12890, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12890]; `tensor/DDL_lfc|DDL_z.npy` [12890]; `embed/gene_vectors.npy` [12890]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12890 or target_col == 12890). Every well: [[MRPS18B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPS18B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
