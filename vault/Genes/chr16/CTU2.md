---
symbol: "CTU2"
type: "gene"
col: 10470
ensembl_id: "ENSG00000174177"
name: "cytosolic thiouridylase subunit 2"
location: "16q24.3"
module: 2
arm: "+"
pooled_cpm: 3.45
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CTU2

*cytosolic thiouridylase subunit 2* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.89× (z +9.2, q 2e-17, up in 39 of 46 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Peretinoin (drug)]] 0.5 µM: 1.47× (z +3.3, q 0.033, up in 3 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.630× (z -3.8, q 0.043, down in 15 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATAD3A]] (+0.73, fdr 7e-06), [[NOC4L]] (+0.73, fdr 7e-06), [[E2F4]] (+0.73, fdr 7e-06); moves opposite to [[NQO1-DT]] (-0.56, fdr 3e-05), [[GIPC2]] (-0.56, fdr 3e-05), [[SNX16]] (-0.56, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HMGN5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10470.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.89×** | +9.2 | 2e-17 | 39/46 (SW480, NCI-H1792, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.49×** | +7.9 | 8e-13 | 30/43 (SW480, RKO, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.24×** | +6.7 | 4e-09 | 13/18 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.90×** | +5.6 | 3e-06 | 19/44 (SW480, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.89×** | +5.3 | 1e-05 | 0/6 | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.79×** | +5.0 | 5e-05 | 16/46 (NCI-H2030, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.74×** | +4.8 | 1e-04 | 12/32 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.68×** | +4.5 | 5e-04 | 16/44 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.66×** | +4.4 | 6e-04 | 4/9 (NCI-H2030, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.38×** | +3.9 | 0.004 | 10/35 (NCI-H1573, LS 180, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.53×** | +3.7 | 0.010 | 11/44 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **1.52×** | +3.6 | 0.014 | 4/17 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.56×** | +3.6 | 0.014 | 1/7 (HOP62) | all doses, stronger at high dose | composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.033 | 3/45 (PANC-1, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.046 | 11/35 (Hs 766T, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | **1.43×** | +3.1 | 0.060 | 2/44 (NCI-H1573, AsPC-1) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.95×** | +3.0 | 0.072 | 2/22 (PANC-1, A498) | top dose only | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.41×** | +3.0 | 0.083 | 7/37 (MIA PaCa-2, NCI-H2030, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10470.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.630×** | -3.8 | 0.043 | 15/40 (Hs 766T, NCI-H2030, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.733×** | -3.8 | 0.043 | 15/44 (A498, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10470. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10470), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATAD3A]] | +0.73 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[NOC4L]] | +0.73 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[E2F4]] | +0.73 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ATAD3B]] | +0.72 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[ZNF598]] | +0.69 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[DPH7]] | +0.68 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ZMYND19]] | +0.67 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[CPSF1]] | +0.67 | +0.64 / +0.58 | both halves | 7e-06 | pathway: tRNA processing |
| [[TREX2]] | +0.66 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[POLRMT]] | +0.66 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[SRM]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[TXNL4A]] | +0.64 | +0.62 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NQO1-DT]] | -0.56 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[GIPC2]] | -0.56 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[SNX16]] | -0.56 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[MKLN1-AS]] | -0.55 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[STX17-DT]] | -0.55 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[SOD1]] | -0.53 | -0.45 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGN5]] | B | HMGN5 activity lowers CTU2's level | lines that do not express HMGN5 (7) vs lines expressing it (43) | 1.29× higher at baseline in the lines without HMGN5 | 0.082 | ⚠ within organs, on part of the lines; also absent: SH3BGRL; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.534). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-4.9, -27.1); signed map (-46.5, -16.8). **Vector** length 50.5, 6.50% of its response variance represented; |z| ≥ 3 in 909 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.6 | +9.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.5 | +7.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.2 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.2 | +6.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | +2.1 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.3 | +3.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.2 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +1.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.2 | +3.0 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -0.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | +0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.4 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | cytosolic thiouridylase subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:88,706,483-88,715,396 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NCS2; previously C16orf84 |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2VPK5](https://www.uniprot.org/uniprotkb/Q2VPK5) (Cytoplasmic tRNA 2-thiolation protein 2):

> Plays a central role in 2-thiolation of mcm(5)S(2)U at tRNA wobble positions of tRNA(Lys), tRNA(Glu) and tRNA(Gln). May act by forming a heterodimer with CTU1/ATPBD3 that ligates sulfur from thiocarboxylated URM1 onto the uridine of tRNAs at wobble position.

**Summary**, from NCBI Gene [348180](https://www.ncbi.nlm.nih.gov/gene/348180):

> This gene encodes a protein which is involved in the post-transcriptional modification of transfer RNAs (tRNAs). The encoded protein plays a role in thiolation of uridine residue present at the wobble position in a subset of tRNAs, resulting in enhanced codon reading accuracy. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:28005](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28005) · Entrez [348180](https://www.ncbi.nlm.nih.gov/gene/348180) · UniProt [Q2VPK5](https://www.uniprot.org/uniprotkb/Q2VPK5) · Ensembl [ENSG00000174177](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174177)

## Data

Gene col 10470: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10470); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10470, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10470]; `tensor/DDL_lfc|DDL_z.npy` [10470]; `embed/gene_vectors.npy` [10470]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10470 or target_col == 10470). Every well: [[CTU2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTU2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
