---
symbol: "POLR2J"
type: "gene"
col: 66
ensembl_id: "ENSG00000005075"
name: "RNA polymerase II subunit J"
location: "7q22.1"
module: 24
arm: "+"
pooled_cpm: 15.08
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# POLR2J

*RNA polymerase II subunit J* — 7q22.1

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.24× (z +6.4, q 1e-07, up in 34 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Rifaximin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0541×).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 25 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF181]] (+0.80, fdr 1e-05), [[C4orf48]] (+0.79, fdr 1e-05), [[UQCR10]] (+0.78, fdr 7e-06, ⚠ UQCR10 in the vector space only through flagged drug-doses), [[TMEM256]] (+0.77, fdr 2e-04); moves opposite to [[SRSF1]] (-0.80, fdr 1e-05), [[U2AF2]] (-0.73, fdr 4e-05), [[DDX39B]] (-0.67, fdr 4e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RASSF7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 66.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **3.24×** | +6.4 | 1e-07 | 34/37 (SW480, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.89×** | +6.2 | 1e-07 | 25/28 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.21×** | +4.8 | 2e-04 | 42/48 (HOP62, LoVo, …) | two highest doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **2.00×** | +4.2 | 0.003 | 29/43 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.80×** | +3.6 | 0.036 | 30/48 (HOP62, LoVo, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **1.79×** | +3.3 | 0.099 | 21/32 (HOP62, HS-578T, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 66.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Rifaximin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0541×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | 0.326× | -3.6 | 0.19 | 28/44 (NCI-H460, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, +0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 66. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 10.4 | 0 | 1 | — | [[Rifaximin (drug)]] 5 µM 0.0541× (z -9.1) |
| [[A-172 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 66), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 25 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF181]] | +0.80 | +0.52 / +0.86 | both halves | 1e-05 | STRING 592 |
| [[C4orf48]] | +0.79 | +0.51 / +0.79 | both halves | 1e-05 |  |
| [[UQCR10]] ⚠ | +0.78 | +0.65 / +0.76 | both halves | 7e-06 | STRING 482; ⚠ in the vector space only through flagged drug-doses |
| [[TMEM256]] | +0.77 | +0.32 / +0.79 | both halves | 2e-04 |  |
| [[LAMTOR5]] | +0.76 | +0.46 / +0.79 | both halves | 2e-05 |  |
| [[IFI27L2]] | +0.76 | +0.60 / +0.79 | both halves | 7e-06 |  |
| [[KRTCAP2]] | +0.76 | +0.52 / +0.84 | both halves | 1e-05 |  |
| [[EMC6]] | +0.76 | +0.62 / +0.82 | both halves | 7e-06 |  |
| [[ATP5MJ]] | +0.76 | +0.44 / +0.75 | both halves | 3e-05 |  |
| [[POLR2I]] | +0.75 | +0.29 / +0.79 | both halves | 3e-04 | same gene group; pathway: HALLMARK_DNA_REPAIR; STRING 999 |
| [[ROMO1]] | +0.75 | +0.52 / +0.78 | both halves | 1e-05 |  |
| [[MIEN1]] | +0.74 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[ATP5MK]] | +0.74 | +0.50 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF1]] | -0.80 | -0.53 / -0.81 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 581 |
| [[U2AF2]] | -0.73 | -0.42 / -0.71 | both halves | 4e-05 | pathway: Dengue Virus-Host Interactions |
| [[DDX39B]] | -0.67 | -0.41 / -0.60 | both halves | 4e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[EWSR1]] | -0.66 | -0.33 / -0.68 | both halves | 1e-04 |  |
| [[DARS2]] | -0.63 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[SYNCRIP]] | -0.63 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[HNRNPA3]] | -0.61 | -0.45 / -0.73 | both halves | 3e-05 | pathway: Dengue Virus-Host Interactions |
| [[SFPQ]] | -0.61 | -0.27 / -0.69 | both halves | 3e-04 |  |
| [[SSU72]] | -0.61 | -0.28 / -0.62 | both halves | 3e-04 | pathway: RNA polymerase II transcribes snRNA genes; STRING 558 |
| [[DDX3X]] | -0.61 | -0.21 / -0.63 | both halves | 6e-04 | pathway: Dengue Virus-Host Interactions |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASSF7]] | B | RASSF7 activity raises POLR2J's level | lines that do not express RASSF7 (5) vs lines expressing it (45) | 1.53× lower at baseline in the lines without RASSF7 | 0.036 | ⚠ within organs, on part of the lines; also absent: SORBS1, CTSV, BCL2L1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.768). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-45.1, -18.6); signed map (-32.9, 7.9). **Vector** length 53.1, 12.7% of its response variance represented; |z| ≥ 3 in 461 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.56 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +2.5 | +4.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +2.1 | +3.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +2.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +0.8 | +1.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.8 | +1.9 |
|  | [[Adagrasib (drug)]] 5 µM |  | +0.8 | +2.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +0.7 | +0.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | -4.1 | +3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | -3.0 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | -2.6 | +6.4 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -2.1 | +0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | +0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -3.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.1 | -0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase II subunit J |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:102,473,128-102,478,922 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPB11, hRPB14, RPB11A, RPB11m, POLR2J1 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 75 pathways, smallest: Signaling by FGFR2 IIIa TM; PIWI-interacting RNA (piRNA) biogenesis; Abortive elongation of HIV-1 transcript in the absence of Tat |
| Matched by | ensembl_id |

**Function**, from UniProt [P52435](https://www.uniprot.org/uniprotkb/P52435) (DNA-directed RNA polymerase II subunit RPB11-a):

> Core component of RNA polymerase II (Pol II), a DNA-dependent RNA polymerase which synthesizes mRNA precursors and many functional non-coding RNAs using the four ribonucleoside triphosphates as substrates.

**Summary**, from NCBI Gene [5439](https://www.ncbi.nlm.nih.gov/gene/5439):

> This gene encodes a subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. The product of this gene exists as a heterodimer with another polymerase subunit; together they form a core subassembly unit of the polymerase. Two similar genes are located nearby on chromosome 7q22.1 and a pseudogene is found on chromosome 7p13. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9197](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9197) · Entrez [5439](https://www.ncbi.nlm.nih.gov/gene/5439) · UniProt [P52435](https://www.uniprot.org/uniprotkb/P52435) · Ensembl [ENSG00000005075](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005075)

## Data

Gene col 66: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 66); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 66, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 66]; `tensor/DDL_lfc|DDL_z.npy` [66]; `embed/gene_vectors.npy` [66]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 66 or target_col == 66). Every well: [[POLR2J — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR2J.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
