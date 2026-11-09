---
symbol: "EME2"
type: "gene"
col: 12460
ensembl_id: "ENSG00000197774"
name: "essential meiotic structure-specific endonuclease subunit 2"
location: "16p13.3"
module: 157
arm: "+"
pooled_cpm: 3.42
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 4
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# EME2

*essential meiotic structure-specific endonuclease subunit 2* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.90× (z +9.0, q 2e-16, up in 4 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.37× (z +3.8, q 0.018, up in 9 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.521× (z -5.5, q 2e-05, down in 18 of 42 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.549× (z -5.3, q 3e-05, down in 18 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Valdecoxib (drug)]] 0.5 µM in 1 line (HT-29 0.0712×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW480 0.116×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (SW480 0.0989×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPEPL1]] (+0.69, fdr 7e-06), [[LENG8]] (+0.67, fdr 9e-06), [[MTA2]] (+0.67, fdr 1e-05); moves opposite to [[INIP]] (-0.60, fdr 1e-05), [[GPN3]] (-0.58, fdr 5e-05), [[GPATCH11]] (-0.57, fdr 4e-05).
> It is in [[Module 157]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12460.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +9.0 | 2e-16 | 4/5 (NCI-H2030, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +8.4 | 2e-14 | 13/18 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.75×** | +8.2 | 4e-14 | 5/6 (NCI-H2030, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.018 | 9/36 (A498, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.69×** | +3.3 | 0.096 | 4/20 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.096 | 6/44 (SW1417, LS 180, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12460.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Valdecoxib (drug)]] 0.5 µM in 1 line (HT-29 0.0712×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SW480 0.116×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (SW480 0.0989×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.521×** | -5.5 | 2e-05 | 18/42 (PANC-1, LOX-IMVI, …) | rises with dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.549×** | -5.3 | 3e-05 | 18/44 (SW 900, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.614×** | -4.3 | 0.003 | 13/44 (A-427, HCT15, …) | all doses, flat | cell-cycle shift (explains ~15% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.732×** | -3.9 | 0.013 | 20/36 (PANC-1, C32, …) | rises with dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12460. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 2.75 | 0 | 2 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.116× (z -8.9) |
| [[BT-474 (line)]] | alt | 5.00 | 0 | 1 | — | [[Loperamide (hydrochloride) (drug)]] 0.5 µM 0.0628× (z -8.5) |
| [[HT-29 (line)]] | alt | 7.51 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0712× (z -10.3) |
| [[A-172 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12460), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPEPL1]] | +0.69 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[LENG8]] | +0.67 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[MTA2]] | +0.67 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[PCED1A]] | +0.67 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[AP1G2-AS1]] | +0.67 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[TMEM147-AS1]] | +0.66 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[CCNL2]] | +0.65 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[IDUA]] | +0.65 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[OPLAH]] ⚠ | +0.64 | +0.63 / +0.65 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CERS2]] | +0.64 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[STRN4]] | +0.64 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[KAT2A]] | +0.63 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[INPPL1]] | +0.63 | +0.55 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INIP]] | -0.60 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[GPN3]] | -0.58 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[GPATCH11]] | -0.57 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[ACTR6]] | -0.55 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[SCAMP1]] | -0.52 | -0.54 / -0.26 | both halves | 4e-04 |  |
| [[PIBF1]] | -0.52 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[LGALS1]] | -0.51 | -0.36 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises EME2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.803). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.7, -24.4); signed map (31.9, -20.7). **Vector** length 50.5, 6.05% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +8.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +8.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +3.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.4 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -1.9 | -5.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -2.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.6 | -5.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.5 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | essential meiotic structure-specific endonuclease subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,772,810-1,781,708 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00151, SLX2B |
| Reactome | 8 pathways, smallest: Resolution of D-loop Structures through Holliday Junction Intermediates; Resolution of D-Loop Structures; Fanconi Anemia Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [A4GXA9](https://www.uniprot.org/uniprotkb/A4GXA9) (Structure-specific endonuclease subunit EME2):

> Non-catalytic subunit of the structure-specific, heterodimeric DNA endonuclease MUS81-EME2 which is involved in the maintenance of genome stability. In the complex, EME2 is required for DNA cleavage, participating in DNA recognition and bending. MUS81-EME2 cleaves 3'-flaps and nicked Holliday junctions, and exhibit limited endonuclease activity with 5' flaps and nicked double-stranded DNAs. MUS81-EME2 which is active during the replication of DNA is more specifically involved in replication …

**Summary**, from NCBI Gene [197342](https://www.ncbi.nlm.nih.gov/gene/197342):

> EME2 forms a heterodimer with MUS81 (MIM 606591) that functions as an XPF (MIM 278760)-type flap/fork endonuclease in DNA repair (Ciccia et al., 2007 [PubMed 17289582]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:27289](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27289) · Entrez [197342](https://www.ncbi.nlm.nih.gov/gene/197342) · UniProt [A4GXA9](https://www.uniprot.org/uniprotkb/A4GXA9) · Ensembl [ENSG00000197774](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197774)

## Data

Gene col 12460: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12460); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12460, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12460]; `tensor/DDL_lfc|DDL_z.npy` [12460]; `embed/gene_vectors.npy` [12460]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12460 or target_col == 12460). Every well: [[EME2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EME2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
