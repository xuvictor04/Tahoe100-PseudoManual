---
symbol: "MRPL15"
type: "gene"
col: 6032
ensembl_id: "ENSG00000137547"
name: "mitochondrial ribosomal protein L15"
location: "8q11.23"
module: 1
arm: "+"
pooled_cpm: 18.84
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MRPL15

*mitochondrial ribosomal protein L15* — 8q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.91× (z +6.5, q 4e-08, up in 34 of 42 measured lines) ⚠ transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.72× (z +5.5, q 9e-06, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.685× (z -5.4, q 4e-05, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRS1]] (+0.76, fdr 7e-06), [[BRIX1]] (+0.75, fdr 7e-06), [[KAT14]] (+0.73, fdr 7e-06); moves opposite to [[APLP2]] (-0.62, fdr 8e-06), [[NUCB1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6032.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.91×** | +6.5 | 4e-08 | 34/42 (SW1417, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +5.8 | 2e-06 | 25/37 (NCI-H2347, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.72×** | +5.5 | 9e-06 | 35/47 (PANC-1, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +5.2 | 3e-05 | 22/32 (KATO III, HS-578T, …) | two highest doses | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +4.4 | 0.001 | 23/47 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.4 | 0.001 | 27/44 (HS-578T, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.003 | 22/48 (NCI-H1792, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.004 | 20/47 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +3.3 | 0.052 | 20/47 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.26×** | +3.3 | 0.054 | 19/48 (CFPAC-1, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 1.37× | +3.1 | 0.11 | 17/46 (NCI-H1792, NCI-H2030, …) | two highest doses | composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.35× | +3.1 | 0.11 | 15/47 (A549, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6032.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.685×** | -5.4 | 4e-05 | 27/47 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.718×** | -4.7 | 7e-04 | 27/47 (COLO 205, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.649×** | -4.3 | 0.003 | 23/47 (SW 900, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.656×** | -4.2 | 0.003 | 24/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.682×** | -3.8 | 0.013 | 25/47 (SW480, SW 1271, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6032. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 35.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -11.7) |
| [[COLO 205 (line)]] | alt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0787× (z -12.5) |
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0756× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 18.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 26.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -9.6) |
| [[SW48 (line)]] | wt | 22.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.111× (z -9.6) |
| [[A-172 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 50.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6032), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRS1]] | +0.76 | +0.75 / +0.74 | both halves | 7e-06 |  |
| [[BRIX1]] | +0.75 | +0.69 / +0.78 | both halves | 7e-06 | STRING 462 |
| [[KAT14]] | +0.73 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[WDR75]] | +0.73 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[IMP4]] | +0.72 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[PAK1IP1]] | +0.72 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[COA4]] | +0.71 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[ZNHIT6]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[MRPL58]] | +0.70 | +0.61 / +0.77 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 974 |
| [[NIFK]] | +0.69 | +0.69 / +0.71 | both halves | 7e-06 | STRING 623 |
| [[ZBTB24]] | +0.68 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[TIMM9]] | +0.68 | +0.57 / +0.73 | both halves | 8e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APLP2]] | -0.62 | -0.58 / -0.60 | both halves | 8e-06 | pathway: HALLMARK_ADIPOGENESIS |
| [[NUCB1]] | -0.62 | -0.53 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MRPL15's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MRPL50]] | C | MRPL50's natural level strengthens MRPL15's drug response | MRPL50's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67, reverse -0.13; direction not clear | 0.031 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.762). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-47.2, -7.5); signed map (-2.1, -40.5). **Vector** length 73.8, 17.4% of its response variance represented; |z| ≥ 3 in 579 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.53 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.54 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.54 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +5.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.6 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.8 | +4.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +1.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.2 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.5 | +0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q11.23 — chr8:54,135,241-54,148,514 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPML7, MRP-L7, HSPC145, L15mt, MRP-L15, uL15m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Hallmark sets | ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9P015](https://www.uniprot.org/uniprotkb/Q9P015) carries no function annotation.

**Summary**, from NCBI Gene [29088](https://www.ncbi.nlm.nih.gov/gene/29088):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14054](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14054) · Entrez [29088](https://www.ncbi.nlm.nih.gov/gene/29088) · UniProt [Q9P015](https://www.uniprot.org/uniprotkb/Q9P015) · Ensembl [ENSG00000137547](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137547)

## Data

Gene col 6032: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6032); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6032, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6032]; `tensor/DDL_lfc|DDL_z.npy` [6032]; `embed/gene_vectors.npy` [6032]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6032 or target_col == 6032). Every well: [[MRPL15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
