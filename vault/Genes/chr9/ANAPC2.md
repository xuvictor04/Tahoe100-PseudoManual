---
symbol: "ANAPC2"
type: "gene"
col: 10701
ensembl_id: "ENSG00000176248"
name: "anaphase promoting complex subunit 2"
location: "9q34.3"
module: 153
arm: "+"
pooled_cpm: 7.39
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# ANAPC2

*anaphase promoting complex subunit 2* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.28× (z +7.9, q 2e-12, up in 40 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (HS-578T 0.0739×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0827×); [[Tucidinostat (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0749×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED16]] (+0.75, fdr 7e-06), [[NOP9]] (+0.74, fdr 7e-06), [[CACTIN]] (+0.73, fdr 7e-06).
> It is in [[Module 153]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10701.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.28×** | +7.9 | 2e-12 | 40/47 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +5.8 | 2e-06 | 32/46 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.098 | 11/47 (RKO, C-33 A, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.46×** | +3.4 | 0.098 | 14/46 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.42× | +3.1 | 0.15 | 12/43 (SNU-423, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.26× | +3.1 | 0.15 | 13/44 (SK-MEL-2, Hs 766T, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.39× | +3.1 | 0.15 | 7/47 (H4, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10701.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (HS-578T 0.0739×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0827×); [[Tucidinostat (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0749×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.767× | -3.6 | 0.17 | 14/47 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Voriconazole (drug)]] 0.5 µM |  | 0.731× | -3.0 | 0.57 | 10/46 (NCI-H2347, NCI-H23, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10701. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 6.75 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -8.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 5.73 | 0 | 1 | — | [[Ciclopirox (drug)]] 0.05 µM 0.0801× (z -8.7) |
| [[HS-578T (line)]] | alt | 4.82 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0739× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 4.33 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0827× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 3.05 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.05 µM 0.0728× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 6.66 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.05 µM 0.0714× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 5.97 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.0749× (z -9.0) |
| [[A-172 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10701), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED16]] | +0.75 | +0.72 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[NOP9]] | +0.74 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[CACTIN]] | +0.73 | +0.67 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[BAP1]] | +0.71 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[WASH8P]] ⚠ | +0.70 | +0.62 / +0.74 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[PCNX3]] | +0.69 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[TUBGCP6]] | +0.68 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[RANBP3]] | +0.68 | +0.66 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[SBF1]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[POLR2J3]] | +0.67 | +0.51 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[WASH9P]] | +0.66 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[WDR6]] | +0.65 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[RAB11B]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ANAPC2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.742). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.7, -25.2); signed map (-13.2, -31.6). **Vector** length 58.9, 8.28% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | +1.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.6 | +0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.7 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +1.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.2 | +7.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +0.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.5 | +1.8 |
|  | [[Arbutin (drug)]] 0.5 µM |  | +1.5 | +2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.4 | -2.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -0.9 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.5 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +0.1 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.0 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.4 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | anaphase promoting complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,174,784-137,188,560 (-) |
| Ensembl biotype | protein_coding |
| Also known as | APC2, KIAA1406 |
| Gene groups (HGNC) | Anaphase promoting complex |
| Reactome | 42 pathways, smallest: Aberrant regulation of mitotic exit in cancer due to RB1 defects; Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase; Phosphorylation of the APC/C |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJX6](https://www.uniprot.org/uniprotkb/Q9UJX6) (Anaphase-promoting complex subunit 2):

> Component of the anaphase promoting complex/cyclosome (APC/C), a cell cycle-regulated E3 ubiquitin ligase that controls progression through the cell cycle. Together with the RING-H2 protein ANAPC11, forms the catalytic component of the E3 ubiquitin ligase complex. APC/C acts by mediating ubiquitination and subsequent degradation of target proteins: it mainly mediates the formation of 'Lys-11'-linked polyubiquitin chains and, to a lower extent, the formation of 'Lys-48'- and 'Lys-63'-linked …

**Summary**, from NCBI Gene [29882](https://www.ncbi.nlm.nih.gov/gene/29882):

> A large protein complex, termed the anaphase-promoting complex (APC), or the cyclosome, promotes metaphase-anaphase transition by ubiquitinating its specific substrates such as mitotic cyclins and anaphase inhibitor, which are subsequently degraded by the 26S proteasome. Biochemical studies have shown that the vertebrate APC contains eight subunits. The composition of the APC is highly conserved in organisms from yeast to humans. The product of this gene is a component of the complex and shares …

**Accessions** — [HGNC:19989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19989) · Entrez [29882](https://www.ncbi.nlm.nih.gov/gene/29882) · UniProt [Q9UJX6](https://www.uniprot.org/uniprotkb/Q9UJX6) · Ensembl [ENSG00000176248](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176248)

## Data

Gene col 10701: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10701); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10701, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10701]; `tensor/DDL_lfc|DDL_z.npy` [10701]; `embed/gene_vectors.npy` [10701]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10701 or target_col == 10701). Every well: [[ANAPC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANAPC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
