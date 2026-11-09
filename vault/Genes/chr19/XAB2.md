---
symbol: "XAB2"
type: "gene"
col: 1166
ensembl_id: "ENSG00000076924"
name: "XPA binding protein 2"
location: "19p13.2"
module: 107
arm: "+"
pooled_cpm: 14.58
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/107"]
generated_by: "tahoemap"
---

# XAB2

*XPA binding protein 2* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.74× (z +11.0, q 2e-25, up in 40 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.750× (z -5.8, q 4e-06, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF3C5]] (+0.67, fdr 7e-06), [[GUCD1]] (+0.65, fdr 1e-05), [[OGFOD2]] (+0.64, fdr 1e-05); moves opposite to [[AP1S3]] (-0.54, fdr 3e-05).
> It is in [[Module 107]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[CCNK]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1166.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +11.0 | 2e-25 | 40/46 (Hs 766T, A549, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +6.4 | 4e-08 | 27/47 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +5.8 | 2e-06 | 22/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +4.9 | 1e-04 | 20/48 (PANC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.40×** | +4.9 | 1e-04 | 17/48 (RKO, SW48, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +4.9 | 1e-04 | 19/45 (LS 180, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.34×** | +4.3 | 0.002 | 20/48 (RKO, SW48, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +4.1 | 0.003 | 9/31 (NCI-H1792, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.69×** | +4.0 | 0.004 | 19/48 (SW480, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.075 | 10/46 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1166.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.750×** | -5.8 | 4e-06 | 27/48 (SK-MEL-2, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.734×** | -4.3 | 0.004 | 19/47 (PANC-1, SNU-423, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.747×** | -4.3 | 0.004 | 21/47 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.941× | -3.1 | 0.21 | 4/48 (BT-474, NCI-H661, …) | inconsistent across doses |  |
| [[ERK5-IN-2 (drug)]] 0.05 µM |  | 0.800× | -3.1 | 0.21 | 14/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Neratinib (drug)]] 0.05 µM |  | 0.811× | -3.1 | 0.21 | 11/47 (BT-474, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1166. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 18.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.272× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[BT-474 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0850× (z -12.1) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 11.5 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0741× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0952× (z -10.6) |
| [[LoVo (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 15.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1166), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF3C5]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[GUCD1]] | +0.65 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[OGFOD2]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[BCKDHA]] | +0.63 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[TRMT2A]] | +0.62 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[ESS2]] | +0.61 | +0.73 / +0.60 | both halves | 7e-06 | same gene group; STRING 576 |
| [[ZNF581]] | +0.61 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[ANAPC2]] | +0.61 | +0.67 / +0.51 | both halves | 1e-05 | STRING 812 |
| [[PTPN23]] | +0.60 | +0.70 / +0.48 | both halves | 2e-05 |  |
| [[CCNK]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[CLK3]] | +0.60 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[SYVN1]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP1S3]] | -0.54 | -0.43 / -0.60 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCNK]] | C | XAB2's natural level weakens CCNK's drug response | XAB2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.28; direction not clear | 0.060 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 107]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.16; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.5, -15.4); signed map (-23.2, 1.0). **Vector** length 69.4, 11.8% of its response variance represented; |z| ≥ 3 in 732 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +11.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.7 | +4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.6 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.2 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +5.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.2 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +1.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +3.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -5.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.5 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | -1.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.5 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | +0.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | XPA binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:7,619,525-7,629,545 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HCNP, HCRN, SYF1, NTC90 |
| Gene groups (HGNC) | Nucleotide excision repair; Spliceosomal B complex; Spliceosomal Bact complex; Spliceosomal C complex; Spliceosomal P complex |
| Reactome | 13 pathways, smallest: Formation of TC-NER Pre-Incision Complex; Gap-filling DNA repair synthesis and ligation in TC-NER; Dual incision in TC-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCS7](https://www.uniprot.org/uniprotkb/Q9HCS7) (Pre-mRNA-splicing factor SYF1):

> Involved in pre-mRNA splicing as component of the spliceosome. Involved in transcription-coupled repair (TCR), transcription and pre-mRNA splicing.

**Summary**, from NCBI Gene [56949](https://www.ncbi.nlm.nih.gov/gene/56949):

> Involved in DNA-templated transcription; mRNA splicing, via spliceosome; and transcription-coupled nucleotide-excision repair. Located in nucleoplasm. Part of U2-type catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14089](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14089) · Entrez [56949](https://www.ncbi.nlm.nih.gov/gene/56949) · UniProt [Q9HCS7](https://www.uniprot.org/uniprotkb/Q9HCS7) · Ensembl [ENSG00000076924](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076924)

## Data

Gene col 1166: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1166); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1166, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1166]; `tensor/DDL_lfc|DDL_z.npy` [1166]; `embed/gene_vectors.npy` [1166]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1166 or target_col == 1166). Every well: [[XAB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XAB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
