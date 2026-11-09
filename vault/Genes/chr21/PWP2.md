---
symbol: "PWP2"
type: "gene"
col: 14292
ensembl_id: "ENSG00000241945"
name: "PWP2 small subunit processome component"
location: "21q22.3"
module: 5
arm: "+"
pooled_cpm: 2.03
n_lines_expressing: 29
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PWP2

*PWP2 small subunit processome component* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.30× (z +6.2, q 3e-07, up in 3 of 7 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.72× (z +4.0, q 0.007, up in 12 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (J82 0.0837×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRP9]] (+0.69, fdr 7e-06), [[NIFK]] (+0.67, fdr 7e-06), [[NIP7]] (+0.67, fdr 7e-06); moves opposite to [[GNAS]] (-0.65, fdr 1e-05), [[PRCP]] (-0.63, fdr 1e-05), [[ARL6IP5]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[FADD]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14292.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.30×** | +6.2 | 3e-07 | 3/7 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.33×** | +6.0 | 4e-07 | 1/2 (HOP62) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.76×** | +4.2 | 0.005 | 10/25 (HOP62, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.72×** | +4.0 | 0.007 | 12/25 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +3.9 | 0.010 | 9/26 (MIA PaCa-2, RKO, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.5 | 0.036 | 3/13 (PANC-1, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +3.5 | 0.036 | 6/14 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.64×** | +3.4 | 0.043 | 1/4 (J82) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.54×** | +3.2 | 0.086 | 12/26 (HOP62, SW 900, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +3.2 | 0.092 | 5/23 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Isocorydine (drug)]] 0.5 µM |  | 1.51× | +3.1 | 0.10 | 4/19 (SW480, RKO, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.53× | +3.0 | 0.10 | 6/24 (CFPAC-1, NCI-H1573, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.50× | +3.0 | 0.10 | 9/25 (HOP62, A-172, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14292.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (J82 0.0837×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Glasdegib (drug)]] 5 µM | ⚠ unreliable plate only | 0.645× | -3.2 | 0.74 | 10/25 (NCI-H460, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14292. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 4.77 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0837× (z -9.1) |
| [[A-172 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.308 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.235 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.213 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.196 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.304 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.277 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.271 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.312 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.161 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.219 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.938 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.233 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.196 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14292), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP9]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[NIFK]] | +0.67 | +0.58 / +0.69 | both halves | 7e-06 | STRING 566 |
| [[NIP7]] | +0.67 | +0.70 / +0.72 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 879 |
| [[POLR1G]] | +0.66 | +0.57 / +0.64 | both halves | 1e-05 | STRING 400 |
| [[LBHD1]] | +0.66 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[NOP16]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[GEMIN4]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[RRP1]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 785 |
| [[POLR3K]] | +0.65 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[RRP7A]] | +0.65 | +0.64 / +0.58 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 996 |
| [[RRS1]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 | STRING 730 |
| [[PPRC1]] | +0.62 | +0.53 / +0.72 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.65 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[PRCP]] | -0.63 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[ARL6IP5]] | -0.58 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[ITM2B]] | -0.57 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[DDOST]] | -0.57 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[PREPL]] | -0.56 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[BPNT1]] | -0.55 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[TMEM59]] | -0.55 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[RNF11]] | -0.55 | -0.37 / -0.65 | both halves | 8e-05 |  |
| [[MYL6B]] | -0.55 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[CD99]] | -0.55 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[SH3BGRL]] | -0.55 | -0.42 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FADD]] | B | PWP2 activity raises FADD's level | lines that do not express PWP2 (21) vs lines expressing it (29) | 1.54× lower at baseline in the lines without PWP2 | 0.015 | ⚠ within organs, on part of the lines; also absent: KRT80, ENSG00000224621, ANO1 |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.528). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.6, -39.1); signed map (-2.5, -45.9). **Vector** length 28.3, 3.63% of its response variance represented; |z| ≥ 3 in 484 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.52 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.3 | +3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +1.2 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | +2.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +1.0 | +3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.0 | +3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.9 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +0.7 | +1.9 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.7 | +1.3 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.1 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -3.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -2.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -2.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -0.8 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.8 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | PWP2 small subunit processome component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:44,107,373-44,131,181 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EHOC-17, UTP1; previously PWP2H |
| Gene groups (HGNC) | WD repeat domain containing; UTPb subcomplex |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15269](https://www.uniprot.org/uniprotkb/Q15269) (Periodic tryptophan protein 2 homolog):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome.

**Summary**, from NCBI Gene [5822](https://www.ncbi.nlm.nih.gov/gene/5822):

> Enables RNA binding activity. Involved in ribosomal small subunit biogenesis. Located in nucleolus. Part of small-subunit processome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9711](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9711) · Entrez [5822](https://www.ncbi.nlm.nih.gov/gene/5822) · UniProt [Q15269](https://www.uniprot.org/uniprotkb/Q15269) · Ensembl [ENSG00000241945](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241945)

## Data

Gene col 14292: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14292); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14292, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14292]; `tensor/DDL_lfc|DDL_z.npy` [14292]; `embed/gene_vectors.npy` [14292]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14292 or target_col == 14292). Every well: [[PWP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PWP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
