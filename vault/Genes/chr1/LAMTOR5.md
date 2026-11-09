---
symbol: "LAMTOR5"
type: "gene"
col: 5529
ensembl_id: "ENSG00000134248"
name: "late endosomal/lysosomal adaptor, MAPK and MTOR activator 5"
location: "1p13.3"
module: 24
arm: "+"
pooled_cpm: 56.87
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# LAMTOR5

*late endosomal/lysosomal adaptor, MAPK and MTOR activator 5* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.69× (z +3.7, q 0.093, up in 37 of 47 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~56% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.672× (z -3.9, q 0.052, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 0.381×, C-33 A 0.289×); [[Citalopram (hydrobromide) (drug)]] 0.05 µM in 1 line (NCI-H596 0.639×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5MJ]] (+0.89, fdr 7e-06), [[RPL36AL]] (+0.87, fdr 7e-06, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[ATP5MK]] (+0.86, fdr 7e-06), [[COMMD6]] (+0.84, fdr 7e-06); moves opposite to [[MAPRE1]] (-0.74, fdr 1e-05), [[DARS2]] (-0.73, fdr 7e-06), [[EIF4G2]] (-0.73, fdr 7e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PDP2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5529.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~56% of this change | **1.69×** | +3.7 | 0.093 | 37/47 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.66×** | +3.6 | 0.093 | 37/48 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.60× | +3.2 | 0.25 | 31/47 (NCI-H1573, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5529.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 0.381×, C-33 A 0.289×); [[Citalopram (hydrobromide) (drug)]] 0.05 µM in 1 line (NCI-H596 0.639×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.672×** | -3.9 | 0.052 | 32/48 (NCI-H2347, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | 0.402× | -3.4 | 0.22 | 35/48 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 0.416× | -3.2 | 0.23 | 40/47 (LS 180, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5529. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 43.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 76.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -9.8) |
| [[NCI-H596 (line)]] | alt | 55.9 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 0.639× (z -10.6) |
| [[A-172 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 82.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 51.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 64.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 70.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 42.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5529), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MJ]] | +0.89 | +0.80 / +0.91 | both halves | 7e-06 |  |
| [[RPL36AL]] ⚠ | +0.87 | +0.75 / +0.88 | both halves | 7e-06 | pathway: Cellular response to starvation; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MK]] | +0.86 | +0.75 / +0.87 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.84 | +0.71 / +0.87 | both halves | 7e-06 |  |
| [[COX6B1]] | +0.82 | +0.69 / +0.85 | both halves | 7e-06 | pathway: TP53 Regulates Metabolic Genes |
| [[SMIM26]] ⚠ | +0.82 | +0.58 / +0.87 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM258]] | +0.81 | +0.74 / +0.87 | both halves | 7e-06 |  |
| [[CHCHD1]] | +0.81 | +0.59 / +0.87 | both halves | 7e-06 |  |
| [[RPL18]] ⚠ | +0.80 | +0.66 / +0.79 | both halves | 7e-06 | pathway: Cellular response to starvation; ⚠ in the vector space only through flagged drug-doses |
| [[TOMM7]] | +0.80 | +0.69 / +0.80 | both halves | 7e-06 | pathway: Autophagy |
| [[ROMO1]] | +0.80 | +0.64 / +0.84 | both halves | 7e-06 |  |
| [[RPL36]] | +0.80 | +0.73 / +0.79 | both halves | 7e-06 | pathway: Cellular response to starvation |
| [[SEC61G]] | +0.80 | +0.76 / +0.81 | both halves | 7e-06 |  |
| [[CAMLG]] | +0.80 | +0.63 / +0.81 | both halves | 7e-06 |  |
| [[ATP5ME]] | +0.79 | +0.61 / +0.81 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE1]] | -0.74 | -0.53 / -0.80 | both halves | 1e-05 |  |
| [[DARS2]] | -0.73 | -0.66 / -0.67 | both halves | 7e-06 |  |
| [[EIF4G2]] | -0.73 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[SF3B4]] | -0.72 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[PSME3]] | -0.72 | -0.63 / -0.72 | both halves | 7e-06 |  |
| [[FGD5-AS1]] | -0.71 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[CAPRIN1]] | -0.70 | -0.47 / -0.76 | both halves | 2e-05 |  |
| [[U2AF2]] | -0.70 | -0.40 / -0.70 | both halves | 5e-05 |  |
| [[TUG1]] | -0.69 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[NRAS]] | -0.69 | -0.49 / -0.65 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDP2]] | C | PDP2's natural level weakens LAMTOR5's drug response | PDP2's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.00; direction not clear | 0.071 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.868). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-43.5, -20.9); signed map (-32.2, 8.8). **Vector** length 88.6, 38.1% of its response variance represented; |z| ≥ 3 in 343 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.57 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | -0.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +2.3 | +3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | -0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.7 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +1.1 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.6 | +1.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.1 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.9 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.2 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.0 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | late endosomal/lysosomal adaptor, MAPK and MTOR activator 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:110,401,249-110,407,942 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XIP, MGC71071; previously HBXIP |
| Gene groups (HGNC) | Ragulator complex |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY |
| Reactome | 15 pathways, smallest: mTORC1-mediated signalling; Energy dependent regulation of mTOR by LKB1-AMPK; MTOR signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [O43504](https://www.uniprot.org/uniprotkb/O43504) (Ragulator complex protein LAMTOR5):

> As part of the Ragulator complex it is involved in amino acid sensing and activation of mTORC1, a signaling complex promoting cell growth in response to growth factors, energy levels, and amino acids. Activated by amino acids through a mechanism involving the lysosomal V-ATPase, the Ragulator plays a dual role for the small GTPases Rag (RagA/RRAGA, RagB/RRAGB, RagC/RRAGC and/or RagD/RRAGD): it (1) acts as a guanine nucleotide exchange factor (GEF), activating the small GTPases Rag and (2) …

**Summary**, from NCBI Gene [10542](https://www.ncbi.nlm.nih.gov/gene/10542):

> This gene encodes a protein that specifically complexes with the C-terminus of hepatitis B virus X protein (HBx). The function of this protein is to negatively regulate HBx activity and thus to alter the replication life cycle of the virus. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17955](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17955) · Entrez [10542](https://www.ncbi.nlm.nih.gov/gene/10542) · UniProt [O43504](https://www.uniprot.org/uniprotkb/O43504) · Ensembl [ENSG00000134248](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134248)

## Data

Gene col 5529: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5529); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5529, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5529]; `tensor/DDL_lfc|DDL_z.npy` [5529]; `embed/gene_vectors.npy` [5529]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5529 or target_col == 5529). Every well: [[LAMTOR5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMTOR5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
